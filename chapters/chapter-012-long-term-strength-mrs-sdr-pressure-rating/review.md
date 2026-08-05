# Chapter 12 Technical Review

## Review status

- Physics review: **completed for draft**
- Standards review: **completed at scope and terminology level**
- Equation review: **completed**
- Units review: **completed**
- Application review: **completed for ISO-framework examples**
- Final editorial review: **pending**
- Locked status: **no**

## Claims verified

- ISO 9080:2012 specifies statistical extrapolation of long-term hydrostatic strength from thermoplastic pipe test data.
- ISO 9080:2012 remains the current published edition and was confirmed by ISO in 2023.
- ISO 12162:2009 establishes classification and designation of thermoplastic pressure-pipe materials and specifies a design-stress calculation method.
- ISO 12162:2009 remains the current published edition and was confirmed by ISO in 2021.
- PE100 corresponds to an MRS class of 10 MPa within the applicable ISO classification framework.
- PE80 corresponds to an MRS class of 8 MPa within the applicable ISO classification framework.
- SDR is the nominal outside diameter divided by nominal wall thickness under the applicable product convention.
- For the conventional ISO pressure relationship, the algebraic conversion between hoop stress and SDR is correct.
- The worked PE100 SDR 11 example gives 1.6 MPa, or 16 bar, when MRS = 10 MPa and C = 1.25.
- PE100+ is not a material-strength class above PE100.
- PE100-RC does not create a higher MRS class than PE100.

## Equation verification

### SDR

\[
SDR=\frac{d_n}{e_n}
\]

Dimensionless when both dimensions use the same unit.

### Hoop-stress relationship

\[
\sigma=\frac{p(d_n-e_n)}{2e_n}
\]

Substitution of \(d_n=SDR\,e_n\) gives:

\[
\sigma=\frac{p(SDR-1)}{2}
\]

Therefore:

\[
p=\frac{2\sigma}{SDR-1}
\]

and with \(\sigma_s=MRS/C\):

\[
p=\frac{2MRS}{C(SDR-1)}
\]

If stress is in MPa, pressure is in MPa. Multiplication by 10 converts MPa to bar:

\[
p_{bar}=\frac{20MRS}{C(SDR-1)}
\]

The derivation is dimensionally consistent.

## Important limitations retained in the chapter

- The equations are not presented as a complete code design method.
- Temperature derating remains product- and standard-specific.
- Chemical compatibility is treated as a separate mandatory check.
- Static pressure classification is not presented as fatigue qualification.
- Pipe rating is not presented as complete system rating.
- Lined and multilayer systems are excluded from automatic use of the simple homogeneous-wall relationship.
- Definitions of PN, MOP, design pressure and test pressure are kept distinct.

## Items requiring future expansion

1. Add a dedicated comparison of ISO MRS/design-coefficient terminology with ASTM/PPI HDB/HDS/DR terminology.
2. Verify the exact current product-standard wording before final publication.
3. Add product-standard examples for PP, PVC-U, PVC-C and PVDF so the chapter does not appear PE-only.
4. Add an original figure showing the chain:
   test data → regression → lower confidence strength → MRS → design stress → SDR → nominal pressure.
5. Add a second figure distinguishing material classification, pipe classification and system allowable operating pressure.
6. Consider a table showing why PN cannot be used without temperature and application context.

## Objectivity check

- No manufacturer-specific design rule is presented as universal.
- PE100+ Association guidance is identified as an industry source.
- No claim is made that a nominal 50-year classification guarantees an installed service life.
- No unsupported universal design coefficient is specified.
- The water-service value C = 1.25 appears only as a conditional worked example.

## Review conclusion

The chapter is suitable as a research-based draft and may be used as the current manuscript source. It should not be marked **locked** until product-standard terminology, non-PE examples, and figures have completed final review.
