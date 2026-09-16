# YM-R54 — native small-field one-step consolidation / exit gate

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R53_20260916.json`
Next cursor: YM-R55 (unconsumed)

## Question

R53 closed CMP116 Lemma 3 / Eq. (2.38) at mathematical/source level. R54 asks the exit-gate question:

> After restoring the post-Lemma-3 effective-action handoff, is any genuinely mathematical obligation still open inside the Paper-I/II small-field one-step induction, or should the traversal leave the small-field branch and enter the complete-density / large-field architecture?

This question is about the mathematical/source architecture, not about whether every source-to-Lean dictionary has been formalized.

## Preflight

The R53 checkpoint was recovered first. It records the CMP116 localized activity construction, the D-stage Eq. (2.29), the P-stage Eq. (2.31), the post-P Eq. (2.32)--(2.37) resummation, and Lemma 3 / Eq. (2.38) as closed at source/mathematical level. R46 had already classified the RP blocking modification as adding no independent source-facing theorem obligations relative to the native Bałaban package; R47--R49 subsequently closed the native analytic-domain gate.

## 1. Lemma 3 is not the end of the one-step argument

CMP116 [21], printed/PDF page 21, Eqs. (2.39)--(2.41), inserts the Lemma-3 activity bound

`|H(Z)| <= C3 epsilon1 exp(-((1-8 delta)/2) L kappa d_{k+1}(Z))`

into the exponentiated polymer series. Equation (2.39) extracts decay from every activity factor and uses connectedness of the union; Eq. (2.40) applies the standard polymer-series summability for large kappa and small epsilon1; Eq. (2.41) produces the next-scale localized effective-action estimate of the same inductive geometric type, with the decay reserve weakened from the Lemma-3 `1-8 delta` coefficient to the post-exponentiation `1-10 delta` coefficient. [21]

The source then chooses the fixed `delta,L` normalization so that this weakened scale-transferred coefficient is exactly the next-step inductive decay rate, and imposes

`O(1) C3 epsilon1 <= E0/2`.

Thus the output of CMP116 is not merely a cluster activity estimate: it is the return map into the Paper-I effective-action class. This is the missing endpoint required for an actual one-step closure statement. [21]

## 2. The extra normalization term is separately source-handled

The effective action also contains the normalization contribution

`log Z^(k)(U_{k+1}) - log Z^(k)(1)`.

CMP116 does not silently absorb this into Lemma 3. The paragraph following (2.41) treats it by a separate generalized random-walk expansion, with the source decay parameter replaced by the corresponding `delta_0 M` rate, and assigns the remaining `E0/2` amplitude budget to this term. [21]

Therefore the one-step output has the full `E0` budget split into two controlled pieces:

1. the exponentiated `H(Z)` contribution, controlled by `O(1) C3 epsilon1 <= E0/2`;
2. the normalization/random-walk contribution, controlled by the other `E0/2`.

No unaccounted post-Lemma-3 scalar normalization term remains.

## 3. Consolidated small-field chain

The current traversal has now source-locked or internally derived every mathematical interface needed by the small-field branch under audit:

1. **Exact RP-compatible blocker and local analytic input.** R18--R26 construct the reflection-positive blocking route, fix the preferred normalized kernel/center, and obtain a bounded-support analytic insertion of size `O(g_k)` on the canonical field tube.
2. **Marginal coordinate.** R21 identifies the Wilson-action coefficient `g_k^-2` as the existing marginal coordinate; any local dimension-four contribution from the modified blocker is extracted into this coordinate rather than creating a new relevant/marginal field.
3. **RP source-hypothesis neutrality.** R36--R46 reduce the added blocker to a multiplicative local analytic factor inside the native product-Gaussian/localization machinery and conclude that it introduces no independent source-facing theorem beyond the native Bałaban package.
4. **Native analytic domain.** R47--R49 recover the Paper-I four-condition `U_j^c` definition, its interior-space criterion, the correct `xi/g_j` field normalization, and close `CanonicalUjcEmbedding` with a scale/volume-uniform canonical Cauchy collar.
5. **Native product-Gaussian and activity interface.** R42--R45 replace unnecessary precision/Hessian reconstruction by the native CMP116 product-Gaussian chart and activity-level localization interface.
6. **Localized activity construction.** R50 locks the source objects `H(Z,Z0)` and `H(Z)`, their index stack, component factorization, single-term object (2.14), and pre-resummation majorant (2.26).
7. **D-stage summability.** R51 closes Eq. (2.29), using the Cammarota polymer/Mayer argument and an explicit entropy-versus-decay threshold.
8. **P-stage summability.** R52 closes the native four-positive-direction carrier and Eq. (2.31) bracket `4 M^4 exp(-2 rho) <= rho`.
9. **Post-P resummation.** R53 closes Eqs. (2.32)--(2.37), the seven-to-eight-delta reserve spend, and Lemma 3 / Eq. (2.38).
10. **Return to the inductive effective-action class.** The present R54 closes Eqs. (2.39)--(2.41) plus the separate normalization-term expansion, restoring the Paper-I next-scale effective-action bound. [7][21]

This is the complete mathematical control loop for the Paper-I/II small-field one-step mechanism relevant to the RP modification.

## 4. What remains but is not a small-field mathematical blocker

Several records remain open, but they must not be confused with an unclosed mathematical one-step induction:

### A. Project/formalization dictionaries

- exact source-to-Lean `D/P/Z0/Z0'` finite-index encodings;
- exact `H(Z)` summand/support/measurability dictionaries;
- project `physicalGaussian` pushforward equality;
- exact `Delta_1/Delta_a/P_j` Hessian/precision dictionary;
- exact finite covariance/root reconstruction interfaces.

