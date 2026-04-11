// zhtw:disable
// TypeScript SDK benchmark
import { readFileSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ITERATIONS = 10_000;

const raw = readFileSync(join(__dirname, "input.txt"), "utf-8");
const text = raw
  .split("\n")
  .filter((l) => !l.startsWith("#"))
  .join("")
  .trim();

// Cold start (includes require + first convert)
const t0 = process.hrtime.bigint();
const { convert } = await import(join(__dirname, "..", "sdk", "typescript", "dist", "index.node.mjs"));
const result = convert(text);
const coldNs = Number(process.hrtime.bigint() - t0);

// Warm throughput
const t1 = process.hrtime.bigint();
for (let i = 0; i < ITERATIONS; i++) {
  convert(text);
}
const warmTotalNs = Number(process.hrtime.bigint() - t1);

console.log(
  JSON.stringify(
    {
      sdk: "typescript",
      version: "4.3.0",
      input_chars: [...text].length,
      iterations: ITERATIONS,
      cold_start_ns: coldNs,
      warm_total_ns: warmTotalNs,
      warm_avg_ns: Math.floor(warmTotalNs / ITERATIONS),
      ops_per_sec: Math.floor(ITERATIONS / (warmTotalNs / 1e9)),
      output_sample: [...result].slice(0, 20).join(""),
    },
    null,
    2
  )
);
