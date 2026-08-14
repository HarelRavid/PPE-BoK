---
chapter: 013
title_en: "Polyethylene (PE)"
part: "Materials"
status: rev-1.0-standards-validation
language: en
technical_level: intermediate
primary_domains:
  - materials
  - pressure-design
  - standards-navigation
  - failure-analysis
review:
  physics: pass
  standards: pending
  academic: pending
  equations: pass
  units: pass
  examples: pass
  editorial: pending
last_updated: 2026-08-09
pds_baseline: "1.0"
cdb: "docs/PDS/Chapter-Design-Briefs/CDB-013-Polyethylene.md"
---

# Chapter 13 — Polyethylene (PE)

## Chapter purpose

Polyethylene is one of the most widely used thermoplastic materials for pressure piping, but its apparent simplicity is deceptive. A pipe may be marked PE100, SDR 11 and PN16, yet none of those markings alone establishes that the system is suitable for a specific project.

The engineering task is broader. The engineer must connect the Design Basis to long-term material behaviour, material classification, pipe geometry, product qualification, temperature, service environment, installation conditions, joining, inspection and the governing standards framework.

This chapter is therefore written as both an explanation of polyethylene behaviour and a practical engineering reference. The target balance is approximately 60% engineering application and 40% engineering understanding, adjusted where necessary to explain a mechanism properly.

> **Chapter engineering question**  
> Given a defined Design Basis, how should an engineer determine whether a polyethylene pressure-piping system is appropriate, how should its classification and geometry be interpreted, and what additional checks are required before the system can be considered technically justified?

---

## What the engineer should be able to do after this chapter

After completing the chapter, the reader should be able to:

1. Distinguish polymer behaviour, material classification, product qualification and system design.
2. Explain why long-term behaviour governs PE pressure-piping engineering more strongly than short-term tensile strength.
3. Navigate the standards chain from long-term testing to classification, product requirements and application-specific design.
4. Interpret MRS, design stress, design coefficient, SDR and nominal pressure without confusing them.
5. Perform and independently check the core pressure-rating relationships used in this chapter.
6. Recognise when temperature, cycling, chemical exposure, installation damage, slow crack growth or other service conditions invalidate a simple nominal-pressure interpretation.
7. Identify the Design Basis information required before selecting a PE material class or SDR.
8. Document a technically justified material and geometry decision while identifying what still requires project-specific engineering.
9. Frame an initial failure investigation from observations and evidence without assuming that the visible fracture location identifies the root cause.

---

# Chapter standards map

The standards chain below is the working navigation framework for this chapter. Exact editions, clause numbers, numerical values and standards-derived interpretations are **not considered final until the dedicated Standards Validation review is completed against authoritative source documents**.

| Engineering question | Standards family | Engineering use in this chapter |
|---|---|---|
| How is long-term hydrostatic behaviour determined? | ISO 9080 | Long-term strength regression / extrapolation framework |
| How is thermoplastic pressure-piping material classified? | ISO 12162 | Material classification, designation and design-coefficient framework |
| What product requirements apply to PE water / pressure drainage systems? | ISO 4427 series | Product and application requirements where within scope |
| What product requirements apply to PE gaseous-fuel systems? | ISO 4437 series | Product and application requirements where within scope |
| How is resistance to internal pressure tested? | ISO 1167 series | Hydrostatic pressure testing framework where applicable |
| What butt-fusion procedure framework may apply? | ISO 21307 | Chapter-level joining context; detailed joining treatment belongs elsewhere |

The map is deliberately a navigation tool, not a substitute for the standards.

**Rule used throughout this chapter:** when the governing standard can be named, the text names it. The phrase “the applicable standard” is reserved for cases where applicability genuinely depends on service, geography, product family or project requirements.

---

# Required Design Basis inputs

A PE selection shall not begin with SDR or PN. It begins with the engineering problem.

Before material or geometry selection, the engineer should establish, as applicable:

- transported fluid or gas and concentration;
- normal, design and upset temperatures;
- operating and design pressures;
- pressure cycling and credible transients;
- intended design life;
- buried or above-ground installation;
- UV and external environmental exposure;
- installation method and credible installation damage;
- joining method;
- inspection and repair philosophy;
- regulatory and geographic context;
- applicable product and application standards.

**Engineering decision rule:** if these inputs are not sufficiently defined, selection of a PE class, SDR or nominal pressure is provisional rather than final.

## Engineering Quick Navigation

You do not need to read this chapter linearly every time you use it.

- **Screening PE as a candidate material:** Investigations **1–4** — behaviour, material characteristics, time dependence and crack-growth considerations.
- **Understanding PE100, MRS, design stress, SDR or pressure designation:** Investigations **5–8** — long-term evidence → classification → design stress → pipe geometry → pressure basis.
- **Selecting PE for an actual project:** Investigation **9** — Design Basis → standards path → material/product → pressure/temperature → service → installation/joining → engineering disposition.
- **Reviewing a PE failure or abnormal condition:** Investigation **10** — observation → hypotheses → evidence → mechanism → engineering response.
- **Checking a completed design:** `CL-013-001` — Chapter 13 Design Review Checklist.

> **Rule of use:** a pipe designation, SDR, PN or catalogue pressure value is an input to the engineering process—not the conclusion of it.

---

# Investigation 1 — Why Did Polyethylene Become a Major Pressure-Piping Material?

Polyethylene became a major pressure-piping material not because it maximises a single material property, but because it combines several engineering advantages in one system: corrosion resistance, low density, toughness, flexibility, fusion joining and long-term pressure capability.

That combination matters more than any one headline property.

A metallic piping system may provide high stiffness and high short-term strength, yet require corrosion allowance, coatings, cathodic protection or additional maintenance in aggressive environments. A more rigid thermoplastic may provide good corrosion resistance but respond differently to impact, ground movement or installation strain. PE occupies a different engineering space: it accepts relatively large deformation while maintaining useful long-term pressure performance when selected, manufactured, joined and operated within its qualified envelope.

This is the first principle of PE engineering:

> **PE is valuable because the complete piping system can tolerate combinations of pressure, deformation and environment that would be managed differently in many conventional materials.**

That statement does not mean PE is universally superior. Its lower stiffness, strong temperature dependence, time-dependent deformation and sensitivity to certain damage mechanisms create their own design obligations.

## 1.1 The useful comparison is system behaviour, not material reputation

A competent material-selection review should avoid questions such as “Is PE stronger than PVC?” or “Is PE100 better than PP?” Those questions are incomplete because the answer depends on the Design Basis.

A more useful engineering comparison asks:

- What loads must the system sustain?
- At what temperature and for how long?
- How will the line be installed and restrained?
- Is movement beneficial or harmful?
- What joining method is practical and inspectable?
- Which chemical and environmental exposures are credible?
- Which product standard governs the application?
- What failure modes are credible over the intended life?

PE may be the preferred solution where fusion joining, flexibility, buried installation, impact tolerance or corrosion resistance provide measurable lifecycle value. In another Design Basis, those same characteristics may be less important than stiffness, dimensional stability or high-temperature capability.

### Engineering screening table

