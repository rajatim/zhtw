package com.rajatim.zhtw;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MatchTest {

    @Test
    void gettersReturnConstructorValues() {
        Match m = new Match(0, 2, "\u8f6f\u4ef6", "\u8edf\u9ad4");
        assertEquals(0, m.getStart());
        assertEquals(2, m.getEnd());
        assertEquals("\u8f6f\u4ef6", m.getSource());
        assertEquals("\u8edf\u9ad4", m.getTarget());
    }

    @Test
    void toStringContainsFields() {
        Match m = new Match(0, 2, "ab", "cd");
        String s = m.toString();
        assertTrue(s.contains("0"));
        assertTrue(s.contains("2"));
        assertTrue(s.contains("ab"));
        assertTrue(s.contains("cd"));
    }

    @Test
    void equalsAndHashCode() {
        Match a = new Match(0, 2, "ab", "cd");
        Match b = new Match(0, 2, "ab", "cd");
        Match c = new Match(1, 3, "ab", "cd");
        assertEquals(a, b);
        assertEquals(a.hashCode(), b.hashCode());
        assertNotEquals(a, c);
    }
}
