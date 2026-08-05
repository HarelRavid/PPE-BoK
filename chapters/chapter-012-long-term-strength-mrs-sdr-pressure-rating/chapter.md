---
chapter: 12
title: Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating
part: Material Selection
status: research-based-draft
language: en
---

# Chapter 12 — Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating

## Why This Chapter Matters

A pressure rating printed on a plastic pipe can appear deceptively simple. An engineer may see **PE100, SDR 11, PN 16** and assume that the system is suitable for any service below 16 bar.

That interpretation is incomplete and can be unsafe.

The pressure capability of a thermoplastic piping system is not determined by short-term yield strength alone. It is derived from long-duration pressure testing, statistical extrapolation, material classification, a design coefficient, pipe geometry, reference temperature, service duration, and the applicable product standard. The resulting nominal pressure is a classification under defined reference conditions—not a universal allowable operating pressure for every fluid, temperature, installation, transient, or service life.

This chapter explains how long-term hydrostatic strength is converted into an engineering pressure rating, what the principal terms mean, and which checks remain necessary after the calculation has been completed.

---

## 12.1 Why Short-Term Strength Is Not Enough

Thermoplastics are viscoelastic. Their response to stress depends on time and temperature as well as stress magnitude.

A pipe specimen may withstand a high internal pressure for a short laboratory test and still be unsuitable for decades of continuous service at a much lower stress. Conversely, a material selected from a short-term tensile value alone may appear stronger than another material while providing inferior long-term pressure performance.

For this reason, pressure-pipe materials are characterized using long-term hydrostatic test data obtained from pipe specimens. The objective is not merely to determine when a specimen bursts. It is to establish a statistically supported relationship between:

- hoop stress;
- time to failure;
- test temperature;
- and the observed failure behaviour.

The resulting long-term strength framework is one of the fundamental differences between thermoplastic pressure-pipe design and ordinary short-term component sizing.

---

## 12.2 Long-Term Hydrostatic Strength

ISO 9080 specifies a statistical extrapolation method for predicting the long-term hydrostatic strength of thermoplastic materials in pipe form. The method is based on pressure-test data obtained at applicable temperatures and was developed from pipe-system test data.

In simplified terms, multiple pipe specimens are tested under internal pressure at different hoop stresses and temperatures. Their failure times are recorded. Statistical analysis is then used to describe and extrapolate the stress-versus-time relationship.

This does **not** mean that one pipe is pressurized for fifty years before a material is classified. It means that a defined body of test data, including accelerated testing at elevated stresses and temperatures, is evaluated using the prescribed extrapolation method.

The full ISO 9080 procedure includes requirements that cannot be replaced by a simple hand calculation. The method addresses data quality, regression, extrapolation limits, failure branches, confidence considerations, and temperature relationships. A piping engineer generally uses the resulting classified material values rather than reproducing the complete statistical analysis during routine design.

### Engineering interpretation

Long-term hydrostatic strength is a material-characterization result obtained from pipe specimens under controlled conditions. It is not, by itself:

- the allowable design stress;
- the pressure rating of a particular pipe;
- proof of chemical compatibility;
- proof of fatigue resistance;
- proof of joint quality;
- or a guarantee of service life in every application.

It is the starting point from which further design values are derived.

---

## 12.3 The Reference Strength at 50 Years

Thermoplastic pressure-pipe classification commonly uses the predicted lower confidence limit of hydrostatic strength at a specified reference time and temperature. In the ISO framework, the material classification is associated with long-term behaviour at **20°C and 50 years**, subject to the definitions and procedures of the relevant standards.

The lower confidence concept matters. Engineering classification is not based simply on the average predicted strength. It is intended to represent a statistically conservative lower estimate derived from the regression analysis.

The relevant notation and exact definitions should be taken from the current editions of ISO 9080, ISO 12162, and the applicable product standard. This chapter deliberately avoids reproducing protected standard text or replacing the formal procedure with an informal summary.

