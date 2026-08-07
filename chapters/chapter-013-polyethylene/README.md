---
chapter: 013
title_en: "Polyethylene (PE)"
part: "Materials"
status: redevelopment-draft
language: en
technical_level: intermediate
primary_domains:
  - materials
  - pressure-design
  - standards-navigation
  - failure-analysis
review:
  physics: pending
  standards: pending
  academic: pending
  equations: pending
  units: pending
  examples: pending
  editorial: pending
last_updated: 2026-08-07
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

---

# Investigation 1 — Why Did Polyethylene Become a Major Pressure-Piping Material?

Polyethylene became a major pressure-piping material not because it maximises a single material property, but because it combines several engineering advantages in one system: corrosion resistance, low density, toughness, flexibility, fusion joining and long-term pressure capability.

That combination matters more than any one headline property.

A metallic piping system may provide high stiffness and high short-term strength, yet require corrosion allowance, coatings, cathodic protection or additional maintenance in aggressive environments. A more rigid thermoplastic may provide good corrosion resistance but respond differently to impact, ground movement or installation strain. PE occupies a different engineering space: it accepts relatively large deformation while maintaining useful long-term pressure performance when selected, manufactured, joined and operated within its qualified envelope.

This is the first principle of PE engineering:

> **PE is valuable because the complete piping system can tolerate combinations of pressure, deformation and environment that would be managed differently in many conventional materials.**

That statement does not mean PE is universally superior. Its lower stiffness, strong temperature dependence, time-dependent deformation and sensitivity to certain damage mechanisms create their own design obligations.

## 1.1 The useful comparison is system behaviour, not material reputation

A competent material-selection review should avoid questions such as:

> “Is PE stronger than PVC?”

or

> “Is PE100 better than PP?”

Those questions are incomplete because the answer depends on the Design Basis.

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

## 1.2 Why short-term strength is not the governing design story

A common mistake is to judge a pressure-piping material primarily by short-term tensile strength.

That is not how PE pressure-piping performance is established.

A PE pipe under sustained internal pressure is not subjected to a one-time tensile test. It experiences stress over years or decades, often while temperature, environment, installation condition and cyclic pressure alter the rate at which damage mechanisms develop.

Therefore, the pressure-design problem must be framed in terms of **time-dependent material behaviour**.

The engineering chain is approximately:

`Long-term hydrostatic test evidence → regression / extrapolation → material classification → design stress framework → pipe geometry → product/application requirements → project verification`

This chain is the central architecture of the chapter.

## 1.3 Engineering implications of PE flexibility

Flexibility is frequently presented as a simple advantage. It is more useful to treat it as an engineering property with both benefits and consequences.

Potential benefits include:

- tolerance of ground settlement and alignment variation;
- reduced sensitivity to some imposed displacement loads;
- practical long-radius field routing;
- good impact response in many installation conditions.

Potential consequences include:

- greater movement under thermal loading;
- lower bending stiffness;
- higher dependence on support and restraint philosophy in above-ground systems;
- greater sensitivity of system geometry to temperature and loading history.

The correct conclusion is not “PE is flexible.”

The correct conclusion is:

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

The governing question is not:

> “What stress causes immediate yielding?”

It is:

> **“What sustained stress can the qualified material withstand for the intended service duration and temperature, within the applicable standards framework?”**

That shift from instantaneous strength to long-term behaviour is fundamental.

## 2.2 Creep is not automatically failure

Under sustained stress, PE continues to deform with time. This time-dependent deformation is commonly described as creep.

Creep should not be treated as synonymous with failure. Some time-dependent deformation is an expected material behaviour and may be compatible with successful service.

The engineering task is to determine whether the resulting deformation, stress redistribution and damage evolution remain inside the qualified design envelope.

This distinction becomes important later when the chapter connects long-term test data to regression behaviour, MRS and design stress.

## 2.3 Crack behaviour requires a separate engineering lens

A component may have adequate nominal wall thickness and still contain a local stress concentration caused by a notch, scratch, installation damage, joint geometry or other discontinuity.

The local crack-driving condition is therefore not described completely by nominal hoop stress alone.

