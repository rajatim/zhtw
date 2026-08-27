# zhtw (Java SDK)

> Traditional Chinese converter for Taiwan — Java SDK

Simplified Chinese / HK Traditional to Taiwan Traditional Chinese converter. Thread-safe, zero external dependencies, embedded dictionary. Byte-for-byte compatible with the Python CLI and all other SDKs, verified by a shared golden fixture.

## Install

**Maven**:

<!-- zhtw:disable -->
```xml
<dependency>
    <groupId>com.rajatim</groupId>
    <artifactId>zhtw</artifactId>
    <version>4.4.5</version>
</dependency>
```
<!-- zhtw:enable -->

**Gradle (Kotlin DSL)**:

```kotlin
implementation("com.rajatim:zhtw:4.4.5")
```

## Quick start

<!-- zhtw:disable -->
```java
import com.rajatim.zhtw.ZhtwConverter;

// Thread-safe singleton, zero config
String result = ZhtwConverter.getDefault().convert("这个软件需要优化");
// => "這個軟體需要最佳化"
```
<!-- zhtw:enable -->

## Builder API

<!-- zhtw:disable -->
```java
ZhtwConverter conv = ZhtwConverter.builder()
    .sources(List.of("cn", "hk"))
    .customDict(Map.of("自定义", "自訂"))
    .ambiguityMode("balanced")
    .build();

conv.convert("自定义几个里程碑");
conv.explain("软件");
conv.convertJson("{\"软件\":\"这个软件\"}");
```
<!-- zhtw:enable -->

## API

| Method | Description |
|--------|-------------|
| `convert(text)` | Convert text |
| `convertJson(text)` | Convert JSON string values only; reject duplicate keys |
| `check(text)` | Return list of replacements without modifying |
| `lookup(word)` | Look up a single word in the dictionary |
| `explain(text)` | Return converted output and stable rule events |

## Performance

Single sentence: 2 us, 100K chars: 5.5 ms (17.9 MB/s). See [`BENCHMARK.md`](BENCHMARK.md) for JMH results.

## Requirements

- Java 11+
- Zero external dependencies

## Links

- [Main README](../../README.md) | [CHANGELOG](../../CHANGELOG.md) | [Maven Central](https://central.sonatype.com/artifact/com.rajatim/zhtw)

## License

MIT
