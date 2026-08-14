# Chapter 13 — Controlled Review Record

**Chapter:** 013 — Polyethylene (PE)  
**PDS baseline:** 1.0  
**Review state:** Standards-validation candidate / not publication frozen  
**Clean-integration branch:** `chapter-013-controlled-integration`  
**Review package synchronized:** 2026-08-14

## 1. Review purpose

This record consolidates the Chapter 13 maturity evidence needed in the active repository without importing the unrelated Chapter 000–012 rewrites and working debris contained in the historical `chapter-013-redevelopment` branch / PR #2.

The consolidated manuscript source is the mature Chapter 13 file developed on that branch and is brought into the current repository as `chapters/chapter-013-polyethylene/chapter.md`. The original development branch and closed PR #2 remain Git history / provenance, not the active integration path.

---

## 2. Source provenance

- Historical development branch: `chapter-013-redevelopment`
- Historical consolidated Chapter 13 blob: `70bd29e661946ac1a30474c7375d6dde208935fb`
- Historical PR: #2 — closed without merge; superseded as an integration vehicle
- Current integration PR: #8 — clean Chapter 13-only integration from the post-hygiene `main` baseline
- Current clean integration intentionally excludes unrelated modifications to Chapters 000–012.

---

## 3. PDS gate status

| Gate / review area | Status | Basis / disposition |
|---|---|---|
| Approved CDB exists | PASS | `docs/PDS/Chapter-Design-Briefs/CDB-013-Polyethylene.md` |
| Engineering narrative | PASS for redevelopment scope | Investigations 1–10 consolidated in manuscript |
| Design Basis integration | PASS | Explicit required-input section and project decision workflow |
| Engineering assets | PASS for authoring stage | Equations, tables, examples, checklist and figure placeholders registered |
| Physics / mechanisms | PASS | Historical Technical Review closed without unresolved physics findings |
| Equations | PASS | Core equations reviewed for algebra, dimensions, assumptions and use boundaries |
| Units | PASS | No open unit/dimensional findings in Technical Review |
| Worked examples | PASS for arithmetic/method | Examples independently recalculated or decision-path re-performed within stated assumptions; normative applicability remains subject to Standards Validation |
| Internal consistency | PASS for redevelopment scope | Gap Closure / integration / pre-Technical verification completed on source branch |
| Current standards identity / public scope / lifecycle | PASS | Rechecked against official ISO public records, latest check 2026-08-14 |
| Authoritative clause/table/equation validation | **OPEN** | Full current normative text not available in repository/session for remaining holds |
| Academic / evidence normalization | **PASS for current core claim set** | `reviews/chapter-013/ACADEMIC-EVIDENCE-REVIEW-2026-08-14.md` |
| Editorial / style review | **CONDITIONAL PASS** | No structural rewrite required; bounded source-formatting/metadata/standards-dependent terminology items remain |
| Final Design Freeze | **BLOCKED** | Requires closure/disposition of authoritative standards holds, final citation/metadata work, publishing actions as applicable and explicit author approval |

---

## 4. Technical Review closure carried forward

The redevelopment evidence records the following as complete:

- gap-closure review for the Chapter 13 redevelopment scope;
- pre-Technical verification;
- Technical Review;
- equation and unit checks;
- worked-example verification;
- integration of Investigations 1–10;
- engineering quick navigation;
- normalized engineering asset register;
- Chapter 13 design-review checklist;
- failure-evidence / engineering-response logic;
- chapter engineering closure.

No open physics, equation, unit, internal-consistency or example-arithmetic finding is currently known from that review history.

This review record does **not** elevate an unverified normative input into a standards-validated fact merely because the arithmetic using that input is correct.

---

## 5. Academic / Evidence Review closure

The current core non-normative material/mechanism claim set has been reviewed against primary research and passed for the engineering depth intended in Chapter 13.

The reviewed evidence set covers, with explicit transferability limits:

- semicrystalline morphology and SCG behaviour;
- branching / tie-molecule / morphology influence on SCG resistance;
- amorphous-phase mobility and craze-fibril mechanisms;
- time- and temperature-dependent HDPE creep response;
- long-term plasticity-controlled PE100 failure behaviour;
- transition between ductile/creep-controlled and slow-crack-growth failure;
- notch/local-defect relevance;
- cyclic crack-growth / SCG interaction under tested HDPE pipe conditions.

Full claim mapping, DOI-level citations and applicability boundaries are recorded in:

`reviews/chapter-013/ACADEMIC-EVIDENCE-REVIEW-2026-08-14.md`

