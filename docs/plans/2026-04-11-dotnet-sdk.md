# zhtw:disable
# C# (.NET) SDK Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a fully-featured .NET SDK for zhtw with Convert/Check/Lookup APIs, multi-target netstandard2.0+net8.0, matching all other SDKs via golden tests.

**Architecture:** Embedded JSON data loaded via `System.Text.Json`, self-implemented Aho-Corasick automaton for term matching, three-layer conversion (term → balanced → char). Builder pattern for custom instances, `Lazy<Converter>` for thread-safe default.

**Tech Stack:** C# / .NET, `System.Text.Json`, xUnit, multi-target `netstandard2.0` + `net8.0`

---

## File Map

| File | Responsibility |
|------|----------------|
| `sdk/dotnet/Zhtw.csproj` | Modify: multi-target, embedded resource, System.Text.Json ref |
| `sdk/dotnet/src/Types.cs` | Create: Source, AmbiguityMode, Match, LookupResult, ConversionDetail |
| `sdk/dotnet/src/CodepointHelper.cs` | Create: UTF-16 ↔ codepoint index conversion |
| `sdk/dotnet/src/ZhtwData.cs` | Create: embedded resource loader + JSON parsing |
| `sdk/dotnet/src/AhoCorasick.cs` | Create: AC automaton (build trie, failure links, match selection) |
| `sdk/dotnet/src/Converter.cs` | Create: three-layer Convert + Check + Lookup |
| `sdk/dotnet/src/ConverterBuilder.cs` | Create: fluent builder |
| `sdk/dotnet/src/ZhtwConvert.cs` | Create: static convenience API + Lazy default |
| `sdk/dotnet/tests/Zhtw.Tests/Zhtw.Tests.csproj` | Create: xUnit test project |
| `sdk/dotnet/tests/Zhtw.Tests/AhoCorasickTests.cs` | Create: AC unit tests |
| `sdk/dotnet/tests/Zhtw.Tests/ConverterTests.cs` | Create: builder, custom dict, edge cases |
| `sdk/dotnet/tests/Zhtw.Tests/GoldenTests.cs` | Create: golden-test.json driven tests |
| `.github/workflows/sdk-dotnet.yml` | Modify: real build + test |

---

### Task 1: Project scaffolding + Types

**Files:**
- Modify: `sdk/dotnet/Zhtw.csproj`
- Create: `sdk/dotnet/src/Types.cs`
- Create: `sdk/dotnet/tests/Zhtw.Tests/Zhtw.Tests.csproj`

- [ ] **Step 1: Update Zhtw.csproj for multi-target + embedded resource**

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFrameworks>netstandard2.0;net8.0</TargetFrameworks>
    <RootNamespace>Zhtw</RootNamespace>
    <PackageId>Zhtw</PackageId>
    <Version>4.2.1</Version>
    <Description>Traditional Chinese converter for Taiwan — .NET SDK</Description>
    <PackageLicenseExpression>MIT</PackageLicenseExpression>
    <RepositoryUrl>https://github.com/rajatim/zhtw</RepositoryUrl>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>
  <ItemGroup>
    <EmbeddedResource Include="../data/zhtw-data.json" Link="zhtw-data.json" />
  </ItemGroup>
  <ItemGroup Condition="'$(TargetFramework)' == 'netstandard2.0'">
    <PackageReference Include="System.Text.Json" Version="8.0.5" />
  </ItemGroup>
</Project>
```

- [ ] **Step 2: Create src/Types.cs**

```csharp
namespace Zhtw
{
    public enum Source
    {
        Cn,
        Hk
    }

    public enum AmbiguityMode
    {
        Strict,
        Balanced
    }

    public sealed class Match
    {
        public int Start { get; }
        public int End { get; }
        public string Source { get; }
        public string Target { get; }

        internal Match(int start, int end, string source, string target)
        {
            Start = start;
            End = end;
            Source = source;
            Target = target;
        }
    }

    public sealed class LookupResult
    {
        public string Input { get; }
        public string Output { get; }
        public bool Changed { get; }
        public System.Collections.Generic.IReadOnlyList<ConversionDetail> Details { get; }

        internal LookupResult(string input, string output, bool changed,
            System.Collections.Generic.IReadOnlyList<ConversionDetail> details)
        {
            Input = input;
            Output = output;
            Changed = changed;
            Details = details;
        }
    }

    public sealed class ConversionDetail
    {
        public string Source { get; }
        public string Target { get; }
        public string Layer { get; }
        public int Position { get; }

        internal ConversionDetail(string source, string target, string layer, int position)
        {
            Source = source;
            Target = target;
            Layer = layer;
            Position = position;
        }
    }
}
```

- [ ] **Step 3: Create test project**

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <RootNamespace>Zhtw.Tests</RootNamespace>
    <IsPackable>false</IsPackable>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.11.1" />
    <PackageReference Include="xunit" Version="2.9.2" />
    <PackageReference Include="xunit.runner.visualstudio" Version="2.8.2" />
  </ItemGroup>
  <ItemGroup>
    <ProjectReference Include="../../Zhtw.csproj" />
  </ItemGroup>
</Project>
```

