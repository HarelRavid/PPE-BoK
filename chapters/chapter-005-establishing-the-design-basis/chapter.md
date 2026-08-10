# Chapter 5 — Establishing the Design Basis

## Why This Chapter Matters

Every engineering project needs a controlled technical baseline.

Without one, different engineers may perform individually correct calculations against different assumptions, different operating conditions, different standards, or different versions of the same requirement.

The **Design Basis** is the mechanism that prevents this fragmentation.

It brings together the approved technical inputs that define what system is being engineered, under which conditions, according to which requirements and governing sources, and with which assumptions, limitations, and unresolved items.

For industrial plastic piping, the Design Basis must capture more than nominal pressure, temperature, and flow.

It must establish the controlled engineering context against which later material selection, hydraulic design, mechanical design, joining, inspection, testing, operation, maintenance, modification, and failure assessment are evaluated.

> **A technically correct calculation is only as valid as the Design Basis against which it was performed.**

### Reader outcomes

After this chapter, the reader should be able to:

- explain the role of the Design Basis as the controlled technical baseline for a piping system;
- identify the major inputs that must be integrated into it;
- distinguish verified inputs, requirements, assumptions, controlled holds, design criteria, and approved design decisions;
- define ownership, approval, revision, and lifecycle status for a Design Basis;
- control assumptions and unresolved items explicitly;
- identify the governing standards basis and applicable editions;
- determine whether the Design Basis is sufficiently mature for detailed engineering;
- trace requirements through the Design Basis into downstream design decisions;
- recognize when a process, requirement, standard, or design change requires the Design Basis and affected decisions to be reopened.

---

## 5.1 Definition

The Design Basis is the **controlled technical description of the conditions, requirements, assumptions, constraints, governing sources, and design principles that define the intended engineering basis of a piping system**.

It provides the common reference for:

- design;
- procurement;
- construction;
- inspection;
- testing;
- commissioning;
- operation;
- maintenance;
- modification;
- failure investigation;
- life extension.

The central question it answers is:

> **What system are we designing, against which approved technical basis, and under which defined conditions must it remain acceptable?**

The Design Basis is therefore not merely a process datasheet, specification, calculation package, or narrative report.

It is an **integration baseline**.

---

## 5.2 Design Basis Assembly

The Design Basis is built from controlled upstream inputs.

A typical assembly includes:

- system function and boundaries;
- process definition;
- approved engineering requirements;
- service conditions and design envelope;
- governing laws, codes, standards, and specifications;
- equipment and interface constraints;
- project constraints;
- design philosophy;
- assumptions;
- controlled holds;
- design-life expectations;
- inspection and testing philosophy;
- operation and maintenance expectations;
- modification and management-of-change considerations.

These inputs originate from different engineering activities.

They should not be treated as interchangeable.

A verified process condition is not the same as an assumption.

An approved requirement is not the same as a design preference.

A controlled hold is not the same as an accepted design input.

The Design Basis should preserve those distinctions.

---

## FIG-005-001 — Design Basis Assembly and Configuration Control

**Conceptual figure placeholder**

Suggested structure:

`System function / boundary`
+
`Process definition`
+
`Approved requirements`
+
`Service conditions / design envelope`
+
`Codes / standards / specifications`
+
`Project constraints / design philosophy`
+
`Assumptions / controlled holds`
+
`Life-cycle requirements`

↓

`DESIGN BASIS BASELINE`

↓

`Material / hydraulic / mechanical / joining / QA / testing / operation decisions`

with two control loops:

`New evidence / process change / requirement change / standards change`
→
`IMPACT REVIEW`
→
`REOPEN AFFECTED DESIGN BASIS ITEMS`

and:

`Revision / approval / supersession`
→
`CONFIGURATION CONTROL`

The purpose of the figure is to show that the Design Basis is both an **integration product** and a **controlled baseline**.

---

## 5.3 Types of Information Inside the Design Basis

A strong Design Basis distinguishes the status and function of the information it contains.

### Verified input

A fact or condition supported sufficiently for the current engineering stage.

Examples may include:

- confirmed process composition;
- approved system boundary;
- validated equipment interface;
- verified site condition.

### Approved requirement

A condition the system must satisfy.

These requirements should already carry the traceability and authority established in Chapter 4.

### Assumption

A provisional input used because final information is not yet available.

