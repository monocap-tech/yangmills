# YM-R72 — beta-map shift covariance / cross-depth mismatch summability audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R73` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R71, which reduced exact cross-depth marginal-tail coherence to exact equality of the aligned scalar one-step maps.

R72 asks whether that equality is actually needed, what part of the beta law can differ between cutoff depths, and what quantitative mismatch theorem would be sufficient if exact cocycle covariance is unavailable.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. Split the beta increment into universal bulk part and cross-depth remainder

On the common interior, CMP119 has `phi_j=1`, so write the inverse-square recursion abstractly as

`x_j = x_(j-1) - B_(N,j)(x_(j-1))`,

where `x=g^-2` and the explicit cutoff-depth label `N` is restored for the cross-cutoff audit.

The secondary locator [85] v2 summarizes the weak-coupling flow as

`g_(k+1)^-2 = g_k^-2 + 2 b_0 log L + O(g_k^2)`

in its convention.

For cross-depth purposes the useful decomposition is therefore

`B_(N,j)(x) = B_univ(x;L) + r_(N,j)(x)`,

where `B_univ` contains every term known to be the same local bulk law at aligned scales, and `r_(N,j)` contains only data whose equality across regulator depths has not been established.

Define the aligned shift defect

`delta r_(N,j)(x) := r_(N+1,j+1)(x) - r_(N,j)(x)`.

Because R70 proved

`a_(N+1,j+1)=a_(N,j)`,

the universal bulk contribution cancels exactly in the comparison if it depends only on the aligned physical scale, `g`, and fixed block factor `L`.

Thus the actual scalar obstruction is not the beta function itself but

`BetaRemainderCrossDepthDifference := delta r_(N,j)`.

## 2. Important negative result: `O(g^2)` is not a cross-depth error estimate

The displayed perturbative law

`B = 2 b_0 log L + O(g^2)`

is an absolute approximation to one beta map.

It does **not** imply

`B_(N+1,j+1)-B_(N,j) = O(g^2)`

and certainly does not imply that the difference tends to zero with `N`.

This matters near the fixed endpoint scale, where

`g_j^(N) -> g_*`

for the last finitely many common steps and `g_*` is fixed rather than tending to zero.

Therefore the asymptotic freedom statement

`g_0^(N) -> 0`

cannot be used to make an arbitrary `O(g^2)` beta remainder summable across the entire aligned tail.

Canonical guardrail:

`AbsoluteBetaRemainderSmallness != CrossDepthBetaMapMismatchSmallness`.

## 3. Exact covariance is the zero-defect special case

R71's exact cocycle condition is simply

`delta r_(N,j)=0`

for every aligned common step.

Together with the common endpoint and backward uniqueness, this gives exact tail nesting.

Thus

`NativeBetaMapShiftCovariance`

is the special case

`BetaRemainderCrossDepthDifference = 0`.

No stronger machinery is hidden here.

## 4. Minimal scalar stability theorem for a nonzero shift defect

Let the aligned forward maps be

`F_(N,j)(x)=x-B_(N,j)(x)`.

Suppose each inverse map on the weak corridor is Lipschitz with constant `lambda_j >= 1` in the relevant orientation.

Set

`delta x_j := x_(j+1)^(N+1) - x_j^(N)`.

Because the endpoints agree,

`delta x_N=0`.

Backward comparison gives the schematic estimate

`|delta x_(j-1)|`

`<= lambda_j ( |delta x_j| + ||delta r_(N,j)||_infty )`.

Iteration yields

`|delta x_j|`

`<= sum_(m=j+1)^N [ product_(r=j+1)^m lambda_r ] ||delta r_(N,m)||_infty`.

Classification: DERIVATION.

Hence exact map equality is unnecessary. It is sufficient that the cross-depth map defect, after amplification by inverse sensitivity, be summable.

Canonical fallback:

`SummableBetaMapShiftDefect + BackwardInverseStability`

`=> SummableMarginalTailMismatch`.

## 5. Polynomial inverse sensitivity is harmless against a geometric UV defect

Suppose the inverse sensitivity across `N` common steps grows at most polynomially,

`sup_(j<m<=N) product_(r=j+1)^m lambda_r <= C N^p`,

