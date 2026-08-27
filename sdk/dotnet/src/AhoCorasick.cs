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

    internal sealed class MatchDecision
    {
        internal AcMatch Hit { get; }
        internal string Outcome { get; }
        internal string ReasonCode { get; }

        internal MatchDecision(AcMatch hit, string outcome, string reasonCode)
        {
            Hit = hit;
            Outcome = outcome;
            ReasonCode = reasonCode;
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
        internal sealed class ScanResult
        {
            internal List<AcMatch> Matches { get; }
            internal HashSet<int> Covered { get; }

            internal ScanResult(List<AcMatch> matches, HashSet<int> covered)
            {
                Matches = matches;
                Covered = covered;
            }
        }

        internal sealed class DetailedScanResult
        {
            internal List<AcMatch> Matches { get; }
            internal HashSet<int> Covered { get; }
            internal List<MatchDecision> Decisions { get; }

            internal DetailedScanResult(List<AcMatch> matches, HashSet<int> covered,
                List<MatchDecision> decisions)
            {
                Matches = matches;
                Covered = covered;
                Decisions = decisions;
            }
        }

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
            return Scan(text).Covered;
        }

        internal List<AcMatch> FindTermMatches(string text)
        {
            return Scan(text).Matches;
        }

        internal ScanResult Scan(string text)
        {
            int[] codepoints = CodepointHelper.ToCodepoints(text);
            var raw = IterEmissions(codepoints);
            var matches = SelectTermMatches(raw, out var covered);
            foreach (var m in matches)
                for (int i = m.Start; i < m.End; i++)
                    covered.Add(i);
            return new ScanResult(matches, covered);
        }

        internal DetailedScanResult ScanDetailed(string text)
        {
            var raw = IterEmissions(CodepointHelper.ToCodepoints(text));
            var matches = SelectTermMatches(raw, true, out var covered, out var decisions);
            foreach (var match in matches)
                for (int i = match.Start; i < match.End; i++)
                    covered.Add(i);
            return new DetailedScanResult(matches, covered, decisions);
        }

        private static List<AcMatch> SelectTermMatches(
            List<AcMatch> raw,
            out HashSet<int> protectedPos)
        {
            return SelectTermMatches(raw, false, out protectedPos, out _);
        }

        private static List<AcMatch> SelectTermMatches(
            List<AcMatch> raw,
            bool detailed,
            out HashSet<int> protectedPos,
            out List<MatchDecision> decisions)
        {
            decisions = new List<MatchDecision>();
            if (raw.Count == 0)
            {
                protectedPos = new HashSet<int>();
                return new List<AcMatch>();
            }

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
            protectedPos = new HashSet<int>();
            var effectiveIdentity = new HashSet<AcMatch>();
            if (nonIdentitySpans.Count == 0)
            {
                foreach (var m in identity)
                {
                    for (int i = m.Start; i < m.End; i++)
                        protectedPos.Add(i);
                    effectiveIdentity.Add(m);
                }
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
                        effectiveIdentity.Add(m);
                    }
                }
            }

            // Left-to-right greedy filter.
            var result = new List<AcMatch>();
            int cursor = 0;
            foreach (var m in raw)
            {
                if (m.Start < cursor)
                {
                    if (detailed)
                    {
                        bool identityMatch = m.Source == m.Target;
                        bool effective = effectiveIdentity.Contains(m);
                        string outcome = identityMatch && effective ? "protected" : "skipped";
                        string reason = !identityMatch ? "overlap_loser" :
                            effective ? "identity_guard" : "identity_contained";
                        decisions.Add(new MatchDecision(m, outcome, reason));
                    }
                    continue;
                }
                bool isIdentity = m.Source == m.Target;
                if (!isIdentity)
                {
                    bool overlaps = false;
                    for (int i = m.Start; i < m.End; i++)
                    {
                        if (protectedPos.Contains(i)) { overlaps = true; break; }
                    }
                    if (overlaps)
                    {
                        if (detailed)
                            decisions.Add(new MatchDecision(m, "skipped", "protected_by_identity"));
                        continue;
                    }
                }
                cursor = m.End;
                if (!isIdentity)
                {
                    result.Add(m);
                    if (detailed)
                        decisions.Add(new MatchDecision(m, "applied", "term_selected"));
                }
                else if (detailed)
                {
                    string reason = effectiveIdentity.Contains(m) ?
                        "identity_guard" : "identity_contained";
                    decisions.Add(new MatchDecision(m, "protected", reason));
                }
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
