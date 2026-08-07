# PPE-BoK Architecture Specification

**Version:** 1.0  
**Status:** Released for Production

## Repository structure

The approved top-level architecture is:

- `/chapters` — chapter source content, one chapter per directory.
- `/docs` — supporting project documentation and chapter design briefs.
- `/templates` — approved templates used during development and review.
- `/assets` — controlled engineering assets and asset-production indexes.
- `/references` — standards register, bibliography and cross-book reference controls.
- `/governance` — PDS governance, configuration and readiness/completion criteria.

Legacy directories may remain until explicitly retired, but new PDS-controlled work shall use the structure above.

## Knowledge architecture

`Book → Part → Chapter → Investigation → Engineering Asset`

The chapter is the primary self-contained knowledge unit. Investigations are progressive internal sections and shall not each repeat chapter-level context.

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
