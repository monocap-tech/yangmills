# YM-R70 — Eq. (0.29) object/dictionary reconstruction and cross-depth index audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R71` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R69, which isolated a potentially decisive Paper-I source-scale irrelevance estimate but kept it conditional because the exact primary CMP109 Eq. (0.29) has not yet been directly extracted.

The present pass asks a logically separate question:

> Assuming the candidate Eq. (0.29) object exists with the traced positive-alpha bound, is that object actually the fresh regular defect created by the extra ultraviolet layer in the depth-`N+1` versus depth-`N` comparison?

This requires reconstructing the type relation between:

- the Paper-I scale-indexed correction `E^(j)`;
- the candidate irrelevant residual `V^(j)`;
- the later CMP119 regular coordinate `E_k`;
- the R62 one-layer cross-cutoff defect `Delta_N`.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. Cross-depth physical scale indexing closes exactly

Normalize the fixed endpoint physical/reference scale to one lattice unit and write the microscopic lattice spacing of the depth-`N` construction as

`eta_N := L^(-N)`.

After `j` RG blocking steps, the corresponding physical lattice spacing is

`a_(N,j) := L^j eta_N = L^(j-N)`.

For the depth-`N+1` construction,

`a_(N+1,j+1)`

`= L^(j+1) eta_(N+1)`

`= L^(j+1) L^(-(N+1))`

`= L^(j-N)`

`= a_(N,j)`.

Therefore

`boxed{ a_(N+1,j+1) = a_(N,j) }`.

This is an exact indexing identity, not a source theorem.

It closes the geometric part of R62's first-common-scale comparison:

- depth `N` scale `j=0` and depth `N+1` scale `j=1` have the same lattice spacing;
- depth `N` scale `j` and depth `N+1` scale `j+1` represent the same physical lattice scale all along the shared tail.

Canonical classification:

`CrossDepthPhysicalScaleAlignment = CLOSED / EXACT`.

This does **not** yet imply equality of couplings, effective densities, domains, beta functions, or localized cutoff data at those aligned scales.

## 2. The extra ultraviolet layer is the first generated correction of the finer theory

The depth-`N` construction begins at spacing

`eta_N = L^(-N)`

with its tuned bare Wilson density `B_N`.

The depth-`N+1` construction begins at

`eta_(N+1) = L^(-(N+1))`.

After one RG step it also lives at spacing `eta_N`.

In the Paper-I source grammar, the first RG step generates the first scale-indexed regular correction `E^(1)` together with a vacuum term and the designated beta/Wilson marginal contribution.

Thus, before normalization and coupling alignment, the common-scale difference has the schematic decomposition

`Delta_N`

`= deltaVac_N * 1`

`  + deltaMarg_N * A`

`  + FreshRegularResidual_N`

`  + FreshR/B/LargeField_N`.

Here:

- `deltaVac_N` is an overall normalization direction;
- `deltaMarg_N` is the Wilson-action / coupling direction;
- `FreshRegularResidual_N` is the marginal-subtracted regular output of the extra first RG layer;
- the `R/B` / large-field pieces belong to their already-separated source sectors.

This decomposition is structural. R70 does not identify every sign or normalization constant because the exact Paper-I extraction formula remains primary-source pending.

## 3. What can safely be called `V^(1)`

The secondary locator [85] changed presentation between versions.

Its v1 writes the Paper-I regular action schematically as

`E_k = sum_j [ - beta_j A + E^(j) ]`

and then gives an explicit formula for a residual called `V^(j)` involving `E^(j)` and the beta/Wilson term.

However, the literal sign convention in that v1 transcription is not safe enough to use as a canonical equality: read mechanically, the displayed formulas create a sign/naming tension.

The corrected v2 avoids this fragile algebraic identification. It describes `V^(j)` functionally as the **irrelevant residual** produced after the Taylor/Ward/beta extraction: the order-at-least-five local remainder together with the large-polymer contribution, controlled by the candidate Eq. (0.29) bound.

Therefore R70 adopts the quotient-safe typing:

`V^(j) := the Paper-I residual regular activity after vacuum and designated marginal extraction`,

without promoting either

`V^(j) = E^(j) + beta_j A`

or

`V^(j) = E^(j) - beta_j A`

until the primary CMP109 convention is inspected directly.

Canonical classification:

`PaperIVjType = IRRELEVANT REGULAR RESIDUAL AFTER EXTRACTION`.

`PaperIVjExactSignFormula = OPEN PRIMARY-SOURCE DETAIL`.

This resolves the object type without inventing a sign convention.

## 4. The common-scale regular defect is `V^(1)` modulo two explicit conditions

At the first common physical scale, compare:

1. the depth-`N` tuned bare Wilson theory; and
2. the one-step RG image of the depth-`N+1` tuned bare theory.

The second theory contains a fresh first-step regular correction.

If both of the following hold:

### A. Vacuum normalization

