# Chapter 13 — Technical Review

**Chapter:** 013 — Polyethylene (PE)  
**Reviewed branch:** `chapter-013-redevelopment`  
**Reviewed chapter baseline:** commit `2117ee113a4dc5f3ec865774d933ce58c766c0a7`  
**PDS baseline:** 1.0 (frozen)  
**Review basis:** CDB-013, EDR-013, RDP-013, integrated Chapter 13 Rev 1.0 candidate, Pre-Technical Verification 013  
**Standards Validation:** deliberately excluded from this review except where a claim must remain behind a hold point

## 1. Review decision

**CONDITIONAL PASS — TARGETED TECHNICAL CORRECTIONS REQUIRED**

The integrated chapter has a coherent engineering architecture and no fundamental redesign is required. The central engineering chain is internally consistent:

`Design Basis → long-term evidence → lower statistical basis → MRS → C → design stress → SDR → reference pressure basis → service verification → engineering disposition`

The review found no arithmetic error in Worked Example A, no dimensional inconsistency in the principal calculation chain, and no substantive conflict between the chapter's material-classification, pressure-design, project-integration and failure-lens sections.

The remaining Technical Review findings are bounded and correctable without reopening the approved redevelopment architecture.

---

## 2. Scope of Technical Review

This review checks:

- physics / engineering logic;
- dimensional and algebraic consistency;
- equation completeness at handbook level;
- internal terminology consistency;
- investigation boundaries and duplication;
- Design Basis logic and decision flow;
- worked-example logic;
- failure-lens reasoning;
- CDB-required engineering assets at technical-outline level.

This review does **not** validate current standard editions, clause numbers, coefficient values, PE100↔MRS values, PE100-RC status, temperature derating rules, product marking requirements or normative wording. Those remain the separate mandatory Standards Validation gate.

---

## 3. Technical strengths confirmed

### 3.1 Architecture and investigation boundaries — PASS

The sequence is progressive and technically coherent:

`Why PE → material behaviour → classification → long-term behaviour → evidence generation → regression interpretation → MRS/design stress → SDR/pressure/marking → Design Basis integration → failure feedback`

Investigation 4 now explains mechanisms without duplicating the evidence-generation role of Investigation 5 or the diagnostic role of Investigation 10. Investigation 9 functions as an integration/decision workflow rather than a catch-all technical chapter.

### 3.2 Material / product / system separation — PASS

The chapter consistently distinguishes:

- material classification;
- product conformity;
- joining quality;
- installed-system condition;
- project allowable operating decision.

This directly prevents the common error of treating a resin/material designation as a complete piping-system qualification.

### 3.3 Long-term evidence chain — PASS, standards terminology pending

Investigations 5–7 correctly preserve the conceptual separation between:

`test evidence → regression → conservative lower statistical result → standardized MRS classification → design coefficient → design stress`

The chapter does not incorrectly use the mean regression line as a design value and does not represent the statistical lower bound as a universal survival probability.

### 3.4 Pressure-design algebra and units — PASS

The chapter uses:

`σ_s = MRS / C`

and

`p = 2σ_s / (SDR - 1)`

with consistent units when pressure and stress share the same unit system. The conversion `1 MPa = 10 bar` is correctly applied in the illustrative calculation.

Independent recalculation confirms Worked Example A:

- `MRS = 10 MPa`
- `C = 1.25`
- `σ_s = 8.0 MPa`
- `SDR = 11`
- `p_reference = 1.6 MPa = 16 bar`

The SDR 9 sensitivity result is also internally correct at `2.0 MPa = 20 bar` under the same illustrative inputs.

### 3.5 Reference-pressure versus project-allowable distinction — STRONG PASS

The chapter repeatedly and correctly prevents the calculated material/geometry pressure result from being treated automatically as the project allowable operating pressure. Temperature/time, fluid/environment, components/joints, transients, installation and application scope remain separate project checks.

### 3.6 Design Basis workflow — PASS

Investigation 9 starts from project inputs, identifies the governing standards path before applying coefficients, separates material and product qualification, reopens temperature/service conditions, addresses chemistry/transients/installation/joining interfaces and ends in an explicit `GO / CONDITIONAL GO / NO-GO` disposition.

