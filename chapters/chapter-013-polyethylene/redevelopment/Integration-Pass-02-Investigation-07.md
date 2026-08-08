# Integration Pass 02 — Investigation 7

**Chapter:** 013 — Polyethylene (PE)  
**Integration target:** Chapter 13 Rev 1.0  
**Source artifact:** `Batch-013-D-investigation-07.md`  
**Status:** Review candidate — awaiting owner approval  
**PDS baseline:** 1.0 (frozen)

> Integration rule: preserve the approved engineering substance of Batch 013-D; edit only for chapter continuity, terminology discipline, duplication control, equation metadata and handoff to Investigation 8. Current normative details remain subject to the final independent Standards Validation pass.

---

# Investigation 7 — How Does Long-Term Evidence Become MRS and Design Stress?

Investigations 5 and 6 established how long-term hydrostatic test evidence is converted into a conservative statistical strength basis. That result is not yet the stress used for pipe pressure design.

The next engineering step is classification.

For pressure-piping materials, classification converts a continuous long-term strength result into a standardized material-classification input that can be used consistently by the governing product and application framework.

The chain should remain explicit:

`long-term regression result → lower statistical bound → MRS → design coefficient C → design stress`

Each quantity has a different engineering meaning. Treating them as interchangeable is a design error.

## 7.1 The lower statistical bound is not yet MRS

The regression/extrapolation process produces a conservative lower estimate of long-term hydrostatic strength. In the older ISO 12162 edition available during redevelopment, that lower-confidence strength basis is used as the input to material classification at a defined reference condition.

The engineering distinction is:

> **The regression result is a continuous strength estimate. MRS is a standardized classification value derived from it.**

This matters because the exact numerical regression output is not simply copied into the material designation.

**Standards Validation Hold Point:** current terminology for the lower statistical value, the applicable reference condition and its relationship to MRS shall be checked against the authoritative current ISO 12162 edition before publication.

## 7.2 MRS is a standardized material-classification value

The older ISO 12162 edition available during redevelopment classifies the applicable lower-confidence strength into a preferred standardized series, using a downward classification rule.

Conceptually:

\[
\sigma_{LCL} \rightarrow \text{standardized downward classification} \rightarrow MRS
\]

The important design consequence is that MRS is a **classification value**, not the exact regression result and not yet the project design stress.

This also clarifies the PE100 designation introduced earlier in Investigation 3. The project material used during redevelopment treats PE100 as corresponding to an MRS class of 10 MPa. That relationship remains a Standards Validation item before publication, but the conceptual role is already clear:

> **PE100 identifies a material-classification branch. It does not mean that 10 MPa may be used directly as project allowable stress.**

This section therefore extends Investigation 3 rather than repeating it: Investigation 3 explains what the designation means; Investigation 7 shows how the classification enters the design calculation.

## 7.3 The design coefficient is a separate engineering input

The next step introduces the design coefficient \(C\).

The older ISO 12162 text available during redevelopment makes clear that the applicable coefficient belongs to the relevant product/system design framework rather than being universally fixed by the PE material designation alone.

Keep the distinction explicit:

`MRS = material-classification input`

`C = governing product / application / service design input`

Therefore two systems using the same PE100 material do not automatically have the same design-stress basis.

The engineer should not select \(C\) from memory or from an unrelated project. Its source, scope and applicability must be traceable to the governing standards path and Design Basis.

## 7.4 From MRS to design stress

The design-stress relationship used in the older ISO 12162 edition is:

\[
\sigma_s = \frac{MRS}{C}
\]

**EQ-013-002 — Design stress from MRS and design coefficient**

where:

- \(\sigma_s\) = design stress;
- \(MRS\) = minimum required strength;
- \(C\) = applicable design coefficient.

### Units

If MRS is expressed in MPa, \(\sigma_s\) is obtained in MPa because \(C\) is dimensionless.

### Derivation / standards basis

This is a standards-based classification-to-design relationship, not a first-principles derivation. Its final normative wording, definition of \(C\), reference conditions and rounding requirements shall be verified against the current authoritative standards before publication.

### Engineering use

Use EQ-013-002 to convert the standardized material-strength classification into the design-stress basis required for the subsequent pipe geometry / pressure relationship.

### Applicability limit

EQ-013-002 does **not** by itself establish:

- which \(C\) applies to a particular project;
- temperature or service-life capability;
- chemical compatibility;
- transient or fatigue suitability;
- fitting or joint capability;
- product conformity;
- or final allowable operating pressure.

Those questions remain part of the governing product/application framework and the project Design Basis.

### Common misuse

Do not substitute:

\[
\sigma_s=MRS
\]

unless the governing framework explicitly produces that result. Doing so implicitly removes the design-coefficient step and confuses material classification with design allowance.

## 7.5 Worked interpretation — why PE100 does not mean 10 MPa design stress

For illustration only, assume:

\[
MRS=10\text{ MPa}
\]

and assume that the governing framework has established:

\[
C=1.25
\]

Then, before any standards-prescribed rounding:

\[
\sigma_s=\frac{10}{1.25}=8.0\text{ MPa}
\]

The purpose of this example is limited to the transformation:

`MRS → C → design stress`

It does **not** establish that \(C=1.25\) is universally applicable to PE100, to every fluid, or to every product/application standard.

The lesson is the separation of roles:

- the material classification supplies MRS;
- the governing design framework supplies the applicable \(C\);
- together they establish the design-stress basis used in the next calculation stage.

## 7.6 Why C should never be copied blindly

The design coefficient should not be treated as a generic safety factor selected by preference.

Its applicability must be traced through the standards path established at the beginning of the chapter. Service conditions, additional stresses, temperature, time, environment and application-specific requirements may affect the governing design basis.

The correct workflow is:

`identify material class`

→ `identify governing product/application standard`

→ `identify applicable C`

→ `calculate design stress`

→ `apply geometry/pressure relationship`

not:

`PE100 → assume familiar C → calculate pressure`

This is the handoff to Investigation 8.

## 7.7 Engineering decision from Investigation 7

At the end of this Investigation, the engineer should be able to distinguish four quantities:

| Quantity | Engineering meaning |
|---|---|
| Lower statistical strength bound | Conservative output from the long-term regression/extrapolation framework |
| MRS | Standardized material-classification value |
| \(C\) | Applicable design coefficient from the governing standards/design framework |
| \(\sigma_s\) | Design-stress basis used in the subsequent geometry/pressure calculation |

The practical rule is:

> **Material classification establishes capability evidence. Design stress is established only after the applicable design coefficient is applied.**

The chapter chain is now:

`long-term evidence → lower statistical bound → MRS → C → design stress → SDR → pressure basis`

### Practical check before moving to Investigation 8

If a calculation begins with:

> “PE100 = 10 MPa allowable stress”

then the design chain is incomplete. The engineer must identify the governing design coefficient and standards/application basis before using the material classification in pressure design.

---

## Integration Review — Pass 02

### Continuity

- Investigation 6 ends at the conservative long-term statistical result and hands off to classification.
- Investigation 7 begins with classification and does not repeat the statistical-method discussion.
- Investigation 3 remains the terminology/designation introduction; Investigation 7 provides the quantitative design meaning.
- Investigation 7 stops at design stress and explicitly hands off geometry/SDR/pressure to Investigation 8.

### Equation control

- `EQ-013-001` remains the thin-wall hoop-stress approximation in Investigation 4.
- `EQ-013-002` is reserved here for the MRS-to-design-stress relationship.
- No Investigation 8 equation numbering is consumed in this pass.

### Duplication control

- PE100 is discussed only as needed to connect the earlier designation discussion to the quantitative chain.
- Detailed SDR and pressure-rating calculations remain deferred to Investigation 8.
- Temperature/service integration remains deferred to Investigation 9.

### Standards Validation Hold Points retained

Before publication, independently verify:

1. current ISO 12162 terminology for the lower long-term statistical value;
2. current classification reference condition;
3. current preferred-number/classification series and downward-classification rule;
4. PE100 ↔ MRS 10 MPa relationship in the governing current standards path;
5. current definition, source and permitted/minimum values of \(C\) for each application path used in the final chapter;
6. current design-stress equation wording and rounding rule.

### Pass 02 disposition

**READY FOR OWNER REVIEW.** No substantive change to the approved Batch 013-D engineering position was introduced. Changes are integration edits: continuity, terminology discipline, equation metadata, duplication control and a clean handoff to Investigation 8.
