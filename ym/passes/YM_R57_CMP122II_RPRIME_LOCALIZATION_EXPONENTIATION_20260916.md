# YM-R57 — CMP122-II R-prime localization / exponentiation / pre-split audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R58` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R56, which identified the CMP122-I intermediate family `C_k^(n)` and the source-attested bound

`|C_k^(n)(X,(U,J))| <= C_0 exp(-(1+3 beta) kappa d_m(X))`.

Audit CMP122-II Eqs. (1.98)–(1.100):

1. identify the exponentiated `R'^(k)` object;
2. record the pre-split metric and decay rate;
3. determine the first-group / second-group role;
4. locate the source of the `exp(-p_0(g_k))` factor without conflating it with ordinary polymer-distance decay;
5. determine exactly what remains for the post-R action handoff.

Repeated sources: [31] Balaban, *Large field renormalization II*; [22] Part I; [59] CMP119.
No new bibliography item is consumed.

## 1. Exponentiation is a genuine localization step

CMP122-II printed page 390 / Eq. (1.98) writes the result of the preceding localization and cluster expansion in exponentiated form

`exp R'^(k) = exp(sum_X R'^(k)(X))`

(up to the source's surrounding prefactor/brace notation).

Thus `R'^(k)(X)` is the localized activity after the Part-II cluster/exponentiation procedure. It is not the same object as the Part-I intermediate `C_k^(n)`, and it is not yet the final post-R `R_k` family before the first/second-group repartition.

Typed chain:

`CMP119 fresh E/R/B -> CMP122-I C_k^(n) -> CMP122-II localized R'^(k)(X) -> group split -> post-R B' + R`.

## 2. Pre-split source bound

Eq. (1.99) gives the analytic local estimate

`|R'^(k)(X,(U,J))| <= O(1) c_1 exp(-(1 + beta/2) kappa d_{k, union Y_i}(X))`.

Here the source metric is not the canonical `d_k(X)`. It is the modified distance `d_{k, union Y_i}(X)` relative to the marked/localization domains entering the large-field construction.

Therefore the pre-split bound must not be simplified to an ordinary `d_k` polymer bound.

## 3. Decay-reserve accounting

R56 recorded the Part-I output reserve

`(1+3 beta) kappa`.

The Part-II pre-split localized activity has

`(1+beta/2) kappa`.

Thus the source-attested net reserve erosion between these displayed stages is

`(1+3 beta)kappa -> (1+beta/2)kappa`,

i.e. a net expenditure of `(5/2) beta kappa` before the group split.

This is a stage-to-stage budget statement only. The present extraction does not justify assigning the entire `(5/2) beta kappa` loss to any single operation such as placement entropy, metric conversion, localization, or Ursell exponentiation. Those mechanisms occur inside the Part-II construction, but their individual numerical shares are not separately source-extracted here.

The correct determination is therefore:

- source fact: the displayed input/output decay rates;
- derivation: positive reserve `(beta/2) kappa` still survives above the canonical `kappa` rate;
- open fine-grained dictionary: exact internal allocation of the reserve losses.

## 4. The group split is the decisive large-field classification

The source then separates the localized `R'^(k)` terms into two groups.

The repository's primary-source audit records the source-side role conservatively:

- the first group is the family that is converted into new boundary terms `B'^(k)` in the post-R action;
- the second group consists of localization domains disjoint from the indicated large-field region and becomes the final localized R-sector.

The exact set-theoretic dictionary is left to Eq. (1.101) and is therefore not promoted beyond this source-attested role in R57.

## 5. Origin of `exp(-p_0(g_k))`

For the second group, Eq. (1.100) specializes the pre-split amplitude `c_1` to the large-field small factor

`c_1 = exp(-p_0(g_k))`

and simultaneously replaces the modified pre-split metric by the canonical polymer metric `d_k(X)`. The resulting source bound is

`|R'^(k)(X,(U,J))| <= exp(-p_0(g_k)) exp(-kappa d_k(X))`.

This answers the structural origin question:

`exp(-p_0(g_k))` is not manufactured by the distance estimate `exp(-kappa d_k(X))`.

It is an independent large-field suppression amplitude which becomes available precisely for the second group after imposing disjointness from the indicated large-field region. The metric decay and the large-field amplitude are two different resources:

`large-field rarity/small factor  x  polymer locality`.

The current primary-source packet does not contain a sufficiently explicit source extraction of the full definition/profile of `p_0(g)` to justify a stronger asymptotic label such as "faster than every power of g". R57 therefore does not call the factor nonperturbative in a quantitative asymptotic sense. The exact `p_0` profile remains source-extraction/custody debt unless later flow/summability arguments require it.

## 6. Canonical R-sector return

The second-group bound is already in the correct CMP119-style local shape:

`amplitude(g_k) * exp(-kappa d_k(X))`,

with amplitude `exp(-p_0(g_k))`.

Compare CMP119's ordinary R-sector condition

`|R^(j)(X,(U,J))| <= g_j^kappa_0 exp(-kappa d_j(X))`.

The exact amplitude conventions differ, but the geometric locality class is restored: canonical metric, exponential polymer decay, and a small coupling-dependent prefactor.

Thus the large-field localization/exponentiation stage succeeds at the geometric level.

## 7. Placement entropy: what is and is not closed

The existence of the exponentiated representation (1.98) and the stronger-than-canonical pre-split exponent in (1.99) certify that the localization/cluster-placement entropy has already been absorbed within the source's constant and decay reserve before Eq. (1.99).

However, because the present primary extraction does not expose a term-by-term entropy ledger, R57 does not reconstruct an independent placement-count theorem or claim an exact entropy constant. No such theorem is needed on the mathematical critical path if Eq. (1.99) is consumed directly as the native output of the Part-II localization/exponentiation theorem.

So:

`placement entropy = source-internal cost already reflected in (1.99), not a new downstream theorem obligation`.

## 8. Source-level determination

R57 closes the following source/mathematical facts:

1. `R'^(k)` is the localized exponentiated Part-II activity family, distinct from `C_k^(n)`.
2. Eq. (1.99) gives analytic pre-split decay with modified metric and rate `(1+beta/2)kappa`.
3. The displayed Part-I to Part-II reserve erosion leaves a positive `beta/2` excess above the canonical decay rate.
4. The first/second-group separation is mathematically substantive, not bookkeeping.
5. For the second group, Eq. (1.100) restores the canonical metric `d_k(X)` and supplies the independent amplitude `exp(-p_0(g_k))`.
6. The large-field small factor and polymer-distance decay are distinct resources.
7. Placement/localization entropy is already absorbed in the native Eq. (1.99) theorem output; exact internal allocation of the reserve loss remains optional source reconstruction.

Hence:

`CMP122-II R-prime localization/exponentiation = CLOSED at source/mathematical level through Eq. (1.100).`

What remains is not another localization estimate, but the post-R repartition itself.

## Negative results / guardrails

- Do not identify `C_k^(n)` with `R'^(k)`.
- Do not replace `d_{k, union Y_i}(X)` by `d_k(X)` before the source's second-group specialization.
- Do not collapse the first-group boundary family and second-group R family into one remainder.
- Do not attribute the entire `(5/2) beta kappa` reserve loss to placement entropy without source extraction.
- Do not call `exp(-p_0(g_k))` quantitatively nonperturbative without an extracted definition/asymptotic theorem for `p_0`.
- Do not replace the polymer-local source bound by a bare scalar `M r^k` recurrence.
- Do not infer continuum existence or mass gap from the post-R lattice activity bound.

## Next frontier — YM-R58

`YM-R58 — CMP122-II Eq. (1.101)-(1.102) post-R E/R/B return-map audit.`

Tasks:

1. recover the exact first-group -> `B'^(k)` and second-group -> `R` split in Eq. (1.101);
2. determine how `A_k`, `A'_k`, `R'^(k)` and `B'^(k)` reassemble the post-R action;
3. check normalization/partition-function preservation around (1.102);
4. then compare the returned action/density directly with CMP119 Sect. 2 and CMP122-II Theorem 1;
5. decide whether any mathematical gate remains in the complete-density return map before moving to the coupling-window / UV-stability theorem.

Highest cumulative reference remains [80]; [81] remains next.