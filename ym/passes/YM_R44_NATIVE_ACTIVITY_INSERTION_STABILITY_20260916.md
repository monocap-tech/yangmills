# YM-R44 — native activity insertion stability / root-reconstruction minimization

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R43_20260916.json`
Next cursor: YM-R45 (unconsumed)

## Target

Test whether the RP blocker needs an exact project reconstruction of the CMP116 covariance root `(C^(k))^(1/2)`, or whether it can consume the source-native localized activities `H(Z,Z0)` and `H(Z)` directly.

## Source-attested architecture

CMP116 (2.5)-(2.6) places the conditioned/localized fluctuation integral in product-Gaussian coordinates by the native change `B'=(C^(k))^(1/2)X`.

CMP116 (2.7)-(2.10) then introduces localization/weakening parameters, generalized random-walk expansions and a resolvent/series treatment of the covariance root, and rewrites the product-Gaussian expression into native localized activities `H(Z,Z0)` and `H(Z)`, with component factorization.

The source audit explicitly records that the later estimates (2.14)-(2.38) bound the resummed localized activity `H(Z)` and do NOT state an exact finite root-piece reconstruction of `(C^(k))^(1/2)`.

Thus a finite exact root decomposition is not source-native output and must not be promoted to a blocker prerequisite.

## Blocker insertion in the native chart

R26 gives, on the canonical weak-field tube,

`K_soft = K_Gauss * exp(V_soft)`,

with fixed local support and analytic norm `||V_soft|| = O(g_k)`.

R43 shows that after the already-existing CMP116 Gaussian change of variables this becomes the same native post-(2.6) integrand multiplied by

`exp(V_soft((C^(k))^(1/2) X))`.

No second Jacobian occurs.

Introduce an interpolation parameter `t in [0,1]` and define

`G_t = G_native * exp(t V_soft((C^(k))^(1/2)X))`.

For each fixed t, apply the SAME source localization construction used after (2.6), producing native activities

`H_t(Z,Z0)` and `H_t(Z)`.

This step does not require a project-level root operator or an exact finite root-piece equality. It uses the source's own generalized random-walk/resolvent localization exactly in the form in which CMP116 proves the activity expansion.

## Derived stability estimate

On the canonical tube,

`|V_soft| <= C g_k`

and fixed-order derivatives are `O(g_k)`. Hence uniformly for `0 <= t <= 1`,

`|exp(t V_soft)| <= exp(C g_k) = O(1)`

and differentiating the interpolated integrand with respect to t inserts exactly one factor `V_soft`, carrying one factor `O(g_k)`.

The same weakening/random-walk derivatives used in the CMP116 localization act either on native propagator/root dependence or on the inserted analytic local factor. The latter has fixed initial support and bounded Cauchy derivatives. Therefore every contribution to the activity difference that reaches a localization domain Z contains the same source-native random-walk connectivity needed to connect that fixed support to Z.

Using the native weighted summability/decay margin and spending a finite amount of exponent gives the source-native stability form

`|H_1(Z) - H_0(Z)| <= C_soft g_k exp(-mu' d_k(Z))`,

for any fixed `mu'` below the native localization margin, uniformly in UV step/volume once the weak-coupling ceiling and source analytic domain are fixed.

Equivalently define

`H_soft(Z) := H_1(Z)-H_0(Z)`.

Then

`|H_soft(Z)| <= C_soft g_k exp(-mu' d_k(Z))`.

This is the activity-level form of the R29 conclusion, now stated without an exact project root reconstruction.

## Important qualification

This is a DERIVATION conditional on the SAME source-native localization estimates being uniform along the interpolation `G_t`. CMP116 supplies the native localization mechanism and the resummed H(Z) estimates; the project still has to verify that the inserted factor lies in the source analytic/local class with the required support typing. R26 supplies the analytic O(g_k) part; the remaining issue is source-domain/support anchoring.

The derivation does NOT claim:

- an exact finite root-piece identity;
- a project covariance-root theorem;
- a source-to-Lean `H(Z)` index/summand dictionary;
- a new CMP116 theorem stated explicitly for arbitrary multiplicative perturbations.

Those are separate reconstruction/formalization questions.

## Critical-path minimization

For the RP blocker, replace the former requirement

`exact project root reconstruction -> project local activity`

by the source-native interface

`CMP116ProductGaussianChart + NativeActivityInsertionStability`.

The blocker-critical chain is now

`V_soft = O(g_k), fixed support`
`-> native CMP116 X-chart`
`-> native CMP116 localization of G_t`
`-> H_soft(Z)=H_1(Z)-H_0(Z)`
`-> O(g_k) exp(-mu' d_k(Z))`
`-> R28 epsilon_1 reserve absorption`.

Thus exact reconstruction of `(C^(k))^(1/2)` in project coordinates is not blocker-specific theorem debt.

## Remaining native seam

The surviving blocker-specific source/dictionary requirement is narrower:

`NativeInsertionSupportAnchor`

It must identify the finite bonds/blocks on which `V_soft` initially depends with the source localization-domain language (`Y0`, `Z0`, enlargements) strongly enough that the source random-walk connectivity/metric used in the H(Z) estimate can be applied.

This is a finite carrier/domain typing problem, not a covariance-root or Hessian theorem.

## Determination

R44 closes the root-reconstruction minimization positively:

**The RP blocker does not require an exact project reconstruction of the covariance root. It is sufficient to compare the native CMP116 localized activities before and after inserting the bounded-support O(g_k) analytic factor.**

The exact `H(Z,Z0)` / `H(Z)` source-to-Lean dictionary remains open for full formal reconstruction, but it is not an additional blocker-specific mathematical hypothesis once the argument is kept in source-native activity coordinates.

## Next frontier — YM-R45

**Native insertion support-anchor / localization-domain audit.**

Identify the minimum finite dictionary from the blocker bond/block support to CMP116's `Y0`, `Z0` and enlargement conventions needed to instantiate the activity-difference decay above. Determine whether this is already supplied by the block geometry and the source's smallest-localization-domain construction, or whether one explicit support theorem remains.

References reused: [21] CMP116 and prior native Balaban sources. No new cumulative source ID consumed. Highest remains [79]; [80] remains next.
