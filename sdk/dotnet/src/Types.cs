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
