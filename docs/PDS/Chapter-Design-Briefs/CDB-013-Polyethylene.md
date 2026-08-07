# CDB-013 — Chapter Design Brief: Polyethylene (PE)

**PDS Baseline:** 1.0
**Status:** Pilot / Reference Chapter Design Brief

## 1. Chapter purpose

Develop Chapter 13 into the reference implementation of the PPE-BoK Development System. The chapter shall explain polyethylene deeply enough to build engineering judgement while also functioning as a practical engineering reference for material selection, pressure design context, qualification, standards navigation, failure mechanisms and system-level decisions.

The chapter is not intended to be a complete joining, stress-analysis, inspection or hydraulic design manual; those subjects are treated elsewhere in the book and are cross-referenced where needed.

## 2. Primary audience

Practicing mechanical, process, piping, materials, reliability, inspection and owner/EPC engineers who need to evaluate or design polyethylene pressure piping systems.

Secondary readers include junior engineers, inspectors, manufacturers and advanced students.

## 3. Engineering problem addressed

Given a defined Design Basis, how should an engineer determine whether a polyethylene pressure piping system is appropriate, how should the material classification and geometry be interpreted, which standards govern the decision, which limitations require additional analysis, and how should the engineer verify that the selected system remains within its qualified engineering envelope?

## 4. Reader outcomes

After completing the chapter, the reader should be able to:

1. Distinguish material behaviour, material classification, product qualification and system design.
2. Explain why long-term behaviour governs PE pressure-piping engineering more than short-term tensile strength.
3. Navigate the standards chain connecting long-term testing, material classification, pipe geometry, product requirements and application-specific design.
4. Interpret MRS, design coefficient / design factor, SDR and pressure designation without confusing one with another.
5. Perform and independently check the core pressure-rating relationships used within the chapter, with stated assumptions and limits.
6. Identify when temperature, chemical environment, cyclic loading, installation damage, slow crack growth or other system conditions invalidate a simple nominal-pressure interpretation.
7. Identify required project inputs before selecting PE grade / classification / SDR.
8. Recognise common misapplications and frame an initial failure-investigation path without assuming that the visible fracture location is the root cause.
9. Document a technically justified material / geometry decision and identify what still requires project-specific engineering or specialist review.

## 5. Design Basis variables to be addressed

The chapter shall make clear that PE selection and pressure interpretation depend, as applicable, on:

- transported fluid / gas and concentration;
- normal, design and upset temperature;
- operating and design pressure;
- pressure cycling / transients;
- intended design life;
- buried / above-ground environment;
- UV and external environment;
- installation method and credible installation damage;
- joining method;
- inspection / repair philosophy;
- regulatory / geographic context;
- applicable product and application standards.

## 6. Standards framework — validation required before publication

The redevelopment shall build a standards map around the following families, subject to direct verification of current editions, scope and exact clause/table references during Standards Validation:

- **ISO 9080** — long-term hydrostatic strength determination / extrapolation methodology for thermoplastic pipe materials.
- **ISO 12162** — classification, designation and design coefficient framework for thermoplastic pressure-piping materials.
- **ISO 4427 series** — PE piping systems for water supply and pressure drainage/sewerage, where applicable.
- **ISO 4437 series** — PE piping systems for gaseous fuels, where applicable.
- **ISO 1167 series** — resistance to internal pressure testing, where applicable.
- **ISO 21307** — PE butt-fusion procedures where relevant to chapter-level joining context.
- Additional national / application standards only where they materially affect engineering interpretation.

The chapter shall avoid vague references such as “the applicable standard” where the governing standard can be identified. Where applicability depends on service, the text shall state what determines the choice.

**Mandatory final rule:** all clause numbers, numerical values, tables, coefficients and standards-derived interpretations introduced during redevelopment must be re-opened and verified against authoritative standards after authoring is complete.

## 7. Core engineering methods / equations

The chapter shall include and number, as appropriate, the core relationships needed to connect material classification to engineering interpretation. At minimum, evaluate inclusion of:

1. Design stress relationship based on MRS and applicable coefficient/factor.
2. SDR definition from nominal outside diameter and nominal wall thickness.
3. Standard pressure relationship linking MRS / design stress and SDR, with clear statement of the standard basis and units.
4. Temperature-dependent pressure / derating treatment where the governing standard provides it.
5. Long-term regression / classification relationships only to the depth necessary for engineering use; the chapter shall explain what the regression output means, not reproduce ISO 9080 methodology unnecessarily.

Every equation shall include symbols, units, assumptions, validity, source basis and common misuse.

## 8. Required engineering assets

