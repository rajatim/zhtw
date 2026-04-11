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