These are formalization/custody side records. R42--R53 showed that none is required to state or execute the native source-level one-step proof.

### B. Optional RP coupling calibration

R21 identified the only allowed CP-even marginal local projection as the existing Wilson-action coefficient. The traversal has not computed a numerical RP-induced finite coupling shift `delta c_k` coefficient. That coefficient is **not** required to close the one-step class: the local extraction defines the new coupling coordinate and the complementary activity is what must satisfy the small-field bound, which is now controlled by the R26--R53 route.

An exact `delta c_k` value may matter later for a precise comparison of coupling schemes or `Lambda` parameters. It is therefore retained as optional scheme-calibration data, not as a live Paper-I/II induction theorem.

### C. Problems outside the small-field branch

The complete finite-volume density still contains the complement of the regular small-field region. Controlling that complement requires the later Bałaban `E/R/B` and large-field `R`-operation architecture. This is genuinely new mathematics and is not discharged by CMP116 Lemma 3.

## 5. Exit determination

The small-field branch has reached a natural STOP:

`Paper-I analytic domain`
`-> one-step fluctuation/product-Gaussian chart`
`-> localized H(Z)`
`-> D/P/post-P resummation`
`-> Lemma 3`
`-> polymer exponentiation`
`-> next-scale effective-action class`.

Hence

`SMALL-FIELD PAPER-I/II ONE-STEP: MATHEMATICALLY CLOSED FOR THE CURRENT RP-COMPATIBILITY TRAVERSAL`.

This statement is deliberately narrower than a Yang-Mills construction. It says that the reflection-positive modification no longer has an unresolved mathematical compatibility seam **inside the native regular small-field one-step mechanism**. It does not control the full density, large-field regions, infinite iteration to a continuum measure, Osterwalder-Schrader reconstruction, or the continuum spectral gap.

## 6. The next aperture is complete density

CMP119 [59] is the natural next layer. Its density expansion and `T`-operation organize the next-scale density into the regular effective-action contribution together with localized remainder and boundary/large-field sectors. The relevant source windows are the density form (2.18), the `T`-operation/action factorization (2.19)--(2.23), the regular `E` bounds (2.24)--(2.29), the localized `R` bound (2.31), and the `B`-term analyticity/bound (2.34)--(2.42). [59]

The later CMP122-I/II papers then supply the genuine large-field `R`-operation machinery rather than another refinement of the CMP116 small-field cluster estimate. [22][31]

Therefore the next traversal should enter through the **handoff architecture**, not jump directly to a final large-field bound.

## Negative results / guardrails

- Do not continue grinding CMP116 source-to-Lean dictionaries on the mathematical critical path merely because the independent formalization still labels them open.
- Do not claim that Lemma 3 alone closes the one-step induction; Eqs. (2.39)--(2.41) and the normalization term are part of the return to the inductive class.
- Do not treat the uncomputed numerical RP coupling shift as an obstruction to the existence of the one-step decomposition; it is optional scheme-calibration data unless a later `Lambda`-matching frontier requires it.
- Do not infer complete-density closure from small-field closure.
- Do not infer continuum Yang-Mills existence or a positive continuum mass gap.

## Next frontier — YM-R55

**CMP119 complete-density entry / E-R-B handoff architecture.**

Recover the exact source meaning and dependency order of CMP119 (2.18)--(2.23):

- what density is being decomposed;
- how the `T` operation separates regular local action, `R`, and boundary/large-field data;
- which parts consume the Paper-I/II small-field bound just closed;
- which obligations are genuinely deferred to CMP122-I/II;
- where complete-density control first introduces a mathematical object not already present in the small-field traversal.

This is the correct entry aperture for the large-field phase.

## References

Reused: [7] CMP109 / Paper I; [21] CMP116 / Paper II; [59] CMP119; [22], [31] Bałaban large-field/R-operation sources already present in the cumulative ledger. [80] Cammarota remains the most recently consumed source.

No new cumulative reference is consumed in R54. Highest remains **[80]**; next new source is **[81]**.
