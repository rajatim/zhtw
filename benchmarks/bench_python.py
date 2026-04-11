# zhtw:disable
"""Python SDK benchmark."""

import json
import os
import time

ITERATIONS = 10000
INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")


def main():
    with open(INPUT_FILE, encoding="utf-8") as f:
        lines = [line for line in f.readlines() if not line.startswith("#")]
    text = "".join(lines).strip()

    # Cold start (includes import + first convert)
    t0 = time.perf_counter()
    from zhtw import convert

    result = convert(text)
    cold_ns = int((time.perf_counter() - t0) * 1e9)

    # Warm throughput
    t0 = time.perf_counter()
    for _ in range(ITERATIONS):
        convert(text)
    warm_total_ns = int((time.perf_counter() - t0) * 1e9)

    print(
        json.dumps(
            {
                "sdk": "python",
                "version": __import__("zhtw").__version__,
                "input_chars": len(text),
                "iterations": ITERATIONS,
                "cold_start_ns": cold_ns,
                "warm_total_ns": warm_total_ns,
                "warm_avg_ns": warm_total_ns // ITERATIONS,
                "ops_per_sec": int(ITERATIONS / (warm_total_ns / 1e9)),
                "output_sample": result[:20],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
