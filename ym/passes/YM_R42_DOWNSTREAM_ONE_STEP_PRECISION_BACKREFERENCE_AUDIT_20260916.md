# YM-R42 — downstream one-step precision back-reference audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R41_20260916.json`
Next cursor: YM-R43 (unconsumed)

## Question

R41 left the direct CMP102 `Delta_1` definition provenance gate unresolved. R42 asks whether the downstream one-step source spine in CMP109/CMP116 actually requires that Hessian identification for the reflection-positive blocker, or whether the native fluctuation covariance/root is already the source-facing object consumed by the cluster expansion.

The admissible target is narrow:

1. identify the covariance/root actually used in the Part-I/Part-II fluctuation integral;
2. determine whether the unresolved `Delta_1/Delta_a/P_j` dictionary is on the critical path to CMP116 localization;
3. determine whether the local `P_j(exp(g_j A))-P_0,j = O(g_j)` defect is a native source obligation or only one sufficient reconstruction route.

No new bibliography source is consumed.

## Source-attested facts

### [21] CMP116 directly consumes `C^(k)` and its square root

The source-extracted CMP116 window at equations (2.5)--(2.6) conditions the correlated fluctuation Gaussian and performs the linear change of variables

`B' = (C^(k))^(1/2) X`,

rewriting the integral against the product standard Gaussian `dmu_0(X)`. The covariance/root-dependent terms move into the integrand.

The following source-extracted window, equation (2.7) and equations (2.8)--(2.10), localizes `(C^(k))^(1/2)` by a resolvent/series representation and generalized random-walk expansions, producing localized activities `H(Z,Z0)` and `H(Z)`.

Thus the cluster-expansion stage is source-shaped as

`correlated Gaussian with covariance C^(k)`
` -> B'=(C^(k))^(1/2)X`
` -> product Gaussian`
` -> localization of (C^(k))^(1/2)`.

This is stronger than a generic claim that some positive precision possesses an inverse square root: the native source actually names and uses the covariance root.

### [21] `Delta_k` remains a distinct operand in the localized integrand

The source extraction after (2.6) records the global integrand schematically as depending on

`G(Z0, X, C^(k)(Z0), (C^(k))^(1/2), Delta_k)`.

Therefore the current source evidence does not license replacing all of these objects by one symbol or asserting from notation alone that

`Delta_k = (C^(k))^(-1)`.

They may of course be related by the Part-I construction, but that relation is a separate dictionary statement and is not needed merely to state the CMP116 Gaussian/root localization mechanism.

### [79] CMP99 already contains a covariance named `C^(k)(A)`

The visually confirmed CMP99 Theorem 3.15 window states that under its regular-background smallness assumptions the covariance propagator `C^(k)(A)` is given by Eq. (3.185) and satisfies an exponential decay estimate in Eq. (3.187).

This gives a strong chronological and notational candidate for the covariance used downstream. However, R42 does not promote the cross-paper identity

`CMP99 C^(k)(A) = CMP116 C^(k)`

to a theorem until the explicit Part-I/Part-II back-reference or normalization statement is extracted.

### [7], [21] Part II continues the Part-I fluctuation integral

CMP116 states at paper level that the fluctuation-field integral constructed in Part I is represented by the exponentiated cluster expansion. Therefore the downstream `C^(k)` root belongs to the one-step fluctuation architecture inherited from CMP109, rather than being a new covariance invented by the cluster-expansion paper.

## Core determination: covariance-first, not precision-first

R36--R41 organized the analytic route around a provisional record

`NativeLocalPrecisionCertificate`

and attempted to derive

`precision -> resolvent -> covariance root -> localized root`.

R42 shows that this is a sufficient reconstruction route but not the source-native dependency direction used by CMP116.

The native direction is instead

`one-step fluctuation covariance C^(k)`
` -> source-used root (C^(k))^(1/2)`
` -> source localization/random-walk expansion`
` -> localized activity H(Z)`.

Therefore, for the RP-blocker splice, the correct source-facing object is better typed as

### `NativeFluctuationCovarianceCertificate`

whose source-facing content is:

- the exact one-step fluctuation covariance object `C^(k)` on its native fluctuation coordinates/domain;
- the source-used positive/specified square root `(C^(k))^(1/2)`;
- the exact product-Gaussian coordinate change including normalization/Jacobian;
- the source regularity/localization hypotheses under which the root is expanded and localized;
- the domain/support dictionary into the project fluctuation-support representation.

The exact Wilson-Hessian identity can be retained separately as provenance/structural mathematics, but it is not required merely to consume the native CMP116 covariance root.

