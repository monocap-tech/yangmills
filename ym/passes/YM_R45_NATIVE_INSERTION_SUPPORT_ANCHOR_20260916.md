# YM-R45 — native insertion support-anchor / localization-domain audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R44_20260916.json`
Next cursor: YM-R46 (unconsumed)

## Question

R44 reduced the reflection-positive blocker to an activity-level insertion problem inside CMP116's native localization machinery.  The remaining blocker-specific object was provisionally named `NativeInsertionSupportAnchor`: identify the fixed local support of the soft factor in Balaban's `Y0/Z0` localization language and determine whether a new finite enlargement theorem is required.

## Source-facing geometry

The registered CMP116 page-12 extraction states that for fixed `Y0` the paper decomposes the cutoff over bond sets `P`, then takes `Z0` to be the smallest localization domain containing `Y0` and `P`; bonds in `P` lie in the interior of `Z0` and do not intersect `dZ0`.  The separate CMP116 support extraction records that a source term indexed by a connected component `Y0` is built from propagators and fields restricted to `Y0` and depends only on the localized set together with its base cube. [21]

This is exactly the kind of source geometry needed by the blocker.  It does not require the blocker support to coincide literally with a pre-existing `Y0`; it requires a uniformly finite source-owned cover that can be adjoined before the minimal localization domain is taken.

## Blocker support is design data

The soft kernel from R18 is built coarse-link by coarse-link from a finite family of fine paths.  R26 then shows that the local logarithmic correction `v_e` is an analytic function of only the bonds occurring in those finitely many paths, with path length/block geometry fixed once the RG scheme is chosen.

Therefore we may and should impose as part of the blocker design that each positive/negative/reflection-boundary coarse-link path family is contained in a fixed finite neighborhood of an anchor coarse block/cube.  Let `S_e` be the fine-bond support and let `SHat_e` be its cover by CMP116 localization cubes.  There is a scale-independent integer `q_soft` such that

`|S_hat_e| <= q_soft`

and a scale-independent localization diameter bound in native block units.  This is not a new source theorem: it is a finite combinatorial property of the chosen blocking paths.

## Native anchoring

For one inserted local factor `v_e`, replace the initial native component by the connected source localization hull

`Y0_soft = ConnHull(Y0 union S_hat_e)`

(or `ConnHull(S_hat_e)` for an insertion-only seed), and define `Z0_soft` by the same native CMP116 rule: the smallest localization domain containing `Y0_soft` and the selected `P` bonds.

No modification of the generalized random-walk/root localization construction is required.  The insertion only changes the seed set by a uniformly bounded number of localization cubes.

If the source convention already includes the anchor/base cube in the initial localized term, choose the blocker anchor to be that base cube and absorb `S_hat_e` into its fixed neighborhood.  The exact project `activeSupport`/`fluctuationSupport` translation remains the already-open CMP116 support dictionary; the blocker does not create a second dictionary.

## Fixed enlargement costs only a constant

Adjoining at most `q_soft` cubes to the initial seed changes native tree/localization distance by at most a fixed additive constant `C_softGeom` depending only on the blocker path geometry and fixed RG block parameters.  Hence a native bound

`exp(-mu d_k(Z))`

becomes at worst

`exp(mu C_softGeom) exp(-mu d_k(Z))`.

The exponential rate is unchanged; only the amplitude constant is renormalized.  If one prefers to avoid a sharp additive-distance statement, the same conclusion follows by spending an arbitrarily small fixed amount of the available decay exponent on the bounded enlargement.

## Hidden multiplicity check

The blocker exists at every coarse link, so an activity `H_soft(Z)` can receive contributions from multiple anchor links.  This does not produce a volume factor in the final uniform amplitude.  CMP116's native localization geometry includes a volume/tree-distance comparison (the extracted Eq. (2.30) window controls localization-domain volume by `d_k`).  Thus the number of possible anchors in a fixed localized polymer is at most linear in its native volume and hence polynomial/linear in the tree metric. [21]

Consequently, for any `mu' < mu`,

`(# anchors in Z) exp(-mu d_k(Z)) <= C(mu-mu') exp(-mu' d_k(Z))`.

So summing the local insertion over all blocker anchors spends only a finite decay margin and does not create a volume-dependent constant.

## Interpolation uniformity

For

`G_t = G_native exp(t V_soft)`, `0 <= t <= 1`,

R26 supplies `V_soft = O(g_k)` with the required fixed-order analytic derivative bounds on the canonical tube.  Therefore `exp(t V_soft)` and its required derivatives are uniformly bounded by `exp(C g_k)` times fixed analytic constants.  Once the independent `CanonicalUjcEmbedding` domain obligation is supplied, the same CMP116 analytic/localization estimates apply uniformly in `t` after a finite adjustment of constants.

Thus the R44 differentiation argument produces

`|H_soft(Z)| <= C_soft g_k exp(-mu' d_k(Z))`

with scale/volume-independent `C_soft`.

## Determination

`NativeInsertionSupportAnchor` is not an independent source theorem.

It decomposes into:

1. **blocker design fact** — each local soft factor uses a fixed finite reflection-compatible path family, hence has a uniformly bounded localization-cube cover;
2. **native CMP116 rule** — `Z0` is the smallest localization domain containing the active `Y0` seed and `P` bonds; and
3. **existing support dictionary** — translate CMP116 localization cubes/base-cube conventions to project support types when full formal reconstruction is desired.

The blocker adds no new support/localization hypothesis.  Its bounded seed enlargement only renormalizes constants and, after summing anchors, spends a finite amount of exponential decay reserve.

## Negative results / guardrails

- Do not require `S_e` to equal an existing source `Y0`; use a bounded connected source hull and the native minimal-`Z0` rule.
- Do not introduce a new project support notion solely for the blocker; reuse the existing CMP116 support dictionary.
- Do not ignore anchor multiplicity when the blocker is inserted at every coarse link; absorb it using native volume/tree-distance control with a finite exponent loss.
- Do not claim the exact project `activeSupport`/`fluctuationSupport` dictionary is closed; it remains a native formalization side record.
- Uniformity of the interpolation still depends on the separate `CanonicalUjcEmbedding` source-domain obligation.

## Critical-path consequence

The RP-blocker chain is now

`block-local analytic O(g_k) insertion`
`-> native CMP116 product-Gaussian chart`
`-> bounded native seed enlargement`
`-> native H_t(Z) localization`
`-> O(g_k) exp(-mu' d_k(Z)) activity difference`
`-> R28 Lemma-3 reserve absorption`.

No blocker-specific Hessian, covariance-root reconstruction, Gaussian pushforward, Jacobian, or support theorem remains.

## Next frontier — YM-R46

**Native-localization uniformity / critical-path consolidation audit.**

Consolidate R36-R45 and ask what genuinely independent source-facing obligations remain on the RP branch after all dependency minimizations.  In particular separate:

- `CanonicalUjcEmbedding` (Paper-I analytic domain);
- native CMP116 activity/localization estimates already required by the original Bałaban step;
- the source/project support dictionary needed only for formal transport;
- side-record Hessian/covariance/Gaussian dictionaries that are no longer blocker gates.

Determine whether the RP modification can now be declared *strictly hypothesis-neutral* relative to the native CMP116 one-step closure, modulo only the already-open Paper-I domain fact.

References reused: [7] CMP109/Paper I and [21] CMP116. No new source ID consumed; highest remains [79], next new source [80].
