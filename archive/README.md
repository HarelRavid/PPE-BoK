# PPE-BoK Archive

This directory preserves superseded, legacy or non-canonical project material that must remain available for traceability but must no longer be treated as active project guidance.

## Archive rule

A file belongs here when it is historically useful but one or more of the following apply:

- it has been superseded by a controlled PDS document;
- it uses a retired repository structure;
- it conflicts with the current source-of-truth hierarchy;
- it is a legacy snapshot retained only for provenance;
- its active location would create ambiguity about which document governs.

Archiving is **not deletion** and does not imply that the historical material was incorrect at the time it was created.

## Active source-of-truth hierarchy

For current work, use:

1. `BOOK_STRUCTURE.md` for the active working book architecture and continuation map;
2. `docs/PDS/` and `governance/` for development and configuration controls;
3. `chapters/` for canonical chapter source content;
4. `references/Standards-Register.md` for the central standards index;
5. `reviews/` for controlled engineering-review evidence and review templates;
6. `templates/` for current authoring/support templates.

Archived documents shall never override an active controlled document.

## Archive organization

- `legacy-book/` — retired manuscript directory structures and snapshots.
- `legacy-governance/` — superseded writing/governance guides.
- `legacy-structure/` — retired top-level structures or indexes.
- `legacy-templates/` — superseded authoring/review template snapshots.

When an archived item is referenced for historical recovery, its archived status must be stated explicitly.