# Chapter 005 — Review Package

**Chapter:** 005 — Establishing the Design Basis  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT / BOUNDARY RESTRUCTURE

## 1. Review basis

Reviewed sources:

- `chapters/chapter-005-establishing-the-design-basis/chapter.md`;
- approved Chapter 004 Rev 1.0 for upstream controlled-requirements handoff;
- `chapters/chapter-006-service-conditions-and-design-envelope/chapter.md` for downstream service-envelope boundary;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims. The review evaluates Design Basis architecture, governance, lifecycle control, internal consistency, and separation from the dedicated service-conditions/design-envelope chapter.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — complete readable draft.

### Not present before this review

- `review.md`;
- `references.md`;
- `notes.md`;
- Design Basis workflow / minimum-record assets.

### Evidence dependency

Chapter 005 is methodological. It contains no equations, clause-level standards claims, or numerical design coefficients. Its main quality burden is whether it defines the Design Basis as a controlled engineering baseline rather than repeating process-definition and service-envelope content already owned by Chapters 003, 004 and 006.

**Gate A result: PASS WITH DESIGN-BASIS-CONTROL GAPS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The current chapter establishes several strong principles:

- the Design Basis is the documented technical foundation for the system;
- nominal process data are insufficient;
- operating conditions and design conditions are not the same thing;
- design margins should not be arbitrary;
- assumptions must be explicit;
- governing laws, codes, standards, specifications and manufacturer limits should be identified;
- the Design Basis is a living document subject to management of change;
- incomplete Design Basis information can generate downstream design failures;
- a minimum Design Basis content list is already present.

This is the correct chapter role.

### 3.2 Boundary with Chapter 004

Chapter 004 now produces a controlled requirements set with source, authority, status, verification route and change impact.

Chapter 005 should consume those approved requirements rather than redefine them.

The canonical relationship should become:

`Process definition + approved requirements + governing constraints + assumptions + design philosophy + unresolved holds → Design Basis baseline`

The current draft implies this relationship but does not yet make the Design Basis assembly process explicit.

### 3.3 Boundary with Chapter 006

The largest architecture issue is overlap with Chapter 006.

Chapter 005 currently contains substantial material on:

- operating versus design conditions;
- the design envelope;
- pressure, temperature, flow, chemistry, phase, time and load dimensions.

Chapter 006 is already the dedicated chapter for **Service Conditions and the Design Envelope** and develops these topics in greater detail.

Chapter 005 should therefore own **integration and control**, while Chapter 006 owns **characterization and representation of service conditions**.

Recommended boundary:

- Chapter 005: what the Design Basis contains, how it is assembled, approved, versioned, reviewed, changed and used as the governing baseline.
- Chapter 006: how the service conditions and multidimensional design envelope are defined, combined and represented.

This requires targeted restructuring, not deletion of the underlying concepts.

### 3.4 Missing chapter-level functions

The following are missing or underdeveloped:

1. **Design Basis assembly model** — explicit inputs and outputs;
2. **Design Basis ownership / approval authority**;
3. **baseline and revision control** — draft / approved / superseded / reopened;
4. **Design Basis assumptions and controlled holds register**;
5. **distinction between input, requirement, assumption, design criterion and design decision**;
6. **standards / code edition control inside the Design Basis**;
7. **Design Basis completeness / readiness review before detailed design**;
8. **change-impact workflow** — not only “review through MOC,” but what gets reopened;
9. **traceability to requirements and downstream design outputs**;
10. **explicit handoff to Chapter 006** for detailed service-envelope construction.

**Gate B result: PASS — TARGETED AUGMENTATION AND BOUNDARY RESTRUCTURE REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The following should remain substantially intact:

- Design Basis as the technical foundation for the full system lifecycle;
- distinction between normal operating conditions and design conditions;
- rejection of arbitrary design margins;
- explicit assumptions;
- hierarchy of applicable requirements and standards;
- management-of-change principle;
- consequences of incomplete Design Basis information;
- the minimum-content concept.

### 4.2 Design Basis needs a canonical input model

The chapter should define the Design Basis as an integration product built from controlled inputs, including:

