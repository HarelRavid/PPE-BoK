# Chapter 13 — Editorial / Style Review

**Record date:** 2026-08-14  
**Chapter:** 013 — Polyethylene (PE)  
**PDS baseline:** 1.0  
**Review type:** Editorial / Style / Navigation Review  
**Decision:** CONDITIONAL PASS — no structural rewrite required

## 1. Review purpose

This review checks the consolidated Chapter 13 manuscript against the active PDS 1.0 Style Guide and current repository architecture after Technical Review and Academic/Evidence Review.

The review does not change engineering meaning and does not attempt to resolve normative terminology that remains blocked by authoritative full-text Standards Validation.

---

## 2. Architecture and heading hierarchy

### Result: PASS

The active Style Guide permits an Investigation-led chapter structure using:

- `# Chapter NNN — Title`;
- chapter-level sections as appropriate;
- `# Investigation N — Engineering Question` for Investigation-led structure;
- `##` / `###` for subsections within an Investigation.

Chapter 13 follows that pattern consistently across Investigations 1–10. The chapter-level standards map, Design Basis inputs and Quick Navigation precede the Investigations and provide useful non-linear navigation.

No heading-level restructuring is required.

---

## 3. Chapter flow and progression

### Result: PASS

The chapter maintains a coherent engineering progression:

`material/system value → molecular/morphological basis → material designation → time-dependent behaviour → long-term evidence → regression interpretation → MRS/design stress → SDR/pressure basis → project design decision → failure evidence feedback`

The progression supports the CDB engineering question and avoids turning the chapter into either a polymer-science textbook or a narrow pressure-rating worksheet.

Repeated decision-chain statements are used as controlled reinforcement at phase transitions. They do not currently create enough redundancy to justify structural rewrite.

---

## 4. Terminology consistency

### Result: CONDITIONAL PASS

The manuscript consistently distinguishes:

- material classification from product qualification and system design;
- MRS from design stress;
- SDR from pressure capability;
- reference pressure basis from project allowable operating pressure;
- SCG resistance evidence from immunity to damage;
- failure observation from mechanism/root cause.

The phrase **reference pressure basis** is used deliberately to avoid presenting generic arithmetic as an application-standard allowable pressure.

### Source-dependent terminology holds

Two terms remain intentionally non-final because the current full normative ISO text is not available:

1. `σ_LCL` in Investigation 7.2;
2. `lower prediction/confidence boundary` in the FIG-013-003 description / surrounding regression discussion.

These are not editorial defects to be guessed away. They shall be normalized after `SVH-013-01` / `SVH-013-02` are closed against authoritative current ISO 12162 / ISO 9080 full text.

The historical/project-literature `MOP` formula in Investigation 8.2 is already bounded in the manuscript by immediately reclassifying the generic arithmetic as a **reference pressure basis** pending the governing product/application standard. Final terminology shall be checked during the same Standards closure.

---

## 5. Engineering asset conventions

### Result: PASS for authoring stage

The chapter uses the active controlled asset conventions:

- `EQ-013-001` through `EQ-013-004`;
- `FIG-013-001` through `FIG-013-007`;
- `TAB-013-001` through `TAB-013-005`;
- `EX-013-001` and `EX-013-002`;
- `CL-013-001`.

Equation assets define units, assumptions, applicability and misuse where required. Tables have engineering-purpose titles. The checklist is registered as one controlled asset; local row labels `CL-01` through `CL-20` function as internal checklist-item labels and do not create competing book-level asset identities.

No duplicated controlled asset ID was identified in the consolidated register.

---

## 6. Visual placeholders

### Result: PASS for authoring / OPEN for publishing

The chapter appropriately retains visual production as a later controlled publishing task.

Current visual state:

- `FIG-013-001` — placeholder, semicrystalline PE structure → engineering consequence;
- `FIG-013-002` — placeholder, SCG/local-notch concept;
- `FIG-013-003` — figure concept defined; final original figure pending;
- `FIG-013-004` — integrated text schematic;
- `FIG-013-005` — integrated Failure Lens schematic;
- `FIG-013-006` — placeholder, evidence → classification → marking chain;
- `FIG-013-007` — placeholder, pipe-marking anatomy.

