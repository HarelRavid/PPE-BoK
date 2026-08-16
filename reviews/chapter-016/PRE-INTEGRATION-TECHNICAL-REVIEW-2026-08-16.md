# Chapter 016 — Pre-Integration Technical Review

**Date:** 2026-08-16  
**Scope:** canonical Investigation 1 + controlled Investigation 2–10 authoring candidates + evidence addendum  
**PDS baseline:** 1.0  
**Disposition:** **CONDITIONAL PASS — CANONICAL INTEGRATION AUTHORIZED WITH BOUNDED FINDINGS**

## 1. Overall technical disposition

The logical manuscript forms a coherent engineering sequence:

1. architecture as measured material state rather than process label;
2. DP / molar mass / relative molecular mass;
3. `M_n`, `M_m/M_w`, MMD and dispersity;
4. SEC/GPC measurement/calibration logic;
5. branching as a multidimensional descriptor;
6. SCB versus LCB and ISO 18177 scope;
7. crosslinks/networks and ISO 10147 gel-content limits;
8. entanglement versus covalent connectivity;
9. four bounded architecture→behaviour primary-evidence cases;
10. supplier-data workflow / stop rule / Chapter 017 handoff.

No chapter-wide scientific rewrite is required.

## 2. Bounded findings to apply during canonical integration

### TR016-01 — integrate Investigations 2–10 without changing scientific content

Replace the canonical post-Investigation-1 development boundary with the reviewed candidate text for Investigations 2–10 in order.

Do not paraphrase the evidence conclusions during mechanical integration.

### TR016-02 — absorb S016-013 through S016-016 into canonical references.md

The temporary `references-addendum-2026-08-16.md` contains the four primary sources admitted by the Investigation 9 gate.

They must become canonical source entries and retain `supported / unsupported / transferability` boundaries.

### TR016-03 — synchronize current metadata

Current development metadata still contains pre-sync statements such as CDB metadata sync being open/non-blocking.

Canonical current-state files (`technical-outline.md`, `review.md`, and manuscript frontmatter if applicable) shall reflect:

- CDB-016 APPROVED;
- CDB metadata sync COMPLETE;
- Definition of Ready PASS;
- Engineering Development COMPLETE after integration;
- final integrated-manuscript reviews PENDING;
- Human Approval PENDING.

Historical DoR/review records shall remain historical and need not be rewritten.

### TR016-04 — preserve controlled molar-mass notation

Canonical explanatory prose shall prefer:

- `molar mass` for dimensional quantity;
- `M_n` number average;
- `M_m ≡ M_w` at controlled introduction;
- `Đ_M` molar-mass dispersity;
- original standard/paper titles retain source wording such as `molecular weight`.

Do not silently rewrite source titles.

### TR016-05 — preserve the `chain length` ambiguity control

Do not reintroduce unqualified `chain length` as the formal molecular-size quantity. Investigation 2 correctly routes quantitative claims to DP, molar mass/distribution or an explicitly defined geometric quantity.

### TR016-06 — one final formal owner per asset

Final integrated chapter shall contain one formal final specification/use for each:

- FIG-016-001 through FIG-016-006;
- TAB-016-001 through TAB-016-005;
- EX-016-001 through EX-016-003;
- WF-016-001;
- CL-016-001.

Supporting unnumbered tables are permitted only if they do not create duplicate formal IDs.

### TR016-07 — preserve Investigation 9 evidence bounds

Only S016-013 through S016-016 are admitted named architecture→behaviour cases.

Mechanical integration must not create any universal statement equivalent to:

- `higher M_w = better pipe/SCG`;
- `broader MWD = better processing`;
- `more SCB = better SCG / higher H2 permeability`;
- `more LCB = better processing`;
- `more crosslinking / higher gel = stronger/better PE-X`;
- `more entanglement = better fusion`.

### TR016-08 — remove temporary authoring artifacts only after validation

After successful canonical integration and assertions, remove:

- Investigation 2–10 authoring candidates;
- temporary primary-evidence addendum;
- one-shot integration script.

## 3. Quantitative review

PASS at candidate level.

Retained quantitative relations are definition/bookkeeping relations, not design equations:

- bounded individual-chain relation `M_chain = x M_0 + M_end`;
- `M_n`;
- `M_m ≡ M_w`;
- `Đ_M = M_m/M_n`;
- `Đ_X = X_m/X_n`.

EX-016-001 was independently recalculated and passes.

No architecture descriptor is converted into pressure rating, lifetime, SCG, permeability or joining acceptance.

## 4. Measurement-boundary review

PASS.

- conventional/universal SEC remain calibration/model aware;
- ISO 16014-2 is not called absolute;
- SEC-LS `absolute` is used only within method scope and is not described as assumption-free;
- ISO 18177 is bounded to its SCB / semicrystalline ethylene-1-olefin scope;
- ISO 10147 gel content is not crosslink density/topology;
- MFR/MVR and density remain correlated/QC/downstream quantities rather than direct architecture substitutes.

## 5. Chapter 017–020 / Part V / VII / VIII boundaries

PASS.

Chapter 016 defines architecture and evidence routing. Detailed morphology, thermal response, rheology/creep, fracture/SCG, lab procedure, joining and design remain downstream.

## 6. Integration authorization

**Canonical integration is technically authorized** if TR016-01 through TR016-08 are applied and the post-integration assertions pass.

Final full-file Technical Review remains mandatory after integration.