and suppose the aligned beta-map defect obeys a source-depth estimate

`||delta r_(N,j)||_infty <= C' L^(-alpha N) w_j`,

with `alpha>0` and `sum_j w_j <= C_w N^q` at worst polynomially.

Then

`sup_j |delta x_j| <= C'' N^(p+q) L^(-alpha N)`.

Therefore

`sum_N sup_j |delta x_j| < infinity`.

The geometric ultraviolet factor dominates any fixed polynomial loss.

This is a DERIVATION, not a source theorem.

It identifies the exact quantitative strength needed from a nonzero beta-map mismatch.

## 6. Where could the cross-depth mismatch come from?

At aligned physical scales, the following are already common or separated:

- the lattice spacing is exactly common by R70;
- the block factor `L` is fixed;
- `phi_j=1` on the common bulk interior by CMP119;
- boundary/domain effects are assigned to the B/boundary sector.

Therefore any residual bulk `delta r_(N,j)` must come from one of two possibilities:

1. the native beta extraction retains genuine dependence on regulator-depth data not removed by physical-scale alignment; or
2. the inherited extra ultraviolet irrelevant activity from the depth-`N+1` theory feeds back into the local marginal extraction at later steps.

The second possibility is exactly the marginal-leakage issue first isolated in R62/R63.

Thus R72 identifies the next native object:

`MarginalLeakageFromExtraUVResidual`.

## 7. The source architecture points toward zero leakage, but does not yet prove it at the required level

CMP119 writes the running coupling through a scalar recursion `beta_j(g_(j-1))` and stores the regular residual separately after subtracting the beta/Wilson direction.

This source grammar strongly suggests that, on the canonical generated class, the beta map is intended to depend on the running coupling and scale data rather than on arbitrary E/R/B coordinates.

If that reading is exact, then inherited irrelevant activity does not modify later beta maps and

`MarginalLeakageFromExtraUVResidual = 0`,

which would give exact bulk shift covariance after the index shift.

But R64 already established the necessary caution: syntactic triangularity of the declared coordinates does not prove the Banach-map identity `D_K T_x=0` for arbitrary perturbations.

The present cross-depth pair is more special than an arbitrary perturbation, but a source theorem is still needed before zero leakage can be promoted.

Canonical status:

`CanonicalBulkMarginalLeakageZero = PLAUSIBLE SOURCE READING / NOT YET EXTRACTED`.

## 8. If leakage is nonzero, the positive-alpha route gives the natural candidate bound

R68-R70 isolated the candidate Paper-I irrelevance estimate for the extra ultraviolet regular residual:

`||V_(N+1)^(1)(X)|| <= C L^(-N(4+alpha)) exp(-kappa d(X))`, `alpha>0`,

conditional on primary Eq. (0.29) custody.

After four-dimensional rooted summation in a fixed region, this becomes

`O(L^(-alpha N))`.

If the beta-extraction functional is locally Lipschitz with respect to that inherited residual, uniformly along the weak trajectory, then the induced cross-depth beta-map defect would inherit the same source-depth factor:

`||delta r_(N,j)|| <= C_j L^(-alpha N)`.

If the accumulated `C_j` growth is at most polynomial, Section 5 then makes the entire marginal tail mismatch summable.

This gives the conditional chain

`PrimaryEq029PositiveAlphaBound`

`+ BoundedMarginalExtractionOnInheritedV`

`+ PolynomialBackwardSensitivity`

`=> SummableMarginalTailMismatch`.

Classification: DERIVATION / THEOREM TARGET.

None of the three source-native hypotheses is promoted here beyond its current custody status.

## 9. Why the endpoint does not spoil this argument

The absolute coupling near the endpoint is fixed at `g_*`, so absolute perturbative corrections there need not shrink with `N`.

But a cross-depth mismatch induced by the **single extra ultraviolet source contribution** can still carry the source-depth factor `L^(-alpha N)` all the way through the bookkeeping if the source-labelled residual retains its UV provenance and the marginal extraction is stable with respect to it.

Thus the relevant small quantity is not

`g_*^2`,

but

`memory of the extra ultraviolet layer`.

This is the same conceptual distinction that R65-R70 established for the regular E sector.

## 10. Source status of the beta law

