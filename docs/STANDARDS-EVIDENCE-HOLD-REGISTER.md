# PPE-BoK — Standards & Evidence Hold Register

**Scope:** current reviewed manuscript baseline, Chapters 000–013  
**Purpose:** separate content closure from standards/evidence closure  
**Status:** CONSOLIDATED REGISTER OPEN

## 1. Control principle

A chapter may be content-reviewed and approved while still carrying standards, evidence, equation, specialist-review, cross-reference, asset, or editorial holds.

The publication rule remains:

> **Content approval ≠ standards validation ≠ publication lock**

This register does not replace the chapter review packages. It consolidates the open final-lock work so those items cannot disappear when chapter prose is marked approved.

## 2. Hold classes

- **STD** — authoritative standard / edition / clause / terminology verification required.
- **EVD** — supporting evidence maturity, independent source or page-level support required.
- **EQV** — independent equation/example verification required.
- **EXP** — specialist or independent expert review required.
- **XREF** — cross-reference / numbering integration check required.
- **AST** — engineering figure/table/checklist asset requires finalization.
- **EDT** — final editorial / visual / punctuation / typography work.

## 3. Chapters 000–008

The Chapter 000–008 content-review phase is closed, but the book-wide review tracker explicitly records standards/evidence as complete **with controlled holds**, not publication lock.

For these chapters, the exact chapter-local hold detail remains owned by each chapter's `review.md` package. Before final lock, the consolidated standards-validation pass shall reopen those review packages and migrate any still-active items into this register at clause/source level.

| Chapters | Current consolidated status | Required final-lock action |
|---|---|---|
| 000–008 | CONTENT REVIEW CLOSED; CONTROLLED HOLDS REMAIN | Re-read each `review.md`; migrate active standards/evidence/expert/asset items before publication lock |

No additional specific normative claim is inferred here beyond the chapter-local review records.

## 4. Chapter 009 — Polymer Fundamentals

Open final-lock actions from the approved Chapter 009 review:

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-009-01 | EVD | Peer-reviewed support for viscoelasticity, creep and slow-crack-growth background | Appropriate peer-reviewed source(s) mapped to the relevant statements |
| H-009-02 | EVD | Page-level textbook support where available and appropriate | Authoritative textbook citation with page-level traceability |
| H-009-03 | EVD | Cross-check material-specific statements against later material-family chapters | Documented consistency review |
| H-009-04 | STD | Recheck temporally unstable standards editions before publication | Authoritative current-edition verification |
| H-009-05 | XREF | Final cross-reference verification after numbering/Parts lock | Final numbering audit |
| H-009-06 | AST/EDT | Figure rendering, table styling, punctuation and typography | Final production/editorial pass |

Repository-location normalization previously recorded for Chapter 009 has been completed in the book-integration pass and is no longer an open evidence hold.

## 5. Chapter 010 — Material Selection Methodology

Open final-lock actions from the approved Chapter 010 review:

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-010-01 | STD | Reconfirm current ISO 12162 edition/status | Authoritative standard metadata/full-text check |
| H-010-02 | STD | Reconfirm ISO 15494 replacement/current-edition status | Authoritative standard metadata/full-text check |
| H-010-03 | STD | Add clause-level citations when authoritative full text is available | Clause/table/annex traceability where normative precision is used |
| H-010-04 | AST/EXP | Complete and technically review original figures | Approved engineering artwork + technical review |
| H-010-05 | XREF | Update cross-references after final book numbering | Final numbering audit |
| H-010-06 | EXP | Independent senior engineering review | Recorded review disposition |
| H-010-07 | EDT | Final copyedit / visual / punctuation cleanup | Publication editorial pass |

## 6. Chapter 011 — Common Plastic Piping Materials

Open final-lock actions from the approved Chapter 011 review:

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-011-01 | STD | Clause-level review of purchased standards and amendments | Authoritative full-text validation |
| H-011-02 | STD | ISO 15494 status recheck immediately before release | Current authoritative edition/status |
| H-011-03 | EVD | Independent technical sources for each major material family | Source matrix with independent support |
| H-011-04 | EXP | Chemical-engineering review of family-level compatibility wording | Recorded specialist review |
| H-011-05 | EXP | Joining-specialist review | Recorded specialist review |
| H-011-06 | STD/EVD | Deeper standards mapping for specialty fluoropolymers | Standards/source mapping for PTFE/PFA/ECTFE scope as applicable |
| H-011-07 | XREF | GRP / FRP / RTRP glossary harmonization and final cross-reference verification | Glossary decision + numbering audit |
| H-011-08 | EXP/EDT | Independent expert review and final copyedit | Review closure + publication edit |
| H-011-09 | AST/EDT | Book-wide visual / punctuation / typography cleanup | Final production pass |

