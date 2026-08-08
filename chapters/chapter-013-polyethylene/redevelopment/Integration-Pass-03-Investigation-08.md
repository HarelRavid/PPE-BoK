# Integration Pass 03 — Investigation 8

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Integrated draft for author approval  
**Integration source:** Batch 013-E + Batch 013-E2  
**PDS baseline:** 1.0 (frozen)

> Standards-validation note: current-edition definitions, coefficients, product-specific applicability, dimensional terminology, pressure-designation conventions, marking requirements, temperature treatment and normative requirements remain subject to the final Standards Validation gate.

# Investigation 8 — How Do MRS, Design Stress, SDR and Product Identification Become a Pressure Basis?

Investigations 5–7 established the material side of the chain:

\[
\text{long-term evidence}\rightarrow MRS\rightarrow C\rightarrow\sigma_s
\]

The next step introduces geometry and product identification.

The practical engineering question is:

> **Given a qualified material, an applicable design coefficient and a selected pipe geometry, what pressure basis follows—and what still remains to be checked before that basis can be used as a project operating limit?**

## 8.1 SDR converts pipe dimensions into a useful geometry parameter

For a pipe series:

\[
SDR=\frac{d_n}{e_n}
\]

**EQ-013-003 — Standard Dimension Ratio**

where:

- \(SDR\) = standard dimension ratio, dimensionless;
- \(d_n\) = nominal outside diameter;
- \(e_n\) = nominal wall thickness.

Because numerator and denominator have the same units, SDR is dimensionless.

The engineering interpretation matters more than memorizing the expression:

> **For the same nominal diameter, lower SDR means a thicker nominal wall.**

Therefore, all else equal:

\[
SDR\downarrow \Rightarrow e_n\uparrow \Rightarrow pressure\ capability\uparrow
\]

This does **not** mean “select the lowest SDR available.” Thicker pipe also affects bore, hydraulic performance, weight, cost, availability, fittings and installation.

## 8.2 Connecting design stress to pressure

The project literature supplied for this chapter uses the PE pressure relationship in terms of MRS, \(C\) and SDR as:

\[
MOP=\frac{20\,MRS}{C(SDR-1)}
\]

when pressure is expressed in bar and MRS in MPa.

From Investigation 7:

\[
\sigma_s=\frac{MRS}{C}
\]

The corresponding stress/geometry form is:

\[
p=\frac{2\sigma_s}{SDR-1}
\]

when \(p\) and \(\sigma_s\) are expressed in the same stress units.

**EQ-013-004 — SDR pressure relationship**

### Units

If \(\sigma_s\) is in MPa, EQ-013-004 returns pressure in MPa.

Since:

\[
1\text{ MPa}=10\text{ bar}
\]

the corresponding form in bar is:

\[
p_{bar}=\frac{20\sigma_s}{SDR-1}
\]

### Source basis

This relationship is carried into the integration pass from the approved redevelopment batch and supporting project literature. Its exact current normative form, notation and applicability shall be checked against the governing current product/application standards during final Standards Validation.

### Engineering use

EQ-013-004 connects:

`design-stress basis + nominal geometry → reference pressure basis`

It does **not** by itself establish the final allowable project operating pressure.

### Common misuse

A correct arithmetic result is often treated as a complete design approval. That is the wrong stopping point.

> **Calculated pressure basis ≠ automatically allowable operating pressure.**

The pressure equation occurs in the middle of the design process, not at the end.

## 8.3 Worked Example A — From PE100 to a reference pressure basis

Consider, for illustration only, a PE100 pipe with:

\[
MRS=10\text{ MPa}
\]

Assume that the governing framework for the example has established:

\[
C=1.25
\]

From EQ-013-002:

\[
\sigma_s=\frac{10}{1.25}=8.0\text{ MPa}
\]

Now take:

\[
SDR=11
\]

Using EQ-013-004:

