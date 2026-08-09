# Chapter 13 — Standards Validation Pass 04

**Scope:** pipe marking, PE100-RC terminology, and slow-crack-growth qualification pathways  
**Chapter:** 013 — Polyethylene (PE)  
**Branch:** `chapter-013-redevelopment`  
**Status:** Standards Validation evidence  
**PDS baseline:** 1.0 (frozen)

## 1. Purpose

Validate the remaining Chapter 13 hold points associated with:

1. what may safely be inferred from pipe marking;
2. the standards status and engineering meaning of the term `PE100-RC`;
3. the current ISO slow-crack-growth (SCG) test-method landscape;
4. whether the chapter may treat SCG methods or PE100-RC terminology as equivalent to a separate pressure-design class.

This pass uses current official ISO public records only. Where public ISO records do not expose the normative clause-level requirement, the item remains a controlled hold rather than being filled from memory or secondary sources.

---

## 2. Pipe marking — validation disposition

Current official ISO product records confirm that pipe product standards contain product requirements and that older ISO 4437 editions explicitly included marking requirements for gaseous-fuel PE pipes. Current ISO 4427-2:2019 and ISO 4437-2:2024 remain the relevant published pipe-product standards for the water and gas standards paths respectively.

However, the public ISO records available in this pass do **not** expose the complete current mandatory marking field list, marking frequency, permanence requirements, wording, traceability structure or any service-specific marking syntax.

### Disposition

**PASS for the chapter's interpretation framework; CONTROLLED HOLD for mandatory marking content.**

The current Chapter 13 table — “what pipe marking may tell the engineer / what it does not establish by itself” — is technically appropriate and should remain non-normative.

The chapter shall **not** state a universal mandatory marking list until the authoritative current product standard text has been checked.

### Publication rule

Retain:

> The pipe marking tells the engineer what product is being presented. It does not tell the engineer whether the complete installed system satisfies the project Design Basis.

Do not add clause-level statements such as “the pipe shall be marked with X, Y, Z” without the full governing product-standard text.

---

## 3. PE100-RC — standards-status validation

Official ISO public material does recognize the term `PE100-RC`. ISO/TR 10358:2021, a current ISO Technical Report on combined chemical resistance of plastics piping materials, explicitly lists `PE100-RC` among examples of PE-HD materials alongside PE63, PE80, PE100 and PE-RT.

This is sufficient to establish that `PE100-RC` is not merely an invented commercial phrase outside ISO usage.

It is **not** sufficient to establish that:

- PE100-RC is a separate MRS class from PE100;
- PE100-RC has a different design-stress relationship;
- PE100-RC has a different pressure-rating equation;
- PE100-RC permits a lower design coefficient `C`;
- PE100-RC automatically changes SDR/PN/PFA/MOP relationships;
- PE100-RC automatically permits arbitrary installation damage;
- every product advertised as PE100-RC has passed the qualification route required by a particular product/application standard.

### Disposition

**PARTIAL PASS / CONTROLLED HOLD.**

Chapter 13 may state that `PE100-RC` is terminology recognized in ISO documentation and is associated in industry with enhanced resistance to slow crack growth, but final publication text shall tie any engineering claim to the qualification requirements of the governing product/application standard.

The chapter shall not describe PE100-RC as a separate pressure-design class unless the applicable authoritative standard explicitly establishes that relationship.

Recommended final wording principle:

> Enhanced SCG-resistance terminology such as PE100-RC is qualification information that must be tied to the governing product/application specification and its required test route. It shall not be treated as an independent project approval or as automatic permission to change the pressure-design basis.

---

## 4. Current SCG test methods

### ISO 13479:2022

Current published edition: **ISO 13479:2022**, Edition 3.

The official ISO abstract confirms that it is a test method for resistance to slow crack growth of polyolefin pipes using a hydrostatic-pressure test on pipe specimens with machined longitudinal external notches. The public scope states applicability to pipes with wall thickness greater than 5 mm.

### ISO 18488:2025

Current published edition: **ISO 18488:2025**, Edition 2. The previous 2015 edition is withdrawn.

