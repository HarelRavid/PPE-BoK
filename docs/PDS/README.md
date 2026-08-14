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

The active working book architecture is [`/BOOK_STRUCTURE.md`](../../BOOK_STRUCTURE.md).

The central standards index is [`/references/Standards-Register.md`](../../references/Standards-Register.md).

Superseded project guidance is retained under [`/archive`](../../archive/) and does not override the released PDS.

## Core baseline decisions

- The **chapter** is the primary self-contained knowledge unit. Investigations are progressive internal engineering questions.
- Engineering decisions are the objective; explanation, theory and standards navigation support defensible use.
- Target balance is approximately **60% engineering application / 40% engineering explanation**, adjusted to the engineering need.
- Standards are authoritative technical sources. PPE-BoK explains, navigates and applies them; it does not replace them.
- Every standards-derived statement is checked again against the authoritative source during the final Standards Validation pass after authoring is complete.
- Engineering assets are used when they increase engineering capability, not as decorative quotas.
- Asset IDs use controlled forms such as `EQ-013-001`, `FIG-013-002`, `TAB-013-001`.
- Versions use `1.0`, `1.1`, `1.2`, `2.0` where controlled revisions are required.
- No technical chapter content becomes repository baseline without explicit author approval.
- GitHub `main` is the official source of truth.
- Working chapter numbers and final Part boundaries are controlled by `BOOK_STRUCTURE.md` and remain unfrozen until architecture/editorial review.

## Development workflow

`Chapter Design Brief → Technical Outline → Engineering Development → Engineering Assets Integration → Technical Review → Standards Validation → Editorial/Style Review → Joint Review → Author Approval → Merge → Baseline`

## Production sequence

Chapter 013 — Polyethylene (PE) remains the PDS pilot/reference implementation. Its redevelopment candidate contains the complete engineering arc developed during the pilot, but publication closure still requires resolution of the active branch/PR state, authoritative Standards Validation and the remaining Definition-of-Done gates.

After Chapter 013 publication closure, the next new development unit is the author-approved CDB for **Working Chapter 014**, followed by continuation according to `BOOK_STRUCTURE.md`.

The recovered book architecture extends well beyond Chapter 013. The PDS does not impose a target chapter count.

## Change control

PDS 1.0 is released for production. New methodology rules require a controlled PDS change and explicit approval; chapter-specific or architecture-specific issues should first be solved within the current PDS and `BOOK_STRUCTURE.md` rather than by silently changing the methodology.
