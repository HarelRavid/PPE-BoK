# Investigation 3 — Why Does a Polymer Have Multiple Molar-Mass Averages?

## 1. Engineering question

Two resin certificates both report `M_w = 100 000 g/mol`.

Can the engineer conclude that the two resins have the same molecular-size population?

No.

A non-uniform polymer is a population of macromolecules. Different averages weight that population differently, and even several averages do not uniquely reconstruct the complete distribution.

Investigation 3 establishes the minimum quantitative language needed to read a polymer molar-mass report without turning one number into a material identity.

The controlling terminology sources are S016-001, S016-002 and S016-003.

---

## 2. Why one average cannot represent every question

Suppose a polymer sample contains many macromolecular species with different molar masses.

A short chain and a very long chain are both **one molecule** when molecules are counted. But the very long chain carries much more of the sample mass.

Therefore two legitimate averaging questions immediately exist:

1. **What is the average molar mass if every molecule counts equally?**
2. **What is the average molar mass when the contribution of heavier molecules is weighted more strongly?**

Those questions lead to different averages.

The existence of several averages is not a mathematical nuisance. It reflects different ways in which a non-uniform molecular population can be observed and weighted.

---

## 3. Number-average molar mass — `M_n`

IUPAC defines the **number-average molar mass**, symbol `M_n`, as a molar-mass average in which each molecule contributes according to molecular number.

For a discrete teaching population containing `N_i` molecules of molar mass `M_i`, the equivalent number-count form is:

`M_n = (Σ N_i M_i) / (Σ N_i)`

where:

- `N_i` = number of molecules in class `i`;
- `M_i` = molar mass of molecules in class `i`;
- `M_n` = number-average molar mass.

Units:

`g mol⁻¹` or `kg mol⁻¹`.

The current Gold Book presents the corresponding definition using mass fractions `w_M`:

`M_n = 1 / Σ(w_M / M)`

The two forms describe the same number-average concept when the discrete population is represented consistently.

### 3.1 What `M_n` emphasizes

Because each molecule counts once, a large number of lower-molar-mass molecules can pull `M_n` downward even if those molecules do not dominate the sample mass.

This makes `M_n` useful as one descriptor of the **molecular-count population**.

It does not make `M_n` a complete distribution.

### 3.2 What `M_n` does not prove

`M_n` alone does not establish:

- the high-molar-mass tail;
- multimodality;
- branching;
- topology;
- crystallinity;
- melt rheology;
- SCG performance;
- fusion behaviour;
- pressure capability.

---

## 4. Mass-average molar mass — `M_m ≡ M_w`

IUPAC defines the **mass-average molar mass** with preferred symbol `M_m` and accepts `M_w` as an equivalent symbol widely used in polymer practice.

For a discrete population:

`M_m ≡ M_w = (Σ N_i M_i²) / (Σ N_i M_i)`

Equivalent mass-fraction form:

`M_m = Σ w_i M_i`

where `w_i` is the mass fraction associated with molar-mass class `i`.

Units:

`g mol⁻¹` or `kg mol⁻¹`.

### 4.1 Why the square appears in the number-count form

In the number-count representation, one factor of `M_i` converts molecular count into mass contribution and the second factor weights the average by that mass.

The result is more sensitive to heavier molecules than `M_n`.

For a non-uniform positive molar-mass population:

`M_m ≥ M_n`

with equality for a perfectly uniform molar-mass population.

### 4.2 Symbol control

PPE-BoK canonical prose will use:

`M_m ≡ M_w`

on first controlled introduction and may retain `M_w` where it is the familiar symbol in industry, standards or source literature.

The reader should understand that the symbol does not change the underlying mass-average definition.

---

## 5. Molar-mass dispersity — `Đ_M`

IUPAC defines **molar-mass dispersity** as:

`Đ_M = M_m / M_n`

Equivalently, with the common accepted symbol:

`Đ_M = M_w / M_n`

`Đ_M` is dimensionless because it is a ratio of two molar masses expressed in the same units.

For a uniform molar-mass population:

`Đ_M = 1`

For a non-uniform population:

`Đ_M > 1`

within the normal positive-mass population definitions used here.

### 5.1 Do not use “PDI” as the controlled term

The expression **polydispersity index (PDI)** is common in industry and historical literature, but IUPAC strongly discourages using `polydispersity index` for `M_m/M_n`.

PPE-BoK therefore uses **molar-mass dispersity**, `Đ_M`, as the controlled term.

If a supplier or paper reports “PDI,” the engineer should first verify that the source actually means `M_w/M_n` before mapping it to `Đ_M`.

---

## 6. Dispersity is not the distribution

This distinction is essential:

> **`Đ_M` measures spread in a particular average sense; it does not uniquely define distribution shape.**

Two populations can have:

- the same `M_n` and different shapes;
- the same `M_m` and different shapes;
- similar `Đ_M` and different tails;
- similar averages but different modal structure;
- the same two averages and still differ in finer distribution detail.

Therefore:

`M_n + M_m + Đ_M ≠ full molecular population identity`

A claim such as `broad MWD`, `narrow MWD`, `bimodal` or `multimodal` should be tied to an actual distribution measurement and method, not inferred from a single average.

Investigation 4 explains how SEC/GPC obtains distribution information and where calibration complicates interpretation.

---

## 7. EX-016-001 — Same `M_m`, different population

Consider two simplified synthetic populations, each containing 100 macromolecules.

The numbers are intentionally artificial. They exist only to demonstrate weighting.

### Population A

- 60 molecules at `80 000 g mol⁻¹`;
- 40 molecules at `120 000 g mol⁻¹`.

Number-average:

`M_n,A = [60(80 000) + 40(120 000)] / 100`

`M_n,A = 96 000 g mol⁻¹`

Mass-average:

`M_m,A = [60(80 000)² + 40(120 000)²] / [60(80 000) + 40(120 000)]`

`M_m,A = 100 000 g mol⁻¹`

Dispersity:

`Đ_M,A = 100 000 / 96 000`

`Đ_M,A = 1.0417`

### Population B

- 75 molecules at `50 000 g mol⁻¹`;
- 25 molecules at `150 000 g mol⁻¹`.

Number-average:

`M_n,B = [75(50 000) + 25(150 000)] / 100`

`M_n,B = 75 000 g mol⁻¹`

Mass-average:

`M_m,B = [75(50 000)² + 25(150 000)²] / [75(50 000) + 25(150 000)]`

`M_m,B = 100 000 g mol⁻¹`

Dispersity:

`Đ_M,B = 100 000 / 75 000`

`Đ_M,B = 1.3333`

### 7.1 What the example proves

Both populations have exactly the same mass-average molar mass in this teaching construction:

`M_m = 100 000 g mol⁻¹`

But they do not have the same molecular population.

Population B has a much larger spread and a lower `M_n`.

Therefore a datasheet comparison based only on `M_w = 100 000` would miss a major difference deliberately built into the example.

### 7.2 What the example does not prove

The example does **not** prove that Population A or B would have better:

- processing;
- stiffness;
- toughness;
- creep;
- SCG resistance;
- permeability;
- fusion performance.

Those are downstream hypotheses requiring measurement.

The synthetic population is not intended to represent a commercial PE or PP distribution.

---

## 8. Why the distribution shape matters beyond `Đ_M`

Imagine three hypothetical distributions with similar `Đ_M`:

1. one broad single peak;
2. two separated peaks;
3. a main peak plus a small very-high-molar-mass tail.

A single ratio cannot tell the engineer which shape is present.

That matters because any downstream mechanism sensitive to different portions of the population may respond differently even when one global ratio is similar.

Chapter 016 does not convert that observation into a performance rule. It converts it into a **measurement requirement**:

> If the engineering hypothesis depends on where material exists within the distribution, request the distribution rather than only its averages.

---

## 9. Degree-of-polymerization dispersity is a separate controlled quantity

IUPAC also defines degree-of-polymerization dispersity:

`Đ_X = X_m / X_n`

For a homopolymer or sufficiently high-molar-mass alternating copolymer where end-group effects can be neglected and DP is directly proportional to molar mass, `Đ_X` and `Đ_M` can coincide.

IUPAC explicitly warns that for a copolymer that is not an alternating copolymer, the proportionality between DP averages and molar-mass averages cannot simply be assumed.

Therefore Chapter 016 will state the quantity explicitly:

- `Đ_M` for molar-mass dispersity;
- `Đ_X` for degree-of-polymerization dispersity when that quantity is actually intended.

Do not silently collapse them for compositionally heterogeneous copolymers.

---

## 10. TAB-016-001 — Chain-architecture quantities

| Quantity | Preferred symbol | Units | What it describes | Common misuse |
|---|---:|---:|---|---|
| individual molar mass | `M` | `g mol⁻¹` or `kg mol⁻¹` | molar mass of specified molecular species | treating one species value as a polymer-population distribution |
| number-average molar mass | `M_n` | `g mol⁻¹` or `kg mol⁻¹` | molecule-number-weighted population average | ignoring low-molar-mass population contribution or calling it “the molecular weight” |
| mass-average molar mass | `M_m ≡ M_w` | `g mol⁻¹` or `kg mol⁻¹` | mass-weighted population average | treating it as the complete MWD |
| molar-mass dispersity | `Đ_M` | dimensionless | ratio `M_m/M_n`; spread descriptor | calling it a complete distribution shape or using undefined “PDI” without mapping |
| degree of polymerization | `x` for an individual chain context | dimensionless | count of monomeric units | confusing count with molar mass |
| DP dispersity | `Đ_X` | dimensionless | `X_m/X_n` | assuming it always equals `Đ_M` in copolymers |
| full molar-mass distribution | method-defined distribution | distribution variable dependent | population over molar mass | replacing it with one average or one dispersity value |