### 3.7 Failure Lens — PASS

Investigation 10 correctly separates observation from mechanism and distinguishes initiation, propagation and final rupture. It avoids the unsupported inference that failure location proves root cause and provides an evidence-driven feedback loop into the Design Basis.

---

## 4. Technical Review findings requiring correction

### TR-013-01 — HIGH — EQ-013-003 metadata is incomplete

**Finding:** `EQ-013-003 — Standard Dimension Ratio` defines the symbols and establishes that SDR is dimensionless, but it does not yet provide the full equation metadata required by CDB-013: source basis, assumptions, validity/applicability and common misuse.

**Required correction:** add explicit metadata without inventing normative requirements. At minimum:

- **Source basis:** standardized nominal geometry concept; exact current definition and dimensional terminology subject to Standards Validation.
- **Assumptions:** nominal outside diameter and nominal wall thickness are taken from the same product/dimensional framework.
- **Engineering use:** geometry descriptor used in the subsequent pressure relationship.
- **Applicability limit:** SDR alone does not establish pressure capability, product conformity, temperature capability or installed minimum wall.
- **Common misuse:** comparing SDR across materials/services as if it were a pressure rating by itself.

**Disposition:** OPEN — correction is editorial/technical and does not require external standards values.

### TR-013-02 — HIGH — EQ-013-004 requires explicit assumptions / validity metadata and terminology discipline

**Finding:** `EQ-013-004` has units, source-basis caution and a misuse warning, but its assumptions and validity boundary should be stated explicitly. In addition, the preceding supporting-literature form is labelled `MOP`, while the chapter intentionally treats the arithmetic result as a **reference pressure basis** pending service verification. Without an explicit terminology note, readers may interpret the displayed `MOP` label more strongly than the chapter intends.

**Required correction:** add:

- **Assumptions:** nominal SDR geometry, design-stress basis already established, compatible unit system, and use within the governing product/application framework.
- **Validity limit:** does not incorporate project temperature/time treatment, chemical compatibility, transient/cyclic effects, local defects, components/joints or other project loads.
- **Terminology note:** supporting literature may label the expression `MOP`; within this chapter the computed value is treated as `p_reference` until the governing current standards path and service conditions are validated.
- **Common misuse:** treating the arithmetic pressure value or a PN marking as unconditional allowable operating pressure.

**Disposition:** OPEN — correction is technical clarification; normative wording remains behind Standards Validation.

### TR-013-03 — MEDIUM — Worked Example A should state its standards path more explicitly

**Finding:** the example correctly states what the arithmetic does not prove and carries Standards Validation hold points, but CDB-013 asks the example to state the applicable standards path explicitly.

**Required correction:** add a concise non-normative path such as:

`material classification framework → governing product/application standard → applicable C → geometry/pressure calculation → service verification`

and state that the exact governing standards and coefficient remain project- and scope-dependent until Standards Validation.

**Disposition:** OPEN.

### TR-013-04 — MEDIUM — CDB-required visual placeholders are not yet complete

**Finding:** the normalized register contains five figures, including an additional Failure Lens. CDB-013 specifically asks placeholders for both:

- `test-data → regression → classification → product marking chain`; and
- `PE pipe marking anatomy`.

Those two visual concepts are not explicitly represented by dedicated placeholder IDs. `FIG-013-004` covers the broader pressure-design decision chain but is not a direct substitute for both requested visuals.

**Required correction:** reserve two additional original-figure placeholders, for example:

- `FIG-013-006 — Test evidence → regression → classification → product marking chain`;
- `FIG-013-007 — PE pipe marking anatomy`.

No image production is required during authoring.

**Disposition:** OPEN — production-asset completeness finding.

### TR-013-05 — MEDIUM — CDB failure-investigation reader outcome is not explicit in the chapter outcomes

**Finding:** the chapter body contains a strong Failure Lens, but the opening reader outcomes do not explicitly state the CDB outcome that the reader should be able to frame an initial failure-investigation path without assuming visible fracture location is root cause.

**Required correction:** add one reader outcome reflecting this capability.

**Disposition:** OPEN — no technical content change required.

### TR-013-06 — LOW — Controlled cross-references remain generic