- [ ] **Step 4: Verify build compiles both targets**

Run: `cd sdk/dotnet && dotnet build -c Release`
Expected: Build Succeeded for both netstandard2.0 and net8.0

- [ ] **Step 5: Commit**

```bash
git add sdk/dotnet/Zhtw.csproj sdk/dotnet/src/Types.cs sdk/dotnet/tests/Zhtw.Tests/Zhtw.Tests.csproj
git commit -m "feat(dotnet): project scaffolding + Types — multi-target netstandard2.0+net8.0"
```

---

### Task 2: CodepointHelper + ZhtwData (embedded resource loader)

**Files:**
- Create: `sdk/dotnet/src/CodepointHelper.cs`
- Create: `sdk/dotnet/src/ZhtwData.cs`

- [ ] **Step 1: Create src/CodepointHelper.cs**

Handles conversion between .NET's UTF-16 string indices and Unicode codepoint indices.

```csharp
using System;
using System.Globalization;

namespace Zhtw
{
    internal static class CodepointHelper
    {
        internal static int[] ToCodepoints(string text)
        {
            var si = new StringInfo(text);
            int len = si.LengthInTextElements;
            int[] codepoints = new int[len];
            int charIndex = 0;
            for (int i = 0; i < len; i++)
            {
                codepoints[i] = char.ConvertToUtf32(text, charIndex);
                charIndex += char.IsSurrogatePair(text, charIndex) ? 2 : 1;
            }
            return codepoints;
        }

        internal static string FromCodepoints(int[] codepoints)
        {
            var sb = new System.Text.StringBuilder(codepoints.Length);
            foreach (int cp in codepoints)
            {
                sb.Append(char.ConvertFromUtf32(cp));
            }
            return sb.ToString();
        }

        internal static int CodepointLength(string text)
        {
            int count = 0;
            int i = 0;
            while (i < text.Length)
            {
                count++;
                i += char.IsSurrogatePair(text, i) ? 2 : 1;
            }
            return count;
        }
    }
}
```

- [ ] **Step 2: Create src/ZhtwData.cs**

Loads embedded `zhtw-data.json` and parses into optimized internal structures.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text.Json;

namespace Zhtw
{
    internal sealed class ZhtwData
    {
        internal string Version { get; }
        internal Dictionary<int, int> CharMap { get; }
        internal Dictionary<int, int> BalancedDefaults { get; }
        internal Dictionary<string, string> TermsCn { get; }
        internal Dictionary<string, string> TermsHk { get; }

        private ZhtwData(string version, Dictionary<int, int> charMap,
            Dictionary<int, int> balancedDefaults,
            Dictionary<string, string> termsCn, Dictionary<string, string> termsHk)
        {
            Version = version;
            CharMap = charMap;
            BalancedDefaults = balancedDefaults;
            TermsCn = termsCn;
            TermsHk = termsHk;
        }

        private static readonly Lazy<ZhtwData> _instance = new Lazy<ZhtwData>(Load);

        internal static ZhtwData Instance => _instance.Value;

        private static ZhtwData Load()
        {
            var assembly = typeof(ZhtwData).Assembly;
            string resourceName = null;
            foreach (var name in assembly.GetManifestResourceNames())
            {
                if (name.EndsWith("zhtw-data.json", StringComparison.Ordinal))
                {
                    resourceName = name;
                    break;
                }
            }
            if (resourceName == null)
                throw new InvalidOperationException("Embedded resource zhtw-data.json not found");

            using (var stream = assembly.GetManifestResourceStream(resourceName))
            using (var reader = new StreamReader(stream))
            {
                string json = reader.ReadToEnd();
                return Parse(json);
            }
        }

        private static ZhtwData Parse(string json)
        {
            using (var doc = JsonDocument.Parse(json))
            {
                var root = doc.RootElement;
                string version = root.GetProperty("version").GetString();

                var charmapEl = root.GetProperty("charmap");

                // Parse chars (single-codepoint only)
                var charMap = new Dictionary<int, int>();
                foreach (var prop in charmapEl.GetProperty("chars").EnumerateObject())
                {
                    int[] kCp = CodepointHelper.ToCodepoints(prop.Name);
                    int[] vCp = CodepointHelper.ToCodepoints(prop.Value.GetString());
                    if (kCp.Length == 1 && vCp.Length == 1)
                    {
                        charMap[kCp[0]] = vCp[0];
                    }
                }

                // Parse balanced_defaults (single-codepoint only)
                var balancedDefaults = new Dictionary<int, int>();
                if (charmapEl.TryGetProperty("balanced_defaults", out var bdEl))
                {
                    foreach (var prop in bdEl.EnumerateObject())
                    {
                        int[] kCp = CodepointHelper.ToCodepoints(prop.Name);
                        int[] vCp = CodepointHelper.ToCodepoints(prop.Value.GetString());
                        if (kCp.Length == 1 && vCp.Length == 1)
                        {
                            balancedDefaults[kCp[0]] = vCp[0];
                        }
                    }
                }

                // Parse terms
                var termsEl = root.GetProperty("terms");
                var termsCn = ParseTerms(termsEl, "cn");
                var termsHk = ParseTerms(termsEl, "hk");

                return new ZhtwData(version, charMap, balancedDefaults, termsCn, termsHk);
            }
        }

