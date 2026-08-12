# PPE-BoK — Book-Wide Review Plan

**Scope:** Chapters 000–012  
**Reference maturity benchmark:** Chapter 013 redevelopment / Technical Review / public-source Standards Validation workflow  
**Review mode:** sequential, chapter-by-chapter  
**Change-control rule:** no substantive chapter rewrite is committed as an approved revision without explicit user approval of the proposed chapter revision.

## 1. Objective

Perform a full review of every existing manuscript chapter before further expansion of the book, using a consistent engineering review method and avoiding chapter-to-chapter skipping.

The review is intended to answer, for each chapter:

- Is the chapter doing the job assigned to it in the book architecture?
- Is the engineering content correct, useful and sufficiently bounded?
- Are the chapter boundaries clean relative to adjacent chapters?
- Are equations, units, examples and standards claims adequately controlled?
- Are there missing engineering decision tools, tables, workflows or failure lenses?
- What should be retained, augmented, restructured or rewritten?

## 2. Review order

The review proceeded strictly in manuscript order:

| Order | Chapter | Title | Initial repository status |
|---:|---:|---|---|
| 1 | 000 | How to Use This Book | Full draft uploaded |
| 2 | 001 | Understanding Industrial Plastic Piping Systems | Full draft uploaded |
| 3 | 002 | The Engineering Decision Process | Full draft uploaded |
| 4 | 003 | Understanding Industrial Processes | Full draft uploaded |
| 5 | 004 | Defining Engineering Requirements | Full draft uploaded |
| 6 | 005 | Establishing the Design Basis | Full draft uploaded |
| 7 | 006 | Service Conditions and the Design Envelope | Full draft uploaded |
| 8 | 007 | Engineering Risk and Uncertainty | Full draft uploaded |
| 9 | 008 | Understanding Process Fluids | Full draft uploaded |
| 10 | 009 | Polymer Fundamentals for Industrial Plastic Piping | Research-based draft uploaded |
| 11 | 010 | Engineering Methodology for Material Selection | Research-based full draft uploaded |
| 12 | 011 | Engineering Characteristics of Common Plastic Piping Materials | Research-based full draft uploaded |
| 13 | 012 | Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating | Research-based full draft uploaded |

Chapter 013 was excluded from this sequence because its redevelopment/review stage was separately closed with documented controlled standards holds.

## 3. Per-chapter review sequence

Each chapter was reviewed using the same order of operations.

### Gate A — File and evidence inventory

- manuscript file(s);
- references / research package where present;
- review notes where present;
- figures / assets;
- existing PDS/CDB/RDP/EDR artifacts if applicable;
- standards sources relied upon by the chapter.

### Gate B — Architecture and scope review

- chapter purpose;
- reader outcomes;
- relationship to preceding/following chapters;
- duplication / missing handoffs;
- material that belongs elsewhere;
- material that is unexpectedly absent.

### Gate C — Technical review

As applicable:

- engineering physics;
- terminology;
- assumptions and applicability limits;
- equations and derivations;
- units and conversions;
- examples and recalculation;
- tables / decision logic;
- failure-mechanism treatment;
- practical engineering usefulness.

### Gate D — Standards / evidence review

- current source identity and edition where material;
- whether a statement is normative, explanatory or project-specific;
- unsupported numerical values;
- ambiguous coefficient / factor use;
- outdated or secondary-source dependence;
- controlled holds requiring authoritative full text.

### Gate E — Editorial and academic review

- progression and readability;
- repeated explanations;
- overstatement / false precision;
- weak transitions;
- terminology consistency across the book;
- citation/source discipline.

### Gate F — Gap Register and disposition

Each chapter received a gap register with severity and disposition:

- **RETAIN** — technically and structurally sound;
- **AUGMENT** — core chapter is sound but requires additional engineering depth/assets;
- **RESTRUCTURE** — content is largely useful but organization/boundaries require material change;
- **REWRITE** — current chapter cannot efficiently reach the required standard through incremental edits.

### Gate G — Revision proposal and approval

For substantive approved changes:

1. present review findings;
2. present recommended revision plan;
3. obtain explicit user approval;
4. create a revision artifact/version;
5. integrate only the approved scope;
6. review the revision before proceeding to the next chapter.

## 4. Book-wide consistency checks carried across chapters

During every chapter review, a cross-chapter watchlist was maintained for:

- Design Basis terminology;
- hierarchy between material, product and system qualification;
- MRS / design stress / SDR / pressure terminology;
- PFA / MOP / PN distinctions;
- standards-navigation style;
- equation metadata and unit conventions;
- evidence versus inference;
- treatment of uncertainty and engineering judgement;
- chapter boundaries and cross-references;
- repeated tables/workflows that should have one canonical home.

These items now continue under `docs/BOOK-WIDE-INTEGRATION-PASS.md`.

## 5. Final progress tracker — content-review phase

| Chapter | Inventory | Architecture | Technical | Standards/evidence | Editorial/academic | Gap register | Revision approved | Status |
|---:|---|---|---|---|---|---|---|---|
| 000 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 001 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 002 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 003 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 004 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 005 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 006 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 007 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 008 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 009 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 010 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 011 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |
| 012 | Complete | Complete | Complete | Complete with controlled holds | Complete | Complete | Yes | REV 1.0 CONTENT REVIEW CLOSED |

## 6. Phase closure

The sequential **content-review phase for Chapters 000–012 is complete**.

This closure does **not** mean that all chapters are publication-locked. Controlled standards, evidence, expert-review, asset, cross-reference and editorial actions remain open where recorded in chapter review packages.

The active book-wide workstream is now:

> **Book-wide integration → standards/evidence consolidation → PDS synchronization → editorial/visual cleanup → final lock workflow**

See:

`docs/BOOK-WIDE-INTEGRATION-PASS.md`

## 7. Review discipline retained after closure

The integration pass must not silently reopen approved technical content. If integration reveals a genuine engineering conflict or content error, it becomes a new controlled finding and follows the normal approval/change-control process.