| PE characteristic | Possible engineering benefit | Design obligation |
|---|---|---|
| Flexibility | Tolerance of settlement, routing variation and some imposed displacement | Evaluate movement, restraint, supports and thermal response |
| Fusion joining | Can create a continuous pressure boundary with few mechanical joint interfaces | Qualified procedure, equipment, operator competence and inspection remain necessary |
| Corrosion resistance | Avoids many metallic corrosion mechanisms and associated protection systems | Chemical and environmental compatibility must still be demonstrated |
| Low density | Easier handling, transport and installation in many projects | Installation method and damage control become important parts of the Design Basis |
| Toughness | Useful impact and deformation tolerance in many installation conditions | Does not eliminate notch, gouge or slow-crack-growth concerns |
| Long-term pressure capability | Suitable for pressure service within a qualified envelope | Must be tied to material classification, geometry, temperature and the governing product/application standard |

The table is a screening aid only. None of these characteristics establishes final suitability without the rest of the chapter's verification chain.

## 1.2 Why short-term strength is not the governing design story

A common mistake is to judge a pressure-piping material primarily by short-term tensile strength. That is not how PE pressure-piping performance is established.

A PE pipe under sustained internal pressure experiences stress over years or decades, often while temperature, environment, installation condition and cyclic pressure alter the rate at which damage mechanisms develop. Therefore, the pressure-design problem must be framed in terms of **time-dependent material behaviour**.

The engineering chain is approximately:

`Long-term hydrostatic test evidence → regression / extrapolation → material classification → design stress framework → pipe geometry → product/application requirements → project verification`

This chain is the central architecture of the chapter.

## 1.3 Engineering implications of PE flexibility

Flexibility is frequently presented as a simple advantage. It is more useful to treat it as an engineering property with both benefits and consequences.

Potential benefits include tolerance of ground settlement and alignment variation, reduced sensitivity to some imposed displacement loads, practical long-radius field routing and good impact response in many installation conditions.

Potential consequences include greater movement under thermal loading, lower bending stiffness, higher dependence on support/restraint philosophy in above-ground systems and greater sensitivity of system geometry to temperature and loading history.

> **PE flexibility changes the load path of the piping system and must therefore be incorporated into the Design Basis rather than treated as a descriptive material property.**

## 1.4 Engineering decision from Investigation 1

PE should enter the candidate-material set when its system-level characteristics create value for the defined Design Basis. Selection should not proceed to a final material class or SDR until long-term pressure behaviour, temperature, product standard, service environment, joining and installation constraints are evaluated.

### Practical check — before moving on

If the current material-selection discussion contains only the words **PE100**, **SDR** and **PN**, the engineering problem is still under-defined.

---

# Investigation 2 — Which Molecular and Morphological Features Control PE Engineering Behaviour?

The purpose of molecular discussion in an engineering handbook is not to teach polymer chemistry for its own sake. It is to explain why PE behaves the way it does in a pressure-piping system.

Polyethylene is a semicrystalline polymer. Its engineering behaviour results from the interaction between more ordered crystalline regions and less ordered amorphous regions, together with the molecular architecture that connects them.

This structure helps explain several observations that matter directly to engineers:

- PE can sustain significant strain without immediately fracturing;
- stiffness is much lower than that of metals and varies with temperature and time;
- sustained stress produces time-dependent deformation;
- crack resistance depends on more than short-term strength;
- molecular architecture and processing quality influence long-term pressure and slow-crack-growth performance.

## 2.1 Semicrystalline structure and the time dimension

In a short-duration test, the material response reflects one loading timescale. In a pressure pipe intended for decades of service, molecular rearrangement and damage accumulation occur over a vastly longer period.

This is why an engineer must resist the temptation to convert a short-term strength value directly into a long-term allowable stress.

> **The governing question is not “What stress causes immediate yielding?” but “What sustained stress can the qualified material withstand for the intended service duration and temperature, within the applicable standards framework?”**

## 2.2 Creep is not automatically failure

Under sustained stress, PE continues to deform with time. This time-dependent deformation is commonly described as creep.

Creep should not be treated as synonymous with failure. Some time-dependent deformation is an expected material behaviour and may be compatible with successful service. The engineering task is to determine whether the resulting deformation, stress redistribution and damage evolution remain inside the qualified design envelope.

## 2.3 Crack behaviour requires a separate engineering lens

A component may have adequate nominal wall thickness and still contain a local stress concentration caused by a notch, scratch, installation damage, joint geometry or other discontinuity.

PE pressure-piping engineering must consider both:

1. **global pressure loading**, and
2. **local resistance to crack initiation and growth**.

This is the conceptual bridge to slow crack growth, addressed later in the chapter.

## 2.4 Processing quality belongs in the engineering chain

Material designation alone does not prove that every manufactured component possesses identical engineering quality. Processing history can influence morphology, residual stress, dimensions and local defects.

Engineering qualification must distinguish between:

- material classification;
- product conformity;
- joining quality;
- installed-system condition.

## 2.5 Engineering decision from Investigation 2

The molecular and semicrystalline structure of PE explains why time, temperature, deformation and crack resistance must be treated as primary design variables. Short-term mechanical properties alone are insufficient to establish pressure-piping suitability.

**FIG-013-001 — Semicrystalline PE structure → engineering consequence [PLACEHOLDER]**  
Show crystalline and amorphous regions conceptually, then connect them to stiffness, creep, ductility and crack resistance. Original engineering illustration; not decorative.

---

# Investigation 3 — What Do PE80, PE100 and Related Material Designations Actually Tell the Engineer?

Material designations are useful because they compress a large amount of qualification information into a short identifier. They become dangerous when the identifier is interpreted as a complete design decision.

> **What engineering property does the designation represent, under which qualification framework, and what does it not establish?**

PE pressure-piping classifications are tied to long-term hydrostatic strength concepts rather than to a simple ranking of short-term tensile strength.

## 3.1 Material class is one input to the design problem

For engineering purposes, the chain should be kept explicit:

`Material evidence → material classification → design coefficient / design stress → geometry → product standard → service verification`

### TAB-013-001 — PE classification and terminology as engineering inputs

| Term / designation | What it represents | What it gives the engineer | What it does **not** prove | Primary standards path |
|---|---|---|---|---|
| PE material class | Long-term pressure-piping material classification | Input to the design-stress / pressure relationship | Project suitability, product conformity, temperature suitability or joining quality | ISO 12162 |
| PE100 | Material-classification designation within the pressure-piping framework | Long-term material-strength class input | Universal approval for any fluid, temperature, installation or application | ISO 12162 + governing product/application standard |
| SDR | Nominal outside-diameter to nominal wall-thickness ratio | Geometry input to the pressure relationship | Material quality, product conformity or service suitability | Governing product standard |
| PN / pressure designation | Product/system pressure designation under defined reference conditions | Quick pressure-class reference within a defined standards framework | Suitability when temperature, application or other Design Basis conditions change | Governing product/application standard |
| SCG resistance property | Resistance to slow crack growth established through a defined test/qualification route | Evidence relevant to a specific long-term damage mechanism | Immunity to arbitrary installation damage or to all failure mechanisms | Governing qualification/test standard |

**Standards Validation Hold Point:** the exact definitions, classification boundaries, reference conditions and standards relationships in TAB-013-001 shall be rechecked against the authoritative editions before publication.

## 3.2 PE100 is not a universal certificate of suitability

A pipe marked PE100 may still be unsuitable for a project if the temperature-adjusted pressure capability is inadequate, the application lies outside the governing product-standard scope, chemical exposure is not acceptable, cyclic/transient loading requires additional assessment, installation damage creates additional risk, or the joining/inspection strategy is not appropriate.

> **PE100 is a material-classification input. It is not a project approval.**

## 3.3 PE100-RC and enhanced SCG-resistance terminology require a defined qualification route

Terms associated with enhanced resistance to slow crack growth are widely used in industry, but a commercial or market designation should not be treated as a self-contained engineering property.

