# Chapter 4 — Defining Engineering Requirements

## Why This Chapter Matters

The quality of an engineering solution is limited by the quality of the requirements on which it is based.

A sophisticated design built on incomplete, ambiguous, conflicting, or unverified requirements can still be fundamentally wrong.

Many piping failures begin before material selection or calculation, when important operating conditions, maintenance needs, environmental exposures, regulatory obligations, or future operating cases are omitted or misunderstood.

Chapter 3 established the process definition.

This chapter performs the next step:

> **Convert process facts, governing obligations, project needs, and engineering constraints into explicit requirements that can be designed against and verified.**

A requirement is not merely a sentence in a specification.

It is a **controlled engineering object** with a source, meaning, authority, verification route, status, and downstream consequence.

### Reader outcomes

After this chapter, the reader should be able to:

- distinguish a requirement from a design decision, target, preference, assumption, or unresolved hold;
- write engineering requirements that are clear, bounded, traceable, and verifiable;
- identify the source, owner, and authority behind a requirement;
- recognize legitimate prescriptive requirements versus premature unsupported solution choices;
- derive engineering requirements from process facts, interfaces, and constraints;
- resolve requirement conflicts in a controlled way;
- define how a requirement will be verified at the time it is created;
- build a traceable chain from source to requirement to design response to verification;
- control requirement status through approval, change, supersession, and waiver;
- recognize when a changed requirement must reopen the Design Basis and downstream engineering decisions.

## 4.1 What Engineering Requirements Are

Engineering requirements describe what the piping system **must accomplish, satisfy, withstand, enable, or prevent** throughout its intended life.

They establish the technical conditions against which design, procurement, construction, testing, commissioning, operation, inspection, maintenance, repair, and modification can be evaluated.

A requirement answers:

> **What outcome, condition, limit, or capability must be satisfied?**

A design decision answers:

> **Which technical solution is selected to satisfy that requirement?**

For example:

> “The system shall transport 25 m³/h of 30 wt.% sodium hydroxide between 20°C and 65°C without unacceptable leakage over the defined design life.”

is a requirement.

> “The system shall be PE100.”

may be a design choice that still requires justification.

However, a prescriptive statement such as “the system shall use a specific material or technology” can also be a legitimate requirement **if the prescription itself comes from an identifiable governing source**, such as:

- law;
- regulation;
- adopted code;
- owner standard;
- qualified technology basis;
- interface constraint;
- approved project decision.

The problem is therefore not prescription itself.

The problem is **premature or unsupported prescription**.

## 4.2 The Requirements Chain

The engineering sequence developed so far is:

> **Process fact / obligation → Requirement → Design response → Verification evidence → Engineering disposition**

This chain matters because each stage answers a different question.

### Process fact or obligation

What is true, expected, imposed, or required by the process or governing environment?

### Requirement

What must the piping system therefore satisfy?

### Design response

What technical choice, calculation, feature, procedure, or control is used to satisfy the requirement?

### Verification evidence

What evidence demonstrates that the design response actually satisfies the requirement?

### Disposition

Is the requirement satisfied, conditionally satisfied, unresolved, or not satisfied?

A strong engineering record allows another engineer to reconstruct this chain.

## FIG-004-001 — Requirements Definition and Traceability Workflow

**Conceptual figure placeholder**

Suggested structure:

`Process fact / regulation / standard / owner need / interface / lesson learned`
↓  
`Requirement statement`
↓  
`Requirement quality check`
↓  
`Requirement approval / status`
↓  
`Design response`
↓  
`Verification method`
↓  
`Verification evidence`
↓  
`Requirement disposition`

with side loops for:

`Conflict / ambiguity / missing authority`
→  
`Resolve or place on controlled hold`

and:

`Requirement change`
→  
`REOPEN DESIGN BASIS AND AFFECTED DECISIONS`

The purpose of the figure is to communicate one principle:

> **A requirement is not complete until its source, verification, status, and downstream impact are visible.**

## 4.3 Sources of Requirements

Requirements may originate from many sources, including:

- process and production needs;
- laws and permits;
- regulatory obligations;
- engineering codes;
- product or application standards;
- client and corporate specifications;
- process-safety studies;
- environmental constraints;
- equipment interfaces;
- operations philosophy;
- maintenance philosophy;
- quality and inspection strategy;
- previous failures;
- lessons learned;
- procurement constraints;
- space constraints;
- schedule constraints;
- approved project decisions.

These sources do not all carry the same authority.

### 4.3.1 Requirement authority

A useful distinction is:

#### Mandatory requirement

A requirement imposed by law, regulation, mandatory code, adopted safety rule, or other binding authority.

#### Adopted project or owner requirement

