# Chapter 015 — Standards / Terminology / Evidence Validation

**Date:** 2026-08-15  
**Scope:** complete pre-integration Chapter 015 authoring arc  
**Disposition:** **PASS FOR CURRENT ENGINEERING-DEVELOPMENT WORDING — PUBLICATION LIFECYCLE HOLDS REMAIN**

## 1. Validation objective

Validate that load-bearing terminology, classification and named process/catalyst claims in Chapter 015 are supported by the correct evidence class and that no terminology source or primary paper is being used as piping design authority.

## 2. Authoritative terminology status

### S015-008 — IUPAC basic polymerization classification

**PASS / controlling current classification source.**

Official IUPAC records confirm that _Basic classification and definitions of polymerization reactions (IUPAC recommendations 2025)_ was published in Pure and Applied Chemistry, Advance Online Publication 12 May 2026, DOI `10.1515/pac-2025-0490`, and is listed in Volume 98 Issue 7 (2026), starting page 1105.

Controlled chapter hierarchy:

- step polymerization;
  - additive step polymerization = polyaddition;
  - condensative step polymerization = polycondensation;
- chain polymerization;
  - additive chain polymerization;
  - condensative chain polymerization.

The chapter's earlier planning language must be synchronized to this final published Recommendation during canonical integration.

### S015-004 — IUPAC Terminology for Chain Polymerization

**PASS / current detailed chain-mechanism terminology source.**

Official IUPAC records confirm publication in Pure and Applied Chemistry 94(9) (2022), 1093–1147.

It supports the chapter's controlled terminology for:

- chain polymerization;
- chain carrier / active-site concepts;
- initiation / propagation / termination / transfer;
- radical polymerization;
- reversible deactivation / living terminology;
- coordination polymerization;
- coordination-insertion polymerization;
- catalyst precursor / initialization;
- heterogeneous and homogeneous coordination polymerization;
- metallocene polymerization.

### S015-001 — IUPAC Gold Book

**PASS for current authoring use.**

The chapter uses the Gold Book 5th edition online framework / current term records as the controlled term-access layer. Load-bearing term identifiers are recorded or scheduled for canonical `references.md` integration.

**Publication hold:** recheck online version / access state at final publication because the online compendium is maintained.

### S015-006 — ISO 472:2013 + Amd 1:2018

**PASS for vocabulary-only role.**

Official ISO status at the 2026-08-15 checkpoint:

- ISO 472:2013 — Published, stage `90.92 — International Standard to be revised`;
- Amendment 1:2018 — Published;
- replacement/revision activity is active.

Chapter 015 does not use ISO 472 as polymerization-mechanism or piping-design authority.

**Publication hold:** lifecycle recheck required before publication freeze.

### S015-007 — ISO 1043-1:2011 + Amd 1:2016

**PASS for abbreviation/symbol role.**

Official ISO status at the checkpoint:

- ISO 1043-1:2011 — Published / Confirmed, stage `90.93`;
- Amendment 1:2016 — Published.

No mechanism or performance claim depends on this standard.

## 3. Named primary-evidence cases

### S015-009 — Piovano et al. 2018

**PASS.** Used only for catalyst-genesis / activation complexity in the defined MgCl2-based Ziegler–Natta system. No universal site count or architecture transfer.

### S015-010 — Busico et al. 1999

**PASS.** Used only for the specified MgCl2-supported PP system in which a three-site statistical model fit the reported stereosequence data better than tested two-site models. No universal `three sites` claim.

### S015-011 — Guo et al. 2025

**PASS.** Used only for the defined MgCl2-supported ethylene/alpha-olefin catalyst system linking measured catalyst-state populations with measured short-chain-branch distribution behavior. No universal Ziegler–Natta branch rule.

### S015-012 — Kenyon et al. 2022

**PASS.** Used as a bounded falsification/process-provenance case: one supported metallocene precursor/system produced bimodal PE under reported conditions and MWD response changed with support composition / conditions. No universal supported-metallocene rule.

### S015-013 — De Rosa et al. 2004

**PASS.** Used only to show different stereoregularity outcomes across the studied zirconocene PP catalyst series. No transfer to all metallocenes, PE or piping performance.

### S015-014 — Czaja & Białek 2001

**PASS.** Used only for the observation that hydrogen addition reduced polymer molecular weight and catalyst activity in the three studied MgCl2(THF)2-supported ethylene/alpha-olefin copolymerization catalyst systems. No universal hydrogen rule.

### S015-015 — Zhang et al. 2021

**PASS.** Used only for E/P-feed-ratio-dependent active-center / copolymer-fraction behavior in the defined TiCl4/Di/MgCl2–TEA/De system. No universal feed-ratio rule.

### S015-016 — Wang et al. 1998

**PASS.** Used only for temperature / mean-residence-time / ethylene-feed history and measured/modelled LCB/kinetic behavior in the defined CGC-Ti continuous solution polymerization system. No universal temperature/residence rule.

## 4. Claim-boundary audit

PASS.

The authoring arc does **not** promote any of the following into universal statements:

- Ziegler–Natta = fixed multi-site distribution;
- Ziegler–Natta = broad MWD;
- metallocene = narrow MWD;
- metallocene = uniform comonomer distribution;
- single-site = one guaranteed polymer population;
- hydrogen always lowers molecular weight;
- higher temperature always raises/lowers molecular weight or branching;
- comonomer feed ratio has one universal architecture effect;
- process history directly determines SCG, RCP, fusion, pressure rating or lifetime.

All such transitions are routed through characterization and qualification.

## 5. Normative-design boundary

PASS.

No IUPAC or ISO vocabulary source is used as pressure-piping design authority.

No primary polymerization study is used to establish:

- pressure rating;
- design stress;
- temperature derating;
- hydrostatic lifetime;
- chemical compatibility;
- fusion procedure/parameter;
- SCG/RCP acceptance;
- service-specific permeability limit.

## 6. Canonical-integration requirements

Before final wording validation:

1. absorb S015-008 into canonical `references.md` as the controlling classification source;
2. add S015-009 through S015-016 with exact supported/unsupported/transferability boundaries;
3. update CDB-015 and Technical Outline to remove stale pre-2026 classification wording;
4. preserve original paper titles exactly even when canonical prose normalizes `molar mass` terminology;
5. delete the temporary evidence addendum only after its content is represented canonically.

## 7. Publication lifecycle holds

The following are not Engineering-Development blockers but remain controlled publication tasks:

- recheck IUPAC Gold Book current online version/access state;
- recheck ISO 472 lifecycle / replacement multipart programme;
- recheck ISO 1043-1 lifecycle;
- verify final rendered figure/source labels;
- perform final claim-level citation audit against the integrated manuscript.

## 8. Decision

**PASS FOR CURRENT ENGINEERING-DEVELOPMENT WORDING.**

Canonical integration is authorized from an evidence perspective subject to the requirements above. Final claim-level Standards/Evidence Validation remains mandatory after integration.