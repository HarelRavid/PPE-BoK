# PPE-BoK — Book-Wide Integration Pass

**Scope:** Chapters 000–012 after approved Rev 1.0 content review  
**Branch:** `chapter-013-redevelopment`  
**Status:** INTEGRATION PASS OPEN  
**Rule:** no new substantive chapter-content change is integrated without the normal change-control route; this pass may directly normalize status/documentation records and may prepare proposed cross-chapter changes for approval.

## 1. Objective

The chapter-by-chapter content review of Chapters 000–012 is complete. The purpose of this pass is to verify that the approved chapters now operate as one coherent engineering book rather than thirteen individually strong chapters.

The integration pass checks:

- canonical terminology;
- chapter ownership and boundaries;
- handoffs and cross-references;
- repeated workflows and tables;
- evidence / standards holds;
- repository structure;
- PDS alignment;
- figure/table/equation placeholder consistency;
- deferred editorial and visual work.

## 2. Canonical book logic established by Chapters 000–012

The current manuscript now establishes the following main engineering chain:

`How to use the evidence`
→ `System definition`
→ `Engineering decision process`
→ `Process definition`
→ `Engineering requirements`
→ `Design Basis`
→ `Service / design envelope`
→ `Risk and uncertainty`
→ `Fluid characterization`
→ `Polymer/material behaviour`
→ `Material-system selection`
→ `Material-family characteristics`
→ `Long-term pressure verification`

This chain should remain the primary integration backbone until the final table of contents is frozen.

## 3. Canonical ownership map

| Topic / method | Canonical home |
|---|---|
| How to interpret requirements, evidence, equations, examples and standards | Chapter 000 |
| System boundaries and interfaces | Chapter 001 |
| Decision workflow and GO / CONDITIONAL GO / NO-GO | Chapter 002 |
| Process-definition inputs | Chapter 003 |
| Controlled engineering requirements | Chapter 004 |
| Design Basis integration / baseline control | Chapter 005 |
| Service/design-envelope case construction | Chapter 006 |
| Uncertainty / sensitivity / residual uncertainty / reopen logic | Chapter 007 |
| Controlled process-fluid characterization | Chapter 008 |
| Polymer behaviour and data interpretation | Chapter 009 |
| Controlled material-system selection | Chapter 010 |
| Family-level material characteristics | Chapter 011 |
| MRS / design stress / SDR / pressure-classification chain | Chapter 012 |

Cross-chapter edits should point to these homes rather than recreating parallel methods.

## 4. Canonical terminology to enforce globally

### Engineering decision language

Use consistently:

- Design Basis;
- requirement;
- assumption;
- controlled hold;
- verified / bounded / provisional evidence status where applicable;
- GO / CONDITIONAL GO / NO-GO;
- reopen trigger / impact review.

### Material / product / system hierarchy

Preserve the book-wide distinction:

> **material qualification ≠ product conformity ≠ system suitability**

Related material-family information should follow:

> **family tendency → compound/grade evidence → qualified product/system evidence → project suitability**

### Pressure hierarchy

Preserve the Chapter 012 distinction:

> **material classification ≠ pipe/product pressure classification ≠ component rating ≠ project system allowable pressure**

PN, MOP, operating pressure, design pressure and test pressure must remain framework-specific and should not be used as casual synonyms.

## 5. Integration findings

### INT-001 — Chapter 009 repository location is inconsistent

**Severity:** High  
**Finding:** Chapters 000–008 and 010–012 are under `chapters/`, while Chapter 009 remains under:

`Book/Part_02_Process_Definition_and_Requirements/Chapter_009_Polymer_Fundamentals/`

This conflicts with the repository naming rule documented in `chapters/README.md` and makes the `chapters/` directory structurally incomplete.

**Required action:** move the Chapter 009 manuscript, references and review package into a canonical `chapters/chapter-009-polymer-fundamentals/` directory during repository-normalization work, then repair internal references if needed.

### INT-002 — Chapter 009 legacy Part placement is no longer conceptually correct

**Severity:** Medium  
**Finding:** The legacy path places polymer fundamentals inside `Part_02_Process_Definition_and_Requirements`, while the reviewed architecture now places it after fluid characterization and before material selection.

**Required action:** treat the legacy Part path as repository history only; do not infer final book-Part architecture from it.

### INT-003 — `chapters/README.md` status table is stale

**Severity:** Medium  
**Finding:** It still reports Chapters 000–012 as uploaded/research-based drafts rather than approved Rev 1.0 content-review baselines.

**Required action:** update repository-status wording after integration status is defined. Avoid calling chapters `Locked` while standards / evidence holds remain.

### INT-004 — `BOOK-WIDE-REVIEW-PLAN.md` progress tracker is stale

**Severity:** Medium  
**Finding:** The tracker still shows Chapter 000 in review and the remaining chapters queued although the sequential content-review phase is complete.

**Required action:** close the content-review phase and point to this integration pass.

### INT-005 — Book structure file is intentionally provisional but now diverges from current architecture

**Severity:** Medium  
**Finding:** `BOOK_STRUCTURE.md` explicitly states that numbering and Parts are provisional, but its current working-chapter list starts at Chapters 77–80+ and does not represent the reviewed 000–012 architecture.

**Required action:** do not rewrite final TOC yet. Add a note or future integration task to reconcile the working structure after the next expansion architecture is decided.

### INT-006 — Cross-reference wording needs a dedicated verification pass

