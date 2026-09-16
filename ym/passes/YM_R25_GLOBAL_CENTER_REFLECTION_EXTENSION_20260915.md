# YM-R25 — global center / reflection-covariant extension audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R26 (unconsumed)

## Target
Construct, or rule out, a globally defined coarse-link center `C_e(U) in G` suitable for a single translated heat-kernel block kernel, requiring:

- endpoint gauge covariance;
- orientation covariance;
- OS reflection covariance;
- positive-half-space locality;
- global continuity / measurability;
- and the Bałaban/Federbush weak-field analytic jet `C_e(exp(gA)) = exp(g(QA)_e + O(g^2))`.

The target is deliberately weaker than a global canonical symmetric group mean.

## Source-attested facts

1. Federbush 1987 [60] states that the block-spin map is a continuous function of finitely many fine path holonomies, agrees in the small-field region with a Bałaban-type invariant-distance average, and is supplied with a suitable continuous extension to large fields. The same paper states that in logarithmic coordinates near the identity the map is complex analytic, has no constant term, and its linear term is the same Abelian averaging operator used in the earlier construction.

2. Bałaban's averaging paper [35] is the primary source family for gauge-field averaging operations. Bałaban's regular-configuration paper [62] confirms that the analytic machinery is organized on regular small-field charts rather than requiring global analyticity over all configurations.

## Construction

Fix an oriented coarse edge `e=(x,y)`. Choose a finite family of fine paths

`Gamma_e = {gamma_0, gamma_1, ..., gamma_m}`

from `x` to `y`, with weights `w_j >= 0`, `sum_j w_j = 1`. Choose `gamma_0` to be the canonical straight fine path along the coarse edge. Transport the entire path family and the weights covariantly under lattice symmetries/reflection.

Let

`U_j = U(gamma_j)`

and define relative endpoint loops

`R_j = U_0^{-1} U_j in G`.

Choose a conjugation- and inversion-invariant logarithm neighborhood `O` of the identity on which the principal logarithm `ell` is analytic, with

`ell(hRh^{-1}) = Ad_h ell(R)`

and

`ell(R^{-1}) = -ell(R)`.

Choose a smooth conjugation- and inversion-invariant cutoff `chi:G->[0,1]` such that:

- `chi=1` on a smaller neighborhood `O_1`;
- `supp chi` is compactly contained in `O`.

Define the globally smooth Lie-algebra map

`phi(R) = chi(R) ell(R)` for `R in O`,

extended by `0` outside `O`.

Because `chi` vanishes before the boundary of the logarithm chart, `phi` is globally continuous/smooth, conjugation equivariant, and inversion odd:

`phi(hRh^{-1}) = Ad_h phi(R)`,

`phi(R^{-1}) = -phi(R)`.

Now define

`S_e(U) = sum_j w_j phi(R_j)`

and

`C_e(U) = U_0 exp(S_e(U))`.

This is the proposed global center.

## Gauge covariance

Under endpoint gauge transformations,

`U_j -> g_x U_j g_y^{-1}`,

so

`R_j -> g_y R_j g_y^{-1}`.

Hence

`S_e -> Ad_{g_y} S_e`

and therefore

`C_e(U^g) = g_x C_e(U) g_y^{-1}`.

Thus the center has exact endpoint gauge covariance globally.

## Orientation covariance

For the reversed edge `e^{-1}`, choose the reversed path family `gamma_j^{-1}` and distinguished path `gamma_0^{-1}`. Then

`R'_j = U_0 R_j^{-1} U_0^{-1}`.

By conjugation covariance and inversion oddness of `phi`,

`S_{e^{-1}} = Ad_{U_0}(-S_e)`.

Therefore

`C_{e^{-1}} = U_0^{-1} exp(Ad_{U_0}(-S_e)) = exp(-S_e) U_0^{-1} = C_e^{-1}`.

So exact orientation reversal is preserved.

## Reflection covariance and half-space locality

Choose the path assignment equivariantly under the OS reflection `theta`. For a coarse link strictly inside the positive half-space, choose every path in `Gamma_e` inside the positive half-space. Coarse links on/crossing the reflection plane are treated as boundary variables with a separately reflection-symmetric prescription.

