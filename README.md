# PPE-BoK

**Plastic Piping Engineering Body of Knowledge**

PPE-BoK is being developed as an engineering reference for plastic piping and pressure equipment. The project is governed by the PPE-BoK Development System (PDS) and is intended to support real engineering work through standards navigation, calculations, engineering assets, worked examples and explicit design decisions.

## Source of truth

GitHub `main` is the official project baseline. Conversation drafts, working branches and unmerged pull requests are not official baselines.

The governing methodology is PDS 1.0:

- Core PDS documents: [`docs/PDS/`](docs/PDS/)
- Repository governance: [`governance/`](governance/)
- Central standards register: [`references/Standards-Register.md`](references/Standards-Register.md)

## Approved repository structure

- `chapters/` — chapter source content.
- `docs/` — supporting documentation and Chapter Design Briefs.
- `templates/` — approved authoring and review templates.
- `assets/` — controlled engineering assets and asset indexes.
- `references/` — standards register, bibliography and shared references.
- `governance/` — architecture, configuration management and readiness/completion controls.

Legacy directories may remain until explicitly retired, but new PDS-controlled work follows the structure above.

## Production rules

- The chapter is the primary self-contained knowledge unit.
- Target balance is approximately 60% engineering application / 40% engineering explanation, adjusted to the subject.
- Standards are navigated and applied, not reproduced.
- Every standards-derived statement is rechecked against the authoritative source after authoring and before publication approval.
- No technical chapter content becomes an official baseline without joint review and explicit author approval.
- Chapter versions use `1.0`, `1.1`, `1.2`, `2.0`.
- After the Chapter 13 pilot is validated, redevelopment proceeds sequentially from Chapter 001 through Chapter 013.

## Engineering asset IDs

Examples: `EQ-013-001`, `FIG-013-002`, `TAB-013-001`, `WF-013-001`, `EX-013-001`, `DT-013-001`, `CL-013-001`.

## Current status

PDS 1.0 is in final repository closeout. Chapter 13 is the pilot/reference implementation used to validate the production method before sequential full-book redevelopment.

See also [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CHANGELOG.md`](CHANGELOG.md), and [`BOOK_STRUCTURE.md`](BOOK_STRUCTURE.md).