This is compliant with the PDS rule that finished visuals are not required merely to close Authoring. Publishing remains responsible for final visual production where the engineering value justifies it.

---

## 7. Worked-example presentation

### Result: PASS

The two examples follow the intended PDS logic:

- Example A separates arithmetic verification from standards applicability and explicitly states what the 16 bar reference calculation does not prove.
- Example B uses a changed Design Basis to teach revalidation logic without inventing an unsupported numerical temperature factor.

The second example's independent check is correctly treated as a re-performance of the engineering decision path rather than fake numerical precision.

---

## 8. Cross-references and navigation

### Result: PASS

Internal references to Investigations and controlled asset IDs are stable and understandable.

The manuscript avoids unnecessary dependence on future final chapter numbers. Interfaces such as detailed joining, structural analysis, buried-pipe mechanics and specialist failure analysis are identified by discipline rather than by an invented final TOC location.

The Quick Navigation and chapter-end asset register materially improve desk-use performance.

---

## 9. Tone and objectivity

### Result: PASS

The manuscript is professional, direct and engineering-oriented. It repeatedly exposes limits and prevents common overclaims, including:

- PE100 is not project approval;
- nominal pressure is not complete system capability;
- SCG qualification is not immunity from arbitrary damage;
- failure location is not automatically root cause;
- arithmetic correctness is not standards applicability.

The tone is appropriately cautionary without becoming promotional or absolute.

---

## 10. Citation and source placement

### Result: OPEN — final editorial/source-formatting action

The active `references.md` now contains the authoritative standards map, controlled standards holds and the primary academic evidence set `AE-013-01` through `AE-013-08`.

The consolidated manuscript itself does not yet contain final claim-level citation placement for those academic sources. This shall be completed during the final source-formatting/editorial pass after standards-dependent wording is stabilized, so citations are not repeatedly moved during technical correction.

Required final action:

- place compact citations at the principal material/mechanism claims in Investigations 2–5 and the cyclic-loading statement in Investigation 9;
- avoid citation clutter where one source clearly supports a compact cluster;
- keep standards citations distinct from academic mechanism citations;
- ensure every final citation maps to an entry in `references.md`.

---

## 11. Metadata synchronization

### Result: OPEN — merge/publication-state action

The manuscript front matter still reflects the historical consolidation date and pre-review state (`academic: pending`, `editorial: pending`, `last_updated: 2026-08-09`).

Because the current clean PR is still a Draft integration candidate, metadata shall be synchronized once this review package is accepted and before or during the approved integration revision:

- `academic` → pass for current claim set;
- `editorial` → conditional/pass status consistent with this record and the remaining source-formatting hold;
- `last_updated` → current integration revision date;
- retain `standards: pending` while full-text holds remain;
- retain non-frozen chapter status.

This is a metadata/editorial action only and shall not silently change engineering content.

---

## 12. Editorial findings register

| Finding | Severity | Status | Required action |
|---|---|---|---|
| ED-013-01 — final claim-level academic citation placement | Medium | OPEN | Add after standards-dependent wording stabilizes |
| ED-013-02 — `σ_LCL` exact terminology/notation | Hold / source-dependent | OPEN under SVH-013-01/02 | Resolve from current authoritative ISO full text |
| ED-013-03 — `lower prediction/confidence` wording | Hold / source-dependent | OPEN under SVH-013-02 | Resolve from current authoritative ISO 9080 full text |
| ED-013-04 — front-matter review/status/date synchronization | Low | OPEN | Update in approved integration/final editorial revision |
| ED-013-05 — final visual production | Publishing | OPEN | Produce approved figures during Publishing where required |

No High or Critical editorial finding is open.

---

## 13. Review decision

**CONDITIONAL PASS — Chapter 13 is structurally and stylistically mature and requires no editorial rewrite.**

The remaining editorial work is bounded to final citation placement, metadata synchronization, publishing visuals, and terminology that is legitimately dependent on the unresolved authoritative full-text standards holds.

This review supports controlled integration of the chapter as a standards-validation candidate. It does not authorize Design Freeze.