Because the construction uses only path holonomies, inversion, conjugation-equivariant `phi`, and the reflection-transported path family, the center obeys the corresponding reflected orientation law. In particular, when reflection reverses the link orientation, the preceding orientation calculation gives the required inverse.

Thus, for bulk positive links, `C_e(U)` depends only on positive-half-space fine links. This is the support property needed for the conditionally factorized single-center heat-kernel kernel from YM-R18/R24.

## Local analytic jet

On the regular chart where all `R_j in O_1`, `chi=1` and `phi=ell`, so the center is genuinely analytic there.

Write

`U_j = exp(g P_j A + O(g^2))`.

Then

`R_j = exp(g(P_j-P_0)A + O(g^2))`,

hence

`S_e = g sum_j w_j (P_j-P_0)A + O(g^2)`.

Since `sum_j w_j = 1`,

`P_0 + sum_j w_j(P_j-P_0) = sum_j w_j P_j = Q`.

Therefore Baker-Campbell-Hausdorff gives

`C_e(exp(gA)) = exp(g(QA)_e + O(g^2))`.

This is exactly the weak-field jet required by the single-center heat-kernel construction.

Federbush [60] independently supplies the historical precedent that the small-field block-spin map is complex analytic, has the Abelian linear part, and may be continuously extended to large fields. The construction above makes one such extension explicit without requiring Federbush's detailed large-field prescription.

## Hypercubic symmetry

The distinguished `gamma_0` does not necessarily break lattice symmetry: for an oriented coarse edge on an odd-block lattice there is a geometrically canonical straight fine path. If the alternative path family, weights, and cutoff are generated covariantly from this datum, lattice rotations/reflections map the construction for `e` into the construction for the transformed edge.

The construction therefore avoids the topological no-global-mean obstruction from YM-R17 by sacrificing permutation symmetry among all paths, not by sacrificing physical lattice covariance.

## Relation to the YM-R17 obstruction

This center is not a globally symmetric idempotent mean. Outside the regular chart the relative-path correction is switched off and the center tends toward the distinguished straight-path holonomy. Hence the maximal-torus `nA=I` obstruction does not apply.

The construction only requires global continuity/smoothness and exact gauge/orientation/reflection covariance, while complex analyticity is required solely on the regular small-field chart used in the UV estimates.

## Consequence for the heat-kernel blocker

Define the exact normalized block kernel

`K_e(dV|U) = rho_{t_k}(V C_e(U)^{-1}) dV_Haar`.

Then:

- Haar translation gives exact normalization;
- centrality of `rho_t` plus gauge covariance of `C_e` gives gauge covariance;
- reflection/orientation covariance and half-space locality of `C_e` give the YM-R18 conditional RP factorization;
- the weak-field limit is a single Gaussian centered at `QA`, giving the Bałaban-type `M + a Q^* Q` Hessian when `t_k = g_k^2/a`;
- the nonlinear center correction begins at positive powers of `g_k` on the analytic chart.

Thus the global-center existence problem is structurally closed.

## Negative result / scope

This does NOT prove the modified RG closes in the 4d Bałaban induction. The new remaining obligation is quantitative: on the fixed complex small-field tube, obtain derivative/Cauchy bounds for the center's nonlinear jet and the translated heat-kernel correction, then pass them through fluctuation integration/random-walk localization to a CMP116 Lemma-3-type activity bound.

The large-field cutoff transition is only smooth, not holomorphic. This is acceptable only because Bałaban's analytic UV estimates are performed on the regular chart where `chi=1`; large-field sectors must remain in exact nonperturbative bookkeeping rather than be inserted into small-field Cauchy estimates.

## Determination

`YM-R25 COMPLETE -> YM-R26`.

The preferred exact blocking architecture is now:

`global cutoff center C_e(U)`
`-> single translated group heat kernel`
`-> exact Markov normalization + RP factorization`
`-> Bałaban Gaussian Hessian`
`-> O(g) analytic local remainder`.

## Next frontier

YM-R26 — cutoff-center analytic remainder / one-step activity closure.

Target: prove equation-level bounds on the nonlinear local jet of `C_e`, combine them with compact-group small-time heat-kernel asymptotics on the fixed complex tube, and determine whether the resulting raw activity fits the CMP116 localization/smallness budget after Wilson-action extraction.