CMP109 [7] is verified to construct beta-functions and define coupling renormalization by recursive RG equations.

CMP119 [59] source-attests the localized scalar recursion used in the complete-density induction.

Reference [85] v2 provides a secondary equation-level traceability claim for the weak-coupling law

`g_(k+1)^-2 = g_k^-2 + 2 b_0 log L + O(g_k^2)`

and explicitly labels its package conditional on faithful transcription of the primary Bałaban/Dimock sources.

The present source corpus still does not provide a primary equation-level theorem saying either

`r_(N+1,j+1)=r_(N,j)`

or

`||r_(N+1,j+1)-r_(N,j)|| <= C L^(-alpha N)`.

Therefore exact and summable beta-map covariance both remain source obligations.

## 11. Determination

R72 establishes:

1. On the common bulk interior, the aligned beta increment can be split into a universal scale-homogeneous part and an unverified cross-depth remainder.
2. The universal part cancels under physical-scale alignment; the scalar obstruction is the difference of the remainder maps, `delta r_(N,j)`.
3. An absolute `O(g^2)` correction to one beta map is not a cross-depth mismatch estimate and does not become small near a fixed weak endpoint merely because the bare UV coupling tends to zero.
4. Exact shift covariance is the special case `delta r=0`.
5. A nonzero but summable shift defect is sufficient: backward inverse stability converts it into a summable marginal-tail mismatch.
6. Any geometric source-depth factor `L^(-alpha N)`, `alpha>0`, survives polynomial inverse-map amplification and remains summable.
7. The only plausible bulk origins of a nonzero shift defect are genuine cutoff-depth dependence of the beta extraction or marginal leakage from the inherited extra-UV irrelevant residual.
8. CMP119's declared coordinate grammar points toward zero canonical leakage but does not yet source-prove the required cross-depth statement.
9. Conditional on the candidate positive-alpha Paper-I bound and a bounded marginal extraction functional, any nonzero leakage from the extra UV residual would naturally inherit a summable `L^(-alpha N)` factor.

Canonical state:

`UniversalLeadingBetaIncrement = SCALE-HOMOGENEOUS at secondary-locator level`.

`AbsoluteO(g^2)Remainder = NOT A CROSS-DEPTH ERROR BOUND`.

`NativeBetaMapShiftCovariance = OPEN`.

`BetaRemainderCrossDepthDifference = LIVE PRECISE OBJECT`.

`SummableBetaMapShiftDefect => SummableMarginalTailMismatch = DERIVED`.

`CanonicalBulkMarginalLeakageZero = NOT YET SOURCE-EXTRACTED`.

`PositiveAlphaResidual + bounded marginal leakage map = LIVE FALLBACK ROUTE`.

## Negative results / guardrails

- Do not use the absolute `O(g^2)` beta remainder as if it were the difference between two cutoff-depth beta maps.
- Do not use `g_0^(N)->0` to control the last common RG steps, where the coupling approaches the fixed endpoint `g_*`.
- Do not infer exact shift covariance from the absence of an explicit `N` label in published notation.
- Do not mix `phi_j` boundary localization effects into the bulk beta-map comparison when `phi_j=1` on the common interior.
- Do not infer zero marginal leakage from coordinate syntax alone.
- Do not promote the candidate positive-alpha leakage bound before primary Eq. (0.29) and the beta-extraction functional are directly sourced.
- Do not infer continuum Yang-Mills existence or a mass gap from marginal-tail summability.

## Next frontier — YM-R73

`YM-R73 — marginal leakage from source-labelled V / beta-extraction dependence audit.`

Tasks:

1. recover from Paper I whether `beta_j` is defined solely from the fresh one-step local fluctuation functional or can depend on inherited regular activities;
2. determine whether the scale-labelled residual `V^(1)` can contribute to later beta extractions;
3. if it can, derive the precise bounded projection/Lipschitz estimate from the analytic jet norm into the Wilson-action coefficient;
4. combine that projection estimate with the candidate positive-alpha source-depth bound to test `||delta r_N|| = O(L^-alpha N)`;
5. retain exact shift covariance as the zero-leakage branch and the full stable-fiber theorem as the final fallback.

Highest cumulative reference remains [85]; [86] remains next.
