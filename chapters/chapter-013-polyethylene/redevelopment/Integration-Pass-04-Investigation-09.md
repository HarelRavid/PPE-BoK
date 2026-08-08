# Integration Pass 04 — Investigation 9

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Integration candidate for author approval  
**Source:** Approved Batch 013-F  
**PDS baseline:** 1.0 (frozen)

> Standards-validation note: this integrated section preserves the approved engineering workflow while keeping numerical coefficients, derating rules, product requirements, joining requirements and application-specific acceptance criteria behind final Standards Validation.

# Investigation 9 — How Should an Engineer Select PE for a Real Design Basis?

A PE design decision should not begin with a catalogue pressure rating. It should begin with a defined Design Basis and end with a documented engineering disposition.

The role of this Investigation is to integrate the material, classification and pressure-design logic developed earlier in the chapter into one auditable project workflow:

`Design Basis → Applicable standards → Qualified material → Product conformity → Long-term/design-stress basis → Geometry/SDR → Reference pressure basis → Temperature/service verification → Chemical/mechanical/service checks → Joining/installation constraints → Verification → Engineering decision`

## 9.1 Freeze the Design Basis before selecting the pipe

The engineer should establish, as applicable:

- transported fluid or gas and concentration;
- normal, design and upset temperature;
- operating and design pressure;
- pressure cycling and credible transients;
- intended service life;
- buried or above-ground installation;
- UV and external environment;
- joining method;
- installation method and credible damage;
- inspection and repair strategy;
- regulatory and geographic context;
- governing product/application standard.

If these are not sufficiently defined, material or SDR selection is **provisional**.

> **PE100 SDR 11 is not a Design Basis. It is an output candidate.**

## 9.2 Determine the standards path before applying coefficients

Before using any design coefficient, pressure designation, temperature treatment or application-specific rule, identify the governing standards chain:

1. material-classification framework;
2. governing product standard;
3. application/service standard, where separate;
4. relevant joining and qualification standards;
5. project/regulatory requirements that modify or supersede the generic product basis.

A coefficient, derating factor or PN value can be valid inside one standards context and still be wrong for the project.

## 9.3 Separate material qualification from product qualification

Ask two different questions:

**Material question:** Does the PE compound have the required long-term classification and associated qualification evidence?

**Product question:** Does the actual pipe, fitting, valve or fabricated component conform to the governing product standard and required dimensional/performance class?

A qualified resin does not automatically qualify the extrusion process, finished pipe, fitting, joint or installed system.

## 9.4 Establish the reference pressure basis

Use the chain developed in Investigations 7–8:

\[
MRS \rightarrow C \rightarrow \sigma_s \rightarrow SDR \rightarrow p_{reference}
\]

At this point the engineer has a **reference pressure basis**, not yet a project allowable operating pressure.

A useful calculation-sheet output label is:

> **Reference pressure basis — service verification pending**

rather than simply “Allowable Pressure”.

## 9.5 Reopen temperature and service duration

Temperature is not a convenience factor applied after the main design calculation. For PE it changes time-dependent behaviour and therefore the service interpretation of the reference pressure basis.

The correct engineering question is not:

> “What derating factor do I multiply by?”

but:

> **“What does the governing standards path require for this temperature and service-duration combination?”**

The answer may involve a factor, a table, a different allowable-stress basis or another standards-specific treatment.

**Standards Validation Hold Point:** all numerical temperature factors and service-life treatments shall be verified against the current authoritative standard actually governing the application.

## 9.6 Verify chemical and environmental compatibility

Pressure qualification does not establish chemical compatibility.

Evaluate the actual exposure as a combination of:

`fluid identity + concentration + temperature + exposure time + stress state`

Compatibility may also be affected by mixtures, contaminants, permeation, environmental stress effects, cleaning chemicals and external exposure.

> **If compatibility is material to the design, trace it to an appropriate source and confirm that the evidence is transferable to the actual project conditions.**

The chapter does not reproduce a chemical-resistance database; it defines the decision interface.

## 9.7 Treat cycling and transients as additional loads

A nominal SDR/pressure relationship is a steady/reference pressure calculation.

The Design Basis may also contain pump starts/stops, valve closure, pressure pulsation, compressor effects, thermal cycling, upset pressure, surge/water hammer or vacuum conditions.

> **If credible transient or cyclic loads materially alter the nominal pressure history, the nominal SDR/pressure calculation is not the complete mechanical assessment.**

Detailed transient hydraulics and fatigue/stress analysis belong in their dedicated treatments.

## 9.8 Installation condition can invalidate an otherwise correct material selection

The same PE pipe may behave very differently depending on whether it is buried, above ground, restrained, unrestrained, pulled through a bore, ploughed, installed in casing, supported intermittently, or exposed to traffic, settlement or soil movement.

Relevant effects can include imposed strain, bending, ovalization, external loading, local damage, restraint forces and thermal movement.

The correct conclusion is not:

> “PE is flexible, therefore installation loads are acceptable.”

It is:

> **PE flexibility changes how loads are carried and therefore changes which installation checks govern.**