Future material technical claims added to Chapter 13 reopen Academic/Evidence Review for those claims.

---

## 6. Standards Validation status

Public-source Standards Validation performed during redevelopment was rechecked on 2026-08-14. It supports the chapter's standards architecture and current-edition navigation, including the separation between:

`long-term evidence → material classification → design-stress framework → product/application standard → service/system verification`

The following remain controlled full-text holds and are tracked in `references.md`:

- `SVH-013-01` — ISO 12162 exact MRS / class / rounding / C / design-stress details;
- `SVH-013-02` — ISO 9080 exact statistical terminology / data / extrapolation / branch rules;
- `SVH-013-03` — ISO 4427 exact pressure/SDR/temperature/marking requirements;
- `SVH-013-04` — ISO 4437 exact MOP/RCP/derating/marking/component/joint rules;
- `SVH-013-05` — PE100-RC / SCG qualification acceptance route and any pressure-design implications.

These holds are deliberately visible. Secondary literature, old withdrawn ISO editions and generated summaries do not close them.

---

## 7. Editorial / Style Review status

The active PDS 1.0 Style Guide was applied to the consolidated manuscript.

**Result:** no structural or prose rewrite is required before controlled integration.

Passed areas include:

- Investigation-led heading hierarchy;
- chapter engineering progression and Quick Navigation;
- controlled engineering asset IDs;
- worked-example structure and limitations;
- cross-reference stability;
- professional/objective tone;
- explicit uncertainty and standards hold points;
- visual-placeholder treatment appropriate to Authoring.

The bounded open editorial items are recorded in:

`reviews/chapter-013/EDITORIAL-STYLE-REVIEW-2026-08-14.md`

They are:

- `ED-013-01` — final claim-level academic citation placement;
- `ED-013-02` — exact `σ_LCL` terminology/notation, dependent on standards full text;
- `ED-013-03` — exact lower prediction/confidence wording, dependent on ISO 9080 full text;
- `ED-013-04` — front-matter review/status/date synchronization;
- `ED-013-05` — final visual production during Publishing where required.

No High or Critical editorial finding is open.

---

## 8. Engineering asset status

| ID | Asset | Review disposition |
|---|---|---|
| EQ-013-001 | Thin-wall hoop-stress approximation | Integrated; technical review passed within stated approximation limits |
| EQ-013-002 | MRS → design stress | Integrated; exact normative notation/rules remain SVH-013-01 |
| EQ-013-003 | SDR definition | Integrated; technical metadata complete; product-standard wording remains validation-dependent |
| EQ-013-004 | SDR / reference-pressure relationship | Integrated; arithmetic reviewed; exact standards context remains controlled hold |
| FIG-013-001..007 | Chapter figures / visual specifications | Authoring placeholders or integrated text schematics; final publishing production pending where identified |
| TAB-013-001..005 | Classification, marking, inputs, failure response, pressure chain | Integrated; standards-derived cells remain subject to applicable hold |
| EX-013-001 | Pressure / SDR interpretation | Arithmetic/method checked; example does not establish project allowable pressure |
| EX-013-002 | Changed Design Basis | Decision-path review complete; numerical normative treatment intentionally bounded |
| CL-013-001 | PE Pressure-Piping Design Review Checklist | Integrated |

---

## 9. Remaining Definition-of-Done actions

Before Chapter 13 can be labelled publication-ready / frozen:

1. obtain or otherwise lawfully access the current authoritative full normative text required to close or precisely disposition `SVH-013-01` through `SVH-013-05`;
2. apply any corrections resulting from that review to chapter text, equations, tables, examples and references;
3. place final claim-level academic citations after standards-dependent wording is stable;
4. synchronize chapter front-matter review/status/date metadata;
5. complete final publishing visual production or approved final disposition for each remaining placeholder;
6. perform the final chapter-to-book cross-reference check against the then-current working architecture;
7. complete joint author review and explicit author approval;
8. merge the approved Chapter 13 revision to `main`;
9. record final chapter version / repository history.

The Academic/Evidence Review is no longer an open Definition-of-Done action for the current claim set. The Editorial/Style Review is structurally closed with the bounded final source-formatting and publishing items listed above.

---

## 10. Review decision

**CONDITIONAL PASS — suitable for controlled integration as the active Chapter 13 standards-validation candidate.**

Chapter 13 is technically mature, academically supported for its current core claim set and structurally/editorially mature enough to enter the active repository for transparent standards/source closure.

It is **not** approved for Design Freeze or final publication while the authoritative full-text standards holds and bounded final publication actions remain open.