A requirement formally imposed by the project, owner, or contract within the applicable authority structure.

#### Derived engineering requirement

A requirement created by engineering analysis from an upstream fact, constraint, or interface condition.

#### Manufacturer constraint

A limitation or condition applicable to a particular product, system, or procedure within its valid scope.

#### Target or objective

A desired performance outcome that may be optimized or traded where allowed.

#### Stakeholder preference

A preferred solution or attribute that does not carry mandatory technical authority unless formally adopted.

These categories should not be silently blended.

## 4.4 Requirement Types Versus Assumptions and Holds

Not every important statement in an engineering record is a requirement.

A controlled requirements process should distinguish at least the following.

### Mandatory requirement

Must be satisfied when applicable.

### Engineering requirement

A technical condition that the design must satisfy, whether externally imposed or derived by engineering.

### Target or objective

A desired outcome that may guide optimization but is not automatically mandatory.

### Preference

A stakeholder or project preference that may influence selection if higher-priority requirements remain satisfied.

### Assumption

A provisional input accepted for the current stage but still dependent on confirmation.

### Controlled hold

A material issue that cannot yet be resolved with sufficient evidence.

The distinction matters because an assumption should not be disguised as a requirement, and a preference should not silently become mandatory.

Likewise, a mandatory requirement should not be downgraded into a preference simply because compliance is inconvenient.

## 4.5 Requirement Anatomy — Minimum Requirement Record

An important requirement should have enough information that another competent engineer can understand what it means and how it will be closed.

A practical minimum record may include:

| Field | Purpose |
|---|---|
| Requirement ID | Unique identification |
| Requirement statement | What must be satisfied |
| Type / category | Functional, performance, safety, operational, etc. |
| Source | Where the requirement came from |
| Owner / authority | Who controls or approves it |
| Rationale / derived basis | Why it exists |
| Applicable conditions | When and where it applies |
| Verification method | How compliance will be demonstrated |
| Status | Proposed, approved, hold, superseded, etc. |
| Downstream impact | Which Design Basis or design items it affects |
| Change trigger | What change would require review |

Not every small requirement needs a large administrative record.

The record should be proportionate to the engineering significance.

But critical requirements should never exist only as informal memory.

## 4.6 Requirement Quality

A technically useful requirement should normally pass a simple quality test.

It should be:

### Identifiable

The requirement can be uniquely referenced.

### Clear

Its meaning is sufficiently unambiguous for the decision being made.

### Bounded

The conditions, system segment, operating state, or scope are clear.

### Verifiable

There is a credible way to demonstrate compliance.

### Traceable

Its source or derived basis is known.

### Correctly scoped

It is written at the appropriate level of abstraction.

### Singular enough to assess

A requirement should not combine so many unrelated obligations that compliance becomes impossible to evaluate.

### Free of hidden assumptions

Important assumptions should be visible rather than embedded inside the wording.

### Consistent with higher-priority requirements

It should not contradict a governing requirement without controlled resolution.

A requirement that fails these tests may still look professional on paper.

It is not yet a strong engineering requirement.

## 4.7 Functional Requirements

Functional requirements describe **what the system must do**.

Examples include:

- transport the required medium and flow;
- isolate equipment safely;
- permit draining;
- permit venting;
- permit flushing;
- permit sampling;
- prevent unacceptable leakage;
- prevent unacceptable contamination;
- support startup and shutdown;
- support cleaning and maintenance;
- allow defined future expansion.

Functional requirements are strongest when the required function can be checked.

For example:

> “The system shall permit complete isolation of Pump P-101 for maintenance without shutting down the parallel operating train.”

is more useful than:

> “Maintenance access shall be good.”

## 4.8 Performance Requirements

Performance requirements define **how well the system must perform**.

They may include:

- pressure capability;
- temperature capability;
- required flow;
- acceptable pressure loss;
- leakage criteria;
- design life;
- availability;
- allowable movement;
- allowable deflection;
- cleanliness limits;
- purity limits;
- inspection intervals;
- reliability targets;
- containment performance.

Performance requirements should be tied to the conditions under which they apply.

A pressure requirement without a temperature basis may be incomplete.

A design-life requirement without the relevant service envelope may also be incomplete.

## 4.9 Environmental Requirements

The external environment can govern long-term performance.

Relevant requirements may address:

- minimum ambient temperature;
- maximum ambient temperature;
- solar exposure;
- ultraviolet exposure;
- rain;
- humidity;
- marine atmosphere;
- external chemical vapours;
- burial;
- groundwater;
- soil movement;
- traffic loads;
- wind;
- seismic loads;
- snow;
- ice;
- fire exposure;
- mechanical impact;
- accessibility for inspection and repair.

