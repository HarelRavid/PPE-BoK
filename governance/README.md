# PPE-BoK Governance

**PDS Version:** 1.0  
**Status:** Released for Production

This directory contains the repository-level governance controls for PPE-BoK.

## Canonical governance set

- `Architecture-Specification.md` — active repository/source layout and source-of-truth rules.
- `Configuration-Management.md` — controlled items, change classes, archive control and development sequence.
- `Definition-of-Ready.md` — entry gate before Engineering Development.
- `Definition-of-Done.md` — completion/publication gate for a chapter.

The core PDS documents remain under `docs/PDS/`:

- `Engineering-Doctrine.md`
- `Engineering-Development-Manual.md`
- `Quality-and-Validation-Manual.md`
- `Style-Guide.md`

The active book architecture and working continuation sequence are controlled separately by root-level `BOOK_STRUCTURE.md`.

The two PDS/governance locations plus `BOOK_STRUCTURE.md` form the active control environment:

- PDS defines **how** chapters are engineered and reviewed.
- Governance defines **how repository/configuration changes are controlled**.
- `BOOK_STRUCTURE.md` defines **what the working book contains and how the continuation is organized**.

Superseded guidance belongs under `archive/` and does not override this active control set.

No technical chapter content becomes official until it passes the applicable Human Approval Gate and is merged to `main`.
