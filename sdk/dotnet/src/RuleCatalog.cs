using System;
using System.Security.Cryptography;

namespace Zhtw
{
    internal sealed class RuleMeta
    {
        internal string Id { get; }
        internal string Source { get; }
        internal string Target { get; }

        internal RuleMeta(string id, string source, string target)
        {
            Id = id;
            Source = source;
            Target = target;
        }
    }

    internal static class RuleCatalog
    {
        internal static string LegacyCustomRuleId(string source, string target)
        {
            string canonical = "{\"rule_class\":\"custom\",\"source\":" +
                JsonAdapter.QuoteString(source) +
                ",\"source_locale\":\"cn\",\"target\":" +
                JsonAdapter.QuoteString(target) + "}";
            using (var sha = SHA256.Create())
            {
                byte[] digest = sha.ComputeHash(System.Text.Encoding.UTF8.GetBytes(canonical));
                return "legacy:cn:custom:" + ToHex(digest, 12);
            }
        }

        private static string ToHex(byte[] bytes, int count)
        {
            char[] output = new char[count * 2];
            const string hex = "0123456789abcdef";
            for (int i = 0; i < count; i++)
            {
                output[i * 2] = hex[bytes[i] >> 4];
                output[i * 2 + 1] = hex[bytes[i] & 0x0f];
            }
            return new string(output);
        }
    }
}