        private static Dictionary<string, string> ParseTerms(JsonElement termsEl, string key)
        {
            var dict = new Dictionary<string, string>();
            if (termsEl.TryGetProperty(key, out var srcEl))
            {
                foreach (var prop in srcEl.EnumerateObject())
                {
                    if (prop.Name.Length > 0)
                    {
                        dict[prop.Name] = prop.Value.GetString();
                    }
                }
            }
            return dict;
        }
    }
}
```

- [ ] **Step 3: Verify build**

Run: `cd sdk/dotnet && dotnet build -c Release`
Expected: Build Succeeded

- [ ] **Step 4: Commit**

```bash
git add sdk/dotnet/src/CodepointHelper.cs sdk/dotnet/src/ZhtwData.cs
git commit -m "feat(dotnet): CodepointHelper + ZhtwData — embedded JSON loader"
```

---

### Task 3: Aho-Corasick automaton + unit tests

**Files:**
- Create: `sdk/dotnet/src/AhoCorasick.cs`
- Create: `sdk/dotnet/tests/Zhtw.Tests/AhoCorasickTests.cs`

- [ ] **Step 1: Create AhoCorasickTests.cs (tests first)**

```csharp
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace Zhtw.Tests
{
    public class AhoCorasickTests
    {
        [Fact]
        public void BasicMatch()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("he", "HE"),
                new AcPattern("she", "SHE"),
                new AcPattern("his", "HIS"),
                new AcPattern("hers", "HERS"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("ushers");
            Assert.Equal(2, matches.Count);
            Assert.Equal("she", matches[0].Source);
            Assert.Equal(1, matches[0].Start);
            Assert.Equal("hers", matches[1].Source);
            Assert.Equal(2, matches[1].Start);
        }

        [Fact]
        public void CjkMatch()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("软件", "軟體"),
                new AcPattern("测试", "測試"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("软件测试");
            Assert.Equal(2, matches.Count);
            Assert.Equal("软件", matches[0].Source);
            Assert.Equal(0, matches[0].Start);
            Assert.Equal(2, matches[0].End);
            Assert.Equal("测试", matches[1].Source);
            Assert.Equal(2, matches[1].Start);
            Assert.Equal(4, matches[1].End);
        }

        [Fact]
        public void IdentityProtection()
        {
            // "檔案" is identity (protects positions 0-1).
            // "案件" is non-identity but overlaps position 1.
            // Protection should prevent "案件" from matching.
            var patterns = new List<AcPattern>
            {
                new AcPattern("檔案", "檔案"),  // identity
                new AcPattern("案件", "案件X"),   // non-identity
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("檔案件");
            Assert.Empty(matches); // identity doesn't emit, non-identity blocked
        }

        [Fact]
        public void EmptyInput()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("ab", "AB"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("");
            Assert.Empty(matches);
        }

        [Fact]
        public void CoveredPositionsIncludesIdentity()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("皇后", "皇后"),  // identity
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var covered = ac.GetCoveredPositions("皇后很美");
            Assert.Contains(0, covered);
            Assert.Contains(1, covered);
            Assert.DoesNotContain(2, covered);
            Assert.DoesNotContain(3, covered);
        }

        [Fact]
        public void LongestMatchWins()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("云", "雲"),
                new AcPattern("云计算", "雲端運算"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("云计算");
            Assert.Single(matches);
            Assert.Equal("云计算", matches[0].Source);
            Assert.Equal("雲端運算", matches[0].Target);
        }
    }
}
```

- [ ] **Step 2: Create src/AhoCorasick.cs**

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Zhtw
{
    internal sealed class AcPattern
    {
        internal string Source { get; }
        internal string Target { get; }
        internal int CodepointLength { get; }

        internal AcPattern(string source, string target)
        {
            Source = source;
            Target = target;
            CodepointLength = CodepointHelper.CodepointLength(source);
        }
    }

    internal sealed class AcMatch
    {
        internal int Start { get; }
        internal int End { get; }
        internal string Source { get; }
        internal string Target { get; }

        internal AcMatch(int start, int end, string source, string target)
        {
            Start = start;
            End = end;
            Source = source;
            Target = target;
        }
    }

    internal sealed class AcNode
    {
        internal Dictionary<int, AcNode> Children = new Dictionary<int, AcNode>();
        internal AcNode Fail;
        internal List<int> Outputs = new List<int>();
    }

    internal sealed class AhoCorasickAutomaton
    {
        private readonly AcNode _root;
        private readonly List<AcPattern> _patterns;

        private AhoCorasickAutomaton(AcNode root, List<AcPattern> patterns)
        {
            _root = root;
            _patterns = patterns;
        }

        internal static AhoCorasickAutomaton Build(List<AcPattern> patterns)
        {
            // Sort for deterministic automaton.
            patterns = patterns.OrderBy(p => p.Source, StringComparer.Ordinal).ToList();

            var root = new AcNode();

            // Insert patterns into trie.
            for (int idx = 0; idx < patterns.Count; idx++)
            {
                var node = root;
                int[] codepoints = CodepointHelper.ToCodepoints(patterns[idx].Source);
                foreach (int cp in codepoints)
                {
                    if (!node.Children.TryGetValue(cp, out var next))
                    {
                        next = new AcNode();
                        node.Children[cp] = next;
                    }
                    node = next;
                }
                node.Outputs.Add(idx);
            }

            // Build failure links (BFS).
            var queue = new Queue<AcNode>();
            foreach (var child in root.Children.Values)
            {
                child.Fail = root;
                queue.Enqueue(child);
            }
            while (queue.Count > 0)
            {
                var node = queue.Dequeue();
                foreach (var kvp in node.Children)
                {
                    int cp = kvp.Key;
                    var child = kvp.Value;
                    queue.Enqueue(child);

                    var f = node.Fail;
                    while (f != null && !f.Children.ContainsKey(cp))
                    {
                        f = f.Fail;
                    }
                    child.Fail = (f != null && f.Children.TryGetValue(cp, out var target))
                        ? target : root;

                    // Merge output-link patterns from fail node.
                    if (child.Fail.Outputs.Count > 0)
                    {
                        var merged = new List<int>(child.Outputs.Count + child.Fail.Outputs.Count);
                        merged.AddRange(child.Outputs);
                        merged.AddRange(child.Fail.Outputs);
                        child.Outputs = merged;
                    }
                }
            }

            return new AhoCorasickAutomaton(root, patterns);
        }

        private List<AcMatch> IterEmissions(int[] codepoints)
        {
            var hits = new List<AcMatch>();
            var node = _root;
            for (int i = 0; i < codepoints.Length; i++)
            {
                int cp = codepoints[i];
                while (node != _root && !node.Children.ContainsKey(cp))
                {
                    node = node.Fail;
                }
                if (node.Children.TryGetValue(cp, out var next))
                {
                    node = next;
                }
                foreach (int idx in node.Outputs)
                {
                    var pat = _patterns[idx];
                    int start = i + 1 - pat.CodepointLength;
                    hits.Add(new AcMatch(start, i + 1, pat.Source, pat.Target));
                }
            }
            return hits;
        }

        internal HashSet<int> GetCoveredPositions(string text)
        {
            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var covered = new HashSet<int>();
            foreach (var m in IterEmissions(codepoints))
            {
                for (int i = m.Start; i < m.End; i++)
                    covered.Add(i);
            }
            return covered;
        }

        internal List<AcMatch> FindTermMatches(string text)
        {
            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var raw = IterEmissions(codepoints);
            if (raw.Count == 0)
                return new List<AcMatch>();

            // Sort by (start ASC, length DESC).
            raw.Sort((a, b) =>
            {
                int cmp = a.Start.CompareTo(b.Start);
                if (cmp != 0) return cmp;
                int lenA = a.End - a.Start;
                int lenB = b.End - b.Start;
                return lenB.CompareTo(lenA); // longer first
            });

            // Separate identity and non-identity hits.
            var identity = new List<AcMatch>();
            var nonIdentitySpans = new List<int[]>(); // [start, end]
            foreach (var m in raw)
            {
                if (m.Source == m.Target)
                    identity.Add(m);
                else
                    nonIdentitySpans.Add(new[] { m.Start, m.End });
            }

            // Build protected positions.
            var protectedPos = new HashSet<int>();
            if (nonIdentitySpans.Count == 0)
            {
                foreach (var m in identity)
                    for (int i = m.Start; i < m.End; i++)
                        protectedPos.Add(i);
            }
            else
            {
                nonIdentitySpans.Sort((a, b) => a[0].CompareTo(b[0]));
                // Build prefix-max-end array.
                int[] prefixMaxEnd = new int[nonIdentitySpans.Count];
                int maxEnd = 0;
                for (int i = 0; i < nonIdentitySpans.Count; i++)
                {
                    if (nonIdentitySpans[i][1] > maxEnd) maxEnd = nonIdentitySpans[i][1];
                    prefixMaxEnd[i] = maxEnd;
                }
                int[] niStarts = nonIdentitySpans.Select(s => s[0]).ToArray();

                foreach (var m in identity)
                {
                    int idx = BisectRight(niStarts, m.Start) - 1;
                    bool contained = idx >= 0 && prefixMaxEnd[idx] >= m.End;
                    if (!contained)
                    {
                        for (int i = m.Start; i < m.End; i++)
                            protectedPos.Add(i);
                    }
                }
            }

            // Left-to-right greedy filter.
            var result = new List<AcMatch>();
            int cursor = 0;
            foreach (var m in raw)
            {
                if (m.Start < cursor) continue;
                bool isIdentity = m.Source == m.Target;
                if (!isIdentity)
                {
                    bool overlaps = false;
                    for (int i = m.Start; i < m.End; i++)
                    {
                        if (protectedPos.Contains(i)) { overlaps = true; break; }
                    }
                    if (overlaps) continue;
                }
                cursor = m.End;
                if (!isIdentity)
                    result.Add(m);
            }
            return result;
        }

        private static int BisectRight(int[] sorted, int value)
        {
            int lo = 0, hi = sorted.Length;
            while (lo < hi)
            {
                int mid = (lo + hi) / 2;
                if (sorted[mid] <= value) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
    }
}
```

