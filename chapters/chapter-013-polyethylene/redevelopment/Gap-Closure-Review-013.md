# Chapter 13 — Gap Closure Review

**Chapter:** 013 — Polyethylene (PE)  
**Review basis:** RDP-013 + GAP Register + integrated Chapter 13 Rev 1.0 candidate  
**Branch:** `chapter-013-redevelopment`  
**PDS baseline:** 1.0 (frozen)  
**Review stage:** Post-integration, pre-Technical Review / pre-Standards Validation

## Status definitions

- **CLOSED — content:** acceptance criterion is satisfied in the integrated chapter; publication hold points may still remain globally.
- **OPEN — standards validation:** engineering content exists, but the linked gap cannot be formally closed until authoritative current standards are validated.
- **OPEN — verification:** content exists, but an independent calculation/review requirement remains.
- **OPEN — asset:** a required engineering asset is still missing or not explicit enough.

## Work-package closure review

| WP | Linked gap(s) | Review result | Closure evidence | Status |
|---|---|---|---|---|
| WP-013-01 | A01, E05 | Investigation 4 is mechanism/screening focused; long-term evidence generation is in 5–6 and detailed failure evidence is in 10. No substantive failure-forensics duplication remains in Investigation 4. | Investigation 4 explicitly defers detailed failure evidence to Investigation 10 and evidence-generation detail to Investigations 5–6. | **CLOSED — content** |
| WP-013-02 | A02 | Investigation 8 now includes explicit pipe-marking interpretation. | `TAB-013-002` states what marking may tell the engineer and what it does not establish; includes interpretation workflow and misuse warning. | **CLOSED — content** |
| WP-013-03 | A03 | Investigation 9 functions as the integration/decision workflow rather than a catch-all technical chapter. | Workflow starts at Design Basis and ends in explicit `GO / CONDITIONAL GO / NO-GO`; specialist subjects remain interfaces rather than duplicated treatments. | **CLOSED — content** |
| WP-013-04 | A04 | Chapter closure is present and reconnects the engineering chain to Design Basis and residual project-specific work. | Chapter Engineering Closure + residual project-specific engineering + publication hold point. | **CLOSED — content** |
| WP-013-05 | E01 | Candidate-screening tool exists in Investigation 1. | Screening table links PE characteristic → possible engineering benefit → design obligation. | **CLOSED — content** |
| WP-013-06 | E02 | Classification / terminology reference table exists. | `TAB-013-001` distinguishes what each designation represents, what it gives the engineer and what it does not prove. | **CLOSED — content** |
| WP-013-07 | E03 | PE100-RC treatment is structurally present but final claims remain intentionally held. | Investigation 3 requires a defined qualification route and explicitly retains a Standards Validation Hold Point for recognition, test route, acceptance criteria and pressure/design implications. | **OPEN — standards validation** |
| WP-013-08 | E04 | Equation 13-01 metadata is complete at engineering-use level. | `EQ-013-001` includes symbols, units, derivation basis, assumptions, engineering use, applicability limit and common misuse. | **CLOSED — content** |
| WP-013-09 | E06 | SCG discussion is tied to a qualification/testing pathway without reproducing test standards. | Investigation 4 provides `defect risk → required SCG evidence → governing standard → referenced test method → qualification → separate installation/system assessment`; Investigation 3 identifies example SCG test routes. | **CLOSED — content** |
| WP-013-10 | P01 | Quick Navigation aid has been integrated and passes the desk-use criterion at chapter level. | Navigation directs screening → 1–4, pressure/classification → 5–8, project selection → 9, failure → 10, final design check → `CL-013-001`. | **CLOSED — content** |
| WP-013-11 | P02 | Investigation 5 explains the long-term evidence chain and controlled extrapolation at engineering-use depth. | Pipe-form evidence chain, multiple stress levels, temperature acceleration, extrapolation limits, knee/failure-branch relevance and supplier-review questions are present. | **CLOSED — content** |
| WP-013-12 | P02 | Investigation 6 explains regression interpretation without unnecessary statistical derivation. | Distinguishes observations, fitted behaviour and lower statistical bound; explains conservative meaning and bridge to MRS. | **CLOSED — content** |
| WP-013-13 | P02 | Investigation 7 provides MRS → C → design-stress chain with numbered equation and limitations. | `EQ-013-002`, definitions, units, standards basis, applicability limit, misuse warning and worked interpretation are present. | **CLOSED — content** |
| WP-013-14 | P02 | Investigation 8 contains SDR/pressure equations, marking interpretation and Worked Example A, but the RDP-required dedicated MRS/coefficient/SDR/pressure **reference table** is not yet explicit, and independent recalculation remains a completion-gate requirement. | `EQ-013-003`, `EQ-013-004`, Worked Example A, sensitivity table and `TAB-013-002` exist. A dedicated consolidated calculation-reference table is still missing. | **OPEN — asset + verification** |
| WP-013-15 | P02 | Investigation 9 and Worked Example B demonstrate changed-service re-evaluation and explicit disposition. However, the global RDP completion gate requires both worked examples to be independently recalculated; Example B is currently qualitative/decision-path based rather than a numerical calculation. | Changed-temperature scenario reopens standards, temperature/life basis, chemistry, component limits and final disposition. | **OPEN — verification / disposition required** |
| WP-013-16 | P02 | Investigation 10 Failure Lens and chapter Design Review Checklist are complete. | `TAB-013-004`, `FIG-013-005` and `CL-013-001` are present; Failure Lens remains bounded from specialist forensic analysis. | **CLOSED — content** |

