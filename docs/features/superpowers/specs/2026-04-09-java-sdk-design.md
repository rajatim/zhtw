<!-- zhtw:disable -->
# Java SDK Design (SP2)

> **Sub-project 2 of 6** — 完整 Java SDK + Maven Central 發佈

## Goal

將 POC（ai-guardrail-gateway 的 ZhtwConverter.java）演進為正式 Java SDK，發佈到 Maven Central。保留兩層轉換架構，升級為 Aho-Corasick + Builder pattern，實作完整 API（convert/check/lookup），通過 golden test 確保與 Python 輸出一致。

## 決策記錄

| 決策 | 結論 | 理由 |
|------|------|------|
| 架構方案 | 直接演進 POC | 兩層架構已 SIT 驗證，核心邏輯不需重寫 |
| 匹配演算法 | Aho-Corasick（取代 HashMap） | O(n) 掃描，支援大檔案批次轉換 |
| 依賴 | Gson + robert-bor/aho-corasick | 最小依賴，避免版本衝突 |
| Lombok | 不用 | SDK 不應強迫使用者裝 annotation processor |
| Java 版本 | 11+ | 跟 POC 一致，覆蓋主流企業環境 |
| 發佈 | Maven Central | 正式公開，任何人可用 |
| 使用場景 | 先 LLM 後處理，API 可擴充到大檔案 | Builder pattern 支援彈性設定 |

## 目錄結構

```
sdk/java/
├── pom.xml
├── src/main/java/com/rajatim/zhtw/
│   ├── ZhtwConverter.java              # 公開 API：Builder + getDefault + convert/check/lookup
│   ├── AhoCorasickMatcher.java         # AC 自動機封裝（package-private）
│   ├── Match.java                      # 匹配結果（public）
│   ├── LookupResult.java              # lookup 結果（public）
│   ├── ConversionDetail.java          # 轉換細節（public）
│   └── ZhtwData.java                  # zhtw-data.json 載入（package-private）
├── src/main/resources/
│   └── zhtw-data.json                 # build 時從 sdk/data/ 複製（.gitignore）
├── src/test/java/com/rajatim/zhtw/
│   ├── ZhtwConverterTest.java         # 轉換器單元測試
│   ├── GoldenTest.java                # golden-test.json 一致性測試
│   └── AhoCorasickMatcherTest.java    # matcher 單元測試
└── src/test/resources/
    ├── zhtw-data.json                 # 測試用（同 main）
    └── golden-test.json               # golden test 資料
```

**分工原則**：
- `ZhtwConverter` 是唯一公開入口
- `AhoCorasickMatcher` 和 `ZhtwData` 是 package-private，不暴露給使用者
- `Match`、`LookupResult`、`ConversionDetail` 是 public data class（final class + getter，Java 11 沒有 record）
- 資源檔透過 Maven resource plugin 從 `sdk/data/` 複製，不手動同步
- `src/main/resources/zhtw-data.json` 加入 `.gitignore`（從 `sdk/data/` 生成）

## 公開 API

### 最簡用法（一行）

```java
String result = ZhtwConverter.getDefault().convert("软件测试");
// → "軟體測試"
```

### Builder 自訂

```java
ZhtwConverter converter = ZhtwConverter.builder()
    .sources(List.of("cn"))              // 只用 CN 詞庫（預設 ["cn", "hk"]）
    .customDict(Map.of("咖啡", "珈琲"))  // 自訂詞條（優先於內建）
    .build();
```

### 三方法

| 方法 | 簽名 | 用途 |
|------|------|------|
| `convert` | `String convert(String text)` | 轉換全文 |
| `check` | `List<Match> check(String text)` | 回報匹配，不修改原文 |
| `lookup` | `LookupResult lookup(String word)` | 查詢單一詞的轉換細節 |

### getDefault() 行為

- 載入 classpath 的 `zhtw-data.json`
- sources = `["cn", "hk"]`
- 無 custom dict
- Lazy init + 雙重檢查鎖定（thread-safe singleton）
- 多次呼叫返回同一實例

### Builder 行為

- 每次 `.build()` 建新實例（因 custom dict 不同，automaton 不能共用）
- `sources(List<String>)` — 過濾載入哪些詞庫（"cn", "hk"）
- `customDict(Map<String, String>)` — 自訂詞條，優先於內建
- `build()` 時建構 AC automaton（一次性成本）

### 資料型別

```java
// Match — check() 回傳的匹配結果
public final class Match {
    int getStart();       // 起始位置（含）
    int getEnd();         // 結束位置（不含）
    String getSource();   // 原始詞（如 "软件"）
    String getTarget();   // 替換詞（如 "軟體"）
}

// LookupResult — lookup() 回傳的查詢結果
public final class LookupResult {
    String getInput();
    String getOutput();
    boolean isChanged();
    List<ConversionDetail> getDetails();
}

// ConversionDetail — 轉換歸因
public final class ConversionDetail {
    String getSource();
    String getTarget();
    String getLayer();    // "term" 或 "char"
    int getPosition();
}
```

## 轉換演算法

兩階段 pipeline，與 Python 完全一致：

### Stage 1 — 詞彙層（Aho-Corasick）