**Finding:** the chapter correctly limits scope for transient hydraulics, detailed stress/flexibility, joining procedure design, inspection and specialist failure analysis, but references to the dedicated treatments remain generic rather than linked to specific chapter IDs.

**Required correction:** resolve actual chapter references once the corresponding PPE-BoK chapter destinations are stable. Until then, keep as an explicit publication/editorial hold point rather than inventing chapter numbers.

**Disposition:** DEFERRED TO EDITORIAL / BOOK-INTEGRATION PASS.

### TR-013-07 — GOVERNANCE / MEDIUM — Example B verification method requires explicit equivalence disposition

**Finding:** Worked Example B is intentionally qualitative. The independent decision-path re-performance is technically appropriate and avoids introducing an unsupported temperature factor. However, CDB-013 success criteria use the phrase “two planned worked examples are independently recalculated.”

**Technical assessment:** inventing arithmetic would be worse engineering than preserving a qualitative example. The current verification method is technically sound.

**Required governance disposition:** record one of the following before final PDS completion:

1. accept independent decision-path re-performance as the approved equivalent verification for a deliberately non-numerical worked example; or
2. after Standards Validation, add a standards-supported numerical temperature/service example and independently recalculate it.

**Disposition:** TECHNICALLY ACCEPTABLE / GOVERNANCE DISPOSITION PENDING.

---

## 5. Standards Validation hold points confirmed, not resolved here

The Technical Review deliberately preserves these as open:

- current ISO 9080 terminology, methodology limits and edition;
- current ISO 12162 terminology, classification series, reference condition and design-stress requirements;
- PE100 ↔ MRS example relationship;
- source, scope and permissible/minimum value of design coefficient `C`;
- normative SDR / pressure relationship terminology and rounding;
- temperature/time treatment by application;
- PE100-RC standards status and qualification route;
- SCG test-method applicability / equivalence;
- product and pipe marking requirements;
- joining/product/application normative requirements;
- all final `shall`, `required`, minimum/maximum and similar normative language.

These are not Technical Review failures because the PDS explicitly requires a separate post-authoring Standards Validation gate.

---

## 6. Technical Review scorecard

| Review dimension | Decision | Comment |
|---|---|---|
| Physics / material behaviour | PASS | Time dependence, creep, rupture and SCG distinctions are coherent |
| Engineering architecture | PASS | Progressive investigations and clean interfaces |
| Equation algebra / dimensions | PASS | No arithmetic or unit defect found in the core calculation chain |
| Equation metadata | CONDITIONAL | EQ-013-003 and EQ-013-004 require explicit completion |
| Material / product / system separation | PASS | Consistent and strong |
| Design Basis integration | PASS | Ends in auditable disposition |
| Worked Example A | PASS | Independently recalculated |
| Worked Example B | PASS technically / governance hold | Decision logic independently verified; literal PDS wording requires disposition |
| Failure Lens | PASS | Evidence-driven and correctly bounded |
| Required engineering assets | CONDITIONAL | Two CDB visual placeholders still need reservation |
| Standards traceability | HOLD | Separate Standards Validation gate |
| Cross-chapter integration | HOLD / minor | Destination chapter IDs not yet resolved |

---

## 7. Required correction set before Technical Review closure

The Technical Review can be closed after the following bounded edits are completed and checked:

1. complete `EQ-013-003` metadata;
2. complete `EQ-013-004` assumptions/validity metadata and clarify `MOP` versus chapter `reference pressure basis` terminology;
3. add explicit standards-path wording to Worked Example A;
4. reserve `FIG-013-006` and `FIG-013-007` placeholders;
5. add the explicit failure-investigation reader outcome;
6. record the Example B verification-equivalence governance disposition (or defer a numerical version until after Standards Validation).

`TR-013-06` may remain deferred to final editorial/book integration because destination chapter IDs are not established in the reviewed source.

---

## 8. Final Technical Review disposition

**CONDITIONAL PASS.**

No fundamental engineering defect was identified. The remaining open findings are targeted completeness/clarity items plus one governance interpretation. Once TR-013-01 through TR-013-05 are corrected and TR-013-07 is formally dispositioned, Chapter 13 may be marked **Technical Review PASS** and proceed to the independent **Standards Validation** gate.
