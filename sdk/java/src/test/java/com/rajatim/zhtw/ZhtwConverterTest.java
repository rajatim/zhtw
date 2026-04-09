package com.rajatim.zhtw;

import org.junit.jupiter.api.Test;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ZhtwConverterTest {

    @Test
    void convertBasicTerm() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u8edf\u9ad4\u6e2c\u8a66", conv.convert("\u8f6f\u4ef6\u6d4b\u8bd5"));
    }

    @Test
    void convertMixedTermAndChar() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals(
                "\u9019\u500b\u4f3a\u670d\u5668\u7684\u8a18\u61b6\u9ad4\u4e0d\u5920",
                conv.convert("\u8fd9\u4e2a\u670d\u52a1\u5668\u7684\u5185\u5b58\u4e0d\u591f")
        );
    }

    @Test
    void convertHkTermOnly() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("hk"))
                .build();
        assertEquals(
                "\u8edf\u9ad4\u5de5\u7a0b\u5e2b",
                conv.convert("\u8edf\u4ef6\u5de5\u7a0b\u5e2b")
        );
    }

    @Test
    void convertNoChange() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u5df2\u7d93\u662f\u7e41\u9ad4", conv.convert("\u5df2\u7d93\u662f\u7e41\u9ad4"));
    }

    @Test
    void convertEmptyString() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("", conv.convert(""));
    }

    @Test
    void convertNullReturnsNull() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertNull(conv.convert(null));
    }

    @Test
    void convertAmbiguousChar() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u982d\u9aee\u5f88\u5e79", conv.convert("\u5934\u53d1\u5f88\u5e72"));
    }

    @Test
    void convertCompoundTerms() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u8cc7\u6599\u5eab\u4f3a\u670d\u5668", conv.convert("\u6570\u636e\u5e93\u670d\u52a1\u5668"));
    }

    @Test
    void convertCloudComputing() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u96f2\u7aef\u904b\u7b97", conv.convert("\u4e91\u8ba1\u7b97"));
    }

    @Test
    void convertFazhan() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\u767c\u5c55\u5f88\u5feb", conv.convert("\u53d1\u5c55\u5f88\u5feb"));
    }

    @Test
    void convertWithCustomDict() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .customDict(Collections.singletonMap("\u5496\u5561", "\u73c8\u7432"))
                .build();
        assertEquals("\u73c8\u7432", conv.convert("\u5496\u5561"));
    }

    // === check() tests ===

    @Test
    void checkReturnsTermAndCharMatches() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        List<Match> matches = conv.check("\u8f6f\u4ef6\u6d4b\u8bd5");
        // Term matches: 软件 (0,2), 测试 (2,4)
        // Char matches: 软 (0,1), 测 (2,3), 试 (3,4)
        assertTrue(matches.size() >= 2, "Should have at least term matches");
        assertEquals(0, matches.get(0).getStart());
        assertEquals(2, matches.get(0).getEnd());
    }

    @Test
    void checkNoChangeReturnsEmpty() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        List<Match> matches = conv.check("\u5df2\u7d93\u662f\u7e41\u9ad4");
        assertTrue(matches.isEmpty());
    }

    @Test
    void checkHkOnlyTermMatches() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("hk"))
                .build();
        List<Match> matches = conv.check("\u8edf\u4ef6\u5de5\u7a0b\u5e2b");
        assertEquals(1, matches.size());
        assertEquals("\u8edf\u4ef6", matches.get(0).getSource());
    }

    // === lookup() tests ===

    @Test
    void lookupKnownTerm() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        LookupResult result = conv.lookup("\u8f6f\u4ef6");
        assertEquals("\u8edf\u9ad4", result.getOutput());
        assertTrue(result.isChanged());
        assertEquals(1, result.getDetails().size());
        assertEquals("term", result.getDetails().get(0).getLayer());
    }

    @Test
    void lookupUnchanged() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        LookupResult result = conv.lookup("\u53f0");
        assertEquals("\u53f0", result.getOutput());
        assertFalse(result.isChanged());
        assertTrue(result.getDetails().isEmpty());
    }

    @Test
    void lookupHkTerm() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("hk"))
                .build();
        LookupResult result = conv.lookup("\u8edf\u4ef6");
        assertEquals("\u8edf\u9ad4", result.getOutput());
        assertTrue(result.isChanged());
    }
}
