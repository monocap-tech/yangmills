# YM-R74 — beta-family hidden-parameter / autonomy audit

Date: 2026-09-22
Lineage date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R75` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R73, which showed that on the canonical CMP119-generated family there is no independent source-native `V -> beta` coordinate: any ultraviolet-history dependence of the scalar law is already encoded in the indexed family `beta_j`.

R74 asks exactly what hidden data the source-visible notation permits `beta_j` to depend on besides the running coupling.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. Start from the exact source-visible argument list

CMP119 Sect. 2 source-attests the localized scalar recursion

`1/g_(j-1)^2(x) = 1/g_j^2(x) + beta_j(g_(j-1)) phi_j(x)`.

The regular action is separately stored as

`E_k(U_k) = sum_(i=1)^k [ E^(i)(Lambda_i,g_(i-1),U_k)`

`                           - E^(i)(Lambda_i,g_(i-1),1)`

`                           - beta_i(g_(i-1)) A(phi_i,U_k) ]`.

The complete action elsewhere depends on the regular/large-field domain sequences, but the source-visible scalar coefficient is still written

`beta_j(g)`.

Thus, in the canonical representation, the explicit beta argument list does **not** contain:

- `Lambda_j`;
- `Omega_j`;
- the large-field sequence `S_j`;
- the finite volume as a direct argument;
- the background gauge field;
- the accumulated regular action `E_k`;
- `R_k` or `B_k`;
- an inherited source-labelled residual `V^(i)`.

Classification:

`SourceVisibleBetaArguments = {j, g}`.

This statement is source-attested at the level of the published CMP119 coordinate grammar.

## 2. Boundary localization is external to the bulk beta coefficient

The position dependence in CMP119 enters through

`phi_j(x)`.

The source record has

`phi_j = 1`

on the relevant interior region.

Hence on the common bulk interior,

`1/g_(j-1)^2 = 1/g_j^2 + beta_j(g_(j-1))`.

Any failure of the localized cutoff functions or domain boundaries to line up under a cross-depth shift is therefore not a hidden argument of the bulk coefficient `beta_j`; it is an external localization/boundary effect.

Canonical classification:

`BulkBetaBoundaryDependence = SEPARATED INTO phi/B-SECTOR BOOKKEEPING`.

This strengthens R71's bulk-versus-boundary split.

## 3. Finite-volume/domain data are not source-visible beta arguments

CMP119's complete action depends on domain sequences such as `Omega_i`, `Lambda_i`, and `S_i`; the source audit explicitly records this dependence for `A_k`.

But Eq. (2.24) does not write

`beta_j(g; Lambda_j,Omega_j,S_j,...)`.

Instead those structures are used to localize the scalar coupling after the coefficient has been supplied.

Therefore R74 can rule out the following *as separate canonical source arguments*:

`DirectFiniteVolumeBetaArgument`,
`DirectRegularDomainBetaArgument`,
`DirectLargeFieldHistoryBetaArgument`.

This does **not** prove mathematically that the construction of the indexed function `beta_j` was performed without reference to any finite-volume or scale-stage data. It says only that such data, if present, are hidden inside the meaning of the index `j`, not independent displayed variables.

That distinction is the central result of this pass.

## 4. The hidden-parameter problem collapses to the semantics of the scale label j

After R73 and Sections 1-3 above, the source-visible family has the form

`beta_j : g -> beta_j(g)`.

Therefore any surviving nonautonomy can only enter through what is encoded by the label `j`.

Possible interpretations are:

### A. Pure RG-step label

The one-step problem is rescaled to the same dimensionless lattice geometry after every blocking step, so

`beta_j(g) = beta(g)`

in the bulk.

Then the family is autonomous and exact cross-depth shift covariance is immediate.

### B. Physical-scale label

There is a single two-variable law

`mathfrak beta(a,g)`

such that

`beta_j^(N)(g) = mathfrak beta(a_(N,j),g)`.

R70 proved

`a_(N+1,j+1)=a_(N,j)`.

Therefore physical-scale dependence also gives exact cross-depth shift covariance:

`beta_(j+1)^(N+1)(g)=beta_j^(N)(g)`.

### C. Absolute-depth / regulator-history label

The function at stage `j` carries data not determined by the aligned physical scale, e.g. the number of preceding UV steps or another global construction parameter.

Then exact shift covariance may fail.

Thus:

`NativeBetaMapShiftCovariance`

is now equivalent to excluding interpretation C, not to proving independence from every complete-density coordinate separately.

## 5. Abstract scale-covariance theorem

Let

`a_(N,j)=L^(j-N)`

as in R70.

Assume there exists a function

`mathfrak B(a,x)`

on the weak inverse-square corridor such that

`B_(N,j)(x)=mathfrak B(a_(N,j),x)`.

Then

`B_(N+1,j+1)(x)`

`= mathfrak B(a_(N+1,j+1),x)`

`= mathfrak B(a_(N,j),x)`

`= B_(N,j)(x)`.

Hence:

`PhysicalScaleLocalityOfBeta => NativeBetaMapShiftCovariance`.

By R71,

`PhysicalScaleLocalityOfBeta + EndpointCondition + BackwardUniqueness`

`=> CrossDepthMarginalTailCoherence`.

Classification: DERIVATION.

This is weaker than demanding full autonomy `beta_j=beta`: dependence on physical scale is harmless because aligned cross-depth scales coincide exactly.

## 6. What the primary/public record does establish

Public metadata for CMP109 [7] states that Bałaban constructs a sequence of localized effective actions, constructs beta-functions, and defines coupling-constant renormalization by a recursive system of RG equations.

CMP119 [59] then uses an indexed beta family in its complete-density induction.

This establishes the existence and role of the indexed family, but the presently extracted equation-level source material does not state whether

`beta_j`

is:

- literally the same function for every `j`;
- a function only of the physical scale and `g`;
- or a family carrying further absolute-depth data.

Therefore:

`BetaIndexSemantics = OPEN PRIMARY-SOURCE DETAIL`.

This is now the entire native scalar source gate.

## 7. Secondary perturbative evidence is compatible with autonomy but does not prove it

Reference [85] and related secondary traceability papers describe a weak-coupling law of the form

`g_(k+1)^-2 = g_k^-2 + 2 b_0 log L + O(g_k^2)`.

The leading term depends only on the fixed blocking factor `L`, and the formula is presented as a local per-step running-coupling law.

This is structurally compatible with either interpretation A or B above.

But the absolute `O(g^2)` remainder still does not determine whether the full indexed function is shift-covariant across cutoff depths.

Thus the secondary literature supplies:

`LeadingBulkBetaScaleHomogeneity = STRUCTURAL EVIDENCE ONLY`.

It does not close `BetaIndexSemantics`.

## 8. Domain and background dependence should not be reintroduced through notation

The source audit for CMP119 records the regular domains and analytic spaces used to control `E^(j)`, `R^(j)`, and `B^(j)`.

Those structures are essential to the proof.

But proof parameters used to establish that a beta coefficient exists and is bounded are not automatically function arguments of the coefficient itself.

R74 therefore imposes the following typing guardrail:

`proof dependence != functional dependence`.

In particular, one may not infer a cross-depth beta mismatch merely because the proof of `beta_j` uses scale-dependent domains, propagators, or analytic collars.

To create a scalar mismatch one needs evidence that the **value of the extracted coefficient** changes after aligned physical-scale identification.

## 9. The fallback mismatch problem is now one-dimensional in hidden data

If interpretation C is correct, write

`B_(N,j)(x)=mathfrak B(a_(N,j),x,h_(N,j))`

where `h_(N,j)` is the residual hidden absolute-depth datum.

Then at aligned scales

`delta B_(N,j)`

`= mathfrak B(a,x,h_(N+1,j+1)) - mathfrak B(a,x,h_(N,j))`.

If `mathfrak B` is Lipschitz in `h`,

`|delta B_(N,j)| <= C_h |delta h_(N,j)|`.

Thus R72's summable-mismatch route reduces further to:

`SummableHiddenBetaDatumShift => SummableBetaMapShiftDefect`.

The difficult part would be identifying a genuine `h` at all.

No such independent datum is presently source-visible.

## 10. Consequence for the stable-fiber fallback

R63's generic stable graph allowed arbitrary complementary coordinates to feed the marginal coordinate.

R73 eliminated the need for that formulation on the canonical generated family.

R74 makes the simplification stronger:

- no explicit complete-density coordinate is a source-visible beta argument;
- boundary localization is external through `phi_j`;
- only the index `j` remains to be interpreted.

Therefore the full stable-fiber theorem is now a **third-line fallback**, needed only if primary source recovery shows that `j` encodes genuine history not determined by the aligned physical scale and that this history is not otherwise summably controlled.

## 11. Determination

R74 establishes:

1. In the source-attested CMP119 canonical coordinates, the explicit beta-function argument list is `{j,g}`.
2. Finite-volume/domain sequences, large-field history, background fields, and inherited E/R/B/V coordinates are not displayed as independent beta arguments.
3. Position/domain localization is externalized by `phi_j`, which equals one on the common bulk interior.
4. Therefore the entire hidden-parameter problem collapses to the meaning of the scale index `j`.
5. If `j` is only a rescaled RG-step label, the bulk beta map is autonomous.
6. If `j` encodes only physical scale, R70's exact aligned-scale identity still gives exact cross-depth shift covariance.
7. Only an absolute-depth/history interpretation of `j` can create a genuine canonical scalar mismatch.
8. The accessible primary-source extraction does not yet decide among these interpretations.
9. Proof dependence on scale-dependent domains or background-field machinery must not be confused with functional dependence of the beta coefficient.
10. The native scalar frontier is therefore reduced to a single source question: `BetaIndexSemantics`.

Canonical state:

`SourceVisibleBetaArguments = {j,g}`.

`DirectFiniteVolumeBetaArgument = ABSENT IN CANONICAL REPRESENTATION`.

`DirectDomainBetaArgument = ABSENT IN CANONICAL REPRESENTATION`.

`DirectInheritedActivityBetaArgument = ABSENT IN CANONICAL REPRESENTATION`.

`BulkBetaBoundaryDependence = SEPARATED VIA phi_j / B-SECTOR`.

`PhysicalScaleLocalityOfBeta => NativeBetaMapShiftCovariance = DERIVED`.

`BetaIndexSemantics = LIVE PRIMARY-SOURCE GATE`.

`GeneralProjectionTriangularity = OPEN but non-default`.

`PrimaryEq029PositiveAlphaBound = independently OPEN`.

## Negative results / guardrails

- Do not treat every parameter occurring in the proof of beta-function existence as an argument of the beta function.
- Do not infer finite-volume or domain dependence of `beta_j` merely because the full effective action depends on those objects.
- Do not infer autonomy solely from the compact notation `beta_j(g)`; the index may still hide absolute-depth data.
- Do not require `beta_j` to be independent of physical scale: physical-scale dependence is compatible with exact cross-depth covariance because aligned scales are equal.
- Do not use secondary `2 b_0 log L + O(g^2)` formulas as exact source custody for the full beta family.
- Do not infer continuum Yang–Mills existence or a positive mass gap from scalar autonomy.

## Next frontier — YM-R75

`YM-R75 — beta-index semantics / physical-scale stationarity audit.`

Tasks:

1. recover the Paper-I definitions surrounding the indexed beta-functions and identify exactly what the index `j` parameterizes;
2. determine whether the one-step beta extraction is formulated after rescaling to a fixed dimensionless lattice problem;
3. test whether `beta_j^(N)` factors through the physical scale `a_(N,j)` or is actually independent of `j`;
4. if an absolute-depth datum remains, name it explicitly and derive its aligned cross-depth difference;
5. retain primary Eq. (0.29) custody as the independent regular-sector gate.

Highest cumulative reference remains [85]; [86] remains next.