---

## 11. Measurement does not produce all averages equally

Different experimental methods can be sensitive to different aspects of the population.

The IUPAC molar-mass-average framework explicitly recognizes that only some averages are directly accessible by particular methods.

This is why an engineering comparison must include:

`reported average + measurement method + calibration/model basis`

not merely:

`reported average`.

Examples of method families relevant to the broader evidence chain include:

- osmometry for number-average information in appropriate solution regimes;
- light scattering for mass-average information under its method assumptions;
- SEC/GPC for distribution characterization with calibration/detector controls.

Chapter 016 does not develop the first two as laboratory methods here. Investigation 4 focuses specifically on SEC/GPC because it is the common distribution route in the active ISO 16014 path.

---

## 12. Failure lens

### Failure mode 1 — `M_w` treated as the molecular identity

Statement:

> “The two grades have the same `M_w`, so they are molecularly equivalent.”

Failure:

EX-016-001 demonstrates mathematically that the same `M_m/M_w` can coexist with different `M_n` and different distribution shape.

### Failure mode 2 — high dispersity treated as proof of bimodality

Statement:

> “The dispersity is high, therefore the resin is bimodal.”

Failure:

`Đ_M` is a ratio. It does not identify how many modes the distribution has.

### Failure mode 3 — low dispersity treated as universal quality

Statement:

> “Lower `Đ_M` means a better resin.”

Failure:

Dispersity is an architecture descriptor, not a quality ranking or piping acceptance criterion.

### Failure mode 4 — `PDI` copied without definition

Statement:

> “PDI = 7.”

Failure:

Confirm what the source means and whether it is actually `M_w/M_n`. Use `Đ_M` in controlled PPE-BoK interpretation.

### Failure mode 5 — architecture statistic converted directly into design

Statement:

> “Higher `M_w` gives better SCG, therefore this grade is suitable.”

Failure:

The first clause may be a testable material hypothesis in a bounded system; the second requires direct downstream evidence and qualification.

---

## 13. FIG-016-001 — Why one molar-mass number is not enough

**Final figure specification.**

Create an original schematic showing a population of polymer chains represented by horizontal lines of different lengths, grouped above a conceptual molar-mass axis.

The figure shall contain three reader cues:

1. `individual macromolecules differ`;
2. `averages compress population information`;
3. `distribution retains information that one average discards`.

Do not use a real resin curve or imply a universal distribution shape.

---

## 14. FIG-016-002 — Different averages weight one distribution differently

**Final figure specification.**

Use one conceptual, clearly labelled non-real distribution. Show the qualitative relationship between:

- number-sensitive view;
- mass-sensitive view;
- `M_n`;
- `M_m/M_w`.

The figure shall state:

`schematic — not to scale; no universal ordering distance implied beyond M_m ≥ M_n for the defined positive population`.

Do not infer processability or performance from the positions.

---

## 15. Verification method

A molar-mass comparison is ready for engineering use only when the engineer can answer:

1. Which average or distribution is reported?
2. What symbol and units apply?
3. What weighting basis defines the value?
4. What method produced it?
5. Is the result absolute, relative or calibration/model dependent?
6. Is the complete distribution available if the hypothesis depends on shape/tails/modes?
7. What downstream conclusion is being proposed, and what separate evidence validates that conclusion?

---

## 16. Engineering decision

Use `M_n`, `M_m/M_w` and `Đ_M` as **different descriptors of the same underlying population**, not as interchangeable synonyms.

Use the complete distribution when the engineering question depends on population shape.

Do not rank materials by `M_w`, `M_n` or `Đ_M` alone.

Do not infer bimodality from dispersity alone.

Do not infer piping qualification from any molar-mass statistic alone.

---

## 17. Handoff to Investigation 4

Investigation 3 has defined the quantities.

The next question is measurement:

> **When a laboratory reports a molar-mass distribution from SEC/GPC, what did the instrument actually separate and measure, and how much of the reported result depends on calibration, detector choice, dissolution and molecular architecture?**

Investigation 4 opens the ISO 16014 method-scope gate and separates relative SEC calibration from light-scattering/other detector routes.