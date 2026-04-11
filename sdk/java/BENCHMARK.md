# Java SDK Benchmark Report

> JMH (Java Microbenchmark Harness) 壓力測試結果

## 測試環境

| 專案 | 規格 |
|------|------|
| JMH | 1.37 |
| JDK | 21.0.10 (OpenJDK 64-Bit Server VM) |
| Platform | macOS Darwin (Apple Silicon) |
| Date | 2026-04-09 |
| SDK Version | 4.2.0 |

## 測試設定

- Warmup: 3 iterations, 2s each
- Measurement: 5 iterations, 2s each
- Fork: 2 (initConverter: 5)
- Thread: 1

## 測試資料

| 名稱 | 大小 | 說明 |
|------|------|------|
| short | ~30 字元 | 單句（混合詞彙+字元轉換） |
| medium | ~450 字元 | 段落（short x15） |
| large | ~100K 字元 | 大量文字（批次場景） |
| supplementary | ~15 字元 | 含 supplementary plane 字元 |

## 結果摘要

### 吞吐量 (Throughput, ops/ms)

| Benchmark | Score | Error (99.9%) | 換算 |
|-----------|------:|------:|------|
| convertShort | 484.96 | ±17.55 | **~485K ops/sec** |
| convertMedium | 36.79 | ±0.63 | ~36.8K ops/sec |
| convertLarge | 0.179 | ±0.002 | ~179 ops/sec (**17.9 MB/s**) |
| convertSupplementary | 983.94 | ±14.10 | ~984K ops/sec |
| checkShort | 387.90 | ±3.43 | ~388K ops/sec |
| checkMedium | 20.88 | ±0.22 | ~20.9K ops/sec |
| lookupShort | 385.24 | ±5.02 | ~385K ops/sec |
| lookupSupplementary | 696.03 | ±71.72 | ~696K ops/sec |

### 延遲 (Average Time, ms/op)

| Benchmark | Avg | Error (99.9%) |
|-----------|----:|------:|
| convertShort | 0.002 | ±0.001 |
| convertMedium | 0.028 | ±0.001 |
| convertLarge | 5.534 | ±0.037 |
| convertSupplementary | 0.001 | ±0.001 |
| checkShort | 0.003 | ±0.001 |
| checkMedium | 0.048 | ±0.001 |
| lookupShort | 0.003 | ±0.001 |
| lookupSupplementary | 0.001 | ±0.001 |

### 初始化 (Single Shot)

| Benchmark | Mean | Error (99.9%) | p50 | p90 |
|-----------|-----:|------:|----:|----:|
| initConverter | 53.85 ms | ±17.95 | 52.47 ms | 60.29 ms |

## 分析

### 效能特徵

1. **單句延遲極低**：convert/check/lookup 短文字均在 2-3 微秒完成，適合即時 API 呼叫
2. **大量文字吞吐高**：100K 字元 convert 只需 5.5ms，換算 **~17.9 MB/s**
3. **線性擴充套件**：medium (450 chars) 28μs vs short (30 chars) 2μs，比例合理
4. **Supplementary plane 無額外開銷**：含非 BMP 字元的文字反而更快（因為文字更短）
5. **初始化一次性成本**：~54ms（載入 JSON + 建立 AC 自動機），singleton 設計確保只付一次

### 與 Python 版比較

| 指標 | Python (v3.1.0) | Java SDK | 倍數 |
|------|---------------:|----------:|-----:|
| 吞吐量 (1MB) | ~3.1 MB/s | ~17.9 MB/s | **~5.8x** |

> Python 在 v3.1.0 最佳化後達到 3,068 KB/s。Java SDK 得益於 JIT 編譯和原生 AC 庫，吞吐量約為 Python 的 5.8 倍。

## 執行方式

```bash
cd sdk/java

# 外帶 benchmark JAR
mvn package -P benchmark -DskipTests

# 執行全部 benchmark
java -jar target/zhtw-benchmark.jar

# 執行特定 benchmark
java -jar target/zhtw-benchmark.jar convertLarge
java -jar target/zhtw-benchmark.jar "check|lookup"

# 輸出結果到檔案
java -jar target/zhtw-benchmark.jar -rf text -rff target/benchmark-results.txt
```
