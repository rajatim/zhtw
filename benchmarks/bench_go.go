// zhtw:disable
// Go SDK benchmark
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/rajatim/zhtw/sdk/go/v4/zhtw"
)

const iterations = 10000

func main() {
	inputPath := filepath.Join("benchmarks", "input.txt")
	if len(os.Args) > 1 {
		inputPath = os.Args[1]
	}
	raw, err := os.ReadFile(inputPath)
	if err != nil {
		panic(err)
	}
	var sb strings.Builder
	for _, line := range strings.Split(string(raw), "\n") {
		if !strings.HasPrefix(line, "#") {
			sb.WriteString(line)
		}
	}
	text := strings.TrimSpace(sb.String())

	// Cold start
	t0 := time.Now()
	conv, err := zhtw.NewBuilder().Sources(zhtw.SourceCn, zhtw.SourceHk).Build()
	if err != nil {
		panic(err)
	}
	result := conv.Convert(text)
	coldNs := time.Since(t0).Nanoseconds()

	// Warm throughput
	t1 := time.Now()
	for i := 0; i < iterations; i++ {
		conv.Convert(text)
	}
	warmTotalNs := time.Since(t1).Nanoseconds()

	out := map[string]any{
		"sdk":           "go",
		"version":       zhtw.DataVersion(),
		"input_chars":   utf8.RuneCountInString(text),
		"iterations":    iterations,
		"cold_start_ns": coldNs,
		"warm_total_ns": warmTotalNs,
		"warm_avg_ns":   warmTotalNs / iterations,
		"ops_per_sec":   int64(float64(iterations) / (float64(warmTotalNs) / 1e9)),
		"output_sample": string([]rune(result)[:20]),
	}
	b, _ := json.MarshalIndent(out, "", "  ")
	fmt.Println(string(b))
}
