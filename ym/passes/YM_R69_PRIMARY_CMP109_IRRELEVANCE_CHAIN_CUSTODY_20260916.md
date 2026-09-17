# YM-R69 — primary CMP109 irrelevance-chain extraction / custody audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R70` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R68, which found a secondary traceability locator [85] claiming that Bałaban CMP109 contains a source-scale irrelevance chain

`(3.34) -> (4.14),(4.15) -> (5.37) -> (5.42) -> (0.29)`

and, in particular, an Eq. `(0.29)` bound with a positive source-scale exponent.

R69 asks only the custody question:

> Can that candidate bound and its interpretation be promoted from [85] to the primary Bałaban source [7]?

Repeated sources: [7] Bałaban CMP109; [85] Eriksson traceability locator.
No new bibliography item is consumed. Highest remains [85].

## 1. Primary-paper identity is verified; equation-level chain is not yet extracted

The publisher/repository metadata for [7] verifies the paper and its stated role: four-dimensional pure lattice gauge theory in the small-field approximation, construction of localized effective actions, beta-functions, and recursive coupling-constant renormalization.

The project also has independent source-custody evidence for a local primary CMP109 PDF/text artifact in the auxiliary source archive, including a recorded PDF SHA-256 and a full-text SHA-256. However, the public source-audit catalogue presently contains extracted CMP109 entries for other equations (for example the localization metric and Eq. `(0.25)`), while its CMP109 one-step fluctuation/extraction package is still explicitly marked extraction-pending.

In particular, the public audited catalogue does **not** presently expose source-verified entries for the claimed chain

`(3.34), (4.14), (4.15), (5.37), (5.42), (0.29)`.

The current web-accessible primary landing pages likewise expose metadata/abstract but not the equation pages needed to inspect those formulas directly.

Therefore:

`PrimaryCMP109Identity = VERIFIED`,

but

`PrimaryEq0.29Extraction = NOT YET VERIFIED`,

and

`PrimaryTaylorWardBetaChain = NOT YET VERIFIED`.

This is a source-access/extraction boundary, not a mathematical disproof.

## 2. [85] remains a locator, not theorem custody

Reference [85] v2 explicitly describes its discharge as **traceable and conditional**, including conditionality on faithful transcription of the cited Bałaban/Dimock results.

AIRR separately marks the preserved record as a historical import whose scientific correctness and bibliography were not assessed under its current hostile-audit gate.

So R68's custody rule was correct:

`[85] != substitute for [7]`.

No equation-level statement from [85] is promoted to `SOURCE-ATTESTED` status in R69.

## 3. The locator's candidate bound is nevertheless mathematically well-typed

The candidate statement attributed by [85] to CMP109 Eq. `(0.29)` is schematically

`||V^(j)(X,.)||_j <= C (L^j eta)^(4+alpha) exp(-kappa d_j(X))`,

with

`alpha > 0`.

[85] describes `V^(j)` as the irrelevant small-field contribution after the local Taylor/Ward/beta extraction, together with the large-polymer part in its packaged notation.

R69 does **not** assert that this transcription is correct. It does establish what would follow if the primary equation verifies it.

Set

`a_{j,N} := L^j eta_N`,

with

`eta_N = L^-N`.

Then

`a_{j,N} = L^{-(N-j)}`.

The candidate bound becomes

`||V^(j)(X)|| <= C L^{-(N-j)(4+alpha)} exp(-kappa d_j(X))`.

Thus the factor is indeed geometric in distance from the fixed physical endpoint toward the ultraviolet cutoff.

## 4. Four-dimensional root counting leaves exactly the positive excess exponent

A fixed physical four-volume contains on the order of

`a_{j,N}^-4`

scale-`j` cells/roots.

Assume the standard rooted polymer summability at that scale,

`sup_b sum_{X contains b} exp(-kappa d_j(X)) <= C_kappa`,

with constants uniform in the relevant cutoff family.

Then a fixed-region sum of the candidate activity is bounded by

`C_region * a_{j,N}^-4 * a_{j,N}^(4+alpha)`

`= C_region * a_{j,N}^alpha`.

Hence

`FixedRegionDefect(j,N) <= C * L^{-alpha(N-j)}`.

For every

`alpha > 0`,

this is geometrically summable in ultraviolet depth.

Classification: DERIVATION conditional on the candidate primary bound plus rooted polymer summability.

This is the precise reason R68 only needs a positive irrelevance excess, not the canonical engineering value two.

## 5. Arithmetic correction to [85]'s dyadic remark

[85] states its A2/source candidate with exponent

`4 + alpha`, `alpha > 0`,

but later remarks that in the dyadic case the volume-corrected factor gives a net

`2^-2`

per step.

Those statements do not imply one another in general.

For `L=2`, four-dimensional volume counting gives

`2^{-alpha(N-j)}`,

so the one-step factor is

`2^-alpha`.

A universal `2^-2` factor follows only if

`alpha = 2`

(or if a separate theorem supplies two powers not represented by the displayed `alpha`).

Therefore:

`[85] UniversalDyadic2^-2 = NOT JUSTIFIED by its displayed 4+alpha formula alone`.

This does **not** damage the present Yang–Mills route, because summability requires only

`alpha > 0`.

Canonical guardrail:

`PositiveAlpha != AlphaEqualsTwo`.

## 6. The cross-cutoff comparison uses a particularly favorable index placement

Compare the depth-`N` and depth-`N+1` tuned theories.

After one blocking step of the depth-`N+1` theory, both constructions live at the same first common lattice spacing

`a_common = L^-N`.

The fresh contribution generated by the extra finest layer has ultraviolet distance `N` from the fixed physical endpoint (up to the exact source indexing convention).

