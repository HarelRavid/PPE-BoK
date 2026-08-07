# PPE-BoK Development System (PDS)

**Baseline:** 1.0  
**Status:** Released for Production

The PPE-BoK Development System governs how the book is engineered, authored, reviewed, validated and maintained.

## Governing documents

Core PDS documents in this directory:

1. [Engineering Doctrine](Engineering-Doctrine.md)
2. [Engineering Development Manual](Engineering-Development-Manual.md)
3. [Quality & Validation Manual](Quality-and-Validation-Manual.md)
4. [Style Guide](Style-Guide.md)

Repository-level governance controls are under [`/governance`](../../governance/), including Architecture Specification, Configuration Management, Definition of Ready and Definition of Done.

The central standards index is [`/references/Standards-Register.md`](../../references/Standards-Register.md).

## Core baseline decisions

- The **chapter** is the primary self-contained knowledge unit. Investigations are progressive internal sections.
- Target balance is approximately **60% engineering application / 40% engineering explanation**, adjusted to the engineering need.
- Standards are authoritative technical sources. PPE-BoK explains, navigates and applies them; it does not replace them.
- Every standards-derived statement is checked again against the authoritative source during the final Standards Validation pass after authoring is complete.
- Engineering assets are used when they increase engineering capability, not as decorative quotas.
- Asset IDs use controlled forms such as `EQ-013-001`, `FIG-013-002`, `TAB-013-001`.
- Versions use `1.0`, `1.1`, `1.2`, `2.0`.
- No technical chapter content becomes repository baseline without explicit author approval.
- GitHub `main` is the official source of truth.

## Development workflow

`Chapter Design Brief → Technical Outline → Engineering Development → Engineering Assets Integration → Technical Review → Standards Validation → Editorial/Style Review → Joint Review → Author Approval → Merge → Baseline`

## Production sequence

Chapter 13 — Polyethylene (PE) is the PDS pilot/reference chapter. After the pilot is accepted, full-book redevelopment proceeds sequentially from Chapter 001 through Chapter 013 unless the author explicitly approves an exception.

## Change control

PDS 1.0 is frozen for production. New methodology rules require a controlled PDS change and explicit approval; chapter-specific difficulties should first be solved within the existing PDS.