The common-scale comparison quotients out the overall field-independent normalization.

### B. Marginal tail coherence

The one-step coupling of the depth-`N+1` theory equals the bare coupling chosen for the depth-`N` theory at the same physical scale,

`g_1^(N+1) = g_0^(N)`,

with the same source convention for the Wilson-action coefficient.

Then the vacuum and marginal pieces of the fresh first-step correction do not survive in the normalized common-scale difference.

The regular small-field part of the one-layer defect is therefore exactly of the **type** controlled by `V^(1)`:

`Delta_(E,N) mod {vacuum, marginal} = V_(N+1)^(1)`.

Classification:

`OneLayerRegularDefectToPaperIV1Dictionary`

`= STRUCTURALLY CLOSED conditional on MarginalTailCoherence and primary extraction convention`.

The word `structurally` is essential: exact equality in the native notation remains gated by the primary Paper-I sign/normalization definition.

## 5. The source-scale factor of the extra layer is exactly the desired UV factor

For the finer depth-`N+1` theory, the first generated correction has source scale

`a_(N+1,1)`

`= L eta_(N+1)`

`= L * L^(-(N+1))`

`= L^(-N)`.

Hence the candidate Paper-I irrelevance factor becomes

`(L eta_(N+1))^(4+alpha)`

`= L^(-N(4+alpha))`.

Conditional on the candidate bound

`||V_(N+1)^(1)(X)||`

`<= C L^(-N(4+alpha)) exp(-kappa d_1(X))`,

and a cutoff-uniform rooted polymer summability estimate, a fixed four-dimensional physical region contributes `O(L^(4N))` scale-one roots.

Therefore the full fixed-region regular defect is bounded by

`epsilon_(E,N) <= C_O L^(4N) L^(-N(4+alpha))`

`= C_O L^(-alpha N)`.

Thus

`sum_N epsilon_(E,N) < infinity`

for every `alpha>0`.

Classification:

`Eq029 + OneLayerDictionary + alpha>0`

`=> FixedRegionRegularDefectSummability`.

This remains a conditional derivation because direct primary Eq. (0.29) custody is still open.

## 6. The scale shift preserves the candidate irrelevance prefactor on the shared tail

For any shared physical scale,

`a_(N+1,j+1) = a_(N,j)`.

Therefore

`(L^(j+1) eta_(N+1))^(4+alpha)`

`= (L^j eta_N)^(4+alpha)`.

This is important for interpreting the source index.

The shifted depth-`N+1` tail does **not** receive an artificial extra small factor merely because its index is one larger. The physical source-scale factor is invariant under the correct cross-depth reindexing.

Thus any agreement of the shared tail must come from genuine RG/coupling/domain coherence, not from an indexing artifact.

Canonical guardrail:

`IndexShift != ExtraIrrelevanceOnSharedTail`.

The one genuinely new small term is the extra finest-layer contribution that has no counterpart in the depth-`N` bare theory.

## 7. Cross-depth scale coherence is closed; coupling coherence is not

R70 separates two statements that were previously bundled together.

### Physical-scale coherence

`a_(N+1,j+1) = a_(N,j)`.

This is exact and closed.

### Marginal-flow coherence

`g_(j+1)^(N+1) = g_j^(N)`

at aligned physical scales.

This remains open.

The source coupling recursion contains indexed objects such as `beta_j`, localized cutoff functions, and regular-domain data. Even if the same endpoint renormalization condition is imposed, the project still needs a source-level cocycle/reindexing statement establishing that the shifted recursion for depth `N+1` is the same recursion used by depth `N` on the common tail.

Therefore:

`CrossDepthPhysicalScaleAlignment = CLOSED`,

but

`CrossDepthMarginalTailCoherence = OPEN`.

This is now the dominant obstruction to turning the regular one-layer dictionary into an actual N-versus-N+1 telescoping estimate.

## 8. The later CMP119 source provenance is compatible with this dictionary

CMP119 retains the regular action as a sum of scale-labelled contributions `E^(j)` and separately carries the localized running coupling.

Therefore the Paper-I source index is not erased by the later complete-density architecture.

Conceptually the chain is:

`extra fine Wilson layer`

`-> first Paper-I RG step`

`-> {vacuum + beta/Wilson + V^(1)}`

`-> later complete-density bookkeeping retaining source-scale provenance`.

This makes it unnecessary to interpret the extra ultraviolet residual as an arbitrary perturbation inserted into a Banach ball. It is a canonical generated source contribution with a known source scale.

This is exactly why the positive-alpha route can be weaker than the R63 stable-manifold theorem.

## 9. What Eq. (0.29) would accomplish if primary custody succeeds

If direct CMP109 extraction confirms all of the following:

1. `V^(j)` is the regular residual after the designated local marginal extraction;
2. the bound has a positive exponent `alpha>0`;
3. the norm is compatible with the later polymer/root summation;
4. constants are uniform in cutoff depth and volume in the stated small-field jurisdiction;
5. the estimate applies to the first generated correction `j=1`;