> **Enhanced SCG-resistance terminology must be tied to a defined qualification route, not inferred from a commercial label alone.**

Where a designation such as PE100-RC is used, the engineer should identify the governing product/application specification, required SCG qualification method, applicable acceptance criteria, scope covered by the qualification and whether the designation changes any design-stress/pressure-rating basis or only adds qualification evidence against a particular damage mechanism.

Different standardized methods can address SCG resistance through different test concepts. For example, ISO 13479 uses a notched-pipe hydrostatic test framework, while ISO 18488 uses strain-hardening modulus as an assessment route. These methods should not be treated as interchangeable evidence unless the governing specification explicitly establishes that relationship.

**Standards Validation Hold Point:** confirm whether the governing project/product standard recognises the designation explicitly, which SCG qualification route it requires, the applicable acceptance criteria, and whether the designation changes any design-stress or pressure-rating basis.

## 3.4 Engineering decision from Investigation 3

Use the PE material designation to establish the material-classification branch of the design process. Do not use it to bypass product qualification, geometry selection, service-condition verification or project-specific engineering checks.

---

# Investigation 4 — Why Does Long-Term Behaviour Govern PE Pressure Design?

A pressure pipe experiences a history of stress, temperature, environment, installation condition and operating events. For polyethylene, that history is not a secondary correction to the design problem; it is part of the design problem itself.

The engineer therefore needs two distinct questions in mind:

1. **Can the pipe resist the present load?**
2. **Can the qualified material and product continue to resist the relevant load history for the required life?**

PE pressure design is governed primarily by the second.

## 4.1 Sustained stress changes the response with time

Under a sustained load, PE exhibits creep: strain continues to develop even when the applied stress is approximately constant. Stress may also redistribute locally as the polymer deforms.

For a pressure pipe, a simple thin-wall representation is useful for intuition:

\[
\sigma_\theta \approx \frac{pD_m}{2e}
\]

**EQ-013-001 — Thin-wall hoop-stress approximation**

where \(\sigma_\theta\) is circumferential/hoop stress, \(p\) is internal pressure, \(D_m\) is a representative mean diameter and \(e\) is wall thickness.

**Units:** use a consistent unit system. If \(p\) is in MPa and \(D_m\) and \(e\) are in mm, the resulting nominal stress is in MPa.

**Derivation basis:** circumferential force equilibrium for a thin-walled cylindrical pressure boundary.

**Assumptions:** membrane-dominated behaviour, approximately uniform wall thickness, representative cylindrical geometry and a wall sufficiently thin relative to diameter for the thin-wall approximation to be reasonable.

**Engineering use:** expose the mechanical dependence of nominal hoop stress on pressure, diameter and wall thickness.

**Applicability limit:** this is not the standards-based PE pressure-rating relationship used later in the chapter.

**Common misuse:** using the nominal hoop-stress result as proof of long-term life or system suitability.

## 4.2 Creep, rupture and crack growth are different engineering questions

- **creep deformation** — time-dependent strain under sustained stress;
- **long-term rupture** — loss of pressure-boundary integrity after a period under load;
- **slow crack growth (SCG)** — progressive crack extension from a local stress concentration over time.

They are related through time-dependent polymer behaviour, but they are not interchangeable. A pipe may creep without failing, or remain dimensionally acceptable while a local crack grows from a notch.

## 4.3 Long-term failure behaviour is not represented by one mechanism

At comparatively high stress or severe conditions, deformation and rupture may be dominated by ductile behaviour. At lower stress and longer times, local crack processes can become increasingly important. Temperature strongly affects the rate at which these mechanisms develop.

> **A lower nominal stress does not make time irrelevant. It changes which time-dependent mechanism may govern.**

## 4.4 Nominal stress is not local crack-driving stress

Potential local stress raisers include scratches, gouges, notches, sharp geometric transitions, local wall-thickness reduction, manufacturing defects, joint discontinuities, embedded damage and installation-induced deformation.

A statement such as “the line pressure was below nominal rating” does not eliminate the possibility of a locally driven long-term crack mechanism.

## 4.5 Slow crack growth is a system concern, not only a resin property

The engineering risk is created by the combination:

`material resistance × local defect severity × stress history × temperature × environment × time`

At the material-selection stage, credible notches, installation damage, temperature and service history must therefore be considered alongside the material's qualified crack-growth resistance. Detailed field-failure interpretation is deferred to Investigation 10.

### SCG qualification navigation

`Credible local defect / notch risk → identify required SCG resistance evidence → identify governing product/application standard → identify referenced SCG test method → verify product/material qualification → separately assess installation damage and system loading`

A successful SCG-resistance test demonstrates performance under the defined test method and acceptance framework. It does **not** prove that an installed system is insensitive to arbitrary gouges, poor joints, excessive local strain or service conditions outside the qualified envelope.

**Standards Validation Hold Point:** confirm the test method and acceptance route required by the governing product/application standard; do not infer equivalence between different SCG test methods without an authoritative basis.

## 4.6 Why time-to-failure data matter

If a material is intended for decades of pressure service, the engineer needs evidence that connects applied stress and temperature to time-dependent performance. A single burst pressure does not provide that relationship.

## 4.7 Engineering use: a long-term behaviour screening check

| Design Basis question | Why it matters | Engineering response |
|---|---|---|
| Is temperature above the reference condition used for nominal classification? | Time-dependent processes accelerate with temperature | Apply governing temperature treatment and re-check pressure capability |
| Are significant pressure cycles or transients credible? | Repeated loading adds a damage mechanism not represented by steady nominal pressure alone | Perform cyclic/transient assessment as required |
| Is installation damage credible? | Local notches can control crack initiation even when nominal stress is acceptable | Define damage acceptance, inspection and repair criteria |
| Is the fluid/environment known to affect PE behaviour? | Environment can influence deformation, cracking or chemical resistance | Perform compatibility and application-specific verification |
| Is the line buried, restrained or subject to imposed displacement? | Secondary loads can alter the local stress state | Evaluate system loads, not internal pressure alone |
| Is the intended life unusually long or uncertain? | Long-term classification is meaningful only within its defined framework | Confirm qualification basis and project life assumptions |

## 4.8 Engineering decision from Investigation 4

A PE pressure design is incomplete if it checks only present-day nominal stress or nominal pressure rating. The engineer must establish that the selected material, geometry and product standard provide an appropriate long-term basis for the actual temperature, loading history, installation condition and credible local damage mechanisms.

`Nominal pressure load → long-term material evidence → local damage considerations → service modifiers → project verification`

not:

`PN marking → acceptance`

**FIG-013-002 — Slow crack growth concept [PLACEHOLDER]**  
Show nominal pipe-wall stress, a local notch, crack initiation and progressive crack extension over time; explicitly separate nominal stress from local crack-driving condition.

---

# Investigation 5 — How Can Decades of Performance Be Evaluated Before Decades Have Passed?

A polyethylene pressure pipe intended for decades of service cannot be qualified by waiting for the full design life of every new material. The engineering solution is to generate a structured body of stress-rupture data and analyse it within a controlled extrapolation framework.

`pipe-form specimens → controlled internal pressure → controlled temperature → observed failure time → regression / extrapolation → long-term hydrostatic strength`

Each specimen contributes a combination of stress, temperature and time-to-failure. Taken together, these observations describe how pressure-carrying capability changes as time increases.

## 5.1 Why the material is tested in pipe form