- [ ] **Step 3: Run tests**

Run: `cd sdk/dotnet && dotnet test -c Release --logger "console;verbosity=detailed"`
Expected: 6 tests pass

- [ ] **Step 4: Commit**

```bash
git add sdk/dotnet/src/AhoCorasick.cs sdk/dotnet/tests/Zhtw.Tests/AhoCorasickTests.cs
git commit -m "feat(dotnet): Aho-Corasick automaton + 6 unit tests"
```

---

### Task 4: Converter (Convert + Check + Lookup)

**Files:**
- Create: `sdk/dotnet/src/Converter.cs`
- Create: `sdk/dotnet/tests/Zhtw.Tests/ConverterTests.cs`

- [ ] **Step 1: Create ConverterTests.cs (tests first)**

```csharp
using System;
using System.Collections.Generic;
using Xunit;

namespace Zhtw.Tests
{
    public class ConverterTests
    {
        [Fact]
        public void ConvertBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Equal("軟體測試", conv.Convert("软件测试"));
        }

        [Fact]
        public void ConvertEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Equal("", conv.Convert(""));
            Assert.Equal("", conv.Convert(null));
        }

        [Fact]
        public void CheckBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var matches = conv.Check("软件测试");
            Assert.Equal(2, matches.Count);
            Assert.Equal("软件", matches[0].Source);
            Assert.Equal("軟體", matches[0].Target);
            Assert.Equal(0, matches[0].Start);
            Assert.Equal(2, matches[0].End);
        }

        [Fact]
        public void CheckEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Empty(conv.Check(""));
            Assert.Empty(conv.Check(null));
        }

        [Fact]
        public void LookupBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup("软件");
            Assert.Equal("软件", result.Input);
            Assert.Equal("軟體", result.Output);
            Assert.True(result.Changed);
            Assert.Single(result.Details);
            Assert.Equal("term", result.Details[0].Layer);
        }

        [Fact]
        public void LookupEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup("");
            Assert.Equal("", result.Input);
            Assert.Equal("", result.Output);
            Assert.False(result.Changed);
            Assert.Empty(result.Details);
        }

        [Fact]
        public void LookupNull()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup(null);
            Assert.Equal("", result.Input);
            Assert.Equal("", result.Output);
            Assert.False(result.Changed);
            Assert.Empty(result.Details);
        }

        [Fact]
        public void CustomDictOverride()
        {
            var conv = new ConverterBuilder()
                .Sources(Source.Cn)
                .CustomDict(new Dictionary<string, string> { { "软件", "軟件" } })
                .Build();
            Assert.Equal("軟件", conv.Convert("软件"));
        }

        [Fact]
        public void BalancedMode()
        {
            var conv = new ConverterBuilder()
                .Sources(Source.Cn)
                .AmbiguityMode(AmbiguityMode.Balanced)
                .Build();
            // "以后" should become "以後" in balanced mode
            Assert.Equal("以後再說", conv.Convert("以后再说"));
            // "皇后" should be protected — not converted
            Assert.Equal("皇后很美", conv.Convert("皇后很美"));
        }

        [Fact]
        public void HkSource()
        {
            var conv = new ConverterBuilder().Sources(Source.Hk).Build();
            Assert.Equal("軟體工程師", conv.Convert("軟件工程師"));
        }
    }
}
```

