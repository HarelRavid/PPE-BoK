# Chapter 006 — Review Package

**Chapter:** 006 — Service Conditions and the Design Envelope  
**Review framework:** `docs/BOOK-WIDE-REVIEW-PLAN.md`  
**Branch:** `chapter-013-redevelopment`  
**Status:** REVIEW COMPLETE — REVISION APPROVAL PENDING  
**Disposition:** AUGMENT / STRUCTURE REFINEMENT

## 1. Review basis

Reviewed sources:

- `chapters/chapter-006-service-conditions-and-design-envelope/chapter.md`;
- approved Chapter 005 Rev 1.0 for upstream Design Basis integration/control boundary;
- `chapters/chapter-007-engineering-risk-and-uncertainty/chapter.md` for downstream risk/uncertainty boundary;
- `docs/BOOK-WIDE-REVIEW-PLAN.md` for review criteria.

No external source was used to introduce new technical or normative claims. The review evaluates service-condition completeness, envelope construction, combination logic, time dependence, traceability, relationship to the Design Basis, and handoff to risk/uncertainty.

---

## 2. Gate A — File and evidence inventory

### Present

- `chapter.md` — complete readable draft.

### Not present before this review

- `review.md`;
- `references.md`;
- `notes.md`;
- service-envelope matrix / case-definition asset.

### Evidence dependency

Chapter 006 is methodological and conceptual. It contains no equations, standards clauses, or numerical acceptance criteria. Its main technical burden is whether it teaches the reader to construct a credible multidimensional service/design envelope rather than merely list individual maxima and minima.

**Gate A result: PASS WITH ENVELOPE-CONSTRUCTION GAPS.**

---

## 3. Gate B — Architecture and scope review

### 3.1 What the chapter already does well

The chapter correctly establishes that:

- nominal operation is not the design envelope;
- service conditions are physical, chemical, mechanical, operational, temporal, and environmental;
- transients, cleaning, maintenance, testing, and abnormal events matter;
- mechanical loads should be considered in combination;
- chemistry depends on concentration, temperature, time, contaminants and mixtures;
- multiphase service should be treated explicitly;
- time is a design variable;
- foreseeable change matters;
- the envelope is multidimensional and can be represented in several ways.

This is the correct role for Chapter 006.

### 3.2 Boundary with Chapter 005

Chapter 005 now owns Design Basis integration, approval, readiness, configuration control and change management.

Chapter 006 should therefore own the technical construction of the service/design envelope itself:

`operating states + process conditions + chemistry + mechanical loads + environment + time + credible combinations → service/design envelope cases`

The chapter should not repeat Design Basis lifecycle/governance material except where needed for traceability back to the approved baseline.

### 3.3 Boundary with Chapter 007

Chapter 007 owns engineering risk and uncertainty.

Chapter 006 should identify uncertain or incomplete envelope inputs and preserve them as assumptions/holds, but should stop before broader risk treatment, consequence ranking, robustness philosophy or uncertainty-management strategy.

The handoff should become explicit:

- Chapter 006 asks: **What conditions and combinations can credibly act on the system?**
- Chapter 007 asks: **How should uncertainty in those conditions and the associated risk be evaluated and managed?**

### 3.4 Missing chapter-level functions

The following are missing or underdeveloped:

1. **canonical envelope-construction workflow** from operating states to discrete design/service cases;
2. **simultaneity / correlation logic** — maxima should not be combined automatically if they cannot credibly occur together;
3. **governing-case concept** — different mechanisms may be governed by different cases rather than one universal worst case;
4. **case identity and traceability** — each material envelope case should have source, state, duration/frequency and affected engineering checks;
5. **local versus system-average conditions** — local pressure, temperature, phase or load conditions can govern;
6. **construction, testing and commissioning cases** deserve explicit inclusion as life-cycle service states;
7. **temporary and maintenance configurations** should be treated as cases, not only fluid exposures;
8. **rate-of-change / sequence information** should be more explicit alongside duration and cycle count;
9. **envelope completeness check** before downstream design;
10. **explicit handoff to Chapter 007** for uncertainty/risk treatment of incomplete or variable conditions.

**Gate B result: PASS — TARGETED AUGMENTATION REQUIRED.**

---

## 4. Gate C — Technical / methodological review

