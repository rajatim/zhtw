package com.rajatim.zhtw;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Loads and provides access to zhtw-data.json.
 *
 * <p>Charmap uses codepoint (int) keys to handle supplementary plane characters
 * (CJK Extension B+, codepoints above U+FFFF) that cannot fit in a Java {@code char}.
 */
final class ZhtwData {

    private final String version;
    private final Map<Integer, String> charmap;   // codepoint -> replacement string
    private final Set<Integer> ambiguous;          // ambiguous codepoints
    private final Map<String, Map<String, String>> terms;

    private ZhtwData(String version,
                     Map<Integer, String> charmap,
                     Set<Integer> ambiguous,
                     Map<String, Map<String, String>> terms) {
        this.version = version;
        this.charmap = Collections.unmodifiableMap(charmap);
        this.ambiguous = Collections.unmodifiableSet(ambiguous);
        Map<String, Map<String, String>> unmodTerms = new HashMap<>();
        for (Map.Entry<String, Map<String, String>> e : terms.entrySet()) {
            unmodTerms.put(e.getKey(), Collections.unmodifiableMap(e.getValue()));
        }
        this.terms = Collections.unmodifiableMap(unmodTerms);
    }

    static ZhtwData fromClasspath() {
        return fromClasspath("/zhtw-data.json");
    }

    static ZhtwData fromClasspath(String resourcePath) {
        InputStream is = ZhtwData.class.getResourceAsStream(resourcePath);
        if (is == null) {
            throw new IllegalStateException("Resource not found: " + resourcePath);
        }
        return fromInputStream(is);
    }

    static ZhtwData fromInputStream(InputStream is) {
        Gson gson = new Gson();
        Reader reader = new InputStreamReader(is, StandardCharsets.UTF_8);

        Type rootType = new TypeToken<Map<String, Object>>() {}.getType();
        Map<String, Object> root = gson.fromJson(reader, rootType);

        String version = (String) root.get("version");

        // Parse charmap — keys and values may be supplementary plane characters
        @SuppressWarnings("unchecked")
        Map<String, Object> charmapObj = (Map<String, Object>) root.get("charmap");

        @SuppressWarnings("unchecked")
        Map<String, String> rawChars = (Map<String, String>) charmapObj.get("chars");
        Map<Integer, String> charmap = new HashMap<>();
        for (Map.Entry<String, String> e : rawChars.entrySet()) {
            String key = e.getKey();
            String val = e.getValue();
            if (!key.isEmpty() && !val.isEmpty()) {
                int codepoint = key.codePointAt(0);
                charmap.put(codepoint, val);
            }
        }

        @SuppressWarnings("unchecked")
        List<String> rawAmbiguous = (List<String>) charmapObj.get("ambiguous");
        Set<Integer> ambiguous = new HashSet<>();
        for (String s : rawAmbiguous) {
            if (!s.isEmpty()) {
                ambiguous.add(s.codePointAt(0));
            }
        }

        // Parse terms
        @SuppressWarnings("unchecked")
        Map<String, Object> rawTerms = (Map<String, Object>) root.get("terms");
        Map<String, Map<String, String>> terms = new HashMap<>();
        for (Map.Entry<String, Object> e : rawTerms.entrySet()) {
            @SuppressWarnings("unchecked")
            Map<String, String> sourceTerms = (Map<String, String>) e.getValue();
            terms.put(e.getKey(), new HashMap<>(sourceTerms));
        }

        return new ZhtwData(version, charmap, ambiguous, terms);
    }

    String getVersion() { return version; }
    Map<Integer, String> getCharmap() { return charmap; }
    Set<Integer> getAmbiguous() { return ambiguous; }

    Map<String, String> getTerms(String source) {
        return terms.getOrDefault(source, Collections.emptyMap());
    }
}
