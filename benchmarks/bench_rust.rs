// zhtw:disable
// Rust SDK benchmark — compile from sdk/rust/zhtw
use std::env;
use std::fs;
use std::time::Instant;

fn main() {
    let input_path = env::args()
        .nth(1)
        .unwrap_or_else(|| "benchmarks/input.txt".to_string());
    let raw = fs::read_to_string(&input_path).expect("read input");
    let text: String = raw
        .lines()
        .filter(|l| !l.starts_with('#'))
        .collect::<Vec<_>>()
        .join("")
        .trim()
        .to_string();
    let iterations = 10_000u64;

    // Cold start
    let t0 = Instant::now();
    let converter = zhtw::Converter::builder()
        .sources([zhtw::Source::Cn, zhtw::Source::Hk])
        .build()
        .expect("build converter");
    let result = converter.convert(&text);
    let cold_ns = t0.elapsed().as_nanos() as u64;

    // Warm throughput
    let t1 = Instant::now();
    for _ in 0..iterations {
        let _ = converter.convert(&text);
    }
    let warm_total_ns = t1.elapsed().as_nanos() as u64;

    let sample: String = result.chars().take(20).collect();
    let input_chars = text.chars().count();

    println!(
        r#"{{
  "sdk": "rust",
  "version": "4.3.0",
  "input_chars": {},
  "iterations": {},
  "cold_start_ns": {},
  "warm_total_ns": {},
  "warm_avg_ns": {},
  "ops_per_sec": {},
  "output_sample": "{}"
}}"#,
        input_chars,
        iterations,
        cold_ns,
        warm_total_ns,
        warm_total_ns / iterations,
        (iterations as f64 / (warm_total_ns as f64 / 1e9)) as u64,
        sample,
    );
}