The objective is to establish long-term pressure behaviour representative of the material as processed into pipe, not to measure an abstract polymer property in isolation.

`material in pipe form ≠ complete piping system`

Joining quality, fittings, installation damage, chemical exposure and project loading still require separate verification.

## 5.2 Why more than one pressure level is required

A single pressure test gives one point. Long-term classification requires a population of observations distributed across pressure/stress levels and time.

> **A long-term curve can only be credible if the data show how failure time changes as stress changes.**

**Standards Validation Hold Point:** exact current-edition requirements for specimen count, pressure levels, duration and temperature spacing shall be verified against the current authoritative ISO 9080 edition before publication.

## 5.3 Temperature is an acceleration variable — but not a free shortcut

Elevated-temperature testing can reveal long-term behaviour sooner, but the data are not simply converted into arbitrary service life. The extrapolation framework constrains temperatures, combination of datasets, failure branches and permitted extrapolation range.

> **Engineering rule:** accelerated testing extends the evidence base only inside a validated extrapolation methodology.

## 5.4 Failure mechanism matters

A change in slope — a **knee** — may indicate transition between different failure behaviours. A regression curve is useful only when the underlying failure behaviour represented by that curve remains physically meaningful.

Detailed field-failure interpretation remains deferred to Investigation 10.

## 5.5 What Investigation 5 gives the engineer

| Engineering question | Why it matters |
|---|---|
| Was the material evaluated in pipe form? | Confirms relevance of the hydrostatic evidence |
| Are multiple stress levels represented? | Establishes stress–life behaviour rather than a single test point |
| Were appropriate temperatures included? | Supports validated time/temperature extrapolation |
| Was a change of failure mechanism assessed? | Prevents inappropriate use of one regression branch |
| Is the required service point inside the permitted extrapolation range? | Prevents unsupported life claims |
| Is the reported value a mean prediction or a conservative lower bound? | Critical for classification and design |

**Engineering decision:** do not treat a long-term strength value as credible merely because it appears on a datasheet. Identify the test and extrapolation framework from which it was derived.

---

# Investigation 6 — What Does Regression Analysis Mean to the Practicing Engineer?

The practicing engineer normally does not need to reproduce the full statistical regression procedure. The engineer **does** need to understand what the regression output means — and what it does not mean.

## 6.1 The regression line is not the design value

A fitted regression represents the central predicted behaviour of the data, but engineering classification does not simply take that mean prediction as the allowable design value.

`observations → fitted behaviour → lower statistical bound → classification input`

## 6.2 Why a lower bound is necessary

Real materials and real tests exhibit scatter. The lower statistical bound provides a deliberately conservative statistical basis for classification.

It should **not** be interpreted as a universal “97.5% probability that every pipe survives”. It is a statistical property of the regression framework and must be interpreted within the assumptions and definitions of the applicable standard.

**Standards Validation Hold Point:** final terminology — including lower prediction limit, lower confidence limit and the exact current-edition statistical definition — shall be verified against current ISO 9080 and ISO 12162 editions before publication.

## 6.3 FIG-013-003 — Long-term hydrostatic regression concept

The original engineering figure shall distinguish individual failure observations, predicted mean long-term behaviour, lower prediction/confidence boundary and, where relevant, a knee separating two failure branches.

## 6.4 Regression is evidence, not a guarantee

The regression result does not by itself establish chemical compatibility, joint quality, resistance to installation damage, system loads, suitability outside the tested/extrapolated range or compliance with a particular product/application standard.

## 6.5 Bridge to MRS

The output of the regression/extrapolation process provides a conservative long-term strength basis. The classification standard then converts that continuous statistical result into a standardized material class.

`test data → regression → lower statistical bound → MRS → design coefficient → design stress → SDR → pressure capability`

**Standards Validation Hold Point:** exact current-edition rounding series, notation, reference conditions and classification rules shall be verified against current authoritative ISO 12162 before publication.

**FIG-013-006 — Test data → regression → classification → product marking chain [PLACEHOLDER]**  
Show the distinction between evidence generation, statistical interpretation, material classification and the information ultimately presented on a product marking. The figure shall make clear that each arrow is governed by a defined standards interface and that marking does not recreate the upstream evidence.

---

# Investigation 7 — How Does Long-Term Evidence Become MRS and Design Stress?

Investigations 5 and 6 established how long-term hydrostatic test evidence is converted into a conservative statistical strength basis. That result is not yet the stress used for pipe pressure design.

`long-term regression result → lower statistical bound → MRS → design coefficient C → design stress`

## 7.1 The lower statistical bound is not yet MRS

> **The regression result is a continuous strength estimate. MRS is a standardized classification value derived from it.**

**Standards Validation Hold Point:** current terminology for the lower statistical value, applicable reference condition and relationship to MRS shall be checked against authoritative current ISO 12162 before publication.

## 7.2 MRS is a standardized material-classification value

Conceptually:

\[
\sigma_{LCL} \rightarrow \text{standardized downward classification} \rightarrow MRS
\]

The important design consequence is that MRS is a **classification value**, not the exact regression result and not yet the project design stress.

> **PE100 identifies a material-classification branch. It does not mean that 10 MPa may be used directly as project allowable stress.**

## 7.3 The design coefficient is a separate engineering input

`MRS = material-classification input`

`C = governing product / application / service design input`

The engineer should not select \(C\) from memory or from an unrelated project. Its source, scope and applicability must be traceable to the governing standards path and Design Basis.

## 7.4 From MRS to design stress

\[
\sigma_s = \frac{MRS}{C}
\]

**EQ-013-002 — Design stress from MRS and design coefficient**

where \(\sigma_s\) is design stress, \(MRS\) is minimum required strength and \(C\) is the applicable design coefficient.

**Units:** if MRS is expressed in MPa, \(\sigma_s\) is in MPa because \(C\) is dimensionless.

**Standards basis:** standards-based classification-to-design relationship; final normative wording, definition of \(C\), reference conditions and rounding requirements remain subject to Standards Validation.

**Engineering use:** convert material classification into the design-stress basis required for the subsequent geometry/pressure relationship.

**Applicability limit:** the equation does not by itself establish the applicable \(C\), temperature/service-life capability, chemical compatibility, transient/fatigue suitability, fitting/joint capability, product conformity or final allowable operating pressure.

**Common misuse:** implicitly removing the design-coefficient step by treating \(MRS\) as design stress.

## 7.5 Worked interpretation — why PE100 does not mean 10 MPa design stress

For illustration only:

\[
MRS=10\text{ MPa}, \qquad C=1.25
\]

then, before any standards-prescribed rounding:

\[
\sigma_s=\frac{10}{1.25}=8.0\text{ MPa}
\]

The example demonstrates only `MRS → C → design stress`. It does not establish that \(C=1.25\) is universally applicable.

## 7.6 Why C should never be copied blindly

`identify material class → identify governing product/application standard → identify applicable C → calculate design stress → apply geometry/pressure relationship`

not:

`PE100 → assume familiar C → calculate pressure`

## 7.7 Engineering decision from Investigation 7

| Quantity | Engineering meaning |
|---|---|
| Lower statistical strength bound | Conservative output from long-term regression/extrapolation |
| MRS | Standardized material-classification value |
| \(C\) | Applicable design coefficient from the governing standards/design framework |
| \(\sigma_s\) | Design-stress basis used in subsequent geometry/pressure calculation |

> **Material classification establishes capability evidence. Design stress is established only after the applicable design coefficient is applied.**

---

# Investigation 8 — How Do MRS, Design Stress, SDR and Product Identification Become a Pressure Basis?

