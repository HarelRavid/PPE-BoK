# Batch 013-G — Investigation 10

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved redevelopment artifact  
**Integration target:** Chapter 13 Rev 1.0  
**PDS baseline:** 1.0 (frozen)

> This Investigation is a structured Failure Lens for practicing engineers. It is not a substitute for specialist forensic failure analysis. Any standards-derived acceptance criteria added during final integration shall be verified against current authoritative sources before publication.

# Investigation 10 — What Can Failure Evidence Tell the Engineer?

Failure evidence is useful only when observation is kept separate from interpretation.

A split pipe, leaking fusion joint, gouge, deformation or brittle-looking fracture surface is an **observation**. It is not, by itself, proof of the governing failure mechanism.

The engineering task is therefore:

\[
\boxed{
Observation
\rightarrow Plausible\ mechanisms
\rightarrow Evidence
\rightarrow Discrimination
\rightarrow Engineering\ response
}
\]

The purpose of this Investigation is not to teach full forensic failure analysis. It is to give the design engineer enough structure to avoid premature conclusions and to convert failure evidence into useful design feedback.

## 10.1 Start with facts, not the preferred explanation

The first record should describe what is known without assigning cause.

For example:

**Observation**

> Longitudinal crack approximately 300 mm long adjacent to a visibly damaged region of the pipe.

is preferable to:

> Pipe failed by slow crack growth caused by installation damage.

The second statement contains several conclusions that have not yet been demonstrated.

A useful initial evidence set includes:

- exact failure location;
- pipe and fitting identification;
- marking and traceability information;
- dimensions and SDR;
- photographs before destructive examination;
- fracture location and orientation;
- visible deformation;
- gouges, scratches or other local damage;
- joint proximity;
- operating pressure and temperature history;
- transient/upset history;
- installation history;
- fluid/environment;
- age and service duration;
- previous repairs or interventions.

The principle is:

> **Preserve evidence before explaining evidence.**

## 10.2 Build more than one plausible mechanism

Investigation 4 established that PE can exhibit different time-dependent and crack-growth behaviours.

Investigation 10 uses those mechanisms diagnostically.

The engineer should initially ask:

> What mechanisms are physically capable of producing the observation under this Design Basis?

—not—

> Which mechanism do I expect to find?

A preliminary hypothesis set may include:

- short-term ductile overload;
- long-term pressure/creep-related rupture;
- slow crack growth initiated or accelerated by a local stress concentrator;
- installation damage;
- joining/fusion deficiency;
- fitting or fabricated-component issue;
- chemical/environmental interaction;
- temperature or service excursion;
- external/mechanical loading;
- or interaction between several mechanisms.

Multiple hypotheses may remain open simultaneously.

## TAB-013-004 — Failure Evidence / Engineering Response Matrix

| Observation / condition | Plausible mechanism to investigate | Evidence that may discriminate | Engineering response if supported | Boundary of inference |
|---|---|---|---|---|
| Large deformation near rupture | Short-term overload / ductile failure | Pressure history, dimensions, temperature, deformation pattern, material verification | Recheck actual load against system capability and transient basis | Deformation alone does not identify the initiating event |
| Failure after long service without obvious gross overload | Long-term time-dependent rupture | Service history, stress basis, temperature history, material/product qualification | Reopen long-term design basis and service envelope | Age alone does not prove creep rupture |
| Crack associated with notch/gouge | Notch-driven SCG or damage-assisted cracking | Damage geometry, fracture examination, material SCG qualification, stress/service history | Assess damage acceptance, installation controls and qualification basis | A gouge near a crack does not prove it initiated the failure |
| Failure at/near fusion joint | Joining-related mechanism, local geometry or interacting load | Procedure records, operator/equipment records, joint geometry, destructive/NDT evidence where applicable | Reassess joining qualification, execution and inspection controls | Location at a joint does not automatically prove poor fusion |
| Local wall loss / severe surface damage | Installation or external mechanical damage | Installation records, excavation evidence, damage dimensions, local loading | Review installation method, damage criteria and protection | Visible damage may be secondary rather than causal |
| Failure associated with unusual fluid/environment | Chemical/environmental interaction | Fluid composition, concentration, temperature, exposure duration, compatibility evidence | Reopen compatibility assessment and material selection | Generic chemical-resistance charts do not establish causation |
| Failure following elevated-temperature period | Temperature/service excursion | Recorded temperatures, duration, pressure history, governing temperature/time basis | Recalculate service capability and investigate permanent damage | Temporal correlation is not proof of causation |
| Repeated failures at similar geometry/location | Systematic design/detailing/loading issue | Population data, geometry, restraint, support, fabrication and operating history | Escalate from individual failure to fleet/system review | Repetition strengthens a hypothesis but does not replace mechanism evidence |

This table is deliberately written as an **investigation aid**, not a lookup table where “appearance X = cause Y”.

## 10.3 Separate initiation from final rupture

One of the easiest mistakes in failure interpretation is to confuse the final event with the initiating mechanism.

A pipe may spend a long period developing a crack and then experience rapid final rupture.

Therefore:

\[
\text{final fracture appearance}
\neq
\text{necessarily the initiating mechanism}
\]

The engineer should distinguish, where evidence permits:

`initiation → propagation → final instability / rupture`

This is particularly important when considering SCG.

A local notch, gouge or defect may increase the local crack-driving condition even when nominal hoop stress remains within the expected design basis.

The nominal pressure calculation therefore cannot, by itself, exclude a local damage-assisted failure mechanism.

## 10.4 Do not use SCG qualification as immunity from damage

The SCG qualification pathway discussed earlier establishes evidence under a defined test and acceptance framework.

