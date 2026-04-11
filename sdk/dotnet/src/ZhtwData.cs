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
