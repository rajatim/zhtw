package com.rajatim.zhtw;

import java.util.Objects;

public final class Match {
    private final int start;
    private final int end;
    private final String source;
    private final String target;

    public Match(int start, int end, String source, String target) {
        this.start = start;
        this.end = end;
        this.source = source;
        this.target = target;
    }

    public int getStart() { return start; }
    public int getEnd() { return end; }
    public String getSource() { return source; }
    public String getTarget() { return target; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Match)) return false;
        Match m = (Match) o;
        return start == m.start && end == m.end
                && Objects.equals(source, m.source)
                && Objects.equals(target, m.target);
    }

    @Override
    public int hashCode() {
        return Objects.hash(start, end, source, target);
    }

    @Override
    public String toString() {
        return "Match{start=" + start + ", end=" + end
                + ", source='" + source + "', target='" + target + "'}";
    }
}
