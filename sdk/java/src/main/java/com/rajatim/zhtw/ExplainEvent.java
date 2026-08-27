package com.rajatim.zhtw;

import com.google.gson.annotations.SerializedName;

import java.util.Objects;

/** One stable, privacy-minimal conversion explanation event. */
public final class ExplainEvent {
    @SerializedName("rule_id")
    private final String ruleId;
    private final String layer;
    private final String outcome;
    @SerializedName("input_start")
    private final int inputStart;
    @SerializedName("input_end")
    private final int inputEnd;
    @SerializedName("output_start")
    private final int outputStart;
    @SerializedName("output_end")
    private final int outputEnd;
    private final String source;
    private final String target;
    @SerializedName("reason_code")
    private final String reasonCode;

    public ExplainEvent(String ruleId, String layer, String outcome,
                        int inputStart, int inputEnd, int outputStart, int outputEnd,
                        String source, String target, String reasonCode) {
        this.ruleId = ruleId;
        this.layer = layer;
        this.outcome = outcome;
        this.inputStart = inputStart;
        this.inputEnd = inputEnd;
        this.outputStart = outputStart;
        this.outputEnd = outputEnd;
        this.source = source;
        this.target = target;
        this.reasonCode = reasonCode;
    }

    public String getRuleId() { return ruleId; }
    public String getLayer() { return layer; }
    public String getOutcome() { return outcome; }
    public int getInputStart() { return inputStart; }
    public int getInputEnd() { return inputEnd; }
    public int getOutputStart() { return outputStart; }
    public int getOutputEnd() { return outputEnd; }
    public String getSource() { return source; }
    public String getTarget() { return target; }
    public String getReasonCode() { return reasonCode; }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (!(other instanceof ExplainEvent)) return false;
        ExplainEvent event = (ExplainEvent) other;
        return inputStart == event.inputStart && inputEnd == event.inputEnd
                && outputStart == event.outputStart && outputEnd == event.outputEnd
                && Objects.equals(ruleId, event.ruleId)
                && Objects.equals(layer, event.layer)
                && Objects.equals(outcome, event.outcome)
                && Objects.equals(source, event.source)
                && Objects.equals(target, event.target)
                && Objects.equals(reasonCode, event.reasonCode);
    }

    @Override
    public int hashCode() {
        return Objects.hash(ruleId, layer, outcome, inputStart, inputEnd,
                outputStart, outputEnd, source, target, reasonCode);
    }
}