- system function and boundary from Chapter 001;
- engineering decision context from Chapter 002;
- process definition from Chapter 003;
- approved requirements from Chapter 004;
- service conditions / design envelope from Chapter 006;
- governing laws, codes, standards and specifications;
- assumptions and controlled holds;
- design philosophy and project constraints;
- life-cycle, inspection, maintenance and modification expectations.

This avoids the common error of treating the Design Basis as a long narrative rather than a controlled engineering baseline.

### 4.3 Design Basis content types should be distinguished

The current definition groups “conditions, assumptions, constraints, codes, and performance requirements,” which is directionally correct but can be strengthened.

The revised chapter should distinguish:

- **facts / verified inputs**;
- **approved requirements**;
- **assumptions**;
- **controlled holds**;
- **governing external requirements**;
- **design criteria / philosophy**;
- **selected design decisions** where they are part of the approved baseline.

These categories should not be silently merged because they have different change-control consequences.

### 4.4 Operating versus design conditions needs tighter scope

The existing example of 6 barg and 35°C versus higher assessment conditions is useful conceptually.

However, Chapter 005 should not become the place where the envelope itself is developed. The revised section should state the principle, then hand off to Chapter 006 for detailed construction of credible combinations, durations, transients and load cases.

### 4.5 Assumptions need lifecycle status

The chapter correctly says assumptions are not defects and hidden assumptions are.

The revised chapter should go further by requiring each material assumption to have:

- statement;
- basis;
- owner;
- significance;
- validation action;
- status;
- trigger if invalidated.

This should align with Chapter 002 evidence states and Chapter 004 change control.

### 4.6 Design Basis approval and configuration control are missing

A Design Basis only functions as a baseline if the organization can tell which version is active.

The chapter should establish a minimal lifecycle such as:

- working draft;
- review candidate;
- approved baseline;
- superseded;
- reopened / under revision.

It should also state that a later document revision does not automatically invalidate earlier design work unless impact assessment determines that affected decisions must be reopened.

### 4.7 Standards control must be explicit

Chapter 000 established edition control. Chapter 005 is the correct location to require the active Design Basis to identify, where material:

- governing standard / code;
- edition / year;
- amendments or adopted project edition;
- applicability / scope;
- controlled unresolved standards holds.

The chapter should not reproduce clauses.

It should control which normative basis the design is using.

### 4.8 Readiness gate is missing

The current minimum-content list is useful, but it does not define when the Design Basis is sufficiently mature for detailed engineering.

The revised chapter should add a readiness review such as:

- system boundary defined;
- process basis sufficiently mature;
- material requirements approved or controlled;
- applicable standards basis identified;
- service envelope defined to the level needed for the current stage;
- material assumptions visible;
- critical holds dispositioned;
- ownership and approvals defined.

If critical items remain unresolved, the correct state may be a conditional design release rather than pretending the basis is complete.

**Gate C result: PASS WITH BASELINE-CONTROL AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

Chapter 005 should remain standards-neutral in content but strong in standards governance.

Recommended rules:

- identify the governing source and edition in the approved Design Basis when material;
- distinguish design code, product standard, installation standard, test standard and manufacturer limitation by role;
- unresolved clause-level requirements remain controlled holds;
- standards changes trigger impact assessment rather than automatic redesign;
- draft standards should not silently replace published adopted editions;
- project deviations or waivers should be traceable to authority.

**Gate D result: AUGMENT.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- concise and readable;
- strong definition and central question;
- useful operating-vs-design distinction;
- strong assumptions and MOC messages;
- practical incomplete-basis examples;
- useful minimum-content list.

### Editorial / architecture gaps

1. No reader outcomes.
2. No canonical Design Basis assembly visual.
3. Chapter overlaps Chapter 006 on service-envelope detail.
4. No owner / approver / baseline lifecycle concept.
5. No minimum Design Basis record / configuration-control fields.
6. No explicit controlled-hold register.
7. No readiness gate.
8. No traceability model from requirements to Design Basis to downstream design.
9. No explicit standards-edition control rule.
10. No clean closing handoff to Chapter 006.

