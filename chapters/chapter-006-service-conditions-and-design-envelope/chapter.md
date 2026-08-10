# Chapter 6 — Service Conditions and the Design Envelope

## Why This Chapter Matters

Industrial piping systems rarely operate at one pressure, one temperature, one flow rate, or one chemical condition.

They experience changing conditions caused by production demand, equipment operation, control actions, cleaning, testing, maintenance, environment, transient events, and process disturbances.

A system designed against one nominal operating point may therefore appear satisfactory while remaining vulnerable under another credible condition.

The engineering task is not simply to identify maxima and minima.

It is to construct a **credible multidimensional service and design envelope** that represents the actual combinations of physical, chemical, mechanical, environmental, and time-dependent conditions that can act on the system.

> **The design envelope is not a list of extremes. It is a controlled set of credible engineering cases.**

### Reader outcomes

After this chapter, the reader should be able to:

- define service conditions across the complete system life cycle;
- distinguish nominal operation from the credible service/design envelope;
- identify operating, transient, abnormal, construction, testing, commissioning, and maintenance states;
- determine which conditions can credibly occur together;
- avoid combining unrelated maxima into artificial design cases;
- define discrete service/design envelope cases;
- recognize that different engineering checks may be governed by different cases;
- include duration, frequency, sequence, dwell, and rate of change where relevant;
- identify local conditions that may differ from line-average conditions;
- record material envelope cases in a traceable format;
- identify incomplete or uncertain conditions for downstream risk and uncertainty treatment.

## 6.1 Service Conditions

Service conditions are the complete set of conditions that can act on the piping system during its life.

They may be:

- physical;
- chemical;
- hydraulic;
- mechanical;
- operational;
- temporal;
- environmental.

Relevant service conditions may include:

- process fluids;
- phase state;
- pressure;
- vacuum;
- temperature;
- flow;
- velocity;
- chemical composition;
- concentration;
- impurities;
- gas content;
- solids content;
- mechanical loads;
- external environment;
- installation condition;
- cleaning;
- flushing;
- commissioning;
- testing;
- maintenance;
- temporary operation;
- abnormal events;
- duration;
- frequency;
- cycle count;
- required design life.

Together, these conditions define the basis from which the service/design envelope is constructed.

## 6.2 The Envelope Is Built from States

A useful starting point is to identify the operating and life-cycle states of the system.

Examples may include:

- normal operation;
- minimum production;
- maximum production;
- startup;
- shutdown;
- standby;
- batch transition;
- pump start;
- pump stop;
- pump trip;
- valve movement;
- cleaning;
- flushing;
- draining;
- commissioning;
- pressure testing;
- maintenance;
- temporary bypass;
- emergency isolation;
- depressurization;
- loss of utilities;
- credible equipment malfunction.

Each state may produce a different combination of process, chemical, mechanical, and environmental conditions.

The envelope should therefore be constructed **state by state**, not by collecting one global maximum for every parameter.

## 6.3 Envelope Construction Workflow

A practical envelope-construction method is:

1. identify operating and life-cycle states;
2. define the relevant condition ranges for each state;
3. identify which conditions can credibly occur simultaneously;
4. define duration and frequency;
5. define sequence, dwell, and rate of change where relevant;
6. identify local conditions and interfaces;
7. convert the information into discrete service/design cases;
8. map each case to the downstream engineering checks it affects;
9. identify unresolved or uncertain inputs.

This workflow converts process information into usable engineering cases.

## FIG-006-001 — Service Envelope Construction

**Conceptual figure placeholder**

Suggested structure:

`Operating / life-cycle states`
↓  
`Condition ranges`
↓  
`Credible simultaneous combinations`
↓  
`Duration / frequency / sequence / rate`
↓  
`Local conditions / interfaces`
↓  
`Discrete envelope cases`
↓  
`Affected engineering checks`
↓  
`Governing case by mechanism / check`

with a side path:

`Uncertain / incomplete condition`
→  
`ASSUMPTION / CONTROLLED HOLD`
→  
`Chapter 007 — Risk and Uncertainty`

The central visual message should be:

> **The envelope is constructed from credible combinations, not from automatic stacking of independent extremes.**

## 6.4 Nominal Operation Is Not the Envelope