Environmental requirements should be connected to the actual installation condition rather than copied generically from another project.

## 4.10 Operational Requirements

Requirements must reflect how the facility will actually operate.

Relevant conditions may include:

- continuous service;
- intermittent service;
- batch operation;
- startup frequency;
- shutdown frequency;
- pressure cycles;
- temperature cycles;
- cleaning procedures;
- sanitation procedures;
- pump behaviour;
- control-valve behaviour;
- process interruptions;
- emergency operating states;
- defined future production changes.

Cumulative cycling can govern some damage or performance mechanisms and should therefore be specified where relevant.

It is not automatically the governing condition for every system.

## 4.11 Maintenance and Inspection Requirements

Maintenance and inspection requirements should be defined early enough to influence the design.

They may include:

- access for inspection;
- access for repair;
- replaceability of valves;
- replaceability of instruments;
- isolation provisions;
- drainage provisions;
- availability of fusion equipment;
- availability of qualified personnel;
- spare-parts strategy;
- transition-component strategy;
- calibration requirements;
- test requirements;
- documentation;
- traceability;
- acceptable downtime.

A low-cost installation can become an expensive asset if maintainability is ignored.

Maintenance requirements are therefore not “later operational details.”

They can be design inputs.

## 4.12 Safety Requirements

Safety extends beyond pressure containment.

Depending on the service, requirements may address:

- toxic release;
- corrosive release;
- fire;
- flammability;
- static electricity;
- personnel exposure;
- impact;
- mechanical damage;
- emergency isolation;
- secondary containment;
- environmental release;
- stored energy during testing;
- stored energy during operation.

Safety requirements may arise from several sources and may have different authority levels.

Their precedence and verification should therefore remain explicit.

## 4.13 Derived Requirements

Many engineering requirements are not handed directly to the engineer.

They are **derived**.

A derived requirement is created when engineering analysis converts an upstream fact, interface, or constraint into a technical requirement.

Examples include:

- a process flow target deriving an acceptable pressure-loss requirement;
- an equipment nozzle-load limit deriving a flexibility or support requirement;
- a contamination limit deriving material, cleaning, and traceability requirements;
- a maintenance philosophy deriving isolation and drainability requirements;
- an external traffic condition deriving burial or protection requirements;
- a credible transient deriving a pressure or mechanical assessment requirement.

Derived requirements should receive the same traceability discipline as externally imposed requirements.

The derivation should be visible enough that another engineer can understand:

> **Why does this requirement exist?**

## 4.14 Conflict and Precedence Resolution

Requirements can conflict.

For example:

- a project specification may prescribe one solution while a mandatory code imposes another constraint;
- a maintenance preference may conflict with an equipment interface;
- a supplier limitation may conflict with the process envelope;
- two project documents may define different acceptance criteria.

A conflict should not be resolved by silently selecting the preferred source.

A controlled workflow is:

1. identify the conflicting requirements;
2. identify the source and authority of each;
3. confirm applicability and edition where relevant;
4. determine whether one source has governing precedence;
5. determine whether both can be satisfied;
6. assess whether clarification, deviation, waiver, or redesign is required;
7. obtain approval from the appropriate authority;
8. document the final disposition;
9. update affected requirements and downstream engineering records.

If the conflict cannot yet be resolved, the correct state is a **controlled hold**.

Not an undocumented compromise.

## 4.15 Verification Is Part of Requirement Definition

A requirement is stronger when the verification route is considered at the time the requirement is created.

Possible verification methods include:

- calculation;
- engineering analysis;
- document review;
- certification review;
- inspection;
- testing;
- qualification record;
- commissioning check;
- operational demonstration;
- independent review;
- combined evidence.

The chosen route should match the type of requirement.

For example:

- a pressure-loss requirement may be verified by calculation and commissioning data;
- a material-identification requirement may be verified by documentation and inspection;
- a joining-qualification requirement may be verified through procedure and qualification records;
- an accessibility requirement may require design review and physical inspection.

This connects directly to the verification categories established in Chapter 2.

## 4.16 Requirements Traceability

A defensible design should allow the engineering chain to be followed in both directions.

A useful model is:

> **Source / process fact → Requirement → Design response → Verification evidence → Disposition**

For example:

| Source / fact | Requirement | Design response | Verification |
|---|---|---|---|
| High process temperature | System shall remain suitable over defined temperature envelope | Material, geometry and component selection | Design review + supporting qualification evidence |
| Aggressive chemistry | All wetted materials and joints shall be compatible with defined fluid range | Material/joint selection | Compatibility review |
| Frequent maintenance | Isolation and access shall permit defined maintenance activity | Valve/isolation/layout design | Drawing review + field inspection |
| Abrasive slurry | System shall manage defined solids service within acceptable wear strategy | Velocity/geometry/material/inspection plan | Calculation + inspection strategy review |