\[
p=\frac{2(8)}{11-1}
\]

\[
p=1.6\text{ MPa}=16\text{ bar}
\]

### What this example proves

It demonstrates the calculation chain:

\[
MRS\rightarrow C\rightarrow\sigma_s\rightarrow SDR\rightarrow reference\ pressure\ basis
\]

### What this example does not prove

It does not establish that:

- \(C=1.25\) applies to every PE100 application;
- 16 bar is allowable at elevated temperature;
- 16 bar is suitable for gas or any other specific service;
- the fluid is chemically compatible;
- fittings and joints have equivalent capability;
- surge/transient conditions are acceptable;
- the selected product complies with the governing current product standard;
- or the installed system may be operated at 16 bar.

This is therefore a **reference pressure-basis calculation**, not a complete design approval.

**Standards Validation Hold Point:** the PE100 ↔ MRS basis, coefficient value, current pressure relationship, dimensional definitions and any prescribed rounding rules used in this example shall be independently revalidated before publication.

## 8.4 Sensitivity — what changes the calculated pressure basis?

For the same material classification:

| Change | Direct effect on calculated pressure basis | Engineering implication |
|---|---|---|
| \(C\uparrow\) | pressure ↓ | More conservative or different application-specific basis |
| \(C\downarrow\) | pressure ↑ | Requires explicit governing-standards justification |
| SDR ↑ | pressure ↓ | Thinner nominal wall relative to diameter |
| SDR ↓ | pressure ↑ | Thicker nominal wall relative to diameter |
| MRS ↑ | pressure ↑ | Higher material-classification input |

This gives the engineer a useful diagnostic tool.

If a supplier proposes a higher allowable pressure without changing the material designation, ask:

- Did the geometry change?
- Did the applicable design coefficient change?
- Did the service or temperature basis change?
- Did the governing product/application standard change?
- Or did only the claimed allowable pressure change?

## 8.5 Geometry sensitivity example

Keep, for comparison only:

\[
MRS=10\text{ MPa}, \qquad C=1.25
\]

For SDR 11:

\[
p=16\text{ bar}
\]

For SDR 9:

\[
p=\frac{20(10)}{1.25(9-1)}=20\text{ bar}
\]

The engineering lesson is not that a particular PE100 SDR 9 product is universally a 20-bar solution.

It is:

> **Changing SDR changes the reference pressure basis even when the material designation remains unchanged.**

That is why material class and geometry must remain separate concepts in the design record.

## 8.6 Temperature and service conditions prevent the first calculation from becoming the final answer

The reference pressure calculation is only one stage of the design chain.

The required sequence is:

`reference pressure basis`

→ `governing product/application standard`

→ `temperature/time treatment`

→ `fluid/environment compatibility`

→ `fittings, joints and components`

→ `transients and other Design Basis loads`

→ `project allowable operating pressure`

The exact temperature/time treatment may be a factor, table, different allowable-stress basis or another standards-specific method. It shall not be universalized across PE applications without an authoritative standards basis.

## 8.7 The pipe is not the system

A calculation for straight pipe cannot establish the capability of the assembled piping system.

The engineer must separately confirm, as applicable:

- fittings;
- valves;
- fusion joints;
- fabricated components;
- branches and local geometry;
- installation damage;
- temperature;
- chemical environment;
- transient pressure;
- imposed displacement;
- supports and restraint;
- application-specific qualification requirements.

This distinction is carried forward deliberately into Investigation 9, where those checks are integrated into the Design Basis decision workflow.

## 8.8 FIG-013-004 — PE pressure-design decision chain

```text
Qualified PE material
        ↓
Long-term strength evidence
        ↓
MRS
        ↓
Applicable design coefficient C
        ↓
Design stress
        ↓
Selected SDR / dimensions
        ↓
Reference pressure basis
        ↓
Temperature / time
        ↓
Fluid + environment
        ↓
Product / application standard
        ↓
Fittings + joints + components
        ↓
Transients + other Design Basis loads
        ↓
Allowable project operating pressure
```

