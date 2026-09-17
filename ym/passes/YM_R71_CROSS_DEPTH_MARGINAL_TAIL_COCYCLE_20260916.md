# YM-R71 — cross-depth marginal-tail coherence / beta-map cocycle audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R72` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R70. The physical-scale indexing problem is now closed exactly:

`a_(N+1,j+1) = a_(N,j)`.

The remaining scalar question is whether the separately endpoint-tuned depth-`N` and depth-`N+1` coupling trajectories are exact shifted tails of one another:

`g_(j+1)^(N+1) = g_j^(N)`

at every aligned physical scale.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. Separate physical-scale alignment from beta-map alignment

For depth `N`, let

`x_j^(N) := (g_j^(N))^-2`, `j=0,...,N`.

Write the one-step scalar map in the abstract R61 form

`x_j^(N) = F_(N,j)(x_(j-1)^(N))`,

where schematically

`F_(N,j)(x) = x - B_(N,j)(x)`

and `B_(N,j)(x)` is the inverse-square beta increment in the relevant source convention.

The depth-`N+1` trajectory has maps `F_(N+1,r)`, `r=1,...,N+1`.

R70 closed only

`physical scale(N,j) = physical scale(N+1,j+1)`.

This does not itself imply

`F_(N,j) = F_(N+1,j+1)`.

The latter is the actual cocycle condition.

Canonical name:

`BetaMapShiftCovariance:`

`F_(N+1,j+1) = F_(N,j)` on the common weak-coupling corridor.

Equivalently, in inverse-square increment notation,

`B_(N+1,j+1) = B_(N,j)`.

## 2. Exact cocycle theorem: shift covariance + endpoint uniqueness forces tail nesting

Assume:

1. the endpoint renormalization condition is the same for both depths,

   `x_N^(N) = x_(N+1)^(N+1) = x_*`;

2. every one-step map in the common weak corridor is injective / backward-selecting as in R61;

3. the common-tail maps satisfy

   `F_(N+1,j+1) = F_(N,j)`, `j=1,...,N`.

Then

`x_(j+1)^(N+1) = x_j^(N)`

for every `j=0,...,N`.

Proof: equality holds at the endpoint `j=N`. Apply the unique inverse of

`F_(N,N) = F_(N+1,N+1)`

to obtain

`x_(N-1)^(N) = x_N^(N+1)`.

Repeat backward through the common maps. This yields the entire shifted-tail equality.

Therefore

`BetaMapShiftCovariance + EndpointCondition + BackwardUniqueness`

`=> CrossDepthMarginalTailCoherence`.

Classification: DERIVATION.

This is a substantial simplification: tail coherence is not an additional global dynamical theorem once the scalar one-step maps are known to be the same on aligned scales.

## 3. CMP119 removes the localized cutoff from the bulk cocycle

CMP119 Eq. (2.24) has the source-normalized shape

`1/g_(j-1)^2(x) = 1/g_j^2(x) + beta_j(g_(j-1)) phi_j(x)`.

The extracted source record states that `phi_j=1` on the indicated interior subdomain.

Hence, for a point / local observable support lying in the common interior jurisdiction,

`1/g_(j-1)^2 = 1/g_j^2 + beta_j(g_(j-1))`.

Thus the bulk cocycle question is not obstructed by the cutoff function itself.

Canonical split:

`BulkMarginalCocycle` depends on the beta map,

whereas

`BoundaryLocalizedCouplingMismatch` belongs to the boundary/localized complete-density sector.

This prevents a boundary bookkeeping device from being mis-typed as a failure of the bulk scalar RG law.

## 4. What the primary literature currently source-attests

CMP109 [7] is source-verified at paper level to construct beta-functions and define coupling-constant renormalization by a recursive system of RG equations.

CMP119 [59] imports those equations into the complete-density induction and writes the localized running coupling through Eq. (2.24).

The accessible source audit verifies the syntactic form

`beta_j(g_(j-1))`

and the interior property `phi_j=1`.

What is **not** presently source-custodied is the cross-depth identity

`beta_(j+1)^(N+1)(g) = beta_j^(N)(g)`

under fixed-physical-scale alignment.

The source notation normally suppresses the cutoff-depth superscript `N`, so the needed covariance cannot be inferred merely by observing that both formulas are written `beta_j`.

