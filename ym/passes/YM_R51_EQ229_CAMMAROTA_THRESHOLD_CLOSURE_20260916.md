# YM-R51 — CMP116 Eq. (2.29) D-family summability / Cammarota threshold closure

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R50_20260916.json`
Next cursor: YM-R52 (unconsumed)

## Question

Close the native CMP116 Eq. (2.29) D-stage summability gate

`sum_D prod_{Y in D} alpha6 exp(-delta*kappa*d_k(Y)) <= 1`

by extracting the actual Cammarota result cited through CMP109 reference [26], identifying the relevant theorem, and determining whether the source's qualitative “large K / small alpha6” threshold is scale/volume uniform.

## 1. Source correction: the relevant Cammarota result is Theorem 2

Primary source [80] was inspected directly from the author-uploaded full text. The relevant general polymer result is Cammarota **Theorem 2**, not Theorem 1.

Theorem 1 concerns high-temperature two-point correlation decay for an unbounded spin system. Theorem 2 is the general polymer Mayer-series convergence theorem used later in the paper and is the structurally relevant result for Bałaban’s Eq. (2.29)-type product/cluster summability.

Cammarota defines finite polymers and their activities, writes the hard-core polymer partition function as a sum over disjoint polymer families, and gives a Mayer expansion in terms of connected-graph coefficients. Theorem 2 assumes a rooted activity smallness condition organized by polymer cardinality, then proves the corresponding absolute Mayer convergence/exponentiation statement.

The proof rewrites connected-graph sums as tree sums, sums recursively from leaves, and exposes the scalar convergence condition

`epsilon/(1-epsilon) < 1/(e-1)`.

Equivalently, one may choose any

`0 < epsilon < 1/e`.

This is the precise small scalar reserve needed in the Cammarota tree argument. [80]

## 2. CMP116 weights satisfy the Cammarota cardinality hypothesis at large decay

CMP116 already supplies the localization-domain metric comparison

`c_M |Y| <= d_k(Y) <= M^-4 |Y| - 1`,

with

`c_M = (3*2^3)^-1 M^-4 = 1/(24 M^4)`.

The D-stage activity is

`w(Y) = alpha6 exp(-delta*kappa*d_k(Y))`.

Hence

`w(Y) <= alpha6 exp(-lambda |Y|)`,

where

`lambda = delta*kappa/(24 M^4)`.

Localization domains are connected unions of fixed-size cubes in a four-dimensional bounded-degree adjacency graph. Therefore there is a geometry constant `C_ent < infinity`, depending only on the fixed localization convention/block geometry, such that the number of connected localization domains of cardinality n containing a specified root cube is bounded by

`N_n <= C_ent^(n-1)`.

This bound is independent of volume, UV step, background field, and the particular root cube.

Consequently

`sup_x sum_{Y contains x, |Y|=n} w(Y)`

is bounded by

`alpha6 C_ent^(n-1) exp(-lambda n)`.

Choose `epsilon` with `0 < epsilon < 1/e`. A sufficient source-independent threshold is obtained by first choosing the decay parameter so that

`C_ent exp(-lambda) <= epsilon/2`,

and then choosing `alpha6` small enough that the remaining prefactor fits the same `epsilon^n` cardinality budget. For example, any fixed choice satisfying

`alpha6 exp(-lambda) <= epsilon/2`

and the preceding entropy inequality gives a strictly stronger rooted cardinality majorant than required by the Cammarota leaf-summing argument.

Thus the threshold dependence is only on

- the fixed four-dimensional localization entropy constant `C_ent`;
- the fixed block parameter `M` through `c_M`;
- `delta*kappa` through `lambda`;
- and the scalar activity amplitude `alpha6`.

It is independent of total lattice volume and RG depth.

## 3. Why the D-family adaptation is finite and source-shaped

CMP116 fixes a connected component `Y0` and sums over finite families `D` of localization domains `Y` whose union is `Y0`. Equation (2.27) uses exactly this connectivity/coverage structure:

`sum_{Y in D} (d_k(Y)+5) >= d_k(Y0)+5`.

This is the same hard-core/overlap geometry needed by the Cammarota tree argument: polymers are localization domains, incompatibility is overlap/contact in the source localization graph, and the polymer activity is `w(Y)` above.

The exact repository `DIndex/DParts` flattening remains optional formalization dictionary work, but no additional mathematical theorem is needed to identify the source combinatorics. The adaptation preserves the two properties used by Cammarota's proof:

1. bounded local polymer entropy at fixed cardinality;
2. tree-connected incompatibility/overlap structure.

Because CMP116 itself says Eq. (2.29)-type inequalities follow by a simple modification of [26], this derivation is source-shaped rather than an unrelated replacement theorem.

## 4. Direct threshold form

A useful explicit sufficient condition can be recorded as follows. Let

`q := C_ent exp(-delta*kappa/(24 M^4))`.

Choose `epsilon < 1/e` and require

`q <= epsilon/2`,

plus `alpha6` small enough that the rooted one-polymer/cardinality prefactor is at most the remaining `epsilon/2` reserve. Then the Cammarota leaf-stripping/tree sum is absolutely convergent with uniform constants, and the restricted CMP116 D-family sum is bounded by a finite function tending to zero with `alpha6`.

Shrinking `alpha6` once more makes that bound at most one, yielding CMP116 Eq. (2.29).

The important point is existential and uniform:

`exists kappa_* < infinity, alpha6_* > 0`

such that for all `kappa >= kappa_*` and `0 < alpha6 <= alpha6_*`, Eq. (2.29) holds uniformly over volume and RG scale.

No numerical optimization of `kappa_*` or `alpha6_*` is needed anywhere downstream.

## 5. Status

The former open object

`CMP116Eq229Summability`

is now closed at mathematical/source level.

What remains project-specific is only the formal encoding of Balaban's source D-family as repository `DIndex/DParts`. That is not a live analytic theorem gate for the research traversal.

## Negative results / guardrails

- Do not cite Cammarota Theorem 1 as the theorem behind Eq. (2.29); the relevant polymer Mayer result is Theorem 2.
- Do not import the spin-system potential hypotheses of Cammarota Theorem 1 into CMP116; they are unnecessary for the D-stage adaptation.
- Do not claim an optimized explicit numerical value of the large-decay/small-alpha6 threshold; only uniform existence is established/needed.
- Do not treat the source-to-Lean `DIndex/DParts` encoding as a new mathematical source theorem.
- Do not infer the later P/Z0/Z0' resummation bounds from Eq. (2.29); those remain separate frontiers.

## Determination

`CMP116 Eq. (2.29): CLOSED` at native mathematical/source level.

The source route is now

`CMP116 metric lower bound + finite-degree localization entropy`
`-> Cammarota/Theorem-2 cardinality regime`
`-> tree/leaf summation`
`-> uniform D-family product bound`
`-> shrink alpha6 -> Eq. (2.29) <= 1`.

## Next frontier — YM-R52

**CMP116 Eq. (2.31) P-family carrier/count and entropy audit.**

Audit the exact P-bond family, the source carrier for P inside `Z0 \ Y0`, the positive-orientation/base-endpoint issue, the cardinality factor, and the rate

`rho = gamma2 epsilon1^2/(20 g_k^2)`

used to obtain the P-stage entropy bound.

## References

Reused: [21] CMP116; [7] CMP109.

Newly consumed: [80] C. Cammarota, *Decay of Correlations for Infinite Range Interactions in Unbounded Spin Systems*, Commun. Math. Phys. 85 (1982), 517–528, DOI 10.1007/BF01403502.

Highest cumulative source ID is now **[80]**; next new source is **[81]**.
