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
