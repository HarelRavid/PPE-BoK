# Chapter 13 — References and Evidence Register

**Chapter:** 013 — Polyethylene (PE)  
**PDS baseline:** 1.0  
**Status:** Standards-validation candidate  
**Last authoritative public-source status check:** 2026-08-14  
**Academic/Evidence Review:** PASS for current core claim set — 2026-08-14

## 1. Source-control rule

This register separates three evidence states:

1. **Authoritative public-source validated** — identity, publication status, edition and public scope have been checked against the issuing body's current public record.
2. **Authoritative full-text hold** — an exact clause, table, equation, coefficient, rounding rule, marking requirement or acceptance criterion requires the current full normative text and is not treated as closed from an abstract, preview, secondary report or historical edition.
3. **Supporting evidence** — textbooks, peer-reviewed literature, professional guidance and manufacturer/industry material may support explanation or context but do not replace an applicable normative standard.

No secondary or project-internal report is used to close an ISO normative claim.

---

## 2. Authoritative standards map

| Standard | Current published source status checked 2026-08-14 | Chapter use | Validation state |
|---|---|---|---|
| ISO 9080:2012 | Edition 2; Published; Confirmed | Statistical extrapolation of long-term hydrostatic strength of thermoplastics materials in pipe form | Public identity/scope/current-edition status validated; exact statistical terminology, data rules, extrapolation limits and branch/knee rules remain full-text holds |
| ISO 12162:2009 | Edition 2; Published; Confirmed | Thermoplastics material classification, designation and design-stress method | Public identity/scope/current-edition status validated; exact MRS class/rounding, design-coefficient and design-stress details remain full-text holds |
| ISO 4427-1:2019 | Edition 2; Published; revision in development | General PE water / pressure drainage-sewerage system framework | Public scope/status validated; final clause/table use remains full-text hold and edition shall be rechecked before Design Freeze |
| ISO 4427-2:2019 + Amd 1:2023 | Published; amendment published; revision in development | PE water / pressure drainage-sewerage pipe requirements | Public status validated; exact SDR/pressure/marking requirements remain full-text holds |
| ISO 4437-1:2024 | Edition 2; Published; replacement FDIS in development | General PE gaseous-fuel system framework | Public scope/status and published service-envelope summary validated; final clause use remains full-text hold and edition shall be rechecked before Design Freeze |
| ISO 4437-2:2024 | Edition 2; Published; replacement project in development | PE gaseous-fuel pipe requirements | Public status validated; exact SDR/pressure/marking requirements remain full-text holds |
| ISO 4437-5:2024 | Edition 2; Published | Fitness for purpose of assembled PE gas piping systems, including joint/system assessment | Public scope/status validated; exact derating and acceptance details remain full-text holds where used numerically |
| ISO 1167 series | Current published parts as applicable | Resistance-to-internal-pressure test framework for pipes/components/assemblies | Standards-family role validated; use exact applicable part and current edition during final clause review |
| ISO 21307:2017 + Amd 1:2020 | Published/current | PE butt-fusion procedure framework | Public identity/status validated; detailed joining procedure intentionally outside Chapter 13 scope |
| ISO 13479:2022 | Edition 3; Published/current | Notched-pipe hydrostatic slow-crack-growth assessment | Public identity/scope validated |
| ISO 18488:2025 | Edition 2; Published/current | Strain-hardening modulus related to PE slow-crack-growth resistance | Public identity/scope validated; supersedes the withdrawn 2015 edition |
| ISO/TS 26873:2010 | Published/current; confirmed | Reference-line concepts for creep rupture properties of thermoplastics pipes | Public identity/scope validated; exact mathematical procedures are not reproduced in this chapter |
| ISO/TR 10358:2021 | Published | Combined chemical-resistance data / contextual terminology | Contextual source only; not a pressure-design or PE100-RC qualification approval |

### Current-edition warning

The ISO 4427 and ISO 4437 families are in active revision cycles. The current **published** editions listed above remain the publication basis unless a replacement International Standard is published and adopted before Chapter 13 Design Freeze. Draft DIS/FDIS documents are not silently treated as the governing published standard.

---

## 3. Controlled normative holds

The following items are deliberately **not closed** without authoritative full-text review of the current applicable standard:

