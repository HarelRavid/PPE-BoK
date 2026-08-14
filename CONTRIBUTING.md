# PPE-BoK Contribution and Review Rules

## Governing system

All chapter development is governed by PDS 1.0. Before editing technical content, read:

- `BOOK_STRUCTURE.md` — active working book architecture and continuation map;
- `docs/PDS/` — engineering-development doctrine, workflow, validation and style controls;
- `governance/` — repository architecture, configuration management and readiness/completion gates.

Archived material under `archive/` is retained for provenance only and does not override active controlled documents.

## Human Approval Gate

No technical chapter content becomes repository baseline without explicit author approval.

Required sequence:

`Draft → Internal Review → Joint Review → Author Approval → Commit / PR → Merge → Baseline`

Do not make silent technical improvements to `main`.

## Chapter development

Before Engineering Development begins, the chapter must satisfy `governance/Definition-of-Ready.md`, including an approved Chapter Design Brief (CDB).

The chapter is the primary self-contained knowledge unit. Investigations build progressively and should not repeatedly restate chapter-level context.

Target approximately 60% engineering application and 40% engineering explanation across a chapter, adjusted to what is required to communicate the engineering point correctly.

Working chapter numbers and Part boundaries may remain provisional until final architecture review. Do not rename or renumber controlled content merely to make the TOC visually tidy during active development.

## Standards

- Name the governing standard where it can be identified.
- Distinguish requirements, recommendations and engineering interpretation.
- Do not reproduce protected standards text beyond permitted use.
- During authoring, standards references may remain working references.
- After authoring is complete, every standards-derived statement must be rechecked directly against the authoritative source before publication approval.
- Record standards in `references/Standards-Register.md` and keep chapter-specific source records synchronized.
- Do not treat a repository-documented edition as proof that it is still the current edition unless the final Standards Validation gate has confirmed it.

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

Controlled asset IDs are not silently reused after baselining.

## Review records

- Formal chapter diagnostic/redevelopment reviews use the controlled templates under `reviews/templates/` where applicable.
- Chapter-specific review evidence belongs under `reviews/chapter-NNN/` or the chapter support files as defined by the applicable CDB/workflow.
- Review records are evidence of decisions and closure; they are not substitutes for the chapter itself.

## Versioning

Use chapter/document versions `1.0`, `1.1`, `1.2`, `2.0` where a controlled revision is required.

A baselined chapter is not silently overwritten. Technical revisions require review and a controlled new version.

## Production order

Chapter 013 is the PDS pilot/reference implementation. Its publication closure remains a controlled prerequisite before starting the next new working chapter.

After Chapter 013 closure, development proceeds according to the active `BOOK_STRUCTURE.md`, beginning with the approved CDB for Working Chapter 014 unless the author explicitly approves another controlled sequence.

The book is topic-driven rather than chapter-count-driven. Final numbering is not a production target.

## Definition of Done

A chapter cannot be baselined until it meets `governance/Definition-of-Done.md`, including Technical Review, independent numerical checks, Standards Validation, editorial review, joint review and explicit author approval.