### What the 50-year reference does and does not mean

The use of a 50-year reference point does not mean:

- that the pipe automatically fails after 50 years;
- that every installed system is guaranteed to last 50 years;
- or that service beyond 50 years is prohibited.

It means that material classification and design values are referenced to a defined long-term test and extrapolation framework. Actual system life depends on the complete service envelope, including temperature, pressure history, fluid environment, installation quality, joints, loads, oxidation, ultraviolet exposure, transients, maintenance, and damage.

Likewise, a nominal 50-year classification should not be interpreted as evidence that an arbitrary higher stress is acceptable for a shorter period without using the relevant standard, design method, and verified time-temperature data.

---

## 12.4 Minimum Required Strength — MRS

ISO 12162 establishes the classification and designation of thermoplastic materials for pressure applications and provides a method for calculating design stress.

The **Minimum Required Strength (MRS)** is the classified long-term strength value assigned in accordance with the standard framework. It is expressed in megapascals.

For example:

- a material designated **PE 100** is associated with an MRS class of 10 MPa;
- a material designated **PE 80** is associated with an MRS class of 8 MPa.

The designation should be interpreted carefully.

**PE100 does not mean:**

- 100 MPa tensile strength;
- 100 bar allowable pressure;
- a 100-year guaranteed service life;
- or universal superiority over every lower-class or different polymer system.

It identifies a polyethylene material class within the applicable long-term hydrostatic-strength framework.

### MRS is not a complete material specification

Two materials with the same MRS classification may differ in:

- resistance to slow crack growth;
- rapid crack propagation performance;
- oxidation stability;
- processing behaviour;
- fusion characteristics;
- chemical resistance;
- pigment and additive package;
- and product certification.

MRS is essential, but it is only one element of material qualification.

---

## 12.5 PE100, PE100-RC and PE100+

These designations are frequently confused.

### PE100

PE100 is a long-term strength classification linked to an MRS of 10 MPa under the applicable ISO classification framework.

### PE100-RC

PE100-RC refers to PE100 materials qualified for enhanced resistance to slow crack growth under the relevant material and product requirements. The designation does not create a higher MRS class and does not remove the need to evaluate temperature, pressure, chemistry, joining, fatigue, installation damage, stress concentration, and abnormal loads.

### PE100+

PE100+ is an industry quality-association designation for listed PE100 materials that satisfy the association's recurring independent-testing requirements. It is not a strength class above PE100 and should not be inserted into pressure equations as though it had an MRS greater than 10 MPa.

A material may therefore be PE100, may additionally satisfy PE100-RC requirements, and may also appear on a PE100+ quality listing. These terms describe different aspects of qualification and should not be used interchangeably.

---

## 12.6 From MRS to Design Stress

The material classification is converted to a design stress using a design coefficient.

A common representation is:

\[
\sigma_s = \frac{MRS}{C}
\]

where:

- \(\sigma_s\) = design stress, in MPa;
- \(MRS\) = minimum required strength class, in MPa;
- \(C\) = overall service or design coefficient, dimensionless.

The coefficient is greater than 1, so the design stress is lower than the MRS.

### What the design coefficient represents

The coefficient provides design allowance for factors not fully represented by the classified material strength. Its prescribed or minimum value depends on the material family, application, product standard, conveyed fluid, regulatory framework, and project requirements.

It should not be selected by habit or copied from an unrelated service.

For example, a coefficient commonly used for PE water service cannot automatically be assumed valid for:

- fuel gas;
- compressed gas;
- aggressive chemicals;
- unusually severe cyclic service;
- elevated temperature;
- or a project governed by a different code.

The applicable product and design standards must establish the required coefficient and any additional reduction factors.

### Design stress is still conditional

Even after dividing MRS by the correct coefficient, the result is not necessarily the final allowable stress for the actual service. Temperature, service duration, chemical environment, cyclic loading, and code-specific rules may require further adjustment or a different design procedure.

---

