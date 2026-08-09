# Chapter 13 — Pre-Technical Verification

**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**Status:** Pre-Technical Review evidence  
**PDS baseline:** 1.0 (frozen)

## 1. Purpose

Close the remaining pre-Technical-Review items identified by the Chapter 13 Gap Closure Review:

1. provide the missing consolidated MRS → C → design stress → SDR → pressure reference asset;
2. independently re-perform Worked Example A;
3. define and execute an appropriate independent verification method for qualitative Worked Example B.

This artifact does **not** close the final Standards Validation hold points. Numerical standards-derived values, coefficient applicability, pressure-design conventions, temperature/time treatment, PE100-RC treatment and marking requirements remain subject to authoritative Standards Validation.

---

## TAB-013-005 — MRS / Design Coefficient / Design Stress / SDR / Pressure Reference Chain

| Step | Quantity / input | Relationship or engineering action | Units | What it establishes | What it does **not** establish |
|---|---|---|---|---|---|
| 1 | Long-term evidence | Evaluate qualified long-term hydrostatic test evidence through the applicable regression/classification pathway | — | Evidence basis for material classification | Project suitability or allowable operating pressure |
| 2 | MRS | Use the standardized material-classification value established by the governing classification framework | MPa | Material-classification strength input | Design stress or system pressure by itself |
| 3 | Design coefficient, `C` | Identify the coefficient applicable to the governing product/application/design framework | dimensionless | Required reduction from classification strength to design-stress basis | Universal coefficient for every PE application |
| 4 | Design stress, `σ_s` | `σ_s = MRS / C` (`EQ-013-002`) | MPa when MRS is MPa | Stress basis for subsequent geometry/pressure relationship | Temperature-adjusted or project-final allowable pressure |
| 5 | SDR | `SDR = d_n / e_n` (`EQ-013-003`) | dimensionless | Nominal pipe geometry relationship | Material quality, product conformity or service suitability |
| 6 | Reference pressure basis | `p = 2σ_s / (SDR - 1)` (`EQ-013-004`) when pressure and stress use consistent units | same pressure/stress units; convert explicitly where required | Reference pressure basis for the selected material/design-stress/geometry chain | Automatic project allowable operating pressure |
| 7 | Service verification | Apply the governing temperature/time, fluid/environment, component/joint, transient, installation and application requirements | project-specific | Basis for project engineering disposition | Immunity from future Design Basis changes or failure |
| 8 | Final disposition | Record `GO / CONDITIONAL GO / NO-GO` with assumptions and open items | — | Auditable engineering decision | Replacement for specialist analyses required by the Design Basis |

**Use rule:** the table is a navigation/reference asset. Exact normative definitions, coefficient values, reference conditions, rounding rules and pressure-design conventions remain subject to final Standards Validation.

---

## 2. Independent Recalculation — Worked Example A

### Given in the integrated chapter

For illustration only:

- `MRS = 10 MPa`
- `C = 1.25`
- `SDR = 11`

### Independent calculation path A — design stress first

`σ_s = MRS / C`

`σ_s = 10 / 1.25 = 8.0 MPa`

Then:

`p = 2σ_s / (SDR - 1)`

`p = 2 × 8.0 / (11 - 1)`

`p = 16 / 10 = 1.6 MPa`

Using `1 MPa = 10 bar`:

`p = 16 bar`

### Independent calculation path B — direct substitution

Starting from the algebraically equivalent form used in the redevelopment basis:

`p_bar = 20 × MRS / [C × (SDR - 1)]`

`p_bar = 20 × 10 / [1.25 × 10]`

`p_bar = 200 / 12.5 = 16 bar`

### Cross-check

Both independent calculation paths return:

- `σ_s = 8.0 MPa`
- `p_reference = 1.6 MPa = 16 bar`

### Geometry sensitivity cross-check

Keeping `MRS = 10 MPa` and `C = 1.25`, for `SDR = 9`:

`p = 2 × 8.0 / (9 - 1) = 16 / 8 = 2.0 MPa = 20 bar`

This independently reproduces the chapter sensitivity result.

### Verification disposition

**Worked Example A: calculation verified.**

The verification confirms arithmetic, algebraic equivalence and unit conversion only. It does **not** validate that `C = 1.25`, the PE100↔MRS example value, the pressure relationship or any associated rounding convention is normatively applicable to a particular project. Those remain Standards Validation items.

---

## 3. Independent Verification — Worked Example B

### Nature of the example

Worked Example B is intentionally qualitative. It demonstrates that a material/product/geometry selection must be reopened when a material Design Basis input changes, even if the pipe marking and nominal geometry remain unchanged.

Adding a fabricated numerical temperature factor solely to make the example 'recalculable' would introduce an unsupported standards-derived value and would conflict with the chapter's Standards Validation discipline.

Therefore the independent verification method is **decision-path re-performance**, not invented arithmetic.

### Initial state

The example assumes:

- qualified PE100 product;
- selected SDR;
- acceptable reference pressure calculation;
- initial service condition within the previously evaluated basis.

### Changed input

Operating temperature increases materially.

### Independent re-performance

The changed temperature is propagated through the decision chain without relying on the original example wording:

1. **Design Basis:** temperature input has changed → previous Design Basis is no longer identical.
2. **Reference pressure calculation:** material designation and SDR may be unchanged → the original reference calculation does not disappear, but it is no longer sufficient for final disposition.
3. **Governing standards path:** reopen the applicable temperature/time treatment because its applicability depends on service condition.
4. **Service-life/pressure basis:** re-evaluate the allowable service basis under the new temperature/time combination.
5. **Chemical/environmental compatibility:** recheck transferability because temperature is part of the exposure condition.
6. **Components and joints:** reconfirm that fitting/joint/component limitations remain acceptable at the changed condition.
7. **Transient/installation interfaces:** determine whether the changed thermal/service condition modifies any associated mechanical assumptions.
8. **Disposition:** issue a new `GO / CONDITIONAL GO / NO-GO`; the previous disposition cannot simply be carried forward unchanged.

### Independence check

The re-performed path reaches the same engineering conclusion as the chapter example:

> A material Design Basis change requires the engineering decision to be reopened even when the pipe marking, material designation, SDR and nominal geometry remain unchanged.

### Verification disposition

**Worked Example B: decision logic independently verified.**

No numerical derating factor is introduced at this stage. If a numerical temperature example is added during or after Standards Validation, that numerical example shall receive a separate independent recalculation before Design Freeze.

---

## 4. Pre-Technical-Review Disposition

The three identified pre-Technical-Review items are now dispositioned as follows:

| Item | Disposition |
|---|---|
| Consolidated MRS → C → design stress → SDR → pressure reference asset | Complete as `TAB-013-005`; integration into the final chapter body/asset register required |
| Worked Example A independent recalculation | Complete — arithmetic, algebra and units verified |
| Worked Example B verification method | Complete — independent decision-path re-performance; numerical calculation intentionally not fabricated |

### Remaining gates

The chapter is now ready to proceed to **Technical Review**, subject to the following explicit remaining gates:

- integrate `TAB-013-005` into the chapter body and normalized asset register;
- Technical Review;
- authoritative Standards Validation;
- resolve PE100-RC hold point;
- apply any corrections resulting from Standards Validation;
- final review / Design Freeze.