It does not establish:

> “This PE grade cannot fail by SCG.”

Nor does an enhanced SCG-resistance designation mean arbitrary installation damage becomes acceptable.

The correct question after a suspected notch-related failure is:

> **Was the actual local condition within the damage, installation and qualification assumptions used by the design?**

That reconnects failure evidence directly to engineering assumptions.

## 10.5 A joint failure is a system question

When failure occurs near a butt fusion, electrofusion fitting or fabricated component, the investigation should not immediately collapse into:

> “bad weld.”

The relevant evidence may involve:

- material/product compatibility;
- joint preparation;
- alignment;
- contamination;
- equipment condition;
- procedure;
- operator execution;
- temperature/environment during joining;
- fitting geometry;
- restraint and imposed displacement;
- local bending;
- pressure/temperature history;
- inspection evidence.

The objective is to determine whether the failure reflects:

**execution**, **qualification**, **design**, **loading**, or an **interaction**.

Investigation 10 does not teach the detailed joining procedure; it teaches the engineer not to erase the rest of the system when a fracture happens to be located at a joint.

## 10.6 Failure evidence should reopen the Design Basis

A credible failure is not merely a maintenance event.

It is also feedback on the assumptions used in design.

The engineer should compare actual service evidence against the original basis:

| Design assumption | Failure-review question |
|---|---|
| Pressure | Was actual pressure, including transients, within the assumed envelope? |
| Temperature | Did actual temperature/time history match the design basis? |
| Material | Was the installed material/product the specified qualified product? |
| SDR / wall | Were actual dimensions and damage condition consistent with the calculation? |
| Chemistry | Was actual fluid/environment consistent with compatibility assumptions? |
| Installation | Were assumed installation and damage controls achieved? |
| Joining | Were qualification/execution/inspection assumptions achieved? |
| External loads | Were settlement, restraint, support or third-party loads omitted or underestimated? |

A failure can therefore expose one of three broad conditions:

1. the Design Basis was correct but execution/product condition departed from it;
2. execution matched the Design Basis but the Design Basis was incomplete or wrong;
3. several small deviations interacted.

That third category is often the one engineers miss.

## 10.7 Failure Lens workflow

**FIG-013-005 — PE Failure Lens**

```text
Failure / abnormal condition observed
                ↓
Preserve and document evidence
                ↓
Confirm product + material + geometry + service history
                ↓
Define multiple plausible mechanisms
                ↓
What evidence would distinguish them?
                ↓
Collect / test / examine
                ↓
Mechanism supported?
        ↙              ↘
      NO                YES
      ↓                  ↓
Revise hypotheses     Identify initiating
and continue          + contributing factors
        \                /
         ↓              ↓
      Reopen Design Basis
                ↓
Design / operation / installation /
joining / inspection response
                ↓
Check for fleet/system implications
                ↓
Document disposition
```

The important feature is the feedback loop.

If evidence does not support the preferred hypothesis, the engineer goes back and changes the hypothesis — not the evidence.

## 10.8 Evidence strength matters

Not all evidence carries the same weight.

A useful hierarchy is:

**Direct evidence**  
Measured dimensions, material identification, logged pressure/temperature, laboratory/fractographic evidence, verified joint records.

**Corroborating evidence**  
Installation records, operator statements, photographs, maintenance history, similar failures.

**Inference**  
Engineering interpretation connecting the evidence to a mechanism.

**Assumption**  
A proposition used because evidence is missing.

The review record should distinguish these explicitly.

A strong conclusion is not one written confidently. It is one supported by an evidence chain.

## 10.9 What the design engineer should do with the result

Failure analysis has little engineering value if it ends with a mechanism name.

The final question is:

> **What must change because we now know this?**

Possible dispositions include:

- no design change — isolated verified execution defect;
- revise installation/damage-control requirements;
- revise joining qualification or inspection;
- revise allowable service envelope;
- change SDR or product configuration;
- change material/product qualification requirements;
- add transient or structural analysis;
- revise chemical compatibility basis;
- inspect similar installed assets;
- restrict operation pending further evidence;
- update Design Basis assumptions;
- escalate to specialist forensic analysis.

The response must correspond to the demonstrated mechanism and uncertainty.

## 10.10 Know when this chapter is no longer enough

This Failure Lens is intentionally limited.

Escalate to specialist failure analysis when, for example:

- safety or regulatory consequences are significant;
- evidence is conflicting;
- fracture interpretation is central to the conclusion;
- litigation/insurance implications exist;
- laboratory characterization is required;
- repeated fleet failures occur;
- the initiating mechanism remains uncertain;
- or the proposed corrective action depends strongly on an unverified hypothesis.

The chapter should help the engineer recognize the need for specialist work — not pretend to replace it.

## 10.11 Engineering decision from Investigation 10

The useful output is not:

> “Failure mode: SCG.”

It is something closer to:

> **Observed condition:** documented.  
> **Initiating mechanism:** supported / probable / unresolved.  
> **Contributing factors:** identified with evidence.  
> **Design Basis deviations:** identified.  
> **Uncertainty:** explicitly recorded.  
> **Corrective action:** linked to demonstrated evidence.  
> **Fleet/system implication:** assessed.

And the closing rule:

> **Failure appearance generates hypotheses. Evidence supports mechanisms. Engineering action follows the supported mechanism and its uncertainty.**

## Investigation 10 boundary

This closes the arc that started in Investigation 4:

**Investigation 4:** why long-term and local crack behaviour matter.  
**Investigations 5–8:** how long-term evidence becomes a pressure-design basis.  
**Investigation 9:** how that basis becomes a project decision.  
**Investigation 10:** how real-world evidence feeds back into that decision.