Investigations 5–7 established the material side of the chain:

\[
\text{long-term evidence}\rightarrow MRS\rightarrow C\rightarrow\sigma_s
\]

The next step introduces geometry and product identification.

## 8.1 SDR converts pipe dimensions into a useful geometry parameter

\[
SDR=\frac{d_n}{e_n}
\]

**EQ-013-003 — Standard Dimension Ratio**

where \(SDR\) is dimensionless, \(d_n\) is nominal outside diameter and \(e_n\) is nominal wall thickness.

**Units:** \(d_n\) and \(e_n\) shall use the same length unit; SDR is dimensionless.

**Source basis:** nominal geometry relationship used by thermoplastics product standards; exact current definition, dimensional terminology and rounding/series conventions remain subject to Standards Validation.

**Assumptions:** \(d_n\) and \(e_n\) are the nominal dimensions defined by the governing product standard for the selected pipe series. The relationship does not represent measured minimum residual wall at a damaged location.

**Engineering use:** express pipe wall geometry in a normalized form that can be connected to the pressure relationship.

**Applicability limit:** SDR alone does not establish material quality, product conformity, temperature capability, damage tolerance, fitting/joint capability or project suitability.

**Common misuse:** comparing SDR values across different materials or services as if SDR alone were a pressure rating.

> **For the same nominal diameter, lower SDR means a thicker nominal wall.**

## 8.2 Connecting design stress to pressure

The supporting project literature used during redevelopment presents the relationship in an MRS-based form labelled `MOP`:

\[
MOP=\frac{20\,MRS}{C(SDR-1)}
\]

when pressure is in bar and MRS in MPa. Within this chapter, the arithmetic result is treated as a **reference pressure basis** until the governing product/application standard, temperature/time treatment and full project Design Basis have been verified.

From Investigation 7:

\[
\sigma_s=\frac{MRS}{C}
\]

so the corresponding stress/geometry form is:

\[
p=\frac{2\sigma_s}{SDR-1}
\]

**EQ-013-004 — SDR pressure relationship**

where \(p\) is the calculated reference pressure basis, \(\sigma_s\) is design stress and SDR is the standard dimension ratio.

**Units:** if \(\sigma_s\) is in MPa, \(p\) is returned in MPa. Since \(1\text{ MPa}=10\text{ bar}\):

\[
p_{bar}=\frac{20\sigma_s}{SDR-1}
\]

**Source basis:** carried from the approved redevelopment basis and supporting project literature; the exact normative pressure-design form, terminology, coefficient path, dimensional definitions and rounding conventions require final Standards Validation against the governing current product/application standard.

**Assumptions:** the selected material classification, design coefficient and nominal SDR are valid within the same governing standards path; pressure and stress units are consistent; and the nominal geometry relationship is applicable to the product under review.

**Engineering use:** connect the validated design-stress basis to nominal pipe geometry to obtain a reference pressure basis for subsequent service verification.

**Applicability limit:** the relationship does not by itself establish allowable project operating pressure, elevated-temperature capability, chemical compatibility, transient/cyclic suitability, component/joint capability, installation acceptability or regulatory compliance.

**Common misuse:** treating the calculated result—or an `MOP`/PN label from another standards context—as unconditional project allowable pressure.

> **Calculated reference pressure basis ≠ automatically allowable operating pressure.**

### TAB-013-005 — MRS / Design Coefficient / Design Stress / SDR / Pressure Reference Chain

| Step | Quantity / input | Relationship or engineering action | Units | What it establishes | What it does **not** establish |
|---|---|---|---|---|---|
| 1 | Long-term evidence | Evaluate qualified long-term hydrostatic test evidence through the applicable regression/classification pathway | — | Evidence basis for material classification | Project suitability or allowable operating pressure |
| 2 | MRS | Use the standardized material-classification value established by the governing classification framework | MPa | Material-classification strength input | Design stress or system pressure by itself |
| 3 | Design coefficient, `C` | Identify the coefficient applicable to the governing product/application/design framework | dimensionless | Required reduction from classification strength to design-stress basis | Universal coefficient for every PE application |
| 4 | Design stress, `σ_s` | `σ_s = MRS / C` (`EQ-013-002`) | MPa when MRS is MPa | Stress basis for subsequent geometry/pressure relationship | Temperature-adjusted or project-final allowable pressure |
| 5 | SDR | `SDR = d_n / e_n` (`EQ-013-003`) | dimensionless | Nominal pipe geometry relationship | Material quality, product conformity or service suitability |
| 6 | Reference pressure basis | `p = 2σ_s / (SDR - 1)` (`EQ-013-004`) when pressure and stress use consistent units | same pressure/stress units; convert explicitly where required | Reference pressure basis for selected material/design-stress/geometry chain | Automatic project allowable operating pressure |
| 7 | Service verification | Apply governing temperature/time, fluid/environment, component/joint, transient, installation and application requirements | project-specific | Basis for project engineering disposition | Immunity from future Design Basis changes or failure |
| 8 | Final disposition | Record `GO / CONDITIONAL GO / NO-GO` with assumptions and open items | — | Auditable engineering decision | Replacement for specialist analyses required by the Design Basis |

**Use rule:** this is a navigation/reference asset. Exact normative definitions, coefficient values, reference conditions, rounding rules and pressure-design conventions remain subject to final Standards Validation.

## 8.3 Worked Example A — From PE100 to a reference pressure basis

For illustration only:

\[
MRS=10\text{ MPa}, \qquad C=1.25, \qquad SDR=11
\]

\[
\sigma_s=8.0\text{ MPa}
\]

\[
p=\frac{2(8)}{11-1}=1.6\text{ MPa}=16\text{ bar}
\]

**Standards path for the example:** long-term hydrostatic evidence / ISO 9080 framework → material classification / ISO 12162 framework → governing PE product/application standard for the service → applicable design coefficient and dimensional series → service-specific temperature/time and system verification. The example deliberately stops at the reference pressure basis because the final governing product/application standard and service-specific conditions are not being asserted universally here.

This demonstrates:

`MRS → C → design stress → SDR → reference pressure basis`

It does **not** establish that the coefficient applies universally, that 16 bar is suitable at elevated temperature or for a particular service, that fluid compatibility is acceptable, or that fittings/joints/system conditions are covered.

**Independent verification:** arithmetic, algebraic equivalence and unit conversion have been independently re-performed. Two calculation paths return \(\sigma_s=8.0\text{ MPa}\) and \(p_{reference}=1.6\text{ MPa}=16\text{ bar}\). This verification does not validate standards applicability.

**Standards Validation Hold Point:** revalidate PE100↔MRS basis, coefficient value, current pressure relationship, dimensional definitions and prescribed rounding rules.

## 8.4 Sensitivity — what changes the calculated pressure basis?

| Change | Direct effect on calculated pressure basis | Engineering implication |
|---|---|---|
| \(C\uparrow\) | pressure ↓ | More conservative or different application-specific basis |
| \(C\downarrow\) | pressure ↑ | Requires explicit governing-standards justification |
| SDR ↑ | pressure ↓ | Thinner nominal wall relative to diameter |
| SDR ↓ | pressure ↑ | Thicker nominal wall relative to diameter |
| MRS ↑ | pressure ↑ | Higher material-classification input |

## 8.5 Geometry sensitivity example

For comparison only, with \(MRS=10\text{ MPa}\) and \(C=1.25\):

- SDR 11 → 16 bar reference basis;
- SDR 9 → 20 bar reference basis.