### SVH-013-01 — ISO 12162 classification/design-stress chain

- exact current definition and notation of MRS;
- standardized class/rounding series and the exact PE100 mapping;
- exact design-coefficient `C` definition, selection/minimum rules and applicability;
- exact design-stress formula notation and required rounding.

### SVH-013-02 — ISO 9080 regression/extrapolation

- exact current name/definition of the conservative lower statistical quantity;
- exact notation;
- data requirements and permitted extrapolation limits;
- branch/knee determination and statistical rules.

### SVH-013-03 — ISO 4427 product/application details

- exact PFA/PN/SDR relationships and tables;
- exact temperature-treatment clauses/table values used numerically;
- exact current mandatory pipe-marking fields, frequency and traceability requirements.

### SVH-013-04 — ISO 4437 product/application details

- exact current MOP calculation and rounding path;
- exact design-coefficient/application rules;
- RCP constraints affecting system pressure designation;
- exact temperature-derating coefficients if a numerical example is added;
- exact pipe marking and component/joint limitations.

### SVH-013-05 — PE100-RC and SCG qualification

- exact product/application-standard acceptance route for PE100-RC or equivalent enhanced-SCG-resistance terminology;
- required SCG test method(s), thresholds and equivalence rules;
- any pressure-design implication, if explicitly established by the governing standard.

These holds block final Design Freeze where they affect normative statements. They do not invalidate the chapter's engineering architecture.

---

## 4. Chapter wording rules while holds remain

Until the full-text holds are closed:

- use **reference pressure basis** for the generic MRS/design-stress/SDR arithmetic result;
- use **PFA** only in an explicit ISO 4427 water-service context;
- use **MOP** only in an explicit ISO 4437 gas-service context;
- do not treat PN, PFA and MOP as generic synonyms;
- keep `MRS = 10 MPa`, `C = 1.25` and the resulting 16 bar arithmetic explicitly illustrative wherever used and not clause-verified;
- do not present PE100-RC as a separate pressure-design class unless the governing current standard explicitly establishes such a relationship;
- distinguish SCG test concepts rather than treating ISO 13479 and ISO 18488 as automatically interchangeable evidence;
- do not state a universal mandatory pipe-marking field list without the current full product-standard text.

---

## 5. Primary academic / experimental evidence

The primary-research set below was directly reviewed for the current Chapter 13 core mechanism claims. Detailed claim mapping and transferability limits are recorded in `reviews/chapter-013/ACADEMIC-EVIDENCE-REVIEW-2026-08-14.md`.

### AE-013-01 — Ductile / SCG long-time failure transition

Brown, N.; Donofrio, J.; Lu, X. “The transition between ductile and slow-crack-growth failure in polyethylene.” *Polymer* 28(8), 1326–1330 (1987). DOI: `10.1016/0032-3861(87)90446-0`.

**Use:** supports the distinction between long-time creep/ductile failure and brittle slow-crack-growth failure and the existence of a mechanism transition under different time/stress conditions.  
**Limit:** not a universal project transition criterion or design allowable.

### AE-013-02 — Branching / tie molecules / morphology and SCG

Huang, Y.-L.; Brown, N. “Dependence of slow crack growth in polyethylene on butyl branch density: Morphology and theory.” *Journal of Polymer Science Part B: Polymer Physics* 29(1), 129–137 (1991). DOI: `10.1002/polb.1991.090290116`.

**Use:** primary evidence linking branching, lamellar/morphological parameters and tie-molecule concepts to SCG behaviour.  
**Limit:** quantitative relationships are system/material specific.

### AE-013-03 — Notched constant-load SCG sensitivity

Lu, X.; Zhou, Z.; Brown, N. “A sensitive mechanical test for slow crack growth in polyethylene.” *Polymer Engineering & Science* 37(11), 1896–1900 (1997). DOI: `10.1002/pen.11839`.

**Use:** supports the importance of notch/crack-growth resistance and the sensitivity of SCG to molecular structure and morphology.  
**Limit:** specimen-level accelerated testing does not establish arbitrary installed-system damage acceptance.

### AE-013-04 — Amorphous-phase mobility / craze-fibril mechanism