PE pressure-piping engineering must consider both:

1. **global pressure loading**, and
2. **local resistance to crack initiation and growth**.

This is the conceptual bridge to slow crack growth, addressed later in the chapter.

## 2.4 Processing quality belongs in the engineering chain

Material designation alone does not prove that every manufactured component possesses identical engineering quality.

Processing history can influence morphology, residual stress, dimensions and local defects. Consequently, engineering qualification must distinguish between:

- material classification;
- product conformity;
- joining quality;
- installed-system condition.

This distinction will recur throughout the chapter because one of the most common conceptual errors in plastic piping is treating qualification of the resin as qualification of the entire system.

## 2.5 Engineering decision from Investigation 2

The molecular and semicrystalline structure of PE explains why time, temperature, deformation and crack resistance must be treated as primary design variables. Short-term mechanical properties alone are insufficient to establish pressure-piping suitability.

**[VISUAL 13-01 — PLACEHOLDER]**  
**Semicrystalline PE structure → engineering consequence**  
Show crystalline and amorphous regions conceptually, then connect them to stiffness, creep, ductility and crack resistance. Original engineering illustration; not decorative.

---

# Investigation 3 — What Do PE80, PE100 and Related Material Designations Actually Tell the Engineer?

Material designations are useful because they compress a large amount of qualification information into a short identifier. They become dangerous when the identifier is interpreted as a complete design decision.

The first question is therefore not “Which PE number is higher?” but:

> **What engineering property does the designation represent, under which qualification framework, and what does it not establish?**

PE pressure-piping classifications are tied to long-term hydrostatic strength concepts rather than to a simple ranking of short-term tensile strength.

A higher classification may permit a higher design stress or a thinner wall for a defined pressure relationship, depending on the governing standards and design coefficient. But that does not automatically establish suitability for temperature, fluid compatibility, installation method, crack-growth resistance, joining procedure or a particular regulatory application.

## 3.1 Material class is one input to the design problem

For engineering purposes, the chain should be kept explicit:

`Material evidence → material classification → design coefficient / design stress → geometry → product standard → service verification`

Each arrow represents a separate engineering step.

Skipping steps is the source of many misapplications.

## 3.2 PE100 is not a universal certificate of suitability

A pipe marked PE100 may still be unsuitable for a project if, for example:

- the temperature-adjusted pressure capability is inadequate;
- the application lies outside the governing product-standard scope;
- chemical exposure is not acceptable;
- cyclic or transient loading requires additional assessment;
- installation damage or environmental conditions create additional risk;
- the joining system or inspection strategy is not appropriate.

Therefore:

> **PE100 is a material-classification input. It is not a project approval.**

## 3.3 PE100-RC requires careful standards treatment

Terms associated with enhanced resistance to slow crack growth are widely used in industry, but terminology, qualification routes and standards status must be handled carefully.

This chapter will not make a generic claim about the meaning or equivalence of such designations until the final Standards Validation pass confirms the authoritative definitions and their applicable scope.

This is intentional. A popular market term is not automatically a universal standards designation.

## 3.4 Engineering decision from Investigation 3

Use the PE material designation to establish the material-classification branch of the design process. Do not use it to bypass product qualification, geometry selection, service-condition verification or project-specific engineering checks.

**[TABLE 13-01 — TO DEVELOP]**  
**PE terminology and classification — what each designation tells the engineer and what it does not tell the engineer.**

---

# Investigation 4 — Why Does Long-Term Behaviour Govern PE Pressure Design?

A pressure pipe does not experience material properties at one instant in time. It experiences a history of stress, temperature, environment, installation condition and operating events. For polyethylene, that history is not a secondary correction to the design problem; it is part of the design problem itself.

The engineer therefore needs two distinct questions in mind:

1. **Can the pipe resist the present load?**
2. **Can the qualified material and product continue to resist the relevant load history for the required life?**

The first question is largely instantaneous. The second is time-dependent. PE pressure design is governed primarily by the second.

## 4.1 Sustained stress changes the response with time