## 12.7 Standard Dimension Ratio — SDR

The **Standard Dimension Ratio (SDR)** describes pipe geometry:

\[
SDR = \frac{d_n}{e_n}
\]

where:

- \(d_n\) = nominal outside diameter;
- \(e_n\) = nominal wall thickness, as defined by the applicable product standard.

Both dimensions must be expressed in the same units, so SDR is dimensionless.

A lower SDR corresponds to a thicker wall for a given outside diameter. A higher SDR corresponds to a thinner wall.

Examples:

- SDR 11 is thicker than SDR 17 at the same nominal outside diameter;
- SDR alone does not identify the material;
- the same SDR does not produce the same pressure capability for materials having different design stresses.

### SDR is a geometry classification, not a performance guarantee

Knowing that a pipe is SDR 11 does not tell the engineer whether it is suitable for service. The engineer must also know:

- the material classification;
- the applicable design coefficient;
- temperature;
- product standard;
- pressure definition;
- fluid service;
- and any derating or additional design requirements.

---

## 12.8 Relationship Between Hoop Stress, Pressure and SDR

For the conventional ISO pressure-pipe relationship based on outside diameter and wall thickness, hoop stress may be expressed as:

\[
\sigma = \frac{p(d_n-e_n)}{2e_n}
\]

Using \(SDR=d_n/e_n\), this becomes:

\[
\sigma = \frac{p(SDR-1)}{2}
\]

Rearranging for pressure:

\[
p = \frac{2\sigma}{SDR-1}
\]

Substituting the design stress:

\[
p = \frac{2MRS}{C(SDR-1)}
\]

where:

- \(p\) = pressure in MPa when stress values are in MPa;
- \(MRS\) = minimum required strength in MPa;
- \(C\) = design coefficient;
- \(SDR\) = standard dimension ratio.

For pressure expressed in bar:

\[
p_{bar} = \frac{20MRS}{C(SDR-1)}
\]

because 1 MPa equals 10 bar.

### Assumptions and limitations

This relationship is used within standardized thermoplastic pressure-pipe design conventions, but it must not be detached from the relevant standard system. It assumes:

- the diameter and wall definitions prescribed by the applicable convention;
- a uniform pressure-resisting wall;
- a qualified thermoplastic pressure-pipe material;
- a design stress applicable to the stated reference conditions;
- and no separate governing requirement that reduces the allowable pressure.

The equation does not independently address:

- temperature derating;
- chemical reduction factors;
- cyclic or transient loading;
- external pressure or vacuum;
- local stresses at branches, flanges, valves, supports, or restraints;
- scratches, notches, ovality, or installation damage;
- joint strength and workmanship;
- multilayer or lined constructions;
- or code-specific design rules.

---

## 12.9 Worked Example — PE100 SDR 11 Water Pipe

Assume:

- material class: PE100;
- \(MRS=10\,MPa\);
- design coefficient: \(C=1.25\), where this value is permitted by the applicable water-pipe standard and project requirements;
- pipe geometry: SDR 11;
- reference conditions appropriate to the nominal classification.

Then:

\[
p = \frac{2(10)}{1.25(11-1)}
\]

\[
p = \frac{20}{12.5}=1.6\,MPa
\]

Therefore:

\[
p=16\,bar
\]

This explains the familiar PE100 SDR 11 PN 16 relationship for the applicable reference water-service convention.

### What this example does not prove

The calculation does not prove that the same pipe may continuously carry every fluid at 16 bar under all conditions. Before specifying the system, the engineer must still verify:

- the current product standard;
- the fluid application;
- design and operating temperatures;
- design life;
- chemical compatibility;
- pressure cycles and transients;
- surge pressure;
- jointing method;
- component ratings;
- and installation configuration.

---

## 12.10 Nominal Pressure — PN

**PN** is a standardized nominal pressure designation associated with a piping component or system under defined reference conditions. It is a convenient classification, but it is frequently misunderstood as an unconditional maximum allowable operating pressure.

