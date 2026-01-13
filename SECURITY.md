# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please **DO NOT** create a public Issue.

Instead, send an email to: **rajatim@gmail.com**

### Email Format

**Subject:**
```
[SECURITY] zhtw - Brief description
```

**Example Subject:**
```
[SECURITY] zhtw - Command injection in CLI parser
```

**Body Template:**
```
## Vulnerability Report

**Version:** [e.g., 2.8.5]
**Component:** [e.g., CLI, Converter, Matcher]
**Severity:** [Critical / High / Medium / Low]

## Description

[Clear description of the vulnerability]

## Steps to Reproduce

1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected vs Actual Behavior

- Expected: [What should happen]
- Actual: [What actually happens]

## Proof of Concept (if applicable)

[Code snippet or command to reproduce]

## Suggested Fix (optional)

[Your suggestion for fixing]

## Your Information (optional)

- Name/Handle: [For acknowledgment in release notes]
- Want public credit: [Yes/No]
```

## Scope

This project is a text conversion tool. Security concerns include:

- Input validation (malicious input handling)
- File system operations (path traversal)
- Dependency vulnerabilities
- Code injection risks

## Acknowledgments

Security researchers who report valid vulnerabilities will be credited in release notes (with permission).
