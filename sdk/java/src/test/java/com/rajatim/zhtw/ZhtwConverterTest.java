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

    // === getDefault() tests ===

    @Test
    void getDefaultReturnsSameInstance() {
        ZhtwConverter a = ZhtwConverter.getDefault();
        ZhtwConverter b = ZhtwConverter.getDefault();
        assertSame(a, b);
    }

    @Test
    void getDefaultConverts() {
        String result = ZhtwConverter.getDefault().convert("\u8f6f\u4ef6\u6d4b\u8bd5");
        assertEquals("\u8edf\u9ad4\u6e2c\u8a66", result);
    }

    @Test
    void getDefaultThreadSafe() throws Exception {
        int threads = 10;
        ZhtwConverter[] results = new ZhtwConverter[threads];
        Thread[] threadArr = new Thread[threads];

        for (int i = 0; i < threads; i++) {
            final int idx = i;
            threadArr[i] = new Thread(() -> results[idx] = ZhtwConverter.getDefault());
            threadArr[i].start();
        }
        for (Thread t : threadArr) {
            t.join();
        }

        for (int i = 1; i < threads; i++) {
            assertSame(results[0], results[i], "All threads should get same instance");
        }
    }

    // === Builder edge cases ===

    @Test
    void builderCnOnly() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertNotNull(conv);
    }

    @Test
    void builderHkOnly() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("hk"))
                .build();
        String result = conv.convert("\u8fd9");
        assertEquals("\u8fd9", result, "HK source should not apply char conversion");
    }

    @Test
    void builderCustomDictOverridesBuiltin() {
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .customDict(Collections.singletonMap("\u8f6f\u4ef6", "SOFTWARE"))
                .build();
        assertEquals("SOFTWARE", conv.convert("\u8f6f\u4ef6"));
    }

    @Test
    void builderEachBuildCreatesNewInstance() {
        ZhtwConverter.Builder b = ZhtwConverter.builder();
        ZhtwConverter a = b.sources(Collections.singletonList("cn")).build();
        ZhtwConverter c = b.sources(Collections.singletonList("hk")).build();
        assertNotSame(a, c);
    }

    // === Supplementary plane position tests (codepoint vs UTF-16) ===

    @Test
    void checkSupplementaryPrefixUsesCodepointPositions() {
        // U+20000 (𠀀) is a supplementary plane char: 1 codepoint but 2 UTF-16 code units.
        // 软件 (U+8F6F U+4EF6) starts at codepoint index 1, NOT UTF-16 index 2.
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        List<Match> matches = conv.check("\uD840\uDC00\u8f6f\u4ef6"); // 𠀀软件
        boolean foundTerm = false;
        for (Match m : matches) {
            if ("\u8f6f\u4ef6".equals(m.getSource())) {
                assertEquals(1, m.getStart(), "Term match should start at codepoint 1, not UTF-16 index 2");
                assertEquals(3, m.getEnd(), "Term match should end at codepoint 3");
                foundTerm = true;
            }
        }
        assertTrue(foundTerm, "Should find term match for 软件");
    }

    @Test
    void checkSupplementaryPrefixCharLevel() {
        // 𠀀这 — char-level match for 这 (U+8FD9) should be at codepoint index 1
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        List<Match> matches = conv.check("\uD840\uDC00\u8fd9"); // 𠀀这
        boolean foundChar = false;
        for (Match m : matches) {
            if ("\u8fd9".equals(m.getSource())) {
                assertEquals(1, m.getStart(), "Char match should start at codepoint 1, not UTF-16 index 2");
                assertEquals(2, m.getEnd());
                foundChar = true;
            }
        }
        assertTrue(foundChar, "Should find char match for 这");
    }

    @Test
    void lookupSupplementaryPrefixUsesCodepointPositions() {
        // 𠀀软件 — lookup detail for 软件 should be at codepoint position 1
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        LookupResult result = conv.lookup("\uD840\uDC00\u8f6f\u4ef6"); // 𠀀软件
        assertTrue(result.isChanged());
        boolean foundTerm = false;
        for (ConversionDetail d : result.getDetails()) {
            if ("term".equals(d.getLayer()) && "\u8f6f\u4ef6".equals(d.getSource())) {
                assertEquals(1, d.getPosition(), "Term detail should be at codepoint 1, not UTF-16 index 2");
                foundTerm = true;
            }
        }
        assertTrue(foundTerm, "Should find term detail for 软件");
    }

    @Test
    void convertSupplementaryPrefixPreservesContent() {
        // 𠀀软件 should convert to 𠀀軟體 (supplementary char preserved, term converted)
        ZhtwConverter conv = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
        assertEquals("\uD840\uDC00\u8edf\u9ad4", conv.convert("\uD840\uDC00\u8f6f\u4ef6"));
    }
}
