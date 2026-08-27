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
        private readonly Dictionary<string, List<RuleMeta>> _ruleRecords;

        private sealed class CharacterChange
        {
            internal int Start;
            internal int End;
            internal string Source;
            internal string Target;
            internal string Layer;
            internal string RuleId;
            internal string ReasonCode;
        }

        internal Converter(AhoCorasickAutomaton ac, Dictionary<int, int> charMap,
            Dictionary<int, int> balancedDefaults, bool charLayerEnabled,
            Dictionary<string, List<RuleMeta>> ruleRecords)
        {
            _ac = ac;
            _charMap = charMap;
            _balancedDefaults = balancedDefaults;
            _charLayerEnabled = charLayerEnabled;
            _ruleRecords = ruleRecords;
        }

        public string Convert(string text)
        {
            if (string.IsNullOrEmpty(text)) return "";

            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var scan = _ac.Scan(text);
            var covered = scan.Covered;
            var hits = scan.Matches;
            return ConvertWithScan(text, codepoints, hits, covered);
        }

        private string ConvertWithScan(string text, int[] codepoints,
            List<AcMatch> hits, HashSet<int> covered)
        {
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

        public string ConvertJson(string text)
        {
            return JsonAdapter.ConvertValues(this, text);
        }

        private List<CharacterChange> CharacterChanges(int[] codepoints, HashSet<int> covered)
        {
            var changes = new List<CharacterChange>();
            for (int position = 0; position < codepoints.Length; position++)
            {
                int source = codepoints[position];
                if (covered.Contains(position)) continue;
                if (_balancedDefaults != null && _balancedDefaults.TryGetValue(source, out int balanced))
                {
                    int target = balanced;
                    if (_charLayerEnabled && _charMap.TryGetValue(target, out int mapped)) target = mapped;
                    if (target != source)
                    {
                        changes.Add(new CharacterChange
                        {
                            Start = position,
                            End = position + 1,
                            Source = char.ConvertFromUtf32(source),
                            Target = char.ConvertFromUtf32(target),
                            Layer = "balanced",
                            RuleId = "balanced:u" + source.ToString("x"),
                            ReasonCode = "balanced_default"
                        });
                    }
                    continue;
                }
                if (_charLayerEnabled && _charMap.TryGetValue(source, out int charTarget) &&
                    charTarget != source)
                {
                    changes.Add(new CharacterChange
                    {
                        Start = position,
                        End = position + 1,
                        Source = char.ConvertFromUtf32(source),
                        Target = char.ConvertFromUtf32(charTarget),
                        Layer = "char",
                        RuleId = "charmap:u" + source.ToString("x"),
                        ReasonCode = "char_map"
                    });
                }
            }
            return changes;
        }

        public ExplainResult Explain(string text)
        {
            if (string.IsNullOrEmpty(text))
                return new ExplainResult("", Array.Empty<ExplainEvent>());

            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var scan = _ac.ScanDetailed(text);
            var changes = CharacterChanges(codepoints, scan.Covered);
            var selectedByStart = new Dictionary<int, AcMatch>();
            foreach (var hit in scan.Matches) selectedByStart[hit.Start] = hit;
            var changesByStart = new Dictionary<int, CharacterChange>();
            foreach (var change in changes) changesByStart[change.Start] = change;

            int[,] spans = new int[codepoints.Length, 2];
            var output = new StringBuilder(text.Length);
            int outputPosition = 0;
            int inputPosition = 0;
            while (inputPosition < codepoints.Length)
            {
                if (selectedByStart.TryGetValue(inputPosition, out var hit))
                {
                    int outputEnd = outputPosition + CodepointHelper.CodepointLength(hit.Target);
                    for (int position = hit.Start; position < hit.End; position++)
                    {
                        spans[position, 0] = outputPosition;
                        spans[position, 1] = outputEnd;
                    }
                    output.Append(hit.Target);
                    outputPosition = outputEnd;
                    inputPosition = hit.End;
                    continue;
                }
                string target = char.ConvertFromUtf32(codepoints[inputPosition]);
                if (changesByStart.TryGetValue(inputPosition, out var change)) target = change.Target;
                int nextOutput = outputPosition + CodepointHelper.CodepointLength(target);
                spans[inputPosition, 0] = outputPosition;
                spans[inputPosition, 1] = nextOutput;
                output.Append(target);
                outputPosition = nextOutput;
                inputPosition++;
            }
            string converted = output.ToString();
            if (converted != ConvertWithScan(text, codepoints, scan.Matches, scan.Covered))
                throw new InvalidOperationException("Explain trace diverged from conversion output");

            var events = new List<ExplainEvent>(scan.Decisions.Count + changes.Count);
            foreach (var decision in scan.Decisions)
            {
                var match = decision.Hit;
                int outputStart = spans[match.Start, 0];
                int outputEnd = spans[match.Start, 1];
                for (int position = match.Start + 1; position < match.End; position++)
                {
                    outputStart = Math.Min(outputStart, spans[position, 0]);
                    outputEnd = Math.Max(outputEnd, spans[position, 1]);
                }
                _ruleRecords.TryGetValue(match.Source, out var candidates);
                if (candidates == null) candidates = new List<RuleMeta>();
                int winner = -1;
                for (int index = candidates.Count - 1; index >= 0; index--)
                {
                    if (candidates[index].Target == match.Target)
                    {
                        winner = index;
                        break;
                    }
                }
                string ruleId = winner >= 0 ? candidates[winner].Id :
                    RuleCatalog.LegacyCustomRuleId(match.Source, match.Target);
                var conflicts = new List<RuleMeta>();
                for (int index = 0; index < candidates.Count; index++)
                    if (index != winner) conflicts.Add(candidates[index]);
                string reasonCode = decision.Outcome == "applied" && conflicts.Count > 0 ?
                    "loader_conflict_winner" : decision.ReasonCode;
                events.Add(new ExplainEvent(
                    ruleId, match.Source == match.Target ? "identity" : "term", decision.Outcome,
                    match.Start, match.End, outputStart, outputEnd,
                    match.Source, match.Target, reasonCode));
                if (decision.Outcome == "applied")
                {
                    foreach (var conflict in conflicts)
                    {
                        events.Add(new ExplainEvent(
                            conflict.Id, "term", "skipped", match.Start, match.End,
                            outputStart, outputEnd, conflict.Source, conflict.Target,
                            "loader_conflict_loser"));
                    }
                }
            }
            foreach (var change in changes)
            {
                events.Add(new ExplainEvent(
                    change.RuleId, change.Layer, "applied", change.Start, change.End,
                    spans[change.Start, 0], spans[change.Start, 1],
                    change.Source, change.Target, change.ReasonCode));
            }
            events.Sort((left, right) =>
            {
                int comparison = left.InputStart.CompareTo(right.InputStart);
                if (comparison != 0) return comparison;
                comparison = left.InputEnd.CompareTo(right.InputEnd);
                if (comparison != 0) return comparison;
                comparison = OutcomeOrder(left.Outcome).CompareTo(OutcomeOrder(right.Outcome));
                if (comparison != 0) return comparison;
                return string.Compare(left.RuleId, right.RuleId, StringComparison.Ordinal);
            });
            return new ExplainResult(converted, events);
        }

        private static int OutcomeOrder(string outcome)
        {
            if (outcome == "applied") return 0;
            if (outcome == "protected") return 1;
            return 2;
        }

        public IReadOnlyList<Match> Check(string text)
        {
            if (string.IsNullOrEmpty(text)) return Array.Empty<Match>();

            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var scan = _ac.Scan(text);
            var covered = scan.Covered;
            var hits = scan.Matches;

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
            var scan = _ac.Scan(word);
            var covered = scan.Covered;
            var hits = scan.Matches;

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
                // Charmap second.
                if (_charLayerEnabled && _charMap.TryGetValue(outCp, out int cm))
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
