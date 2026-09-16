# YM-R32 — complex precision/coercivity / exact source-domain audit

Date: 2026-09-15
Status: COMPLETE
Claim status: UNPROVED RESEARCH PROGRAM
Previous head: `ym/checkpoints/YM_HEAD_R31_20260915.json`
Next cursor: YM-R33

## Question

Can the native Bałaban covariance-root package be supplied with a scale/volume-uniform complex resolvent margin on the actual small-field analytic domain, rather than only real-field positivity?

## Source facts recovered

### CMP99 background-field propagator regime

Bałaban's background-field paper [79] defines the Green operator in the form

`G(U) = (Delta_a | Omega_0)^(-1)`

and the auxiliary source audit has visually confirmed the following source anchors:

1. Theorems 3.3 and inequalities (3.42)–(3.47): regularity/decay estimates for `G(U)` under the stated hypotheses.
2. Theorem 3.11: positivity of the relevant propagator/operator family.
3. Theorem 3.12: the preceding estimates persist for external gauge fields satisfying regularity conditions (3.35),(3.36), with `alpha_0` sufficiently small.
4. Theorem 3.15: for `M alpha_0` sufficiently small, the covariance `C^(k)(A)` has a scale-uniform exponential kernel bound of the form

   `||C^(k)(Lambda; y,y')|| <= B_0 exp(-delta_0 ||y-y'||)`.

These are real/external-field source results; no claim is made that CMP99 itself prints the exact complex-sectorial inequality derived below. [79]

### CMP116 analytic field domain

The CMP116 source audit locates the termwise cluster estimate on the complex analytic domain written

`U^c_{k+1}(X, alpha_0, alpha_1)`.

The source restrictions later in the Lemma-3 argument require `(LM)^4 alpha_0`, `(LM)^4 alpha_1`, `(LM)^4 alpha_4`, and `(LM)^4 gamma_2` to remain bounded by fixed M-independent constants. Thus the analytic neighborhood is governed by fixed inductive parameters once the block parameters are fixed; the source record does not force a radius tending to infinity or zero with the RG step. The exact source-to-project field-variable dictionary for this domain remains open. [21]

## Derived operator statement

Let `A_k(U)` denote the exact local gauge-fixed precision corresponding to the CMP99/CMP116 Gaussian covariance, after the still-open source dictionary is supplied.

Assume on the real admissible small-field backgrounds:

1. `A_k(U_r)` is self-adjoint and positive;
2. the source Green/covariance decay bounds imply a volume/scale-uniform inverse bound

   `||A_k(U_r)^(-1)|| <= G_0`;

3. `A_k(U)` is finite range / bounded coordination and analytic in the local link variables on a complex neighborhood.

Then positivity plus the inverse bound gives a real coercivity margin

`A_k(U_r) >= m_0 I`,  `m_0 := G_0^(-1) > 0`.

Because each row of the precision contains only O(1) local matrix blocks, local analyticity gives a volume-independent Schur/operator bound

`||A_k(U_c)-A_k(U_r)|| <= K_loc delta`

when the complex background lies within local complex distance `delta` of a real admissible background. The constant `K_loc` depends on the fixed local geometry and analytic derivative bounds, not on volume.

Choose a smaller complex sub-tube

`delta_* <= min(delta_source, m_0/(2 K_loc))`.

Then for every vector `v`,

`Re <v,A_k(U_c)v>`
`>= <v,A_k(U_r)v> - ||A_k(U_c)-A_k(U_r)|| ||v||^2`
`>= (m_0/2) ||v||^2`.

Therefore

`boxed: Re A_k(U_c) >= (m_0/2) I`

uniformly in UV scale and volume on this smaller fixed complex sub-domain.

This is a project derivation, not a quotation from CMP99/CMP116.

## Uniform resolvent consequence

For `r >= 0`, sectorial coercivity immediately gives

`||(A_k(U_c)+r I)^(-1)|| <= 1/(m_0/2 + r)`.

This is especially convenient because the native covariance-root representation can be written as the Stieltjes/functional-calculus integral