The SDR 9 result has also been independently recalculated as \(2.0\text{ MPa}=20\text{ bar}\).

> **Changing SDR changes the reference pressure basis even when the material designation remains unchanged.**

## 8.6 Temperature and service conditions prevent the first calculation from becoming the final answer

`reference pressure basis → governing product/application standard → temperature/time treatment → fluid/environment compatibility → fittings, joints and components → transients and other Design Basis loads → project allowable operating pressure`

The exact temperature/time treatment shall not be universalized without authoritative standards basis.

## 8.7 The pipe is not the system

A straight-pipe calculation cannot establish the capability of the assembled piping system. Fittings, valves, fusion joints, fabricated components, branches/local geometry, installation damage, temperature, chemical environment, transient pressure, imposed displacement, supports/restraint and application-specific qualification requirements require separate confirmation.

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

## 8.9 Pipe marking is an identification package—not a Design Basis

### TAB-013-002 — What pipe marking may tell the engineer

| Marking / information type | What it may tell the engineer | What it does **not** establish by itself |
|---|---|---|
| Manufacturer / traceability identification | Who produced the product and how it may be traced | Installed quality or project suitability |
| Material designation, e.g. PE100 | Material-classification branch | Allowable project pressure or chemical suitability |
| SDR / dimensional series | Nominal geometry relationship | Temperature-adjusted capability or system rating |
| Nominal pressure / pressure designation where used | Standardized pressure-class information under defined reference conditions | Unconditional allowable operating pressure |
| Product-standard reference | Product conformity framework being claimed | Applicability of that standard to actual project service |
| Production / batch identification | Manufacturing traceability | Absence of damage after transport or installation |
| Size / dimensions | Nominal product geometry | As-installed minimum wall at a damaged location |

> **The pipe marking tells the engineer what product is being presented. It does not tell the engineer whether the complete installed system satisfies the project Design Basis.**

`read marking → identify product standard → verify material class → verify SDR/dimensions → confirm service/application scope → apply temperature/service conditions → verify fittings/joints/system → accept or reject`

**FIG-013-007 — PE pipe marking anatomy [PLACEHOLDER]**  
Show a generic pipe-marking string broken into manufacturer/traceability, material designation, nominal dimensions/SDR, pressure designation where applicable, product-standard reference and production/batch information. The figure shall visually separate identification/traceability fields from engineering conclusions that still require verification.

## 8.10 Practical engineering check

The engineer should be able to identify the material class, MRS basis, source of \(C\), SDR/dimensional definitions, pressure relationship, unit conversions, temperature/time basis, governing product/application standard, meaning of the marking, component/joint coverage and service-specific loads/environmental effects.

## 8.11 Engineering decision from Investigation 8

> **Calculate a reference pressure basis first; then prove that the actual project Design Basis remains inside the qualified service envelope.**

---

# Investigation 9 — How Should an Engineer Select PE for a Real Design Basis?

A PE design decision should not begin with a catalogue pressure rating. It should begin with a defined Design Basis and end with a documented engineering disposition.

`Design Basis → Applicable standards → Qualified material → Product conformity → Long-term/design-stress basis → Geometry/SDR → Reference pressure basis → Temperature/service verification → Chemical/mechanical/service checks → Joining/installation constraints → Verification → Engineering decision`

## 9.1 Freeze the Design Basis before selecting the pipe

Establish fluid/concentration, normal/design/upset temperature, operating/design pressure, credible transients, intended service life, installation condition, UV/external environment, joining method, damage risk, inspection/repair strategy, regulatory/geographic context and governing product/application standard.

If these are not sufficiently defined, selection is **provisional**.

> **PE100 SDR 11 is not a Design Basis. It is an output candidate.**

## 9.2 Determine the standards path before applying coefficients

Identify material-classification framework, product standard, application/service standard, joining/qualification standards and project/regulatory requirements before applying coefficients, pressure designations or temperature rules.

## 9.3 Separate material qualification from product qualification

A qualified resin does not automatically qualify the extrusion process, finished pipe, fitting, joint or installed system.

## 9.4 Establish the reference pressure basis

\[
MRS \rightarrow C \rightarrow \sigma_s \rightarrow SDR \rightarrow p_{reference}
\]

Label the result:

> **Reference pressure basis — service verification pending**

rather than simply “Allowable Pressure”.

## 9.5 Reopen temperature and service duration

> **What does the governing standards path require for this temperature and service-duration combination?**

The answer may involve a factor, table, different allowable-stress basis or another standards-specific treatment.

**Standards Validation Hold Point:** all numerical temperature factors and service-life treatments shall be verified against the current authoritative standard actually governing the application.

## 9.6 Verify chemical and environmental compatibility

Evaluate:

`fluid identity + concentration + temperature + exposure time + stress state`

and confirm the evidence is transferable to actual project conditions.

## 9.7 Treat cycling and transients as additional loads

> **If credible transient or cyclic loads materially alter the nominal pressure history, the nominal SDR/pressure calculation is not the complete mechanical assessment.**

## 9.8 Installation condition can invalidate an otherwise correct material selection

PE flexibility changes how loads are carried and therefore changes which installation checks govern. Consider burial, above-ground support, restraint, casing, bore/pull installation, settlement, soil movement, traffic and other imposed conditions.

## 9.9 Joining is a qualification interface, not a footnote

Identify joining method, procedure qualification, equipment requirements, operator competence, inspection requirements, repair philosophy, fitting/joint pressure compatibility and environmental controls where relevant.

## 9.10 TAB-013-003 — PE Design Input / Verification Matrix

| Design input | Required question | Evidence / source | Status |
|---|---|---|---|
| Fluid/service | What is transported and at what concentration? | Process Design Basis | Open / Verified |
| Temperature | Normal, design and upset temperatures? | Process / thermal basis | Open / Verified |
| Pressure | Operating, design and transient pressure? | Hydraulic / process basis | Open / Verified |
| Service life | What duration must be justified? | Project basis | Open / Verified |
| Material class | Is the required long-term classification demonstrated? | Material qualification | Open / Verified |
| Product standard | Does the selected product fall within governing scope? | Product certification | Open / Verified |
| SDR / dimensions | Does geometry satisfy the reference pressure basis? | Calculation + product data | Open / Verified |
| Chemical compatibility | Is compatibility transferable to actual service? | Validated compatibility evidence | Open / Verified |
| Installation | What mechanical/damage conditions are credible? | Installation specification | Open / Verified |
| Joining | Is the joining route qualified and inspectable? | Joining specification | Open / Verified |
| Transients / cycles | Are additional mechanical checks required? | Design analysis | Open / Verified |
| Final disposition | Are all remaining assumptions controlled? | Engineering review | GO / CONDITIONAL GO / NO-GO |

## 9.11 Worked Example B — The pipe did not change, but the Design Basis did

Assume a qualified PE100 product, selected SDR and acceptable reference pressure calculation. Then operating temperature increases materially.

The pipe marking, material designation, SDR and geometry are unchanged. The previous engineering decision must still be reopened.

`original reference pressure basis → temperature change → reopen governing standard → re-evaluate temperature/service-life pressure basis → recheck chemical compatibility → reconfirm fitting/joint/component limits → review affected transients/installation assumptions → issue new engineering disposition`

> **A Design Basis change can invalidate the previous engineering decision even when nothing printed on the pipe changes.**

The example is complete only when the final disposition is explicit: **GO**, **CONDITIONAL GO**, or **NO-GO**.