## 7. Chapter 012 — Long-Term Strength / MRS / SDR / Pressure Rating

Open standards/evidence actions retained by the approved Chapter 012 review:

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-012-01 | STD | Exact ISO 9080 lower-bound terminology / notation | Authoritative full-text clause/notation verification |
| H-012-02 | STD | Exact MRS classification / rounding / designation rules | ISO 12162 authoritative verification |
| H-012-03 | STD | Exact minimum/application design-coefficient requirements | Applicable authoritative standard(s) by service/application |
| H-012-04 | STD | Exact PN and MOP definitions and product-standard context | Product/application-standard full-text verification |
| H-012-05 | STD | Exact temperature / time / cumulative-exposure rules where stated normatively | Applicable product/design-standard verification |
| H-012-06 | STD | Current applicable product-standard parts / editions | Authoritative edition/status check |
| H-012-07 | STD/EVD | Maintain ISO versus ASTM/PPI terminology separation; no informal crosswalk | Controlled crosswalk only if supported by authoritative sources |
| H-012-08 | EVD | Non-PE product examples only if adequately supported | Appropriate product-standard/source basis |
| H-012-09 | EXP | Independent technical review | Recorded review disposition |
| H-012-10 | XREF/AST/EDT | Final figures, cross-references and presentation cleanup | Final production and numbering audit |

The pressure-equation algebra already reviewed at content stage remains separate from these normative terminology holds.

## 8. Chapter 013 — Polyethylene

The Chapter 013 gap-closure package explicitly retains multiple non-content holds.

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-013-01 | STD | PE100-RC recognition, qualification route, test route, acceptance criteria and pressure/design implications | Final authoritative standards validation |
| H-013-02 | AST | Consolidated `TAB-013-005 — PE pressure-design relationship reference` required by RDP/gap closure unless already added in later chapter work | Verify current manuscript; add/approve table if absent |
| H-013-03 | EQV | Worked Example A independent recalculation | Independent arithmetic/unit verification record |
| H-013-04 | EQV | Worked Example B verification method and independent review/reperformance | Formal disposition: numerical recalculation if numerical, otherwise independently reperformed decision-path verification |
| H-013-05 | STD | Equation/coefficient/marking/temperature standards hold points | Dedicated final standards-validation record |
| H-013-06 | EXP | Technical Review and resolution of review-generated changes | Completed Technical Review disposition |
| H-013-07 | EDT/AST | Academic/editorial/visual completion | Final publication review after technical/standards closure |

The current Chapter 013 metadata correctly states a standards-validation stage and should not be interpreted as publication lock.

## 9. Book-wide integration holds

| ID | Class | Hold | Closure evidence required |
|---|---|---|---|
| H-BW-01 | XREF | Verify all working chapter-number references after final numbering/Parts lock | Book-wide cross-reference report |
| H-BW-02 | AST | Reconcile every conceptual figure/table/checklist with `docs/BOOK-WIDE-ASSET-REGISTER.md` | Asset register shows final status |
| H-BW-03 | STD | Run one final authoritative standards-validation pass after authoring/integration is complete | Chapter-by-chapter standards validation record |
| H-BW-04 | EXP | Complete required specialist/independent reviews | Recorded dispositions |
| H-BW-05 | EDT | Execute `docs/EDITORIAL-VISUAL-CLEANUP-BACKLOG.md` only after integration corrections | Editorial/visual closure record |
| H-BW-06 | XREF | Reconcile Chapter 013 generic-method overlap with Chapters 009–012 through approved boundary edits | Approved integration edit or explicit no-change disposition |

## 10. Closure rule

A hold may be marked closed only when the evidence specified in the closure column exists.

Do not close a standards hold because:

- the current prose sounds correct;
- a secondary source agrees;
- an earlier edition used the same wording;
- a calculation is mathematically correct;
- a manufacturer document appears consistent;
- an AI-generated summary repeats the same claim.

Where the authoritative source conflicts with the manuscript, the manuscript must be corrected through normal change control.

## 11. Current disposition

**Content review:** CLOSED for Chapters 000–012  
**Chapter 013 engineering integration:** substantially complete; specific holds remain  
**Standards/evidence register:** ESTABLISHED AND OPEN  
**Publication lock:** NOT COMPLETE