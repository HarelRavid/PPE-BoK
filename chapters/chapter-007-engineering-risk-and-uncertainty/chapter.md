# Chapter 7 — Engineering Risk and Uncertainty

## Why This Chapter Matters

Every engineering decision is made with incomplete knowledge.

The future operating history of a piping system cannot be known exactly. Material properties vary. Manufacturing and joining are not perfectly uniform. Process conditions change. Models simplify reality. Inspection has limits. Human and organizational performance varies. New evidence may appear after the original design decision has been made.

The objective of engineering is therefore not to eliminate uncertainty.

It is to:

- identify it;
- understand why it exists;
- determine whether it matters to the decision;
- reduce it where practical;
- control the consequences where it cannot be removed;
- record what remains uncertain;
- reopen the decision when new evidence changes the basis.

> **A defensible engineering decision does not require perfect certainty. It requires uncertainty to be visible, proportionate, and controlled.**

### Reader outcomes

After this chapter, the reader should be able to:

- distinguish expected variability, uncertainty, nonconformance, assumptions, and controlled holds;
- identify the uncertainty that matters to a specific engineering decision;
- determine whether a decision is sensitive to plausible uncertainty;
- consider consequence together with sensitivity and evidence quality;
- select proportionate actions to reduce or control uncertainty;
- distinguish risk controls by their engineering function;
- avoid unsupported numerical precision;
- avoid double-counting design margins;
- record residual uncertainty after controls are applied;
- make GO / CONDITIONAL GO / NO-GO decisions under uncertainty;
- identify when independent review is appropriate;
- define monitoring and reopen triggers.

---

## 7.1 Decision-Making Under Uncertainty

Engineering rarely produces absolute answers.

It works with:

- imperfect measurements;
- variable materials;
- manufacturing tolerances;
- incomplete operating histories;
- uncertain future conditions;
- simplified models;
- incomplete evidence;
- changing requirements.

A sound engineering decision is not one that claims certainty.

It is one that is:

- reasonable;
- traceable;
- evidence-based;
- proportionate to consequence;
- explicit about assumptions;
- explicit about residual uncertainty;
- revisable when the evidence changes.

The central question is:

> **Does the uncertainty materially affect the engineering decision, and if so, what must be done about it?**

---

## 7.2 The Engineering Uncertainty Decision Workflow

A practical uncertainty-management sequence is:

1. define the engineering decision or requirement at risk;
2. identify the uncertain input, condition, model, or assumption;
3. identify the source and evidence status;
4. define plausible bounds or scenarios where possible;
5. determine decision sensitivity;
6. consider the consequence if the decision is wrong;
7. select proportionate uncertainty and risk controls;
8. evaluate residual uncertainty;
9. make a GO / CONDITIONAL GO / NO-GO disposition;
10. define monitoring and reopen triggers.

This keeps uncertainty connected to an actual decision rather than treating it as an abstract project problem.

---

## FIG-007-001 — Engineering Uncertainty Decision Workflow

**Conceptual figure placeholder**

Suggested structure:

`Engineering decision / requirement`
↓  
`Uncertain input / model / condition / assumption`
↓  
`Evidence status`
↓  
`Plausible bounds / scenarios`
↓  
`Decision sensitivity`
+
`Consequence if wrong`
↓  
`Proportionate controls`
↓  
`Residual uncertainty`
↓  
`GO / CONDITIONAL GO / NO-GO`
↓  
`Monitoring / reopen trigger`

Side branches:

`Insufficient evidence`
→  
`TEST / INSPECT / OBTAIN DATA / HOLD`

`High consequence + weak evidence`
→  
`INDEPENDENT REVIEW / ESCALATION`

The visual should reinforce one principle:

> **Uncertainty is managed in relation to the decision it can change.**

---

## 7.3 Sources of Uncertainty

### Material variability

Properties may vary with:

- resin grade;
- production batch;
- processing history;
- geometry;
- temperature;
- environment;
- ageing.

Some variability may be expected within the qualified or accepted material population.

### Manufacturing and joining variability