**Equivalent independent verification:** because this example is intentionally qualitative and contains no standards-derived numerical temperature factor, its independent verification is a decision-path re-performance rather than arithmetic recalculation. The changed temperature has been propagated independently through standards applicability, service-life/pressure basis, compatibility, components/joints, affected mechanical assumptions and final disposition, reaching the same conclusion. This equivalent verification satisfies the current example objective without fabricating unsupported numerical data. If a numerical temperature treatment is added after Standards Validation, that numerical addition requires separate independent recalculation before Design Freeze.

## 9.12 Make the final design decision explicit

Record material/product, geometry, standards basis, independently checked reference pressure basis, temperature/service-life verification, chemical compatibility, transient/cyclic assessment, installation constraints, joining/inspection requirements, residual open items and final disposition.

## 9.13 Engineering decision from Investigation 9

> **Nominal classification is an input to engineering judgement, not a substitute for it.**

---

# Investigation 10 — What Can Failure Evidence Tell the Engineer?

Failure evidence is useful only when observation is kept separate from interpretation. A split pipe, leaking fusion joint, gouge, deformation or brittle-looking fracture surface is an **observation**. It is not, by itself, proof of the governing failure mechanism.

\[
\boxed{Observation\rightarrow Plausible\ mechanisms\rightarrow Evidence\rightarrow Discrimination\rightarrow Engineering\ response}
\]

## 10.1 Start with facts, not the preferred explanation

Record exact failure location, identification/traceability, dimensions/SDR, photographs before destructive examination, fracture orientation, deformation, damage, joint proximity, pressure/temperature/transient history, installation history, environment, age/service duration and prior repairs.

> **Preserve evidence before explaining evidence.**

## 10.2 Build more than one plausible mechanism

Potential hypotheses include short-term ductile overload, long-term pressure/creep-related rupture, SCG from a local stress concentrator, installation damage, joining/fusion deficiency, fitting/fabricated-component issue, chemical/environmental interaction, temperature/service excursion, external loading or interactions between several mechanisms.

## TAB-013-004 — Failure Evidence / Engineering Response Matrix

| Observation / condition | Plausible mechanism to investigate | Evidence that may discriminate | Engineering response if supported | Boundary of inference |
|---|---|---|---|---|
| Large deformation near rupture | Short-term overload / ductile failure | Pressure history, dimensions, temperature, deformation pattern, material verification | Recheck actual load against system capability and transient basis | Deformation alone does not identify the initiating event |
| Failure after long service without obvious gross overload | Long-term time-dependent rupture | Service history, stress basis, temperature history, material/product qualification | Reopen long-term Design Basis and service envelope | Age alone does not prove creep rupture |
| Crack associated with notch/gouge | Notch-driven SCG or damage-assisted cracking | Damage geometry, fracture examination, material SCG qualification, stress/service history | Assess damage acceptance, installation controls and qualification basis | A gouge near a crack does not prove it initiated failure |
| Failure at/near fusion joint | Joining-related mechanism, local geometry or interacting load | Procedure records, operator/equipment records, joint geometry, destructive/NDT evidence where applicable | Reassess joining qualification, execution and inspection controls | Location at a joint does not automatically prove poor fusion |
| Local wall loss / severe surface damage | Installation or external mechanical damage | Installation records, excavation evidence, damage dimensions, local loading | Review installation method, damage criteria and protection | Visible damage may be secondary rather than causal |
| Failure associated with unusual fluid/environment | Chemical/environmental interaction | Fluid composition, concentration, temperature, exposure duration, compatibility evidence | Reopen compatibility assessment and material selection | Generic chemical-resistance charts do not establish causation |
| Failure following elevated-temperature period | Temperature/service excursion | Recorded temperatures, duration, pressure history, governing temperature/time basis | Recalculate service capability and investigate permanent damage | Temporal correlation is not proof of causation |
| Repeated failures at similar geometry/location | Systematic design/detailing/loading issue | Population data, geometry, restraint, support, fabrication and operating history | Escalate from individual failure to fleet/system review | Repetition strengthens a hypothesis but does not replace mechanism evidence |

## 10.3 Separate initiation from final rupture

\[
\text{final fracture appearance}\neq\text{necessarily the initiating mechanism}
\]

Where evidence permits, distinguish `initiation → propagation → final instability / rupture`.

## 10.4 Do not use SCG qualification as immunity from damage

> **Was the actual local condition within the damage, installation and qualification assumptions used by the design?**

## 10.5 A joint failure is a system question

Do not collapse a failure near a fusion or fitting into “bad weld.” Review material/product compatibility, preparation, alignment, contamination, equipment, procedure, operator execution, joining environment, fitting geometry, restraint/displacement, bending, service history and inspection evidence.

## 10.6 Failure evidence should reopen the Design Basis

| Design assumption | Failure-review question |
|---|---|
| Pressure | Was actual pressure, including transients, within the assumed envelope? |
| Temperature | Did actual temperature/time history match the Design Basis? |
| Material | Was the installed material/product the specified qualified product? |
| SDR / wall | Were actual dimensions and damage condition consistent with the calculation? |
| Chemistry | Was actual fluid/environment consistent with compatibility assumptions? |
| Installation | Were assumed installation and damage controls achieved? |
| Joining | Were qualification/execution/inspection assumptions achieved? |
| External loads | Were settlement, restraint, support or third-party loads omitted or underestimated? |

A failure can expose a Design Basis/execution departure, an incomplete Design Basis, or several smaller deviations that interacted.

## 10.7 FIG-013-005 — PE Failure Lens

```text
Failure / abnormal condition observed
                ↓
Preserve and document evidence
                ↓
Confirm product + material + geometry + service history
                ↓
Define multiple plausible mechanisms
                ↓
What evidence would distinguish them?
                ↓
Collect / test / examine
                ↓
Mechanism supported?
        ↙              ↘
      NO                YES
      ↓                  ↓
Revise hypotheses     Identify initiating
and continue          + contributing factors
        \                /
         ↓              ↓
      Reopen Design Basis
                ↓
Design / operation / installation /
joining / inspection response
                ↓
Check for fleet/system implications
                ↓
Document disposition
```

If evidence does not support the preferred hypothesis, revise the hypothesis—not the evidence.

## 10.8 Evidence strength matters

Distinguish **direct evidence**, **corroborating evidence**, **inference** and **assumption** explicitly in the review record.

## 10.9 Convert the result into engineering action

Possible dispositions include revising installation/damage controls, joining qualification/inspection, allowable service envelope, SDR/product configuration, material/product qualification, transient/structural analysis, chemical compatibility basis, fleet inspection, operating restriction, Design Basis assumptions or escalation to specialist failure analysis.

## 10.10 Know when this chapter is no longer enough

Escalate when safety/regulatory consequences are significant, evidence is conflicting, fracture interpretation is central, litigation/insurance implications exist, laboratory characterization is required, repeated fleet failures occur, the initiating mechanism remains uncertain or corrective action depends strongly on an unverified hypothesis.

## 10.11 Engineering decision from Investigation 10

> **Failure appearance generates hypotheses. Evidence supports mechanisms. Engineering action follows the supported mechanism and its uncertainty.**

This closes the chapter arc: mechanism understanding → long-term evidence → classification/design → project decision → field evidence feedback.

---

# CL-013-001 — PE Pressure-Piping Design Review Checklist

