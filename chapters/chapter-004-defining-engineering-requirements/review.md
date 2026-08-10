# Chapter 004 — Review Package

**Chapter:** 004 — Defining Engineering Requirements  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT

## 1. Review basis

Reviewed sources:

- `chapters/chapter-004-defining-engineering-requirements/chapter.md`;
- approved Chapter 003 Rev 1.0 for upstream process-definition boundary;
- `chapters/chapter-005-establishing-the-design-basis/chapter.md` for downstream Design Basis handoff;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims. The review evaluates requirements architecture, traceability, verification, source hierarchy, change control, and the boundary between process definition and Design Basis.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — complete readable draft.

### Not present before this review

- `review.md`;
- `references.md`;
- `notes.md`;
- requirements workflow / traceability assets.

### Evidence dependency

Chapter 004 is methodological rather than calculation-heavy. It contains no equations, standards clauses or design coefficients. The key quality question is whether it teaches the reader to turn process facts and external obligations into requirements that are clear, testable, traceable, prioritized, and controlled through change.

**Gate A result: PASS WITH REQUIREMENTS-CONTROL GAPS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter establishes several sound principles:

- requirements define what the system must accomplish;
- requirements should describe required performance rather than prematurely prescribe a solution;
- requirements arise from process, regulation, standards, project obligations, safety, environment, operations, inspection, maintenance and lessons learned;
- conflicts among requirement sources must be resolved explicitly;
- functional, performance, environmental, operational, maintenance/inspection and safety requirements all matter;
- requirements must evolve with project change;
- every major engineering decision should be traceable to approved requirements;
- acceptance verification should be defined rather than assumed.

The PE100 example is especially useful because it cleanly separates a performance requirement from a design choice.

### 3.2 Boundary with Chapter 003

Chapter 003 now owns the process definition: boundary, process data, operating states, time history, evidence status, local conditions and process-change triggers.

Chapter 004 should therefore not re-characterize the process in depth. Its job is to transform approved process facts and other governing inputs into explicit engineering requirements.

The current draft generally respects this boundary, but the revised chapter should make the transformation logic explicit:

`process fact / obligation → requirement statement → verification method → downstream Design Basis input`

### 3.3 Boundary with Chapter 005

Chapter 005 owns the Design Basis as the integrated technical foundation of conditions, assumptions, constraints, codes and performance requirements.

Chapter 004 should therefore stop before assembling the complete Design Basis. It should produce a controlled requirements set that Chapter 005 can consume.

This distinction is important:

- Chapter 003 asks: **What is true or credibly expected about the process?**
- Chapter 004 asks: **What must the piping system do or satisfy because of those facts and obligations?**
- Chapter 005 asks: **What complete technical basis governs the design?**

The current manuscript implies this sequence but does not yet make it canonical.

### 3.4 Missing chapter-level functions

The following are missing or underdeveloped:

1. **requirement anatomy** — identifier, statement, source, owner, rationale, verification method, status and change trigger;
2. **shall / should / preference distinction** — mandatory requirement versus target/guidance versus preference;
3. **requirement quality criteria** — clear, singular, bounded, verifiable, solution-neutral where appropriate, and free of hidden assumptions;
4. **requirement conflicts and precedence** — current text says conflicts must be resolved but provides no resolution workflow;
5. **derived requirements** — engineering requirements often arise from analysis rather than direct stakeholder wording;
6. **assumptions versus requirements** — assumptions should not be disguised as requirements;
7. **verification planning** — every important requirement should identify how compliance will be demonstrated;
8. **requirements traceability matrix concept** — source → requirement → design response → verification;
9. **status and approval control** — proposed / approved / superseded / hold / waived-with-authority should be visible;
10. **change impact** — changed requirement should reopen affected Design Basis elements and downstream decisions, not merely update a document.

**Gate B result: PASS — TARGETED AUGMENTATION REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The following should remain substantially intact:

- requirements define the problem before detailed design;
- performance requirements should be preferred over premature solution prescription;
- functional, performance, environmental, operational, maintenance/inspection and safety requirements are distinct but interacting categories;
- requirements should be measurable or verifiable where practical;
- traceability supports design review, management of change, commissioning and failure investigation;
- maintenance and inspection requirements can materially affect system architecture;
- safety is broader than pressure containment.