Examples include:

- wall thickness;
- ovality;
- dimensional tolerance;
- surface condition;
- heating;
- fusion parameters;
- alignment;
- contamination;
- workmanship.

### Process variability

Examples include:

- pressure;
- temperature;
- flow;
- composition;
- solids concentration;
- gas fraction;
- transient frequency.

### Environmental variability

Examples include:

- ambient temperature;
- ultraviolet exposure;
- soil condition;
- groundwater;
- chemical atmosphere;
- external loading.

### Human and organizational variability

Examples include:

- installation;
- inspection;
- operation;
- maintenance;
- documentation;
- training;
- management of change.

### Model uncertainty

Calculations and correlations simplify reality.

Their assumptions, calibration, and validation range may not fully represent the actual system.

### Data uncertainty

Measured or supplied information may itself be uncertain because of:

- limited samples;
- measurement error;
- incomplete records;
- uncertain source quality;
- insufficient operating history;
- extrapolation beyond available evidence.

---

## 7.4 Variability, Uncertainty, Nonconformance, Assumptions, and Holds

These terms describe different engineering states.

### Expected variability

Variation that exists within an accepted process, population, tolerance, or operating range.

Expected variability is not automatically a defect.

### Uncertainty

Incomplete knowledge about:

- the true value;
- future condition;
- model accuracy;
- actual system response.

### Nonconformance

A demonstrated failure to satisfy a defined requirement.

Nonconformance is not merely “uncertainty.”

There is evidence that a requirement has not been met.

### Assumption

A provisional input used in order to proceed.

An assumption must remain visible until validated or replaced.

### Controlled hold

A material unresolved condition for which the current evidence is insufficient to support the affected decision.

These states require different responses.

Confusing them can lead to unnecessary conservatism in one case and dangerous overconfidence in another.

---

## 7.5 Variability Is Not Automatically Nonconformance

Engineering products are manufactured and operated within ranges.

Standards, specifications, and qualified processes commonly recognize permissible variability because perfect uniformity is not physically achievable.

The engineering question is not:

> “Is there variation?”

It is:

> **“Does the observed variation remain within the accepted basis, and has its effect been adequately considered?”**

A dimensional variation inside a permitted tolerance may be acceptable.

A dimensional variation outside the requirement is a nonconformance.

An unknown dimension that has not been measured is an uncertainty.

Those are three different states.

---

## 7.6 Risk and Uncertainty Are Different

Uncertainty describes incomplete knowledge.

Risk concerns the possibility of an undesirable outcome and the consequence associated with it.

The same uncertainty can therefore lead to very different engineering responses.

For example, uncertainty in future cycle count may be relatively unimportant if:

- the system is insensitive to cycling;
- consequence of failure is low;
- inspection can detect deterioration.

The same uncertainty may require strong action if:

- the mechanism is highly cycle-sensitive;
- failure consequence is severe;
- degradation is difficult to detect.

Reducing uncertainty can improve the decision.

But risk can also be reduced without eliminating uncertainty.

---

## 7.7 Decision Sensitivity

Not every uncertain input deserves the same engineering effort.

The key question is:

> **Can plausible variation in this input change the engineering decision?**

### Low sensitivity

If the decision remains unchanged over a credible input range, further precision may add little value.

### Moderate sensitivity

The uncertainty affects margin or confidence but does not necessarily reverse the decision.

Additional evidence or monitoring may still be justified.

### High sensitivity

A relatively small change in the input can change:

- pass to fail;
- acceptable to unacceptable;
- material choice;
- pressure capability;
- support strategy;
- inspection requirement;
- operating limit.

High-sensitivity uncertainty deserves stronger treatment.

This principle prevents two opposite mistakes:

- under-analyzing uncertainty that can reverse the decision;
- spending excessive effort refining uncertainty that cannot materially affect the conclusion.

---

## 7.8 Plausible Bounds and Scenarios

Where possible, uncertainty should be bounded.

Possible approaches include:

- measured range;
- operating range;
- qualified tolerance;
- supplier information;
- conservative engineering bound;
- scenario analysis;
- sensitivity range.

