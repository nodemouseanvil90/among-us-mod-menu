# Security Policy

## Scope

`among-us-mod-menu` is a client-side desktop utility. It does **not** ship
network exploits, lobby-crashing vectors, or anti-cheat bypasses.

## Reporting

Report memory-safety issues, unsafe offset writes, or privilege escalation in
the native helper via a private security advisory. Do not open public issues
for exploitable findings.

## Supported versions

| Version | Supported |
|---------|-----------|
| 2026.x  | yes       |
| 2025.x  | no        |

## Known constraints

- The injector requires the game process to be launched by the same user.
- Offset tables are validated against a hash manifest before use.