**Gate E result: PASS — TARGETED AUGMENTATION / BOUNDARY RESTRUCTURE.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-005-01 | High | No canonical Design Basis assembly model | Add inputs → baseline → downstream design model |
| GAP-005-02 | High | Overlap with Chapter 006 on design-envelope detail | Restrict 005 to integration/control and hand detailed envelope construction to 006 |
| GAP-005-03 | High | No Design Basis owner / approval authority | Add ownership and approval fields |
| GAP-005-04 | High | No baseline / revision lifecycle | Add draft / review / approved / superseded / reopened states |
| GAP-005-05 | High | Assumptions lack status, owner and validation action | Add assumption-control model |
| GAP-005-06 | High | No controlled-hold register concept | Add unresolved-item / hold treatment |
| GAP-005-07 | Medium | Facts, requirements, assumptions, criteria and decisions are blended | Distinguish Design Basis content types |
| GAP-005-08 | High | No readiness gate before detailed engineering | Add Design Basis readiness review |
| GAP-005-09 | Medium | Standards edition / adopted basis not explicit | Add standards-source and edition control |
| GAP-005-10 | Medium | Requirement traceability into Design Basis not explicit | Add requirement → Design Basis → design-output traceability |
| GAP-005-11 | High | MOC language lacks explicit impact/reopen workflow | Add change-impact review and affected-decision reopen rule |
| GAP-005-12 | Medium | No canonical Design Basis asset | Add `FIG-005-001` assembly/configuration-control placeholder |
| GAP-005-13 | Medium | Minimum content list lacks status/owner/source fields | Expand to minimum controlled Design Basis record |
| GAP-005-14 | Low | No reader outcomes | Add concise outcomes |
| GAP-005-15 | Medium | Operating/design-condition section risks duplicating Chapter 006 | Keep principle only and link forward |
| GAP-005-16 | Low | Closing handoff to Chapter 006 missing | Add explicit transition |

---

## 8. Disposition

# AUGMENT / BOUNDARY RESTRUCTURE

The chapter should **not** be rewritten from scratch.

Its core definition, assumptions, applicable-requirements logic, living-document concept and incomplete-basis examples are strong.

The revision should make Chapter 005 the canonical chapter for **Design Basis integration, approval, configuration control, readiness, traceability and change management**, while moving detailed treatment of service-condition combinations and envelope representation to Chapter 006.

---

## 9. Proposed Chapter 005 Rev 1.0 scope

Recommended revision package:

1. Retain the existing definition and most current prose.
2. Add concise reader outcomes.
3. Add **Design Basis Assembly** with explicit inputs:
   - system function/boundary;
   - process definition;
   - approved requirements;
   - governing codes/standards/specifications;
   - service conditions/design envelope;
   - assumptions and controlled holds;
   - project constraints and design philosophy;
   - life-cycle / inspection / maintenance expectations.
4. Add `FIG-005-001 — Design Basis Assembly and Configuration Control` conceptual placeholder.
5. Distinguish Design Basis content types: verified input / approved requirement / assumption / controlled hold / governing source / design criterion / approved design decision.
6. Add **Design Basis Minimum Controlled Record** including revision, owner, approver, status, governing standards edition, source references, assumptions, holds and affected system boundary.
7. Add Design Basis lifecycle: working draft / review candidate / approved baseline / superseded / reopened-under-revision.
8. Add controlled assumptions model with basis, owner, validation action, status and invalidation trigger.
9. Add controlled-hold register logic.
10. Keep operating-vs-design-condition principle but defer detailed service-envelope construction to Chapter 006.
11. Add standards edition/adopted-basis control consistent with Chapter 000.
12. Add requirement traceability: approved requirement → Design Basis item → downstream design response / verification.
13. Add **Design Basis Readiness Review** before detailed engineering or major release.
14. Add change-impact workflow: process/requirement/standard/design-basis change → identify affected items → reopen impacted decisions → reverify as required.
15. Expand minimum-content list into a controlled baseline checklist rather than only topic headings.
16. Add explicit handoff to Chapter 006 as the chapter that develops the service conditions and multidimensional design envelope in detail.
17. Keep the chapter methodological; do not turn it into a project Design Basis template or repeat Chapter 006 calculations/representations.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this review.

If the revision scope above is approved, prepare **Chapter 005 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 006.
