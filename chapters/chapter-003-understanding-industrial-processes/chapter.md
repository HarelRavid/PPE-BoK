# Chapter 3 — Understanding Industrial Processes

## Why This Chapter Matters

A piping system cannot be engineered independently of the process it serves.

Material selection, pipe sizing, joining, support design, inspection, maintenance, and operating strategy all originate from process conditions and requirements.

The same material or product may produce very different system outcomes in different services because chemistry, pressure, temperature, phase behaviour, transients, installation, operation, cleaning, maintenance, and equipment interfaces are different.

The engineering task therefore begins before material selection.

It begins by defining the process well enough that downstream engineering requirements can be written, verified, and reopened when the process changes.

### Reader outcomes

After this chapter, the reader should be able to:

- define the process segment and interfaces relevant to a piping decision;
- characterize fluids and all relevant phases across the operating envelope;
- distinguish nominal values from the credible operating envelope;
- capture time, duration, frequency, sequence, and rate of change as process inputs;
- identify local process conditions that may differ from line-average conditions;
- distinguish verified process data from estimates, assumptions, and controlled holds;
- trace process facts into downstream engineering requirements;
- recognize when a process change requires the requirements and Design Basis to be reopened.

## 3.1 The Role of Piping in the Process

Piping connects process equipment and enables the controlled transfer of mass and, in many systems, energy.

Its behaviour can affect:

- pressure;
- flow distribution;
- residence time;
- heat transfer;
- mixing;
- phase distribution;
- contamination;
- equipment performance;
- control behaviour;
- operability.

Piping is therefore part of the process—not merely a utility or connection between equipment items.

A piping decision can influence the process, and a process decision can change the piping requirements.

The two cannot be separated cleanly.

## 3.2 Process First, Piping Second

A disciplined engineering sequence is:

1. define the process objective;
2. define the process segment and system boundary;
3. characterize the fluid and all expected phases;
4. identify operating states and transients;
5. establish the credible process envelope;
6. record the source, maturity, and uncertainty of the process data;
7. identify process-driven engineering implications;
8. convert those implications into controlled engineering requirements;
9. evaluate piping materials and system concepts.

Material selection is therefore an **output of process definition**, not its starting point.

This chapter does not yet select the material, pipe class, SDR, joining method, or support system.

Its purpose is to make sure the engineering team understands the process information those later decisions depend on.

## 3.3 Define the Process Boundary

Before collecting process data, the engineer should define **which part of the process is being described**.

A process definition may apply to:

- one line;
- one equipment-to-equipment transfer;
- one utility branch;
- one distribution network;
- one skid;
- one process area;
- one temporary operating configuration.

The boundary should identify:

- upstream equipment or source;
- downstream equipment or destination;
- relevant branch connections;
- pumps, valves, restrictions, control elements, and instruments;
- drains and vents;
- utility interfaces;
- cleaning and flushing connections;
- temporary service connections;
- connected equipment interfaces;
- operating states included in the definition.

This matters because the conditions at one point in a system may not represent the conditions everywhere else.

A process definition with an unclear boundary can produce technically correct data that are applied to the wrong engineering problem.

## FIG-003-001 — Process Definition to Engineering Requirements

**Conceptual figure placeholder**

Suggested structure:

`Process objective`
↓  
`Process boundary / interfaces`
↓  
`Fluid composition + phase state`
↓  
`Operating states`
↓  
`Pressure / temperature / flow / chemistry / solids / hazards`
↓  
`Time history / duty cycle / transients`
↓  
`Source / owner / evidence status`
↓  
`Credible operating envelope`
↓  
`Process implications`
↓  
`Controlled engineering requirements`
↓  
`Design Basis`

with a return arrow:

`Process change / new evidence`
→  
`REOPEN REQUIREMENTS AND DESIGN BASIS`

The purpose of the figure is to communicate one central principle:

> **Process definition is an engineering input chain, not a list of nominal operating values.**