### 4.1 Strong content to retain

The following should remain substantially intact:

- definition of service conditions;
- nominal operation is not the envelope;
- mechanical, chemical, multiphase and environmental conditions all matter;
- time-at-condition and cycle count matter;
- foreseeable changes should be considered where practical;
- multiple representation methods are useful;
- isolated maxima can be misleading.

### 4.2 The chapter needs an explicit case-building method

The current draft identifies the dimensions of the envelope but does not fully show how the engineer turns them into usable cases.

A revised chapter should teach a simple sequence such as:

1. identify operating/life-cycle states;
2. define condition ranges for each state;
3. identify credible simultaneous combinations;
4. add duration, frequency, sequence and rate-of-change where relevant;
5. identify local conditions and interfaces;
6. define discrete envelope cases;
7. map each case to affected downstream engineering checks;
8. identify uncertainty/holds for Chapter 007 treatment.

This is the largest technical augmentation required.

### 4.3 One “worst case” is not enough

The current text correctly warns against combining unrelated maxima, but should go further.

Different cases may govern different engineering questions. For example, one case may govern pressure capability, another chemical exposure, another support loading, another cyclic response, and another installation or test condition.

The chapter should therefore avoid implying that one single global maximum envelope case must govern every check.

### 4.4 Mechanical combinations need bounded treatment

The statement that loads must be considered in combination is sound, but the chapter should not imply that every listed load is simultaneous.

Recommended wording should distinguish:

- credible concurrent loads;
- mutually exclusive conditions;
- temporary construction/test loads;
- operational loads;
- abnormal/transient combinations.

Detailed code-specific load combinations belong in later mechanical-design chapters.

### 4.5 Chemical-service treatment should connect condition + time

The current chemical section is strong but can be sharpened by framing each material chemical exposure as a combination of:

- chemical / mixture;
- concentration;
- temperature;
- mechanical stress context where relevant;
- duration/frequency;
- operating state.

This keeps chemistry inside the same envelope logic as pressure and mechanical loading.

### 4.6 Multiphase service should include location and state

The current chapter correctly identifies multiphase consequences. The revised version should add that phase distribution may vary with operating state and location, so a line-level description may not be sufficient.

No detailed multiphase calculation belongs here.

### 4.7 Time requires sequence and rate as well as count

The chapter already includes duration and cycle count. It should explicitly add:

- sequence;
- rate of pressure/temperature change;
- dwell time;
- cumulative exposure by state.

This aligns Chapter 006 with the process-definition treatment established in Chapter 003 without duplicating the upstream data-governance discussion.

**Gate C result: PASS WITH ENVELOPE-CASE AUGMENTATION.**

---

## 5. Gate D — Standards / evidence review

Chapter 006 should remain standards-neutral.

Its evidence-control role is to ensure that envelope cases can be traced to approved process data, requirements, Design Basis inputs, equipment information, operating evidence or controlled assumptions.

Recommended rules:

- do not create design conditions by arbitrary addition of unrelated maxima;
- do not treat an unverified transient as established fact;
- identify the source/status of material service conditions;
- unresolved credible conditions remain controlled assumptions or holds;
- code-specific load combinations, pressure definitions or acceptance limits belong to the governing downstream design method rather than being invented in this chapter.

**Gate D result: PASS WITH TRACEABILITY AUGMENTATION.**

---

## 6. Gate E — Editorial and academic review

### Strengths

- concise and readable;
- strong multidimensional framing;
- good separation of mechanical, chemical, multiphase and time effects;
- useful examples of envelope representations;
- avoids premature equations.

### Editorial / structure gaps

1. No reader outcomes.
2. No canonical envelope-construction visual.
3. The chapter lists dimensions more strongly than it teaches case construction.
4. No compact service-case table model.
5. No explicit governing-case concept.
6. Construction/test/commissioning states are present only indirectly.
7. Handoff to Chapter 007 is missing.
8. Final visual/punctuation polish should remain deferred to the book-wide cleanup pass.

**Gate E result: PASS — TARGETED AUGMENTATION.**

---

## 7. Gate F — Gap Register