Nominal values from a PFD, datasheet, or operating summary are useful.

They rarely define the complete engineering basis.

A system should also be reviewed for conditions such as:

- minimum throughput;
- maximum throughput;
- pump shutoff;
- pump trip;
- valve opening;
- valve closure;
- startup;
- shutdown;
- batch transition;
- cleaning;
- flushing;
- blocked outlet where credible;
- utility loss;
- emergency isolation;
- ambient extremes.

The governing condition may be:

- a short transient;
- a repeated moderate cycle;
- long exposure at elevated temperature;
- temporary chemical exposure;
- an unusual load combination;
- a maintenance or testing state.

The highest numerical value is not automatically the most damaging condition.

## 6.5 Credible Combination and Simultaneity

A common design error is to combine independent maxima as though they all occur at the same time.

For example:

- maximum pressure;
- maximum temperature;
- maximum flow;
- maximum chemical concentration;
- maximum external load.

These values may each be real.

The combined case may still be physically impossible.

The engineer should therefore ask:

- Can these conditions occur simultaneously?
- Under which operating state?
- For how long?
- How often?
- What sequence produces them?
- Is the combined case physically credible?

### 6.5.1 Conservative does not mean artificial

Conservatism can be appropriate.

But a design case should still have a defensible basis.

Arbitrary stacking of unrelated extremes can distort the design and hide the actual governing mechanism.

Where uncertainty exists about correlation, the uncertainty should be visible rather than silently converted into an unrealistic combination.

## 6.6 Different Checks May Have Different Governing Cases

There may be no single universal “worst case.”

Different service cases can govern different engineering questions.

For example:

- one case may govern pressure capability;
- another may govern chemical compatibility;
- another may govern thermal movement;
- another may govern support loading;
- another may govern cyclic response;
- another may govern abrasion;
- another may govern testing or installation.

The engineering question is therefore not:

> “What is the worst case?”

It is:

> **“Which case governs this particular mechanism, calculation, component, or acceptance decision?”**

This distinction becomes increasingly important as the system becomes more complex.

## 6.7 Mechanical Service Conditions

Mechanical conditions may arise from:

- internal pressure;
- external pressure;
- vacuum;
- thermal expansion;
- thermal contraction;
- pipe weight;
- fluid weight;
- valves;
- instruments;
- hoses;
- connected equipment;
- support settlement;
- misalignment;
- wind;
- seismic loading;
- snow;
- burial;
- traffic loads;
- vibration;
- pulsation;
- accidental impact;
- construction;
- testing.

These loads should be evaluated in **credible combinations**.

This does not mean every load acts simultaneously.

The envelope should distinguish:

- normal concurrent loads;
- transient combinations;
- abnormal combinations;
- temporary construction loads;
- temporary testing loads;
- mutually exclusive states.

Detailed code-specific load combinations belong in the later mechanical design chapters and governing design methods.

## 6.8 Chemical Service Conditions

Chemical compatibility cannot be evaluated from the primary chemical name alone.

A useful chemical service description includes:

- chemical or mixture;
- concentration;
- temperature;
- exposure duration;
- frequency;
- operating state;
- impurities;
- contaminants;
- dissolved gases;
- oxidizing or reducing conditions;
- cleaning agents;
- sanitizing agents;
- temporary fluids;
- reaction products;
- relevant mechanical-stress context where applicable.

Chemical service should therefore be treated as a **condition tuple**, not a single fluid label.

For example:

`chemical + concentration + temperature + duration + operating state`

may be more meaningful than simply:

`chemical name`.

## 6.9 Multiphase and Non-Homogeneous Service

Examples include:

- gas-liquid flow;
- liquid-solid slurry;
- gas-liquid-solid flow;
- foams;
- emulsions;
- suspensions;
- crystallizing solutions.

These conditions can affect:

- pressure loss;
- flow regime;
- gas accumulation;
- venting;
- pumping;
- erosion;
- settling;
- vibration;
- cyclic loading;
- instrumentation;
- local heat transfer;
- local mass transfer.

Phase distribution may also vary with **location and operating state**.

A line that is mostly liquid may contain significant gas at a high point.

A slurry may behave differently during normal flow and shutdown.

A single line-level description may therefore be insufficient.