The purpose is not to invent a precise statistical distribution.

It is to define a defensible region within which the engineering conclusion can be tested.

If even a plausible bound cannot be established, the uncertainty may require:

- new data;
- test;
- inspection;
- monitoring;
- controlled hold.

---

## 7.9 Consequence Matters

Sensitivity alone does not determine the required response.

The consequence of being wrong also matters.

Relevant consequences may include:

- loss of containment;
- personnel exposure;
- environmental release;
- fire;
- equipment damage;
- production loss;
- contamination;
- repair difficulty;
- inaccessible failure;
- repeated degradation;
- loss of critical service.

As consequence increases, the engineering basis may justify:

- stronger evidence;
- greater review depth;
- more independent verification;
- stronger controls;
- closer monitoring.

This does not mean assigning unsupported numerical risk values.

It means matching the decision process to what is at stake.

---

## 7.10 Proportionate Responses to Uncertainty

Possible engineering responses include:

### Obtain better data

Examples:

- improved process data;
- operating history;
- supplier data;
- field measurement.

### Bound the uncertainty

Establish a credible range or scenario envelope.

### Perform sensitivity analysis

Determine whether the uncertain input can materially change the conclusion.

### Test or qualify

Obtain evidence through:

- material test;
- component test;
- joining qualification;
- mock-up;
- performance test.

### Inspect

Determine the actual condition or verify conformity.

### Monitor

Track the uncertain variable or a degradation indicator during operation.

### Add operational control

Examples:

- limit pressure;
- limit temperature;
- control chemistry;
- limit cycles;
- impose inspection intervals.

### Add engineered control

Examples:

- containment;
- isolation;
- redundancy;
- improved support;
- protective barrier.

### Redesign

Change the design so the decision becomes less sensitive to the uncertainty.

### Hold

Do not proceed until the uncertainty is resolved.

### Reject

Conclude that the current option does not provide a defensible basis.

The correct response depends on:

- sensitivity;
- consequence;
- evidence quality;
- practicality;
- project stage.

---

## 7.11 Risk-Control Functions

Controls should connect to the physical mechanism and failure consequence.

Useful control functions include:

### Prevention

Prevent the initiating condition or mechanism.

### Likelihood reduction

Reduce the chance of the undesirable condition developing.

### Demand or exposure reduction

Reduce:

- pressure;
- temperature;
- cycling;
- chemical exposure;
- mechanical demand.

### Detection

Identify degradation or abnormal condition before failure.

### Containment

Limit the consequence of release or failure.

### Isolation

Permit the affected system to be isolated safely.

### Recovery and repair

Enable timely restoration after failure or degradation.

### Monitoring

Observe indicators and trigger predefined action.

A generic risk score is not a substitute for understanding what the control actually does.

---

## 7.12 Design Margins

Margins may arise from:

- code-defined design coefficients;
- material classification;
- statistical treatment;
- dimensional tolerances;
- load combinations;
- service-condition uncertainty;
- project-specific controls.

Margins should have a defined purpose.

The engineer should understand:

- what uncertainty or variability the margin addresses;
- what it does not address;
- whether another margin already covers the same effect.

### 7.12.1 Do not assume one margin covers everything

A pressure-design coefficient does not automatically cover:

- chemical degradation;
- joining defects;
- support error;
- abnormal transient;
- installation damage;
- unknown process chemistry.

### 7.12.2 Avoid double-counting conservatism

Multiple independent margins can unintentionally overlap.

Stacking conservatism without understanding its origin may create:

- unnecessary wall thickness;
- increased stiffness;
- higher loads;
- installation difficulty;
- higher cost;
- new local stress effects.

The objective is not minimum conservatism.

It is **controlled conservatism with a known basis**.

---

## 7.13 False Precision

Uncertainty should not be hidden behind numbers that the evidence cannot support.

Examples of false precision include:

- assigning a probability without a defensible dataset;
- quoting excessive decimal places from approximate input data;
- presenting a speculative likelihood as statistically established;
- converting expert judgement into a precise confidence level without basis.