- [ ] **Step 2: Create src/Converter.cs**

```csharp
using System;
using System.Collections.Generic;
using System.Text;

namespace Zhtw
{
    public sealed class Converter
    {
        private readonly AhoCorasickAutomaton _ac;
        private readonly Dictionary<int, int> _charMap;
        private readonly Dictionary<int, int> _balancedDefaults; // null for strict
        private readonly bool _charLayerEnabled;

        internal Converter(AhoCorasickAutomaton ac, Dictionary<int, int> charMap,
            Dictionary<int, int> balancedDefaults, bool charLayerEnabled)
        {
            _ac = ac;
            _charMap = charMap;
            _balancedDefaults = balancedDefaults;
            _charLayerEnabled = charLayerEnabled;
        }

        public string Convert(string text)
        {
            if (string.IsNullOrEmpty(text)) return "";

            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var covered = _ac.GetCoveredPositions(text);
            var hits = _ac.FindTermMatches(text);
            bool layersEnabled = _charLayerEnabled || _balancedDefaults != null;

            if (hits.Count == 0)
            {
                if (layersEnabled)
                    return ApplyLayers(codepoints, covered, 0);
                return text;
            }

            var buf = new StringBuilder(text.Length);
            int lastEnd = 0;
            foreach (var h in hits)
            {
                // Gap before this match.
                if (h.Start > lastEnd)
                {
                    int[] gap = Slice(codepoints, lastEnd, h.Start);
                    if (layersEnabled)
                        buf.Append(ApplyLayers(gap, covered, lastEnd));
                    else
                        buf.Append(CodepointHelper.FromCodepoints(gap));
                }
                buf.Append(h.Target);
                lastEnd = h.End;
            }
            // Tail after last match.
            if (lastEnd < codepoints.Length)
            {
                int[] tail = Slice(codepoints, lastEnd, codepoints.Length);
                if (layersEnabled)
                    buf.Append(ApplyLayers(tail, covered, lastEnd));
                else
                    buf.Append(CodepointHelper.FromCodepoints(tail));
            }
            return buf.ToString();
        }

        public IReadOnlyList<Match> Check(string text)
        {
            if (string.IsNullOrEmpty(text)) return Array.Empty<Match>();

            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var covered = _ac.GetCoveredPositions(text);
            var hits = _ac.FindTermMatches(text);

            var matches = new List<Match>();

            // 1. Term layer.
            foreach (var h in hits)
            {
                matches.Add(new Match(h.Start, h.End, h.Source, h.Target));
            }

            // 2. Balanced defaults layer.
            if (_balancedDefaults != null)
            {
                for (int i = 0; i < codepoints.Length; i++)
                {
                    if (covered.Contains(i)) continue;
                    if (_balancedDefaults.TryGetValue(codepoints[i], out int mapped))
                    {
                        matches.Add(new Match(i, i + 1,
                            char.ConvertFromUtf32(codepoints[i]),
                            char.ConvertFromUtf32(mapped)));
                    }
                }
            }

            // 3. Char layer.
            if (_charLayerEnabled)
            {
                for (int i = 0; i < codepoints.Length; i++)
                {
                    if (covered.Contains(i)) continue;
                    if (_charMap.TryGetValue(codepoints[i], out int mapped) && mapped != codepoints[i])
                    {
                        matches.Add(new Match(i, i + 1,
                            char.ConvertFromUtf32(codepoints[i]),
                            char.ConvertFromUtf32(mapped)));
                    }
                }
            }

            return matches;
        }

        public LookupResult Lookup(string word)
        {
            if (string.IsNullOrEmpty(word))
                return new LookupResult("", "", false, Array.Empty<ConversionDetail>());

            int[] codepoints = CodepointHelper.ToCodepoints(word);
            var covered = _ac.GetCoveredPositions(word);
            var hits = _ac.FindTermMatches(word);

            var details = new List<ConversionDetail>();

            // 1. Term layer.
            foreach (var h in hits)
            {
                details.Add(new ConversionDetail(h.Source, h.Target, "term", h.Start));
            }

            // 2. Balanced defaults layer.
            if (_balancedDefaults != null)
            {
                for (int i = 0; i < codepoints.Length; i++)
                {
                    if (covered.Contains(i)) continue;
                    if (_balancedDefaults.TryGetValue(codepoints[i], out int mapped))
                    {
                        details.Add(new ConversionDetail(
                            char.ConvertFromUtf32(codepoints[i]),
                            char.ConvertFromUtf32(mapped),
                            "char", i));
                    }
                }
            }

            // 3. Char layer.
            if (_charLayerEnabled)
            {
                for (int i = 0; i < codepoints.Length; i++)
                {
                    if (covered.Contains(i)) continue;
                    if (_charMap.TryGetValue(codepoints[i], out int mapped) && mapped != codepoints[i])
                    {
                        details.Add(new ConversionDetail(
                            char.ConvertFromUtf32(codepoints[i]),
                            char.ConvertFromUtf32(mapped),
                            "char", i));
                    }
                }
            }

            // Sort by position (ascending).
            details.Sort((a, b) => a.Position.CompareTo(b.Position));

            string output = Convert(word);
            bool changed = output != word;

            return new LookupResult(word, output, changed, details);
        }

        private string ApplyLayers(int[] codepoints, HashSet<int> covered, int offset)
        {
            var buf = new StringBuilder(codepoints.Length * 3);
            for (int i = 0; i < codepoints.Length; i++)
            {
                int cp = codepoints[i];
                if (covered.Contains(offset + i))
                {
                    buf.Append(char.ConvertFromUtf32(cp));
                    continue;
                }
                int outCp = cp;
                // Balanced defaults first.
                if (_balancedDefaults != null && _balancedDefaults.TryGetValue(cp, out int bd))
                {
                    outCp = bd;
                }
                // Charmap second (only if balanced didn't change it).
                if (outCp == cp && _charLayerEnabled && _charMap.TryGetValue(cp, out int cm))
                {
                    outCp = cm;
                }
                buf.Append(char.ConvertFromUtf32(outCp));
            }
            return buf.ToString();
        }

        private static int[] Slice(int[] arr, int start, int end)
        {
            int[] result = new int[end - start];
            Array.Copy(arr, start, result, 0, result.Length);
            return result;
        }
    }
}
```

