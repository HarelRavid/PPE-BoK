# Chapter 13 Rev 1.0 — Integration Pass 01

**Scope:** Investigations 5–6  
**Status:** Integrated candidate for author approval  
**Source:** Approved Batch 013-C  
**PDS baseline:** 1.0 (frozen)

## Integration decisions

1. Preserve Investigations 1–4 as the explanatory foundation.
2. Investigation 4 ends by establishing why long-term evidence is required; detailed evidence generation is handled here in Investigation 5.
3. Investigation 5 covers evidence generation and the controlled extrapolation concept without reproducing the ISO 9080 statistical procedure.
4. Investigation 6 covers interpretation of regression output and the lower statistical bound without turning the chapter into a statistics manual.
5. Investigation 6 terminates at the classification interface and hands off to Investigation 7 for MRS and design stress.
6. Current-edition normative details remain Standards Validation hold points because the full standards available during redevelopment are superseded editions.

---

# Investigation 5 — How Can Decades of Performance Be Evaluated Before Decades Have Passed?

A polyethylene pressure pipe intended for decades of service cannot be qualified by waiting for the full design life of every new material. The engineering solution is not to replace long-term evidence with a short-term burst test, but to generate a structured body of stress-rupture data and analyse it within a controlled extrapolation framework.

The essential evidence chain is:

`pipe-form specimens → controlled internal pressure → controlled temperature → observed failure time → regression / extrapolation → long-term hydrostatic strength`

The important point is that the test output is not simply “passed” or “failed”. Each specimen contributes a combination of stress, temperature and time-to-failure. Taken together, these observations describe how pressure-carrying capability changes as time increases.

## 5.1 Why the material is tested in pipe form

The extrapolation method is intended for thermoplastic material evaluated in pipe form. This matters because the objective is not to measure an abstract polymer property in isolation, but to establish long-term pressure behaviour representative of the material as processed into pipe.

The resulting evidence therefore sits between a resin property and a finished-system qualification:

`material in pipe form ≠ complete piping system`

Joining quality, fittings, installation damage, chemical exposure and project loading still require separate verification.

## 5.2 Why more than one pressure level is required

A single pressure test gives one point.

Long-term classification requires a population of observations distributed across pressure/stress levels and time. The available ISO 9080:2003 edition requires a statistically meaningful distribution of observations rather than concentrating all tests near one condition.

For the practicing engineer, the reason is more important than the exact test count:

> **A long-term curve can only be credible if the data show how failure time changes as stress changes.**

This is why a short-duration burst value cannot be substituted directly for long-term hydrostatic strength.

**Standards Validation Hold Point:** exact current-edition requirements for specimen count, pressure levels, duration and temperature spacing shall be verified against the current authoritative ISO 9080 edition before publication.

## 5.3 Temperature is an acceleration variable — but not a free shortcut

Testing at elevated temperature can reveal long-term behaviour sooner because polymer time-dependent processes accelerate with temperature.

However, elevated-temperature data are not simply “converted” into arbitrary service life.

The extrapolation framework constrains:

- which temperatures are used;
- how data from different temperatures are combined;
- whether the same failure branch is being represented;
- and how far beyond observed test duration the prediction may extend.

The available ISO 9080:2003 edition explicitly defines extrapolation-time limits rather than allowing unlimited extension of a fitted curve.

> **Engineering rule:** accelerated testing extends the evidence base only inside a validated extrapolation methodology.

## 5.4 Failure mechanism matters

Long-term data may not follow one continuous mechanism across all stress and time ranges.

A change in slope — a **knee** — may indicate transition between different failure behaviours. The extrapolation method therefore includes detection and treatment of such transitions rather than forcing all observations through one convenient line.

> **A regression curve is only useful when the underlying failure behaviour represented by that curve remains physically meaningful.**

Detailed interpretation of field failure evidence remains deferred to Investigation 10; this section addresses only the relevance of failure-branch behaviour to the long-term evidence framework.

## 5.5 What Investigation 5 gives the engineer

Investigation 5 does **not** teach how to run an ISO 9080 qualification programme.

It gives the engineer the ability to recognize the evidence chain behind a material classification and to ask useful questions of a supplier or qualification report:

| Engineering question | Why it matters |
|---|---|
| Was the material evaluated in pipe form? | Confirms relevance of the hydrostatic evidence |
| Are multiple stress levels represented? | Establishes stress–life behaviour rather than a single test point |
| Were appropriate temperatures included? | Supports validated time/temperature extrapolation |
| Was a change of failure mechanism assessed? | Prevents inappropriate use of one regression branch |
| Is the required service point inside the permitted extrapolation range? | Prevents unsupported life claims |
| Is the reported value a mean prediction or a conservative lower bound? | Critical for classification and design |

**Engineering decision:** do not treat a long-term strength value as credible merely because it appears on a datasheet. Identify the test and extrapolation framework from which it was derived.

---

# Investigation 6 — What Does Regression Analysis Mean to the Practicing Engineer?

The practicing engineer normally does not need to reproduce the full statistical regression procedure.

The engineer **does** need to understand what the regression output means — and what it does not mean.

## 6.1 The regression line is not the design value

The test observations scatter.

A fitted regression represents the central predicted behaviour of the data, but engineering classification does not simply take that mean prediction as the allowable design value.

The available ISO 9080:2003 edition distinguishes predicted long-term hydrostatic strength from a lower statistical bound and uses a 97.5% lower prediction/confidence concept for the conservative result.

Conceptually:

`observations → fitted behaviour → lower statistical bound → classification input`

This distinction is one of the most important ideas in the chapter.

## 6.2 Why a lower bound is necessary

Real materials and real tests exhibit scatter.

If the engineering value were taken directly from the mean fitted curve, it would not represent a deliberately conservative statistical basis for classification.

The lower statistical bound provides that conservative step.

It should **not** be interpreted as a universal “97.5% probability that every pipe survives”. It is a statistical property of the regression framework and must be interpreted within the assumptions and definitions of the applicable standard.

**Standards Validation Hold Point:** final terminology — including lower prediction limit, lower confidence limit and the exact current-edition statistical definition — shall be verified against the current ISO 9080 and ISO 12162 editions before publication.

## 6.3 FIG-013-003 — Long-term hydrostatic regression concept

The original engineering figure shall distinguish:

`individual failure observations`

from

`predicted mean long-term behaviour`

from

`lower prediction / confidence boundary`

and, where relevant, show a knee separating two failure branches.

The visual is intended to explain the engineering meaning of the regression, not reproduce a standards figure.

## 6.4 Regression is evidence, not a guarantee

The regression result does not by itself establish:

- chemical compatibility;
- joint quality;
- resistance to installation damage;
- system loads;
- suitability outside the tested/extrapolated temperature-time range;
- or compliance with a particular product/application standard.

It answers a narrower question:

> **What long-term hydrostatic-strength evidence can reasonably be assigned to the qualified pipe material under the defined extrapolation framework?**

## 6.5 Bridge to MRS

This is where Investigation 6 ends and Investigation 7 begins.

The output of the regression/extrapolation process provides a conservative long-term strength basis. The classification standard then converts that continuous statistical result into a standardized material class.

The available ISO 12162:1995 edition shows this transition explicitly: a lower confidence value is rounded downward into a standardized **MRS**, after which design stress is derived using the applicable design coefficient.

The complete chain is therefore:

`test data → regression → lower statistical bound → MRS → design coefficient → design stress → SDR → pressure capability`

**Standards Validation Hold Point:** the exact current-edition rounding series, notation, reference conditions and classification rules shall be verified against the current authoritative ISO 12162 edition before publication.

---

## Pass-01 acceptance check

- Investigation 4 → 5 boundary: **clear**.
- Investigation 5 → 6 boundary: **clear**.
- Investigation 6 → 7 handoff: **explicit**.
- Detailed failure-forensics content duplicated from Investigation 10: **no**.
- Full statistical derivation reproduced unnecessarily: **no**.
- Standards-derived details treated as publication-ready despite superseded source editions: **no**.
- FIG-013-003 requirement retained: **yes**.
- Engineering-use questions retained: **yes**.

**Disposition:** Integration Pass 01 is ready for author review. After approval, Investigations 5–6 may replace the current redevelopment placeholders in the Chapter 13 Rev 1.0 body during consolidation.