Under a sustained load, PE exhibits creep: strain continues to develop even when the applied stress is approximately constant. At the same time, stress may redistribute locally as the polymer deforms. The result is that a geometry which appears acceptable in a short-duration test cannot be assumed to behave identically over years of service.

For a pressure pipe, internal pressure produces circumferential stress in the wall. A simple thin-wall representation is useful for intuition:

\[
\sigma_\theta \approx \frac{pD_m}{2e}
\]

**Eq. 13-01 — Thin-wall hoop-stress approximation**

where:

- \(\sigma_\theta\) = circumferential or hoop stress;
- \(p\) = internal pressure;
- \(D_m\) = representative mean diameter;
- \(e\) = wall thickness.

This equation is not the pressure-rating equation used later in the chapter. It is included here only to expose the mechanical relationship: increasing pressure or diameter increases nominal hoop stress, while increasing wall thickness reduces it.

**Validity note:** the expression is a thin-wall approximation and does not replace the geometry and stress relationships required by the governing product or design standard.

**Common misuse:** using a nominal hoop-stress calculation as proof of long-term life. The equation estimates nominal membrane stress; it says nothing by itself about time-to-failure, temperature, notches, local defects, material qualification or crack-growth resistance.

## 4.2 Creep, rupture and crack growth are different engineering questions

Three phenomena are often mixed together in casual discussion:

- **creep deformation** — time-dependent strain under sustained stress;
- **long-term rupture** — loss of pressure-boundary integrity after a period under load;
- **slow crack growth (SCG)** — progressive crack extension from a local stress concentration over time.

They are related through time-dependent polymer behaviour, but they are not interchangeable.

A pipe may creep without failing. A pipe may remain dimensionally acceptable while a local crack grows from a notch. A short-term burst test may show high immediate strength while providing limited information about the slow damage mechanism that governs a long service period.

The practical consequence is that engineers should not use one test result to answer a different failure question.

## 4.3 Long-term failure behaviour is not represented by one mechanism

At comparatively high stress or severe conditions, deformation and rupture may be dominated by ductile behaviour. At lower stress and longer times, local crack processes can become increasingly important. Temperature strongly affects the rate at which these mechanisms develop.

The exact transition behaviour is material- and condition-dependent and is treated through qualified test and regression procedures rather than a universal hand calculation.

For design purposes, the important point is this:

> **A lower nominal stress does not make time irrelevant. It changes which time-dependent mechanism may govern.**

This is one reason long-duration evidence is central to PE pressure-piping classification.

## 4.4 Nominal stress is not local crack-driving stress

Pressure design calculations normally work with nominal geometry and nominal stress. Failures, however, often initiate locally.

Potential local stress raisers include:

- scratches and gouges;
- notches;
- sharp geometric transitions;
- local wall-thickness reduction;
- manufacturing defects;
- joint discontinuities;
- embedded damage or foreign-body effects;
- installation-induced deformation.

The local condition at such a feature can be much more severe than the nominal pipe-wall stress suggests.

This distinction is essential when reviewing a damaged pipe. A statement such as “the line pressure was below nominal rating” does not eliminate the possibility of a locally driven long-term crack mechanism.

## 4.5 Slow crack growth is a system concern, not only a resin property

Slow crack growth resistance is strongly influenced by material behaviour, but the engineering risk is created by the combination of:

`material resistance × local defect severity × stress history × temperature × environment × time`

This is why a high-performing resin cannot compensate for every installation defect, and why an observed crack cannot automatically be blamed on resin quality.

When SCG is credible, the engineer should ask:

- Where did the crack initiate?
- What local feature created the stress concentration?
- What was the pressure and temperature history?
- Was installation damage present before service?
- Did the crack grow through base pipe, joint region or another local feature?
- Is the observed morphology consistent with a slow process, a rapid overload, or a combination?

The detailed forensic methodology belongs to the failure-analysis chapters, but these questions belong in material selection because the failure mechanism begins with the Design Basis and installation reality.

## 4.6 Why time-to-failure data matter

If a material is intended for decades of pressure service, the engineer needs evidence that connects applied stress and temperature to the time at which failure occurs.

A single burst pressure does not provide that relationship.

