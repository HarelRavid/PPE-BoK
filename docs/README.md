# PPE-BoK Documentation Index

This directory contains supporting project documentation. It is not the canonical location for chapter narrative; chapter source belongs under `/chapters`.

## Active document groups

### PDS — development methodology

[`PDS/`](PDS/) contains the released PPE-BoK Development System:

- Engineering Doctrine
- Engineering Development Manual
- Quality & Validation Manual
- Style Guide
- Chapter Design Briefs

### Book-scope recovery controls

- [`MASTER-KNOWLEDGE-SCOPE-MAP.md`](MASTER-KNOWLEDGE-SCOPE-MAP.md) — atomic knowledge-scope control used to prevent loss of historically intended depth.
- [`HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md`](HISTORICAL-KNOWLEDGE-SCOPE-RECOVERY.md) — recovery evidence, verified historical ranges and unresolved historical holds.

These documents support the active working architecture in root-level [`BOOK_STRUCTURE.md`](../BOOK_STRUCTURE.md). They do not freeze the final TOC.

### Repository audits

- [`REPOSITORY-METADATA-AUDIT-2026-08-12.md`](REPOSITORY-METADATA-AUDIT-2026-08-12.md) — audit and disposition record for non-content repository files, legacy structures and metadata synchronization.

## Governing hierarchy

For current work:

1. `BOOK_STRUCTURE.md` controls working book architecture and continuation.
2. `docs/PDS/` controls chapter development/review methodology.
3. `governance/` controls repository/configuration changes.
4. `chapters/` contains canonical manuscript source.
5. `references/Standards-Register.md` is the active central standards index.
6. `archive/` preserves superseded documents for provenance only.

A historical recovery document may describe an earlier planning state. When it conflicts with a later active architecture decision, retain the historical evidence but use `BOOK_STRUCTURE.md` for current working structure.
