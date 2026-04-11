using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using Xunit;

namespace Zhtw.Tests
{
    public class GoldenTests
    {
        private static readonly JsonDocument _golden;

        static GoldenTests()
        {
            // Navigate from bin output to sdk/data/golden-test.json
            string dir = AppDomain.CurrentDomain.BaseDirectory;
            string path = Path.GetFullPath(Path.Combine(dir, "..", "..", "..", "..", "..", "..", "data", "golden-test.json"));
            string json = File.ReadAllText(path);
            _golden = JsonDocument.Parse(json);
        }

        private static Converter BuildConverter(JsonElement testCase)
        {
            var builder = new ConverterBuilder();

            var sourcesArr = testCase.GetProperty("sources");
            var sources = new List<Source>();
            foreach (var s in sourcesArr.EnumerateArray())
            {
                switch (s.GetString())
                {
                    case "cn": sources.Add(Source.Cn); break;
                    case "hk": sources.Add(Source.Hk); break;
                }
            }
            builder.Sources(sources.ToArray());

            if (testCase.TryGetProperty("ambiguity_mode", out var modeEl))
            {
                switch (modeEl.GetString())
                {
                    case "balanced": builder.AmbiguityMode(AmbiguityMode.Balanced); break;
                    case "strict": builder.AmbiguityMode(AmbiguityMode.Strict); break;
                }
            }

            return builder.Build();
        }

        [Fact]
        public void ConvertGolden()
        {
            foreach (var tc in _golden.RootElement.GetProperty("convert").EnumerateArray())
            {
                string input = tc.GetProperty("input").GetString();
                string expected = tc.GetProperty("expected").GetString();
                var conv = BuildConverter(tc);

                string actual = conv.Convert(input);
                Assert.True(actual == expected,
                    $"Convert(\"{input}\"): expected \"{expected}\", got \"{actual}\"");
            }
        }

        [Fact]
        public void CheckGolden()
        {
            foreach (var tc in _golden.RootElement.GetProperty("check").EnumerateArray())
            {
                string input = tc.GetProperty("input").GetString();
                var conv = BuildConverter(tc);
                var actual = conv.Check(input);

                var expectedArr = tc.GetProperty("expected_matches").EnumerateArray().ToList();
                Assert.True(actual.Count == expectedArr.Count,
                    $"Check(\"{input}\"): expected {expectedArr.Count} matches, got {actual.Count}");

                for (int i = 0; i < expectedArr.Count; i++)
                {
                    var e = expectedArr[i];
                    int eStart = e.GetProperty("start").GetInt32();
                    int eEnd = e.GetProperty("end").GetInt32();
                    string eSource = e.GetProperty("source").GetString();
                    string eTarget = e.GetProperty("target").GetString();

                    Assert.True(actual[i].Start == eStart,
                        $"Check(\"{input}\")[{i}].Start: expected {eStart}, got {actual[i].Start}");
                    Assert.True(actual[i].End == eEnd,
                        $"Check(\"{input}\")[{i}].End: expected {eEnd}, got {actual[i].End}");
                    Assert.True(actual[i].Source == eSource,
                        $"Check(\"{input}\")[{i}].Source: expected \"{eSource}\", got \"{actual[i].Source}\"");
                    Assert.True(actual[i].Target == eTarget,
                        $"Check(\"{input}\")[{i}].Target: expected \"{eTarget}\", got \"{actual[i].Target}\"");
                }
            }
        }

        [Fact]
        public void LookupGolden()
        {
            foreach (var tc in _golden.RootElement.GetProperty("lookup").EnumerateArray())
            {
                string input = tc.GetProperty("input").GetString();
                var conv = BuildConverter(tc);
                var actual = conv.Lookup(input);

                string expectedOutput = tc.GetProperty("expected_output").GetString();
                bool expectedChanged = tc.GetProperty("expected_changed").GetBoolean();

                Assert.True(actual.Output == expectedOutput,
                    $"Lookup(\"{input}\").Output: expected \"{expectedOutput}\", got \"{actual.Output}\"");
                Assert.True(actual.Changed == expectedChanged,
                    $"Lookup(\"{input}\").Changed: expected {expectedChanged}, got {actual.Changed}");

                var expectedDetails = tc.GetProperty("expected_details").EnumerateArray().ToList();
                Assert.True(actual.Details.Count == expectedDetails.Count,
                    $"Lookup(\"{input}\"): expected {expectedDetails.Count} details, got {actual.Details.Count}");

                for (int i = 0; i < expectedDetails.Count; i++)
                {
                    var e = expectedDetails[i];
                    string eSource = e.GetProperty("source").GetString();
                    string eTarget = e.GetProperty("target").GetString();
                    string eLayer = e.GetProperty("layer").GetString();
                    int ePos = e.GetProperty("position").GetInt32();

                    Assert.True(actual.Details[i].Source == eSource,
                        $"Lookup(\"{input}\").Details[{i}].Source: expected \"{eSource}\", got \"{actual.Details[i].Source}\"");
                    Assert.True(actual.Details[i].Target == eTarget,
                        $"Lookup(\"{input}\").Details[{i}].Target: expected \"{eTarget}\", got \"{actual.Details[i].Target}\"");
                    Assert.True(actual.Details[i].Layer == eLayer,
                        $"Lookup(\"{input}\").Details[{i}].Layer: expected \"{eLayer}\", got \"{actual.Details[i].Layer}\"");
                    Assert.True(actual.Details[i].Position == ePos,
                        $"Lookup(\"{input}\").Details[{i}].Position: expected {ePos}, got {actual.Details[i].Position}");
                }
            }
        }
    }
}
