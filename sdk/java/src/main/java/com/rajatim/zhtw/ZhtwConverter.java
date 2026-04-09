package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Simplified Chinese to Traditional Chinese (Taiwan) converter.
 *
 * <p>Positions in {@link Match} and {@link ConversionDetail} use Unicode codepoint
 * indices (not Java UTF-16 code unit indices), consistent with Python.
 */
public final class ZhtwConverter {

    private static volatile ZhtwConverter defaultInstance;

    private final AhoCorasickMatcher matcher;
    private final Map<Integer, String> charmap;    // codepoint -> replacement
    private final boolean charLayerEnabled;
    private final List<String> sources;

    private ZhtwConverter(AhoCorasickMatcher matcher,
                          Map<Integer, String> charmap,
                          boolean charLayerEnabled,
                          List<String> sources) {
        this.matcher = matcher;
        this.charmap = charmap;
        this.charLayerEnabled = charLayerEnabled;
        this.sources = Collections.unmodifiableList(new ArrayList<>(sources));
    }

    /**
     * Get the default converter instance (thread-safe singleton).
     * Uses sources ["cn", "hk"], no custom dict.
     */
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

    /** Create a new builder. */
    public static Builder builder() {
        return new Builder();
    }

    /**
     * Convert text from Simplified Chinese to Traditional Chinese (Taiwan).
     *
     * @param text input text
     * @return converted text, or null if input is null
     */
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

    /**
     * Check text for conversions without modifying it.
     * Returns all matches (term-level + char-level on original text).
     * Positions are Unicode codepoint indices, not UTF-16 code unit indices.
     *
     * @param text input text
     * @return list of matches found
     */
    public List<Match> check(String text) {
        if (text == null || text.isEmpty()) {
            return Collections.emptyList();
        }

        List<Match> result = new ArrayList<>();

        // Term-level matches (matcher returns UTF-16 indices, convert to codepoint)
        for (Match m : matcher.findMatches(text)) {
            int cpStart = Character.codePointCount(text, 0, m.getStart());
            int cpEnd = Character.codePointCount(text, 0, m.getEnd());
            result.add(new Match(cpStart, cpEnd, m.getSource(), m.getTarget()));
        }

        // Char-level matches (on original text, track codepoint index)
        if (charLayerEnabled) {
            int cpIndex = 0;
            int i = 0;
            while (i < text.length()) {
                int cp = text.codePointAt(i);
                String replacement = charmap.get(cp);
                String original = new String(Character.toChars(cp));
                if (replacement != null && !replacement.equals(original)) {
                    result.add(new Match(cpIndex, cpIndex + 1, original, replacement));
                }
                cpIndex++;
                i += Character.charCount(cp);
            }
        }

        return result;
    }

    /**
     * Look up conversion details for a single word or phrase.
     * Positions are Unicode codepoint indices, not UTF-16 code unit indices.
     *
     * @param word input word
     * @return lookup result with conversion details
     */
    public LookupResult lookup(String word) {
        if (word == null || word.isEmpty()) {
            return new LookupResult(
                    word == null ? "" : word,
                    word == null ? "" : word,
                    false,
                    Collections.emptyList()
            );
        }

        // Internal work uses UTF-16 indices (needed by buildOutput for string slicing)
        List<ConversionDetail> utf16Details = new ArrayList<>();
        Set<Integer> coveredUtf16 = new HashSet<>();

        // 1. Term layer
        List<Match> termMatches = matcher.findMatches(word);
        for (Match m : termMatches) {
            String target = m.getTarget();
            // Apply charmap to term target (matching Python pipeline)
            if (charLayerEnabled) {
                target = applyCharmap(target);
            }
            utf16Details.add(new ConversionDetail(m.getSource(), target, "term", m.getStart()));
            for (int i = m.getStart(); i < m.getEnd(); i++) {
                coveredUtf16.add(i);
            }
        }

        // 2. Char layer: scan uncovered positions
        if (charLayerEnabled) {
            int i = 0;
            while (i < word.length()) {
                int cp = word.codePointAt(i);
                int charLen = Character.charCount(cp);
                if (!coveredUtf16.contains(i)) {
                    String replacement = charmap.get(cp);
                    String original = new String(Character.toChars(cp));
                    if (replacement != null && !replacement.equals(original)) {
                        utf16Details.add(new ConversionDetail(original, replacement, "char", i));
                    }
                }
                i += charLen;
            }
        }

        // Sort by UTF-16 position (for buildOutput)
        utf16Details.sort((a, b) -> Integer.compare(a.getPosition(), b.getPosition()));

        // Build output using UTF-16 positions
        String output = buildOutput(word, utf16Details);
        boolean changed = !output.equals(word);

        // Convert to codepoint positions for public API
        List<ConversionDetail> cpDetails = new ArrayList<>();
        for (ConversionDetail d : utf16Details) {
            int cpPos = Character.codePointCount(word, 0, d.getPosition());
            cpDetails.add(new ConversionDetail(d.getSource(), d.getTarget(), d.getLayer(), cpPos));
        }

        return new LookupResult(word, output, changed, cpDetails);
    }

    /**
     * Build output text from conversion details (uses UTF-16 positions internally).
     */
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

    /**
     * Builder for ZhtwConverter.
     */
    public static final class Builder {

        private List<String> sources = Arrays.asList("cn", "hk");
        private Map<String, String> customDict = Collections.emptyMap();

        private Builder() {}

        /**
         * Set which term sources to use.
         * @param sources list of sources, e.g. ["cn"], ["hk"], or ["cn", "hk"]
         */
        public Builder sources(List<String> sources) {
            this.sources = new ArrayList<>(sources);
            return this;
        }

        /**
         * Set custom dictionary entries (take priority over built-in terms).
         * @param customDict map of source to target terms
         */
        public Builder customDict(Map<String, String> customDict) {
            this.customDict = new HashMap<>(customDict);
            return this;
        }

        /** Build the converter. */
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
                    charLayerEnabled,
                    sources
            );
        }
    }
}