An assumption remains an assumption until it is validated, replaced, or invalidated.

### Controlled hold

A material unresolved issue that prevents full closure of the affected decision.

### Governing source

A law, regulation, code, standard, project specification, or other controlled source that defines the applicable engineering basis.

### Design criterion or philosophy

An approved engineering rule used to guide downstream analysis or design choices.

Examples may include:

- required design life;
- inspection philosophy;
- maintenance approach;
- redundancy philosophy;
- defined treatment of abnormal conditions.

### Approved design decision

Some design decisions may become part of the controlled baseline after formal approval.

For example:

- selected system architecture;
- defined interface philosophy;
- approved joining route;
- approved material family.

These categories have different change-control consequences and should not be silently merged.

---

## 5.4 The Design Basis Is Not the Design Envelope

The Design Basis includes the service conditions and design envelope.

It should not duplicate the full technical development of them.

Chapter 6 develops the service conditions and multidimensional design envelope in detail.

Chapter 5 instead establishes that the Design Basis must:

- identify which envelope is governing;
- record the approved basis;
- state relevant assumptions or holds;
- connect the envelope to downstream design decisions.

The distinction is:

> **Chapter 6 defines the envelope. Chapter 5 controls the envelope as part of the approved design baseline.**

---

## 5.5 Operating Conditions and Design Conditions

Operating conditions describe expected service.

Design conditions define the conditions against which the system must be evaluated according to the governing design method and project philosophy.

They are not automatically identical.

A system may normally operate at one pressure and temperature but still require evaluation against another condition because of:

- static head;
- pump shutoff;
- control behaviour;
- startup or shutdown;
- credible upset;
- transient events;
- cleaning;
- testing;
- governing code requirements.

Design conditions should not be created by adding arbitrary margins to nominal operation.

Their basis should be traceable to:

- credible process scenarios;
- approved engineering requirements;
- governing design methods;
- defined project philosophy.

The detailed construction of these combinations belongs in Chapter 6.

---

## 5.6 Explicit Assumptions

All engineering work contains assumptions.

Examples may include:

- production does not exceed a defined capacity;
- fluid concentration remains within a defined range;
- a transient occurs no more frequently than specified;
- supports are installed as designed;
- inspection intervals are maintained;
- cleaning chemicals remain within specified limits.

Assumptions are not defects.

**Hidden assumptions are.**

A material Design Basis assumption should normally include:

- statement;
- basis;
- owner;
- engineering significance;
- validation action;
- current status;
- target closure point;
- consequence if false;
- trigger for reopening affected decisions.

An assumption whose failure would materially invalidate the design deserves more control than a low-significance assumption.

---

## 5.7 Controlled Holds

Some information cannot be closed when the Design Basis is first assembled.

Examples may include:

- unresolved process chemistry;
- pending equipment data;
- incomplete transient definition;
- unresolved standard interpretation;
- missing manufacturer limitation;
- unconfirmed site condition;
- pending test or qualification result.

These should not disappear inside narrative text.

They should be maintained as **controlled holds**.

A controlled hold should state:

- what remains unresolved;
- why it matters;
- which decisions it affects;
- owner;
- required closure evidence;
- current status;
- latest acceptable closure point.

A critical unresolved hold may justify a **conditional design release**.

It does not justify pretending the Design Basis is complete.

---

## 5.8 Applicable Requirements and Governing Sources

The Design Basis should identify the applicable technical authority structure.

This may include:

- governing law;
- regulatory authority;
- design codes;
- product standards;
- installation standards;
- test standards;
- project specifications;
- client or owner requirements;
- manufacturer limitations;
- approved deviations or waivers.

Different documents perform different roles.

A product standard does not necessarily provide the complete design method.

A test standard does not necessarily establish system suitability.

A manufacturer limitation does not automatically replace a governing code requirement.

The Design Basis should therefore identify not only the document, but also its **role in the design**.

---

## 5.9 Standards Edition and Adopted Basis

Where standards materially affect the design, the active Design Basis should identify, as applicable:

- document number;
- edition or year;
- amendment or corrigendum status;
- adopted project edition;
- scope or applicability;
- unresolved standards hold.

A new publication does not silently change the approved engineering basis.

Likewise, a draft standard should not automatically replace the adopted published edition.

A standards change should trigger **impact assessment**.

The engineering question is not:

> “Has a newer standard appeared?”

It is:

> **“Does the changed normative basis affect any approved requirement, Design Basis item, calculation, product selection, or previous engineering decision?”**

---

## 5.10 Ownership and Approval

A Design Basis can function as a baseline only if responsibility is clear.

The project should identify, at an appropriate level:

- Design Basis owner;
- contributors;
- technical reviewers;
- approving authority;
- disciplines responsible for specific inputs.

Ownership does not mean one person creates every technical input.

It means someone is responsible for ensuring that the baseline is coherent, current, and controlled.

Approval means that the organization recognizes a defined revision as the active engineering basis.

---

## 5.11 Design Basis Lifecycle

A useful lifecycle may include:

### Working Draft

Inputs are being assembled and may still change materially.

### Review Candidate

The Design Basis is sufficiently mature for interdisciplinary review.

### Approved Baseline

The Design Basis is formally accepted as the active technical basis for downstream work.

### Superseded

A later approved revision has replaced the previous baseline.

### Reopened / Under Revision

New information or change has materially affected the approved basis and a controlled revision is in progress.

These states help prevent a common project failure:

different disciplines working against different versions of “the same” Design Basis.

---

## 5.12 Minimum Controlled Design Basis Record

A useful Design Basis record should normally identify:

| Field | Purpose |
|---|---|
| System / project identification | Defines what baseline applies |
| System boundary | Defines included scope |
| Revision | Enables configuration control |
| Status | Draft, review, approved, superseded, reopened |
| Owner | Responsible for baseline control |
| Approver | Authority for approved issue |
| Process basis | Links to controlled process definition |
| Approved requirements | Links to governing requirements set |
| Service/design envelope | Identifies governing envelope |
| Codes / standards / editions | Defines normative basis |
| Project constraints | Records significant non-process constraints |
| Design criteria / philosophy | Defines approved engineering principles |
| Assumptions | Records provisional inputs |
| Controlled holds | Records unresolved material issues |
| Life-cycle expectations | Design life, inspection, maintenance, repair |
| Change history | Records material revisions |
| Downstream impacts | Identifies affected design activities |

The exact project document format may vary.

The engineering control principles should not.

---

## 5.13 Traceability Through the Design Basis

The Design Basis should sit inside a visible engineering chain:

> **Source / process fact → Approved requirement → Design Basis item → Design response → Verification evidence**

For example:

A confirmed process temperature range may create an approved temperature-performance requirement.

That requirement is incorporated into the Design Basis.

The Design Basis then governs material selection and pressure-temperature assessment.

The final verification demonstrates that the selected system satisfies the requirement within the approved basis.

Traceability allows an engineer to work backwards as well.

If a material or component selection is challenged, the engineer should be able to determine:

- which Design Basis item drove it;
- which requirement drove that item;
- which process fact or governing obligation drove the requirement.

---

## 5.14 Design Basis Readiness Review

Before detailed engineering or another major design release, the Design Basis should be reviewed for maturity.

A practical readiness review should ask:

- Is the system boundary defined?
- Is the process basis sufficiently mature?
- Are key requirements approved?
- Is the applicable standards basis identified?
- Is the service/design envelope sufficiently defined for the current stage?
- Are critical equipment interfaces known?
- Are major assumptions visible?
- Are controlled holds identified?
- Are owners and closure actions assigned?
- Are life-cycle expectations defined?
- Are required approvals in place?

The Design Basis does not need to contain every final project detail before work can proceed.

But critical uncertainty must be controlled.

Possible readiness outcomes include:

### READY

The basis is sufficiently mature for the intended engineering stage.

### CONDITIONALLY READY

Engineering may proceed with explicit controlled holds and defined limitations.

### NOT READY

Material uncertainties or conflicts prevent defensible downstream work.

This readiness decision should be proportionate to the project and stage.

---

## 5.15 A Living Baseline

Facilities change.

Examples include:

- production increases;
- pumps are replaced;
- control strategies change;
- chemicals change;
- cleaning procedures change;
- repairs alter geometry;
- support arrangements change;
- inspection evidence reveals new degradation;
- standards or project requirements change.

The Design Basis should therefore remain a controlled living baseline.

This does **not** mean continuously rewriting the document whenever a minor field change occurs.

It means material changes are assessed against the baseline and managed through change control.

---

## 5.16 Change Impact and Reopening Decisions

A Design Basis change should trigger an impact review.