- [ ] **Step 3: Run tests**

Run: `cd sdk/dotnet && dotnet test -c Release --logger "console;verbosity=detailed"`
Expected: All converter tests pass (10 new + 6 AC = 16 total)

- [ ] **Step 4: Commit**

```bash
git add sdk/dotnet/src/Converter.cs sdk/dotnet/tests/Zhtw.Tests/ConverterTests.cs
git commit -m "feat(dotnet): Converter — three-layer Convert/Check/Lookup"
```

---

### Task 5: ConverterBuilder + ZhtwConvert static API

**Files:**
- Create: `sdk/dotnet/src/ConverterBuilder.cs`
- Create: `sdk/dotnet/src/ZhtwConvert.cs`

- [ ] **Step 1: Create src/ConverterBuilder.cs**

```csharp
using System;
using System.Collections.Generic;

namespace Zhtw
{
    public sealed class ConverterBuilder
    {
        private Source[] _sources = { Source.Cn, Source.Hk };
        private AmbiguityMode _ambiguityMode = AmbiguityMode.Strict;
        private IReadOnlyDictionary<string, string> _customDict;

        public ConverterBuilder Sources(params Source[] sources)
        {
            _sources = sources;
            return this;
        }

        public ConverterBuilder AmbiguityMode(AmbiguityMode mode)
        {
            _ambiguityMode = mode;
            return this;
        }

        public ConverterBuilder CustomDict(IReadOnlyDictionary<string, string> dict)
        {
            _customDict = dict;
            return this;
        }

        public Converter Build()
        {
            if (_sources == null || _sources.Length == 0)
                throw new ArgumentException("Sources must not be empty.", nameof(_sources));

            var data = ZhtwData.Instance;

            // Merge terms from selected sources.
            var merged = new Dictionary<string, string>();
            foreach (var src in _sources)
            {
                Dictionary<string, string> bucket;
                switch (src)
                {
                    case Source.Cn: bucket = data.TermsCn; break;
                    case Source.Hk: bucket = data.TermsHk; break;
                    default: continue;
                }
                foreach (var kvp in bucket)
                {
                    if (kvp.Key.Length > 0)
                        merged[kvp.Key] = kvp.Value;
                }
            }

            // Custom dict overrides.
            if (_customDict != null)
            {
                foreach (var kvp in _customDict)
                {
                    if (kvp.Key.Length > 0)
                        merged[kvp.Key] = kvp.Value;
                }
            }

            // Build AC patterns.
            var patterns = new List<AcPattern>(merged.Count);
            foreach (var kvp in merged)
            {
                patterns.Add(new AcPattern(kvp.Key, kvp.Value));
            }
            var ac = AhoCorasickAutomaton.Build(patterns);

            bool hasCn = false;
            foreach (var s in _sources)
            {
                if (s == Source.Cn) { hasCn = true; break; }
            }

            Dictionary<int, int> balanced = null;
            if (_ambiguityMode == Zhtw.AmbiguityMode.Balanced && hasCn)
            {
                balanced = data.BalancedDefaults;
            }

            return new Converter(ac, data.CharMap, balanced, hasCn);
        }
    }
}
```

