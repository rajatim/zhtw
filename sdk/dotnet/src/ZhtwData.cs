using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text.Json;
using System.Text.RegularExpressions;

namespace Zhtw
{
    internal sealed class ZhtwData
    {
        internal string Version { get; }
        internal Dictionary<int, int> CharMap { get; }
        internal Dictionary<int, int> BalancedDefaults { get; }
        internal Dictionary<string, string> TermsCn { get; }
        internal Dictionary<string, string> TermsHk { get; }
        internal Dictionary<string, List<RuleMeta>> RuleRecordsCn { get; }
        internal Dictionary<string, List<RuleMeta>> RuleRecordsHk { get; }

        private ZhtwData(string version, Dictionary<int, int> charMap,
            Dictionary<int, int> balancedDefaults,
            Dictionary<string, string> termsCn, Dictionary<string, string> termsHk,
            Dictionary<string, List<RuleMeta>> ruleRecordsCn,
            Dictionary<string, List<RuleMeta>> ruleRecordsHk)
        {
            Version = version;
            CharMap = charMap;
            BalancedDefaults = balancedDefaults;
            TermsCn = termsCn;
            TermsHk = termsHk;
            RuleRecordsCn = ruleRecordsCn;
            RuleRecordsHk = ruleRecordsHk;
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

        internal static ZhtwData Parse(string json)
        {
            using (var doc = JsonDocument.Parse(json))
            {
                var root = doc.RootElement;
                int schemaVersion = root.GetProperty("schema_version").GetInt32();
                if (schemaVersion != 1 && schemaVersion != 2)
                    throw new InvalidOperationException("Unsupported zhtw data schema version");
                if (schemaVersion == 1)
                    RequireOnlyProperties(root, "schema_version", "version", "stats", "charmap", "terms");
                else
                    RequireOnlyProperties(root, "schema_version", "version", "stats", "charmap", "terms", "rule_catalog");
                string version = root.GetProperty("version").GetString();
                if (string.IsNullOrEmpty(version))
                    throw new InvalidOperationException("Missing zhtw data version");

                var charmapEl = root.GetProperty("charmap");
                RequireOnlyProperties(charmapEl, "chars", "ambiguous", "balanced_defaults", "balanced_protect_terms");

                // Parse chars (single-codepoint only)
                var charMap = new Dictionary<int, int>();
                foreach (var prop in charmapEl.GetProperty("chars").EnumerateObject())
                {
                    int[] kCp = CodepointHelper.ToCodepoints(prop.Name);
                    int[] vCp = CodepointHelper.ToCodepoints(prop.Value.GetString());
                    if (kCp.Length != 1 || vCp.Length != 1)
                        throw new InvalidOperationException("Charmap entries must contain one Unicode code point");
                    charMap[kCp[0]] = vCp[0];
                }

                // Parse balanced_defaults (single-codepoint only)
                var balancedDefaults = new Dictionary<int, int>();
                if (charmapEl.TryGetProperty("balanced_defaults", out var bdEl))
                {
                    foreach (var prop in bdEl.EnumerateObject())
                    {
                        int[] kCp = CodepointHelper.ToCodepoints(prop.Name);
                        int[] vCp = CodepointHelper.ToCodepoints(prop.Value.GetString());
                        if (kCp.Length != 1 || vCp.Length != 1)
                            throw new InvalidOperationException("Balanced defaults must contain one Unicode code point");
                        balancedDefaults[kCp[0]] = vCp[0];
                    }
                }

                // Parse terms
                var termsEl = root.GetProperty("terms");
                foreach (var prop in termsEl.EnumerateObject())
                {
                    if (prop.Name != "cn" && prop.Name != "hk")
                        throw new InvalidOperationException("Unsupported term source: " + prop.Name);
                }
                var termsCn = ParseTerms(termsEl, "cn");
                var termsHk = ParseTerms(termsEl, "hk");

                if (schemaVersion == 2)
                    ValidateRuleCatalog(root, termsEl);

                var ruleRecordsCn = new Dictionary<string, List<RuleMeta>>();
                var ruleRecordsHk = new Dictionary<string, List<RuleMeta>>();
                if (schemaVersion == 2)
                    ParseRuleRecords(root, ruleRecordsCn, ruleRecordsHk);

                return new ZhtwData(version, charMap, balancedDefaults, termsCn, termsHk,
                    ruleRecordsCn, ruleRecordsHk);
            }
        }

        private static void ParseRuleRecords(JsonElement root,
            Dictionary<string, List<RuleMeta>> cn,
            Dictionary<string, List<RuleMeta>> hk)
        {
            foreach (var group in root.GetProperty("rule_catalog").GetProperty("groups").EnumerateArray())
            {
                if (group.GetProperty("review_status").GetString() != "approved") continue;
                var destination = group.GetProperty("source_locale").GetString() == "cn" ? cn : hk;
                foreach (var rule in group.GetProperty("rules").EnumerateObject())
                {
                    string source = rule.Value[0].GetString();
                    if (!destination.TryGetValue(source, out var records))
                    {
                        records = new List<RuleMeta>();
                        destination[source] = records;
                    }
                    records.Add(new RuleMeta(rule.Name, source, rule.Value[1].GetString()));
                }
            }
        }

        private static void ValidateRuleCatalog(JsonElement root, JsonElement termsEl)
        {
            var catalog = root.GetProperty("rule_catalog");
            RequireOnlyProperties(catalog, "format", "groups");
            if (catalog.GetProperty("format").GetString() != "grouped-v1" ||
                catalog.GetProperty("groups").ValueKind != JsonValueKind.Array)
                throw new InvalidOperationException("Invalid rule catalog envelope");

            var ruleClasses = new HashSet<string> { "bulk", "generated_guard", "curated", "custom" };
            var trustLevels = new HashSet<string> { "imported", "generated", "curated", "custom" };
            var reviewStatuses = new HashSet<string> { "pending", "approved", "rejected" };
            var domains = new HashSet<string> { "general", "business", "daily", "ecommerce",
                "education", "finance", "formal", "gaming", "geography", "it", "legal",
                "medical", "social", "ui" };
            var ruleId = new Regex("^[a-z0-9][a-z0-9._:-]{2,127}$", RegexOptions.CultureInvariant);
            var ids = new HashSet<string>();
            var approved = new HashSet<string>();
            int count = 0;

            foreach (var group in catalog.GetProperty("groups").EnumerateArray())
            {
                RequireOnlyProperties(group, "source_locale", "rule_class", "domain", "trust_level",
                    "priority", "context", "evidence_source", "review_status", "rules");
                string locale = group.GetProperty("source_locale").GetString();
                string ruleClass = group.GetProperty("rule_class").GetString();
                string domain = group.GetProperty("domain").GetString();
                string trust = group.GetProperty("trust_level").GetString();
                string review = group.GetProperty("review_status").GetString();
                int priority = group.GetProperty("priority").GetInt32();
                if ((locale != "cn" && locale != "hk") || !ruleClasses.Contains(ruleClass) ||
                    !domains.Contains(domain) || !trustLevels.Contains(trust) ||
                    !reviewStatuses.Contains(review) || priority < -1000 || priority > 1000)
                    throw new InvalidOperationException("Invalid rule catalog group metadata");

                var contexts = new HashSet<string>();
                foreach (var context in group.GetProperty("context").EnumerateArray())
                {
                    string value = context.GetString();
                    if (string.IsNullOrEmpty(value) || !contexts.Add(value))
                        throw new InvalidOperationException("Invalid rule catalog context");
                }
                var evidence = group.GetProperty("evidence_source");
                if (evidence.ValueKind != JsonValueKind.Null &&
                    (evidence.ValueKind != JsonValueKind.String || string.IsNullOrEmpty(evidence.GetString())))
                    throw new InvalidOperationException("Invalid rule catalog evidence source");
                if (review == "approved" && evidence.ValueKind == JsonValueKind.Null)
                    throw new InvalidOperationException("Approved rule catalog groups require evidence");

                foreach (var rule in group.GetProperty("rules").EnumerateObject())
                {
                    if (!ruleId.IsMatch(rule.Name) || !ids.Add(rule.Name) ||
                        rule.Value.ValueKind != JsonValueKind.Array || rule.Value.GetArrayLength() != 2)
                        throw new InvalidOperationException("Duplicate or invalid rule catalog entry");
                    string source = rule.Value[0].GetString();
                    string target = rule.Value[1].GetString();
                    if (string.IsNullOrEmpty(source) || string.IsNullOrEmpty(target))
                        throw new InvalidOperationException("Rule catalog source and target must be non-empty");
                    count++;
                    if (review == "approved")
                        approved.Add(locale + "\0" + source + "\0" + target);
                }
            }

            int expectedCount = root.GetProperty("stats").GetProperty("rule_catalog_count").GetInt32();
            if (count != expectedCount)
                throw new InvalidOperationException("Rule catalog count does not match stats");
            foreach (var locale in termsEl.EnumerateObject())
            {
                foreach (var term in locale.Value.EnumerateObject())
                {
                    string key = locale.Name + "\0" + term.Name + "\0" + term.Value.GetString();
                    if (!approved.Contains(key))
                        throw new InvalidOperationException("Rule catalog does not cover effective terms");
                }
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

        private static void RequireOnlyProperties(JsonElement element, params string[] expected)
        {
            var actual = new HashSet<string>();
            foreach (var prop in element.EnumerateObject()) actual.Add(prop.Name);
            if (!actual.SetEquals(expected))
                throw new InvalidOperationException("Unexpected or missing zhtw data fields");
        }
    }
}