### 4.2 Requirement versus design decision needs stronger treatment

The sodium-hydroxide example is good, but the chapter should make the distinction canonical.

A requirement answers:

> What outcome, condition, limit or capability must be satisfied?

A design decision answers:

> Which technical solution is selected to satisfy the requirement?

Some requirements may legitimately prescribe a solution when imposed by law, adopted code, owner standard, qualified technology basis, interface constraint or project decision. The chapter should therefore avoid implying that all prescriptive requirements are bad.

**Recommended rule:** avoid premature prescription unless the prescription itself is a governing requirement with an identifiable source and authority.

### 4.3 Requirement quality needs an explicit test

A technically useful requirement should normally be:

- identifiable;
- unambiguous enough for the decision being made;
- bounded by applicable conditions;
- verifiable;
- traceable to a source or derived basis;
- stated at the correct level of abstraction;
- free from hidden assumptions;
- consistent with higher-priority requirements.

The chapter currently says “measurable or verifiable wherever practical,” but it should show the reader how to judge whether a requirement is usable.

### 4.4 “Cumulative cycles may be more important” is too broad

The statement is directionally useful, but as written it can sound universal.

**Recommended action:** align with Chapter 003 language: cumulative cycling can govern some damage mechanisms and should be specified where relevant.

### 4.5 Requirement sources need authority and ownership

The source list is good, but all sources do not have equal authority.

The revised chapter should distinguish, at minimum:

- mandatory legal/regulatory/code requirements;
- adopted project / owner requirements;
- derived engineering requirements;
- manufacturer constraints within applicable scope;
- stakeholder preferences or targets.

This follows Chapter 000 governance without turning Chapter 004 into a legal hierarchy chapter.

### 4.6 Derived requirements are missing

Many requirements are not handed to the engineer directly.

Examples:

- a process flow target may derive a pressure-loss requirement;
- an equipment nozzle load limit may derive a flexibility/support requirement;
- a contamination limit may derive material, cleaning and traceability requirements;
- a maintenance philosophy may derive isolation, drainability and access requirements.

The chapter should teach that derived requirements need the same traceability as externally imposed requirements.

### 4.7 Verification should be planned with the requirement

The current chapter correctly warns against failing to define how acceptance will be verified, but this deserves first-class treatment.

A requirement is stronger when the verification route is identified at creation:

- calculation;
- document review;
- inspection;
- test;
- qualification record;
- commissioning check;
- operational demonstration;
- combined evidence.

This should connect cleanly to Chapter 002 verification categories.

**Gate C result: PASS WITH REQUIREMENTS-CONTROL AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

Chapter 004 should remain standards-neutral and should not reproduce code clauses.

The standards/evidence function here is to teach **how a standards obligation becomes a controlled requirement**.

Recommended rules:

- identify the governing source and edition where material;
- distinguish mandatory requirements from explanatory guidance;
- do not convert a secondary summary into a normative project requirement without checking the authoritative source;
- record requirement precedence/conflict resolution where multiple sources apply;
- retain a controlled hold when the authoritative basis is unresolved;
- do not silently downgrade a requirement into a preference because compliance is inconvenient;
- do not silently upgrade a preference into a mandatory technical requirement without authority.

**Gate D result: AUGMENT.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- concise and readable;
- strong opening distinction between requirements and solutions;
- useful category structure;
- practical maintainability and safety examples;
- good high-level traceability message;
- no premature equations or standards catalogue.

### Editorial gaps

1. No reader outcomes.
2. No canonical requirements workflow / traceability visual.
3. Requirement categories are useful, but the chapter lacks a canonical “minimum requirement record.”
4. No explicit requirement-quality checklist.
5. No distinction between mandatory requirement, target, preference and assumption.
6. Conflict resolution is mentioned but not operationalized.
7. Verification planning is too late and too brief.
8. Change control lacks explicit downstream reopen logic.
9. The handoff to Chapter 005 is implicit rather than explicit.

