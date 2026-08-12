# PPE-BoK

**Plastic Piping Engineering Body of Knowledge**

PPE-BoK is an engineering reference for industrial plastic and thermoplastic piping systems. It is designed to support real engineering work through first-principles understanding, standards navigation, calculations, engineering assets, worked examples, verification steps and explicit engineering decisions.

## Source of truth

GitHub `main` is the official project baseline. Conversation drafts, working branches and unmerged pull requests are not official baselines.

Use the following active control documents:

- Working book architecture and continuation map: [`BOOK_STRUCTURE.md`](BOOK_STRUCTURE.md)
- PPE-BoK Development System (PDS): [`docs/PDS/`](docs/PDS/)
- Repository governance: [`governance/`](governance/)
- Central standards register: [`references/Standards-Register.md`](references/Standards-Register.md)
- Engineering review evidence and templates: [`reviews/`](reviews/)
- Repository metadata audit: [`docs/REPOSITORY-METADATA-AUDIT-2026-08-12.md`](docs/REPOSITORY-METADATA-AUDIT-2026-08-12.md)

## Active repository structure

- `chapters/` — canonical chapter source content, one chapter per directory.
- `docs/` — project documentation, PDS documents, Chapter Design Briefs and scope controls.
- `templates/` — current authoring and support templates.
- `assets/` — controlled engineering assets and asset indexes.
- `references/` — central standards register and shared reference controls.
- `reviews/` — chapter review packages and controlled review templates.
- `governance/` — architecture, configuration management and readiness/completion controls.
- `archive/` — superseded or legacy material retained for provenance; archived files are not active guidance.

Retired directory structures shall not remain in the active namespace merely for historical convenience. Historical material is preserved under `archive/`.

## Book architecture rule

The final chapter count is **topic-driven, not number-driven**. Working chapter numbers and Part boundaries remain provisional until the knowledge-scope coverage audit, technical review and editorial/architecture review are complete.

`BOOK_STRUCTURE.md` governs the current working continuation architecture.

## Production rules

- The chapter is the primary self-contained knowledge unit.
- Investigations are progressive engineering questions inside a chapter.
- Engineering decisions are the objective; theory is included to support correct application and judgement.
- Target approximately 60% engineering application / 40% engineering explanation where appropriate to the subject.
- Standards are navigated and applied, not reproduced.
- Standards-derived claims are rechecked against authoritative sources during the final Standards Validation gate.
- Equations and important engineering assets include assumptions, units, validity limits and source/derivation basis.
- No technical chapter content becomes an official baseline without the required review and explicit author approval.
- Working chapter numbers may change during final architecture review; controlled asset IDs are not silently reused after baselining.

## Engineering asset IDs

Examples: `EQ-013-001`, `FIG-013-002`, `TAB-013-001`, `WF-013-001`, `EX-013-001`, `DT-013-001`, `CL-013-001`.

## Current status

- Chapters 000–012 form the current early-book baseline/foundation on `main`.
- Chapter 009 is stored canonically under `chapters/chapter-009-polymer-fundamentals/`; the former `Book/` structure is archived.
- Chapter 013 — Polyethylene is the PDS pilot/reference implementation. Its redevelopment candidate contains the full Investigation 1–10 engineering arc, but publication closure still requires resolution of its branch/PR state, authoritative Standards Validation and the remaining publication gates.
- The recovered continuation architecture extends beyond Chapter 013. Working Chapter 014 is the next planned development unit after Chapter 013 closure.

See [`BOOK_STRUCTURE.md`](BOOK_STRUCTURE.md) for the full working roadmap and [`CHANGELOG.md`](CHANGELOG.md) for repository-level changes.
