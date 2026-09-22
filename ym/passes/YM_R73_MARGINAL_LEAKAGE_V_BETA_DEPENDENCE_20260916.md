# YM-R73 — marginal leakage from source-labelled V / beta-extraction dependence audit

Lineage date: 2026-09-16
Audit continuation: 2026-09-22
Status: COMPLETE
Next cursor: `YM-R74` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R72, which isolated the aligned cross-depth beta-family defect

`delta r_(N,j) = r_(N+1,j+1) - r_(N,j)`

and left two possible explanations for a nonzero bulk defect:

1. genuine cutoff-depth / history dependence of the indexed beta family; or
2. explicit marginal leakage from the inherited extra-UV irrelevant residual `V^(1)`.

R73 asks whether these are genuinely distinct native source objects.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. CMP119 separates the scalar beta family from the accumulated regular history

The source-verified CMP119 Sect. 2 representation writes the localized running coupling in the form

`1/g_(j-1)^2(x) = 1/g_j^2(x) + beta_j(g_(j-1)) phi_j(x)`.

The same source section writes the accumulated regular coordinate schematically as

`E_k(U_k) = sum_(j=1)^k [`

`  E^(j)(Lambda_j,g_(j-1),U_k)`

`  - E^(j)(Lambda_j,g_(j-1),1)`

`  - beta_j(g_(j-1)) A(phi_j,U_k) ]`.

The important type information is therefore:

- the scalar coefficient at source scale `j` is written `beta_j(g_(j-1))`;
- the scale-`j` regular contribution is separately retained in the accumulated `E_k`;
- no earlier regular coordinate `E_i`, `V_i`, `R_i`, or `B_i` appears as an explicit argument of the displayed scalar beta map.

Classification:

`CanonicalDeclaredBetaArguments = {scale/index data, running coupling}`.

`InheritedRegularHistory = STORED SEPARATELY IN E_k`.

This is a source-representation statement, not a Banach-map derivative theorem.

## 2. The canonical source construction does not define a separate V-to-beta feedback variable

Suppose a source-labelled irrelevant residual `V^(i)` is generated at an earlier ultraviolet scale.

In the published CMP119 bookkeeping, that contribution persists as part of the scale-labelled regular history inside `E_k`. The later scalar recursion is still written with the indexed function `beta_j(g_(j-1))`.

Therefore the native canonical construction does not present an update of the form

`beta_j = Beta_j(g_(j-1), V^(1),...,V^(j-1))`.

Consequently there is no source-native independent coordinate

`MarginalLeakageFromExtraUVResidual`

whose norm must be estimated in addition to the beta-family comparison.

Any dependence of the later marginal coefficient on earlier history must already be encoded implicitly in which indexed function `beta_j` the canonical construction assigns at that scale.

Canonical retyping:

`MarginalLeakageFromExtraUVResidual`

`= NOT AN INDEPENDENT NATIVE COORDINATE ON THE CANONICAL GENERATED FAMILY`.

Its possible effect is absorbed into

`BetaFamilyNonautonomy / BetaRemainderCrossDepthDifference`.

This is the principal result of R73.

## 3. Why this does not prove general triangularity

R64 correctly distinguished source-coordinate triangularity from the much stronger statement

`D_K T_x = 0`

on an open Banach neighborhood of arbitrary complete densities.

R73 does not reverse that guardrail.

If one takes an arbitrary complete density with the same coupling but modifies its complementary activity by `delta V`, then performs a fresh exact RG step and re-extracts the Wilson coefficient, the new coupling could in principle change.

That problem asks for a map

`D_V beta`

or a nonlinear Lipschitz estimate for the extraction functional.

CMP119's canonical representation does not supply such a theorem merely because its generated beta sequence is written without an explicit `V` argument.

Therefore:

`GeneralProjectionTriangularity = still OPEN`.

But the N-versus-(N+1) cutoff comparison need not be reformulated as an arbitrary off-manifold perturbation if both sides are kept in their native canonical generated representations.

## 4. The apparent V-feedback problem becomes beta-family shift covariance

At the first common physical scale, the depth-`N+1` construction carries one extra source-labelled residual absent from the depth-`N` bare theory.

There are two possible descriptions.

### Description A — native canonical comparison

Compare the two complete canonical generated trajectories directly.

Then the scalar objects are

`beta_(N,j)`

and

