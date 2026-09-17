# YM-R65 — Paper-I marginal orthogonality / UV-defect amplitude audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R66` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R64, which established source-attested triangularity of the *declared* CMP119 coupling coordinate and identified two possible cross-cutoff Cauchy mechanisms:

1. common marginal tail + complementary difference contraction; or
2. one-layer UV defect tending to zero rapidly enough that only bounded propagation is required.

R65 audits the source evidence needed for the second route and sharpens what is, and is not, proved by the Paper-I/CMP119 marginal subtraction.

Repeated sources: [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [22] Bałaban CMP122-II.
No new bibliography item is consumed. Highest remains [84].

Source-extraction note: an auxiliary public source-audit corpus with locators to locally rendered CMP109/CMP116/CMP119 primary pages was used only to target formulas already attributed here to the primary papers. It is not assigned a project bibliography number.

## 1. The source architecture removes the designated beta multiple exactly

CMP119 Eq. (2.24) prescribes the localized inverse-square coupling recursion

`1/g_{j-1}^2(x) = 1/g_j^2(x) + beta_j(g_{j-1}) phi_j(x)`.

CMP119 Eq. (2.25) then writes the regular action as a scale sum whose `j`-th contribution has the normalized shape

`E^(j)(Lambda_j,g_{j-1},U_k)`

`- E^(j)(Lambda_j,g_{j-1},1)`

`- beta_j(g_{j-1}) A(phi_j,U_k)`.

Thus two pieces are removed from each fresh regular contribution before it enters the stored `E` coordinate:

1. the field-independent/vacuum value;
2. the designated local Wilson-action / marginal contribution with coefficient `beta_j`.

This is stronger than a merely informal statement that the coupling is "kept separately".

Canonical classification:

`PrescribedVacuumSubtraction = SOURCE-ATTESTED`.

`PrescribedBetaASubtraction = SOURCE-ATTESTED`.

## 2. But exact projection orthogonality is still not source-custodied

The stronger object needed by R63/R64 would be a source-defined extraction functional `Loc_A` satisfying, for the residual contribution,

`Loc_A( E^(j) - E^(j)(1) - beta_j A ) = 0`,

with `beta_j = Loc_A(E^(j)-E^(j)(1))` in the exact native normalization.

The displayed CMP119 formula is fully consistent with this interpretation, and it is clearly the intended coordinate grammar.

However, the present corpus still lacks the exact Paper-I definition of `beta_j` and the exact local-extraction operation used to obtain it. Therefore R65 does **not** promote the above projector identity from interpretation to theorem.

Canonical status:

`ExactExtractionOrthogonality = NARROWED BUT OPEN`.

The remaining source question is no longer whether a subtraction exists. It is only whether the source defines `beta_j` by an exact projection/extraction identity strong enough to support perturbations or cross-cutoff differences.

## 3. The Paper-I/CMP116 regular E bound is uniform-small, not source-attested as g-vanishing

A source-extracted CMP109 localization formula uses the bound

`|E^(j)(X,U)| <= E_0 exp(-kappa d_j(X))`.

CMP116 Lemma 3 and Eqs. (2.39)--(2.41) propagate the one-step cluster contribution into the next regular action with source-normalized shape

`|E^(k+1)(X)| <= O(1) C_3 epsilon_1 exp(-kappa d_{k+1}(X))`

after the source choice of the decay normalization, and the proof requires the amplitude to fit an `E_0/2` budget.

These are powerful small/localized bounds, but the extracted statements presently do **not** identify either

`E_0 -> 0 as g -> 0`

or

`epsilon_1 = O(g^p)`

for a positive `p`.

Therefore the currently source-attested regular-sector estimate is of the logical type

`||E_new|| <= small fixed budget`,

not

`||E_new|| <= C g^p`.

Canonical negative result:

`RegularEDefectVanishingFromCurrentSourceBound = NOT ESTABLISHED`.

## 4. The R sector is genuinely UV-small

CMP119 Eq. (2.31) supplies the qualitatively different bound

`|R^(j)(X,(U,J))| <= g_j^kappa0 exp(-kappa d_j(X))`,

where `kappa0` may be chosen large after the other parameters have been fixed.

Along the R60/R61 tuned ultraviolet family,

`g_UV^(N) -> 0`.

Hence for a defect created in the extra ultraviolet layer, any component controlled directly by this estimate satisfies

`g_UV^(N)^kappa0 -> 0`.

Under the abstract R60 corridor `g_UV^(N) = O(N^-1/2)`, this gives

`g_UV^(N)^kappa0 = O(N^(-kappa0/2))`.

Thus, for `kappa0>2`, the scalar amplitude is summable in `N` before polymer counting, provided the relevant polymer sum is uniformly controlled.

Classification:

`R-SectorUVDefectSmallness = DERIVED conditional on the tuned coupling law and native polymer summability`.

This does **not** prove smallness of the complete density defect.

## 5. Boundary / large-field terms are not g-small in the recorded complete-density norm

CMP119 Eq. (2.42) bounds localized boundary terms schematically by

`|B^(j)(X,...)| <= B_0 exp(-kappa d_j(X))`.

The source amplitude `B_0` in the extracted bound does not itself carry a positive power of `g_j`.

Likewise, large-field machinery supplies strong geometric/probabilistic suppression in its own localized architecture, but this is not the same as saying that the `B` coordinate has norm `O(g^p)`.

Therefore a raw complete-density norm that treats the `B` amplitude directly does not currently make the extra ultraviolet boundary piece tend to zero solely from `g_UV -> 0`.

Canonical status:

`BoundaryDefectVanishingInRawCompleteDensityNorm = NOT ESTABLISHED`.

## 6. The small-UV-defect shortcut therefore fails in the strongest native norm

R64 left open the possibility

`D_N := ||Delta_N|| -> 0`

for the complete one-layer cross-cutoff defect.

The component audit now gives:

`Delta_N = Delta_E,N + Delta_R,N + Delta_B,N + ...`.

The source bounds support

`Delta_R,N -> 0`

in the explicit `g^kappa0` sector, but do not presently imply

`Delta_E,N -> 0`

or

`Delta_B,N -> 0`

in the corresponding raw complete-density norm.

Hence:

`g_UV -> 0`

**does not by itself imply**

`||Delta_N||_complete -> 0`.

Canonical negative result:

`UVDefectSmallnessAlternative[raw complete-density norm] = INSUFFICIENT / NOT CLOSED`.

This eliminates the easiest reading of R64's alternative route.

## 7. This does not mean the extra UV layer remains physically visible

The failure above is norm-specific.

CMP119 retains source-scale provenance in the regular action:

`E_k = sum_j E^(j) ...`.

A contribution created very far in the ultraviolet may remain `O(E_0)` in a **renormalized source-scale activity norm** while nevertheless becoming negligible when transported to:

- a fixed physical reference scale;
- a fixed finite set of coarse gauge-invariant observables;
- a topology that assigns the correct irrelevant scaling to source-scale-separated local operators.

This is exactly the distinction between

`native inductive boundedness`

and

`physical loss of ultraviolet memory`.

The source norm is designed to close the RG induction. It need not be the topology in which the continuum state is Cauchy.

## 8. Why the E sector is the decisive new carrier

After vacuum and designated `A(U)` subtraction, symmetry/power-counting arguments from earlier passes suggest that a genuinely local residual pure-gauge jet should begin beyond the dimension-four marginal direction.

If a source-compatible theorem turned this into a scale-separated estimate such as

`||Transport_{j->k} E_res^(j)||_obs <= C L^{-eta (k-j)} ||E_res^(j)||_native`,

with `eta>0`, then an `O(E_0)` fresh ultraviolet contribution could still disappear at a fixed endpoint as its scale separation grows.

This would close cross-cutoff memory without demanding that the fresh native amplitude itself tend to zero.

But R65 does **not** claim such an estimate. The published bounds presently custodied here establish localization and absolute smallness, not the above source-scale transport inequality.

Canonical new object:

`ScaleSeparatedETransport`.

## 9. Revised Cauchy routes

After R65 the cross-cutoff problem has three precisely typed routes.

### Route A — strict complementary loss of memory

`bounded one-layer defect`

`+ q<1 complementary difference contraction`

`=> endpoint Cauchy`.

This is R62/R63's stable-fiber route.

### Route B — raw one-layer amplitude vanishing

`Delta_N -> 0 summably in complete-density norm`

`+ bounded propagation`

`=> endpoint Cauchy`.

R65 shows this route is source-supported for the explicit `R` sector only, not for the complete E/R/B density.

### Route C — scale-separated observable irrelevance

`fresh UV E/B defect may be O(1) in native scale norm`

but

`its transport to fixed physical observables decays with UV/endpoint scale separation`.

This route is now the most natural alternative to a full two-trajectory contraction theorem.

## 10. Important topology correction

R62 formulated a convenient sufficient theorem in the complete-density norm. R65 shows that this may be stronger than necessary for continuum construction.

What the continuum theory ultimately needs is convergence of a compatible family of gauge-invariant local expectations / Schwinger functionals in a topology sufficient for OS reconstruction, not necessarily Cauchy convergence of every renormalized action coordinate in the strongest native induction norm.

Thus:

`CompleteDensityNormCauchy`

is a sufficient target, but not obviously a necessary one.

This correction prevents the project from turning Bałaban's deliberately scale-renormalized `E` coordinate into an artificial obstruction.

## 11. Determination

R65 establishes:

1. CMP119 source-attests exact subtraction of the vacuum value and the designated `beta_j A` term from each stored regular contribution.
2. The exact Paper-I local-extraction functional defining `beta_j` is still missing, so general projector orthogonality remains open.
3. The source-attested regular `E` bound is an `E_0`/`epsilon_1` small-budget bound; the current extraction does not prove that its amplitude vanishes as `g -> 0`.
4. The CMP119 `R` sector does carry an explicit arbitrarily-high positive power `g^kappa0`, so the extra-UV-layer R defect vanishes, and under the abstract `N^-1/2` tuning law can be made summable by choosing `kappa0` large enough.
5. The recorded `B`-sector bound has no explicit g-small amplitude, so complete-density UV-defect vanishing does not follow from the existing component estimates.
6. Therefore R64's `small UV defect + bounded propagation` shortcut is not closed in the raw complete-density norm.
7. This exposes a better alternative object: source-scale-separated transport of the marginal-subtracted `E` increment into a fixed physical/observable topology.
8. Complete-density-norm Cauchy is retained as a sufficient condition, but it is no longer treated as the uniquely correct continuum topology.

Canonical state:

`PrescribedBetaASubtraction = CLOSED / SOURCE-ATTESTED`.

`ExactExtractionOrthogonality = OPEN, narrowly localized to Paper-I beta extraction`.

`R-SectorUVDefectSmallness = CLOSED conditionally on tuned g and polymer summability`.

`RegularEDefectVanishingInNativeNorm = NOT ESTABLISHED`.

`BoundaryDefectVanishingInNativeNorm = NOT ESTABLISHED`.

`FullUVDefectSmallnessInNativeNorm = NOT CLOSED`.

`ScaleSeparatedETransport = LIVE NEW OBLIGATION`.

`NativeComplementaryDifferenceContraction = still OPEN`.

## Negative results / guardrails

- Do not infer `Loc_A(E_res)=0` for arbitrary perturbations from the visible subtraction alone until the Paper-I beta extraction is recovered.
- Do not infer `E_0` or `epsilon_1` tends to zero with `g` from the currently extracted source statements.
- Do not promote the `g^kappa0` R-sector estimate to the whole E/R/B density.
- Do not infer B-coordinate norm smallness from the probabilistic rarity of large fields without the corresponding weighted norm theorem.
- Do not demand Cauchy convergence in the strongest native induction norm if convergence of fixed gauge-invariant observables can be proved in a weaker physical topology.
- Do not infer continuum construction or a mass gap from source-scale irrelevance alone.

## Next frontier — YM-R66

`YM-R66 — source-scale E transport / fixed-observable ultraviolet-memory audit.`

Tasks:

1. use the explicit `E_k = sum_j E^(j)` provenance to compare one extra ultraviolet `E` increment after many common RG layers;
2. determine whether Paper I/II contains a scale-gain estimate for a marginal-subtracted regular activity beyond mere same-scale `E_0 exp(-kappa d_j)` boundedness;
3. identify the weakest topology on fixed-scale gauge-invariant observables in which the extra-UV-layer contribution would vanish;
4. distinguish operator-dimension/power-counting expectation from a source-native norm theorem;
5. if no transport theorem exists, return to `NativeComplementaryDifferenceContraction` as the remaining route.

Highest cumulative reference remains [84]; [85] remains next.