### Standards Map
One chapter-level map from long-term material testing → classification → product standard → design / application → joining / inspection.

### Key tables
At minimum develop:

- PE terminology / classification table (e.g. PE80 / PE100 / PE100-RC concepts, with standards status carefully verified).
- MRS / design coefficient / SDR / pressure-relationship reference table where technically justified.
- Design-input checklist.
- “What the pipe marking tells you / does not tell you” table.
- Failure-mechanism / evidence / engineering-response table.

### Worked examples
Normally two substantial examples:

**Example A — Pressure / SDR interpretation**
Given a qualified PE material and defined service, calculate or verify the relevant nominal pressure relationship, explicitly state applicable standard path and show what the arithmetic does not prove.

**Example B — Design decision under changed service conditions**
Start from a Design Basis change such as elevated temperature, cycling or changed service; show which initial nominal classification remains useful, which assumptions must be revisited, and what additional standards / checks become necessary.

### Workflow
One engineering material-selection / verification workflow:

`Design Basis → Applicable standards → Qualified material → Long-term/design stress input → Geometry/SDR → Pressure/temperature verification → Chemical/mechanical/service checks → Joining/installation constraints → Verification → Engineering decision`

### Design Review Checklist
One chapter-end checklist suitable for practical use during design review.

### Visual placeholders
Specify original figures for:

- molecular architecture / semicrystalline structure and engineering consequence;
- slow crack growth concept;
- long-term hydrostatic regression concept;
- test-data → regression → classification → product marking chain;
- PE pipe marking anatomy;
- complete chapter engineering workflow.

No visual is produced during Authoring.

## 9. Investigation roadmap

The exact headings may be refined during Technical Outline, but the chapter should progress approximately through:

1. Why polyethylene became a major pressure-piping material.
2. Which molecular / morphological features determine engineering behaviour.
3. How PE material generations / classifications evolved and what engineers should infer from them.
4. Long-term behaviour, creep, ductile/brittle transition and slow crack growth.
5. Why decades of performance are evaluated using accelerated long-term testing.
6. What regression analysis and lower-confidence behaviour mean to the engineer.
7. How long-term evidence becomes MRS / material classification.
8. How classification, SDR and product standards become pressure designation and pipe marking.
9. How to design / select within a project Design Basis and identify where nominal classifications are insufficient.
10. Failure Lens and engineering decision framework.

Investigations shall build progressively and shall not repeat chapter-level standards maps or introductory explanations.

## 10. Common errors the chapter must explicitly address

- Treating PE100 as a universal statement of suitability.
- Treating PN / nominal pressure as an unconditional allowable operating pressure.
- Confusing MRS, allowable/design stress and pressure rating.
- Comparing SDR without considering material, service, temperature and governing product standard.
- Using short-term tensile data as the primary pressure-design basis.
- Treating qualification of material as qualification of the finished product or system.
- Applying standards outside their scope without identifying the transferability issue.
- Ignoring installation damage / SCG / temperature / cycling because the pipe is nominally pressure-rated.
- Assuming failure next to a weld or fitting proves the weld or fitting is the root cause.

## 11. Out of scope / controlled cross-reference

The chapter shall introduce but not duplicate full treatments of:

- detailed butt-fusion and electrofusion procedure design;
- full pipe-stress / flexibility analysis;
- support-spacing design;
- transient hydraulics / water hammer;
- detailed NDT / inspection qualification;
- complete chemical-resistance databases;
- detailed fracture-surface / fractography methodology.

Where these affect PE decisions, the chapter shall state the engineering consequence and cross-reference the dedicated chapter.

## 12. Success criteria

Chapter 13 is accepted as the PDS reference chapter when:

- the chapter can be opened independently and used by a practicing engineer;
- its engineering content is approximately application-led (target ~60/40 application/explanation, non-binding);
- all material technical claims are traceable;
- the standards path is explicit rather than generic;
- key equations are numbered, sourced, dimensionally checked and bounded by assumptions;
- at least the two planned worked examples are independently recalculated;
- tables and workflows materially reduce engineering effort;
- common misinterpretations are explicitly prevented;
- Technical Review is passed;
- Standards Validation is completed against authoritative source documents after the writing pass;
- the chapter passes the Desk Test and can serve as the template/reference chapter for redevelopment of the remaining manuscript.

## 13. Pilot note

The objective of this pilot is **engineering redevelopment, not wholesale rewriting**. Existing strong explanatory material shall be retained where it supports the approved CDB. Missing standards navigation, calculations, tables, workflows, practical examples, limitations and design-review tools shall be added systematically.