| ID | Review question | Required evidence / disposition |
|---|---|---|
| CL-01 | Is the Design Basis sufficiently defined? | Fluid, pressure, temperature, life, environment, installation and operating envelope documented |
| CL-02 | Has the governing standards path been identified? | Material, product, application, joining and project/regulatory standards identified |
| CL-03 | Is the selected PE material classification demonstrated? | Traceable qualification/classification evidence |
| CL-04 | Is product conformity separate from material qualification? | Pipe/fitting/product certification or equivalent evidence |
| CL-05 | Is the long-term strength basis understood and traceable? | Appropriate qualification/regression/classification route identified |
| CL-06 | Is the applicable design coefficient C justified? | Source and application scope recorded; not copied from an unrelated service |
| CL-07 | Has design stress been calculated and independently checked? | `EQ-013-002` calculation, units and rounding basis verified |
| CL-08 | Are SDR and dimensions correctly interpreted? | Product dimensions/SDR verified against governing product framework |
| CL-09 | Has the reference pressure basis been independently calculated? | `EQ-013-003/004` calculation and unit conversion checked |
| CL-10 | Has temperature and required service duration been addressed? | Governing temperature/time treatment documented |
| CL-11 | Has chemical/environmental compatibility been demonstrated? | Evidence applicable to actual fluid, concentration, temperature and exposure |
| CL-12 | Have credible pressure transients and cyclic loads been addressed? | Included in pressure envelope or separately analysed |
| CL-13 | Have installation and external mechanical conditions been evaluated? | Burial/support/restraint/movement/damage assumptions documented |
| CL-14 | Are fittings, valves, fabricated components and joints compatible with the system basis? | Component and joining qualification/limitations verified |
| CL-15 | Is the joining route defined and controllable? | Procedure, equipment, competence and inspection requirements identified |
| CL-16 | Have pipe markings and traceability been verified without treating them as proof of suitability? | Marking reconciled with specified product and documentation |
| CL-17 | Are assumptions, exclusions and unresolved items explicit? | Open-item register or calculation notes |
| CL-18 | Have all standards-derived values been validated against the authoritative current source? | Final Standards Validation complete |
| CL-19 | Have worked calculations and critical engineering decisions received independent review? | Checker/reviewer evidence |
| CL-20 | Is the final disposition explicit? | **GO / CONDITIONAL GO / NO-GO** with conditions stated |

### Checklist completion rule

A checked box means **evidence reviewed and acceptable**, not merely that the subject was considered. If an item does not apply, record **N/A with justification**. If a material item remains unresolved, the disposition remains **CONDITIONAL GO** or **NO-GO** rather than silently converting uncertainty into an assumption.

---

# Chapter 13 Engineering Closure

Polyethylene pressure-piping design is not a sequence that begins with PE100 and ends with SDR. It begins with the **Design Basis**.

`Design Basis → Standards Path → Material Behaviour → Long-Term Evidence → Classification → MRS → C → Design Stress → SDR → Reference Pressure → Service Verification → System Decision`

Each arrow represents an engineering obligation. Skipping one may still produce a plausible number. It does not necessarily produce a justified design.

## Three distinctions to retain

1. **Material capability is not system capability.** A qualified material is necessary, but finished product, joints, fittings, installation and actual service environment still require engineering verification.
2. **Reference pressure is not automatically allowable operating pressure.** The material/geometry calculation is important, but temperature, service duration, application requirements, components, transients and other Design Basis conditions still have to be applied.
3. **Qualification evidence is not immunity from failure.** Long-term pressure qualification and SCG-resistance evidence demonstrate performance within defined qualification frameworks; they do not make arbitrary defects, poor joints, excessive temperature, incompatible environments or loads outside the qualified envelope acceptable.

## Final engineering decision

A defensible PE selection should allow another competent engineer to reconstruct why the material was selected, which standards govern it, what evidence establishes long-term capability, how design stress was obtained, why the SDR was selected, how pressure capability was calculated, what changed when actual service conditions were applied, how joining/installation/components were addressed and what assumptions remain.

## Residual project-specific engineering

Depending on the application, additional work may include transient hydraulic analysis, detailed flexibility/stress analysis, buried-pipe/soil interaction, support/restraint design, detailed chemical compatibility assessment, joining procedure development and qualification, NDE/inspection planning, installation engineering, specialist failure analysis, regulatory qualification and application-specific code/standard compliance.

The chapter's job is to tell the engineer **when those interfaces have been reached**, not to reproduce every specialist discipline inside the PE chapter.

---

# Chapter engineering assets — normalized register

| ID | Asset | Integrated status |
|---|---|---|
| FIG-013-001 | Semicrystalline structure → engineering behaviour | Placeholder retained |
| FIG-013-002 | Slow crack growth concept | Placeholder retained |
| FIG-013-003 | Long-term hydrostatic regression concept | Defined; original figure pending |
| FIG-013-004 | PE pressure-design decision chain | Integrated |
| FIG-013-005 | PE Failure Lens | Integrated |
| FIG-013-006 | Test data → regression → classification → product marking chain | Placeholder retained |
| FIG-013-007 | PE pipe marking anatomy | Placeholder retained |
| EQ-013-001 | Thin-wall hoop-stress approximation | Integrated |
| EQ-013-002 | MRS → design stress | Integrated; standards validation pending |
| EQ-013-003 | SDR definition | Integrated; technical metadata complete; standards validation pending |
| EQ-013-004 | SDR pressure relationship | Integrated; technical metadata complete; standards validation pending |
| TAB-013-001 | PE classification / terminology | Integrated; standards validation pending |
| TAB-013-002 | Pipe marking interpretation | Integrated; standards validation pending |
| TAB-013-003 | PE Design Input / Verification Matrix | Integrated |
| TAB-013-004 | Failure Evidence / Engineering Response Matrix | Integrated |
| TAB-013-005 | MRS / C / design stress / SDR / pressure reference chain | Integrated; standards validation pending |
| EX-013-001 | Worked Example A — pressure / SDR interpretation | Integrated; independently recalculated; standards path explicit |
| EX-013-002 | Worked Example B — changed Design Basis | Integrated; equivalent independent decision-path verification complete; numerical standards treatment intentionally withheld |
| CL-013-001 | PE Pressure-Piping Design Review Checklist | Integrated |

---

# Publication Hold Point — Standards Validation Required

Completion of the engineering narrative does not close Chapter 13.

Before publication, every standards-derived statement used in the chapter shall be reviewed against the authoritative applicable edition. The review shall include, at minimum:

`edition and scope → terminology → equations → coefficients → classification values → reference conditions → rounding rules → temperature/time treatment → test/qualification pathways → PE100-RC treatment → product marking → normative wording`

Any discrepancy discovered during this review shall be resolved in favour of the authoritative standard, and affected chapter text, equations, tables and examples shall be corrected before Design Freeze.

Specific hold points include current ISO 9080/12162 terminology and editions; PE100↔MRS relationship; definition/source/applicability of design coefficient C; pressure relationship and unit convention; temperature/time treatment; PE100-RC status and qualification route; product marking requirements; and any final normative wording.

---

# Integration status

This file is the consolidated **Chapter 13 Rev 1.0 Standards-Validation candidate** under PDS Baseline 1.0. Gap Closure Review, pre-Technical verification and Technical Review are complete. The Technical Review closed with no unresolved physics, equation, unit, internal-consistency or example-verification findings. Investigations 1–10, Quick Navigation, normalized engineering assets, the Design Review Checklist and chapter closure are integrated.

The chapter is **not yet publication-frozen**. The remaining gates are authoritative Standards Validation against current sources, correction of any standards findings, final editorial/academic review as required, and Design Freeze.