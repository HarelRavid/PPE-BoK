---
chapter: 12
title: Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating
part: Material Selection
status: research-based-draft
language: en
---

# Chapter 12 — Long-Term Strength, MRS, Design Stress, SDR and Pressure Rating

## Why This Chapter Matters

A pressure designation printed on a thermoplastic pipe can appear deceptively simple.

An engineer may see:

**PE100 — SDR 11 — PN 16**

and conclude that the system is suitable for every service below 16 bar.

That conclusion is incomplete.

Thermoplastic pressure capability is derived through a chain that begins with long-term material evidence and ends with a project-specific engineering decision.

The relevant chain is:

> **long-term pipe-test evidence → statistical strength basis → material classification → application design stress → pipe geometry → product pressure classification → project service-case verification → allowable project decision**

Each step answers a different engineering question.

Confusing the steps can produce serious errors.

A material classification is not a pipe pressure rating.

A pipe pressure classification is not a complete system rating.

A nominal pressure designation is not automatically the allowable operating pressure for the actual project.

### Reader outcomes

After this chapter, the reader should be able to:

- explain why short-term strength is insufficient for thermoplastic pressure design;
- describe the conceptual role of long-term hydrostatic testing and statistical extrapolation;
- distinguish long-term material strength information from MRS and design stress;
- explain the role of the application-specific design coefficient;
- define SDR and interpret its geometric meaning;
- use the conventional SDR pressure relationship only when its applicability conditions are satisfied;
- distinguish material classification, pipe/product classification, component rating, and project system allowable pressure;
- distinguish PN, MOP, operating pressure, design pressure, and test pressure;
- explain why temperature, time, chemistry, cycling, components, joints, and local geometry remain separate checks;
- recognize when incomplete pressure-design evidence requires an assumption, controlled hold, or additional verification.

---

## 12.1 The Pressure-Design Chain

Thermoplastic pressure design is not one equation.

It is a chain of engineering evidence and decisions.

A useful representation is:

1. long-term pressure-test evidence;
2. statistical long-term strength basis;
3. material classification;
4. application-specific design stress;
5. pipe geometry;
6. product pressure classification;
7. service-condition verification;
8. component and system verification;
9. final project pressure decision.

The chain should not be shortened casually.

For example:

`PE100`
does not directly mean
`PN 16`.

And:

`PN 16`
does not directly mean
`16 bar allowable project operating pressure`.

Every link between those statements matters.

---

## FIG-012-001 — Long-Term Strength to Project Pressure Decision

**Conceptual figure placeholder**

`Long-term pipe test evidence`
↓
`Statistical strength basis`
↓
`Material classification`
↓
`Application design coefficient`
↓
`Design stress`
↓
`Pipe geometry / SDR`
↓
`Product pressure classification`
↓
`Temperature / time / chemistry / cycling`
↓
`Components / joints / local geometry`
↓
`PROJECT PRESSURE DECISION`

Side branches:

`Missing evidence`
→
`ASSUMPTION / CONTROLLED HOLD`

`Changed service case`
→
`REOPEN PRESSURE VERIFICATION`

Central message:

> **PN is a product classification inside the chain, not the final engineering decision.**

---

## 12.2 Why Short-Term Strength Is Not Enough

Thermoplastics are viscoelastic.

Their response depends on:

- stress magnitude;
- time;
- temperature;
- loading history;
- material structure;
- environment.

A thermoplastic pipe can withstand a high stress for a short period while being unsuitable for sustained long-term operation at that same stress.

Short-duration mechanical values therefore cannot be used automatically as decades-long pressure-design values.

Long-term pressure-pipe classification instead uses data from pipe specimens tested under pressure at defined conditions.

The objective is to characterize the relationship among:

- hoop stress;
- test temperature;
- time to failure;
- observed failure behaviour.

This is one of the fundamental differences between thermoplastic pressure-pipe engineering and design based only on short-term mechanical strength.

---

## 12.3 Long-Term Hydrostatic Strength Evidence

ISO 9080 is identified in the chapter source register as the primary standard framework for statistical extrapolation of long-term hydrostatic strength from thermoplastic pipe-test data.

In simplified engineering terms:

- multiple pipe specimens are tested;
- different stresses and temperatures are used;
- failure times are recorded;
- the resulting dataset is evaluated statistically;
- long-term behaviour is extrapolated according to the governing procedure.

The piping engineer normally does not recreate the complete statistical classification procedure during routine project design.

