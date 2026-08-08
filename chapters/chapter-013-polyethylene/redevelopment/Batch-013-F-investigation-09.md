# Batch 013-F — Investigation 9

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved redevelopment artifact  
**Integration target:** Chapter 13 Rev 1.0  
**PDS baseline:** 1.0 (frozen)

> Standards-validation note: this Investigation defines an engineering integration workflow. Any numerical coefficient, derating rule, product requirement, joining requirement or application-specific acceptance criterion used during final integration shall be verified against the current authoritative governing standard before publication.

# Investigation 9 — How Should an Engineer Select PE for a Real Design Basis?

A PE design decision should not begin with a catalogue pressure rating.

It should begin with a defined Design Basis and end with a documented engineering disposition.

The role of this Investigation is to integrate the previous material, classification and pressure-design logic into a practical decision path.

The full workflow is:

`Design Basis → Applicable standards → Qualified material → Long-term/design-stress basis → Geometry/SDR → Pressure/temperature verification → Chemical/mechanical/service checks → Joining/installation constraints → Verification → Engineering decision`

## 9.1 Step 1 — Freeze the Design Basis before selecting the pipe

The engineer should establish, as applicable:

- transported fluid or gas and concentration;
- normal, design and upset temperature;
- operating and design pressure;
- pressure cycling and credible transients;
- intended service life;
- buried or above-ground installation;
- UV / external environment;
- joining method;
- installation method and credible damage;
- inspection / repair strategy;
- regulatory and geographic context;
- governing product/application standard.

If these are not sufficiently defined, material or SDR selection is **provisional**.

This is important because “PE100 SDR 11” is not a Design Basis. It is an output candidate.

## 9.2 Step 2 — Determine the standards path before applying coefficients

The engineer should identify:

1. the material-classification framework;
2. the governing product standard;
3. the application/service standard, where separate;
4. the relevant joining and qualification standards;
5. project/regulatory requirements that modify or supersede the generic product basis.

This prevents one of the most common errors in plastic piping design: taking a valid equation or coefficient from the wrong standards context.

A coefficient, derating factor or PN value can be perfectly correct inside its own scope and still be wrong for the project.

## 9.3 Step 3 — Verify material classification and product qualification separately

The engineer should ask two different questions:

**Material question:** Does the PE compound have the required long-term classification and associated qualification evidence?

**Product question:** Does the actual pipe/fitting/valve product conform to the governing product standard and required dimensional / performance class?

These are not the same question.

A qualified resin does not automatically qualify:

- the extrusion process;
- the finished pipe;
- the fitting;
- the joint;
- or the installed system.

## 9.4 Step 4 — Establish the reference pressure basis

Use the chain developed in Investigations 7–8:

\[
MRS \rightarrow C \rightarrow \sigma_s \rightarrow SDR \rightarrow p_{reference}
\]

At this point the engineer has a **reference pressure basis**.

Not yet a project allowable operating pressure.

The distinction should remain explicit in the calculation sheet. A useful output label is:

> **Reference pressure basis — service verification pending**

rather than simply “Allowable Pressure”.

## 9.5 Step 5 — Reopen temperature and service duration

Temperature is not simply a convenience factor added at the end. For PE it directly affects time-dependent behaviour.

The correct question is therefore not:

> “What derating factor do I multiply by?”

but:

> **“What does the governing standards path require for this temperature and service-duration combination?”**

The calculation may require a factor, a table, a different allowable stress basis, or another standards-specific treatment. One method should not be universalized across all PE applications.

**Standards Validation Hold Point:** all numerical temperature factors and service-life treatments must be verified against the current authoritative standard actually governing the application.

## 9.6 Step 6 — Verify chemical and environmental compatibility

Pressure qualification does not establish chemical compatibility.

The engineer should consider the actual environment:

`fluid identity + concentration + temperature + exposure time + stress state`

rather than asking only:

> “Is PE chemically resistant to this chemical?”

Compatibility may be influenced by concentration, temperature, mixtures, contaminants, permeation, environmental stress effects, cleaning chemicals and external exposure.

The purpose here is not to recreate a chemical-resistance database.

The engineering decision is:

> **If compatibility is material to the design, trace it to an appropriate data source and confirm that the test/service conditions are transferable to the project.**

Detailed compatibility assessment belongs in the relevant dedicated material/process-fluid treatment.

## 9.7 Step 7 — Treat cycling and transients as additional loads

A nominal pressure relationship is fundamentally a steady/reference pressure calculation.

The Design Basis may also contain:

- pump start/stop events;
- valve closure;
- pressure pulsation;
- compressor effects;
- thermal cycling;
- occasional upset pressure;
- water hammer / surge;
- vacuum conditions.

The chapter should not reproduce transient hydraulics.

Instead, Investigation 9 should enforce the decision gate:

> **If credible transient or cyclic loads materially exceed or alter the nominal pressure history, the nominal SDR/pressure calculation is not the complete mechanical assessment.**

Cross-reference the dedicated transient/fatigue/stress-analysis treatment.

## 9.8 Step 8 — Installation condition can invalidate an otherwise correct material selection

The same PE pipe may experience very different engineering conditions depending on installation.

The engineer should identify whether the system is buried, above ground, restrained, unrestrained, pulled through a bore, ploughed, installed in a casing, supported intermittently, or exposed to traffic / soil movement / settlement.

The design implications can include imposed strain, bending, ovalization, external loading, local damage, restraint forces and thermal movement.

The decision is not:

> “PE is flexible, therefore installation loads are acceptable.”

It is:

> **PE flexibility changes how loads are carried and therefore changes which installation checks govern.**

## 9.9 Step 9 — Joining is a qualification interface, not a footnote

Investigation 9 does not teach butt fusion or electrofusion procedures in detail.

But the engineering decision must still identify:

- joining method;
- procedure qualification;
- equipment requirements;
- operator competence;
- inspection requirements;
- repair philosophy;
- fitting/joint pressure compatibility;
- environmental controls during joining where relevant.

A straight-pipe pressure calculation cannot automatically be transferred to every fitting or fabricated joint.

## 9.10 Step 10 — Make the decision explicit

At the end of the workflow, the engineer should not write simply:

> “PE100 SDR 11 selected.”

The decision record should state something closer to:

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

That turns selection into an auditable engineering decision.

## TAB-013-003 — PE Design Input / Verification Matrix

| Design input | Required question | Evidence / source | Status |
|---|---|---|---|
| Fluid/service | What is transported and at what concentration? | Process Design Basis | Open / Verified |
| Temperature | Normal, design and upset temperatures? | Process / thermal basis | Open / Verified |
| Pressure | Operating, design and transient pressure? | Hydraulic / process basis | Open / Verified |
| Service life | What duration must be justified? | Project basis | Open / Verified |
| Material class | Is the required long-term classification demonstrated? | Material qualification | Open / Verified |
| Product standard | Does the selected pipe/product fall within scope? | Product certification | Open / Verified |
| SDR / dimensions | Does geometry satisfy the reference pressure basis? | Calculation + product data | Open / Verified |
| Chemical compatibility | Is compatibility transferable to actual service? | Validated compatibility evidence | Open / Verified |
| Installation | What mechanical / damage conditions are credible? | Installation specification | Open / Verified |
| Joining | Is the joining route qualified and inspectable? | Joining specification | Open / Verified |
| Transients / cycles | Are additional mechanical checks required? | Design analysis | Open / Verified |
| Final disposition | Are all remaining assumptions controlled? | Engineering review | GO / Conditional / NO-GO |

This table is the working interface between the chapter and an actual design review.

## Worked Example B — The pipe did not change, but the Design Basis did

Initial condition:

- qualified PE100 product;
- selected SDR;
- reference pressure calculation acceptable;
- service at reference/near-reference temperature.

Then the project changes one thing:

> **Operating temperature increases materially.**

The pipe marking is unchanged.

The material designation is unchanged.

The SDR is unchanged.

The nominal geometry is unchanged.

But the engineering decision must be reopened because the temperature/time basis has changed.

The example should walk through:

`original pressure basis`

→ `temperature change`

→ `reopen governing standard`

→ `re-evaluate allowable pressure/service-life basis`

→ `check chemistry because temperature also affects compatibility evidence`

→ `reconfirm fitting/joint limits`

→ `new engineering disposition`

The educational point is not the final numerical factor.

It is:

> **A Design Basis change can invalidate the previous engineering decision even when nothing printed on the pipe changes.**

## 9.11 Engineering decision from Investigation 9

A PE system should be accepted only when the full chain is technically justified:

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

And the key rule:

> **Nominal classification is an input to engineering judgement, not a substitute for it.**

## Standards Validation Hold Points

Before publication, verify against the current authoritative governing standards:

1. application-specific temperature/time treatment;
2. applicable product/application scope and coefficient path;
3. mandatory product, fitting and joining qualification requirements;
4. any numerical pressure, transient or service limitations used during final integration;
5. any normative acceptance criteria added to the final worked example;
6. all standards-derived claims introduced when this redevelopment artifact is integrated into Chapter 13 Rev 1.0.
