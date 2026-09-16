# YM-R37 — exact precision identity / small-background defect audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R36_20260916.json`
Next cursor: YM-R38 (unconsumed)

## Question

Does the source-facing `NativeLocalPrecisionCertificate` require a separate analytic regularity package, or does a correctly identified finite-range physical precision plus one small-background defect estimate generate the needed coercivity/resolvent/root control?

## Source-attested spine

Existing custody already records the relevant Bałaban source architecture:

- CMP99 defines the background-field operator `Delta_a(U)` and the Dirichlet Green operator `G(U)`; its recorded theorems provide positivity and background-field propagator bounds.
- CMP102 gives the variational/background-field second-variation route, including the positive quadratic Hessian form at the transformed critical configuration.
- The exact source-to-project dictionary between the CMP99/CMP102 symbols and the project precision remains open.

No new bibliography source is introduced here.

## Derivation: one local defect estimate is analytically sufficient

Assume that, after the source dictionary is fixed, the physical precision satisfies

`P_j(exp(g_j A)) = P_0,j + E_j(A)`

on the fixed canonical background domain, with

`||E_j(A)|| <= C_E g_j`

uniformly in UV scale and volume, and assume the flat/reference operator obeys

`Re <v,P_0,j v> >= lambda_0 ||v||^2`

with `lambda_0 > 0` uniform.

Then for sufficiently small coupling,

`Re <v,P_j v> >= (lambda_0 - C_E g_j)||v||^2 >= (lambda_0/2)||v||^2`.

Thus real and complex coercivity do not need to be separately sourced once the defect estimate is valid on the complex canonical collar.

## Local kernel form is enough

A source theorem need not state the defect in global operator norm. If

`|E_j(A;x,y)| <= C g_j 1_{d(x,y)<=r}`

with fixed range `r` and uniformly bounded local degree, the Schur estimate gives

`||E_j(A)||_{2->2} <= C' g_j`

with no volume factor.

Hence a finite-range local `O(g_j)` estimate is sufficient.

## Resolvent and root control are downstream

Finite range plus a uniform coercive gap gives weighted-resolvent decay by the standard exponential-weight/Neumann argument. The inverse square root then follows from analytic functional calculus, and the already-custodied matrix-function controls give exponential root decay and higher background derivatives.

Therefore the following are consequences rather than independent source obligations:

- real coercivity;
- complex coercivity;
- uniform inverse norm;
- weighted resolvent decay;
- inverse-square-root norm/decay;
- higher background derivatives of the root.

## Remaining residue

The analytic package therefore collapses to source identification plus one local perturbative estimate. The unresolved source-facing items are:

1. identify CMP102 `Delta_1` and CMP99 `Delta_a/G(U)` with the same physical fluctuation precision on the correct gauge-fixed domain;
2. fix sign, normalization and coordinate conventions;
3. verify the finite-range/holomorphic local dependence of that same operator;
4. source or derive the uniform local defect `P_j(exp(g_j A))-P_0,j = O(g_j)`.

The main danger is no longer analysis; it is silently identifying unlike source operators.

## Determination

`NativeLocalPrecisionCertificate` is not an independent coercivity/resolvent/root theorem package. Its analytic content reduces to a source dictionary, local finite-range holomorphic dependence, a flat/reference gap, and one local `O(g_j)` small-background defect estimate. Everything else is downstream.

## Negative results / guardrails

- Do not source separate real and complex coercivity if the local defect plus reference gap are available.
- Do not require the source defect in global matrix norm if a fixed-range local kernel bound is available.
- Do not identify `Delta_1`, `Delta_a` and the project precision merely because all are called Hessian/precision operators.
- Do not consume a new source for generic matrix-function decay already covered by the existing analytic-control references.

## Next frontier — YM-R38

**`Delta_1/Delta_a/P_j` gauge-slice and normalization dictionary.**

Determine the exact native domain on which CMP99 inverts its precision, whether an ambient projector is genuinely required, and which scale/sign/inner-product factors belong to coordinate transport rather than theorem hypotheses.

## References

Reused existing CMP99/CMP102 custody and the previously numbered analytic-control sources. No new cumulative source is consumed. Highest source ID remains **[79]**; next new source is **[80]**.
