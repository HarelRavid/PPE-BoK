# Batch 013-D — Investigation 7

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved redevelopment artifact  
**Integration target:** Chapter 13 Rev 1.0  
**PDS baseline:** 1.0 (frozen)

> Standards-validation note: the full ISO 12162 copy available during drafting is ISO 12162:1995, not the current edition. The engineering chain below may be used for redevelopment, but current terminology, classification boundaries, rounding rules, coefficients, reference conditions and normative requirements shall be reopened against the current authoritative edition before publication.

# Investigation 7 — How Does Long-Term Evidence Become MRS and Design Stress?

The regression process described in Investigations 5 and 6 produces a conservative long-term hydrostatic-strength basis. That result is still not the final design stress.

The next engineering step is classification.

For pressure-piping materials, the purpose of classification is to convert a continuous long-term strength result into a standardized material designation that can be used consistently by product and design standards.

The important chain is:

`long-term regression result → lower statistical bound → MRS → design coefficient C → design stress`

Each step has a different meaning.

## 7.1 The lower statistical bound is not yet MRS

The long-term regression process yields a lower conservative estimate of hydrostatic strength.

In the older ISO 12162 edition available for this review, this long-term lower-confidence value is used as the basis for material classification at the stated reference condition.

The engineering point is simple:

> **The regression result is a continuous strength estimate. MRS is a standardized classification value derived from it.**

The two should not be treated as interchangeable.

## 7.2 MRS is a classification value

The older ISO 12162 edition defines the **minimum required strength, MRS**, by rounding the applicable lower-confidence strength downward into a preferred standardized series.

This downward classification step matters.

It means that a material whose statistical lower-bound result lies above a classification threshold is not assigned its exact regression value as its material class. It is assigned the corresponding standardized MRS value below or at that result.

Conceptually:

\[
\sigma_{LCL} \rightarrow \text{standardized downward classification} \rightarrow MRS
\]

**Standards Validation Hold Point:** the exact current terminology, reference condition, preferred-number series and classification boundaries shall be rechecked against the current authoritative ISO 12162 edition before publication.

## 7.3 What PE100 means in this chain

For engineering interpretation, the designation PE100 should be understood as a material-classification statement tied to an MRS class.

The supporting project literature supplied for this chapter uses **MRS = 10 MPa** for PE100 and then uses that value as the material-strength input to later pressure calculations.

The critical design lesson is:

> **PE100 does not mean that 10 MPa may be used directly as the design stress.**

The classification value is only one input.

## 7.4 Design coefficient C

The classification framework introduces a design coefficient \(C\), with a value greater than 1, to account for service and system considerations not represented solely by the lower-confidence material-strength classification.

The older ISO 12162 text also makes clear that the applicable \(C\) value belongs to the relevant product/system framework rather than being universally fixed by material designation alone.

This distinction is essential:

`MRS = material-classification input`

while

`C = application / product / service design input`

Therefore two systems using the same PE100 material may not necessarily use the same design coefficient.

## 7.5 From MRS to design stress

The older ISO 12162 edition gives the design-stress relationship in the form:

\[
\sigma_s = \frac{MRS}{C}
\]

**EQ-013-002 — Design stress from MRS and design coefficient**

where:

- \(\sigma_s\) = design stress;
- \(MRS\) = minimum required strength;
- \(C\) = applicable design coefficient.

The older edition also applies a prescribed rounding rule to the calculated design stress.

### Units

If MRS is expressed in MPa, \(\sigma_s\) is obtained in MPa because \(C\) is dimensionless.

### Engineering use

The equation converts a material-classification value into a lower design-stress basis for subsequent pressure/geometry calculations.

### Validity / applicability limit

This equation does **not** by itself establish:

- which \(C\) applies to a particular project;
- temperature capability;
- chemical compatibility;
- transient or fatigue suitability;
- fitting/joint capability;
- product conformity;
- or final allowable operating pressure.

Those depend on the applicable product/application standard and Design Basis.

### Common misuse

A frequent error is to substitute:

\[
\sigma_s = MRS
\]

which implicitly assumes \(C = 1\).

For a pressure-piping design framework, that would remove the design-coefficient step entirely and confuse material classification with design allowance.

## 7.6 Simple engineering interpretation example

Assume, for illustration only:

\[
MRS = 10\text{ MPa}
\]

If the governing framework requires:

\[
C = 1.25
\]

then, before any prescribed rounding:

\[
\sigma_s = \frac{10}{1.25}
\]

\[
\sigma_s = 8.0\text{ MPa}
\]

This example is intentionally limited.

It demonstrates only:

`MRS → C → design stress`

It does **not** establish that \(C = 1.25\) is applicable to every PE100 system.

The project literature supplied for this review also illustrates why this distinction matters: different assumed/applicable \(C\) values materially change the resulting pressure capability. Those application-specific coefficient claims remain subject to Standards Validation before reuse in the chapter.

## 7.7 Why C should never be copied blindly

The design coefficient is not simply a generic “safety factor” that may be selected by preference.

Its applicability must be traced to the governing standards path.

The older ISO 12162 edition points the applicable coefficient back to the product/system framework and identifies service conditions, additional stresses, temperature, time and environment as relevant considerations.

Therefore the correct workflow is:

`identify material class`

→ `identify governing product/application standard`

→ `identify applicable C`

→ `calculate design stress`

→ `apply geometry/pressure relationship`

not:

`PE100 → assume familiar C → calculate pressure`

## 7.8 Engineering decision from Investigation 7

At the end of this Investigation, the engineer should be able to distinguish four separate quantities:

| Quantity | Engineering meaning |
|---|---|
| Lower statistical strength bound | Conservative result from long-term regression |
| MRS | Standardized material-classification value |
| \(C\) | Applicable design coefficient from the governing standards framework |
| \(\sigma_s\) | Design-stress basis used in later geometry/pressure calculations |

The practical rule is:

> **Material classification establishes capability evidence. Design stress is created only after the applicable design coefficient is applied.**

And the full chain now becomes:

`ISO 9080 evidence → lower bound → ISO 12162 classification → MRS → C → design stress → SDR → pressure designation`

### Practical check — before moving on

If a calculation starts with:

> “PE100 = 10 MPa allowable stress”

the design chain is incomplete.

The engineer must still identify the applicable design coefficient and the governing product/application framework before using the value in pressure design.

## Standards Validation Hold Points

Before integration into the publication baseline, reopen and verify against the current authoritative standards:

1. current ISO 12162 terminology for the long-term lower statistical value;
2. current reference condition used for classification;
3. current preferred-number/classification series and downward-rounding rule;
4. current definition and rounding rule for design stress;
5. the applicable source and minimum/permitted value of \(C\) for each product/application path used later in the chapter;
6. PE100 ↔ MRS 10 MPa designation in the governing current standards path.