Traceability supports:

- design review;
- procurement;
- change management;
- commissioning;
- maintenance;
- modification;
- failure investigation.

If a final design choice cannot be traced back to a requirement, the engineer should ask whether the choice is actually necessary or whether the requirement record is incomplete.

## 4.17 Requirement Status and Lifecycle

Requirements evolve through the project and operating life.

Useful status categories may include:

### Proposed

The requirement has been identified but is not yet formally approved.

### Approved

The requirement is accepted as part of the controlled engineering basis.

### Controlled hold

The requirement or its governing basis is unresolved and blocks or conditions downstream work.

### Superseded

The requirement has been replaced by an approved later requirement.

### Waived with authority

The requirement has been formally waived by an authority permitted to do so.

A waiver should not be assumed merely because a requirement is difficult or expensive to meet.

### Invalidated

The basis for the requirement is no longer valid.

Status control prevents obsolete or provisional requirements from remaining active by accident.

## 4.18 Change and Impact Assessment

Requirements change.

Production targets change.

Chemicals change.

Equipment changes.

Regulations change.

Operating philosophy changes.

Maintenance strategy changes.

A requirement change should therefore not be treated as a document-editing exercise alone.

The engineer should ask:

- Which Design Basis items depend on this requirement?
- Which calculations depend on it?
- Which materials or components depend on it?
- Which interfaces are affected?
- Which procurement decisions are affected?
- Which verification evidence is no longer valid?
- Which previous decisions must be reopened?

The rule is:

> **A material requirement change reopens the affected Design Basis elements and downstream engineering decisions.**

Change control therefore includes both updating the requirement and assessing its consequences.

## 4.19 Requirements and the Design Basis

The boundary between this chapter and the next is deliberate.

Chapter 3 asks:

> **What is true or credibly expected about the process?**

Chapter 4 asks:

> **What must the piping system satisfy because of those facts and governing obligations?**

Chapter 5 asks:

> **What complete technical basis governs the design?**

The controlled requirements set produced here becomes one of the major inputs to the Design Basis.

It is not yet the complete Design Basis.

The Design Basis also integrates:

- process conditions;
- assumptions;
- constraints;
- governing codes and standards;
- operating philosophy;
- design conditions;
- engineering boundaries;
- open items.

## 4.20 Common Mistakes

Common requirements errors include:

- beginning detailed design before requirements are sufficiently defined;
- confusing a solution with a requirement;
- treating every prescriptive statement as automatically valid;
- rejecting a legitimate governing prescription merely because it is prescriptive;
- omitting the source or authority of a requirement;
- failing to distinguish a preference from a mandatory requirement;
- disguising an assumption as a requirement;
- failing to define how compliance will be verified;
- combining several unrelated obligations into one untestable requirement;
- omitting transients, cleaning, or maintenance conditions;
- failing to control conflicting requirements;
- failing to update requirement status;
- continuing to use superseded requirements;
- changing a requirement without reopening affected downstream decisions.

## 4.21 Minimum Requirements Review

Before the requirements set is passed into the Design Basis, the engineer should be able to answer:

- Are the important requirements uniquely identifiable?
- Is the source of each material requirement known?
- Is the authority clear?
- Are assumptions separated from requirements?
- Are requirements clear enough to design against?
- Are applicable conditions defined?
- Are verification methods identified?
- Are derived requirements traceable to their basis?
- Are conflicts resolved or placed on controlled hold?
- Are mandatory requirements distinguished from targets and preferences?
- Are statuses current?
- Are change impacts understood?

If the answer to a material question is no, the requirements set may not yet be ready for design integration.

## Chapter Summary

Engineering requirements define what the piping system must accomplish or satisfy.

A strong requirement is not merely a sentence.

It is a controlled engineering object with:

- identity;
- source;
- authority;
- technical meaning;
- applicability;
- verification route;
- status;
- traceability;
- change impact.

The engineer must distinguish among:

- mandatory requirements;
- engineering requirements;
- targets;
- preferences;
- assumptions;
- controlled holds.

Requirements should be clear, bounded, verifiable, traceable, and free of hidden assumptions.

Derived requirements should be controlled just as carefully as externally imposed requirements.

Conflicts should be resolved explicitly.

Verification should be planned early.

And when a requirement changes, affected downstream decisions must be reopened.

The next chapter, **Chapter 5 — Establishing the Design Basis**, integrates the approved requirements with process conditions, assumptions, constraints, governing standards, operating philosophy, and design conditions into the controlled technical foundation for the piping system.