The figure should make one point visually unavoidable:

> **The pressure equation occurs in the middle of the design process, not at the end.**

## 8.9 Pipe marking is an identification package—not a Design Basis

A PE pipe marking can provide valuable traceability and classification information, but it should be interpreted as a set of inputs to engineering verification rather than as a complete statement of system suitability.

### TAB-013-002 — What pipe marking may tell the engineer

| Marking / information type | What it may tell the engineer | What it does **not** establish by itself |
|---|---|---|
| Manufacturer / traceability identification | Who produced the product and how it may be traced | Installed quality or project suitability |
| Material designation, e.g. PE100 | Material-classification branch | Allowable project pressure or chemical suitability |
| SDR / dimensional series | Nominal geometry relationship | Temperature-adjusted capability or system rating |
| Nominal pressure / pressure designation where used | Standardized pressure-class information under defined reference conditions | Unconditional allowable operating pressure |
| Product-standard reference | Product conformity framework being claimed | Applicability of that standard to the actual project service |
| Production / batch identification | Manufacturing traceability | Absence of damage after transport or installation |
| Size / dimensions | Nominal product geometry | As-installed minimum wall at a damaged location |

> **The pipe marking tells the engineer what product is being presented. It does not tell the engineer whether the complete installed system satisfies the project Design Basis.**

### Engineering interpretation workflow

`read marking → identify product standard → verify material class → verify SDR/dimensions → confirm service/application scope → apply temperature/service conditions → verify fittings/joints/system → accept or reject`

### Common misuse

Treating a marking such as `PE100 / SDR 11 / PN16` as a compact project approval collapses material classification, geometry, product identification and project suitability into one label.

The marking may support identification and traceability. It does not resolve temperature, fluid compatibility, application scope, transient loading, fitting/joint capability, installation damage or other Design Basis variables.

## 8.10 Practical engineering check

When reviewing a PE pressure calculation and product identification, the engineer should be able to answer:

1. What material class was used?
2. What MRS basis was used?
3. Where did \(C\) come from?
4. What SDR and dimensional definitions were used?
5. What pressure relationship was used?
6. Are the units and conversions consistent?
7. What temperature/time basis applies?
8. Which product/application standard governs?
9. What does the product marking actually demonstrate?
10. Are fittings and joints covered by the same design basis?
11. Have service-specific loads and environmental effects been addressed?

If these questions cannot be answered, the fact that the pipe carries a familiar marking or the calculation produces a plausible pressure does not make the design complete.

## 8.11 Engineering decision from Investigation 8

At the end of Investigation 8 the engineer should be able to keep five different ideas separate:

| Quantity / information | Engineering meaning |
|---|---|
| MRS | Standardized material-classification input |
| \(C\) | Applicable design coefficient from the governing framework |
| \(\sigma_s\) | Design-stress basis |
| SDR | Nominal geometry relationship |
| Pipe marking / pressure designation | Product identification and standards-context information, not complete project approval |

The chapter therefore carries forward this rule into Investigation 9:

> **Calculate a reference pressure basis first; then prove that the actual project Design Basis remains inside the qualified service envelope.**

## Standards Validation Hold Points

Before publication, reopen and verify against the current authoritative governing standards:

1. exact current definition of SDR and dimensional terminology;
2. normative pressure/MOP equation and unit convention;
3. current applicability and source of \(C\);
4. current temperature/time treatment;
5. product-series relationships such as SDR/PN where used;
6. rounding rules;
7. fitting/component pressure-rating provisions;
8. every numerical standards-derived example;
9. mandatory marking fields, wording, frequency and durability requirements;
10. manufacturer/batch/traceability requirements;
11. pressure/PN/MOP designation conventions;
12. required product-standard identification and application-specific marking requirements.
