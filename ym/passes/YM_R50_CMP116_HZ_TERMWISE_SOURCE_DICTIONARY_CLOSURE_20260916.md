# YM-R50 — CMP116 H(Z) termwise/source dictionary closure

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R49_20260916.json`
Next cursor: YM-R51 (unconsumed)

## Question

R49 exhausted the native analytic-domain branch. R50 returns to CMP116 Part II and asks whether the mathematical source object underlying `H(Z,Z0)` / `H(Z)` can be typed exactly enough to remove the broad “activity identification / termwise dictionary” source obligation before auditing the later D/P/Z0/Z0' summability residues.

## 1. Exact native index stack

CMP116 Sect. 2 starts with the Mayer expansion (2.1). A source subfamily `D subset D_k` of localization domains `Y` determines

`Y0 = union_{Y in D} Y`  (2.2).

For fixed `Y0`, Balaban defines the auxiliary bond set `Y0^{c,*}` and decomposes the cutoff `chi_k` into a sum over bond subsets `P subset Y0^{c,*}` in (2.3). For each such `P`, `Z0 in D_k` is the smallest localization domain containing both `Y0` and the bonds of `P`; the source explicitly requires the P-bonds to be interior to `Z0` and disjoint from `dZ0`.

All D/P terms determining the same `Z0` are then resummed into the source underintegral `F(Z0,B)`, giving (2.4)

`(2.1) = sum_{Z0 in D_k} int dmu_{C^(k)}(B) F(Z0,B)`.

The integral is conditioned on `Z0^c`, changed to product-Gaussian coordinates by `B'=(C^(k))^(1/2)X`, and denoted by a source function `G(Z0,X,C^(k)(Z0),(C^(k))^(1/2),Delta_k)`.

## 2. Second localization and H(Z,Z0)

CMP116 then performs a second localization of the still-global propagator/operator dependence. It introduces an enlarged `Z0'` consisting of the smallest family of scale-(k+1) LM-cubes containing `Z0`, introduces weakening parameters `s(Delta)` on cubes outside the interior of this enlarged seed, and uses generalized random-walk expansions plus the resolvent/series expansion of `(C^(k))^(1/2)`.

Applying the source fundamental-theorem/decomposition formula gives (2.8): for fixed `Z0`, the product-Gaussian integral is a sum of terms denoted

`H(Z,Z0)`.

The source sum is over localization domains `Z` such that every connected component of `Z` contains a connected component of the enlarged source seed `Z0'`.

This is the exact source meaning of `H(Z,Z0)`: it is not an arbitrary project summand and not a finite covariance-root piece; it is the fixed-Z0 output of the second weakening/random-walk localization.

## 3. H(Z) is an explicit finite/resummed source sum

Equations (2.4), (2.6), and (2.8) imply (2.9)

`(2.1) = sum_Z H(Z)`,

with

`H(Z) = sum_{Z0 : Z0' subset Z} H(Z,Z0)`

using the source enlargement convention.

Balaban then states that `H(Z)` is localized in the interior of `Z` with respect to the external gauge fields.

Thus the native source activity has the following exact dependency stack:

`D -> Y0 -> P -> Z0 -> conditioned/product-Gaussian integral -> second localization Z -> H(Z,Z0) -> sum over Z0 -> H(Z)`.

There is no additional unnamed source index between `Z0` and `Z` required to define the mathematical activity. The weakening derivatives and generalized-random-walk data are internal construction data of `H(Z,Z0)`, not a new top-level polymer index.

## 4. Connected-component factorization is explicit

CMP116 (2.10) states that if

`Z = Z1 union ... union Zn`

is the decomposition into connected components, then

`H(Z) = H(Z1) ... H(Zn)`.

The subsequent hard-core polymer expansion (2.11) therefore sums products of connected activities, with source incompatibility function `zeta(Z,Z')` equal to zero when two polymers overlap in a cube or a cube wall and one otherwise.

The exponentiated cluster expansion (2.12)-(2.13) is downstream of this source factorization. Hence component factorization is not an open mathematical source theorem; only any project-specific finite-product/flat-sum representation of it remains a dictionary issue.

## 5. Exact termwise object and majorant