The meaning of PN must be read together with:

- the applicable product standard;
- reference temperature;
- material;
- design coefficient;
- component type;
- and service conditions.

### PN is not necessarily the operating limit at elevated temperature

Thermoplastic strength decreases as temperature increases. Therefore, a pipe classified as PN 16 at the reference temperature may have a substantially lower allowable operating pressure at a higher continuous service temperature.

The applicable pressure-temperature relationship or reduction factors must be taken from the relevant standard and qualified product data. Generic derating tables should not be transferred between polymer families, grades, or manufacturers without verification.

### The system rating is controlled by the weakest applicable component

A pipeline assembled from PN 16 pipe is not automatically a PN 16 system. The complete pressure boundary may include:

- fittings;
- valves;
- flanges;
- branch saddles;
- mechanical couplings;
- instruments;
- gaskets;
- transition joints;
- and fabricated components.

The allowable system pressure cannot exceed the governing rating of the applicable component, joint, design condition, or code requirement.

---

## 12.11 MOP, Operating Pressure and Design Pressure

Terms such as **Maximum Operating Pressure (MOP)**, operating pressure, design pressure, allowable pressure, and nominal pressure are not interchangeable.

Their exact definitions depend on the governing standard and industry.

In general engineering usage:

- **operating pressure** describes pressure expected during operation;
- **design pressure** defines a design condition under the governing code or project basis;
- **MOP** is used in certain standards for the maximum pressure permitted during operation under specified conditions;
- **PN** is a nominal classification;
- **test pressure** is the pressure applied under a defined test procedure.

The project documentation should define each term explicitly and use it consistently. Many errors occur because a value is transferred between a product catalogue, process datasheet, stress calculation, and test procedure without preserving its original definition.

---

## 12.12 Temperature and Time Derating

The reference classification is not a universal pressure-temperature envelope.

At elevated temperature, the predicted long-term hydrostatic strength changes. Product standards and manufacturer design data may provide allowable pressure reduction factors, time-dependent strength values, or specific pressure-temperature tables.

The engineer must distinguish between:

- temporary exposure;
- intermittent operation;
- continuous operation;
- and cumulative time at each temperature.

A short cleaning cycle at elevated temperature may require a different assessment from continuous high-temperature operation, but it should not be ignored merely because it is brief.

Where a system operates at multiple temperatures and pressures, cumulative damage or service-time allocation may need to be assessed using the method required by the relevant standard. A single average temperature can conceal severe periods that dominate long-term degradation.

---

## 12.13 Chemical Environment and Pressure Capability

Long-term hydrostatic classification is commonly generated using defined test media and controlled laboratory conditions. The process fluid may change material behaviour through:

- swelling;
- plasticization;
- extraction of additives;
- oxidation;
- environmental stress cracking;
- permeation;
- or accelerated crack growth.

Therefore, hydraulic pressure classification and chemical compatibility are separate checks that must be combined in the final design.

A compatibility table marked “resistant” does not automatically confirm retention of the full pressure rating. The engineer should determine whether the source addresses:

- concentration;
- temperature;
- exposure time;
- applied stress;
- purity and contaminants;
- and the exact material compound.

---

## 12.14 Static Rating Versus Cyclic and Transient Service

The standard long-term hydrostatic classification is primarily a sustained-pressure material framework. Real systems may also experience:

- pump starts and stops;
- control-valve cycling;
- rapid pressure fluctuations;
- surge and water hammer;
- daily depressurization and repressurization;
- vibration;
- thermal cycles;
- and combined mechanical loads.

A pipe can satisfy the static pressure calculation and still require a separate fatigue or transient assessment.

This does not mean that every pressure cycle is damaging to the same degree. Fatigue depends on stress range, mean stress, cycle count, temperature, material, geometry, defects, and environment. The important engineering point is that **PN and SDR do not replace a cyclic-service evaluation**.

---

## 12.15 Components, Fabrication and Local Geometry

