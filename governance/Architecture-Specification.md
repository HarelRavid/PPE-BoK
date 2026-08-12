# PPE-BoK Architecture Specification

**Version:** 1.1  
**Status:** Released for Production

## Repository structure

The approved active top-level architecture is:

- `/chapters` — canonical chapter source content, one chapter per directory.
- `/docs` — supporting project documentation, PDS documents, Chapter Design Briefs and scope/recovery controls.
- `/templates` — approved active authoring/support templates.
- `/assets` — controlled engineering assets and asset-production indexes.
- `/references` — central standards register, bibliography and shared reference controls.
- `/reviews` — formal engineering-review templates and chapter review evidence.
- `/governance` — PDS governance, configuration and readiness/completion criteria.
- `/archive` — superseded or legacy material retained for provenance and historical recovery only.

Root control/orientation files include:

- `README.md` — repository orientation and current status.
- `BOOK_STRUCTURE.md` — active working book architecture and continuation map.
- `CHANGELOG.md` — repository-level change history.
- `CONTRIBUTING.md` — contribution and review rules.

Retired directory structures shall not remain active merely for historical convenience. Superseded material is preserved under `/archive` and does not override active controlled documents.

## Book architecture control

`BOOK_STRUCTURE.md` is the active architecture contract for Parts, working chapter scope, continuation sequencing, controlled historical holds and final-TOC freeze criteria.

The architecture is topic-driven rather than chapter-count-driven. Working chapter numbers and Part boundaries may change before final architecture freeze when required to preserve knowledge depth and engineering usability.

## Knowledge architecture

`Book → Part → Chapter → Investigation → Engineering Asset`

The chapter is the primary self-contained knowledge unit. Investigations are progressive internal engineering questions and shall not each repeat chapter-level context.

## Chapter source rule

Canonical chapter narrative belongs under:

`chapters/chapter-NNN-short-title/chapter.md`

Supporting chapter files may include `references.md`, `review.md`, `notes.md` and controlled figure/source files. Formal review packages may additionally reside under `reviews/chapter-NNN/`.

A legacy or archived copy is never the canonical chapter source.

## Versioning

PDS documents and chapter baselines use semantic-style document versions: `1.0`, `1.1`, `1.2`, `2.0`.

- `x.0` — released baseline or major technical/structural change.
- `x.y` — controlled revision that preserves the same major baseline.

## Engineering asset identifiers

Every controlled engineering asset uses a unique chapter-based identifier:

- Equation: `EQ-013-001`
- Figure: `FIG-013-001`
- Table: `TAB-013-001`
- Workflow: `WF-013-001`
- Worked Example: `EX-013-001`
- Decision Tree: `DT-013-001`
- Checklist: `CL-013-001`

Identifiers are permanent once baselined. Deleted or superseded IDs are not silently reused.

## Source-of-truth rule

GitHub `main` is the official repository baseline. Conversation drafts, working notes and branch content are not official until reviewed, explicitly approved by the author and merged to `main`.

Within `main`, active controlled documents take precedence over archived historical material. If active documents conflict, resolve the conflict through configuration/change control rather than relying on whichever file was read first.
