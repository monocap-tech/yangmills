# YM-R24 — coercivity / complex-tube window audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: `YM-R25` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM

## Target

Test whether the reflection-positive heat-kernel blocking candidate from YM-R23 admits a UV-uniform parameter window combining:

1. a nonzero Gaussian block coercivity coefficient `a` in the linearized operator `M + a Q*Q`, and
2. complex-analytic control on the Cauchy tube used by the Bałaban inductive scheme.

A secondary 2026 source audit, explicitly retained only as a locator/audit source rather than a replacement for the primary papers, reports that the large-field Bałaban scheme uses a complex fast-field radius `hat alpha_1(gamma)>0` that depends on a fixed weak-coupling threshold `gamma` but is uniform in the RG step `k` while the effective couplings remain in `(0,gamma]`. This is consistent with the step-uniform analyticity demanded by the published UV-stability theorem. Direct equation-level verification from the primary CMP 122-II PDF remains desirable.

## Finding 1 — the relevant Cauchy radius is not the full small-field envelope

The project had provisionally written a generic canonical radius `R_k` and worried that it might grow as the bare coupling tends to zero, making heat-kernel holomorphic growth `exp(C a R_k^2)` uncontrollable.

That conflates two different domains:

- the *physical small/large-field threshold* used to decide where nonlinear gauge coordinates remain regular and where large-field suppression is invoked; and
- the *local complex Cauchy tube* around an admissible background used to differentiate polymer activities.

The available Bałaban-source extraction reports the second radius as a fixed positive constant `hat alpha_1(gamma)` uniform in `k`, not as a radius diverging with `g_k^{-1}`.

Therefore a fixed positive blocking coefficient `a` gives a scale-uniform raw holomorphic growth factor of the schematic form

`exp(C a hat_alpha_1(gamma)^2)`

rather than an automatic UV divergence.

This removes the specific scale-collapse scenario posed at YM-R23. It does not yet prove the kernel satisfies the polymer smallness budget.

## Finding 2 — the leading Gaussian must be part of the reference measure

For compact-group heat kernel `rho_t`, the local small-time parametrix near the identity has the Gaussian form

`rho_t(exp X) = c_t exp(-|X|^2/(const*t)) * [Jacobian/curvature factor + higher t terms]`

on a fixed normal neighborhood, with holomorphic continuation supplied by the compact-group heat-kernel theory.

Putting

`X = g_k Y`, `t_k = g_k^2/a`

gives

`rho_{t_k}(exp(g_k Y)) = c_k exp(-a |Y|^2/const) * J_{k,a}(Y)`.

On any fixed complex tube `|Y| < R`, the local geometric factor has an expansion

`J_{k,a}(Y) = 1 + O(g_k^2)`

(with non-principal geodesic/image terms exponentially small in `1/g_k^2`, subject to the usual normal-neighborhood restriction).

Hence the factor `exp(C a R^2)` belongs to the *Gaussian reference kernel* itself and should not be charged wholesale against the polymer activity smallness budget. The object that must be small after Gaussian extraction is the residual analytic factor.

This substantially weakens the apparent coercivity-versus-holomorphy conflict for a **single-center** translated heat kernel.

## Finding 3 — the convex path mixture has a more serious defect

The normalized mixture proposed in YM-R23 was

`K(B|A) ~ sum_j w_j rho_{g_k^2/a}( exp(g_k B) exp(-g_k P_j A + ...))`.

Taking `g_k -> 0` at fixed canonical fields gives the nontrivial limit

`K_0(B|A) proportional to sum_j w_j exp[-(a/2)||B-P_j A||^2]`.

Unless all `P_j A` coincide, this is a **mixture of distinct Gaussians**, not a single Gaussian.

Consequently, after taking `-log` or integrating against a Gaussian fine measure, the higher canonical-field cumulants of the blocking kernel are generically `O(1)` as `g_k -> 0`; they are not automatically `O(g_k)` or `O(g_k^2)` perturbations of the Gaussian fixed point.

The quadratic Hessian calculation of YM-R23 remains correct, including the positive path-variance operator

`D = sum_j w_j P_j^*P_j - Q^*Q`,

but Hessian agreement alone is insufficient. The full leading kernel can alter the Gaussian fixed-point transformation at order one.

This is a stronger defect than the complex-growth issue.

## Finding 4 — the clean replacement is a single translated heat kernel

A better normalized-by-construction kernel is

`K_e(dV|U) = rho_{t_k}( V C_e(U)^{-1}) dV_Haar`,

where `C_e(U) in G` is a globally defined gauge-covariant block center satisfying on the regular small-field chart

`C_e(exp(g A)) = exp( g (Q A)_e + O(g^2) )`.

Then:

- normalization is field-independent by Haar translation;
- the compact-group heat kernel supplies holomorphic continuation;
- the `g_k -> 0` canonical-field limit is a single Gaussian centered at `Q A`;
- the fine-field Hessian is exactly of the `M + a Q^*Q` type;
- nonlinear block-center corrections begin at positive powers of `g_k` in canonical variables.

The topological obstruction found in YM-R17 does not forbid such a center. It only forbids demanding a globally continuous, fully permutation-symmetric, idempotent group mean. A global center may sacrifice those unnecessary properties outside the regular chart while retaining gauge covariance, reflection covariance, locality, and the correct small-field jet.

Federbush [60] is direct precedent: his block-spin transformation uses Bałaban-type invariant-distance averaging in the small-field region, states that the resulting block-spin function is continuous, and uses a suitable continuous extension to large-field configurations. He also states that in the small-field chart the transformation is complex analytic and has the same linear part as the Abelian block transformation. His definition differs slightly from Bałaban's original one and does not by itself prove the OS half-space/reflection contract required here.

## Determination

The specific YM-R23 fear

`fixed coercivity a > 0` versus `UV-shrinking holomorphic window`

is not supported by the available source extraction: the relevant Bałaban Cauchy radius is step-uniform in the weak-coupling regime.

However, the **convex path-mixture kernel is demoted** because its canonical `g -> 0` limit is generically non-Gaussian at order one. The preferred candidate is now a **single translated heat kernel centered on a globally extended deterministic block map** whose small-field jet is Bałaban's linear average.

This returns one obligation from YM-R17 in a weaker and more tractable form: we no longer require a globally symmetric group mean, only a global gauge/reflection-covariant center agreeing with the local Bałaban average where the analytic RG is performed.

## Next frontier — YM-R25

`YM-R25 — global center / reflection-covariant extension audit`

Audit whether a global center `C_e(U)` can be chosen with all of:

1. endpoint gauge covariance;
2. orientation inversion covariance;
3. OS reflection covariance;
4. positive-half-space support for reflection-aligned blocks;
5. continuity/measurability on all configurations;
6. complex analyticity on the regular small-field chart;
7. small-field expansion `C_e(exp(gA)) = exp(g Q A + O(g^2))` with the Bałaban linear `Q`;
8. uniform derivative bounds sufficient for the raw-activity localization step.

Federbush [60] should be audited as the leading constructive precedent. If his extension can be reflection-adapted without changing the local jet, the heat-kernel normalization/holomorphy problem is effectively closed and the live UV deficit returns to the CMP116-style activity bound.
