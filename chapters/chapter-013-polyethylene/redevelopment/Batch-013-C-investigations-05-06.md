# Batch 013-C — Investigations 5–6

**Chapter:** 013 — Polyethylene (PE)  
**Status:** Approved engineering redevelopment content  
**PDS baseline:** 1.0  
**Standards status:** Working engineering content; final Standards Validation pending against current authoritative editions.

> Source basis for this batch includes the available ISO 9080:2003 and ISO 12162:1995 copies supplied during redevelopment. These are superseded editions and are used here to establish the engineering chain and terminology only. Current-edition normative details shall be revalidated before publication.

---

# Investigation 5 — How Can Decades of Performance Be Evaluated Before Decades Have Passed?

A polyethylene pressure pipe intended for decades of service cannot be qualified by waiting for the full design life of every new material. The engineering solution is not to replace long-term evidence with a short-term burst test, but to generate a structured body of stress-rupture data and analyse it within a controlled extrapolation framework.

The essential evidence chain is:

`pipe-form specimens → controlled internal pressure → controlled temperature → observed failure time → regression / extrapolation → long-term hydrostatic strength`

The important point is that the test output is not simply “passed” or “failed”. Each specimen contributes a combination of stress, temperature and time-to-failure. Taken together, these observations describe how the material loses pressure-carrying capability as time increases.

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

That point is extremely important to design:

> **A regression curve is only useful when the underlying failure behaviour represented by that curve remains physically meaningful.**

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

This distinction is one of the most important ideas in the whole chapter.

## 6.2 Why a lower bound is necessary

Real materials and real tests exhibit scatter.

If the engineering value were taken directly from the mean fitted curve, it would not represent a deliberately conservative statistical basis for classification.

The lower statistical bound provides that conservative step.

It should **not** be interpreted as a universal “97.5% probability that every pipe survives”. It is a statistical property of the regression framework and must be interpreted within the assumptions and definitions of the applicable standard.

**Standards Validation Hold Point:** final terminology — including lower prediction limit, lower confidence limit and the exact current-edition statistical definition — shall be verified against the current ISO 9080 and ISO 12162 editions before publication.

## 6.3 FIG-013-003 — Long-term hydrostatic regression concept

The figure should clearly distinguish:

`individual failure observations`

from

`predicted mean long-term behaviour`

from

`lower prediction / confidence boundary`

and, where relevant, show a knee separating two failure branches.

The visual should explain the engineering meaning of the regression rather than reproduce a standards figure.

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

# Integration note

This approved batch is staged as a controlled redevelopment artifact on the Chapter 13 branch. It shall be consolidated into the Chapter 13 Rev 1.0 chapter body during the chapter integration pass, together with the subsequent MRS/design-stress and SDR/pressure-design investigations, so that terminology and cross-references remain internally consistent.