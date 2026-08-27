package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

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
    private final Map<String, List<ZhtwData.RuleMeta>> ruleRecords;

    private ZhtwConverter(AhoCorasickMatcher matcher,
                          Map<Integer, String> charmap,
                          Map<Integer, String> balancedDefaults,
                          boolean charLayerEnabled,
                          boolean balancedMode,
                          List<String> sources,
                          List<ZhtwData.RuleMeta> ruleCatalog) {
        this.matcher = matcher;
        this.charmap = charmap;
        this.balancedDefaults = balancedDefaults;
        this.charLayerEnabled = charLayerEnabled;
        this.balancedMode = balancedMode;
        this.sources = Collections.unmodifiableList(new ArrayList<>(sources));
        Map<String, List<ZhtwData.RuleMeta>> grouped = new HashMap<>();
        for (ZhtwData.RuleMeta record : ruleCatalog) {
            grouped.computeIfAbsent(record.source, ignored -> new ArrayList<>()).add(record);
        }
        this.ruleRecords = Collections.unmodifiableMap(grouped);
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

        return convertWithScan(text, matcher.scan(text));
    }

    private String convertWithScan(String text, AhoCorasickMatcher.ScanResult scan) {
        Set<Integer> covered = scan.covered;
        List<Match> matches = scan.matches;

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

    /** Convert only JSON string values while preserving all unrelated bytes. */
    public String convertJson(String text) {
        return JsonAdapter.convert(text, this::convert);
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
        AhoCorasickMatcher.ScanResult scan = matcher.scan(text);
        Set<Integer> coveredUtf16 = scan.covered;

        // Term-level matches (matcher returns UTF-16 indices, convert to codepoint)
        for (Match m : scan.matches) {
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
        AhoCorasickMatcher.ScanResult scan = matcher.scan(word);
        Set<Integer> coveredUtf16 = scan.covered;

        // 1. Term layer — targets stored verbatim (matching Python/TS/Rust).
        List<Match> termMatches = scan.matches;
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
                    if (replacement != null && charLayerEnabled) {
                        String remapped = charmap.get(replacement.codePointAt(0));
                        if (remapped != null) replacement = remapped;
                    }
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

    private static final class CharacterChange {
        final int position;
        final int length;
        final String source;
        final String target;
        final String layer;
        final String ruleId;
        final String reasonCode;

        CharacterChange(int position, int length, String source, String target,
                        String layer, String ruleId, String reasonCode) {
            this.position = position;
            this.length = length;
            this.source = source;
            this.target = target;
            this.layer = layer;
            this.ruleId = ruleId;
            this.reasonCode = reasonCode;
        }
    }

    private List<CharacterChange> characterChanges(String text, Set<Integer> covered) {
        List<CharacterChange> changes = new ArrayList<>();
        int position = 0;
        while (position < text.length()) {
            int cp = text.codePointAt(position);
            int length = Character.charCount(cp);
            String source = new String(Character.toChars(cp));
            if (!covered.contains(position)) {
                String balanced = balancedMode ? balancedDefaults.get(cp) : null;
                if (balanced != null) {
                    String target = charLayerEnabled
                            ? charmap.getOrDefault(balanced.codePointAt(0), balanced)
                            : balanced;
                    if (!target.equals(source)) {
                        changes.add(new CharacterChange(
                                position, length, source, target, "balanced",
                                "balanced:u" + Integer.toHexString(cp), "balanced_default"));
                    }
                } else if (charLayerEnabled) {
                    String target = charmap.get(cp);
                    if (target != null && !target.equals(source)) {
                        changes.add(new CharacterChange(
                                position, length, source, target, "char",
                                "charmap:u" + Integer.toHexString(cp), "char_map"));
                    }
                }
            }
            position += length;
        }
        return changes;
    }

    private ZhtwData.RuleMeta ruleRecordFor(Match match) {
        List<ZhtwData.RuleMeta> candidates = ruleRecords.getOrDefault(
                match.getSource(), Collections.emptyList());
        for (int i = candidates.size() - 1; i >= 0; i--) {
            ZhtwData.RuleMeta record = candidates.get(i);
            if (record.target.equals(match.getTarget())) return record;
        }
        return null;
    }

    /** Convert text and return stable rule events from the same matcher scan. */
    public ExplainResult explain(String text) {
        if (text == null || text.isEmpty()) {
            return new ExplainResult(text, Collections.emptyList());
        }

        AhoCorasickMatcher.DetailedScanResult scan = matcher.scanDetailed(text);
        List<CharacterChange> changes = characterChanges(text, scan.covered);
        Map<Integer, Match> selectedByStart = new HashMap<>();
        for (Match match : scan.matches) selectedByStart.put(match.getStart(), match);
        Map<Integer, CharacterChange> changesByStart = new HashMap<>();
        for (CharacterChange change : changes) changesByStart.put(change.position, change);

        int[][] spans = new int[text.length()][2];
        StringBuilder output = new StringBuilder(text.length());
        int inputPosition = 0;
        int outputPosition = 0;
        while (inputPosition < text.length()) {
            Match match = selectedByStart.get(inputPosition);
            if (match != null) {
                int outputEnd = outputPosition
                        + match.getTarget().codePointCount(0, match.getTarget().length());
                for (int i = match.getStart(); i < match.getEnd(); i++) {
                    spans[i][0] = outputPosition;
                    spans[i][1] = outputEnd;
                }
                output.append(match.getTarget());
                outputPosition = outputEnd;
                inputPosition = match.getEnd();
                continue;
            }
            int cp = text.codePointAt(inputPosition);
            int length = Character.charCount(cp);
            String source = new String(Character.toChars(cp));
            CharacterChange change = changesByStart.get(inputPosition);
            String target = change == null ? source : change.target;
            int outputEnd = outputPosition + target.codePointCount(0, target.length());
            for (int i = inputPosition; i < inputPosition + length; i++) {
                spans[i][0] = outputPosition;
                spans[i][1] = outputEnd;
            }
            output.append(target);
            outputPosition = outputEnd;
            inputPosition += length;
        }
        String outputText = output.toString();
        if (!outputText.equals(convertWithScan(text, scan))) {
            throw new IllegalStateException("explain trace diverged from conversion output");
        }

        List<ExplainEvent> events = new ArrayList<>();
        for (AhoCorasickMatcher.MatchDecision decision : scan.decisions) {
            Match match = decision.match;
            int outputStart = Integer.MAX_VALUE;
            int outputEnd = Integer.MIN_VALUE;
            for (int i = match.getStart(); i < match.getEnd(); i++) {
                outputStart = Math.min(outputStart, spans[i][0]);
                outputEnd = Math.max(outputEnd, spans[i][1]);
            }
            ZhtwData.RuleMeta winner = ruleRecordFor(match);
            List<ZhtwData.RuleMeta> conflicts = new ArrayList<>();
            for (ZhtwData.RuleMeta candidate : ruleRecords.getOrDefault(
                    match.getSource(), Collections.emptyList())) {
                if (winner == null || !candidate.id.equals(winner.id)) conflicts.add(candidate);
            }
            String reasonCode = "applied".equals(decision.outcome) && !conflicts.isEmpty()
                    ? "loader_conflict_winner" : decision.reasonCode;
            events.add(new ExplainEvent(
                    winner == null
                            ? legacyCustomRuleId(match.getSource(), match.getTarget())
                            : winner.id,
                    match.getSource().equals(match.getTarget()) ? "identity" : "term",
                    decision.outcome,
                    Character.codePointCount(text, 0, match.getStart()),
                    Character.codePointCount(text, 0, match.getEnd()),
                    outputStart,
                    outputEnd,
                    match.getSource(),
                    match.getTarget(),
                    reasonCode));
            if ("applied".equals(decision.outcome)) {
                for (ZhtwData.RuleMeta conflict : conflicts) {
                    events.add(new ExplainEvent(
                            conflict.id, "term", "skipped",
                            Character.codePointCount(text, 0, match.getStart()),
                            Character.codePointCount(text, 0, match.getEnd()),
                            outputStart, outputEnd, conflict.source, conflict.target,
                            "loader_conflict_loser"));
                }
            }
        }
        for (CharacterChange change : changes) {
            events.add(new ExplainEvent(
                    change.ruleId, change.layer, "applied",
                    Character.codePointCount(text, 0, change.position),
                    Character.codePointCount(text, 0, change.position + change.length),
                    spans[change.position][0], spans[change.position][1],
                    change.source, change.target, change.reasonCode));
        }
        Map<String, Integer> outcomeOrder = Map.of(
                "applied", 0, "protected", 1, "skipped", 2);
        events.sort((left, right) -> {
            int compare = Integer.compare(left.getInputStart(), right.getInputStart());
            if (compare != 0) return compare;
            compare = Integer.compare(left.getInputEnd(), right.getInputEnd());
            if (compare != 0) return compare;
            compare = Integer.compare(
                    outcomeOrder.get(left.getOutcome()), outcomeOrder.get(right.getOutcome()));
            if (compare != 0) return compare;
            return left.getRuleId().compareTo(right.getRuleId());
        });
        return new ExplainResult(outputText, events);
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
                    sources,
                    buildRuleCatalog(data)
            );
        }

        private List<ZhtwData.RuleMeta> buildRuleCatalog(ZhtwData data) {
            List<ZhtwData.RuleMeta> records = new ArrayList<>();
            for (ZhtwData.RuleMeta record : data.getRuleCatalog()) {
                if (sources.contains(record.sourceLocale)) records.add(record);
            }
            for (Map.Entry<String, String> entry : customDict.entrySet()) {
                if (entry.getKey().isEmpty()) continue;
                records.add(new ZhtwData.RuleMeta(
                        legacyCustomRuleId(entry.getKey(), entry.getValue()),
                        "cn", entry.getKey(), entry.getValue()));
            }
            return records;
        }
    }

    private static String legacyCustomRuleId(String source, String target) {
        String canonical = "{\"rule_class\":\"custom\",\"source\":"
                + JsonAdapter.quote(source)
                + ",\"source_locale\":\"cn\",\"target\":"
                + JsonAdapter.quote(target) + "}";
        try {
            byte[] digest = MessageDigest.getInstance("SHA-256")
                    .digest(canonical.getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder();
            for (byte value : digest) hex.append(String.format("%02x", value & 0xff));
            return "legacy:cn:custom:" + hex.substring(0, 24);
        } catch (NoSuchAlgorithmException impossible) {
            throw new IllegalStateException("SHA-256 is unavailable", impossible);
        }
    }
}
