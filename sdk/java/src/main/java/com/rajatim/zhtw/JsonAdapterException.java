package com.rajatim.zhtw;

/** Raised when JSON cannot be converted without preserving its structure. */
public final class JsonAdapterException extends IllegalArgumentException {
    private final String code;

    JsonAdapterException(String message, String code) {
        super(message);
        this.code = code;
    }

    public String getCode() { return code; }
}
