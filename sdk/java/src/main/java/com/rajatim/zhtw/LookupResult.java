package com.rajatim.zhtw;

import java.util.Collections;
import java.util.List;
import java.util.Objects;

public final class LookupResult {
    private final String input;
    private final String output;
    private final boolean changed;
    private final List<ConversionDetail> details;

    public LookupResult(String input, String output, boolean changed, List<ConversionDetail> details) {
        this.input = input;
        this.output = output;
        this.changed = changed;
        this.details = Collections.unmodifiableList(details);
    }

    public String getInput() { return input; }
    public String getOutput() { return output; }
    public boolean isChanged() { return changed; }
    public List<ConversionDetail> getDetails() { return details; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof LookupResult)) return false;
        LookupResult r = (LookupResult) o;
        return changed == r.changed
                && Objects.equals(input, r.input)
                && Objects.equals(output, r.output)
                && Objects.equals(details, r.details);
    }

    @Override
    public int hashCode() {
        return Objects.hash(input, output, changed, details);
    }

    @Override
    public String toString() {
        return "LookupResult{input='" + input + "', output='" + output
                + "', changed=" + changed + ", details=" + details + "}";
    }
}
