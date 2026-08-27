using System;
using Xunit;

namespace Zhtw.Tests
{
    public class DataValidationTests
    {
        [Fact]
        public void StillAcceptsSchemaV1()
        {
            string json = @"{
              ""schema_version"": 1,
              ""version"": ""1.2.3"",
              ""stats"": {},
              ""charmap"": {
                ""chars"": {},
                ""ambiguous"": [],
                ""balanced_defaults"": {},
                ""balanced_protect_terms"": {}
              },
              ""terms"": { ""cn"": {}, ""hk"": {} }
            }";

            Assert.Equal("1.2.3", ZhtwData.Parse(json).Version);
        }

        [Fact]
        public void RejectsSchemaV2CatalogMismatch()
        {
            string json = @"{
              ""schema_version"": 2,
              ""version"": ""1.2.3"",
              ""stats"": { ""rule_catalog_count"": 0 },
              ""charmap"": {
                ""chars"": {},
                ""ambiguous"": [],
                ""balanced_defaults"": {},
                ""balanced_protect_terms"": {}
              },
              ""terms"": { ""cn"": { ""software"": ""target"" } },
              ""rule_catalog"": { ""format"": ""grouped-v1"", ""groups"": [] }
            }";

            Assert.Throws<InvalidOperationException>(() => ZhtwData.Parse(json));
        }
    }
}
