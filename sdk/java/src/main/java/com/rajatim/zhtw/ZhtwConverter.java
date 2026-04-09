package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
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