After establishing analyticity, CMP116 says explicitly that to bound `H(Z)` one considers a single term in the sums over `D,P`; this is equation (2.14). Besides the fixed source data `D,P,Z0,Z`, it contains the weakening contours/parameters `sigma(Z), tau`, the product-Gaussian X integral, the conditioned B integral, the cutoff factors, and the product/exponential of native potentials `V_k(Y,B)`.

After the perturbative field estimates (2.15)-(2.25), CMP116 gathers them into the single-term majorant (2.26):

`|(2.14)| <=`

` exp(-(kappa1-1)(LM)^(-4) |Z \ Z0'|)`

` * [ product_{Y in D} 2 E0 epsilon1 C1 alpha4^(-1) M^q exp(C2 kappa1) exp(-(1-3 delta) kappa d_k(Y)) ]`

` * exp(-(1/2) gamma2^2 epsilon1^2 g_k^(-2) |P|)`

` * exp(O(1) alpha5 |Z|)`.

The source defines/gathers

`alpha5 = O(1) exp(-c M) + O(alpha0+alpha1) + O(1) alpha4 + gamma2`

before this bound, with the native smallness assumptions stated in the adjacent estimates.

This (2.26) expression is the correct source `termWeight` object. It is not the final Lemma-3 bound; it is the pointwise majorant subsequently resummed in the explicit order D, then Y0/P at fixed Z0, then Z0 at fixed Z0', then Z0', yielding (2.27)-(2.37) and Lemma 3/(2.38).

## 6. Source closure versus project dictionary

R50 therefore closes the mathematical/source activity-identification layer:

- native `H(Z,Z0)` construction: CLOSED;
- native `H(Z)` summation/index stack: CLOSED;
- native connected-component factorization: CLOSED;
- native single-term object (2.14): CLOSED;
- native single-term majorant / termWeight (2.26): CLOSED.

The external formalization audit may still correctly label its source-to-Lean flattening as `dictionary_open`. That is a project-representation issue: mapping the nested source family `(D,P,Z0,Z, weakening data)` to a particular finite Lean index type, summand constructor, and finite-product theorem. It is not evidence that the source mathematical object is unknown.

## 7. Remaining native residues after R50

The critical native residues are now later resummation obligations, not H(Z) identification:

1. Eq. (2.29): D-family summability and the precise large-kappa/small-alpha6 threshold/uniformity argument, including the cited Cammarota-style combinatorics.
2. Eq. (2.31): P-family carrier/count dictionary and the entropy inequality at fixed Z0.
3. Eq. (2.32)-(2.37): geometric passage from component/Y0 bounds through fixed Z0' and the final post-P exponent reserve.
4. Lemma 3/(2.38): endpoint assembly once the preceding three source families are fully typed.

The H(Z) source object itself should no longer be carried as an upstream blocker.

## Negative results / guardrails

- Do not replace `H(Z,Z0)` by a fictitious finite root-piece decomposition.
- Do not treat the later D/P/Z0/Z0' resummation order as part of the definition of H(Z); it is the proof of its bound.
- Do not infer the project's exact finite index type from the source notation; that flattening remains formalization debt if desired.
- Do not infer Lemma 3 directly from component factorization or (2.26); the later summability/entropy/geometric estimates remain live.
- Do not reopen CanonicalUjcEmbedding or the RP-specific covariance/Hessian/Jacobian seams.

## Determination

The broad `H(Z) activity identification / termwise source dictionary` mathematical obligation is exhausted. CMP116 itself gives the complete nested source construction and the exact pre-resummation majorant. The native frontier moves one stage later, to the D-family combinatorial summability in Eq. (2.29).

Canonical transition:

`YM-R50 COMPLETE -> YM-R51`.

## Next frontier — YM-R51

**CMP116 Eq. (2.29) D-family summability / Cammarota threshold audit.**

Recover the exact argument or theorem supporting

`sum_D product_{Y in D} alpha6 exp(-delta kappa d_k(Y)) <= 1`,

including threshold dependencies and uniformity over scale/volume/background. Determine whether the cited modification of [26] is enough as a theorem citation, or whether a short native polymer-count derivation is needed.

## References

Reused: [21] Balaban CMP116. No new cumulative source consumed. Highest source ID remains **[79]**; next new source is **[80]**.
