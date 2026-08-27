package com.rajatim.zhtw;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Converted output and its ordered explanation events. */
public final class ExplainResult {
    private final String output;
    private final List<ExplainEvent> events;

    public ExplainResult(String output, List<ExplainEvent> events) {
        this.output = output;
        this.events = Collections.unmodifiableList(new ArrayList<>(events));
    }

    public String getOutput() { return output; }
    public List<ExplainEvent> getEvents() { return events; }
}