## Gap Register disposition

| Gap ID | Disposition after integration | Formal status recommendation |
|---|---|---|
| GAP-013-A01 | Investigation boundaries corrected. | **Close** |
| GAP-013-A02 | Pipe-marking interpretation added. | **Close** |
| GAP-013-A03 | Investigation 9 converted to integration/decision workflow. | **Close** |
| GAP-013-A04 | Chapter closure added. | **Close** |
| GAP-013-E01 | Candidate-screening table added. | **Close** |
| GAP-013-E02 | Classification/terminology table developed. | **Close** |
| GAP-013-E03 | Content drafted; authoritative current Standards Validation still required. | **Keep open** |
| GAP-013-E04 | EQ-013-001 metadata completed. | **Close** |
| GAP-013-E05 | Detailed failure evidence moved to Investigation 10. | **Close** |
| GAP-013-E06 | SCG linked to qualification/testing pathway. | **Close content gap; retain standards validation hold point** |
| GAP-013-P01 | Quick Navigation added and retained. | **Close** |
| GAP-013-P02 | Most reference layer is complete, but WP-013-14 still lacks the dedicated consolidated MRS/C/SDR/pressure reference table and the RDP independent-example verification gate is not complete. | **Keep open** |

## Findings that prevent formal RDP closure

### 1. Missing consolidated pressure-design reference table

RDP-013 requires a minimum asset described as an **MRS / coefficient / SDR / pressure reference table**, and WP-013-14 requires a reference table in addition to numbered equations and Worked Example A.

The integrated chapter currently has:

- `TAB-013-001` — classification / terminology;
- `TAB-013-002` — pipe marking;
- `TAB-013-003` — Design Input / Verification Matrix;
- `TAB-013-004` — Failure Evidence / Engineering Response Matrix;
- an unnumbered sensitivity table in Investigation 8.

None is yet a single consolidated calculation-reference table covering the complete `MRS → C → design stress → SDR → reference pressure` chain.

**Required action:** add `TAB-013-005 — PE pressure-design relationship reference`, clearly marked as an engineering calculation aid and subject to final standards validation.

### 2. Independent recalculation gate remains open

RDP-013 states that closure requires both worked examples to be independently recalculated.

- **Worked Example A:** numerical and suitable for independent arithmetic/unit recalculation.
- **Worked Example B:** currently qualitative. The review must either (a) add a controlled numerical calculation suitable for independent recalculation, or (b) formally disposition the RDP wording so Example B is independently *reperformed/reviewed* as a decision-path example rather than falsely claiming numerical recalculation.

No formal closure should be recorded until this is resolved.

### 3. PE100-RC / current-standard validation remains open

GAP-013-E03 was explicitly defined as a Standards Validation hold point. It cannot be closed from the current engineering narrative alone.

### 4. Global final gates remain pending

Even content-closed work packages do not make the chapter publication-ready. RDP closure still requires:

1. Technical Review;
2. independent example verification;
3. final authoritative Standards Validation;
4. resolution of any changes generated by those reviews.

## Overall disposition

**Chapter 13 Rev 1.0 engineering integration: SUBSTANTIALLY COMPLETE.**

**RDP-013: NOT YET CLOSED.**

The remaining pre-review work is narrow and controlled:

1. create `TAB-013-005` consolidated pressure-design reference table;
2. independently recalculate Worked Example A;
3. resolve the verification method for Worked Example B and perform it;
4. then proceed to Technical Review;
5. then perform the dedicated final Standards Validation, including PE100-RC and all equation/coefficient/marking/temperature hold points.

No new Investigation is required by this Gap Closure Review.