**Severity:** High  
**Finding:** Approved revisions now contain explicit handoffs among Chapters 001–012, while Chapter 000 correctly warns that numbering/grouping may still change.

**Required action:** build a cross-reference register and verify every chapter-number reference after repository normalization and before final numbering lock.

### INT-007 — Repeated canonical rules should have one wording baseline

**Severity:** Medium  
**Finding:** Several chapters intentionally repeat key book rules, especially material/product/system suitability, GO/CONDITIONAL GO/NO-GO, assumptions/holds and reopen logic.

**Required action:** preserve purposeful reinforcement but normalize the exact core wording and avoid independent variants that could later diverge in meaning.

### INT-008 — Asset placeholders need a global register

**Severity:** Medium  
**Finding:** The reviewed chapters introduced conceptual assets such as `FIG-001-001`, `FIG-003-001`, `FIG-004-001`, `FIG-005-001`, `FIG-006-001`, `FIG-007-001`, `FIG-008-001`, `FIG-009-001`, `FIG-010-001`, `FIG-011-001/002`, `FIG-012-001/002` and multiple `TAB-xxx-001` items.

**Required action:** create one book-wide figure/table register identifying owner chapter, purpose, status (`placeholder / drafted / final`), and whether the asset is canonical or illustrative.

### INT-009 — PDS doctrine is broadly aligned but needs synchronization with the new canonical controls

**Severity:** Medium  
**Finding:** The current Engineering Doctrine and Quality & Validation Manual already require Design Basis, traceability, uncertainty visibility, book consistency and standards validation. The reviewed chapters now add more explicit control vocabulary.

**Required action:** prepare a controlled PDS synchronization proposal covering, at minimum:

- controlled holds;
- GO / CONDITIONAL GO / NO-GO;
- reopen triggers / impact review;
- material qualification / product conformity / system suitability;
- requirements lifecycle;
- service-case register logic;
- pressure terminology hierarchy.

Because PDS changes are governance changes, they require explicit controlled approval under the Quality & Validation Manual.

### INT-010 — Standards holds must remain separate from content closure

**Severity:** High  
**Finding:** Content review is complete, but multiple chapters retain full-text / edition / specialist-review holds. The Quality & Validation Manual correctly separates authoring completion from standards validation.

**Required action:** create a single standards/evidence hold register before the final Lock phase. No content-review closure should be interpreted as standards-validation closure.

### INT-011 — Editorial / visual cleanup is now eligible to begin, but only after integration corrections

**Severity:** Low  
**Finding:** `docs/EDITORIAL-VISUAL-CLEANUP-BACKLOG.md` explicitly defers punctuation, spacing, heading consistency, visual placement and typography until Chapters 000–012 complete substantive review.

**Required action:** keep that backlog open until architecture, cross-reference, repository and terminology integration are complete; then execute it as a dedicated presentation pass.

### INT-012 — Chapter 013 must be reconnected to the reviewed 000–012 chain

**Severity:** High  
**Finding:** Chapter 013 was excluded from the sequential review because its redevelopment and standards-validation workflow were handled separately. Chapters 009–012 were subsequently clarified around polymer fundamentals, selection, family characteristics and pressure design.

**Required action:** perform a boundary-only integration check between Chapter 013 and Chapters 009–012 before continuing later material-family chapters. This is not a reopening of Chapter 013's completed redevelopment review unless a real conflict is found.

## 6. Proposed integration execution order

### Phase I — Repository and status normalization

1. close the outdated review-plan tracker;
2. normalize Chapter 009 repository location;
3. update `chapters/README.md` status language;
4. establish the canonical chapter inventory.

### Phase II — Cross-chapter architecture

5. verify chapter ownership and remove accidental duplicate methods;
6. normalize repeated canonical terminology;
7. build and verify cross-reference register;
8. boundary-check Chapter 013 against Chapters 009–012.

### Phase III — Assets and evidence control

9. create figure/table register;
10. create consolidated standards/evidence hold register;
11. classify chapters by current maturity without falsely marking them publication-locked.

### Phase IV — PDS synchronization

12. prepare proposed PDS updates;
13. obtain explicit approval for PDS / Doctrine changes;
14. integrate approved governance changes.

### Phase V — Editorial / visual cleanup

15. execute the existing final editorial & visual backlog;
16. replace conceptual figure placeholders with final assets later in the production sequence;
17. perform final punctuation, typography, label and presentation normalization.

## 7. Integration change-control classes

Use the Quality & Validation Manual classes:

- **A — Editorial:** presentation only;
- **B — Structural:** navigation, repository or chapter architecture;
- **C — Technical:** engineering meaning changes;
- **D — PDS / Doctrine:** governance methodology changes.

This integration pass may directly execute clearly non-controversial status-record updates. Structural repository changes should be recorded. Technical and PDS/Doctrine changes require the normal controlled review/approval route.

## 8. Current integration disposition

**Content review of Chapters 000–012:** COMPLETE  
**Standards validation:** NOT COMPLETE BOOK-WIDE  
**Book integration:** IN PROGRESS  
**Editorial / visual cleanup:** DEFERRED UNTIL INTEGRATION CORRECTIONS COMPLETE  
**Final numbering / Parts:** NOT LOCKED

## 9. Immediate next action

Begin Phase I with:

1. updating the completed book-wide review tracker;
2. normalizing Chapter 009 into the canonical `chapters/` structure;
3. updating the chapter inventory/status record;
4. then performing the cross-reference and terminology integration audit.