A practical workflow is:

1. identify the changed input;
2. identify affected requirements;
3. identify affected Design Basis items;
4. identify downstream calculations, specifications, selections, procedures, or approvals;
5. determine which previous decisions remain valid;
6. reopen affected decisions;
7. perform additional analysis or verification where required;
8. approve the revised basis;
9. supersede the previous baseline where appropriate.

Potential triggers include:

- process change;
- requirement change;
- new operating evidence;
- invalidated assumption;
- closed or newly opened hold;
- equipment substitution;
- material substitution;
- product substitution;
- standards-edition change;
- modified installation condition;
- changed maintenance strategy;
- failure or near miss.

A changed Design Basis does not automatically mean every previous decision is wrong.

It means the impact must be assessed rather than assumed.

---

## 5.17 Consequences of an Incomplete Design Basis

Examples of incomplete-basis failures include:

- selecting material for normal process temperature while ignoring hot cleaning cycles;
- checking steady pressure while omitting credible cyclic or transient service;
- designing supports without considering thermal movement;
- assessing pure-chemical compatibility while overlooking contaminants;
- assuming single-phase service where gas can evolve or solids can precipitate;
- specifying testing without considering trapped gas, material response, or test temperature;
- selecting components without confirming equipment-interface requirements;
- designing a system that cannot be inspected or repaired as required;
- using different standards editions across disciplines without realizing it;
- allowing an unresolved assumption to become a permanent design fact.

These failures are not primarily calculation errors.

They are **baseline-control failures**.

---

## 5.18 Minimum Design Basis Content

A practical Design Basis should normally address:

1. system function;
2. system boundary and interfaces;
3. process definition;
4. approved engineering requirements;
5. operating conditions;
6. design conditions;
7. service/design envelope reference;
8. abnormal and transient scenarios;
9. design life;
10. governing codes, standards, editions, and specifications;
11. project constraints;
12. approved design philosophy;
13. material or cleanliness constraints;
14. equipment/interface requirements;
15. assumptions;
16. controlled holds;
17. installation environment;
18. inspection and testing philosophy;
19. operation and maintenance expectations;
20. repair and modification assumptions;
21. ownership and approvals;
22. revision and status;
23. change history;
24. downstream impact / traceability links.

This is a controlled baseline checklist.

It is not a requirement that every project use the same document template.

---

## 5.19 Common Mistakes

Common Design Basis errors include:

- treating nominal process data as the complete basis;
- assembling the Design Basis from uncontrolled documents;
- mixing facts, assumptions, preferences, and requirements without distinction;
- failing to identify the active standards edition;
- leaving unresolved issues buried in narrative text;
- issuing detailed design before the basis is sufficiently mature;
- allowing different disciplines to use different revisions;
- using arbitrary design margins without documented basis;
- updating the Design Basis without assessing downstream impact;
- assuming a new standard edition automatically invalidates all prior work;
- failing to reopen decisions after a material process or requirement change;
- treating the Design Basis as a one-time project deliverable rather than a controlled life-cycle baseline.

---

## 5.20 Handoff to the Design Envelope

The first five chapters now establish the engineering chain:

> **System definition → Decision process → Process definition → Engineering requirements → Design Basis**

The next chapter, **Chapter 6 — Service Conditions and the Design Envelope**, develops one of the most important technical elements contained within that Design Basis.

Chapter 6 asks:

> **What complete set and combination of physical, chemical, mechanical, environmental, and time-dependent conditions can credibly act on the system?**

Chapter 5 controls that answer inside the approved baseline.

Chapter 6 develops it in technical detail.

---

## Chapter Summary

The Design Basis is the controlled technical baseline of the piping system.

It integrates:

- system boundaries;
- process definition;
- approved requirements;
- service conditions;
- governing standards;
- constraints;
- assumptions;
- controlled holds;
- design philosophy;
- life-cycle expectations.

A strong Design Basis has:

- defined ownership;
- formal approval;
- identifiable revision;
- controlled lifecycle status;
- standards-edition control;
- explicit assumptions;
- visible unresolved holds;
- requirement traceability;
- readiness review;
- change-impact logic.

Its purpose is not merely to document what the engineering team once believed.

Its purpose is to ensure that every important downstream decision is made against the **same controlled technical basis**.

And when that basis changes materially, the affected engineering decisions must be reopened.
