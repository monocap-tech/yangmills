# YM-R22 — analytic-jet / polymer-norm closure

Date: 2026-09-15
Status: COMPLETE
Next cursor: `YM-R23`
Claim discipline: UNPROVED RESEARCH PROGRAM

## Target

Replace canonical-dimension heuristics by the actual source-shaped Bałaban induction. Determine the quantitative activity bound that a reflection-positive soft blocking kernel would have to satisfy, and identify the first compatibility defect between the candidate kernel and Bałaban's analytic/polymer machinery.

## Source-shaped polymer target

Bałaban Part II (CMP 116, 1988) exponentiates the one-step fluctuation-field cluster expansion and proves that the resulting terms satisfy the inductive assumptions. A source-extraction audit of the primary PDF identifies the key localized-activity estimate as Lemma 3 / Eq. (2.38):

`|H(Z)| <= C3 * epsilon1 * exp(-(1-8 delta) * (L kappa / 2) * d_{k+1}(Z))`.

The following polymer exponentiation, Eqs. (2.39)–(2.41), turns this into the next-scale effective-action bound of the same geometric type, with the exponent weakened from `1-8 delta` to `1-10 delta` and with an `O(1) C3 epsilon1` amplitude. The proof then chooses `delta,L` so the decay exponent renormalizes back to the inductive target and assumes the amplitude fits the next-scale `E0/2` budget.

The exact typography of the source should be checked against the primary PDF before publication transcription; the structural content is what is installed here: **a raw localized activity bound with exponential tree-distance decay is the input, and polymer exponentiation is the consumer**.

Thus the useful project abstraction is not merely a canonical-dimension statement but a weighted activity norm of the form

`||H||_{k,kappa} := sup_Z sup_{analytic domain} |H(Z)| exp(kappa d_k(Z))`,

where this notation is a project abstraction rather than claimed verbatim Bałaban notation.

## Consequence for the soft kernel

After vacuum and Wilson-action extraction from YM-R21, the modified blocking must generate a localized raw activity `H_soft(Z)` satisfying the same kind of source-shaped bound:

`|H_soft(Z)| <= epsilon_soft * exp(-kappa_soft d_{k+1}(Z))`,

with `epsilon_soft` small enough to enter the existing Lemma-3/polymer-exponentiation budget.

Therefore the correct insertion point is **before** Lemma 3, not after it as a truncated Symanzik effective action.

Canonical dimension six only predicts a possible scale gain in the local jet. It does not establish:

- analyticity on Bałaban's complex field domain;
- Cauchy derivative bounds;
- localization under the random-walk weakening parameters;
- exponential polymer tree-distance decay;
- cutoff/volume-uniform constants.

## New analytic compatibility defect

The R18 candidate kernel was written on the real compact group in matrix-Fisher form

`exp[ beta kappa Re Tr(V Q(U)^dagger) ]`.

Taken literally, `dagger`/`Re` is not holomorphic in independently complexified matrix coordinates. Bałaban-style Cauchy estimates and localization machinery require a holomorphic/complex-analytic extension on a controlled complex field domain. This is not cosmetic.

### Holomorphic repair candidate

Let

`Q_plus(U) = sum_gamma w_gamma U_gamma`,

and define the reverse-orientation holomorphic companion

`Q_sharp(U) = sum_gamma w_gamma U_gamma^{-1}`.

For compact-group fields, `Q_sharp(U) = Q_plus(U)^dagger` when the weights are real. On the complexified group, inversion is holomorphic. Define the complexified blocking potential

`Phi(V,U) = -(kappa/2) [ Tr(V Q_sharp(U)) + Tr(V^{-1} Q_plus(U)) ]`.

On the compact real form this agrees with `-kappa Re Tr(V Q(U)^dagger)`. It is holomorphic in complexified group variables wherever the group inverse is defined, and it retains endpoint gauge covariance because `Q_plus` and `Q_sharp` transform with opposite orientations.

This repairs the **formal holomorphy** problem of the local weight.

## Remaining normalization obstruction

A normalized Markov kernel requires

`Z(U) = integral_G exp[-beta Phi(V,U)] dV`,

and the effective local factor includes `-log Z(U)`.

On the real compact group `Z(U)>0`. On the complex analytic tube, however, constructive use of `log Z(U)` requires a **uniform zero-free complex neighborhood** and derivative/Cauchy bounds compatible with the Bałaban analytic radius.

This has not been proved.

The obstruction is sharper than generic analyticity:

1. the exponent carries the large factor `beta ~ g^{-2}`;
2. a small complex displacement can therefore amplify the phase/variation of the normalization integral;
3. the zero-free radius obtained from a crude continuity estimate could shrink with `g`;
4. Bałaban's induction requires the complex domain to remain large enough for the Cauchy/localization estimates used at every UV step.

Thus the first concrete analytic closure problem for the soft kernel is the normalization factor, not the quadratic Hessian.

## Source-side activity locality

The CMP 116 source-extraction record further identifies the actual localization mechanism:

- after the product-Gaussian change of variables the integrand still depends on whole-lattice external fields through propagators/operators;
- Bałaban introduces weakening parameters and generalized random-walk expansions;
- this produces localized activities `H(Z,Z0)` and `H(Z)`;
- Lemma 3 then supplies the exponential tree-distance bound;
- Eqs. (2.39)–(2.41) exponentiate it into the next effective action.

Therefore finite support of the original path kernel is **not sufficient by itself**. The soft perturbation must remain stable under the same nonlocal propagator/minimizer insertion followed by random-walk localization.

## Determination

R22 does not prove inductive closure. It does reduce the theorem deficit to two explicit analytic obligations:

1. **Holomorphic normalized-kernel obligation:** construct the reflection-adapted soft gauge kernel as a normalized holomorphic local functional on a complex field tube with a cutoff-uniform zero-free normalization factor and Cauchy bounds.

2. **Raw-activity obligation:** after one fluctuation integral and Bałaban localization, prove the added activity `H_soft(Z)` satisfies the same Lemma-3-type exponential polymer bound with amplitude small enough for the existing exponentiation budget.

The quadratic `p^4` irrelevance and coupling-coordinate extraction from YM-R19/R21 are necessary but not sufficient.

## Negative results

- Do not treat `Re Tr(V Q^dagger)` as automatically compatible with complex-analytic Cauchy norms.
- Do not infer polymer decay from finite-range path support before the propagator/minimizer localization step.
- Do not infer the CMP 116 Lemma-3 activity bound from engineering dimension alone.
- Do not use scalar/QED analytic-radius constants as 4d Yang–Mills constants.

## Next frontier

`YM-R23 — normalized-kernel holomorphy / zero-free-radius audit`

Questions:

- Can the local normalization be chosen field-independent, eliminating `log Z(U)`?
- If not, can one prove a zero-free complex tube for the matrix-Fisher normalization with radius compatible with Bałaban's small-field analytic domain?
- Is a heat-kernel or convex-mixture blocking kernel preferable because it is normalized by construction and still admits the required weak-field Gaussian Hessian?
- Which candidate preserves the R18 reflection-half-space factorization and R19 quadratic matching simultaneously?

## References

Repeated: [7], [21], [32], [67].

New controls: [69] Dimock 2013 (methodological, scalar model); [70] Bałaban–O'Carroll–Schor 1991 (complex-gauge analyticity control example, not 4d pure-YM closure).