This chapter identifies the need for explicit cases.

Detailed multiphase calculations belong elsewhere.

## 6.10 Local Conditions

System-average conditions do not always govern local behaviour.

Important locations may include:

- pump suction;
- pump discharge;
- control valves;
- restrictions;
- reducers;
- branch points;
- mixing points;
- equipment nozzles;
- heat sources;
- injection points;
- high points;
- low points;
- vents;
- drains;
- plastic-to-metal transitions;
- restraint or support interfaces.

Local pressure, temperature, velocity, phase distribution, chemical concentration, or mechanical loading may differ from the line-level condition.

The envelope should therefore ask:

> **Does any local condition materially exceed or differ from the system-average case relevant to the engineering check?**

If yes, that local condition may require its own envelope case.

## 6.11 Time as a Design Variable

Thermoplastics exhibit time-dependent behaviour.

Time should therefore be treated as part of the service condition.

Relevant descriptors may include:

- duration;
- frequency;
- cycle count;
- sequence;
- rate of pressure change;
- rate of temperature change;
- dwell time;
- recovery time;
- cumulative exposure.

Examples include:

- repeated thermal cycling;
- pressure cycling;
- pump start-stop duty;
- cleaning cycles;
- long hot-service exposure;
- temporary chemical exposure;
- extended shutdown;
- repeated emergency depressurization.

A peak condition without information about time may be incomplete engineering information.

## 6.12 Sequence Matters

Some conditions are influenced by what happens immediately before or after them.

Examples include:

- rapid heating after cold standby;
- depressurization after high-temperature operation;
- chemical cleaning after production service;
- startup after solids settling;
- pump restart after gas accumulation;
- repeated short transients separated by insufficient recovery time.

Sequence may therefore matter independently of maximum and minimum values.

Where sequence can affect the engineering mechanism, it should be recorded as part of the case.

## 6.13 Construction, Testing, and Commissioning Cases

The service envelope should not begin only when the plant enters normal operation.

Temporary project phases may impose significant conditions.

Examples include:

- lifting;
- transport;
- temporary supports;
- partial installation;
- alignment operations;
- pressure testing;
- flushing;
- drying;
- commissioning fluids;
- temporary heating or cooling;
- trapped gas during testing;
- temporary restraints.

Where relevant, these should be established as explicit envelope cases.

A system can be damaged before normal operation begins.

## 6.14 Maintenance and Temporary Configurations

Maintenance can change the system configuration.

Examples may include:

- isolated sections;
- drained sections;
- temporary hoses;
- bypasses;
- temporary blinds;
- replacement equipment;
- local supports;
- temporary heating;
- temporary chemical exposure.

A temporary configuration is still an engineering state if it can produce a material load or exposure.

Maintenance cases should therefore be included where they can affect system integrity.

## 6.15 Foreseeable Change

Facilities evolve.

Potential changes include:

- increased production;
- different chemicals;
- higher concentration;
- replacement pumps;
- changed control strategy;
- revised operating schedules;
- additional equipment;
- modified cleaning procedure.

Not every future condition can be predicted.

Where a future condition is reasonably foreseeable and material to the design, it should be addressed by:

- an envelope case;
- a defined limitation;
- a controlled assumption;
- a future-change trigger.

Foreseeable change should not be converted automatically into unlimited design margin.

## 6.16 Representing the Envelope

The service/design envelope is multidimensional.

Useful representations may include:

- pressure-temperature maps;
- operating-state tables;
- case registers;
- cycle histograms;
- chemical concentration-temperature matrices;
- transient scenarios;
- time-at-condition profiles;
- load-case matrices.

The chosen representation should help answer:

- which conditions occur together;
- when they occur;
- how long they last;
- which downstream checks they affect.

No single visualization is sufficient for every system.

## TAB-006-001 — Service / Design Envelope Case Register

A compact case register may include:

| Field | Purpose |
|---|---|
| Case ID | Unique reference |
| Operating / life-cycle state | Defines when the case occurs |
| Location / system segment | Defines where it applies |
| Pressure / vacuum | Hydraulic condition |
| Temperature | Thermal condition |
| Flow / velocity | Hydraulic state |
| Fluid / phase | Service medium and phase |
| Chemistry / concentration | Chemical exposure |
| Mechanical loads | Relevant concurrent loads |
| Environmental conditions | External exposure |
| Duration / dwell | Time at condition |
| Frequency / cycles | Repetition |
| Sequence / rate of change | Transient character |
| Source / evidence status | Traceability |
| Assumption / hold | Uncertainty state |
| Affected engineering checks | Downstream use |
| Governing for | Mechanism or decision potentially controlled by case |

