using System;
using System.Collections.Generic;
using Xunit;

namespace Zhtw.Tests
{
    public class ConverterTests
    {
        [Fact]
        public void ConvertBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Equal("軟體測試", conv.Convert("软件测试"));
        }

        [Fact]
        public void ConvertEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Equal("", conv.Convert(""));
            Assert.Equal("", conv.Convert(null));
        }

        [Fact]
        public void CheckBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var matches = conv.Check("软件测试");
            Assert.Equal(2, matches.Count);
            Assert.Equal("软件", matches[0].Source);
            Assert.Equal("軟體", matches[0].Target);
            Assert.Equal(0, matches[0].Start);
            Assert.Equal(2, matches[0].End);
        }

        [Fact]
        public void CheckEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            Assert.Empty(conv.Check(""));
            Assert.Empty(conv.Check(null));
        }

        [Fact]
        public void LookupBasic()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup("软件");
            Assert.Equal("软件", result.Input);
            Assert.Equal("軟體", result.Output);
            Assert.True(result.Changed);
            Assert.Single(result.Details);
            Assert.Equal("term", result.Details[0].Layer);
        }

        [Fact]
        public void LookupEmpty()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup("");
            Assert.Equal("", result.Input);
            Assert.Equal("", result.Output);
            Assert.False(result.Changed);
            Assert.Empty(result.Details);
        }

        [Fact]
        public void LookupNull()
        {
            var conv = new ConverterBuilder().Sources(Source.Cn).Build();
            var result = conv.Lookup(null);
            Assert.Equal("", result.Input);
            Assert.Equal("", result.Output);
            Assert.False(result.Changed);
            Assert.Empty(result.Details);
        }

        [Fact]
        public void CustomDictOverride()
        {
            var conv = new ConverterBuilder()
                .Sources(Source.Cn)
                .CustomDict(new Dictionary<string, string> { { "软件", "軟件" } })
                .Build();
            Assert.Equal("軟件", conv.Convert("软件"));
        }

        [Fact]
        public void BalancedMode()
        {
            var conv = new ConverterBuilder()
                .Sources(Source.Cn)
                .AmbiguityMode(AmbiguityMode.Balanced)
                .Build();
            // "以后" should become "以後" in balanced mode
            Assert.Equal("以後再說", conv.Convert("以后再说"));
            // "皇后" should be protected — not converted
            Assert.Equal("皇后很美", conv.Convert("皇后很美"));
        }

        [Fact]
        public void HkSource()
        {
            var conv = new ConverterBuilder().Sources(Source.Hk).Build();
            Assert.Equal("軟體工程師", conv.Convert("軟件工程師"));
        }
    }
}
