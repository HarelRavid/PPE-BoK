# Batch 013-H — Navigation, Design Review Checklist and Chapter Closure

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved redevelopment artifact  
**Integration target:** Chapter 13 Rev 1.0  
**PDS baseline:** 1.0 (frozen)

## H1 — Engineering Quick Navigation

You do not need to read this chapter linearly every time you use it.

- **Screening PE as a candidate material:** Investigations **1–4** — behaviour, material characteristics, time dependence and crack-growth considerations.
- **Understanding PE100, MRS, design stress, SDR or pressure designation:** Investigations **5–8** — long-term evidence → classification → design stress → pipe geometry → pressure basis.
- **Selecting PE for an actual project:** Investigation **9** — Design Basis → standards path → material/product → pressure/temperature → service → installation/joining → engineering disposition.
- **Reviewing a PE failure or abnormal condition:** Investigation **10** — observation → hypotheses → evidence → mechanism → engineering response.
- **Checking a completed design:** `CL-013-001` — Chapter 13 Design Review Checklist.

> **Rule of use:** a pipe designation, SDR, PN or catalogue pressure value is an input to the engineering process—not the conclusion of it.

## H2 — CL-013-001 — PE Pressure-Piping Design Review Checklist

| ID | Review question | Required evidence / disposition |
|---|---|---|
| CL-01 | Is the Design Basis sufficiently defined? | Fluid, pressure, temperature, life, environment, installation and operating envelope documented |
| CL-02 | Has the governing standards path been identified? | Material, product, application, joining and project/regulatory standards identified |
| CL-03 | Is the selected PE material classification demonstrated? | Traceable qualification/classification evidence |
| CL-04 | Is product conformity separate from material qualification? | Pipe/fitting/product certification or equivalent evidence |
| CL-05 | Is the long-term strength basis understood and traceable? | Appropriate qualification/regression/classification route identified |
| CL-06 | Is the applicable design coefficient C justified? | Source and application scope recorded; not copied from an unrelated service |
| CL-07 | Has design stress been calculated and independently checked? | `EQ-013-002` calculation, units and rounding basis verified |
| CL-08 | Are SDR and dimensions correctly interpreted? | Product dimensions/SDR verified against the governing product framework |
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

A checked box means **evidence reviewed and acceptable**, not merely that the subject was considered. If an item does not apply, record **N/A with justification**. If a material item remains unresolved, the disposition remains **CONDITIONAL GO** or **NO-GO** rather than silently converting the uncertainty into an assumption.

## H3 — Chapter 13 Engineering Closure

Polyethylene pressure-piping design is not a sequence that begins with PE100 and ends with SDR. It begins with the **Design Basis**.

The engineering chain developed through this chapter is:

`Design Basis → Standards Path → Material Behaviour → Long-Term Evidence → Classification → MRS → C → Design Stress → SDR → Reference Pressure → Service Verification → System Decision`

Each arrow represents an engineering obligation. Skipping one may still produce a plausible number. It does not necessarily produce a justified design.

### What PE100 does — and does not — tell the engineer

A PE material designation provides valuable information about the material-classification framework. It does not, by itself, establish project allowable operating pressure, suitability at project temperature, chemical compatibility, acceptable transient behaviour, fitting or joint capability, installation-damage tolerance, product conformity, or suitability for the intended application.

Likewise, SDR describes geometry. A pressure designation exists within a defined standards context. Pipe marking supports identification and traceability. None individually represents the complete Design Basis.

### Three distinctions to retain

1. **Material capability is not system capability.** A qualified material is necessary, but the finished product, joints, fittings, installation and actual service environment still require engineering verification.
2. **Reference pressure is not automatically allowable operating pressure.** The material/geometry calculation is important, but temperature, service duration, application requirements, components, transients and other Design Basis conditions still have to be applied.
3. **Qualification evidence is not immunity from failure.** Long-term pressure qualification and SCG-resistance evidence demonstrate performance within defined qualification frameworks; they do not make arbitrary defects, poor joints, excessive temperature, incompatible environments or loads outside the qualified envelope acceptable.

## Final engineering decision

A defensible PE selection should allow another competent engineer to reconstruct the reasoning: why the material was selected; which standards govern it; what evidence establishes long-term capability; how design stress was obtained; why the SDR was selected; how pressure capability was calculated; what changed when actual service conditions were applied; how joining, installation and components were addressed; and what assumptions remain.

If those questions can be answered from the design record, the selection is traceable. If they cannot, a correct-looking SDR or pressure calculation is not enough.

## Residual project-specific engineering

Depending on the application, additional work may include transient hydraulic analysis, detailed flexibility/stress analysis, buried-pipe/soil interaction, support and restraint design, detailed chemical compatibility assessment, joining procedure development and qualification, NDE/inspection planning, installation engineering, specialist failure analysis, regulatory qualification, and application-specific code or standard compliance.

The chapter's job is to tell the engineer **when those interfaces have been reached**, not to reproduce every specialist discipline inside the PE chapter.

## Publication Hold Point — Standards Validation Required

Completion of the engineering narrative does not close Chapter 13.

Before publication, every standards-derived statement used in the chapter shall be reviewed against the authoritative applicable edition. The review shall include, at minimum:

`edition and scope → terminology → equations → coefficients → classification values → reference conditions → rounding rules → temperature/time treatment → test/qualification pathways → PE100-RC treatment → product marking → normative wording`

Any discrepancy discovered during this review shall be resolved in favour of the authoritative standard, and affected chapter text, equations, tables and examples shall be corrected before Design Freeze.