Canonical status:

`NativeBetaMapShiftCovariance = OPEN SOURCE/THEOREM OBLIGATION`.

## 5. The secondary locator supports autonomy only at leading form, not exact cocycle custody

Reference [85] v2 summarizes the Paper-I beta extraction as a discrete weak-coupling flow of the form

`g_(k+1)^-2 = g_k^-2 + 2 b_0 log L + O(g_k^2)`

and describes the coupling as increasing toward the infrared.

This is useful structural evidence that the leading step is scale-homogeneous: the universal `2 b_0 log L` term has no explicit dependence on the ultraviolet depth.

But [85] is deliberately retained only as a traceability locator. Its `O(g_k^2)` remainder is not an exact source-custodied map, and it does not establish that finite-volume, localized-domain, or cutoff-dependent corrections satisfy the exact shift identity required above.

Therefore R71 does not promote

`BetaMapShiftCovariance`

from this secondary statement.

## 6. Exact tail coherence is stronger than what the regular E-sector actually needs

R70 showed that, conditional on the candidate Paper-I positive-alpha estimate, the extra first-layer regular defect is summable like

`L^(-alpha N)`.

Suppose the scalar tails are not exactly identical but instead satisfy a small mismatch

`delta x_j^(N) := x_(j+1)^(N+1) - x_j^(N)`.

Then exact equality is not necessary if the marginal mismatch induced in fixed-scale observables is itself summable in `N`.

This suggests a weaker fallback object:

`SummableMarginalTailMismatch`.

To make it quantitative, let the aligned one-step maps differ by

`epsilon_(N,j)(x) := F_(N+1,j+1)(x) - F_(N,j)(x)`.

If the inverse maps on the weak corridor are uniformly Lipschitz with factor at most `lambda_j`, then backward comparison gives schematically

`|delta x_(j-1)| <= lambda_j ( |delta x_j| + sup |epsilon_(N,j)| )`.

With zero endpoint mismatch, iteration yields an accumulated beta-map defect controlled by a weighted sum of the `epsilon_(N,j)`.

Hence exact cocycle covariance may be replaced by a summable cross-depth beta-map mismatch theorem.

Classification: DERIVATION / FALLBACK THEOREM SHAPE.

No native bound of this form is currently source-extracted.

## 7. Why endpoint equality alone still does not force the common tail

It is tempting to reason:

`same endpoint g_* + same number of physical scales in the tail => same tail`.

This is false without one-step map covariance.

Two nonautonomous recursions can share the same terminal value and nevertheless have different predecessors. Backward uniqueness only selects a unique predecessor **for a given one-step map**.

Thus R61's uniqueness theorem and R70's physical-scale identity become sufficient only after the map-cocycle condition is supplied.

Canonical guardrail:

`EndpointEquality + ScaleAlignment != TailCoherence`.

The missing equality is equality of the actual renormalization maps.

## 8. Bulk versus boundary/localized mismatch

CMP119 localizes the coupling with `phi_j`. On the common interior, `phi_j=1`, so the scalar bulk map reduces to the beta recursion.

Near boundaries of the regular domains, however, `phi_j` can differ from one and the nested domain sequences for the `N` and `N+1` constructions need not coincide under a naive shift.

R71 therefore types any such discrepancy as

`BoundaryLocalizedCouplingMismatch`,

not as a new bulk marginal coordinate.

For fixed local observables whose support eventually lies in the common interior as the UV cutoff is removed, the relevant scalar theorem is `BulkMarginalCocycle`. Boundary contributions must instead be controlled together with the `B` / large-field localized sector.

This separation is compatible with the CMP119 complete-density architecture, where boundary terms are already stored separately.

## 9. Revised scalar dependency graph

The scalar cross-cutoff branch is now:

`CrossDepthPhysicalScaleAlignment` [R70, CLOSED]

`+ EndpointRenormalizationCondition` [R61, CLOSED as datum]

`+ BackwardScalarUniqueness` [R61, ABSTRACTLY CLOSED under corridor]

`+ NativeBetaMapShiftCovariance` [OPEN]

`=> CrossDepthMarginalTailCoherence`.

If exact covariance fails or is unavailable, the weaker route is

`SummableBetaMapShiftDefect + inverse-map stability`

`=> SummableMarginalTailMismatch`.