Instead, the engineer uses the resulting qualified material classification within the relevant product and design framework.

### Engineering interpretation

The long-term hydrostatic-strength result is not, by itself:

- the final design stress;
- the pressure rating of a pipe;
- the allowable system pressure;
- proof of chemical compatibility;
- fatigue qualification;
- proof of joint quality;
- a guarantee of installed service life.

It is one upstream input into the pressure-design chain.

---

## 12.4 Statistical Strength Basis and the Reference Period

The ISO classification framework uses long-term statistical interpretation of pipe-test data at defined reference conditions.

The existing chapter basis associates material classification with a long-term reference at:

- **20°C**;
- **50 years**,

subject to the definitions and procedures of the applicable standards.

At this stage of the manuscript, the safest conceptual description is:

> **a conservative lower statistical long-term strength basis derived according to the applicable classification framework**

rather than attempting to reproduce clause-level statistical terminology without the final full-text standards lock.

### What the 50-year reference does not mean

A 50-year classification does not mean:

- automatic failure after 50 years;
- guaranteed 50-year field life;
- prohibition of service beyond 50 years;
- automatic permission to increase stress arbitrarily for shorter service.

The classification is a reference point within a controlled long-term strength framework.

Actual installed life depends on the complete service and system context.

---

## 12.5 Minimum Required Strength — MRS

ISO 12162 is identified in the chapter source register as the primary ISO framework for thermoplastic material classification, designation, and design-stress calculation.

The **Minimum Required Strength — MRS** is a classified long-term strength value assigned within that framework.

It is expressed in MPa.

Examples used in the current manuscript include:

- PE100 → MRS class of 10 MPa;
- PE80 → MRS class of 8 MPa.

### PE100 does not mean

- 100 MPa tensile strength;
- 100 bar allowable pressure;
- 100-year guaranteed life;
- universal superiority over every alternative.

It is a material classification within a defined long-term hydrostatic-strength system.

### MRS is not a complete material specification

Two materials with the same MRS may differ in:

- slow-crack-growth performance;
- rapid-crack-propagation behaviour;
- oxidation stability;
- processing behaviour;
- fusion behaviour;
- chemical resistance;
- additive package;
- product qualification.

MRS answers one important question.

It does not answer every material or system question.

---

## 12.6 PE100, PE100-RC, and PE100+

These terms describe different aspects of polyethylene qualification.

### PE100

A long-term strength classification associated with an MRS class of 10 MPa in the applicable ISO framework.

### PE100-RC

A PE100 material with additional slow-crack-growth qualification within the relevant material/product framework.

It does not create a higher MRS class automatically.

### PE100+

An industry quality-assurance designation associated with listed PE100 materials that satisfy additional recurring requirements.

It is not an ISO MRS class above PE100.

The same material may therefore be:

- PE100;
- additionally qualified as PE100-RC;
- and also included in a PE100+ quality listing.

These designations should not be inserted interchangeably into pressure calculations.

---

## 12.7 From MRS to Design Stress

A material classification must be converted into a design stress appropriate to the applicable engineering framework.

A common ISO-form relationship is:

\[
\sigma_s = \frac{MRS}{C}
\]

where:

- \(\sigma_s\) = design stress, MPa;
- \(MRS\) = minimum required strength, MPa;
- \(C\) = design coefficient, dimensionless.

The design coefficient reduces the classified material strength to a design value.

---

## 12.8 The Design Coefficient Is a Controlled Application Input

The coefficient \(C\) should not be treated as a generic personal “safety factor.”

Its applicable value depends on the governing framework.

Relevant influences may include:

- material family;
- application;
- conveyed medium;
- product standard;
- regulatory context;
- design standard;
- project requirements.

The engineer should therefore ask:

> **Which governing document authorizes this coefficient for this application?**

A coefficient used in one water-service framework should not automatically be transferred to:

- fuel gas;
- industrial chemicals;
- another material family;
- another jurisdiction;
- another product-standard system.

### Design stress remains conditional

Even after:

\[
\sigma_s = \frac{MRS}{C}
\]

the result is not automatically the final project allowable stress.

Additional service-specific treatment may still be required for:

- temperature;
- duration;
- chemical environment;
- pressure cycling;
- application-specific requirements.

---

## 12.9 Standard Dimension Ratio — SDR

The **Standard Dimension Ratio** describes pipe geometry.

\[
SDR = \frac{d_n}{e_n}
\]

where:

- \(d_n\) = nominal outside diameter;
- \(e_n\) = nominal wall thickness,