- [ ] **Step 2: Create src/ZhtwConvert.cs**

```csharp
using System;
using System.Collections.Generic;

namespace Zhtw
{
    public static class ZhtwConvert
    {
        private static readonly Lazy<Converter> _default =
            new Lazy<Converter>(() => new ConverterBuilder().Build());

        public static string DataVersion => ZhtwData.Instance.Version;

        public static string Convert(string text) => _default.Value.Convert(text);

        public static IReadOnlyList<Match> Check(string text) => _default.Value.Check(text);

        public static LookupResult Lookup(string word) => _default.Value.Lookup(word);
    }
}
```

- [ ] **Step 3: Add static API tests to ConverterTests.cs**

Append these tests to the existing `ConverterTests.cs`:

```csharp
        [Fact]
        public void StaticConvert()
        {
            Assert.Equal("軟體測試", ZhtwConvert.Convert("软件测试"));
        }

        [Fact]
        public void StaticCheck()
        {
            var matches = ZhtwConvert.Check("软件测试");
            Assert.Equal(2, matches.Count);
        }

        [Fact]
        public void StaticLookup()
        {
            var result = ZhtwConvert.Lookup("软件");
            Assert.True(result.Changed);
            Assert.Equal("軟體", result.Output);
        }

        [Fact]
        public void DataVersionNotEmpty()
        {
            Assert.False(string.IsNullOrEmpty(ZhtwConvert.DataVersion));
        }

        [Fact]
        public void EmptySourcesThrows()
        {
            Assert.Throws<ArgumentException>(() =>
                new ConverterBuilder().Sources().Build());
        }
```

