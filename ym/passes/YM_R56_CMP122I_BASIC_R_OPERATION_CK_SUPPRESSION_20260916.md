# YM-R56 — CMP122-I basic R-operation / intermediate C_k^(n) suppression

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R55_20260916.json`
Next cursor: YM-R57 (unconsumed)

## Question

R55 identified the first genuinely new post-small-field burden as the large-field R-operation return map. R56 asks what CMP122-I actually constructs before CMP122-II: what the intermediate `C_k^(n)` objects are, what Eq. (1.70) proves, how much of the fresh CMP119 decay reserve is spent, and where Part I stops.

## 1. Source role of CMP122-I

CMP122-I is explicitly the **basic step** of the R operation. Its abstract states that it constructs the renormalization operation attached to the large-field regions and that the proof is completed in Part II. [22]

Therefore Part I should not be typed as the final post-R return theorem. Its output is intermediate large-field structure prepared for the localization/exponentiation stage of CMP122-II.

## 2. Minimal source-native typing of C_k^(n)

The primary extraction around Eq. (1.70) states that `C_k^(n)(X,U_k^(n))` is a term in the representation (1.63), with an analytic extension on the source's stated enlarged `U-bar` space. The exact internal symbol dictionary for representation (1.63) is not needed to overtype the object: `n` is the source index on the intermediate R-operation family and must not be silently identified with RG scale, connected-component count, or perturbative order unless a later source extraction proves that identification. [22]

For `X in D_m`, Eq. (1.70) gives

`|C_k^(n)(X,(U,J))| <= C_0 exp(-(1+3 beta) kappa d_m(X))`.

Thus each intermediate term is already polymer-local in the source metric `d_m(X)` and retains strictly stronger-than-canonical exponential decay. [22]

## 3. Decay-reserve bookkeeping

R55 recovered the CMP119 pre-R statement that newly created `E^(k), R^(k), B^(k)` expressions are placed on slightly enlarged analytic spaces with improved decay, schematically

`kappa -> (1+4 beta) kappa`,

for use in the R operation. [59]

CMP122-I Eq. (1.70) outputs

`(1+3 beta) kappa`.

Therefore, at source-architecture level, the basic Part-I R step spends at most one unit of reserve:

`(1+4 beta) kappa -> (1+3 beta) kappa`.

This is a bookkeeping derivation from the two source-attested rates. It should not be read as a claim that every internal substep of CMP122-I individually loses exactly `beta*kappa`; the exact internal loss decomposition remains unnecessary unless later constant optimization requires it.

The structural fact is stronger and sufficient: **Part I preserves a positive `3 beta kappa` excess over the canonical decay rate.**

## 4. Eq. (1.70) is not yet the final R' bound

CMP122-II later proves a pre-split localized bound of the form

`|R'^(k)(X,(U,J))| <= O(1)c_1 exp(-(1+beta/2) kappa d_{k, union Y_i}(X))`

and, for the second group after the split,

`|R'^(k)(X,(U,J))| <= exp(-p_0(g_k)) exp(-kappa d_k(X))`.

Those are different objects, metrics, and stages from the Part-I `C_k^(n)` family. [31]

Hence the correct chain is

`fresh CMP119 E/R/B reserve`
`-> CMP122-I intermediate C_k^(n)`
`-> CMP122-II localization/exponentiation into R'^(k)`
`-> post-R split`
`-> return to CMP119 E/R/B class`.

Do not identify `C_k^(n)` with `R'^(k)` or with the final `B'^(k)` boundary family.

## 5. What Part I has accomplished mathematically

At the level needed by the traversal, Part I establishes the nontrivial bridge that the large-field operation does not immediately destroy polymer locality or decay. The intermediate family remains analytic on the required enlarged domain and satisfies

`C_0 exp(-(1+3 beta) kappa d_m(X))`.

This is precisely the reserve needed for Part II to perform localization, placement summation, and exponentiation while still having room to return to the canonical `exp(-kappa d_k(X))` class.

Thus the basic-R obstruction is no longer 'does the first large-field transformation preserve any local decay?' The source answer is yes.

## 6. Surviving mathematical seam

The unresolved theorem-bearing stage is now entirely in CMP122-II:

1. localize/exponentiate the Part-I output;
2. control placement entropy and the source metric `d_{k, union Y_i}`;
3. prove the `(1+beta/2)kappa` pre-split bound;
4. separate first-group boundary terms from second-group R terms;
5. recover the sharp second-group factor `exp(-p_0(g_k)) exp(-kappa d_k(X))`;
6. return the resulting action to the CMP119 Sect. 2 E/R/B form.

CMP122-II Theorem 1 states the final return at theorem level, conditional on the effective couplings remaining in a sufficiently small interval. [31]

## Determination

R56 closes the **CMP122-I basic-R reserve-preservation gate**:

`CMP119 fresh reserve (1+4 beta)kappa`
`-> CMP122-I C_k^(n)`
`-> retained reserve (1+3 beta)kappa`.

The `C_k^(n)` internal representation dictionary remains source/formalization custody work, but no longer blocks the mathematical critical path because Eq. (1.70) supplies the property Part II consumes: analytic polymer-local exponential suppression with positive excess decay reserve.

## Negative results / guardrails

- Do not identify the index `n` with RG scale, component number, or perturbative degree without source text.
- Do not identify `C_k^(n)` with the final `R'^(k)` activity.
- Do not relabel Eq. (1.70) as a global scalar remainder or mass-gap estimate.
- Do not claim the full R operation is closed from CMP122-I alone; the paper itself defers completion to Part II.
- Do not infer continuum Yang-Mills existence or a continuum mass gap from this lattice large-field bound.

## Next frontier — YM-R57

**CMP122-II localization/exponentiation / R-prime pre-split audit.**

Start with Eqs. (1.98)-(1.100): recover the exponentiated `R'^(k)` construction, the metric `d_{k, union Y_i}`, the `(1+beta/2)kappa` pre-split decay, and the mechanism that separates the second-group `exp(-p_0(g_k)) exp(-kappa d_k(X))` terms from the first-group boundary terms before Eq. (1.101).

## References

Reused: [22] Balaban CMP122-I; [31] Balaban CMP122-II; [59] Balaban CMP119. No new cumulative reference consumed. Highest remains [80]; [81] remains next.
