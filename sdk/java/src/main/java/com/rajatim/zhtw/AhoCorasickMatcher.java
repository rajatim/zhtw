package com.rajatim.zhtw;

import org.ahocorasick.trie.Emit;
import org.ahocorasick.trie.Trie;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

final class AhoCorasickMatcher {

    private final Map<String, String> terms;
    private final Trie trie;

    AhoCorasickMatcher(Map<String, String> terms) {
        this.terms = Collections.unmodifiableMap(new HashMap<>(terms));
        this.trie = buildTrie();
    }

    private Trie buildTrie() {
        if (terms.isEmpty()) {
            return null;
        }
        Trie.TrieBuilder builder = Trie.builder();
        for (String key : terms.keySet()) {
            builder.addKeyword(key);
        }
        return builder.build();
    }

    List<Match> findMatches(String text) {
        if (trie == null || text == null || text.isEmpty()) {
            return Collections.emptyList();
        }

        Collection<Emit> emits = trie.parseText(text);
        if (emits.isEmpty()) {
            return Collections.emptyList();
        }

        // Convert to Match objects (Emit.getEnd() is INCLUSIVE, we need EXCLUSIVE)
        List<Match> allMatches = new ArrayList<>();
        for (Emit emit : emits) {
            String source = emit.getKeyword();
            String target = terms.get(source);
            allMatches.add(new Match(emit.getStart(), emit.getEnd() + 1, source, target));
        }

        // Sort by start, then longer first
        allMatches.sort((a, b) -> {
            int cmp = Integer.compare(a.getStart(), b.getStart());
            if (cmp != 0) return cmp;
            return Integer.compare(b.getEnd() - b.getStart(), a.getEnd() - a.getStart());
        });

        // Build protected ranges from identity mappings
        Set<Integer> protectedPositions = buildProtectedRanges(allMatches);

        // Greedy left-to-right selection
        List<Match> result = new ArrayList<>();
        int lastEnd = -1;
        for (Match match : allMatches) {
            if (match.getStart() >= lastEnd) {
                boolean isIdentity = match.getSource().equals(match.getTarget());
                if (!isIdentity) {
                    boolean overlapsProtected = false;
                    for (int i = match.getStart(); i < match.getEnd(); i++) {
                        if (protectedPositions.contains(i)) {
                            overlapsProtected = true;
                            break;
                        }
                    }
                    if (overlapsProtected) {
                        continue;
                    }
                }
                lastEnd = match.getEnd();
                if (!isIdentity) {
                    result.add(match);
                }
            }
        }

        return result;
    }

    private Set<Integer> buildProtectedRanges(List<Match> allMatches) {
        List<Match> identityMatches = new ArrayList<>();
        List<int[]> nonIdentity = new ArrayList<>();

        for (Match m : allMatches) {
            if (m.getSource().equals(m.getTarget())) {
                identityMatches.add(m);
            } else {
                nonIdentity.add(new int[]{m.getStart(), m.getEnd()});
            }
        }

        Set<Integer> protectedPositions = new HashSet<>();

        if (!nonIdentity.isEmpty()) {
            nonIdentity.sort((a, b) -> Integer.compare(a[0], b[0]));

            int[] starts = new int[nonIdentity.size()];
            int[] maxEnds = new int[nonIdentity.size()];
            int maxE = 0;
            for (int i = 0; i < nonIdentity.size(); i++) {
                starts[i] = nonIdentity.get(i)[0];
                maxE = Math.max(maxE, nonIdentity.get(i)[1]);
                maxEnds[i] = maxE;
            }

            for (Match identity : identityMatches) {
                int idx = bisectRight(starts, identity.getStart()) - 1;
                boolean isContained = idx >= 0 && maxEnds[idx] >= identity.getEnd();
                if (!isContained) {
                    for (int i = identity.getStart(); i < identity.getEnd(); i++) {
                        protectedPositions.add(i);
                    }
                }
            }
        } else {
            for (Match identity : identityMatches) {
                for (int i = identity.getStart(); i < identity.getEnd(); i++) {
                    protectedPositions.add(i);
                }
            }
        }

        return protectedPositions;
    }

    private static int bisectRight(int[] arr, int value) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= value) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    String replaceAll(String text) {
        List<Match> matches = findMatches(text);
        if (matches.isEmpty()) {
            return text;
        }

        StringBuilder sb = new StringBuilder(text.length());
        int lastEnd = 0;
        for (Match m : matches) {
            sb.append(text, lastEnd, m.getStart());
            sb.append(m.getTarget());
            lastEnd = m.getEnd();
        }
        sb.append(text, lastEnd, text.length());
        return sb.toString();
    }

    /**
     * Return all UTF-16 positions covered by any raw automaton hit,
     * including identity terms (source == target). This is used to
     * prevent the char layer from converting characters that are
     * protected by identity term matches.
     */
    Set<Integer> getCoveredPositions(String text) {
        if (trie == null || text == null || text.isEmpty()) {
            return Collections.emptySet();
        }
        Set<Integer> covered = new HashSet<>();
        for (Emit emit : trie.parseText(text)) {
            // Emit.getEnd() is inclusive
            for (int i = emit.getStart(); i <= emit.getEnd(); i++) {
                covered.add(i);
            }
        }
        return covered;
    }
}
