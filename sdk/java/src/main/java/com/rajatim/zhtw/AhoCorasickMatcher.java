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

    static class ScanResult {
        final List<Match> matches;
        final Set<Integer> covered;

        ScanResult(List<Match> matches, Set<Integer> covered) {
            this.matches = matches;
            this.covered = covered;
        }
    }

    static final class MatchDecision {
        final Match match;
        final String outcome;
        final String reasonCode;

        MatchDecision(Match match, String outcome, String reasonCode) {
            this.match = match;
            this.outcome = outcome;
            this.reasonCode = reasonCode;
        }
    }

    static final class DetailedScanResult extends ScanResult {
        final List<MatchDecision> decisions;

        DetailedScanResult(List<Match> matches,
                           Set<Integer> covered,
                           List<MatchDecision> decisions) {
            super(matches, covered);
            this.decisions = decisions;
        }
    }

    private static final class Protection {
        final Set<Integer> positions;
        final Set<Match> effectiveIdentity;

        Protection(Set<Integer> positions, Set<Match> effectiveIdentity) {
            this.positions = positions;
            this.effectiveIdentity = effectiveIdentity;
        }
    }

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

    ScanResult scan(String text) {
        return scanInternal(text, false);
    }

    DetailedScanResult scanDetailed(String text) {
        ScanResult result = scanInternal(text, true);
        return (DetailedScanResult) result;
    }

    private ScanResult scanInternal(String text, boolean detailed) {
        if (trie == null || text == null || text.isEmpty()) {
            return detailed
                    ? new DetailedScanResult(
                            Collections.emptyList(), Collections.emptySet(), Collections.emptyList())
                    : new ScanResult(Collections.emptyList(), Collections.emptySet());
        }

        Collection<Emit> emits = trie.parseText(text);
        if (emits.isEmpty()) {
            return detailed
                    ? new DetailedScanResult(
                            Collections.emptyList(), Collections.emptySet(), Collections.emptyList())
                    : new ScanResult(Collections.emptyList(), Collections.emptySet());
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
        Protection protection = buildProtectedRanges(allMatches);
        Set<Integer> protectedPositions = protection.positions;
        Set<Integer> covered = new HashSet<>(protectedPositions);

        // Greedy left-to-right selection
        List<Match> result = new ArrayList<>();
        List<MatchDecision> decisions = detailed ? new ArrayList<>() : Collections.emptyList();
        int lastEnd = -1;
        for (Match match : allMatches) {
            boolean isIdentity = match.getSource().equals(match.getTarget());
            if (match.getStart() < lastEnd) {
                if (detailed) {
                    boolean effective = protection.effectiveIdentity.contains(match);
                    decisions.add(new MatchDecision(
                            match,
                            isIdentity && effective ? "protected" : "skipped",
                            isIdentity
                                    ? (effective ? "identity_guard" : "identity_contained")
                                    : "overlap_loser"));
                }
                continue;
            }
            if (!isIdentity) {
                boolean overlapsProtected = false;
                for (int i = match.getStart(); i < match.getEnd(); i++) {
                    if (protectedPositions.contains(i)) {
                        overlapsProtected = true;
                        break;
                    }
                }
                if (overlapsProtected) {
                    if (detailed) {
                        decisions.add(new MatchDecision(
                                match, "skipped", "protected_by_identity"));
                    }
                    continue;
                }
            }
            lastEnd = match.getEnd();
            if (!isIdentity) {
                result.add(match);
                for (int i = match.getStart(); i < match.getEnd(); i++) {
                    covered.add(i);
                }
                if (detailed) {
                    decisions.add(new MatchDecision(match, "applied", "term_selected"));
                }
            } else if (detailed) {
                decisions.add(new MatchDecision(
                        match,
                        "protected",
                        protection.effectiveIdentity.contains(match)
                                ? "identity_guard" : "identity_contained"));
            }
        }

        return detailed
                ? new DetailedScanResult(result, covered, decisions)
                : new ScanResult(result, covered);
    }

    List<Match> findMatches(String text) {
        return scan(text).matches;
    }

    private Protection buildProtectedRanges(List<Match> allMatches) {
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
        Set<Match> effectiveIdentity = new HashSet<>();

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
                    effectiveIdentity.add(identity);
                }
            }
        } else {
            for (Match identity : identityMatches) {
                for (int i = identity.getStart(); i < identity.getEnd(); i++) {
                    protectedPositions.add(i);
                }
                effectiveIdentity.add(identity);
            }
        }

        return new Protection(protectedPositions, effectiveIdentity);
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
     * Return UTF-16 positions covered by selected terms or effective identity
     * guards. Losing overlap candidates do not block the character layer.
     */
    Set<Integer> getCoveredPositions(String text) {
        return scan(text).covered;
    }
}