If that fresh marginal-subtracted contribution is an instance of the primary Eq. `(0.29)` object with uniform constants, then the fixed-region size of the one-layer regular defect obeys schematically

`epsilon_N^E <= C L^{-alpha N}`,

and therefore

`sum_N epsilon_N^E < infinity`.

Combined with the R66 fixed-observable perturbation lemma, this would give Cauchy convergence of bounded fixed-endpoint observables for the regular-E contribution without requiring a global complete-density contraction theorem.

This is a DERIVATION under a still-open source dictionary.

## 7. The missing dictionary is smaller than the whole Taylor/Ward derivation

For the continuum-cross-cutoff route, the first theorem actually required is not necessarily the entire internal derivation

`(3.34) -> (4.14),(4.15) -> (5.37) -> (5.42) -> (0.29)`.

If Eq. `(0.29)` is a standalone theorem/bound whose hypotheses are satisfied by the canonical generated trajectory, then it is enough to extract:

1. the exact definition of `V^(j)`;
2. the exact power of `L^j eta` and the allowed range of `alpha`;
3. the polymer/locality norm in which the estimate holds;
4. uniformity of its constants in `j`, cutoff depth, volume, and weak coupling;
5. the relation of `V^(j)` to the fresh one-layer marginal-subtracted `E` defect in the depth-`N` versus depth-`N+1` comparison.

The internal Taylor/Ward/beta equations become necessary only insofar as they are required to prove that dictionary or to identify which marginal pieces have already been extracted.

Canonical new object:

`OneLayerDefectToPaperIVjDictionary`.

## 8. [85]'s own continuum-telescoping caution must be preserved

[85] v2 explicitly says that its broader RG-Cauchy interface `(M1)` remains hypothesis-level and labels the continuum-direction summability issue `F-SUM`.

R69 therefore does not promote [85]'s full consumer conclusion.

The present derivation is narrower:

`primary positive-alpha bound on the actual fresh one-layer E defect`

`+ fixed-region root/polymer summability`

`=> summable E-sector endpoint perturbations`.

Whether the `V^(j)` used by Eq. `(0.29)` is exactly that one-layer compatibility defect is precisely the open dictionary above.

Thus there is no contradiction between:

- [85]'s warning that its full M1 consumer has not been audited, and
- the observation that a correctly typed one-layer `a^(4+alpha)` defect would be summable after four-dimensional root counting.

## 9. R69 determination

R69 establishes:

1. Bałaban CMP109 [7] is correctly identified as the primary source for localized small-field effective actions, beta-functions, and recursive coupling renormalization.
2. The claimed Eq. `(0.29)` / Taylor-Ward-beta chain has **not** yet been primary-extracted in the accessible audited source corpus, and the current web-facing primary records do not expose the necessary equation pages.
3. Consequently, [85]'s transcription remains a locator only and is not promoted to primary theorem custody.
4. Conditional on the displayed candidate bound `(L^j eta)^(4+alpha)` with `alpha>0`, fixed four-dimensional root counting leaves exactly `(L^j eta)^alpha`; this is geometrically summable in ultraviolet depth.
5. [85]'s separate claim of a universal dyadic `2^-2` net factor does not follow from `4+alpha` with merely `alpha>0`; the generic factor is `2^-alpha`.
6. The sharp `L^-2` quotient contraction sought in R67 remains unnecessary if the weaker positive-alpha source-scale bound is primary-verified and applies to the actual one-layer E defect.
7. The minimal remaining source/dictionary object is `OneLayerDefectToPaperIVjDictionary`, together with direct primary extraction of Eq. `(0.29)` and its hypotheses/uniformity.

Canonical state:

`PrimaryCMP109PaperIdentity = CLOSED`.

`PrimaryEq0.29PositiveAlphaBound = SOURCE-VERIFICATION OPEN`.

`PrimaryTaylorWardBetaChain = SOURCE-VERIFICATION OPEN`.

`PositiveAlphaFixedRegionSummability = DERIVED CONDITIONALLY`.

`[85]UniversalDyadic2^-2 = REJECTED AS UNSUPPORTED BY ITS DISPLAYED FORMULA ALONE`.

`OneLayerDefectToPaperIVjDictionary = LIVE`.

`SharpL^-2ProjectedContraction = FALLBACK / OVER-SPECIFIED`.

## Negative results / guardrails

- Do not promote [85] to primary theorem custody; its own v2 says faithful source transcription remains a condition.
- Do not identify `alpha>0` with `alpha=2`.
- Do not infer the one-layer cross-cutoff dictionary merely from matching notation `V^(j)` / `E^(j)`.
- Do not infer uniform constants in cutoff depth or volume until Eq. `(0.29)` and its hypotheses are read directly.
- Do not infer the full RG-Cauchy consumer `(M1)` from the candidate Eq. `(0.29)` bound alone.
- Do not infer continuum Yang–Mills construction or a mass gap from the conditional fixed-region summability calculation.

## Next frontier — YM-R70

`YM-R70 — Eq. (0.29) object/dictionary reconstruction and cross-depth index audit.`

Tasks:

1. reconstruct, without promoting unverified formulas, the exact type of `V^(j)` required by the candidate Eq. `(0.29)` statement;
2. compare that type with CMP119's scale-indexed `E^(j)` decomposition and R62's one-layer defect `Delta_N`;
3. identify the exact reindexing needed when a depth-`N+1` trajectory is blocked once to the depth-`N` first common scale;
4. determine whether positive-alpha suppression survives all normalization/marginal retuning operations at that common scale;
5. keep direct primary Eq. `(0.29)` extraction as a source-verification gate rather than inventing its contents.

Highest cumulative reference remains [85]; [86] remains next.