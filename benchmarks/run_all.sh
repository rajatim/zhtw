#!/usr/bin/env bash
# zhtw:disable
# Cross-SDK benchmark runner
set -euo pipefail
cd "$(dirname "$0")/.."

RESULTS_DIR="benchmarks/results"
mkdir -p "$RESULTS_DIR"

echo "=== zhtw cross-SDK benchmark ==="
echo ""

# --- Python ---
echo "[1/5] Python..."
uv run python benchmarks/bench_python.py > "$RESULTS_DIR/python.json" 2>&1 && \
  echo "  OK" || echo "  FAILED"

# --- Java ---
echo "[2/5] Java..."
(
  cd sdk/java
  mvn -q compile -pl . --batch-mode 2>/dev/null
  mvn -q exec:java -pl . --batch-mode \
    -Dexec.mainClass="bench_java" \
    -Dexec.classpathScope=compile \
    -Dexec.args="../../benchmarks/input.txt" \
    -Dexec.sourceRoot="../../benchmarks" 2>/dev/null
) > "$RESULTS_DIR/java_raw.txt" 2>&1
# Java via direct javac is simpler
(
  cd sdk/java
  javac -cp target/classes ../../benchmarks/bench_java.java -d /tmp/zhtw-bench 2>/dev/null && \
  java -cp "target/classes:/tmp/zhtw-bench" bench_java "../../benchmarks/input.txt"
) > "$RESULTS_DIR/java.json" 2>&1 && echo "  OK" || echo "  FAILED (trying mvn approach)"

# --- TypeScript ---
echo "[3/5] TypeScript..."
(cd sdk/typescript && npm ls zhtw-js >/dev/null 2>&1 || npm install --silent 2>/dev/null)
NODE_PATH="sdk/typescript/node_modules" node benchmarks/bench_typescript.mjs > "$RESULTS_DIR/typescript.json" 2>&1 && \
  echo "  OK" || echo "  FAILED"

# --- Go ---
echo "[4/5] Go..."
(cd sdk/go && go run ../../benchmarks/bench_go.go "../../benchmarks/input.txt") > "$RESULTS_DIR/go.json" 2>&1 && \
  echo "  OK" || echo "  FAILED"

# --- Rust ---
echo "[5/5] Rust..."
(
  cd sdk/rust/zhtw
  cargo build --release --example bench_rust 2>/dev/null || \
  (mkdir -p examples && cp ../../../benchmarks/bench_rust.rs examples/bench_rust.rs && \
   cargo build --release --example bench_rust 2>/dev/null)
  cargo run --release --example bench_rust -- "../../../benchmarks/input.txt"
) > "$RESULTS_DIR/rust.json" 2>&1 && echo "  OK" || echo "  FAILED"

echo ""
echo "=== Results ==="
echo ""
printf "%-12s %10s %10s %10s\n" "SDK" "Cold (ms)" "Avg (us)" "Ops/sec"
printf "%-12s %10s %10s %10s\n" "---" "---" "---" "---"

for f in "$RESULTS_DIR"/*.json; do
  [ -f "$f" ] || continue
  sdk=$(python3 -c "import json; print(json.load(open('$f'))['sdk'])" 2>/dev/null) || continue
  cold=$(python3 -c "import json; print(f\"{json.load(open('$f'))['cold_start_ns']/1e6:.1f}\")" 2>/dev/null)
  avg=$(python3 -c "import json; print(f\"{json.load(open('$f'))['warm_avg_ns']/1e3:.1f}\")" 2>/dev/null)
  ops=$(python3 -c "import json; print(f\"{json.load(open('$f'))['ops_per_sec']:,}\")" 2>/dev/null)
  printf "%-12s %10s %10s %10s\n" "$sdk" "$cold" "$avg" "$ops"
done