then the **regular E-sector** of the one-layer cross-cutoff defect is no longer a live convergence obstruction.

Indeed, under marginal tail coherence,

`epsilon_(E,N) = O(L^(-alpha N))`,

which is summable.

At that point the cross-cutoff UV problem decomposes into:

- scalar marginal-tail coherence;
- already-suppressed `R` sector;
- large-field/boundary sector transport;
- conversion of summable endpoint defects into the desired observable/state topology.

No global quotient contraction theorem is needed for the regular E-sector.

## 10. Primary custody remains the one hard source gate

R70 still does not promote [85]'s Eq. (0.29) transcription to Bałaban theorem status.

Public primary metadata verifies that CMP109 constructs localized effective actions, beta functions, and a recursive coupling renormalization in four dimensions [7]. The project also has an external source-audit record stating that a private primary CMP109 PDF exists in a source cache, but the exact Eq. (0.29) chain has not been committed in source-verified form.

Therefore:

`PrimaryEq029PositiveAlphaBound = OPEN SOURCE GATE`.

The object/index reconstruction above is valuable precisely because it tells us what that one source extraction would buy.

## 11. Determination

R70 establishes:

1. With `eta_N=L^-N`, the aligned depth-`N` / depth-`N+1` physical scales satisfy the exact cocycle identity `a_(N+1,j+1)=a_(N,j)`.
2. The extra ultraviolet layer of the depth-`N+1` theory produces the first scale-indexed regular correction at exactly the depth-`N` bare physical scale.
3. The safe type for Paper-I `V^(j)` is the irrelevant regular residual after vacuum and designated beta/Wilson extraction; the exact plus/minus sign convention is left primary-source pending.
4. Conditional on vacuum normalization and marginal-tail coherence, the regular small-field component of the R62 one-layer defect is exactly of `V^(1)` type.
5. The candidate Eq. (0.29) factor on this extra first layer is `L^-N(4+alpha)`; four-dimensional root counting leaves `L^-alpha N`, which is geometrically summable for every `alpha>0`.
6. The source-scale factor is invariant on the correctly shifted shared tail, so index shifting cannot be mistaken for physical suppression.
7. Cross-depth physical-scale alignment is closed, while cross-depth marginal-tail coherence remains open and is now the main scalar compatibility theorem.
8. If primary Eq. (0.29) custody succeeds, the regular E-sector cross-cutoff memory problem reduces to a summable extra-layer source contribution rather than a full two-trajectory contraction theorem.

Canonical state:

`CrossDepthPhysicalScaleAlignment = CLOSED / EXACT`.

`PaperIVjType = IRRELEVANT REGULAR RESIDUAL AFTER EXTRACTION`.

`PaperIVjExactSignFormula = OPEN PRIMARY DETAIL`.

`OneLayerRegularDefectToPaperIV1Dictionary = STRUCTURALLY CLOSED conditional on MarginalTailCoherence`.

`PrimaryEq029PositiveAlphaBound = OPEN SOURCE GATE`.

`Eq029 + alpha>0 + rooted summability => FixedRegionRegularDefectSummability = DERIVED CONDITIONAL`.

`CrossDepthMarginalTailCoherence = LIVE`.

`SharpProjectedQuotientContraction = FALLBACK / NOT REQUIRED if the positive-alpha route is source-verified`.

## Negative results / guardrails

- Do not use the v1 secondary sign convention for `V^(j)` as a primary equality; v2's quotient-safe residual typing is the safer object description.
- Do not infer coupling-tail equality from the exact physical-scale identity.
- Do not infer extra suppression on the shared tail from the `j -> j+1` index shift; the physical source-scale factor is invariant under that shift.
- Do not apply the Paper-I small-field regular bound to `R`, `B`, or large-field sectors without their own source dictionaries.
- Do not promote [85] to primary theorem custody.
- Do not infer continuum Yang–Mills existence, OS reconstruction, infinite volume, or a mass gap from conditional regular-sector summability.

## Next frontier — YM-R71

`YM-R71 — cross-depth marginal-tail coherence / beta-map cocycle audit.`

Tasks:

1. write the depth-dependent scalar recursion at fixed physical scales and perform the exact `N -> N+1`, `j -> j+1` reindexing;
2. determine whether `beta_(j+1)^(N+1)` and `beta_j^(N)` are the same source function after scale/domain identification, or whether boundary/localization data produce a mismatch;
3. distinguish bulk/interior tail coherence from finite-volume boundary coherence;
4. determine whether uniqueness of the R61 backward scalar tuning then forces `g_(j+1)^(N+1)=g_j^(N)`;
5. retain direct primary CMP109 Eq. (0.29) extraction as an independent source gate.

Highest cumulative reference remains [85]; [86] remains next.