## 9.9 Joining is a qualification interface, not a footnote

This chapter does not teach detailed butt-fusion or electrofusion procedures. It does require the engineer to identify:

- joining method;
- procedure qualification;
- equipment requirements;
- operator competence;
- inspection requirements;
- repair philosophy;
- fitting/joint pressure compatibility;
- environmental controls during joining where relevant.

A straight-pipe pressure calculation cannot automatically be transferred to every fitting or fabricated joint.

## 9.10 TAB-013-003 — PE Design Input / Verification Matrix

| Design input | Required question | Evidence / source | Status |
|---|---|---|---|
| Fluid/service | What is transported and at what concentration? | Process Design Basis | Open / Verified |
| Temperature | Normal, design and upset temperatures? | Process / thermal basis | Open / Verified |
| Pressure | Operating, design and transient pressure? | Hydraulic / process basis | Open / Verified |
| Service life | What duration must be justified? | Project basis | Open / Verified |
| Material class | Is the required long-term classification demonstrated? | Material qualification | Open / Verified |
| Product standard | Does the selected product fall within the governing scope? | Product certification | Open / Verified |
| SDR / dimensions | Does geometry satisfy the reference pressure basis? | Calculation + product data | Open / Verified |
| Chemical compatibility | Is compatibility transferable to actual service? | Validated compatibility evidence | Open / Verified |
| Installation | What mechanical/damage conditions are credible? | Installation specification | Open / Verified |
| Joining | Is the joining route qualified and inspectable? | Joining specification | Open / Verified |
| Transients / cycles | Are additional mechanical checks required? | Design analysis | Open / Verified |
| Final disposition | Are all remaining assumptions controlled? | Engineering review | GO / CONDITIONAL GO / NO-GO |

This matrix is the working interface between the chapter and an actual design review.

## 9.11 Worked Example B — The pipe did not change, but the Design Basis did

### Initial condition

Assume the project has:

- a qualified PE100 product;
- a selected SDR;
- an acceptable reference pressure calculation;
- service at or near the original reference temperature basis.

Now change one project condition:

> **Operating temperature increases materially.**

The pipe marking is unchanged. The material designation is unchanged. The SDR is unchanged. The nominal geometry is unchanged.

The previous engineering decision must still be reopened because the temperature/time basis has changed.

### Decision sequence

`original reference pressure basis`

→ `temperature change identified`

→ `reopen governing product/application standard`

→ `re-evaluate temperature/service-life pressure basis`

→ `recheck chemical compatibility at the new temperature`

→ `reconfirm fitting/joint/component limits`

→ `review transients and installation assumptions if affected`

→ `issue new engineering disposition`

The educational point is not a universal numerical derating factor. It is:

> **A Design Basis change can invalidate the previous engineering decision even when nothing printed on the pipe changes.**

### Example completion rule

The worked example is complete only when the final disposition is explicit:

- **GO** — all required checks remain acceptable;
- **CONDITIONAL GO** — one or more controlled items remain open but are explicitly bounded;
- **NO-GO** — the changed Design Basis is outside the demonstrated product/system envelope or requires redesign.

No numerical temperature factor is introduced here without authoritative standards validation.

## 9.12 Make the final design decision explicit

The design record should not end with:

> “PE100 SDR 11 selected.”

It should record, at minimum:

**Material:** qualified PE class / product  
**Geometry:** selected SDR / dimensions  
**Standards basis:** identified product/application path  
**Reference pressure basis:** calculated and independently checked  
**Temperature/service-life verification:** acceptable / pending  
**Chemical compatibility:** acceptable / pending  
**Transient/cyclic assessment:** acceptable / additional analysis required  
**Installation constraints:** defined  
**Joining/inspection requirements:** defined  
**Residual open items:** listed  
**Decision:** GO / CONDITIONAL GO / NO-GO

That turns material selection into an auditable engineering decision rather than a catalogue selection.

## 9.13 Engineering decision from Investigation 9

A PE system should be accepted only when the complete chain is technically justified:

\[
\boxed{
Design\ Basis
\rightarrow Standards
\rightarrow Material
\rightarrow Product
\rightarrow Geometry
\rightarrow Pressure/Temperature
\rightarrow Service\ Conditions
\rightarrow Installation/Joining
\rightarrow Verification
\rightarrow Decision
}
\]

> **Nominal classification is an input to engineering judgement, not a substitute for it.**

## Standards Validation Hold Points

Before publication, verify against the current authoritative governing standards:

1. application-specific temperature/time treatment;
2. applicable product/application scope and coefficient path;
3. mandatory product, fitting and joining qualification requirements;
4. numerical pressure, transient or service limitations used during final chapter integration;
5. any normative acceptance criteria added to Worked Example B;
6. all standards-derived claims introduced when this section is integrated into Chapter 13 Rev 1.0.

## Integration review decision

**PASS — ready for author approval.**

The integration keeps Investigation 9 as a controlled project-decision workflow, avoids duplicating specialist chemical/transient/joining chapters, and ends in an explicit GO / CONDITIONAL GO / NO-GO disposition rather than an open-ended list of checks.
