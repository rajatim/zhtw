using System;

namespace Zhtw
{
    internal static class CodepointHelper
    {
        internal static int[] ToCodepoints(string text)
        {
            int len = CodepointLength(text);
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
