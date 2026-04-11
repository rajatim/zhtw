// zhtw:disable
// Java SDK benchmark — compile and run from sdk/java
import com.rajatim.zhtw.ZhtwConverter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class bench_java {
    static final int ITERATIONS = 10_000;

    public static void main(String[] args) throws IOException {
        String raw = Files.readString(Path.of(args.length > 0 ? args[0] : "benchmarks/input.txt"));
        StringBuilder sb = new StringBuilder();
        for (String line : raw.split("\n")) {
            if (!line.startsWith("#")) sb.append(line);
        }
        String text = sb.toString().strip();

        // Cold start (includes singleton init)
        long t0 = System.nanoTime();
        ZhtwConverter conv = ZhtwConverter.getDefault();
        String result = conv.convert(text);
        long coldNs = System.nanoTime() - t0;

        // Warm throughput
        t0 = System.nanoTime();
        for (int i = 0; i < ITERATIONS; i++) {
            conv.convert(text);
        }
        long warmTotalNs = System.nanoTime() - t0;

        System.out.printf("""
        {
          "sdk": "java",
          "version": "4.3.0",
          "input_chars": %d,
          "iterations": %d,
          "cold_start_ns": %d,
          "warm_total_ns": %d,
          "warm_avg_ns": %d,
          "ops_per_sec": %d,
          "output_sample": "%s"
        }
        """,
            text.codePointCount(0, text.length()),
            ITERATIONS,
            coldNs,
            warmTotalNs,
            warmTotalNs / ITERATIONS,
            (long)(ITERATIONS / (warmTotalNs / 1e9)),
            result.substring(0, Math.min(20, result.length()))
        );
    }
}
