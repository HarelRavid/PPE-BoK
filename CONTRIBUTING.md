# PPE-BoK Contribution and Review Rules

## Governing system

All chapter development is governed by PDS 1.0. Read `docs/PDS/` and `governance/` before editing technical content.

## Human Approval Gate

No technical chapter content becomes repository baseline without explicit author approval.

Required sequence:

`Draft → Internal Review → Joint Review → Author Approval → Commit / PR → Merge → Baseline`

Do not make silent technical improvements to `main`.

## Chapter development

Before Engineering Development begins, the chapter must satisfy `governance/Definition-of-Ready.md`.

The chapter is the primary self-contained knowledge unit. Investigations build progressively and should not repeatedly restate chapter-level context.

Target approximately 60% engineering application and 40% engineering explanation across a chapter, adjusted to what is required to communicate the engineering point correctly.

## Standards

- Name the governing standard where it can be identified.
- Distinguish requirements, recommendations and engineering interpretation.
- Do not reproduce protected standards text beyond permitted use.
- During authoring, standards references may remain working references.
- After authoring is complete, every standards-derived statement must be rechecked directly against the authoritative source before publication approval.
- Record standards in `references/Standards-Register.md`.

## Equations and engineering assets

Every material equation includes symbols, units, assumptions, validity limits, source/derivation basis and common misuse where relevant.

Use controlled identifiers:

- `EQ-CCC-NNN`
- `FIG-CCC-NNN`
- `TAB-CCC-NNN`
- `WF-CCC-NNN`
- `EX-CCC-NNN`
- `DT-CCC-NNN`
- `CL-CCC-NNN`

## Versioning

Use chapter/document versions `1.0`, `1.1`, `1.2`, `2.0`.

A baselined chapter is not silently overwritten. Technical revisions require review and a controlled new version.

## Production order

Chapter 13 is the PDS pilot. After pilot acceptance, full-book redevelopment proceeds sequentially from Chapter 001 through Chapter 013 unless the author explicitly approves an exception.

## Definition of Done

A chapter cannot be baselined until it meets `governance/Definition-of-Done.md`, including Technical Review, independent numerical checks, Standards Validation, editorial review, joint review and explicit author approval.
