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
        Map<Character, Character> charmap = data.getCharmap();
        // Note: supplementary-plane chars (codepoint > 0xFFFF) are not representable as a single Java char.
        // Only BMP chars (~2600) are stored; the full dataset has ~6300 entries total.
        assertTrue(charmap.size() > 2000, "charmap should have > 2000 BMP entries, got " + charmap.size());
    }

    @Test
    void ambiguousHasExpectedSize() {
        ZhtwData data = ZhtwData.fromClasspath();
        Set<Character> ambiguous = data.getAmbiguous();
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
    void charmapContainsKnownEntry() {
        ZhtwData data = ZhtwData.fromClasspath();
        assertEquals('\u842c', data.getCharmap().get('\u4e07'));
    }

    @Test
    void ambiguousContainsKnownChar() {
        ZhtwData data = ZhtwData.fromClasspath();
        assertTrue(data.getAmbiguous().contains('\u53f0'));
    }

    @Test
    void cnTermsContainKnownEntry() {
        ZhtwData data = ZhtwData.fromClasspath();
        assertEquals("\u8edf\u9ad4", data.getTerms("cn").get("\u8f6f\u4ef6"));
    }
}
