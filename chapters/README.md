# Book Chapters

GitHub `main` is the master source for the PPE-BoK manuscript. Canonical chapter source content is stored under `/chapters`, one chapter per directory.

```text
chapters/chapter-000-short-title/
├── chapter.md          # canonical chapter narrative
├── references.md       # chapter source register where present
├── review.md           # chapter-local review/support record where present
├── notes.md            # unresolved working notes where present
└── figures/            # controlled/original figure source files where present
```

Formal PDS review packages may additionally be stored under `reviews/chapter-NNN/`.

Not every early draft currently has all supporting files. A chapter is not publication-complete merely because a readable manuscript exists.

## Naming rules

- Three-digit working chapter number in the directory name.
- Short lowercase English title separated by hyphens.
- Canonical manuscript file: `chapter.md`.
- Working chapter numbers may change during final architecture review; the active roadmap is `BOOK_STRUCTURE.md`.

## Current manuscript inventory on `main`

| Chapter | Title | Current `main` status |
|---:|---|---|
| 000 | How to Use This Book | Early-book baseline draft |
| 001 | Understanding Industrial Plastic Piping Systems | Early-book baseline draft |
| 002 | The Engineering Decision Process | Early-book baseline draft |
| 003 | Understanding Industrial Processes | Early-book baseline draft |
| 004 | Defining Engineering Requirements | Early-book baseline draft |
| 005 | Establishing the Design Basis | Early-book baseline draft |
| 006 | Service Conditions and the Design Envelope | Early-book baseline draft |
| 007 | Engineering Risk and Uncertainty | Early-book baseline draft |
| 008 | Understanding Process Fluids | Early-book baseline draft |
| 009 | Polymer Fundamentals for Industrial Plastic Piping | Canonicalized under `/chapters`; source register and review record present; further depth is planned elsewhere in the recovered architecture |
| 010 | Engineering Methodology for Material Selection | Research-based full draft; source register and review record present |
| 011 | Engineering Characteristics of Common Plastic Piping Materials | Research-based full draft; source register and review record present |
| 012 | Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating | Research-based full draft; source register and review record present |
| 013 | Polyethylene (PE) | Full redevelopment candidate exists on `chapter-013-redevelopment`; not yet a `main` chapter baseline; authoritative Standards Validation and remaining publication gates are still required |

## Working continuation

Working Chapters 014 onward are defined in `BOOK_STRUCTURE.md`. They are roadmap entries, not active manuscript directories until the applicable CDB and development work begin.

## Status interpretation

- **Baseline draft:** readable source exists on `main`; this does not imply publication readiness.
- **Research-based full draft:** substantive source and evidence/review support exist, but Definition of Done may remain open.
- **Redevelopment candidate:** controlled work exists on a branch/PR but has not yet become the official `main` chapter baseline.
- **Publication ready / released:** may be used only after all gates in `governance/Definition-of-Done.md` are satisfied and the approved revision is merged to `main`.

No chapter may be treated as complete solely because a heading, outline, PDF, branch or pull request exists. The complete approved manuscript and required review evidence must reach the official repository baseline.