## 3.4 Process Data Must Be Traceable

A process value should not be treated as complete simply because a number exists.

For every material process input, the engineer should be able to identify, as appropriate:

- **parameter or condition**;
- **value or range**;
- **operating state**;
- **frequency or duration**;
- **source or owner**;
- **evidence status**;
- **change trigger**.

Examples of process inputs include:

- pressure;
- temperature;
- flow rate;
- concentration;
- phase fraction;
- solids loading;
- particle size;
- cleaning chemical;
- transient duration;
- upset frequency;
- utility condition.

### 3.4.1 Source and ownership

Important process data should have an identifiable basis.

Depending on the project, that basis may come from:

- process calculations;
- process simulations;
- equipment information;
- operating data;
- laboratory data;
- production records;
- commissioning data;
- operating procedures;
- process engineering judgement;
- defined project assumptions.

The purpose is not to create bureaucracy.

It is to make it possible to answer:

> **Where did this process input come from, and who is responsible for its validity?**

## 3.5 Process Data Maturity and Uncertainty

Chapter 2 established that engineering decisions must distinguish evidence status.

The same principle applies to process data.

A useful status model is:

### Verified

The value or condition has adequate evidence for the current engineering decision.

### Bounded uncertainty

The exact value is uncertain, but a justified range or envelope has been established.

### Provisional assumption

A value or condition is being used temporarily and still requires confirmation.

### Controlled hold

The information is material to the decision but is not yet sufficiently established.

### Invalidated or superseded

The previous process input is no longer valid because new data, operating changes, or revised assumptions have replaced it.

A provisional process input should not silently become a permanent design fact.

If the process basis is uncertain, the uncertainty must remain visible downstream.

## 3.6 Characterizing the Process Fluid

The engineer should understand the complete service fluid, not only its nominal name.

Relevant characteristics may include:

- complete chemical composition;
- concentration range;
- expected contaminants;
- phase or phase combinations;
- density;
- viscosity;
- vapour pressure where relevant;
- gas solubility where relevant;
- suspended solids;
- solids concentration;
- particle size;
- abrasiveness;
- toxicity;
- flammability;
- oxidizing potential;
- environmental hazard;
- tendency to foam;
- tendency to crystallize;
- tendency to precipitate;
- tendency to polymerize;
- tendency to decompose;
- purity limits;
- contamination limits;
- cleaning fluids;
- flushing fluids;
- temporary service fluids.

The relevant properties should be considered over the **actual operating range**, not only at one reference condition.

### 3.6.1 Temporary fluids are still process fluids

Cleaning, flushing, commissioning, preservation, maintenance, or temporary fluids may expose the piping to conditions different from normal production.

They should therefore be included when they are credible parts of the system life cycle.

A piping system designed only around the production fluid may still be unsuitable for the cleaning or maintenance condition.

## 3.7 Phase State and Phase Changes

The process definition should identify whether the system contains:

- liquid;
- gas;
- solid;
- liquid–gas combinations;
- liquid–solid combinations;
- gas–solid combinations;
- three-phase combinations.

It should also identify whether the phase state changes during operation.

Examples may include:

- gas evolving from liquid;
- flashing;
- condensation;
- solids settling;
- solids resuspension;
- crystallization;
- precipitation;
- gas pockets forming during shutdown;
- two-phase conditions during startup.

The purpose here is not to perform detailed multiphase analysis.

It is to make sure a phase change is not hidden inside a single nominal fluid description.

A process that is “liquid service” during normal operation may not remain single-phase during every credible state.

## 3.8 Time History and Duty Cycle

A process definition is not complete if it records only maxima and minima.

Engineering effects may also depend on:

- how long a condition lasts;
- how often it occurs;
- what happens before it;
- what happens after it;
- how quickly the condition changes;
- how many times it repeats;
- whether the fluid phase changes during the sequence.

Important descriptors may therefore include:

- duration;
- frequency;
- sequence;
- rate of change;
- cumulative cycles;
- dwell time;
- recovery time.