Men, Y. F.; Rieger, J.; Enderle, H.-F.; Lilge, D. “The mobility of the amorphous phase in polyethylene as a determining factor for slow crack growth.” *European Physical Journal E* 15(4), 421–425 (2004). DOI: `10.1140/epje/i2004-10059-3`.

**Use:** supports the role of amorphous-phase mobility and craze-fibril development in PE SCG for the materials studied.  
**Limit:** the reported correlation is not a substitute for product/application-standard qualification.

### AE-013-05 — Morphology influence on HDPE SCG

Pan, Y.; Gao, X.; Wang, Z.; Lei, J.; Li, Z.; Shen, K. “Effect of different morphologies on slow crack growth of high-density polyethylene.” *RSC Advances* 5, 28191–28202 (2015). DOI: `10.1039/C5RA00918A`.

**Use:** experimental evidence that different HDPE morphologies can materially alter SCG behaviour.  
**Limit:** the special specimen-processing route is not a quantitative surrogate for every extruded pressure-pipe product.

### AE-013-06 — HDPE creep / time-temperature / thermal-history evidence

Pilz, G.; Wurzer, S.; Morak, M.; Pinter, G. “Assessment of the stepped isothermal method for accelerated creep testing of high-density polyethylene.” *Mechanics of Time-Dependent Materials* 26, 775–790 (2022). DOI: `10.1007/s11043-021-09512-1`.

**Use:** experimental evidence for time- and temperature-dependent HDPE creep/viscoelastic response, non-linearity at higher loading/temperature and thermal-history/morphology effects.  
**Limit:** SIM on the tested HDPE material is not the ISO 9080 normative pipe-form qualification route.

### AE-013-07 — Long-term plasticity-controlled PE100 failure

Kanters, M. J. W.; Remerie, K.; Govaert, L. E. “A new protocol for accelerated screening of long-term plasticity-controlled failure of polyethylene pipe grades.” *Polymer Engineering & Science* 56(6), 676–688 (2016). DOI: `10.1002/pen.24294`.

**Use:** primary PE100 pipe-grade evidence that long-term failure behaviour is rate/time/temperature dependent and cannot be inferred from one short-term strength number.  
**Limit:** research protocol, not the governing classification/product-standard method.

### AE-013-08 — Cyclic crack growth / SCG in HDPE pipe

Gao, B.; Luo, M.; Lin, K.; Ding, J.; Liu, B. “Fatigue crack growth and slow crack growth of HDPE pipes under internal pressure and flat plate compression.” *International Journal of Pressure Vessels and Piping* 208, 105155 (2024). DOI: `10.1016/j.ijpvp.2024.105155`.

**Use:** primary pipe-level evidence that pulsatile loading and local cracks can affect HDPE crack growth and that fatigue/SCG interactions require separate engineering attention.  
**Limit:** no universal fatigue design curve or cycle limit is inferred from the tested geometry/conditions.

### Academic review disposition

The current core non-normative material/mechanism claim set is **adequately supported for Chapter 13 engineering depth**. Future new material technical claims reopen Academic/Evidence Review for those claims. Deeper polymer morphology, constitutive viscoelasticity, fracture mechanics and fatigue methodology remain intentionally allocated to later dedicated chapters.

### Historical project literature

Project-internal literature reviews and earlier Chapter 13 development artifacts may be retained as supporting context and provenance. They are not authoritative normative sources and shall not be used to close the controlled ISO holds above.

---

## 6. Evidence maturity summary

| Evidence layer | Status |
|---|---|
| Engineering narrative / mechanisms | Technical Review passed in redevelopment evidence |
| Equations / units / worked-example arithmetic | Technical Review passed in redevelopment evidence |
| Current standards identity / public scope / lifecycle status | Rechecked against official ISO public records on 2026-08-14 |
| Current authoritative clause/table/equation validation | **OPEN — controlled holds SVH-013-01 through SVH-013-05** |
| Academic / peer-reviewed evidence normalization | **PASS for current core claim set — review dated 2026-08-14** |
| Final claim-level citation placement / source formatting | OPEN — editorial stage |
| Final editorial/style review | OPEN |
| Design Freeze | BLOCKED until required holds and Definition-of-Done gates close |

---

## 7. Final source rule

If this register, a prior draft, a project report or secondary literature conflicts with the current authoritative applicable standard, the authoritative standard governs and Chapter 13 shall be corrected before publication approval.
