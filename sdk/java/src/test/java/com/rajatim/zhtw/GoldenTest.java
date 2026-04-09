package com.rajatim.zhtw;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class GoldenTest {

    private Map<String, Object> loadGolden() {
        InputStream is = getClass().getResourceAsStream("/golden-test.json");
        assertNotNull(is, "golden-test.json not found on classpath");
        Type type = new TypeToken<Map<String, Object>>() {}.getType();
        return new Gson().fromJson(
                new InputStreamReader(is, StandardCharsets.UTF_8), type);
    }

    private ZhtwConverter converterFor(List<String> sources) {
        return ZhtwConverter.builder().sources(sources).build();
    }

    @TestFactory
    @SuppressWarnings("unchecked")
    Collection<DynamicTest> convertCases() {
        Map<String, Object> golden = loadGolden();
        List<Map<String, Object>> cases = (List<Map<String, Object>>) golden.get("convert");
        List<DynamicTest> tests = new ArrayList<>();

        for (Map<String, Object> c : cases) {
            String input = (String) c.get("input");
            List<String> sources = (List<String>) c.get("sources");
            String expected = (String) c.get("expected");

            tests.add(DynamicTest.dynamicTest(
                    "convert: " + input + " [" + String.join(",", sources) + "]",
                    () -> {
                        ZhtwConverter conv = converterFor(sources);
                        assertEquals(expected, conv.convert(input),
                                "Convert mismatch for '" + input + "'");
                    }
            ));
        }
        return tests;
    }

    @TestFactory
    @SuppressWarnings("unchecked")
    Collection<DynamicTest> checkCases() {
        Map<String, Object> golden = loadGolden();
        List<Map<String, Object>> cases = (List<Map<String, Object>>) golden.get("check");
        List<DynamicTest> tests = new ArrayList<>();

        for (Map<String, Object> c : cases) {
            String input = (String) c.get("input");
            List<String> sources = (List<String>) c.get("sources");
            List<Map<String, Object>> expectedMatches =
                    (List<Map<String, Object>>) c.get("expected_matches");

            tests.add(DynamicTest.dynamicTest(
                    "check: " + input + " [" + String.join(",", sources) + "]",
                    () -> {
                        ZhtwConverter conv = converterFor(sources);
                        List<Match> actual = conv.check(input);

                        assertEquals(expectedMatches.size(), actual.size(),
                                "Match count mismatch for '" + input + "': " +
                                "expected " + expectedMatches.size() + " but got " + actual.size() +
                                "\nExpected: " + expectedMatches +
                                "\nActual: " + actual);

                        for (int i = 0; i < expectedMatches.size(); i++) {
                            Map<String, Object> em = expectedMatches.get(i);
                            Match am = actual.get(i);
                            int expStart = ((Number) em.get("start")).intValue();
                            int expEnd = ((Number) em.get("end")).intValue();
                            String expSource = (String) em.get("source");
                            String expTarget = (String) em.get("target");

                            assertEquals(expStart, am.getStart(),
                                    "Match[" + i + "] start mismatch for '" + input + "'");
                            assertEquals(expEnd, am.getEnd(),
                                    "Match[" + i + "] end mismatch for '" + input + "'");
                            assertEquals(expSource, am.getSource(),
                                    "Match[" + i + "] source mismatch for '" + input + "'");
                            assertEquals(expTarget, am.getTarget(),
                                    "Match[" + i + "] target mismatch for '" + input + "'");
                        }
                    }
            ));
        }
        return tests;
    }

    @TestFactory
    @SuppressWarnings("unchecked")
    Collection<DynamicTest> lookupCases() {
        Map<String, Object> golden = loadGolden();
        List<Map<String, Object>> cases = (List<Map<String, Object>>) golden.get("lookup");
        List<DynamicTest> tests = new ArrayList<>();

        for (Map<String, Object> c : cases) {
            String input = (String) c.get("input");
            List<String> sources = (List<String>) c.get("sources");
            String expectedOutput = (String) c.get("expected_output");
            boolean expectedChanged = (boolean) c.get("expected_changed");
            List<Map<String, Object>> expectedDetails =
                    (List<Map<String, Object>>) c.get("expected_details");

            tests.add(DynamicTest.dynamicTest(
                    "lookup: " + input + " [" + String.join(",", sources) + "]",
                    () -> {
                        ZhtwConverter conv = converterFor(sources);
                        LookupResult result = conv.lookup(input);

                        assertEquals(expectedOutput, result.getOutput(),
                                "Lookup output mismatch for '" + input + "'");
                        assertEquals(expectedChanged, result.isChanged(),
                                "Lookup changed mismatch for '" + input + "'");
                        assertEquals(expectedDetails.size(), result.getDetails().size(),
                                "Lookup details count mismatch for '" + input + "'");

                        for (int i = 0; i < expectedDetails.size(); i++) {
                            Map<String, Object> ed = expectedDetails.get(i);
                            ConversionDetail ad = result.getDetails().get(i);

                            assertEquals(ed.get("source"), ad.getSource(),
                                    "Detail[" + i + "] source mismatch for '" + input + "'");
                            assertEquals(ed.get("target"), ad.getTarget(),
                                    "Detail[" + i + "] target mismatch for '" + input + "'");
                            assertEquals(ed.get("layer"), ad.getLayer(),
                                    "Detail[" + i + "] layer mismatch for '" + input + "'");
                            assertEquals(((Number) ed.get("position")).intValue(),
                                    ad.getPosition(),
                                    "Detail[" + i + "] position mismatch for '" + input + "'");
                        }
                    }
            ));
        }
        return tests;
    }
}