The simple SDR pressure equation describes the cylindrical pipe wall. It does not fully characterize local stress at:

- tees;
- reducers;
- elbows;
- fabricated branches;
- flange adapters;
- valve connections;
- instrument nozzles;
- support points;
- anchors;
- and transitions to rigid equipment.

Standard injection-moulded fittings may be qualified as part of a product system, but fabricated components and non-standard geometry can require separate design verification.

Similarly, a valid pipe pressure class does not validate a poor fusion joint, misalignment, contamination, excessive restraint, or a notch introduced during installation.

---

## 12.16 Common Engineering Mistakes

### Mistake 1 — Treating PE100 as a pressure rating

PE100 is a material classification, not a 100-bar rating.

### Mistake 2 — Treating PE100+ as a higher strength class

PE100+ is a quality-association listing, not an MRS class above PE100.

### Mistake 3 — Selecting pipe from PN alone

PN must be linked to material, SDR, standard, temperature, fluid, and component system.

### Mistake 4 — Ignoring temperature derating

The reference PN does not automatically remain available at elevated temperature.

### Mistake 5 — Using the pipe rating as the system rating

Valves, fittings, joints, fabricated parts, and transitions may govern.

### Mistake 6 — Using a water-service design coefficient for another service

The coefficient and design method must come from the applicable standard.

### Mistake 7 — Assuming a 50-year classification guarantees a 50-year installation life

System life depends on actual pressure, temperature, environment, joints, loads, ageing, damage, and operation.

### Mistake 8 — Treating static pressure capability as fatigue qualification

Cyclic and transient service may require separate assessment.

### Mistake 9 — Applying the SDR equation to lined or multilayer construction without verification

Different structures may require different test or calculation methods.

---

## 12.17 Engineering Checklist

Before accepting a pressure rating, verify:

- [ ] The exact polymer family, grade, compound, and material classification are known.
- [ ] The applicable product and design standards are identified.
- [ ] The current MRS or equivalent material classification is verified.
- [ ] The required design coefficient is taken from the correct application standard.
- [ ] SDR is calculated from the correct nominal diameter and wall-thickness definitions.
- [ ] Reference temperature and design life are understood.
- [ ] Continuous, intermittent, and transient temperatures are assessed.
- [ ] Chemical compatibility is evaluated under pressure, temperature, concentration, and time.
- [ ] Cyclic pressure and surge conditions are considered separately.
- [ ] Fittings, valves, joints, flanges, instruments, and fabricated components are checked.
- [ ] External pressure, vacuum, buckling, and mechanical loads are assessed where applicable.
- [ ] Test pressure is determined from the correct test standard rather than directly from PN.
- [ ] All pressure terms used in the project are explicitly defined.

---

## If You Remember Only One Thing

> A thermoplastic pipe pressure rating is the final result of a chain of assumptions and classifications: long-term material strength, statistical confidence, design coefficient, geometry, temperature, time, service, and product-standard requirements. **PN is the label at the end of that chain—not a substitute for understanding it.**

---

## Chapter Summary

Thermoplastic pressure-pipe design is based on long-term hydrostatic behaviour rather than short-term material strength alone.

ISO 9080 provides the statistical framework used to predict long-term hydrostatic strength from pipe-test data. ISO 12162 establishes material classification and the calculation of design stress. MRS identifies a classified long-term material strength; the design coefficient reduces that value to a design stress; and SDR defines the relationship between outside diameter and wall thickness.

For conventional pressure-pipe geometry, these values can be related through:

\[
p = \frac{2MRS}{C(SDR-1)}
\]

when pressure and stress are expressed in MPa.

The resulting nominal pressure remains conditional. Temperature, service duration, chemistry, cyclic loading, surge, component ratings, joints, fabrication, external loads, and the governing standard can reduce or otherwise control the permissible operating pressure.

A reliable design therefore uses MRS, SDR, and PN as parts of a complete engineering assessment—not as isolated catalogue values.
