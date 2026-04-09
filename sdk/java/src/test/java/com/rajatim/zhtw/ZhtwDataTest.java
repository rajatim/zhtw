package com.rajatim.zhtw;

import org.junit.jupiter.api.Test;

import java.util.Map;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.*;

class ZhtwDataTest {

    @Test
    void loadsFromClasspath() {
        ZhtwData data = ZhtwData.fromClasspath();
        assertNotNull(data);
    }

    @Test
    void versionIsPresent() {
        ZhtwData data = ZhtwData.fromClasspath();
        assertNotNull(data.getVersion());
        assertFalse(data.getVersion().isEmpty());
    }

    @Test
    void charmapHasExpectedSize() {
        ZhtwData data = ZhtwData.fromClasspath();
        Map<Integer, String> charmap = data.getCharmap();
        assertTrue(charmap.size() > 6000, "charmap should have > 6000 entries, got " + charmap.size());
    }

    @Test
    void ambiguousHasExpectedSize() {
        ZhtwData data = ZhtwData.fromClasspath();
        Set<Integer> ambiguous = data.getAmbiguous();
        assertTrue(ambiguous.size() > 100, "ambiguous should have > 100 entries, got " + ambiguous.size());
    }

    @Test
    void cnTermsHasExpectedSize() {
        ZhtwData data = ZhtwData.fromClasspath();
        Map<String, String> cn = data.getTerms("cn");
        assertTrue(cn.size() > 30000, "CN terms should have > 30000 entries, got " + cn.size());
    }

    @Test
    void hkTermsPresent() {
        ZhtwData data = ZhtwData.fromClasspath();
        Map<String, String> hk = data.getTerms("hk");
        assertTrue(hk.size() > 50, "HK terms should have > 50 entries, got " + hk.size());
    }

    @Test
    void unknownSourceReturnsEmpty() {
        ZhtwData data = ZhtwData.fromClasspath();
        Map<String, String> unknown = data.getTerms("unknown");
        assertTrue(unknown.isEmpty());
    }

    @Test
    void charmapContainsKnownBmpEntry() {
        // U+4E07 (万) -> U+842C (萬) — both BMP
        ZhtwData data = ZhtwData.fromClasspath();
        assertEquals("\u842c", data.getCharmap().get(0x4E07));
    }

    @Test
    void charmapContainsSupplementaryEntry() {
        // U+36DF (㛟) -> U+217B5 (𡞵) — value is supplementary plane
        ZhtwData data = ZhtwData.fromClasspath();
        String replacement = data.getCharmap().get(0x36DF);
        assertNotNull(replacement, "Should contain supplementary plane mapping");
        assertEquals(0x217B5, replacement.codePointAt(0));
    }

    @Test
    void ambiguousContainsKnownChar() {
        // U+53F0 (台) is ambiguous
        ZhtwData data = ZhtwData.fromClasspath();
        assertTrue(data.getAmbiguous().contains(0x53F0));
    }

    @Test
    void cnTermsContainKnownEntry() {
        // \u8f6f\u4ef6 (软件) -> \u8edf\u9ad4 (軟體)
        ZhtwData data = ZhtwData.fromClasspath();
        assertEquals("\u8edf\u9ad4", data.getTerms("cn").get("\u8f6f\u4ef6"));
    }
}
