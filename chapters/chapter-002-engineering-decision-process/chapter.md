# Chapter 2 — The Engineering Decision Process

## Why This Chapter Matters

Engineering failures rarely occur because an engineer is unable to perform a calculation.

More often, they result from:

- poorly defined problems;
- incomplete requirements;
- hidden assumptions;
- missing evidence;
- unsuitable models;
- correct methods applied outside their valid range;
- decisions that were never formally closed;
- or decisions that were not reopened when conditions changed.

Every pipe, fitting, joint, valve, support, inspection activity, test, repair, and modification is the outcome of a chain of decisions.

Sound engineering therefore requires more than technical knowledge.

It requires a disciplined method for converting incomplete information into a **traceable, defensible engineering decision**.

### Reader outcomes

After this chapter, the reader should be able to:

- define the actual engineering decision rather than jump directly to a product or calculation;
- distinguish requirements, constraints, assumptions, unknowns, and evidence;
- compare alternatives against declared engineering criteria;
- evaluate risk without introducing unsupported precision;
- distinguish different forms of verification;
- document an engineering decision and its conditions;
- use **GO / CONDITIONAL GO / NO-GO** dispositions where appropriate;
- identify when a previous decision must be reopened.

## 2.1 Engineering as the Management of Constraints

Engineering is rarely the search for one perfect answer.

It is the selection of a defensible solution among competing constraints such as:

- safety and regulatory compliance;
- reliability and service life;
- hydraulic and mechanical performance;
- chemical compatibility;
- constructability;
- inspectability;
- maintainability and repairability;
- availability;
- cost;
- schedule;
- environmental impact.

Improving one characteristic can affect another.

For example, increasing wall thickness may improve a pressure-design margin while also changing flexibility, joining requirements, installation handling, or cost depending on material, geometry, SDR, and joining process.

The engineer should therefore not maximize one property in isolation.

The objective is to **balance and justify competing requirements across the complete system**.

## 2.2 Decisions Under Uncertainty

Engineers rarely possess complete information.

Material properties vary.

Operating conditions evolve.

Workmanship differs.

Future modifications occur.

Evidence may be incomplete.

Abnormal events may happen.

Good engineering does not eliminate uncertainty.

It makes uncertainty visible, evaluates its significance, and controls how it enters the decision.

A useful distinction is:

- **known and verified**;
- **accepted with bounded uncertainty**;
- **provisional assumption**;
- **missing / controlled hold**;
- **superseded or invalidated**.

A provisional input must not silently become a fact simply because the design process continues.

## 2.3 The Canonical PPE-BoK Engineering Decision Process

The decision process used throughout this book is:

> **Define → Requirements → Constraints → Assumptions / Evidence → Alternatives → Evaluate → Verify → Decide / Document → Monitor / Reopen**

This is not intended to make simple decisions bureaucratic.

It is intended to ensure that important decisions can be reconstructed, checked, and reopened when the basis changes.

## FIG-002-001 — Canonical PPE-BoK Engineering Decision Process

**Conceptual figure placeholder**

Suggested structure:

`Define decision`
↓
`Establish requirements`
↓
`Identify constraints`
↓
`Record assumptions / unknowns / evidence`
↓
`Generate alternatives`
↓
`Evaluate performance / risks / failure modes`
↓
`Verify`
↓
`Decision disposition`
↓
`Document`
↓
`Monitor`

with a return arrow:

`Change / new evidence / failure / modification`
→
`REOPEN DECISION`

The figure should communicate one key principle:

> **Engineering decisions are loops, not one-time calculations.**

## 2.4 Step 1 — Define the Decision and Its Boundary

“Which pipe should I buy?” is not a sufficient engineering decision statement.

A better formulation is:

> “Which piping system solution can provide the required containment, flow, reliability, maintainability, and service life within the documented operating envelope and governing requirements?”

The decision statement should make clear:

- what is being decided;
- why the decision is required;
- which system boundary is included;
- which interfaces are relevant;
- what is outside the scope;
- what constitutes an acceptable outcome.

Poor problem definition creates poor engineering even when every later calculation is correct.

## 2.5 Step 2 — Establish Requirements and Success Criteria

The engineer must identify what the solution is required to achieve.

Requirements may include:

- fluid composition;
- pressure;
- temperature;
- flow;
- transients;
- environment;
- required life;
- safety function;
- reliability;
- purity;
- inspection needs;
- maintenance strategy;
- repairability;
- consequences of failure.

Requirements should be stated in a way that permits a decision to be evaluated.

Instead of:

> “The system should be reliable.”

Prefer:

> “The selected system shall be suitable for the documented operating envelope, intended service life, inspection strategy, and defined failure consequences.”

A decision cannot be verified if success has not been defined.

The detailed development of process inputs begins in the next chapter and continues through the requirements and Design Basis chapters.

## 2.6 Step 3 — Identify Constraints and Non-Negotiables

Not all constraints have equal status.

### Mandatory constraints

These may include:

- law;
- regulation;
- mandatory code;
- adopted safety requirement;
- binding project requirement.

These are not tradeable against cost or schedule.

### Project and design constraints

Examples include:

- owner requirements;
- required service life;
- available space;
- equipment interfaces;
- access;
- environmental conditions;
- inspection philosophy;
- maintenance requirements.

### Commercial and execution constraints

Examples include:

- availability;
- procurement lead time;
- cost;
- schedule;
- contractor capability;
- installation limitations.

Commercial pressure is real.

It is not justification for violating mandatory requirements.

## 2.7 Step 4 — Record Assumptions, Unknowns, and Evidence Status

Hidden assumptions are dangerous because they behave like facts until they are challenged.

An assumption should therefore be treated as an engineering input with uncertainty attached to it.

For every material assumption, record at least:

- the assumption;
- its basis;
- why it matters;
- how sensitive the decision is to it;
- who or what must validate it;
- current status;
- what happens if it proves false.

Examples:

- future maximum temperature is assumed not to exceed a defined value;
- a cleaning chemical is assumed to be used only periodically;
- a support condition is assumed fixed;
- a supplier property is assumed applicable to the actual product form.

Assumptions are not automatically unacceptable.

Uncontrolled assumptions are.

## 2.8 Step 5 — Generate Credible Alternatives

Many engineering problems have more than one technically credible solution.

Alternatives should be generated before a preferred answer becomes psychologically fixed.

Possible alternatives may differ in:

- material;
- wall geometry;
- joining method;
- routing;
- support concept;
- component type;
- inspection strategy;
- operating philosophy;
- maintenance approach.

The objective is not to create artificial alternatives.

It is to avoid treating the first familiar solution as the only possible one.

## 2.9 Step 6 — Evaluate Alternatives, Risks, and Failure Modes

Alternatives should be compared against declared criteria derived from the requirements.

Typical criteria may include:

- safety;
- regulatory compliance;
- service capability;
- reliability;
- failure consequence;
- inspectability;
- maintainability;
- constructability;
- repairability;
- life-cycle cost;
- uncertainty;
- evidence quality.

The engineer should ask:

- What can fail?
- How could it fail?
- What would initiate failure?
- What are the consequences?
- Can the failure be detected?
- Can it be isolated?
- Can it be repaired?
- Which interface or condition governs?

### Qualitative versus quantitative risk

Not every decision supports a meaningful numerical probability.

When evidence does not support quantitative likelihood, qualitative risk screening is acceptable.

False numerical precision does not improve a weak decision.

It only hides uncertainty behind decimal places.

## 2.10 Step 7 — Verify Inputs, Methods, and Results

Verification is not one activity.

It can include several distinct forms.

### Input verification

Are the data, assumptions, service conditions, material properties, and requirements credible and applicable?

### Method verification

Is the selected equation, model, test method, standard route, or analysis method appropriate for the problem?

### Result verification

Were calculations, units, conversions, model outputs, and conclusions obtained correctly?

### Independent review

Can another competent engineer reproduce the reasoning and accept the assumptions, methods, and conclusions?

### Validation against reality

Where applicable:

- testing;
- commissioning;
- inspection;
- prototype evidence;
- qualification records;
- field experience;
- operating data.

Verification increases confidence.

It does not create certainty.

## 2.11 Step 8 — Decide and Document the Disposition

Verification does not itself state the engineering decision.

The decision must be explicit.

Where appropriate, PPE-BoK uses the following default dispositions:

### GO

The available evidence is sufficient to support the decision within the stated Design Basis and conditions.

### CONDITIONAL GO

The solution may proceed, but one or more controlled conditions, assumptions, actions, or verification items remain open.

A Conditional Go should state exactly what must be closed and by when.

### NO-GO

The available evidence, requirements, risks, or constraints do not support proceeding with the proposed solution.

A No-Go is not an engineering failure.

It is a valid engineering outcome.

## 2.12 The Minimum Decision Record

A defensible decision should allow another competent engineer to reconstruct:

- what was decided;
- which requirements and Design Basis inputs were used;
- which constraints were governing;
- which assumptions and unknowns remained;
- what evidence was relied upon;
- which alternatives were considered;
- which failure modes or risks were important;
- what calculations or analyses were performed;
- what verification was completed;
- the final disposition;
- any conditions or open items;
- the triggers that would require the decision to be reopened.

If the reasoning cannot be reconstructed, the engineering record is incomplete even if the final answer happened to be correct.

## 2.13 Data, Information, and Engineering Knowledge

A pressure, temperature, flow rate, concentration, or material property is data.

When its source, uncertainty, relationship, and operating context are understood, it becomes useful information.

It becomes engineering knowledge only when it is used to answer a decision.

For example:

- Is the material suitable?
- Is the pressure-temperature basis adequate?
- Is thermal movement significant?
- Are cyclic loads relevant?
- Is the jointing route appropriate?
- Does the evidence support GO or only CONDITIONAL GO?

Data maturity therefore matters.