The official ISO abstract confirms that the method determines **strain-hardening modulus** as a measure of resistance to slow crack growth of polyethylene, using compression-moulded samples and true-stress/draw-ratio behaviour. The method is stated to be valid for all types of polyethylene used for pipe and fitting applications, independent of manufacturing technology, comonomer or catalyst type.

### Engineering interpretation

These methods assess SCG resistance using fundamentally different test concepts:

- `ISO 13479` — notched pipe + hydrostatic time-to-failure response;
- `ISO 18488` — material strain-hardening modulus from compression-moulded samples.

### Disposition

**PASS for method differentiation.**

Chapter 13 is correct not to treat the two methods as interchangeable evidence by default.

The governing product/application specification must establish which method, threshold, acceptance criterion or combination is required.

---

## 5. Qualification route versus pressure-design route

The official ISO records reviewed in this pass support keeping two engineering branches separate:

`long-term hydrostatic classification / MRS / design stress / SDR / pressure basis`

and

`SCG-resistance qualification / damage-mechanism evidence`

No public official record reviewed here supports collapsing those branches into one rule such as:

`PE100-RC → different MRS`  
or  
`PE100-RC → higher allowable pressure`.

### Disposition

**PASS for Chapter 13 architecture.**

The chapter's current statement that SCG qualification demonstrates resistance to a defined mechanism under a defined test framework — rather than immunity from arbitrary installation damage — is retained.

---

## 6. Marking and SCG — controlled inference boundary

A marking or product designation may help identify:

- manufacturer and traceability path;
- material designation claimed by the manufacturer;
- dimensional series / SDR;
- product-standard claim;
- pressure designation where used by the governing standard;
- production/batch information where required.

It does **not**, by itself, prove:

- project pressure acceptability;
- elevated-temperature capability;
- fluid compatibility;
- absence of installation damage;
- joining quality;
- satisfaction of all SCG qualification criteria;
- applicability of the product standard to the actual project service.

This interpretation remains suitable for `TAB-013-002`.

---

## 7. Lifecycle / edition observations

- `ISO 13479:2022` is the current published notched-pipe SCG test method.
- `ISO 18488:2025` is the current published strain-hardening-modulus SCG method; `ISO 18488:2015` is withdrawn.
- `ISO 4427-2:2019` remains the published PE pipe product standard for water / pressure drainage applications but is under active revision.
- `ISO 4437-2:2024` remains the published PE pipe product standard for gaseous-fuel applications but is expected to be replaced by a new edition in the current revision cycle.

Therefore, the final Design Freeze must include an edition-status recheck immediately before publication.

---

## 8. Chapter 13 text disposition

### Safe to retain now

1. PE100-RC shall not be presented as universal project approval.
2. Enhanced SCG-resistance terminology shall be tied to a defined qualification route.
3. ISO 13479 and ISO 18488 shall be described as different SCG assessment concepts.
4. Marking shall be treated as product-identification/traceability information, not as the complete Design Basis.
5. Successful SCG qualification shall not be described as immunity to arbitrary gouges, notches, poor joints or service outside the qualified envelope.

### Remains on hold

1. Exact mandatory marking fields and marking frequency for current ISO 4427-2 / ISO 4437-2.
2. Exact product-standard recognition and acceptance criteria for the term PE100-RC.
3. Exact required SCG test route and threshold by each product/application standard.
4. Any claim that PE100-RC changes MRS, `C`, design stress or pressure rating.
5. Any equivalence rule between ISO 13479 and ISO 18488.

---

## 9. Pass 04 decision

**Decision: PARTIAL PASS / CONTROLLED HOLD.**

The chapter's conceptual treatment of marking, PE100-RC and SCG qualification is technically sound and does not require structural rewrite.

The remaining uncertainty is normative rather than conceptual: exact mandatory marking content, PE100-RC acceptance status in the applicable product standard, and specific SCG acceptance criteria require authoritative full-standard access.

No current evidence justifies changing the chapter's pressure-design equations or treating PE100-RC as a separate pressure-design class.

## 10. Next Standards Validation pass

Proceed to **Pass 05 — ISO 9080 regression / lower-confidence terminology / reference conditions / classification interface**, then consolidate all remaining controlled holds into one final Standards Validation closure register before Design Freeze.
