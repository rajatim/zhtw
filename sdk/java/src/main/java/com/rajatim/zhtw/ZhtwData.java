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
import java.util.regex.Pattern;

/**
 * Loads and provides access to zhtw-data.json.
 *
 * <p>Charmap uses codepoint (int) keys to handle supplementary plane characters
 * (CJK Extension B+, codepoints above U+FFFF) that cannot fit in a Java {@code char}.
 */
final class ZhtwData {

    private static final Set<Integer> SUPPORTED_SCHEMA_VERSIONS = Set.of(1, 2);
    private static final Pattern RULE_ID =
            Pattern.compile("^[a-z0-9][a-z0-9._:-]{2,127}$");
    private static final Set<String> RULE_CLASSES =
            Set.of("bulk", "generated_guard", "curated", "custom");
    private static final Set<String> TRUST_LEVELS =
            Set.of("imported", "generated", "curated", "custom");
    private static final Set<String> REVIEW_STATUSES =
            Set.of("pending", "approved", "rejected");
    private static final Set<String> RULE_DOMAINS = Set.of(
            "general", "business", "daily", "ecommerce", "education", "finance", "formal",
            "gaming", "geography", "it", "legal", "medical", "social", "ui");

    private final String version;
    private final Map<Integer, String> charmap;   // codepoint -> replacement string
    private final Set<Integer> ambiguous;          // ambiguous codepoints
    private final Map<Integer, String> balancedDefaults; // codepoint -> default replacement
    private final Map<String, Map<String, String>> terms;

    private ZhtwData(String version,
                     Map<Integer, String> charmap,
                     Set<Integer> ambiguous,
                     Map<Integer, String> balancedDefaults,
                     Map<String, Map<String, String>> terms) {
        this.version = version;
        this.charmap = Collections.unmodifiableMap(charmap);
        this.ambiguous = Collections.unmodifiableSet(ambiguous);
        this.balancedDefaults = Collections.unmodifiableMap(balancedDefaults);
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
        Type rootType = new TypeToken<Map<String, Object>>() {}.getType();
        Map<String, Object> root;
        try (Reader reader = new InputStreamReader(is, StandardCharsets.UTF_8)) {
            root = gson.fromJson(reader, rootType);
        } catch (java.io.IOException e) {
            throw new IllegalStateException("Failed to read zhtw data", e);
        }

        Number schemaVersion = (Number) root.get("schema_version");
        if (schemaVersion == null
                || schemaVersion.doubleValue() % 1 != 0
                || !SUPPORTED_SCHEMA_VERSIONS.contains(schemaVersion.intValue())) {
            throw new IllegalStateException("Unsupported zhtw data schema version");
        }
        int parsedSchemaVersion = schemaVersion.intValue();

        String version = (String) root.get("version");
        if (version == null || version.isEmpty()) {
            throw new IllegalStateException("Missing zhtw data version");
        }
        Set<String> expectedRoot = parsedSchemaVersion == 1
                ? Set.of("schema_version", "version", "stats", "charmap", "terms")
                : Set.of("schema_version", "version", "stats", "charmap", "terms", "rule_catalog");
        if (!root.keySet().equals(expectedRoot)) {
            throw new IllegalStateException("Unexpected or missing top-level zhtw data fields");
        }

        // Parse charmap — keys and values may be supplementary plane characters
        @SuppressWarnings("unchecked")
        Map<String, Object> charmapObj = (Map<String, Object>) root.get("charmap");
        if (!charmapObj.keySet().equals(Set.of(
                "chars", "ambiguous", "balanced_defaults", "balanced_protect_terms"))) {
            throw new IllegalStateException("Unexpected or missing charmap fields");
        }

        @SuppressWarnings("unchecked")
        Map<String, String> rawChars = (Map<String, String>) charmapObj.get("chars");
        Map<Integer, String> charmap = new HashMap<>();
        for (Map.Entry<String, String> e : rawChars.entrySet()) {
            String key = e.getKey();
            String val = e.getValue();
            requireSingleCodepoint(key, "charmap key");
            requireSingleCodepoint(val, "charmap value");
            charmap.put(key.codePointAt(0), val);
        }

        @SuppressWarnings("unchecked")
        List<String> rawAmbiguous = (List<String>) charmapObj.get("ambiguous");
        Set<Integer> ambiguous = new HashSet<>();
        for (String s : rawAmbiguous) {
            requireSingleCodepoint(s, "ambiguous entry");
            ambiguous.add(s.codePointAt(0));
        }

        // Parse balanced_defaults
        Map<Integer, String> balancedDefaults = new HashMap<>();
        @SuppressWarnings("unchecked")
        Map<String, String> rawBalanced = (Map<String, String>) charmapObj.get("balanced_defaults");
        if (rawBalanced != null) {
            for (Map.Entry<String, String> e : rawBalanced.entrySet()) {
                String key = e.getKey();
                String val = e.getValue();
                requireSingleCodepoint(key, "balanced default key");
                requireSingleCodepoint(val, "balanced default value");
                balancedDefaults.put(key.codePointAt(0), val);
            }
        }

        // Parse terms
        @SuppressWarnings("unchecked")
        Map<String, Object> rawTerms = (Map<String, Object>) root.get("terms");
        if (!Set.of("cn", "hk").containsAll(rawTerms.keySet())) {
            throw new IllegalStateException("Unsupported term source");
        }
        Map<String, Map<String, String>> terms = new HashMap<>();
        for (Map.Entry<String, Object> e : rawTerms.entrySet()) {
            @SuppressWarnings("unchecked")
            Map<String, String> sourceTerms = (Map<String, String>) e.getValue();
            terms.put(e.getKey(), new HashMap<>(sourceTerms));
        }

        if (parsedSchemaVersion == 2) {
            validateRuleCatalog(root, rawTerms);
        }

        return new ZhtwData(version, charmap, ambiguous, balancedDefaults, terms);
    }