A meaningful long-term dataset contains multiple specimens tested at controlled stress and temperature conditions, producing a population of failure times. Those data can then be evaluated through a defined regression and extrapolation methodology.

Conceptually:

`controlled stress + controlled temperature → observed time to failure → regression model → long-term strength evidence`

Investigation 5 explains how this evidence can be generated without waiting for the full intended design life, and Investigation 6 explains what the regression output means to the practicing engineer.

## 4.7 Engineering use: a long-term behaviour screening check

Before treating a nominal PE pressure designation as sufficient, the engineer should screen the Design Basis for conditions that can change the long-term damage process.

| Design Basis question | Why it matters to long-term behaviour | Engineering response |
|---|---|---|
| Is temperature above the reference condition used for nominal classification? | Time-dependent deformation and failure processes accelerate with temperature | Apply the governing temperature treatment and re-check pressure capability |
| Are significant pressure cycles or transients credible? | Repeated loading adds a damage mechanism not represented by steady nominal pressure alone | Perform cyclic/transient assessment as required by the project basis |
| Is installation damage credible? | Local notches can control crack initiation even when nominal stress is acceptable | Define damage acceptance, inspection and repair criteria |
| Is the fluid/environment known to affect PE behaviour? | Environment can influence deformation, cracking or chemical resistance | Perform compatibility and application-specific verification |
| Is the line buried, restrained or subject to imposed displacement? | Secondary loads can alter the local stress state | Evaluate system loads, not internal pressure alone |
| Is the intended life unusually long or uncertain? | Long-term classification is meaningful only when used within its defined framework | Confirm the relevant qualification basis and project life assumptions |

The table is intentionally a screening tool, not a substitute for the detailed analyses elsewhere in the book.

## 4.8 Failure evidence: what can and cannot be concluded quickly

A failed PE component often invites an immediate explanation based on where the fracture is visible. That is unsafe engineering practice.

Examples of weak conclusions include:

- “It failed beside the fusion bead, therefore the fusion was bad.”
- “The pipe was below PN, therefore pressure was not involved.”
- “The material was PE100, therefore the resin could not be the issue.”
- “The fracture looks brittle, therefore there was no prior ductile deformation.”

A technically defensible conclusion requires reconstruction of the load history, temperature, installation condition, product identity, joint history, damage state and fracture origin.

Investigation 10 develops this failure lens in detail.

## 4.9 Engineering decision from Investigation 4

A PE pressure design is incomplete if it checks only present-day nominal stress or nominal pressure rating. The engineer must establish that the selected material, geometry and product standard provide an appropriate long-term basis for the actual temperature, loading history, installation condition and credible local damage mechanisms.

The correct engineering sequence is therefore:

`Nominal pressure load → long-term material evidence → local damage considerations → service modifiers → project verification`

not:

`PN marking → acceptance`

### Practical check — before moving on

If the design review cannot answer **what evidence supports the required service duration**, then the long-term pressure basis has not yet been demonstrated.

**[VISUAL 13-02 — PLACEHOLDER]**  
**Slow crack growth concept**  
Show nominal pipe-wall stress, a local notch, crack initiation and progressive crack extension over time. The figure should explicitly separate nominal stress from the local crack-driving condition.

---

# Investigation 5 — How Can Decades of Performance Be Evaluated Before Decades Have Passed?

*Engineering redevelopment pending.*

Required content:

- accelerated long-term hydrostatic testing concept;
- temperature as an acceleration variable;
- test evidence versus service prediction;
- why extrapolation must remain inside a validated methodology;
- direct standards navigation to ISO 9080 after validation.

---

# Investigation 6 — What Does Regression Analysis Mean to the Practicing Engineer?

*Engineering redevelopment pending.*

Required content:

- stress versus time-to-failure concept;
- lower-confidence behaviour;
- regression output as engineering evidence rather than a graph-fitting exercise;
- assumptions and transferability;
- relationship to material classification.

**[VISUAL 13-03 — PLACEHOLDER]** Long-term hydrostatic regression concept.

---

# Investigation 7 — How Does Long-Term Evidence Become MRS and Material Classification?

*Engineering redevelopment pending.*

Required equations / concepts:

- MRS classification basis;
- design coefficient / design stress relationship;
- exact terminology and notation to be validated against current authoritative standards;
- explicit distinction between material classification and project allowable condition.

---

# Investigation 8 — How Do SDR, Wall Thickness and Material Class Become a Pressure Designation?

*Engineering redevelopment pending.*

Core equations to develop and number:

\[
SDR = \frac{d_n}{e_n}
\]

and the applicable standards-based pressure relationship linking design stress / MRS, coefficient and SDR.

The final equation form, notation and standards attribution will be validated before publication.

Required assets:

- numbered equations;
- symbol / unit definitions;
- validity and misuse notes;
- MRS / coefficient / SDR / pressure relationship table;
- Worked Example A — Pressure / SDR interpretation.

---

# Investigation 9 — How Should an Engineer Select PE for a Real Design Basis?

*Engineering redevelopment pending.*

Required workflow:

`Design Basis → Applicable standards → Qualified material → Long-term/design stress input → Geometry/SDR → Pressure/temperature verification → Chemical/mechanical/service checks → Joining/installation constraints → Verification → Engineering decision`

Required content:

- temperature effects;
- chemical/environmental compatibility;
- cycling and transients as additional checks;
- installation damage;
- buried versus above-ground context;
- joining and inspection interfaces;
- Worked Example B — changed service conditions.

**[VISUAL 13-04 — PLACEHOLDER]** Full PE engineering workflow.

---

# Investigation 10 — Failure Lens: What Does a PE Failure Actually Prove?

*Engineering redevelopment pending.*

Required content:

- visible failure location versus root cause;
- pressure, temperature and service-history reconstruction;
- installation damage and slow crack growth;
- joining evidence;
- distinction between material failure, product failure, joint failure and system-design failure;
- evidence-preservation workflow.

Required asset:

**[TABLE 13-02 — TO DEVELOP]** Failure mechanism / evidence / engineering response.

---

# Chapter engineering assets — development register

| ID | Asset | Status |
|---|---|---|
| Visual 13-01 | Semicrystalline structure → engineering behaviour | Placeholder defined |
| Visual 13-02 | Slow crack growth concept | Placeholder defined |
| Visual 13-03 | Long-term hydrostatic regression concept | Placeholder defined |
| Visual 13-04 | Full PE engineering workflow | Placeholder defined |
| Table 13-01 | PE terminology / classification | To develop |
| Table 13-02 | Failure mechanism / evidence / response | To develop |
| Table 13-03 | Design-input checklist | To develop |
| Table 13-04 | Pipe marking: tells / does not tell | To develop |
| Table 13-05 | MRS / coefficient / SDR / pressure relationship | To develop after standards validation basis is established |
| Example 13-A | Pressure / SDR interpretation | To develop |
| Example 13-B | Changed service condition | To develop |
| Checklist 13-01 | PE design-review checklist | To develop |

---

# Standards validation hold points

The following shall not be treated as publication-ready until rechecked against authoritative standards after the writing pass:

- standard editions;
- clause / table references;
- material-classification terminology;
- numerical MRS values used in examples or tables;
- minimum design coefficients / factors by application;
- pressure-relationship notation;
- temperature derating values or tables;
- PE100-RC terminology / standards status;
- product-marking requirements;
- any claim using the words *shall*, *required*, *minimum*, *maximum* or equivalent normative language.

---

# Chapter-end Design Review Checklist

*To be completed after Investigations 4–10 are developed.*

The final checklist shall allow a practicing engineer to verify, at minimum:

- Design Basis completeness;
- correct standards path;
- material classification;
- product qualification;
- design stress basis;
- SDR / pressure interpretation;
- temperature effects;
- chemical and environmental compatibility;
- cyclic / transient conditions;
- joining and installation constraints;
- inspection / repair strategy;
- residual project-specific checks.

---

# Development note

This chapter is the reference implementation of PDS Baseline 1.0. Existing strong explanatory material is to be preserved where it supports the approved Chapter Design Brief. Missing standards navigation, equations, tables, workflows, worked examples, limitations and design-review tools are to be added systematically rather than by wholesale stylistic rewriting.