| Gap ID | Severity | Finding | Required disposition |
|---|---|---|---|
| GAP-006-01 | High | No canonical envelope-construction workflow | Add state → combinations → cases → downstream checks method |
| GAP-006-02 | High | Simultaneity/correlation logic underdeveloped | Add credible-combination rule; reject automatic stacking of unrelated maxima |
| GAP-006-03 | High | No explicit governing-case concept | Add mechanism/check-specific governing case principle |
| GAP-006-04 | High | No controlled service-case record | Add case ID, state, conditions, duration/frequency, source/status and affected checks |
| GAP-006-05 | Medium | Local conditions not explicit enough | Add local/interface condition awareness |
| GAP-006-06 | Medium | Construction/testing/commissioning not established as explicit cases | Add life-cycle temporary cases |
| GAP-006-07 | Medium | Temporary maintenance configurations underdeveloped | Add temporary configuration case concept |
| GAP-006-08 | Medium | Rate-of-change and sequence not explicit enough | Add rate/sequence/dwell/cumulative exposure fields |
| GAP-006-09 | Medium | Mechanical load-combination wording can imply universal simultaneity | Qualify concurrent vs mutually exclusive/temporary cases |
| GAP-006-10 | Medium | Chemical envelope not expressed as a complete condition tuple | Tie chemistry to concentration, temperature, time/state and relevant stress context |
| GAP-006-11 | Medium | Multiphase section lacks local/state distribution concept | Add state/location dependence |
| GAP-006-12 | Medium | No envelope completeness/readiness check | Add pre-design completeness review |
| GAP-006-13 | Low | No reader outcomes | Add concise outcomes |
| GAP-006-14 | Medium | No canonical visual | Add `FIG-006-001 — Service Envelope Construction` placeholder |
| GAP-006-15 | Medium | No compact envelope-case table | Add `TAB-006-001 — Service/Design Envelope Case Register` concept |
| GAP-006-16 | Low | Closing handoff to Chapter 007 missing | Add explicit uncertainty/risk transition |

---

## 8. Disposition

# AUGMENT / STRUCTURE REFINEMENT

The chapter is conceptually strong and should **not** be rewritten from scratch.

Its major improvement is to move from “these are the dimensions of the envelope” to “this is how an engineer constructs, records, checks and uses credible envelope cases.”

---

## 9. Proposed Chapter 006 Rev 1.0 scope

Recommended revision package:

1. Retain the current definition and most existing technical content.
2. Add concise reader outcomes.
3. Add a canonical **Envelope Construction Workflow**:
   - operating/life-cycle states;
   - condition ranges;
   - credible simultaneous combinations;
   - duration/frequency/sequence/rate;
   - local conditions;
   - discrete envelope cases;
   - downstream checks.
4. Add `FIG-006-001 — Service Envelope Construction` conceptual placeholder.
5. Add `TAB-006-001 — Service/Design Envelope Case Register` with fields such as case ID, state, pressure, temperature, fluid/phase, chemistry, mechanical/environmental loads, duration/frequency, source/status, and affected engineering checks.
6. Add explicit simultaneity/correlation rule: do not automatically combine independent maxima.
7. Add explicit principle that different engineering checks may have different governing cases.
8. Add local-condition awareness near equipment, restrictions, high/low points, heat sources and interfaces without adding detailed calculations.
9. Add construction, testing, commissioning and temporary maintenance configurations as explicit life-cycle cases where relevant.
10. Strengthen time treatment with sequence, rate-of-change, dwell and cumulative exposure.
11. Qualify mechanical combinations as credible concurrent cases rather than universal stacking of loads.
12. Express chemical exposure as a condition tuple including chemistry/concentration, temperature, duration/frequency and operating state.
13. Add multiphase location/state dependence.
14. Add an **Envelope Completeness Review** before downstream design.
15. Preserve uncertainties/holds and hand them to Chapter 007 rather than resolving them with unsupported conservatism.
16. Add explicit handoff to Chapter 007 for engineering risk and uncertainty.
17. Keep detailed code-specific load combinations, equations and acceptance criteria in later specialist design chapters.

---

## 10. Approval gate

No substantive change has been made to `chapter.md` in this review.

If the revision scope above is approved, prepare **Chapter 006 Rev 1.0** as a complete proposed replacement, present the integrated text for review, and only after explicit approval commit the revised manuscript before proceeding to Chapter 007.