    @SuppressWarnings("unchecked")
    private static void validateRuleCatalog(
            Map<String, Object> root,
            Map<String, Object> rawTerms) {
        Object rawCatalog = root.get("rule_catalog");
        if (!(rawCatalog instanceof Map)) {
            throw new IllegalStateException("rule_catalog must be an object");
        }
        Map<String, Object> catalog = (Map<String, Object>) rawCatalog;
        if (!catalog.keySet().equals(Set.of("format", "groups"))
                || !"grouped-v1".equals(catalog.get("format"))
                || !(catalog.get("groups") instanceof List)) {
            throw new IllegalStateException("Invalid rule_catalog envelope");
        }

        Set<String> ids = new HashSet<>();
        Set<String> approved = new HashSet<>();
        int count = 0;
        for (Object rawGroup : (List<Object>) catalog.get("groups")) {
            if (!(rawGroup instanceof Map)) {
                throw new IllegalStateException("rule_catalog group must be an object");
            }
            Map<String, Object> group = (Map<String, Object>) rawGroup;
            Set<String> groupKeys = Set.of(
                    "source_locale", "rule_class", "domain", "trust_level", "priority",
                    "context", "evidence_source", "review_status", "rules");
            if (!group.keySet().equals(groupKeys)) {
                throw new IllegalStateException("Unexpected or missing rule_catalog group fields");
            }
            String locale = requireMember(group, "source_locale");
            String ruleClass = requireMember(group, "rule_class");
            String domain = requireMember(group, "domain");
            String trust = requireMember(group, "trust_level");
            String review = requireMember(group, "review_status");
            if (!Set.of("cn", "hk").contains(locale)
                    || !RULE_CLASSES.contains(ruleClass)
                    || !RULE_DOMAINS.contains(domain)
                    || !TRUST_LEVELS.contains(trust)
                    || !REVIEW_STATUSES.contains(review)) {
                throw new IllegalStateException("Invalid rule_catalog group metadata");
            }
            Object priority = group.get("priority");
            if (!(priority instanceof Number)
                    || ((Number) priority).doubleValue() % 1 != 0
                    || ((Number) priority).intValue() < -1000
                    || ((Number) priority).intValue() > 1000) {
                throw new IllegalStateException("Invalid rule_catalog priority");
            }
            Object context = group.get("context");
            if (!(context instanceof List)
                    || ((List<Object>) context).stream().anyMatch(
                            item -> !(item instanceof String) || ((String) item).isEmpty())
                    || new HashSet<>((List<Object>) context).size() != ((List<Object>) context).size()) {
                throw new IllegalStateException("Invalid rule_catalog context");
            }
            Object evidence = group.get("evidence_source");
            if (evidence != null && (!(evidence instanceof String) || ((String) evidence).isEmpty())) {
                throw new IllegalStateException("Invalid rule_catalog evidence_source");
            }
            if ("approved".equals(review) && evidence == null) {
                throw new IllegalStateException("Approved rule_catalog groups require evidence");
            }
            Object rawRules = group.get("rules");
            if (!(rawRules instanceof Map)) {
                throw new IllegalStateException("rule_catalog rules must be an object");
            }
            for (Map.Entry<String, Object> entry : ((Map<String, Object>) rawRules).entrySet()) {
                String id = entry.getKey();
                if (!RULE_ID.matcher(id).matches() || !ids.add(id)) {
                    throw new IllegalStateException("Duplicate or invalid rule ID");
                }
                if (!(entry.getValue() instanceof List)) {
                    throw new IllegalStateException("rule_catalog rule must be a pair");
                }
                List<Object> pair = (List<Object>) entry.getValue();
                if (pair.size() != 2
                        || !(pair.get(0) instanceof String)
                        || ((String) pair.get(0)).isEmpty()
                        || !(pair.get(1) instanceof String)
                        || ((String) pair.get(1)).isEmpty()) {
                    throw new IllegalStateException("rule_catalog rule must contain source and target");
                }
                count++;
                if ("approved".equals(review)) {
                    approved.add(locale + "\0" + pair.get(0) + "\0" + pair.get(1));
                }
            }
        }

        Map<String, Object> stats = (Map<String, Object>) root.get("stats");
        Object expectedCount = stats.get("rule_catalog_count");
        if (!(expectedCount instanceof Number) || ((Number) expectedCount).intValue() != count) {
            throw new IllegalStateException("rule_catalog count does not match stats");
        }
        for (Map.Entry<String, Object> localeEntry : rawTerms.entrySet()) {
            Map<String, String> sourceTerms = (Map<String, String>) localeEntry.getValue();
            for (Map.Entry<String, String> term : sourceTerms.entrySet()) {
                String key = localeEntry.getKey() + "\0" + term.getKey() + "\0" + term.getValue();
                if (!approved.contains(key)) {
                    throw new IllegalStateException("rule_catalog does not cover effective terms");
                }
            }
        }
    }

    private static String requireMember(Map<String, Object> value, String name) {
        Object member = value.get(name);
        if (!(member instanceof String)) {
            throw new IllegalStateException("rule_catalog field must be a string: " + name);
        }
        return (String) member;
    }

    private static void requireSingleCodepoint(String value, String name) {
        if (value == null || value.codePointCount(0, value.length()) != 1) {
            throw new IllegalStateException(name + " must contain exactly one Unicode code point");
        }
    }

    String getVersion() { return version; }
    Map<Integer, String> getCharmap() { return charmap; }
    Set<Integer> getAmbiguous() { return ambiguous; }
    Map<Integer, String> getBalancedDefaults() { return balancedDefaults; }

    Map<String, String> getTerms(String source) {
        return terms.getOrDefault(source, Collections.emptyMap());
    }
}
