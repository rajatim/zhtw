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
    private final Map<Integer, String> balancedDefaults; // codepoint -> default replacement
    private final boolean charLayerEnabled;
    private final boolean balancedMode;
    private final List<String> sources;

    private ZhtwConverter(AhoCorasickMatcher matcher,
                          Map<Integer, String> charmap,
                          Map<Integer, String> balancedDefaults,
                          boolean charLayerEnabled,
                          boolean balancedMode,
                          List<String> sources) {
        this.matcher = matcher;
        this.charmap = charmap;
        this.balancedDefaults = balancedDefaults;
        this.charLayerEnabled = charLayerEnabled;
        this.balancedMode = balancedMode;
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

        // Covered positions from ALL automaton hits (including identity terms).
        // Must be computed on original text before any replacements.
        Set<Integer> covered = matcher.getCoveredPositions(text);
        List<Match> matches = matcher.findMatches(text);

        boolean layersEnabled = charLayerEnabled || balancedMode;

        if (matches.isEmpty()) {
            return layersEnabled ? applyLayersSkipping(text, covered, 0) : text;
        }

        // Gap mode: term targets are inserted verbatim; gaps get char/balanced layers
        // applied only on uncovered positions.
        StringBuilder sb = new StringBuilder(text.length());
        int lastEnd = 0;
        for (Match m : matches) {
            String gap = text.substring(lastEnd, m.getStart());
            sb.append(layersEnabled ? applyLayersSkipping(gap, covered, lastEnd) : gap);
            sb.append(m.getTarget());
            lastEnd = m.getEnd();
        }
        String tail = text.substring(lastEnd);
        sb.append(layersEnabled ? applyLayersSkipping(tail, covered, lastEnd) : tail);
        return sb.toString();
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

        // Covered positions from ALL automaton hits (including identity terms)
        Set<Integer> coveredUtf16 = matcher.getCoveredPositions(text);

        // Term-level matches (matcher returns UTF-16 indices, convert to codepoint)
        for (Match m : matcher.findMatches(text)) {
            int cpStart = Character.codePointCount(text, 0, m.getStart());
            int cpEnd = Character.codePointCount(text, 0, m.getEnd());
            result.add(new Match(cpStart, cpEnd, m.getSource(), m.getTarget()));
        }

        // Balanced defaults matches (skip covered positions)
        if (balancedMode) {
            int cpIndex = 0;
            int i = 0;
            while (i < text.length()) {
                int cp = text.codePointAt(i);
                if (!coveredUtf16.contains(i)) {
                    String replacement = balancedDefaults.get(cp);
                    if (replacement != null) {
                        String original = new String(Character.toChars(cp));
                        result.add(new Match(cpIndex, cpIndex + 1, original, replacement));
                    }
                }
                cpIndex++;
                i += Character.charCount(cp);
            }
        }

        // Char-level matches (on original text, skip covered positions)
        if (charLayerEnabled) {
            int cpIndex = 0;
            int i = 0;
            while (i < text.length()) {
                int cp = text.codePointAt(i);
                if (!coveredUtf16.contains(i)) {
                    String replacement = charmap.get(cp);
                    String original = new String(Character.toChars(cp));
                    if (replacement != null && !replacement.equals(original)) {
                        result.add(new Match(cpIndex, cpIndex + 1, original, replacement));
                    }
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

        // Covered positions from ALL automaton hits (including identity terms)
        Set<Integer> coveredUtf16 = matcher.getCoveredPositions(word);

        // 1. Term layer — targets stored verbatim (matching Python/TS/Rust).
        List<Match> termMatches = matcher.findMatches(word);
        for (Match m : termMatches) {
            utf16Details.add(new ConversionDetail(m.getSource(), m.getTarget(), "term", m.getStart()));
        }

        // 2. Balanced defaults layer: scan uncovered positions
        if (balancedMode) {
            int i = 0;
            while (i < word.length()) {
                int cp = word.codePointAt(i);
                int charLen = Character.charCount(cp);
                if (!coveredUtf16.contains(i)) {
                    String replacement = balancedDefaults.get(cp);
                    if (replacement != null) {
                        String original = new String(Character.toChars(cp));
                        utf16Details.add(new ConversionDetail(original, replacement, "char", i));
                    }
                }
                i += charLen;
            }
        }

        // 3. Char layer: scan uncovered positions
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

    /**
     * Apply balanced defaults and charmap to a text segment, skipping covered positions.
     * Balanced defaults are checked first (matching Python order).
     */
    private String applyLayersSkipping(String segment, Set<Integer> covered, int offset) {
        StringBuilder sb = new StringBuilder(segment.length());
        boolean changed = false;
        int i = 0;
        while (i < segment.length()) {
            int cp = segment.codePointAt(i);
            int charLen = Character.charCount(cp);
            if (covered.contains(offset + i)) {
                sb.appendCodePoint(cp);
            } else {
                // Balanced defaults first, then charmap.
                String replacement = null;
                if (balancedMode) {
                    replacement = balancedDefaults.get(cp);
                }
                if (replacement == null && charLayerEnabled) {
                    replacement = charmap.get(cp);
                }
                if (replacement != null) {
                    sb.append(replacement);
                    changed = true;
                } else {
                    sb.appendCodePoint(cp);
                }
            }
            i += charLen;
        }
        return changed ? sb.toString() : segment;
    }

    /**
     * Builder for ZhtwConverter.
     */
    public static final class Builder {

        private List<String> sources = Arrays.asList("cn", "hk");
        private Map<String, String> customDict = Collections.emptyMap();
        private String ambiguityMode = "strict";

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

        /**
         * Set ambiguity handling mode.
         * @param mode "strict" (default) or "balanced"
         */
        public Builder ambiguityMode(String mode) {
            this.ambiguityMode = mode != null ? mode : "strict";
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
            // balanced defaults are CN→TW mappings; degrade to strict when CN not in sources.
            boolean balanced = "balanced".equals(ambiguityMode) && charLayerEnabled;

            return new ZhtwConverter(
                    matcher,
                    data.getCharmap(),
                    data.getBalancedDefaults(),
                    charLayerEnabled,
                    balanced,
                    sources
            );
        }
    }
}
