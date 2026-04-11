// zhtw:disable
// C# SDK benchmark
using System.Diagnostics;
using Zhtw;

const int iterations = 10_000;

string inputPath = args.Length > 0 ? args[0] : "benchmarks/input.txt";
string raw = File.ReadAllText(inputPath);
string text = string.Join("", raw.Split('\n').Where(l => !l.StartsWith('#'))).Trim();

// Cold start
var sw = Stopwatch.StartNew();
string result = ZhtwConvert.Convert(text);
sw.Stop();
long coldNs = sw.Elapsed.Ticks * 100; // 1 tick = 100ns

// Warm throughput
sw.Restart();
for (int i = 0; i < iterations; i++)
{
    ZhtwConvert.Convert(text);
}
sw.Stop();
long warmTotalNs = sw.Elapsed.Ticks * 100;

int inputChars = text.EnumerateRunes().Count();
string sample = new string(result.EnumerateRunes().Take(20).SelectMany(r => r.ToString().ToCharArray()).ToArray());

Console.WriteLine($$"""
{
  "sdk": "csharp",
  "version": "{{ZhtwConvert.DataVersion}}",
  "input_chars": {{inputChars}},
  "iterations": {{iterations}},
  "cold_start_ns": {{coldNs}},
  "warm_total_ns": {{warmTotalNs}},
  "warm_avg_ns": {{warmTotalNs / iterations}},
  "ops_per_sec": {{(long)(iterations / (warmTotalNs / 1e9))}},
  "output_sample": "{{sample}}"
}
""");