A precise number from an uncertain source may be less valuable than a bounded estimate whose limitations are understood.

## 2.14 Standards and Engineering Judgement

Standards define accepted requirements, methods, definitions, and technical boundaries.

They do not anticipate every:

- process;
- geometry;
- operating philosophy;
- interface;
- maintenance strategy;
- future modification.

Compliance does not eliminate the need for engineering judgement.

Equally, engineering judgement must not be used to bypass mandatory requirements.

The engineer must therefore determine:

- which standard applies;
- which edition applies;
- whether the method is within scope;
- whether additional project requirements apply;
- where judgement remains necessary.

If clause-level evidence is missing and materially affects the decision, the correct disposition may be a controlled hold rather than an unsupported conclusion.

## 2.15 Experience in Context

Experience is valuable because it reveals patterns that calculations may not.

But experience is evidence only within its context.

A solution that worked in one plant may fail elsewhere because of differences in:

- chemistry;
- temperature;
- loading;
- joining quality;
- geometry;
- installation;
- environment;
- operation;
- inspection;
- maintenance.

A useful experience-based question is therefore not:

> “Has this worked before?”

but:

> “Under what conditions did it work before, and are those conditions relevant here?”

## 2.16 Common Decision Errors

### Confirmation bias

Selecting evidence that supports a preferred solution while discounting contradictory evidence.

### Experience bias

Assuming previous success guarantees future success.

### Specification bias

Treating component conformity as proof of system suitability.

### Single-factor optimization

Improving one characteristic while degrading overall system performance.

### Unchallenged assumptions

Allowing provisional assumptions to become permanent design inputs without validation.

### False precision

Using detailed numerical methods on inputs whose uncertainty does not justify the apparent accuracy.

### Premature closure

Treating a calculation, quotation, supplier recommendation, or pressure class as the final engineering decision.

### Failure to reopen

Continuing to rely on a previous decision even after the Design Basis, evidence, standard, product, or operating conditions have changed.

## 2.17 Decisions Continue After Commissioning

Engineering decisions do not end when the system enters service.

They continue through:

- inspection;
- operating changes;
- repairs;
- modifications;
- life extension;
- failure investigation;
- replacement planning.

A previous engineering decision should be reopened when a material input changes.

Typical reopen triggers include:

- change in Design Basis;
- change in fluid or concentration;
- change in pressure or temperature envelope;
- new transient condition;
- change in standard or adopted edition;
- product substitution;
- joining-process change;
- installation modification;
- changed support or restraint condition;
- new inspection evidence;
- unexpected degradation;
- failure or near miss;
- invalidated assumption;
- new credible technical evidence.

A decision should remain valid only while its basis remains valid.

## 2.18 Worked Qualitative Example — From Vague Question to Engineering Decision

### Initial question

> “Which pipe should I buy?”

This question is too vague to support engineering selection.

### Step 1 — Define

The actual decision is:

> Select a piping-system concept suitable for a defined fluid, pressure, temperature, service life, installation environment, maintenance strategy, and failure consequence.

### Step 2 — Requirements

The engineer records:

- service conditions;
- operating envelope;
- expected life;
- chemical exposure;
- inspection requirements;
- joining limitations.

### Step 3 — Constraints

Mandatory requirements and project constraints are identified before cost or availability is considered.

### Step 4 — Assumptions / evidence

One temperature transient remains unconfirmed.

It is recorded as a controlled hold.

### Step 5 — Alternatives

Several credible material/system concepts are compared.

### Step 6 — Evaluate

Chemical compatibility, pressure-temperature capability, joining, inspection, installation, and credible failure modes are assessed.

### Step 7 — Verify

Key inputs, design methods, product documentation, and calculations are checked.

### Step 8 — Decide

The preferred solution meets the current evidence basis, but the transient temperature remains unresolved.

**Disposition: CONDITIONAL GO**

Condition:

> Final material/system approval requires confirmation that the transient temperature remains within the validated service envelope.

### Step 9 — Reopen

If the transient temperature is later found to exceed the assumed value, the decision is automatically reopened.

The important output is not simply a selected pipe.

It is a traceable decision whose evidence, limitations, and reopen condition are visible.

## Chapter Summary

Engineering is the disciplined conversion of incomplete information into defensible decisions.

The canonical PPE-BoK process is:

> **Define → Requirements → Constraints → Assumptions / Evidence → Alternatives → Evaluate → Verify → Decide / Document → Monitor / Reopen**

A good engineering decision therefore requires:

- a clearly defined problem;
- complete enough requirements;
- explicit constraints;
- visible assumptions;
- credible evidence;
- reasonable alternatives;
- failure and risk evaluation;
- appropriate verification;
- a clear disposition;
- a traceable decision record;
- defined reopen triggers.

Standards, science, experience, evidence, and judgement are complementary.

None is sufficient alone.

The next chapter, **Chapter 3 — Understanding Industrial Processes**, develops the first major input to this decision process: understanding the process well enough to define valid engineering requirements.