**Gate E result: PASS — TARGETED AUGMENTATION.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-004-01 | High | No canonical requirement anatomy / minimum record | Add requirement record model |
| GAP-004-02 | High | Mandatory requirement, target, preference and assumption are not distinguished | Add requirement-type/status distinctions |
| GAP-004-03 | High | No explicit requirement quality criteria | Add requirement-quality test |
| GAP-004-04 | High | Conflict/precedence resolution stated but not operationalized | Add bounded conflict-resolution workflow |
| GAP-004-05 | High | Derived requirements not explicitly taught | Add derived-requirements subsection |
| GAP-004-06 | High | Verification route is not tied to requirement creation | Add verification-planning rule |
| GAP-004-07 | Medium | No source/owner/authority field for requirements | Add provenance/ownership fields |
| GAP-004-08 | Medium | No requirements traceability matrix concept | Add source → requirement → design response → verification mapping |
| GAP-004-09 | Medium | Requirement lifecycle/status control not explicit | Add proposed / approved / hold / superseded / waived-with-authority model |
| GAP-004-10 | High | Change control does not explicitly reopen Design Basis/downstream decisions | Add impact/reopen rule |
| GAP-004-11 | Medium | Prescriptive requirement discussion is too binary | Clarify legitimate prescriptive requirements when imposed by authority or project basis |
| GAP-004-12 | Low | Cumulative-cycle statement too broad | Qualify as mechanism-dependent |
| GAP-004-13 | Low | No reader outcomes | Add concise outcomes |
| GAP-004-14 | Medium | No canonical requirements workflow visual | Add `FIG-004-001` conceptual traceability workflow |
| GAP-004-15 | Medium | Current requirement→consequence table lacks verification/traceability dimension | Expand or reframe table |
| GAP-004-16 | Low | Closing handoff to Chapter 005 is weak | Add explicit transition to Design Basis |

---

## 8. Disposition

# AUGMENT

The current chapter is structurally sound and should **not** be rewritten from scratch.

Its strongest material — performance-vs-solution distinction, requirement sources, requirement categories, maintainability/safety treatment and traceability principle — should remain.

The main revision is to turn “requirements” from a list of good intentions into **controlled engineering objects** that have identity, source, authority, verification, status, traceability and change impact.

---

## 9. Proposed Chapter 004 Rev 1.0 scope

Recommended revision package:

1. Retain the existing architecture and most current prose.
2. Add concise reader outcomes.
3. Add **Requirement Anatomy / Minimum Requirement Record** with:
   - unique ID;
   - requirement statement;
   - type/category;
   - source / owner / authority;
   - rationale or derived basis;
   - applicable conditions;
   - verification method;
   - status;
   - change trigger / affected downstream item.
4. Add a distinction among:
   - mandatory requirement;
   - engineering requirement;
   - target / objective;
   - stakeholder preference;
   - assumption / unresolved hold.
5. Add a requirement-quality test: clear, bounded, traceable, verifiable, solution-neutral where appropriate, singular enough to assess, and free of hidden assumptions.
6. Clarify that prescriptive requirements are legitimate when they are themselves governing requirements with identifiable authority; the problem is **premature unsupported prescription**, not prescription in all cases.
7. Add **Derived Requirements** and show how process facts and interfaces generate downstream engineering requirements.
8. Add a bounded **Conflict and Precedence Resolution** workflow aligned with Chapter 000 governance.
9. Add verification planning at requirement creation, aligned with Chapter 002 verification categories.
10. Add a compact requirements traceability model:
   - `source / process fact → requirement → design response → verification evidence → disposition`.
11. Add `FIG-004-001 — Requirements Definition and Traceability Workflow` conceptual placeholder.
12. Reframe the existing consequence table to include requirement category and verification route where useful.
13. Qualify cumulative-cycle wording as mechanism-dependent.
14. Add requirement status/lifecycle control: proposed / approved / controlled hold / superseded / waived-with-authority where applicable.
15. Add explicit change-impact rule: a material requirement change reopens affected Design Basis elements and downstream decisions.
16. Add explicit handoff to Chapter 005 as the chapter that integrates the approved requirements with process conditions, assumptions, constraints and governing standards into the Design Basis.
17. Keep the chapter methodological; do not turn it into a project specification template or standards catalogue.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this review.

If the revision scope above is approved, prepare **Chapter 004 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 005.
