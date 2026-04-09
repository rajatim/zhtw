package com.rajatim.zhtw.benchmark;

import com.rajatim.zhtw.ZhtwConverter;
import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.results.format.ResultFormatType;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.Collections;
import java.util.concurrent.TimeUnit;

/**
 * JMH benchmarks for ZhtwConverter.
 *
 * <p>Run via:
 * <pre>
 *   cd sdk/java
 *   mvn package -P benchmark -DskipTests
 *   java -jar target/zhtw-benchmark.jar
 * </pre>
 *
 * <p>Or run specific benchmarks:
 * <pre>
 *   java -jar target/zhtw-benchmark.jar convertThroughput
 *   java -jar target/zhtw-benchmark.jar "check|lookup"
 * </pre>
 */
@BenchmarkMode({Mode.Throughput, Mode.AverageTime})
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
@Warmup(iterations = 3, time = 2)
@Measurement(iterations = 5, time = 2)
@Fork(2)
public class ZhtwBenchmark {

    private ZhtwConverter converter;

    /** Single sentence (~20 chars) — typical API call */
    private String shortText;

    /** Medium paragraph (~500 chars) — typical document paragraph */
    private String mediumText;

    /** Large text (~100K chars) — bulk conversion scenario */
    private String largeText;

    /** Text with supplementary plane characters */
    private String supplementaryText;

    @Setup(Level.Trial)
    public void setup() {
        converter = ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();

        // Short: single sentence with mixed term + char conversions
        // 这个服务器的内存不够，需要购买新的软件来优化数据库的性能。
        shortText = "\u8fd9\u4e2a\u670d\u52a1\u5668\u7684\u5185\u5b58\u4e0d\u591f\uff0c"
                + "\u9700\u8981\u8d2d\u4e70\u65b0\u7684\u8f6f\u4ef6\u6765\u4f18\u5316"
                + "\u6570\u636e\u5e93\u7684\u6027\u80fd\u3002";

        // Medium: repeat short text ~15 times to get ~500 chars
        StringBuilder sb = new StringBuilder(600);
        for (int i = 0; i < 15; i++) {
            sb.append(shortText);
        }
        mediumText = sb.toString();

        // Large: repeat short text to get ~100K chars
        sb = new StringBuilder(110_000);
        String base = shortText;
        while (sb.length() < 100_000) {
            sb.append(base);
        }
        largeText = sb.toString();

        // Supplementary: text with non-BMP chars interspersed
        // 𠀀软件𠀁数据库𠀂服务器
        supplementaryText = "\uD840\uDC00\u8f6f\u4ef6\uD840\uDC01\u6570\u636e\u5e93\uD840\uDC02\u670d\u52a1\u5668";
    }

    // === convert() benchmarks ===

    @Benchmark
    public String convertShort() {
        return converter.convert(shortText);
    }

    @Benchmark
    public String convertMedium() {
        return converter.convert(mediumText);
    }

    @Benchmark
    public String convertLarge() {
        return converter.convert(largeText);
    }

    @Benchmark
    public String convertSupplementary() {
        return converter.convert(supplementaryText);
    }

    // === check() benchmarks ===

    @Benchmark
    public Object checkShort() {
        return converter.check(shortText);
    }

    @Benchmark
    public Object checkMedium() {
        return converter.check(mediumText);
    }

    // === lookup() benchmarks ===

    @Benchmark
    public Object lookupShort() {
        return converter.lookup(shortText);
    }

    @Benchmark
    public Object lookupSupplementary() {
        return converter.lookup(supplementaryText);
    }

    // === Initialization benchmark ===

    @Benchmark
    @BenchmarkMode(Mode.SingleShotTime)
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    @Fork(5)
    @Warmup(iterations = 0)
    @Measurement(iterations = 1)
    public ZhtwConverter initConverter() {
        return ZhtwConverter.builder()
                .sources(Collections.singletonList("cn"))
                .build();
    }

    /** Convenience main — allows `java -jar zhtw-benchmark.jar` */
    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder()
                .include(ZhtwBenchmark.class.getSimpleName())
                .resultFormat(ResultFormatType.TEXT)
                .build();
        new Runner(opt).run();
    }
}