using the definitions of the applicable product convention.

SDR is dimensionless.

For the same nominal outside diameter:

- lower SDR → thicker wall;
- higher SDR → thinner wall.

For example:

- SDR 11 is thicker than SDR 17 at the same nominal outside diameter.

SDR alone does not identify:

- material;
- pressure rating;
- application;
- allowable temperature;
- chemical suitability.

It is a geometry classification.

---

## 12.10 Equation Applicability Gate

Before using the conventional SDR pressure equation, confirm all of the following.

- Is the pipe a homogeneous pressure-resisting thermoplastic wall for which the governing relationship applies?
- Are the diameter and wall-thickness definitions consistent with the applicable product standard?
- Is the material classification valid?
- Is the selected design stress valid for the intended application?
- Is the product-standard framework identified?
- Are reference conditions understood?
- Is another governing requirement more restrictive?
- Is the equation being applied to straight pressure pipe rather than local geometry that requires separate treatment?

If these conditions are not established, the engineer should not use the equation merely because \(SDR\), \(MRS\), and pressure values are available.

The simple relationship should not automatically be applied to:

- lined piping;
- multilayer systems;
- fibre-reinforced composites;
- non-standard fabricated geometry;
- systems governed by a different design convention.

---

## 12.11 Pressure, Hoop Stress, and SDR Relationship

For the conventional ISO-style homogeneous pressure-pipe relationship:

\[
\sigma = \frac{p(d_n-e_n)}{2e_n}
\]

where:

- \(\sigma\) = hoop stress;
- \(p\) = internal pressure;
- \(d_n\) = nominal outside diameter;
- \(e_n\) = nominal wall thickness.

Using:

\[
SDR = \frac{d_n}{e_n}
\]

the equation becomes:

\[
\sigma = \frac{p(SDR-1)}{2}
\]

Rearranging:

\[
p = \frac{2\sigma}{SDR-1}
\]

Substituting the design stress:

\[
\sigma_s = \frac{MRS}{C}
\]

gives:

\[
p = \frac{2MRS}{C(SDR-1)}
\]

If MRS is in MPa, the resulting pressure is in MPa.

Using:

\[
1\;MPa = 10\;bar
\]

the pressure in bar may be expressed as:

\[
p_{bar} = \frac{20MRS}{C(SDR-1)}
\]

The existing technical review verified this derivation as dimensionally and algebraically consistent.

---

## 12.12 What the SDR Equation Does Not Evaluate

The equation does not independently verify:

- elevated-temperature capability;
- chemical compatibility;
- cyclic loading;
- surge;
- external pressure;
- vacuum;
- buckling;
- local fitting stresses;
- branch geometry;
- flange loading;
- valve loads;
- supports;
- restraints;
- scratches;
- notches;
- ovality;
- installation damage;
- joint quality;
- workmanship;
- component-system rating.

It answers a defined straight-pipe pressure/geometry relationship inside a larger engineering framework.

---

## 12.13 Worked Example — PE100 SDR 11 Reference Water-Service Case

Assume, for an illustrative reference case:

- material class: PE100;
- \(MRS = 10\;MPa\);
- \(C = 1.25\), **where that value is permitted by the applicable water-service framework**;
- SDR = 11;
- appropriate reference conditions.

Then:

\[
p = \frac{2(10)}{1.25(11-1)}
\]

\[
p = \frac{20}{12.5}
\]

\[
p = 1.6\;MPa
\]

Therefore:

\[
p = 16\;bar
\]

This illustrates the familiar relationship between:

- PE100;
- SDR 11;
- PN 16

under the applicable reference water-service convention.

### The example is not a universal design rule

It does **not** establish that:

- every PE100 SDR 11 product is acceptable in every application;
- \(C = 1.25\) is valid for every PE service;
- 16 bar is acceptable at every temperature;
- 16 bar is acceptable for every chemical;
- 16 bar is the allowable system pressure;
- the same rule applies to gas service;
- the same rule applies to another polymer family.

Before project use, the engineer must still verify the actual governing basis.

---

## 12.14 Material Classification, Pipe Classification, and System Pressure

These levels should remain distinct.

### Material classification

Examples:

- MRS;
- PE100.

Describes a qualified material characteristic.

### Pipe/product classification

Examples:

- SDR;
- PN designation;
- applicable product standard.

Describes the qualified product under a defined framework.

### Component rating

Applies to:

- fittings;
- valves;
- flanges;
- couplings;
- instruments;
- transitions;
- fabricated components.

### Project system allowable pressure

The pressure actually permitted for the complete installed system after considering:

- service temperature;
- service duration;
- chemistry;
- operating states;
- transients;
- components;
- joints;
- local geometry;
- project requirements;
- governing code/design framework.

This is the final project-level question.

---

## FIG-012-002 — Classification Level Versus Project Decision

`MATERIAL`
→ MRS / material classification

`PIPE PRODUCT`
→ SDR / PN / product-standard classification

`COMPONENT`
→ fitting / valve / flange rating

`INSTALLED SYSTEM`
→ service-case allowable pressure

Central message:

> **The project system cannot inherit the pipe label without verification.**

---

## 12.15 Nominal Pressure — PN

PN is a standardized nominal pressure designation associated with a component or piping system under defined reference conditions.

It is a useful classification.

It is not automatically:

- MOP;
- design pressure;
- operating pressure;
- test pressure.

PN must be interpreted together with:

- applicable product standard;
- reference temperature;
- material;
- design coefficient;
- component type;
- service basis.

At elevated temperature, the usable pressure capability may be lower than the nominal reference classification.

---

## 12.16 Pressure Terminology Must Be Controlled

Pressure terms are often transferred among:

- process datasheets;
- pipe catalogues;
- stress calculations;
- specifications;
- test procedures.

This is a major source of engineering error.

The project should define its terminology explicitly.

---

## TAB-012-001 — Pressure Terminology and Ownership Map

| Term | General engineering role | Typical source / owner | Must not automatically be treated as |
|---|---|---|---|
| Operating pressure | Expected process operating condition | Process / operations basis | Design pressure |
| Design pressure | Governing pressure condition used in design framework | Design Basis / code methodology | PN |
| PN | Nominal product/system pressure classification at defined reference basis | Product standard | Actual allowable operating pressure |
| MOP | Maximum operating pressure under the applicable framework | Application standard / project basis | Universal synonym for PN |
| Test pressure | Pressure applied during a defined test | Test standard / procedure | Operating pressure |
| Allowable project pressure | Final permitted pressure after project verification | Engineering approval | Catalogue label |

Exact definitions must follow the governing standard for the application.

This table is an interpretation aid, not a replacement for those definitions.

---

## 12.17 Temperature and Service Time

The reference material/product classification is not automatically the complete project pressure-temperature envelope.

Temperature can change:

- long-term material strength;
- creep rate;
- failure mechanism;
- available pressure capability.

The engineer should connect pressure verification to the discrete service cases established in Chapter 6.

Relevant cases may include:

- continuous normal operation;
- intermittent hot operation;
- cleaning;
- startup;
- shutdown;
- temporary operation;
- elevated-temperature transients.

A single average temperature may hide periods that are important to long-term performance.

---

## 12.18 Multiple Pressure-Temperature Cases

When the system experiences several pressure-temperature states, the engineer should not automatically select only:

- maximum pressure;
- maximum temperature;

and combine them unless they are a credible simultaneous case.

Instead, the pressure design should reference the actual service-envelope cases.

One case may govern:

- sustained pressure;

another:

- elevated-temperature exposure;

another:

- surge;

another:

- chemical exposure.

Different mechanisms may therefore have different governing cases.

---

## 12.19 Chemical Environment and Pressure Capability

Chemical compatibility and hydrostatic pressure classification are separate technical questions.

The process fluid may influence material performance through:

- swelling;
- plasticization;
- oxidation;
- additive extraction;
- environmental stress cracking;
- permeation;
- accelerated crack growth.

A chemical-resistance table marked “resistant” does not automatically establish retention of the full nominal pressure classification.

The pressure decision should therefore verify, where relevant:

- compound;
- concentration;
- temperature;
- exposure duration;
- applied stress;
- contaminants;
- purity;
- available product evidence.

---

## 12.20 Static Pressure Versus Cyclic and Transient Service

Long-term hydrostatic classification is primarily a sustained-pressure framework.

Real systems may also experience:

- pump starts;
- pump stops;
- valve cycling;
- surge;
- water hammer;
- pressure pulsation;
- repeated depressurization;
- thermal cycles;
- vibration.

A static pressure calculation does not automatically qualify cyclic service.

The relevant downstream assessment may depend on:

- stress range;
- mean stress;
- cycle count;
- temperature;
- geometry;
- defects;
- environment.

PN and SDR do not replace fatigue or transient assessment where such assessment is required.

