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
