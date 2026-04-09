package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public final class ZhtwConverter {

    private static volatile ZhtwConverter defaultInstance;

    private final AhoCorasickMatcher matcher;
    private final Map<Integer, String> charmap;    // codepoint -> replacement
    private final Set<Integer> ambiguous;           // ambiguous codepoints
    private final boolean charLayerEnabled;
    private final List<String> sources;

    private ZhtwConverter(AhoCorasickMatcher matcher,
                          Map<Integer, String> charmap,
                          Set<Integer> ambiguous,
                          boolean charLayerEnabled,
                          List<String> sources) {
        this.matcher = matcher;
        this.charmap = charmap;
        this.ambiguous = ambiguous;
        this.charLayerEnabled = charLayerEnabled;
        this.sources = Collections.unmodifiableList(new ArrayList<>(sources));
    }

    public static ZhtwConverter getDefault() {
        if (defaultInstance == null) {
            synchronized (ZhtwConverter.class) {
                if (defaultInstance == null) {
                    defaultInstance = builder().build();
                }
            }
        }
        return defaultInstance;
    }

    public static Builder builder() {
        return new Builder();
    }

    public String convert(String text) {
        if (text == null) {
            return null;
        }
        if (text.isEmpty()) {
            return text;
        }

        // Stage 1: Term-level replacement
        String result = matcher.replaceAll(text);

        // Stage 2: Char-level conversion (only when "cn" in sources)
        if (charLayerEnabled) {
            result = applyCharmap(result);
        }

        return result;
    }

    public List<Match> check(String text) {
        if (text == null || text.isEmpty()) {
            return Collections.emptyList();
        }

        List<Match> result = new ArrayList<>();

        // Term-level matches
        result.addAll(matcher.findMatches(text));

        // Char-level matches (on original text)
        if (charLayerEnabled) {
            int i = 0;
            while (i < text.length()) {
                int cp = text.codePointAt(i);
                String replacement = charmap.get(cp);
                String original = new String(Character.toChars(cp));
                if (replacement != null && !replacement.equals(original)) {
                    int charLen = Character.charCount(cp);
                    result.add(new Match(i, i + charLen, original, replacement));
                }
                i += Character.charCount(cp);
            }
        }

        return result;
    }

    public LookupResult lookup(String word) {
        if (word == null || word.isEmpty()) {
            return new LookupResult(
                    word == null ? "" : word,
                    word == null ? "" : word,
                    false,
                    Collections.emptyList()
            );
        }

        List<ConversionDetail> details = new ArrayList<>();
        Set<Integer> covered = new HashSet<>();  // covered char indices

        // 1. Term layer
        List<Match> termMatches = matcher.findMatches(word);
        for (Match m : termMatches) {
            String target = m.getTarget();
            // Apply charmap to term target (matching Python pipeline)
            if (charLayerEnabled) {
                target = applyCharmap(target);
            }
            details.add(new ConversionDetail(m.getSource(), target, "term", m.getStart()));
            for (int i = m.getStart(); i < m.getEnd(); i++) {
                covered.add(i);
            }
        }

        // 2. Char layer: scan uncovered positions
        if (charLayerEnabled) {
            int i = 0;
            while (i < word.length()) {
                int cp = word.codePointAt(i);
                int charLen = Character.charCount(cp);
                if (!covered.contains(i)) {
                    String replacement = charmap.get(cp);
                    String original = new String(Character.toChars(cp));
                    if (replacement != null && !replacement.equals(original)) {
                        details.add(new ConversionDetail(original, replacement, "char", i));
                    }
                }
                i += charLen;
            }
        }

        // Sort by position
        details.sort((a, b) -> Integer.compare(a.getPosition(), b.getPosition()));

        // Build output
        String output = buildOutput(word, details);
        boolean changed = !output.equals(word);

        return new LookupResult(word, output, changed, details);
    }

    private String buildOutput(String text, List<ConversionDetail> details) {
        if (details.isEmpty()) {
            return text;
        }

        StringBuilder sb = new StringBuilder();
        int lastEnd = 0;

        for (ConversionDetail d : details) {
            sb.append(text, lastEnd, d.getPosition());
            sb.append(d.getTarget());
            lastEnd = d.getPosition() + d.getSource().length();
        }

        sb.append(text, lastEnd, text.length());
        return sb.toString();
    }

    /** Apply codepoint-based charmap to text. Handles supplementary plane characters. */
    private String applyCharmap(String text) {
        StringBuilder sb = new StringBuilder(text.length());
        boolean changed = false;
        int i = 0;
        while (i < text.length()) {
            int cp = text.codePointAt(i);
            String replacement = charmap.get(cp);
            if (replacement != null) {
                sb.append(replacement);
                changed = true;
            } else {
                sb.appendCodePoint(cp);
            }
            i += Character.charCount(cp);
        }
        return changed ? sb.toString() : text;
    }

    public static final class Builder {

        private List<String> sources = Arrays.asList("cn", "hk");
        private Map<String, String> customDict = Collections.emptyMap();

        private Builder() {}

        public Builder sources(List<String> sources) {
            this.sources = new ArrayList<>(sources);
            return this;
        }

        public Builder customDict(Map<String, String> customDict) {
            this.customDict = new HashMap<>(customDict);
            return this;
        }

        public ZhtwConverter build() {
            ZhtwData data = ZhtwData.fromClasspath();

            Map<String, String> allTerms = new HashMap<>();
            for (String source : sources) {
                allTerms.putAll(data.getTerms(source));
            }
            allTerms.putAll(customDict);

            AhoCorasickMatcher matcher = new AhoCorasickMatcher(allTerms);
            boolean charLayerEnabled = sources.contains("cn");

            return new ZhtwConverter(
                    matcher,
                    data.getCharmap(),
                    data.getAmbiguous(),
                    charLayerEnabled,
                    sources
            );
        }
    }
}