`A^(-1/2) = (1/pi) integral_0^infinity r^(-1/2) (A+r)^(-1) dr`.

Thus the complex root exists with a scale/volume-uniform norm bound throughout the smaller tube. Combined with the local derivative support and the R31 resolvent-chain identity, the same tube yields

`||D_{b_1}...D_{b_n} A_k(U)^(-1/2)(x,y)||`
`<= n! K^n exp(-mu' T(x,y,b_1,...,b_n))`

provided the localized resolvent has the corresponding Combes-Thomas/random-walk exponential bound.

## Why the uniformity is not volume-dangerous

The complex perturbation is local. If each precision row couples only a fixed number of neighboring bonds/sites and every local coefficient changes by at most `c delta`, then the row and column sums of the perturbation are O(delta) independently of the number of lattice sites. The Schur bound therefore does not accumulate an extensive volume factor.

This is the key reason a fixed complex tube is compatible with a thermodynamic/UV-uniform resolvent margin.

## Exact scope / remaining dictionary debt

R32 does **not** identify the repository precision with CMP99 `Delta_a`, CMP99 `C^(k)(A)`, and the CMP116 covariance in a theorem-ready source dictionary. The auxiliary source corpus explicitly keeps this mapping open.

R32 also does not claim that the entire printed domain `U^c_{k+1}(X,alpha_0,alpha_1)` enjoys the derived coercivity margin. The conclusion only requires a smaller source-contained complex subdomain. This is sufficient for Cauchy/weakening estimates if the subdomain still contains the evaluation domain with a fixed positive Cauchy collar.

Thus the native analytic problem separates as

`source real propagator/coercivity`
`+ local analytic finite-range precision`
`=> fixed complex sectorial subtube`
`=> R31 root derivative/tree decay`
`=> CMP116 weakening localization`.

The remaining source-native issue is no longer complex invertibility itself. It is the exact identification of:

- the CMP99/CMP116 precision/covariance variables;
- the inner/evaluation domain and outer complex Cauchy collar;
- the localization-domain enlargement `Z0 -> Z` and background-support ownership used in CMP116 (2.7)–(2.10).

## Determination

The complex-resolvent obstruction is structurally closed modulo the already-existing precision dictionary:

`boxed: real uniform coercivity + local analyticity => a fixed volume-uniform complex coercive subtube.`

No scale-dependent collapse of the complex radius is forced.

This means the live frontier moves downstream to the exact Cauchy-collar/support-enlargement dictionary rather than another propagator theorem.

## Negative results / guardrails

1. Do not claim CMP99 directly proves the complex-sectorial inequality; it is a derived perturbative consequence.
2. Do not use mere finite-dimensional positivity as a uniform coercivity theorem; the uniform inverse/decay bound is essential.
3. Do not claim the full CMP116 complex domain is coercive when only a smaller fixed subtube has been justified.
4. Do not collapse the source-to-project precision dictionary into notation matching.

## References

[21] T. Bałaban, *Renormalization group approach to lattice gauge field theories II: Cluster expansions*, Commun. Math. Phys. 116 (1988), 1–22.

[76] M. Benzi and N. Razouk, *Decay bounds and O(n) algorithms for approximating functions of sparse matrices*, ETNA 28 (2007/08), 16–39.

[78] N. J. Higham and S. D. Relton, *Higher Order Fréchet Derivatives of Matrix Functions and the Level-2 Condition Number*, SIAM J. Matrix Anal. Appl. 35 (2014), 1019–1037.

[79] T. Bałaban, *Propagators for lattice gauge theories in a background field*, Commun. Math. Phys. 99 (1985), 389–434.

## Next frontier

`YM-R33 — Cauchy-collar / support-enlargement dictionary audit`.

Target: extract the two nested field domains actually used by CMP116 and the exact geometry by which interpolation/random-walk weakening turns dependence on the global external field into dependence on the enlarged localization set `Z`, so that `activeSupport` / `fluctuationSupport` can be typed without inventing an exact finite root decomposition.