- [ ] **Step 4: Run tests**

Run: `cd sdk/dotnet && dotnet test -c Release --logger "console;verbosity=detailed"`
Expected: All tests pass (16 previous + 5 new = 21 total)

- [ ] **Step 5: Commit**

```bash
git add sdk/dotnet/src/ConverterBuilder.cs sdk/dotnet/src/ZhtwConvert.cs sdk/dotnet/tests/Zhtw.Tests/ConverterTests.cs
git commit -m "feat(dotnet): ConverterBuilder + ZhtwConvert static API"
```

---

### Task 6: Golden tests

**Files:**
- Create: `sdk/dotnet/tests/Zhtw.Tests/GoldenTests.cs`

- [ ] **Step 1: Create GoldenTests.cs**

```csharp
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
            string path = Path.GetFullPath(Path.Combine(dir, "..", "..", "..", "..", "..", "data", "golden-test.json"));
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
```

- [ ] **Step 2: Run all tests**

Run: `cd sdk/dotnet && dotnet test -c Release --logger "console;verbosity=detailed"`
Expected: All tests pass (21 previous + 3 golden = 24 total). The golden tests cover 19 convert cases, 19 check cases, and 9 lookup cases all in 3 test methods.

- [ ] **Step 3: Commit**

```bash
git add sdk/dotnet/tests/Zhtw.Tests/GoldenTests.cs
git commit -m "test(dotnet): golden tests — convert/check/lookup parity with all SDKs"
```

---

### Task 7: CI workflow

**Files:**
- Modify: `.github/workflows/sdk-dotnet.yml`

- [ ] **Step 1: Update sdk-dotnet.yml**

```yaml
name: SDK .NET

on:
  push:
    paths: ['sdk/dotnet/**', 'sdk/data/**']
  pull_request:
    paths: ['sdk/dotnet/**', 'sdk/data/**']
  release:
    types: [published]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'
      - name: Build
        working-directory: sdk/dotnet
        run: dotnet build -c Release
      - name: Test
        working-directory: sdk/dotnet
        run: dotnet test -c Release --logger "console;verbosity=detailed"
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/sdk-dotnet.yml
git commit -m "ci(dotnet): real build + test workflow"
```

---

## Self-Review Checklist

**1. Spec coverage:**
- ✅ Multi-target netstandard2.0 + net8.0 (Task 1)
- ✅ Types: Source, AmbiguityMode, Match, LookupResult, ConversionDetail (Task 1)
- ✅ CodepointHelper for UTF-16 ↔ codepoint (Task 2)
- ✅ Embedded resource loading with System.Text.Json (Task 2)
- ✅ Aho-Corasick with identity protection (Task 3)
- ✅ Three-layer Convert + Check + Lookup (Task 4)
- ✅ Check ordering: layer discovery order (Task 4, not sorted)
- ✅ Lookup ordering: sorted by position (Task 4, details.Sort)
- ✅ Builder with Sources/AmbiguityMode/CustomDict (Task 5)
- ✅ Custom dict overrides built-in terms (Task 5)
- ✅ Static convenience API + Lazy default (Task 5)
- ✅ DataVersion (Task 5)
- ✅ Empty sources → ArgumentException (Task 5)
- ✅ Null/empty input handling (Task 4)
- ✅ Golden tests for all three APIs (Task 6)
- ✅ CI workflow (Task 7)
- ✅ balanced_protect_terms: pre-injected as identity mappings in terms.cn — no separate parsing needed
- ✅ NuGet publish: deferred (no publish job)

**2. Placeholder scan:** No TBD/TODO/placeholder text found.

**3. Type consistency:** All type names, method signatures, and property names match across all tasks.