Thus the scalar problem has been compressed to one one-step source object.

## 10. Interaction with the R70 positive-alpha route

If `NativeBetaMapShiftCovariance` is established, then:

1. the fine depth-`N+1` theory after one step has exactly the depth-`N` bare coupling at the first common scale;
2. the common scalar tail nests exactly;
3. vacuum normalization plus marginal alignment removes the fresh Wilson-direction piece from the R70 one-layer regular defect;
4. conditional on primary Eq. (0.29), the remaining regular defect is the positive-alpha `V^(1)` contribution and is fixed-region summable.

Therefore the pair

`BetaMapShiftCovariance + PrimaryEq029PositiveAlphaBound`

would close the small-field `g/E` cross-cutoff memory mechanism without invoking the R63 global stable-manifold theorem.

The remaining UV sectors would then be `R`, boundary/large-field transport, and observable/state reconstruction.

## 11. Determination

R71 establishes:

1. Cross-depth marginal-tail coherence is an algebraic consequence of three ingredients: common endpoint condition, backward uniqueness, and shift covariance of the one-step beta maps.
2. R61 already supplies the abstract uniqueness grammar; R70 supplies exact physical-scale alignment. Therefore the only genuinely new scalar theorem is `BetaMapShiftCovariance`.
3. CMP119's localized cutoff `phi_j` disappears on the common interior (`phi_j=1`), so the bulk cocycle problem is purely the beta recursion. Boundary cutoff mismatches should be assigned to the boundary/localized sector.
4. The primary published chain verifies construction of recursive beta functions but the current source corpus does not establish the exact cross-depth identity `beta_(j+1)^(N+1)=beta_j^(N)`.
5. [85] gives secondary evidence for a scale-homogeneous leading flow `2 b_0 log L + O(g^2)` but does not supply exact cocycle custody.
6. Exact tail equality is stronger than strictly necessary: a summable cross-depth beta-map mismatch, combined with inverse-map stability, would suffice for observable Cauchy convergence.
7. Endpoint coupling equality and physical-scale alignment alone do not imply tail coherence.
8. If exact beta-map shift covariance and the candidate positive-alpha Paper-I bound are both ultimately source-verified, the small-field marginal-plus-regular cross-cutoff branch becomes summable without a global stable-fiber theorem.

Canonical state:

`CrossDepthPhysicalScaleAlignment = CLOSED / EXACT`.

`BackwardScalarUniqueness = ABSTRACTLY CLOSED under R61 corridor`.

`BulkPhiEqualsOne = SOURCE-ATTESTED on interior`.

`NativeBetaMapShiftCovariance = OPEN`.

`CrossDepthMarginalTailCoherence = REDUCED TO NativeBetaMapShiftCovariance`.

`SummableMarginalTailMismatch = LIVE FALLBACK`.

`BoundaryLocalizedCouplingMismatch = RETYPED INTO B/BOUNDARY SECTOR`.

## Negative results / guardrails

- Do not infer exact tail nesting from endpoint equality alone.
- Do not infer beta-map shift covariance merely because the source suppresses the cutoff-depth superscript.
- Do not use the secondary `2 b_0 log L + O(g^2)` formula as an exact primary cocycle theorem.
- Do not mix `phi_j != 1` boundary effects into the bulk scalar recursion when the fixed observable lies in the common interior.
- Do not require exact marginal-tail equality if a quantitatively summable mismatch theorem is sufficient for the final observable topology.
- Do not infer continuum construction or a mass gap from scalar cocycle closure.

## Next frontier — YM-R72

`YM-R72 — beta-map shift covariance / cross-depth mismatch summability audit.`

Tasks:

1. target the Paper-I beta-function definition and determine which parameters besides `g` and the fixed block factor `L` enter `beta_j`;
2. test whether those parameters are invariant under `(N,j)->(N+1,j+1)` at aligned physical scales;
3. separate exact bulk scale covariance from finite-volume / regular-domain boundary corrections;
4. if exact equality is not source-native, derive the weakest quantitative bound on `F_(N+1,j+1)-F_(N,j)` sufficient for summable marginal mismatch;
5. retain the primary Eq. (0.29) source gate in parallel but do not conflate it with the scalar beta cocycle.

Highest cumulative reference remains [85]; [86] remains next.