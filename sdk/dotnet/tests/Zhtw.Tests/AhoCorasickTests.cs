using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace Zhtw.Tests
{
    public class AhoCorasickTests
    {
        [Fact]
        public void BasicMatch()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("he", "HE"),
                new AcPattern("she", "SHE"),
                new AcPattern("his", "HIS"),
                new AcPattern("hers", "HERS"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("ushers");
            Assert.Equal(2, matches.Count);
            Assert.Equal("she", matches[0].Source);
            Assert.Equal(1, matches[0].Start);
            Assert.Equal("hers", matches[1].Source);
            Assert.Equal(2, matches[1].Start);
        }

        [Fact]
        public void CjkMatch()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("软件", "軟體"),
                new AcPattern("测试", "測試"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("软件测试");
            Assert.Equal(2, matches.Count);
            Assert.Equal("软件", matches[0].Source);
            Assert.Equal(0, matches[0].Start);
            Assert.Equal(2, matches[0].End);
            Assert.Equal("测试", matches[1].Source);
            Assert.Equal(2, matches[1].Start);
            Assert.Equal(4, matches[1].End);
        }

        [Fact]
        public void IdentityProtection()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("檔案", "檔案"),  // identity
                new AcPattern("案件", "案件X"),   // non-identity
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("檔案件");
            Assert.Empty(matches); // identity doesn't emit, non-identity blocked
        }

        [Fact]
        public void EmptyInput()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("ab", "AB"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("");
            Assert.Empty(matches);
        }

        [Fact]
        public void CoveredPositionsIncludesIdentity()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("皇后", "皇后"),  // identity
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var covered = ac.GetCoveredPositions("皇后很美");
            Assert.Contains(0, covered);
            Assert.Contains(1, covered);
            Assert.DoesNotContain(2, covered);
            Assert.DoesNotContain(3, covered);
        }

        [Fact]
        public void LongestMatchWins()
        {
            var patterns = new List<AcPattern>
            {
                new AcPattern("云", "雲"),
                new AcPattern("云计算", "雲端運算"),
            };
            var ac = AhoCorasickAutomaton.Build(patterns);
            var matches = ac.FindTermMatches("云计算");
            Assert.Single(matches);
            Assert.Equal("云计算", matches[0].Source);
            Assert.Equal("雲端運算", matches[0].Target);
        }
    }
}
