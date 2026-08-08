# Batch 013-E — Investigation 8

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved redevelopment artifact  
**Integration target:** Chapter 13 Rev 1.0  
**PDS baseline:** 1.0 (frozen)

> Standards-validation note: the pressure relationships and application-specific factors used during drafting are supported by the project literature and older standards context available in the review set. Exact current definitions, coefficients, product-specific applicability, temperature treatment and normative requirements shall be revalidated against the current authoritative standards before publication.

# Investigation 8 — How Do MRS, Design Stress and SDR Become a Pressure Basis?

Investigations 5–7 established the material side of the chain:

\[
\text{long-term evidence}\rightarrow MRS\rightarrow C\rightarrow\sigma_s
\]

The next step introduces pipe geometry.

The objective is to answer a practical engineering question:

> **Given a qualified material, an applicable design coefficient and a selected pipe geometry, what pressure basis follows — and what still remains to be checked?**

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

The project literature supplied for this chapter gives the PE pressure relationship in terms of MRS, \(C\) and SDR as:

\[
MOP=\frac{20\,MRS}{C(SDR-1)}
\]

when pressure is expressed in bar and MRS in MPa.

From Investigation 7:

\[
\sigma_s=\frac{MRS}{C}
\]

Therefore the same basic relationship may be written conceptually as:

\[
p=\frac{2\sigma_s}{SDR-1}
\]

when \(p\) and \(\sigma_s\) are expressed in the same stress units.

**EQ-013-004 — SDR pressure relationship**

### Unit warning

If \(\sigma_s\) is in MPa, EQ-013-004 returns pressure in MPa.

Since:

\[
1\text{ MPa}=10\text{ bar}
\]

the corresponding expression in bar becomes:

\[
p_{bar}=\frac{20\sigma_s}{SDR-1}
\]

This unit conversion is why the factor 20 appears in the MRS-based expression used in the supplied project literature.

## 8.3 What EQ-013-004 actually means

The equation connects three things:

**material/design-stress basis**

+

**pipe geometry**

→

**pressure basis**

It does **not**, by itself, prove that this pressure may be used as the project's operating pressure.

That distinction is fundamental.

The supplied engineering review itself demonstrates this: a PE100 SDR 11 calculation using one coefficient produces 16 bar at the initial reference calculation, but the same document subsequently reduces the pressure after applying a different application-specific coefficient and temperature treatment.

So:

> **Calculated pressure basis ≠ automatically allowable operating pressure.**

## 8.4 Worked Example A — From PE100 to pressure basis

Consider a PE100 pipe with:

\[
MRS=10\text{ MPa}
\]

For this **illustrative calculation only**, assume that the governing framework has established:

\[
C=1.25
\]

From EQ-013-002:

\[
\sigma_s=\frac{10}{1.25}=8.0\text{ MPa}
\]

Now consider:

\[
SDR=11
\]

Using EQ-013-004:

\[
p=\frac{2(8)}{11-1}
\]

\[
p=1.6\text{ MPa}
\]

or:

\[
p=16\text{ bar}
\]

This reproduces the same numerical reference calculation contained in the supplied project literature for PE100 SDR 11 under that assumed coefficient.

### What this example proves

It proves the calculation chain:

\[
MRS\rightarrow C\rightarrow\sigma_s\rightarrow SDR\rightarrow pressure
\]

### What this example does **not** prove

It does not prove that:

- \(C=1.25\) applies to the project;
- 16 bar is allowable at elevated temperature;
- 16 bar is suitable for gas service;
- the fluid is chemically compatible;
- fittings and joints have equivalent capability;
- surge/transient conditions are acceptable;
- the selected product complies with the governing product standard;
- or the system may be operated at 16 bar.

That is exactly why this is a **pressure-basis calculation**, not a complete design approval.

## 8.5 Sensitivity — what changes the result?

The equation makes several design sensitivities immediately visible.

For the same MRS:

| Change | Direct effect on calculated pressure basis | Engineering implication |
|---|---|---|
| \(C\uparrow\) | pressure ↓ | More conservative/application-specific design basis |
| \(C\downarrow\) | pressure ↑ | Requires explicit standards justification |
| SDR ↑ | pressure ↓ | Thinner wall relative to diameter |
| SDR ↓ | pressure ↑ | Thicker wall relative to diameter |
| MRS ↑ | pressure ↑ | Higher material-classification strength input |

This gives the engineer a useful diagnostic tool.

If a supplier proposes increasing allowable pressure without changing the material, ask:

> Did the geometry change?

> Did the applicable design coefficient change?

> Did the service/temperature basis change?

> Or was only the claimed allowable pressure changed?

## 8.6 Geometry sensitivity example

Keep:

\[
MRS=10\text{ MPa}
\]

and, purely for comparison:

\[
C=1.25
\]

For SDR 11:

\[
p=16\text{ bar}
\]

For SDR 9:

\[
p=\frac{20(10)}{1.25(9-1)}
\]

\[
p=20\text{ bar}
\]

The point is **not** that PE100 SDR 9 is universally a 20-bar design solution.

The point is:

> changing SDR alone changes the pressure basis even though the material designation remains PE100.

The supplied project review makes the same engineering observation: reducing SDR increases calculated MOP, but it also notes significant cost consequences and then applies additional service-specific factors.

## 8.7 Temperature exposes the danger of stopping at the first calculation

The supplied project literature gives an example of why the first calculated pressure cannot automatically become MOP.

For its particular gas-service analysis at elevated temperature, it introduces an additional temperature-related factor and obtains a lower pressure result than the ambient/reference calculation.

That factor is not carried into this chapter as a universal PE derating rule.

Instead, the chapter teaches the engineering workflow:

\[
\text{reference pressure basis}
\]

↓

\[
\text{governing application/product standard}
\]

↓

\[
\text{temperature/time adjustment}
\]

↓

\[
\text{fluid/environment compatibility}
\]

↓

\[
\text{fittings + joints + components}
\]

↓

\[
\text{transients and other Design Basis loads}
\]

↓

\[
\boxed{\text{project allowable operating pressure}}
\]

The exact temperature factor and its mathematical form are **standards-path dependent** and therefore remain behind a Standards Validation hold point.

## 8.8 The pipe is not the system

A pressure calculation for straight pipe cannot establish the rating of an assembled piping system.

At minimum the engineer must consider:

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
- supports/restraint;
- and any application-specific qualification requirements.

The supplied literature separately discusses fittings, fabricated components and welded joints after performing the straight-pipe pressure calculation. That separation is retained here deliberately.

## 8.9 Engineering workflow

**FIG-013-004 — PE pressure-design decision chain**

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
Calculated pressure basis
        ↓
Temperature / time
        ↓
Fluid + environment
        ↓
Product/application standard
        ↓
Fittings + joints + components
        ↓
Transients + other Design Basis loads
        ↓
Allowable project operating pressure
```

The figure's purpose is to make one thing visually unavoidable:

**the pressure equation occurs in the middle of the design process, not at the end.**

## 8.10 Practical engineering check

When reviewing a PE pressure calculation, the engineer should be able to answer:

1. What material class was used?
2. What MRS was used?
3. Where did \(C\) come from?
4. What SDR and dimensional definition were used?
5. What pressure equation was used?
6. Are the units consistent?
7. What temperature/time basis applies?
8. Which product/application standard governs?
9. Are fittings and joints covered by the same pressure basis?
10. Have service-specific loads and environmental effects been addressed?

If the calculation cannot answer these questions, the fact that it produces a pressure value does not make it a complete pressure design.

## Standards Validation Hold Points

Before publication reopen and verify:

- the exact current definition of SDR and dimensional terminology;
- the normative pressure/MOP equation and unit convention;
- current applicability of \(C\);
- current temperature/time derating methodology;
- product-series relationships such as SDR/PN where used;
- rounding rules;
- fitting/component pressure-rating provisions;
- every numerical standards-derived example;
- any application-specific factor or coefficient mentioned in the supporting project literature.
