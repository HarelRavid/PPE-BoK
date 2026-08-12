# PPE-BoK — Cross-Chapter Architecture Audit

**Scope:** Chapters 000–013  
**Branch:** `chapter-013-redevelopment`  
**Integration phase:** Phase II — Cross-Chapter Architecture  
**Status:** AUDIT COMPLETE — CONTROLLED EDIT PROPOSALS PENDING

## 1. Purpose

This audit verifies that the reviewed Chapters 000–012 and the separately redeveloped Chapter 013 operate as one engineering sequence rather than as parallel or competing methods.

This document does **not** silently reopen approved technical content. It identifies canonical ownership, cross-reference rules, terminology baselines, controlled overlap, and any integration change that should be proposed through normal change control.

---

## 2. Canonical engineering sequence

The current book-wide engineering backbone is:

`How to use the evidence`
→ `System definition`
→ `Engineering decision process`
→ `Process definition`
→ `Engineering requirements`
→ `Design Basis`
→ `Service/design-envelope cases`
→ `Risk and uncertainty`
→ `Fluid characterization`
→ `Polymer/material behaviour`
→ `Material-system selection`
→ `Material-family characteristics`
→ `Long-term pressure verification`
→ `Material-family deep dive / PE application`

This sequence preserves the distinction between generic engineering method and material-specific application.

---

## 3. Canonical ownership and handoff register

| Chapter | Canonical ownership | Primary handoff / use |
|---:|---|---|
| 000 | How to use requirements, evidence, equations, standards and examples | Governs reading and evidence discipline across the book |
| 001 | System definition, boundaries, interfaces, complete piping-system concept | Feeds process definition and later design decisions |
| 002 | Engineering decision workflow; evidence status; GO / CONDITIONAL GO / NO-GO | Cross-cutting decision-control method for all later chapters |
| 003 | Process-definition inputs and operating context | Feeds Chapter 004 requirements |
| 004 | Controlled engineering requirements | Feeds Chapter 005 Design Basis |
| 005 | Design Basis assembly, ownership, baseline and configuration control | Controls the approved technical basis used by Chapters 006 onward |
| 006 | Construction of discrete service/design-envelope cases | Feeds Chapter 007 uncertainty review and Chapter 008 characterization |
| 007 | Uncertainty, sensitivity, residual uncertainty, controls and reopen logic | Cross-cutting uncertainty discipline for later technical decisions |
| 008 | Controlled process-fluid characterization package | Provides fluid-side inputs to material and design chapters |
| 009 | Polymer fundamentals and material-data interpretation | Feeds Chapter 010 selection and Chapter 012 pressure-design interpretation |
| 010 | Controlled material-system selection methodology | Uses family information and pressure verification without duplicating them |
| 011 | Family-level characteristics and candidate-orientation reference | Supports Chapter 010 candidate generation/screening; points to Chapter 012 for pressure verification |
| 012 | Long-term strength → MRS → design stress → SDR → product pressure classification → project pressure verification | Supplies the generic pressure-design chain to material-specific chapters |
| 013 | PE-specific engineering application and standards navigation | Applies Chapters 009–012 to polyethylene rather than replacing their generic methods |

---

## 4. Cross-reference policy

Until final numbering and Parts are frozen:

1. Prefer references by **chapter title/topic** and working chapter number together where useful.
2. Avoid hard-coded section-number cross-references unless the referenced section is stable enough to justify it.
3. When another chapter owns the canonical method, summarize only the minimum local context and point to the canonical home.
4. Purposeful reinforcement is allowed, but independent alternative definitions or workflows are not.
5. Circular references are acceptable only where chapter roles differ explicitly, for example:
   - Chapter 010 owns the **selection method**;
   - Chapter 011 supplies **family characteristics** used by that method.
6. A material-family deep dive may repeat a generic concept only to apply it to that material; the generic definition remains owned by the earlier canonical chapter.

---

## 5. Canonical wording baselines

The following phrases should be treated as book-wide wording baselines unless a governing standard requires different terminology.

### 5.1 Material / product / system hierarchy

> **material qualification ≠ product conformity ≠ system suitability**

### 5.2 Family-information hierarchy

> **family tendency → compound/grade evidence → qualified product/system evidence → project suitability**

### 5.3 Pressure hierarchy

> **material classification ≠ pipe/product pressure classification ≠ component rating ≠ project system allowable pressure**

### 5.4 Decision disposition

Use:

- **GO**
- **CONDITIONAL GO**
- **NO-GO**

### 5.5 Uncertainty and change control

Use consistently:

- **assumption** for a provisional input accepted to proceed;
- **controlled hold** for an unresolved issue that materially prevents closure;
- **residual uncertainty** for uncertainty remaining after controls;
- **reopen trigger** and **impact review** when the decision basis changes.

### 5.6 Design Basis

Use **Design Basis** consistently as the controlled technical baseline, not as a casual synonym for a datasheet, design condition, or process description.

---

## 6. Chapter 013 boundary-only integration review

### 6.1 Overall result

**PASS WITH CONTROLLED OVERLAP REFINEMENT.**

No direct engineering contradiction was identified between the current Chapter 013 and the approved roles of Chapters 009–012 in the portions reviewed for this integration pass.

The principal issue is **duplication risk**, not technical conflict.

### 6.2 Chapter 009 ↔ Chapter 013