`beta_(N+1,j+1)`.

Any effect of the extra UV history on the scalar law is, by definition of this representation, part of the difference between these indexed beta functions.

The obstruction is exactly R72's

`delta r_(N,j)`.

### Description B — synthetic perturbation comparison

Identify the depth-`N+1` common-scale density as

`depth-N reference density + V perturbation`

and then evolve both using one common nonlinear RG map.

This formulation requires a derivative / Lipschitz theorem from `V` into the marginal coefficient.

Description B is mathematically legitimate but is a stronger, synthetic stable-fiber formulation. It is not the minimal source-native representation of the cutoff comparison.

Hence the project should prefer Description A until source evidence forces otherwise.

## 5. Source-scale provenance still matters even though there is no explicit feedback coordinate

Eliminating a separate `V -> beta` variable does not make the extra UV residual irrelevant to the whole construction.

The residual still contributes to:

- the regular `E` sector;
- fixed-observable endpoint defects;
- possibly the indexed value of the canonical beta family through whatever historical construction defines `beta_j`.

R68-R70 showed conditionally that a Paper-I positive-alpha bound of type

`||V_(N+1)^(1)(X)|| <= C L^(-N(4+alpha)) exp(-kappa d(X))`

would yield a fixed-region regular defect

`O(L^(-alpha N))`.

R73's point is only that a **second independent projection estimate** from this `V` into beta is not automatically required in the canonical formulation.

The remaining scalar question is instead whether the indexed beta family itself is shift-covariant or has a summably small cross-depth defect.

## 6. The beta family's hidden dependencies are now the exact source target

The notation

`beta_j(g)`

suppresses whatever data were used to construct the function at source scale `j`.

Possible hidden data include:

- localization domains / finite-volume geometry;
- scale-indexed background-field conventions;
- historical choices entering the Paper-I recursive construction;
- boundary modifications, though CMP119's `phi_j=1` removes the explicit cutoff multiplier in the common bulk interior.

The source-verified CMP119 formula is therefore enough to exclude an explicit independent `E/R/B` argument, but not enough to prove

`beta_(N+1,j+1) = beta_(N,j)`

after physical-scale alignment.

Thus the scalar source gate is not a generic marginal-leakage theorem.

It is:

`NativeBetaFamilyHiddenParameterAudit`.

Equivalently:

`Which suppressed parameters, besides g and fixed L, actually distinguish beta_j?`

## 7. A perturbative beta remainder is still not a history-dependence bound

Secondary source [85], and another secondary traceability manuscript inspected during R73, describe a weak-coupling beta function analytic in `g^2`, with a universal leading coefficient and an absolute remainder of order `g^2`.

This does not answer the present question.

Even if

`beta_j(g) = b_0 + O(g^2)`

uniformly in `j`, two different indexed functions can both satisfy this estimate while differing by an `O(g^2)` amount that does not vanish with cutoff depth.

The cross-depth quantity remains

`beta_(N+1,j+1)(g) - beta_(N,j)(g)`,

not either function's absolute distance from `b_0`.

Therefore R72's guardrail remains intact.

## 8. Abstract fallback if one insists on the perturbation picture

Although the native route does not require it, R73 records the minimal analytic theorem that would control explicit V-to-beta leakage.

Let `Loc_A` denote the local extraction functional producing the Wilson-action coefficient from an analytic local activity.

If on a common analytic collar

`|Loc_A(F)-Loc_A(G)| <= C_Loc ||F-G||_an`

with `C_Loc` uniform along the weak trajectory, then

`|delta beta| <= C_Loc ||delta V||_an`.

If the inherited source-labelled residual satisfies

`||delta V||_an <= C L^(-alpha N)`

after the fixed-region/root normalization appropriate to the extraction, then

`|delta beta| <= C' L^(-alpha N)`.

Combined with R72's backward inverse stability, this makes the marginal-tail mismatch summable even if explicit leakage exists.

Classification:

`BoundedMarginalExtractionOnV + PositiveAlphaVBound => SummableBetaLeakage`

is an ABSTRACT DERIVATION.

The source-native hypotheses remain unextracted, so this is fallback only.

## 9. The canonical route is strictly cheaper than the stable-fiber route

The hierarchy is now:

### Native canonical route

1. compare the indexed beta families directly;
2. prove exact shift covariance or a summable cross-depth beta-family defect;
3. separately use the source-scale irrelevance estimate for the regular `V` sector.