---

## 12.21 Components and the Complete Pressure Boundary

The pressure boundary may contain:

- pipe;
- fittings;
- valves;
- flanges;
- branch saddles;
- couplings;
- instruments;
- gaskets;
- transition joints;
- fabricated components.

The usable system pressure cannot exceed the governing limitation of the applicable:

- component;
- joint;
- service case;
- code requirement;
- local geometry.

A PN-labelled pipe does not transfer its classification automatically to every connected component.

---

## 12.22 Local Geometry and Fabrication

The SDR pressure equation describes a cylindrical pipe wall.

It does not fully characterize local stresses in:

- tees;
- reducers;
- elbows;
- fabricated branches;
- flange adapters;
- valve connections;
- nozzles;
- support points;
- anchors;
- rigid transitions.

Standard components may be qualified within a product system.

Non-standard or fabricated geometry may require additional verification.

The project should distinguish:

> **product qualification**

from:

> **engineering verification of project-specific geometry**

---

## 12.23 Joint Integrity Is a Separate Requirement

A valid pipe pressure classification does not prove:

- fusion-joint quality;
- solvent-joint quality;
- flange assembly quality;
- mechanical-joint integrity.

Joint performance depends on:

- qualified system;
- procedure;
- preparation;
- equipment;
- operator;
- environment;
- inspection;
- assembly.

The pressure equation should never be used to conceal an unverified joining basis.

---

## 12.24 External Pressure and Vacuum

Internal-pressure classification does not automatically establish resistance to:

- external pressure;
- vacuum;
- soil pressure;
- groundwater;
- buckling;
- ovality-related instability.

These conditions require separate engineering treatment where relevant.

A pipe with high internal-pressure capability may still be vulnerable to external instability.

---

## 12.25 Test Pressure Is Not Derived Directly from PN

Pressure testing is governed by the applicable:

- test standard;
- product standard;
- project procedure;
- safety requirements.

The test pressure should not be invented by multiplying PN by a convenient factor.

The engineer should separately define:

- test medium;
- test temperature;
- test pressure;
- duration;
- trapped-gas control;
- stabilization;
- acceptance criteria.

Detailed test methodology belongs later in the book.

---

## 12.26 Missing Pressure-Design Evidence

A project may lack:

- validated high-temperature data;
- chemical-service pressure evidence;
- product-standard confirmation;
- current design-coefficient basis;
- cycle-history information;
- component ratings.

These are not reasons to fabricate an answer.

Possible dispositions include:

- obtain manufacturer/product evidence;
- confirm governing standard;
- test;
- bound the service case;
- perform sensitivity analysis;
- apply a controlled assumption;
- open a controlled hold;
- issue CONDITIONAL GO;
- issue NO-GO.

Chapter 7 governs the uncertainty discipline around these decisions.

---

## 12.27 Pressure Verification Record

A project pressure decision should be reconstructable.

A compact record may include:

| Field | Purpose |
|---|---|
| Pressure decision ID | Unique reference |
| Design Basis revision | Governing basis |
| Service-case ID | Pressure-temperature-chemistry state |
| Material classification | MRS / material class |
| Product system | Actual qualified product |
| SDR / geometry | Relevant pipe geometry |
| Design coefficient basis | Governing source |
| Reference product classification | PN / equivalent |
| Temperature/time treatment | Service adjustment basis |
| Chemical-pressure basis | Compatibility / pressure retention evidence |
| Component limits | Governing component ratings |
| Joint basis | Qualification / verification |
| Transient/cyclic assessment | Separate check status |
| External-pressure assessment | Where relevant |
| Evidence status | Verified / provisional / hold |
| Final disposition | GO / CONDITIONAL GO / NO-GO |
| Reopen triggers | Conditions that invalidate decision |

---

## 12.28 Pressure-Design Release Check

Before accepting a project pressure basis, confirm:

- [ ] The exact material classification is known.
- [ ] The actual product system is identified.
- [ ] The applicable product/design framework is identified.
- [ ] The current design-coefficient basis is confirmed.
- [ ] The equation applicability gate is satisfied.
- [ ] SDR uses the correct dimensional definitions.
- [ ] Reference conditions are understood.
- [ ] Relevant service-envelope cases are identified.
- [ ] Elevated-temperature conditions are addressed.
- [ ] Continuous, intermittent, and transient conditions are distinguished.
- [ ] Chemical environment is considered separately.
- [ ] Cyclic and surge conditions are assessed where relevant.
- [ ] Fittings, valves, joints, flanges, instruments, and fabricated parts are checked.
- [ ] External pressure and vacuum are assessed where relevant.
- [ ] Pressure terminology is controlled consistently.
- [ ] Test pressure comes from the proper test basis.
- [ ] Unresolved evidence remains visible.
- [ ] Final disposition is explicit.

