package zhtw

import (
	"crypto/sha256"
	"fmt"
)

func legacyCustomRuleID(source, target string) string {
	canonical := fmt.Sprintf(
		`{"rule_class":"custom","source":%s,"source_locale":"cn","target":%s}`,
		quoteJSONString(source), quoteJSONString(target),
	)
	digest := sha256.Sum256([]byte(canonical))
	return fmt.Sprintf("legacy:cn:custom:%x", digest[:12])
}