Chapter 009 owns generic polymer-science interpretation:

- semicrystalline structure;
- viscoelasticity;
- creep;
- stress relaxation;
- time/temperature dependence;
- distinction between response and degradation/failure mechanisms.

Chapter 013 may retain PE-specific molecular/morphological discussion where it explains polyethylene behaviour, but should not become a second generic polymer-fundamentals chapter.

**Integration rule:**

> Chapter 009 defines the generic material-science concept; Chapter 013 explains what that concept means specifically for PE piping.

### 6.3 Chapter 010 ↔ Chapter 013

Chapter 010 owns the controlled material-system selection process:

`readiness → candidate systems → hard gates → evidence / uncertainty → comparison → verification → approval`.

Chapter 013 Investigation 9 is appropriately described in its gap-closure review as an integration/decision workflow, but it must remain a **PE-specific project-verification workflow**, not an alternative general material-selection methodology.

**Integration rule:**

> Chapter 010 decides how candidate systems are selected; Chapter 013 verifies a PE candidate against the defined project basis.

### 6.4 Chapter 011 ↔ Chapter 013

Chapter 011 owns family-level orientation and comparison.

Chapter 013 is allowed to go much deeper on PE because it is a dedicated material-family chapter.

The overlap is acceptable provided Chapter 013 does not present PE-specific advantages as universal rankings against other polymer families.

**Integration rule:**

> Chapter 011 helps the engineer decide whether PE belongs in the candidate set; Chapter 013 helps the engineer engineer the PE option once it is under serious consideration.

### 6.5 Chapter 012 ↔ Chapter 013

Chapter 012 owns the generic pressure-design chain and pressure terminology:

`long-term evidence → statistical strength basis → material classification → application design stress → SDR/geometry → product pressure classification → project verification`.

Chapter 013 Investigations 5–8 may retain PE-specific examples, standards navigation, markings and calculation application.

The generic definitions of MRS, design stress, design coefficient, SDR, PN/MOP/design/operating/test pressure remain canonically owned by Chapter 012.

**Integration rule:**

> Chapter 012 defines the generic pressure framework; Chapter 013 applies it to PE and its product/application standards.

### 6.6 Design Basis inputs in Chapter 013

Chapter 013 currently contains a useful PE-focused list of required Design Basis inputs.

For book-wide consistency, that list should be treated as a **PE application checklist consuming Chapters 005, 006 and 008**, not as a second canonical definition of the Design Basis or service envelope.

### 6.7 Chapter 013 standards-validation status

The current Chapter 013 metadata and gap-closure package correctly preserve standards-validation and verification holds. The chapter should not be downgraded to draft, nor promoted to publication lock, during this architecture pass.

---

## 7. Metadata and architecture findings

### ARCH-001 — Chapter 009 Part metadata is stale

The Chapter 009 frontmatter still states:

`part: II - Process Definition and Requirements`

This no longer matches the reviewed content architecture and was inherited from the legacy repository location.

**Disposition:** structural metadata cleanup required. Because final Parts are not locked, do not assign a new permanent Part yet.

### ARCH-002 — Chapter 012 status metadata is stale

The Chapter 012 frontmatter still states:

`status: research-based-draft`

although the Rev 1.0 content review is approved and integrated.

**Disposition:** update status metadata to the current reviewed baseline; this is a non-technical status correction.

### ARCH-003 — Chapter 013 is intentionally more integrated than a normal family overview

Chapter 013 spans PE material behaviour, standards navigation, pressure interpretation, project verification and failure framing.

This breadth is acceptable because the chapter is a material-family engineering deep dive, but its generic methods must remain subordinate to Chapters 009–012.

**Disposition:** no chapter split required by this integration pass.

### ARCH-004 — Cross-reference validation must be repeated after final numbering

Working chapter numbers are currently useful and coherent, but final Parts and numbering remain provisional.

**Disposition:** retain a final-numbering cross-reference gate before publication lock.

---

## 8. Controlled edit proposals generated by this audit

The following changes may be executed without reopening engineering content because they are status/metadata/documentation corrections:

1. correct Chapter 012 status metadata;
2. remove or neutralize stale Chapter 009 legacy Part metadata without assigning a final Part;
3. add this audit to the integration workstream.

The following changes are **proposed technical/structural manuscript refinements** and should follow normal approval before editing approved prose:

1. add a concise boundary note in Chapter 013 stating that Chapters 009–012 own the generic methods and Chapter 013 applies them to PE;
2. where Chapter 013 repeats generic MRS/SDR/selection/polymer definitions at length, replace only unnecessary duplication with concise PE-specific application wording and cross-references;
3. ensure Investigation 9 is explicitly named/framed as PE project verification rather than a competing general selection method;
4. add a forward handoff from Chapter 012 to Chapter 013 once the exact final wording is approved.

---

## 9. Phase II disposition

**Canonical ownership audit:** COMPLETE  
**Canonical terminology baseline:** COMPLETE  
**Cross-reference policy:** COMPLETE  
**Chapter 013 boundary-only check:** COMPLETE  
**Direct technical conflicts found:** NONE requiring immediate reopen  
**Controlled overlap refinements:** PROPOSED  
**Final numbering cross-reference check:** DEFERRED

The next integration phase may proceed to assets/evidence control while the controlled Chapter 013 overlap refinements are queued for explicit approval.