## Consequence for the unresolved `Delta_1/Delta_a/P_j` seam

The R41 source-dictionary problem remains mathematically legitimate:

`CMP102 Delta_1 <-> CMP99 Delta_a/G(U) <-> project precision P_j`.

But R42 demotes it from **RP-blocker-critical theorem debt** to a separate precision/Hessian identification problem.

For the branch that needs the CMP116 Gaussian root and its localization, one may define the project covariance by transport of the source covariance itself:

`C_project,j := T_j C^(k) T_j^*`

on the correctly typed fluctuation space, and transport the source root accordingly once the finite-dimensional coordinate normalization is fixed.

No independent proof of

`P_j = (C_project,j)^(-1)`

is needed to state or use the source covariance-root localization theorem. That inverse identity matters only if one wants the separate precision formulation or a rederivation of the source bounds.

## Consequence for the `O(g_j)` precision defect

The previously targeted estimate

`P_j(exp(g_j A)) - P_0,j = O(g_j)`

is one clean sufficient route to rederive coercivity, weighted resolvent decay and root decay from a flat reference operator.

CMP116, however, already enters the cluster expansion with `(C^(k))^(1/2)` and then localizes that root directly. Hence the small-background precision defect is not an independent native source hypothesis needed by the blocker if the CMP116 covariance/root dictionary is used directly.

It remains useful for:

- independent formal reconstruction of the propagator package;
- comparison with the flat/reference operator;
- proving source bounds from a more abstract local-SPD shell;
- identifying the physical Hessian precisely.

But it should no longer be counted as unavoidable theorem debt for the R25--R32 RP splice.

## Negative results / guardrails

- Do not identify `Delta_k`, `Delta_1`, `Delta_a`, and `(C^(k))^(-1)` merely from suggestive notation.
- Do not require the CMP102 Hessian definition lock before using the source-native CMP116 covariance root.
- Do not claim the exact CMP99-to-CMP116 `C^(k)` normalization/back-reference until the Part-I/Part-II dictionary is extracted.
- Do not replace the CMP116 root localization by a finite-range equality; the source uses resolvent/series and generalized random-walk localization.
- Do not discard the Jacobian/determinant and coordinate normalization in `B'=(C^(k))^(1/2)X`.

## Revised dependency picture

The R36 source-facing packet can now be sharpened from

`A. CanonicalUjcEmbedding`
`B. NativeLocalPrecisionCertificate`
`C. CMP116SupportDictionary`

to

`A. CanonicalUjcEmbedding`
`B'. NativeFluctuationCovarianceCertificate`
`C. CMP116SupportDictionary`,

with the former full precision/Hessian dictionary moved to a noncritical structural side record.

For the RP blocker the critical chain is now

`CanonicalUjcEmbedding`
` + native C^(k)/(C^(k))^(1/2) Gaussian dictionary`
` + CMP116 support/localization dictionary`
` -> YM-R29 soft localized activity`
` -> YM-R28 reserve absorption`.

This removes the requirement to close `Delta_1/Delta_a/P_j` before the blocker can be source-spliced.

## Bounded determination

R42 does **not** prove the one-step covariance dictionary completely. It proves a dependency minimization:

`exact Hessian/precision identity` is not upstream of the source-native CMP116 root localization.

The remaining covariance-critical obligations are finite and concrete:

1. exact CMP109/CMP116 coordinate/normalization dictionary for `B'`, `C^(k)`, `(C^(k))^(1/2)` and `X`;
2. determinant/Jacobian normalization of the product-Gaussian pushforward;
3. exact source-domain/support typing for the localized root/activity;
4. optionally, the explicit CMP99/CMP109 back-reference identifying the earlier `C^(k)(A)` normalization with the one-step covariance.

The old direct Hessian-definition gate remains useful but is no longer on the RP blocker critical path.

## Next frontier — YM-R43

**CMP116 covariance-coordinate / Jacobian closure audit.**

Inspect the already-custodied equations (2.5)--(2.7) and the Part-I handoff only for the finite-dimensional Gaussian dictionary:

- what space `B'` occupies;
- what covariance restriction `C^(k)(Z0)` is being conditioned/integrated;
- whether the determinant normalization is already absorbed into the displayed measure/factor;
- how `(C^(k))^(1/2)` maps into the product coordinates `X`;
- whether this directly closes `NativeFluctuationCovarianceCertificate` without the precision/Hessian side record.

YM-R43 is unconsumed here.

## References

Reused: [7] CMP109; [21] CMP116; [41] CMP102; [79] CMP99. No new cumulative source is consumed. Highest source ID remains **[79]**; next new source is **[80]**.
