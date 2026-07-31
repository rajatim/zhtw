# Security Policy

## Supported Versions

Security fixes are provided for the latest stable release line.

| Version | Supported |
|---|---|
| 4.4.x | Yes |
| < 4.4 | No |

Users should upgrade to the latest published patch release before reporting a
problem that may already be fixed.

## Reporting a Vulnerability

Do not open a public Issue for a suspected security vulnerability.

Use [GitHub Private Vulnerability Reporting](https://github.com/rajatim/zhtw/security/advisories/new)
whenever possible. If that channel is unavailable, email `rajatim@gmail.com`
with the subject:

```text
[SECURITY] zhtw - Brief description
```

Include the following information when available:

- Affected zhtw version, SDK, operating system, and runtime
- Vulnerability type and expected impact
- Minimal steps or proof of concept needed to reproduce the issue
- Whether the report or your identity may be acknowledged publicly
- Any suggested fix or temporary mitigation

Do not include real credentials, customer data, private benchmark answers, or
other sensitive data unless the maintainer requests a secure transfer method.

## Scope

Security reports may cover:

- CLI input handling and command execution
- File reads, writes, path traversal, backups, and encoding handling
- Malformed dictionary or SDK data handling
- Dependency and build-chain vulnerabilities
- CI, release workflows, package publishing, and release artifacts
- Denial of service caused by crafted input
- Code injection or unsafe deserialization

Incorrect Chinese conversion is normally an accuracy bug, not a security
vulnerability. Report it through a regular Issue unless it creates a security
impact such as policy bypass, data corruption, or unsafe command execution.

## Disclosure

Please allow time to confirm and fix the problem before public disclosure. The
maintainer will coordinate disclosure and release notes with the reporter when
the vulnerability is valid.

Security researchers who report valid vulnerabilities will be credited with
permission.