The table is a model, not a mandatory project format.

The purpose is to make each material case reconstructable.

## 6.17 Mapping Cases to Engineering Checks

Once the cases are defined, they should be mapped to downstream engineering work.

Examples include:

- pressure design;
- material compatibility;
- hydraulic analysis;
- thermal movement;
- support design;
- equipment loads;
- cyclic assessment;
- joining qualification;
- erosion or abrasion review;
- inspection strategy;
- testing;
- commissioning;
- maintenance planning.

Not every case affects every check.

A clean mapping prevents both omission and unnecessary duplication.

## 6.18 Envelope Completeness Review

Before downstream design relies on the envelope, the engineer should review whether it is sufficiently complete.

A practical review asks:

- Are all important operating states identified?
- Are startup and shutdown included?
- Are credible abnormal states included?
- Are cleaning and temporary fluids included?
- Are construction, testing, and commissioning cases included where relevant?
- Are maintenance configurations included where relevant?
- Are multiphase or solids conditions represented?
- Are local conditions identified?
- Are credible simultaneous combinations defined?
- Have unrelated maxima been kept separate?
- Are duration and frequency defined where material?
- Are sequence and rate of change included where material?
- Are sources and evidence status visible?
- Are uncertain conditions identified as assumptions or holds?
- Is each important downstream engineering check covered by at least one relevant case?

The envelope does not need perfect knowledge.

It does need controlled completeness for the engineering stage.

## 6.19 Incomplete or Uncertain Envelope Inputs

Some service conditions may remain uncertain.

Examples include:

- incomplete transient data;
- uncertain future chemistry;
- unknown cycle frequency;
- uncertain external load;
- incomplete equipment information.

These should not be closed through unsupported conservatism.

The appropriate response may be:

- bounded assumption;
- sensitivity study;
- monitoring requirement;
- controlled hold;
- conditional design release;
- further investigation.

Chapter 006 identifies the uncertainty.

Chapter 007 develops how uncertainty and risk should be managed.

## 6.20 Common Mistakes

Common service-envelope errors include:

- designing only for nominal operation;
- combining unrelated maxima into one artificial case;
- assuming one global worst case governs everything;
- omitting short but frequent transients;
- ignoring cleaning or temporary service;
- omitting construction and testing states;
- ignoring temporary maintenance configurations;
- treating gas or solids as negligible without basis;
- failing to define duration or cycle count;
- ignoring rate of change or sequence;
- using line-average conditions where local conditions govern;
- stacking all mechanical loads as though they were simultaneous;
- failing to trace a case to its source;
- converting an uncertain condition into an unsupported design fact.

## 6.21 Handoff to Risk and Uncertainty

Chapter 6 answers:

> **What conditions and combinations can credibly act on the system?**

Some of those conditions will be well established.

Others will remain uncertain.

The next chapter, **Chapter 7 — Engineering Risk and Uncertainty**, asks:

> **How should incomplete knowledge, variability, model limitations, and the consequences of being wrong influence the engineering decision?**

The distinction is deliberate.

Chapter 6 constructs the cases.

Chapter 7 manages uncertainty and risk around those cases.

## Chapter Summary

The service/design envelope is the controlled set of credible conditions and combinations that can act on the piping system throughout its life.

It includes:

- operating states;
- process conditions;
- chemistry;
- phase state;
- mechanical loads;
- environment;
- local conditions;
- temporary project states;
- time;
- sequence;
- frequency;
- credible combinations.

A strong envelope does not automatically combine all maxima.

It defines discrete cases.

Different cases may govern different engineering mechanisms.

Each important case should be traceable to a source, carry its time and state information, and identify which engineering checks it affects.

Incomplete conditions should remain visible as assumptions or controlled holds.

The purpose is not to invent one universal worst case.

It is to ensure that downstream engineering is performed against the **right cases for the right decisions**.
