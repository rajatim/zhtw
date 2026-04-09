package com.rajatim.zhtw;

import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class AhoCorasickMatcherTest {

    private AhoCorasickMatcher matcher(Map<String, String> terms) {
        return new AhoCorasickMatcher(terms);
    }

    @Test
    void basicMatch() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u8f6f\u4ef6", "\u8edf\u9ad4");
        AhoCorasickMatcher m = matcher(terms);
        List<Match> matches = m.findMatches("\u8f6f\u4ef6");
        assertEquals(1, matches.size());
        assertEquals(new Match(0, 2, "\u8f6f\u4ef6", "\u8edf\u9ad4"), matches.get(0));
    }

    @Test
    void longestMatchWins() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u670d\u52a1", "\u670d\u52d9");
        terms.put("\u670d\u52a1\u5668", "\u4f3a\u670d\u5668");
        AhoCorasickMatcher m = matcher(terms);
        List<Match> matches = m.findMatches("\u670d\u52a1\u5668");
        assertEquals(1, matches.size());
        assertEquals("\u670d\u52a1\u5668", matches.get(0).getSource());
        assertEquals("\u4f3a\u670d\u5668", matches.get(0).getTarget());
    }

    @Test
    void multipleNonOverlapping() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u8f6f\u4ef6", "\u8edf\u9ad4");
        terms.put("\u6d4b\u8bd5", "\u6e2c\u8a66");
        AhoCorasickMatcher m = matcher(terms);
        List<Match> matches = m.findMatches("\u8f6f\u4ef6\u6d4b\u8bd5");
        assertEquals(2, matches.size());
        assertEquals(0, matches.get(0).getStart());
        assertEquals(2, matches.get(0).getEnd());
        assertEquals(2, matches.get(1).getStart());
        assertEquals(4, matches.get(1).getEnd());
    }

    @Test
    void identityMappingNotYielded() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u6a94\u6848", "\u6a94\u6848");
        AhoCorasickMatcher m = matcher(terms);
        List<Match> matches = m.findMatches("\u6a94\u6848");
        assertTrue(matches.isEmpty());
    }

    @Test
    void emptyInput() {
        Map<String, String> terms = new HashMap<>();
        terms.put("a", "b");
        AhoCorasickMatcher m = matcher(terms);
        assertTrue(m.findMatches("").isEmpty());
    }

    @Test
    void noMatch() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u8f6f\u4ef6", "\u8edf\u9ad4");
        AhoCorasickMatcher m = matcher(terms);
        assertTrue(m.findMatches("hello").isEmpty());
    }

    @Test
    void emptyTerms() {
        AhoCorasickMatcher m = matcher(new HashMap<>());
        assertTrue(m.findMatches("anything").isEmpty());
    }

    @Test
    void replaceAll() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u8f6f\u4ef6", "\u8edf\u9ad4");
        terms.put("\u6d4b\u8bd5", "\u6e2c\u8a66");
        AhoCorasickMatcher m = matcher(terms);
        assertEquals("\u8edf\u9ad4\u6e2c\u8a66", m.replaceAll("\u8f6f\u4ef6\u6d4b\u8bd5"));
    }

    @Test
    void replaceAllPreservesUnmatched() {
        Map<String, String> terms = new HashMap<>();
        terms.put("\u8f6f\u4ef6", "\u8edf\u9ad4");
        AhoCorasickMatcher m = matcher(terms);
        assertEquals("abc\u8edf\u9ad4xyz", m.replaceAll("abc\u8f6f\u4ef6xyz"));
    }

    @Test
    void longerMatchTakesPriorityOverSubstring() {
        // 发展 (发展 -> 發展) should match as a whole, not 发 (发 -> 發)
        Map<String, String> terms = new HashMap<>();
        terms.put("\u53d1\u5c55", "\u767c\u5c55");
        terms.put("\u53d1", "\u767c");
        AhoCorasickMatcher m = matcher(terms);
        List<Match> matches = m.findMatches("\u53d1\u5c55\u5f88\u5feb");
        assertEquals(1, matches.size());
        assertEquals("\u53d1\u5c55", matches.get(0).getSource());
    }
}