A qualitative engineering conclusion can be more defensible than a numerical result that only appears rigorous.

The rule is:

> **Do not quantify beyond the evidence.**

Where quantification is justified, use it.

Where it is not, preserve the uncertainty honestly.

---

## 7.14 Robustness

A robust design remains acceptable despite expected variation.

Examples may include:

- avoiding highly stress-sensitive geometry;
- allowing controlled thermal movement;
- supporting heavy components independently;
- reducing sensitivity to installation tolerance;
- selecting joining processes that can be reliably controlled in the actual site environment;
- choosing operating ranges with stable performance margin.

Robustness reduces dependence on perfect conditions.

---

## 7.15 Resilience

A resilient system can tolerate or recover from disturbance without disproportionate consequence.

Examples may include:

- isolation capability;
- drainage;
- venting;
- repair access;
- redundancy;
- monitoring;
- maintainable components;
- defined response procedures.

Robustness and resilience are related but different.

A robust system resists variation.

A resilient system can manage disturbance when it occurs.

---

## 7.16 Residual Uncertainty

Engineering controls rarely eliminate all uncertainty.

After data collection, testing, bounding, redesign, monitoring, or other controls, some uncertainty may remain.

That remaining uncertainty should be identified explicitly.

The engineer should ask:

- What is still unknown?
- How sensitive is the decision to it?
- What is the consequence if the assumption is wrong?
- Which controls remain active?
- Is monitoring required?
- What event would reopen the decision?

Residual uncertainty may be:

- acceptable;
- conditionally acceptable;
- unacceptable.

The existence of residual uncertainty does not automatically invalidate a design.

Failure to recognize it can.

---

## TAB-007-001 — Uncertainty and Risk Decision Register

A compact decision record may include:

| Field | Purpose |
|---|---|
| Item ID | Unique reference |
| Affected decision / requirement | What may change |
| Uncertainty | What is not sufficiently known |
| Type / source | Material, process, model, data, human, etc. |
| Evidence status | What evidence exists |
| Plausible range / scenario | Defensible bounds |
| Decision sensitivity | Low / moderate / high or equivalent qualitative basis |
| Consequence if wrong | Why it matters |
| Proposed control | Action used to reduce/manage uncertainty |
| Residual uncertainty | What remains |
| Owner | Responsibility |
| Disposition | GO / CONDITIONAL GO / NO-GO |
| Monitoring | Required ongoing observation |
| Reopen trigger | What invalidates the current decision |

The exact project format may vary.

The purpose is to prevent material uncertainty from disappearing into meeting notes or personal memory.

---

## 7.17 GO / CONDITIONAL GO / NO-GO Under Uncertainty

Chapter 2 established the book-wide disposition model.

The same model applies here.

### GO

The available evidence, uncertainty, sensitivity, consequence, and controls support proceeding without unresolved material conditions that would invalidate the decision.

### CONDITIONAL GO

The decision may proceed subject to explicit conditions.

Examples may include:

- operating limit;
- monitoring requirement;
- pending validation;
- inspection requirement;
- temporary restriction;
- controlled assumption;
- closure action.

The conditions must be visible and owned.

### NO-GO

The current evidence or control basis does not support proceeding.

This may occur when:

- uncertainty is too large;
- decision sensitivity is high;
- consequence is severe;
- evidence is inadequate;
- critical hold remains unresolved;
- no acceptable control exists.

A NO-GO decision is not a failure of engineering.

Proceeding without a defensible basis can be.

---

## 7.18 Independent Review and Escalation

Some decisions justify additional review.

Possible triggers include:

- high consequence of failure;
- weak evidence;
- high decision sensitivity;
- novel application;
- conflicting technical opinions;
- extrapolation outside validated experience;
- unresolved model limitations;
- multiple interacting uncertainties;
- previous failure history.

Independent review does not replace the responsible engineer.

It adds a separate challenge to:

- assumptions;
- evidence;
- logic;
- calculation;
- control strategy.

