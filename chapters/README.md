# Book Chapters

GitHub is the master source for the PPE-BoK manuscript. Each reviewed chapter is stored in an independent directory under `chapters/`.

```text
chapters/chapter-000-short-title/
├── chapter.md
├── references.md
├── review.md
├── notes.md
└── figures/
```

Not every chapter currently has every supporting file. A chapter is not considered publication-locked until its evidence, standards validation, technical review and final integration requirements are complete.

## Naming Rules

- Three-digit working chapter number.
- Short lowercase English title separated by hyphens.
- Main manuscript file: `chapter.md`.

## Current Reviewed Manuscript — Chapters 000–012

| Chapter | Title | Current status |
|---:|---|---|
| 000 | How to Use This Book | Rev 1.0 content review closed; final-lock holds may remain |
| 001 | Understanding Industrial Plastic Piping Systems | Rev 1.0 content review closed; final-lock holds may remain |
| 002 | The Engineering Decision Process | Rev 1.0 content review closed; final-lock holds may remain |
| 003 | Understanding Industrial Processes | Rev 1.0 content review closed; final-lock holds may remain |
| 004 | Defining Engineering Requirements | Rev 1.0 content review closed; final-lock holds may remain |
| 005 | Establishing the Design Basis | Rev 1.0 content review closed; final-lock holds may remain |
| 006 | Service Conditions and the Design Envelope | Rev 1.0 content review closed; final-lock holds may remain |
| 007 | Engineering Risk and Uncertainty | Rev 1.0 content review closed; final-lock holds may remain |
| 008 | Understanding Process Fluids | Rev 1.0 content review closed; final-lock holds may remain |
| 009 | Polymer Fundamentals for Industrial Plastic Piping | Rev 1.0 content review closed; final-lock evidence holds remain |
| 010 | Engineering Methodology for Material Selection | Rev 1.0 content review closed; final-lock evidence holds remain |
| 011 | Engineering Characteristics of Common Plastic Piping Materials | Rev 1.0 content review closed; final-lock evidence holds remain |
| 012 | Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating | Rev 1.0 content review closed; final-lock standards holds remain |

Chapter 009 was normalized into the canonical `chapters/chapter-009-polymer-fundamentals/` location during the book-wide integration pass.

## Status Meaning

- **Draft:** readable manuscript exists but substantive content review remains open.
- **Rev 1.0 content review closed:** approved content baseline exists; this does not imply standards-validation or publication lock.
- **Reviewed / technically reviewed:** defined technical review gates have been completed for the stated scope.
- **Standards validated:** standards-derived statements have been checked against authoritative current sources for the applicable scope.
- **Locked / publication baseline:** approved source text after required content, standards, evidence, integration and editorial gates; later changes require documented change control.

## Active Book-Wide Workstream

The sequential content review for Chapters 000–012 is complete.

Current work proceeds under:

`docs/BOOK-WIDE-INTEGRATION-PASS.md`

The final editorial / visual cleanup remains tracked separately in:

`docs/EDITORIAL-VISUAL-CLEANUP-BACKLOG.md`

No chapter may be treated as publication-complete solely because a heading, outline, PDF or content-review closure exists. The complete controlled manuscript and its required evidence package must be present in this repository.
