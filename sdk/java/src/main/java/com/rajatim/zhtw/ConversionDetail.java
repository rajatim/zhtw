package com.rajatim.zhtw;

import java.util.Objects;

public final class ConversionDetail {
    private final String source;
    private final String target;
    private final String layer;  // "term" or "char"
    private final int position;

    public ConversionDetail(String source, String target, String layer, int position) {
        this.source = source;
        this.target = target;
        this.layer = layer;
        this.position = position;
    }

    public String getSource() { return source; }
    public String getTarget() { return target; }
    public String getLayer() { return layer; }
    public int getPosition() { return position; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof ConversionDetail)) return false;
        ConversionDetail d = (ConversionDetail) o;
        return position == d.position
                && Objects.equals(source, d.source)
                && Objects.equals(target, d.target)
                && Objects.equals(layer, d.layer);
    }

    @Override
    public int hashCode() {
        return Objects.hash(source, target, layer, position);
    }

    @Override
    public String toString() {
        return "ConversionDetail{source='" + source + "', target='" + target
                + "', layer='" + layer + "', position=" + position + "}";
    }
}