### Synthetic stable-fiber route

1. identify both theories in one Banach chart at the common scale;
2. measure the extra UV residual as a perturbation `delta V`;
3. bound `D_V beta` and the transverse update;
4. solve the mixed-boundary/stable-graph problem if required.

The second route remains a safe fallback but is no longer the default theorem burden.

Canonical determination:

`CanonicalCrossCutoffScalarProblem = BetaFamilyShiftDefect`.

`ExplicitVToBetaLeakageEstimate = OPTIONAL FALLBACK, NOT INDEPENDENT NATIVE RESIDUE`.

## 10. What source evidence would close the scalar branch

Any one of the following would suffice.

### Exact autonomy

A primary Paper-I statement showing that, after scale identification, `beta_j` is the same function of `g` and fixed block factor `L` at every bulk step.

Then

`delta r_(N,j)=0`

and R71 gives exact tail coherence.

### Summable hidden-parameter defect

A theorem showing

`sup_g |beta_(N+1,j+1)(g)-beta_(N,j)(g)| <= C L^(-alpha N) w_j`

with `alpha>0` and at most polynomially summable `w_j`.

Then R72 gives summable marginal mismatch.

### Off-manifold projection control

A uniform analytic estimate from inherited `V` into the Wilson coefficient, together with the positive-alpha source-scale bound.

This is sufficient but stronger than the first two.

## 11. Determination

R73 establishes:

1. CMP119 source-attests a canonical representation in which the running beta coefficient is written as an indexed scalar function of the running coupling, while all previously generated regular contributions remain separately stored in the scale-labelled `E_k` sum.
2. Consequently, on the canonical generated family, there is no independent source coordinate representing `V -> beta` feedback.
3. Any influence of ultraviolet history on later canonical beta values is already encoded in the indexed beta family itself and is therefore part of R72's cross-depth beta-family defect.
4. This does not prove general Banach-map triangularity `D_K T_x=0`; arbitrary off-manifold perturbations may still require a marginal-extraction derivative theorem.
5. For the actual N-versus-(N+1) canonical cutoff comparison, the cheaper native target is exact or summable shift covariance of the beta family.
6. A bounded analytic projection from `V` to the Wilson coefficient remains a valid fallback. Conditional on a positive-alpha `V` estimate, it would inherit the same geometric source-depth suppression.
7. The live source question is now which hidden parameters enter `beta_j` beyond `g`, fixed `L`, and aligned physical scale.

Canonical state:

`CanonicalDeclaredBetaArguments = scalar coupling + suppressed scale/history data`.

`ExplicitInheritedVArgumentInBeta = ABSENT IN SOURCE REPRESENTATION`.

`MarginalLeakageFromExtraUVResidual = RETYPED INTO BetaFamilyCrossDepthDifference on canonical family`.

`GeneralProjectionTriangularity = OPEN`.

`BoundedMarginalExtractionOnV = FALLBACK / OPEN`.

`NativeBetaFamilyHiddenParameterAudit = LIVE`.

`PrimaryEq029PositiveAlphaBound = independently OPEN`.

## Negative results / guardrails

- Do not create a separate canonical `V -> beta` obstruction when the native representation already encodes all history dependence inside the indexed beta family.
- Do not promote absence of an explicit `V` argument to the Banach derivative identity `D_V beta=0`.
- Do not use an absolute `O(g^2)` beta remainder as a cross-depth beta-family mismatch bound.
- Do not assume the suppressed scale index carries no hidden domain/history data.
- Do not use the synthetic stable-fiber chart when a cheaper source-native canonical comparison is available.
- Do not infer continuum Yang–Mills existence or a mass gap from closure of the scalar branch.

## Next frontier — YM-R74

`YM-R74 — beta-family hidden-parameter / autonomy audit.`

Tasks:

1. recover from Paper I and the CMP119 inheritance exactly what `beta_j` depends on besides `g`;
2. separate bulk-local quantities from finite-volume/domain/boundary data;
3. decide whether aligned physical scale plus fixed `L` makes the canonical bulk beta family autonomous;
4. if not, identify the hidden-parameter difference and test whether it is source-scale suppressed;
5. keep primary Eq. (0.29) custody as the independent regular-sector gate.

Highest cumulative reference remains [85]; [86] remains next.