1. 將所有詞條（內建 + custom dict）餵入 AC automaton
2. AC 掃描全文，收集所有匹配（含重疊）
3. 左到右貪心，取最長不重疊匹配
4. Identity mapping（source == target）佔位不替換，但標記 protected range
5. 替換命中的詞條

### Stage 2 — 字元層（逐字查表）

1. **僅在 sources 包含 "cn" 時啟用**（HK 只做詞彙層）
2. 用 `boolean[]` 標記 protected range（Stage 1 已匹配的位置）
3. 逐字查 charmap，跳過：
   - protected range 內的位置
   - ambiguous chars（119 個多義字，如 `发` 可能是 `髮` 或 `發`）
4. 替換命中的字元

### 跟 POC 的差異

| | POC | 正式版 |
|--|-----|--------|
| 匹配 | HashMap 逐位置 O(n×maxLen) | AC automaton O(n) |
| 重疊處理 | 隱式（最長先命中就 break） | 明確收集全部 → 貪心選最長 |
| Protected range | 無 | `boolean[]` 標記 |
| Identity mapping | 無 | 有（防誤轉） |
| Ambiguous chars | 無 | 跳過（防多義字誤轉） |
| maxTermLen | 寫死 8 | 不需要（AC 自動掃描） |

## 資料載入

### 單一資源檔

`zhtw-data.json`（~900KB）從 classpath 載入，Gson 反序列化。

```java
// ZhtwData — package-private
ZhtwData data = ZhtwData.fromClasspath();       // 預設 /zhtw-data.json
ZhtwData data = ZhtwData.fromInputStream(is);   // 自訂來源（測試用）

data.getCharmap();      // Map<Character, Character> — 6,343 筆
data.getAmbiguous();    // Set<Character> — 119 字
data.getTerms("cn");    // Map<String, String> — 31,794 筆
data.getTerms("hk");    // Map<String, String> — 61 筆
data.getVersion();      // "3.3.0"
```

### Build 時資源複製

Maven resource plugin 在 `generate-resources` phase：
- `sdk/data/zhtw-data.json` → `src/main/resources/zhtw-data.json`
- `sdk/data/golden-test.json` → `src/test/resources/golden-test.json`

## 測試策略

### 1. AhoCorasickMatcherTest — 匹配器單元測試

- 基本匹配
- 最長匹配優先（"服务器" 贏 "服务"）
- 重疊處理（左到右貪心）
- Identity mapping 佔位不替換
- 空輸入、無匹配

### 2. ZhtwConverterTest — 轉換器單元測試

- convert: 純詞彙層、純字元層、兩層混合
- convert: HK source 不啟用字元層
- convert: identity mapping 防誤轉
- convert: ambiguous chars 跳過
- convert: custom dict 優先於內建
- check: 回傳正確的 Match 位置
- lookup: 回傳正確的 ConversionDetail
- getDefault: thread-safe singleton
- builder: sources 過濾、custom dict

### 3. GoldenTest — 一致性測試

讀取 `golden-test.json`，驗證 Java SDK 輸出與 Python 完全一致：

- 每個 convert case：`converter.convert(input) == expected`
- 每個 check case：matches 的 start/end/source/target 完全一致
- 每個 lookup case：output/changed/details 完全一致

## Maven Central 發佈

### pom.xml 依賴

| GroupId | ArtifactId | Version | Scope |
|---------|-----------|---------|-------|
| com.google.code.gson | gson | 2.11.0 | compile |
| org.ahocorasick | ahocorasick | 0.6.3 | compile |
| org.junit.jupiter | junit-jupiter | 5.11.4 | test |

### 發佈設定

- `maven-source-plugin` — 附帶 sources jar
- `maven-javadoc-plugin` — 附帶 javadoc jar
- `maven-gpg-plugin` — GPG 簽名
- `maven-deploy-plugin` + `nexus-staging-maven-plugin` — 發到 OSSRH

### CI 發佈流程

`sdk-java.yml` 在 `release: types: [published]` 時觸發 publish job：

```
mvn deploy -P release
```

**SP2 範圍**：pom.xml 和 CI 設定寫好，但實際發佈需要先設定：
- Sonatype OSSRH 帳號
- GPG key
- GitHub Actions secrets（`OSSRH_USERNAME`、`OSSRH_TOKEN`、`GPG_PRIVATE_KEY`）

帳號設定不在 SP2 scope 內。

## SP2 範圍總結

1. `pom.xml` — 完整 Maven 設定（依賴、plugin、發佈 profile）
2. `ZhtwConverter.java` — Builder + getDefault + convert/check/lookup
3. `AhoCorasickMatcher.java` — AC 封裝
4. `Match.java`、`LookupResult.java`、`ConversionDetail.java` — data class
5. `ZhtwData.java` — 資料載入
6. `ZhtwConverterTest.java` — 單元測試
7. `AhoCorasickMatcherTest.java` — matcher 測試
8. `GoldenTest.java` — golden test 一致性
9. `sdk-java.yml` — 正式化 CI（build + test + publish skeleton）
10. `.gitignore` — 排除生成的資源檔
<!-- zhtw:enable -->