The required review depth should be proportionate to the decision.

---

## 7.19 Engineering Judgement

Engineering judgement combines:

- physical understanding;
- standards and accepted practice;
- test evidence;
- operating evidence;
- model awareness;
- project constraints;
- failure consequence;
- uncertainty awareness;
- willingness to revise the conclusion.

Judgement is not personal preference.

A defensible judgement should be explainable.

Another competent engineer should be able to understand:

- what evidence was used;
- what was assumed;
- what remained uncertain;
- why the decision was considered acceptable.

---

## 7.20 Unknown Unknowns

Some events cannot be predicted during design.

The existence of unknown unknowns does not justify speculative scenarios without basis.

It does support engineering practices such as:

- robustness;
- resilience;
- independent review;
- monitoring;
- inspection;
- learning from operating data;
- effective management of change;
- failure and near-miss feedback.

The response to unknown unknowns is not imaginary precision.

It is a system capable of learning and adapting.

---

## 7.21 Monitoring and Reopen Triggers

An engineering decision remains valid only while its basis remains valid.

Possible reopen triggers include:

- new operating data;
- changed process conditions;
- failed assumption;
- monitoring threshold exceeded;
- unexpected degradation;
- new failure mechanism;
- changed material or component;
- changed joining method;
- new equipment configuration;
- modified maintenance practice;
- standards or requirement change;
- test result inconsistent with the original basis;
- evidence that the model is not representing the system adequately.

The engineer should define reopen triggers wherever residual uncertainty materially affects the decision.

---

## 7.22 Learning from Failure and Near Misses

Failures expose assumptions that were:

- incorrect;
- incomplete;
- poorly controlled;
- no longer valid.

Near misses and unexpected degradation can provide equally valuable evidence.

A useful review asks:

- Which decision allowed this mechanism to develop?
- Which assumption was wrong or incomplete?
- Was the uncertainty known?
- Was the decision sensitive to it?
- Which control failed to prevent or detect the condition?
- Was the original decision reasonable with the evidence available at the time?
- What should now be changed?

This connects failure learning directly back to engineering decision control.

---

## 7.23 Common Errors

Common uncertainty and risk errors include:

- treating uncertainty as a reason to avoid making any decision;
- treating an assumption as a verified fact;
- confusing expected variability with nonconformance;
- hiding uncertainty behind precise numbers;
- assigning probabilities without evidence;
- applying safety factors without understanding what they cover;
- double-counting overlapping conservatism;
- spending excessive effort on uncertainty that cannot change the decision;
- ignoring uncertainty that can reverse the decision;
- considering likelihood without consequence;
- using a generic risk score without understanding the mechanism;
- assuming code compliance eliminates all system risk;
- failing to record residual uncertainty;
- failing to define monitoring or reopen triggers;
- continuing to use a decision after its original evidence basis has changed.

---

## 7.24 Handoff to the Technical Chapters

Chapter 7 does not replace technical engineering methods.

It provides the decision discipline applied around them.

Later chapters will provide domain-specific methods for subjects such as:

- process-fluid characterization;
- material selection;
- polymer behaviour;
- long-term strength;
- hydraulics;
- mechanical design;
- joining;
- inspection;
- testing.

The relationship is:

> **Technical method tells the engineer how to analyze the system.**

> **Chapter 7 tells the engineer how to manage uncertainty around the inputs, models, evidence, and decision.**

Both are required.

---

## Chapter Summary

Engineering is the practice of making defensible decisions despite incomplete knowledge.

Uncertainty should be connected to the specific decision it can affect.

The engineer should:

- identify the uncertainty;
- distinguish it from variability and nonconformance;
- define plausible bounds;
- understand decision sensitivity;
- consider consequence;
- select proportionate controls;
- avoid unsupported precision;
- account for margins carefully;
- record residual uncertainty;
- make GO / CONDITIONAL GO / NO-GO decisions;
- define monitoring and reopen triggers.

A strong engineering decision does not pretend uncertainty has disappeared.

It makes uncertainty visible, controlled, and proportionate to what is at stake.