---

## 12.29 Common Engineering Mistakes

### Mistake 1 — Treating PE100 as a pressure rating

PE100 is a material classification.

### Mistake 2 — Treating PE100+ as a stronger MRS class

It is not an MRS class above PE100.

### Mistake 3 — Selecting pipe from PN alone

PN is conditional on its product framework and reference basis.

### Mistake 4 — Treating the design coefficient as a universal safety factor

Its application is controlled by the governing design framework.

### Mistake 5 — Ignoring temperature and time

Reference classification does not automatically remain valid for every service condition.

### Mistake 6 — Treating pipe rating as system rating

Components, joints, and local geometry may govern.

### Mistake 7 — Treating static pressure classification as fatigue qualification

Cyclic and transient service may require separate assessment.

### Mistake 8 — Using the SDR equation outside its applicable construction

Lined, multilayer, composite, and specialized systems may require different methods.

### Mistake 9 — Treating chemical resistance as automatic pressure retention

Chemistry can modify material behaviour.

### Mistake 10 — Treating a 50-year classification as guaranteed installed life

The installed system has a broader life-cycle basis.

### Mistake 11 — Treating test pressure as a multiple of PN by habit

The correct test basis comes from the applicable test framework.

### Mistake 12 — Mixing PN, MOP, operating pressure, and design pressure

Pressure terminology must remain controlled.

---

## 12.30 Boundary with Chapters 9–11 and Later Design Chapters

### Chapter 9

Explains:

> **why thermoplastics exhibit time-dependent behaviour**

### Chapter 10

Explains:

> **how a candidate piping system is selected and approved**

### Chapter 11

Explains:

> **the characteristic behaviour of the main plastic-piping families**

### Chapter 12

Explains:

> **how long-term thermoplastic material strength, design stress, and geometry connect to pressure classification and project pressure verification**

Later chapters must still address:

- hydraulic transients;
- fatigue;
- mechanical loads;
- supports;
- flexibility;
- joining;
- inspection;
- testing.

Pressure classification is therefore one part of complete system design.

---

## 12.31 Evidence and Standards Holds

The current chapter source package identifies:

- ISO 9080;
- ISO 12162;
- ISO 4427 series;
- ISO 4437 series;
- ISO 15494;
- ISO 17456;
- PE100+ Association material;
- PPI technical material.

The existing technical review also records that the equation derivation and units have been verified.

Before final lock, the following remain controlled evidence actions:

- verify current product-standard wording and editions;
- complete full-text clause-level terminology review where normative precision matters;
- verify non-PE product-standard examples;
- preserve the distinction between ISO and ASTM/PPI terminology;
- complete independent technical review;
- finalize figures and cross-references.

The Rev 1.0 content revision does not close those final-lock actions.

---

## If You Remember Only One Thing

> **A thermoplastic pressure label is the output of a chain, not the starting point of a design.**

The chain is:

**long-term evidence**

→ **material classification**

→ **design stress**

→ **SDR / geometry**

→ **product pressure classification**

→ **service-case verification**

→ **component and system verification**

→ **project allowable pressure**

**PN is somewhere in the middle of that chain.**

It is not the final engineering answer.

---

## Chapter Summary

Thermoplastic pressure design begins with long-term material behaviour rather than short-term strength.

Long-term pipe-test evidence is evaluated statistically and converted into a material classification such as MRS.

The applicable engineering framework then uses a design coefficient to establish a design stress.

Pipe geometry is represented by SDR.

For the conventional homogeneous thermoplastic pressure-pipe relationship:

\[
p = \frac{2MRS}{C(SDR-1)}
\]

when pressure and stress are expressed in MPa.

The equation is valid only within its applicable design framework.

The resulting product pressure classification remains conditional.

The project must still verify:

- temperature;
- time;
- chemistry;
- cyclic and transient pressure;
- components;
- joints;
- local geometry;
- external pressure;
- governing standards;
- project requirements.

A reliable engineer therefore distinguishes:

> **material classification ≠ pipe pressure classification ≠ system allowable pressure**

The final pressure decision belongs to the complete system and the actual service case.