Examples where time history may matter include:

- thermal cycling;
- pressure cycling;
- pump starts and stops;
- batch transitions;
- cleaning cycles;
- gas evolution;
- slurry settling;
- emergency depressurization;
- repeated startup and shutdown.

Cumulative cycling can govern some damage or operating mechanisms.

It is not universally the controlling condition.

The engineer must determine when the time history is relevant to the later engineering analysis.

## 3.9 The Credible Operating Envelope

Industrial systems rarely remain at one steady state.

A robust process definition should therefore distinguish among multiple operating conditions.

These may include:

- normal operation;
- minimum operating state;
- maximum operating state;
- startup;
- shutdown;
- standby;
- batch transition;
- cleaning;
- flushing;
- maintenance;
- equipment trip;
- pump changeover;
- control-system action;
- credible equipment malfunction;
- emergency isolation;
- depressurization;
- loss of utilities;
- foreseeable future operating cases.

The design should not be based only on a nominal operating point.

The process definition should instead establish the **credible operating envelope**.

### 3.9.1 Credible does not mean arbitrary

The envelope should include credible and defined operating cases.

It should not be expanded without basis merely to create unspecified conservatism.

If a possible future condition is not yet defined but could materially affect the engineering decision, it should be recorded as an assumption or controlled hold rather than silently incorporated as fact.

## 3.10 Local Process Conditions

Line-average conditions do not always represent the most important local condition.

Local effects may exist near:

- pump suction or discharge;
- control valves;
- restrictions;
- reducers;
- mixing points;
- equipment nozzles;
- high points;
- low points;
- drains;
- vents;
- heat sources;
- injection points;
- branch connections.

These locations may experience different:

- pressure;
- temperature;
- phase distribution;
- velocity;
- gas content;
- solids concentration;
- residence time;
- mixing intensity.

This chapter does not calculate those effects.

It establishes a review question:

> **Are there locations where the local process condition may differ materially from the line-level process envelope?**

If yes, those locations require downstream engineering attention.

## 3.11 Different Processes Create Different Priorities

Different industries and applications emphasize different engineering concerns.

The following examples are **illustrative and non-exhaustive**.

### Water and wastewater

Typical considerations may include:

- service life;
- corrosion resistance;
- installation efficiency;
- leakage control;
- hydraulic performance;
- maintenance.

### Chemical processing

Typical considerations may include:

- chemical resistance;
- temperature;
- permeation;
- joint integrity;
- containment;
- upset chemistry;
- cleaning compatibility.

### Hydrogen and electrochemical systems

Depending on the system segment, relevant considerations may include:

- gas tightness;
- pressure cycling;
- gas evolution;
- liquid circulation;
- purity;
- phase behaviour.

Electrochemical systems are useful examples of gas generation within circulating liquid, but the same physical behaviour may arise in other reacting or gas-evolving systems.

### Mining and mineral processing

Relevant considerations may include:

- abrasion;
- slurry behaviour;
- settling;
- particle size;
- solids concentration;
- long transport distances;
- pumping energy.

### Semiconductor and high-purity service

Relevant considerations may include:

- contamination control;
- extractables;
- surface condition;
- cleanliness;
- traceability;
- leak prevention.

### Food and pharmaceutical processes

Relevant considerations may include:

- cleanability;
- hygienic design;
- product compatibility;
- contamination prevention;
- regulatory controls.

The engineering lesson is not that each sector has one fixed priority list.

It is that **process function changes which requirements become governing**.

## 3.12 From Process Facts to Engineering Requirements

Chapter 3 identifies the process facts.

Chapter 4 converts those facts into controlled engineering requirements.

The handoff can be understood as:

| Process fact | Downstream requirement category / engineering implication |
|---|---|
| Higher production rate | Flow-capacity and acceptable pressure-loss requirement |
| Increased pressure | Pressure-capability and mechanical-load requirement |
| Higher or variable temperature | Pressure-temperature, movement, and material-performance requirement |
| Aggressive chemistry | Material, joint, and component compatibility requirement |
| Frequent cycling | Transient / cyclic assessment requirement where relevant |
| Outdoor service | Environmental and mechanical-design requirement |
| Abrasive slurry | Velocity, wear, geometry, and inspection requirement |
| High purity | Material, surface, cleaning, contamination, and traceability requirement |
| Gas evolution | Phase-behaviour, operability, venting, and hydraulic review requirement |
| Cleaning chemical exposure | Temporary-service compatibility requirement |
| Defined abnormal condition | Design-envelope and risk-treatment requirement |

The process engineer does not need to solve every downstream design question in this chapter.

But the process fact must be visible so the requirement can be written.

## 3.13 Process Definition Minimum Record

A compact process-definition record should allow another competent engineer to reconstruct the basis of the downstream requirements.

For important process conditions, the record should capture:

- process segment;
- process objective;
- fluid composition;
- phase state;
- pressure range;
- temperature range;
- flow range;
- operating state;
- transient conditions;
- frequency;
- duration;
- sequence where relevant;
- solids or gas behaviour;
- hazards;
- cleaning / temporary fluids;
- data source;
- data owner;
- evidence status;
- unresolved items;
- expected change triggers.

The exact project format may vary.

The engineering content should not.

## 3.14 Process Changes Reopen Engineering Decisions

A process definition is not permanently valid simply because the system has already been designed or commissioned.

A material change in process conditions should trigger review of downstream requirements and the Design Basis.

Typical reopen triggers include:

- changed chemical composition;
- changed concentration;
- changed production rate;
- changed pressure;
- changed temperature;
- new transient;
- changed phase behaviour;
- changed solids loading;
- changed particle size;
- changed equipment;
- changed pump or control philosophy;
- changed cleaning practice;
- changed utility conditions;
- changed operating mode;
- new credible upset condition;
- new operating evidence that invalidates an earlier assumption.

The rule is:

> **If the process basis changes materially, the requirements and Design Basis derived from it must be reviewed.**

A previous engineering decision remains valid only while its process basis remains valid.

## 3.15 Common Mistakes

Common process-definition errors include:

- designing from historical practice without validating current conditions;
- using nominal values as if they define the full operating envelope;
- recording maxima and minima but ignoring duration or frequency;
- overlooking startup, shutdown, cleaning, maintenance, and temporary service;
- selecting a material before characterizing the complete fluid;
- ignoring phase changes or multiphase behaviour;
- assuming line-average conditions apply at every local interface;
- using process values without identifying their source or status;
- allowing provisional assumptions to become permanent design inputs;
- assuming future operation will remain unchanged;
- failing to involve operations and maintenance personnel during process definition;
- failing to reopen the engineering basis after the process changes.

## 3.16 Process Definition as the Input to Requirements

The engineering sequence established by the first chapters is now:

> **System definition → Decision process → Process definition → Engineering requirements → Design Basis**

Chapter 1 defined the engineering object.

Chapter 2 defined the method used to make decisions.

Chapter 3 defines the process information those decisions depend on.

The next chapter, **Chapter 4 — Defining Engineering Requirements**, converts this process definition into explicit, controlled requirements that can be checked against proposed piping solutions.

## Chapter Summary

Piping engineering begins with the process.

A valid process definition includes more than a fluid name and nominal pressure, temperature, and flow.

It should define:

- the process boundary;
- system and equipment interfaces;
- fluid composition;
- phase state;
- operating states;
- credible transients;
- time history;
- duty cycle;
- local conditions;
- hazards;
- cleaning and temporary services;
- data source and ownership;
- evidence status;
- unresolved conditions;
- change triggers.

The objective is not to solve the entire piping design in the process chapter.

It is to make the process basis **complete enough, traceable enough, and explicit enough** that downstream engineering requirements can be written defensibly.

And when the process changes, those downstream requirements must be reopened.
