# PPE-BoK — PDS Synchronization Proposal

**Scope:** governance alignment after Chapters 000–012 Rev 1.0 review and Chapter 013 boundary integration  
**Status:** PROPOSAL ONLY — NO PDS / DOCTRINE CHANGE YET  
**Change class if approved:** D — PDS / Doctrine

## 1. Purpose

The existing PDS baseline already requires Design Basis discipline, traceability, standards validation, uncertainty visibility, engineering consistency and controlled review gates.

The reviewed manuscript has now made several governance concepts more explicit and more operational. This proposal identifies the minimum changes required to synchronize the PDS with the engineering controls already established in the book.

No existing PDS file is modified by this proposal.

## 2. Proposed doctrine-level additions

### PDS-SYNC-01 — Controlled holds

Add a formal definition of **controlled hold**:

> A material unresolved condition for which the available evidence is insufficient to close the affected engineering decision. The hold must identify owner, affected decisions, closure evidence and release condition.

Reason:

- Chapters 004–007 and later technical chapters now use controlled holds as a book-wide decision-control state.

### PDS-SYNC-02 — Decision disposition vocabulary

Adopt the canonical engineering disposition set:

- **GO**
- **CONDITIONAL GO**
- **NO-GO**

Clarify that CONDITIONAL GO requires explicit owned conditions and closure/monitoring logic.

### PDS-SYNC-03 — Reopen triggers and impact review

Add a rule:

> A technical decision remains valid only while its approved basis remains valid. Material change to process, requirement, Design Basis, evidence, standards basis, product configuration or service condition triggers an impact review and reopens affected decisions where necessary.

### PDS-SYNC-04 — Material / product / system hierarchy

Adopt the canonical distinction:

> **material qualification ≠ product conformity ≠ system suitability**

This should become a PDS-level interpretive rule for material/system chapters.

### PDS-SYNC-05 — Family-information hierarchy

Adopt:

> **family tendency → compound/grade evidence → qualified product/system evidence → project suitability**

Purpose:

- prevent family-level statements from being used as product qualification or project approval.

### PDS-SYNC-06 — Requirement lifecycle

Expand the PDS governance language to recognize controlled requirement states such as:

- proposed;
- approved;
- controlled hold;
- superseded;
- waived with authority;
- invalidated.

Requirement changes should include downstream impact review.

### PDS-SYNC-07 — Service-case register logic

Add a book-level expectation that relevant technical analysis consumes discrete, traceable service/design cases rather than isolated maxima.

Canonical logic:

`operating/lifecycle state → credible condition combination → duration/frequency/sequence → engineering case → affected check`

### PDS-SYNC-08 — Pressure terminology hierarchy

Adopt the Chapter 012 hierarchy:

> **material classification ≠ pipe/product pressure classification ≠ component rating ≠ project system allowable pressure**

Also state that PN, MOP, operating pressure, design pressure and test pressure are framework-specific and are not casual synonyms.

## 3. Proposed Quality & Validation Manual additions

### QVM-SYNC-01 — Hold register required before publication lock

Before a chapter enters publication baseline, all active standards/evidence/equation/expert/asset holds must be visible in either:

- the chapter review package; or
- the book-wide hold register.

A chapter may not be marked publication-ready while a material hold is hidden only in narrative notes.

### QVM-SYNC-02 — Cross-chapter canonical-home check

Expand Engineering Consistency review to ask:

- Does this chapter duplicate a method that has a canonical home elsewhere?
- If repetition exists, is it application-specific rather than a competing definition?

### QVM-SYNC-03 — Reopen verification

For changed content, the reviewer should confirm whether the change invalidates:

- requirements;
- Design Basis items;
- service cases;
- calculations;
- product/system selections;
- verification evidence;
- cross-references.

### QVM-SYNC-04 — Final numbering and asset gate

Before Level 6 / publication ready:

- final cross-references must be verified after final numbering;
- engineering asset register must show required figures/tables/checklists in final approved state.

## 4. Proposed Engineering Development Manual additions

### EDM-SYNC-01 — Controlled engineering record models

Recognize the recurring record types introduced by the reviewed chapters:

- Requirement Record;
- Design Basis Record;
- Service/Design Envelope Case Register;
- Uncertainty and Risk Decision Register;
- Fluid Characterization Package;
- Material-System Selection Record;
- Pressure Verification Record.

These are models, not mandatory identical templates for every project or chapter.

### EDM-SYNC-02 — Verification planning at decision creation

Add the rule that verification should be identified when a material engineering requirement/decision is created, not only at final review.

## 5. Proposed Style Guide additions

Only minimal governance-level terminology changes are proposed now; full presentation rules remain in the deferred editorial/visual pass.

Add controlled capitalization and spelling for:

- Design Basis;
- GO / CONDITIONAL GO / NO-GO;
- controlled hold;
- reopen trigger;
- impact review;
- service/design-envelope case;
- material qualification / product conformity / system suitability.

Do not yet freeze final chapter/Part numbering conventions.

## 6. Items intentionally not proposed

This proposal does **not** recommend:

- replacing the current Engineering Doctrine;
- changing the evidence hierarchy;
- weakening standards-first validation;
- turning chapter record examples into mandatory project templates;
- locking final Parts or chapter numbering;
- performing editorial/visual cleanup inside the PDS change.

## 7. Approval package

If approved, the PDS change should be integrated as a controlled D-class update in this order:

1. Engineering Doctrine — concise additions only where doctrine-level rules belong;
2. Quality & Validation Manual — validation and reopen gates;
3. Engineering Development Manual — recurring controlled engineering records;
4. Style Guide — canonical terminology only;
5. PDS README — baseline/version note and change summary if required.

Each file should be shown as a proposed diff/replacement before commit if the change is substantive.

## 8. Proposed disposition

**PDS synchronization need:** CONFIRMED  
**Technical manuscript basis:** ESTABLISHED  
**Governance change integrated:** NO  
**Next gate:** explicit approval before modifying PDS / Doctrine files.