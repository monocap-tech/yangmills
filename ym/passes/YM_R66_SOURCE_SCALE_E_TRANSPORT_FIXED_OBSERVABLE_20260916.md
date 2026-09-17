# YM-R66 — source-scale E transport / fixed-observable ultraviolet-memory audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R67` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R65, which showed that the extra ultraviolet layer is not source-attested to vanish in the raw complete-density norm: the `R` sector carries an explicit positive power of the ultraviolet coupling, while the regular `E` and boundary `B` amplitudes are only uniformly small/bounded in the presently extracted source norms.

R66 asks whether the explicit source-scale provenance

`E_k = sum_j E^(j)`

contains enough scale-transfer structure for an `E^(j)` contribution born arbitrarily far in the ultraviolet to become invisible at a fixed physical scale or to fixed gauge-invariant observables, even if its native same-scale amplitude remains `O(E_0)`.

Repeated sources: [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [68] Curci–Menotti–Paffuti / Symanzik dimension-six pure-gauge control source.
No new bibliography item is consumed. Highest remains [84].

Source-extraction note: an auxiliary public source-audit corpus with locators to locally rendered CMP116/CMP119 primary pages was used only to target the formulas attributed below to the primary papers. It is not assigned a project bibliography number.

## 1. The regular coordinate retains scale-of-origin provenance

CMP119 Eq. (2.25) has the source-normalized form

`E_k(U_k) = sum_{j=1}^k [`

`  E^(j)(Lambda_j,g_{j-1},U_k)`

`  - E^(j)(Lambda_j,g_{j-1},1)`

`  - beta_j(g_{j-1}) A(phi_j,U_k) ]`.

Thus the complete regular action is not stored as an undifferentiated scalar norm. Each contribution retains a source index `j`, its source localization domain, its source coupling, and its vacuum/marginal subtraction.

This makes a scale-separated audit meaningful: a contribution can be `O(E_0)` in its own inductive norm while carrying geometric information about how many blocking steps separate its birth scale from the fixed endpoint.

Canonical fact:

`RegularScaleProvenance = SOURCE-ATTESTED`.

## 2. CMP116 supplies a genuine one-step metric scale gain

The localization estimates in CMP116 contain an explicit fine-to-coarse geometric comparison.

In the source notation surrounding Eq. (2.36), a fine-scale connected component `Z_i` determines a coarse component `Z_i'`, and the source gives

`2 d_k(Z_i) >= L d_{k+1}(Z_i')`.

Equivalently,

`d_k(Z_i) >= (L/2) d_{k+1}(Z_i')`.

This is not merely a change of notation: it is the geometric resource used in the cluster proof to transfer exponential localization from scale `k` to scale `k+1`.

Combined with a source-scale bound

`|E(X)| <= E_0 exp(-kappa d_k(X))`,

one obtains, for a component to which the comparison applies,

`|E(X_k)| <= E_0 exp[-kappa (L/2) d_{k+1}(X_{k+1})]`.

CMP116 spends most of this gain in restoring the next-scale inductive decay exponent after the cluster/resummation losses; it does not state this as cross-cutoff convergence.

Canonical classification:

`OneStepLocalizationMetricGain = SOURCE-ATTESTED`.

## 3. Iterating the metric gain isolates the extended sector

Abstractly suppose a source component has a descendant chain

`X_j -> X_{j+1} -> ... -> X_k`

for which the CMP116-type scale-transfer comparison is valid at every common RG step:

`d_r(X_r) >= (L/2) d_{r+1}(X_{r+1})`.

Then iteration gives

`d_j(X_j) >= (L/2)^(k-j) d_k(X_k)`.

Therefore the original source bound yields

`|E^(j)(X_j)|`

`<= E_0 exp[-kappa (L/2)^(k-j) d_k(X_k)]`.

For every endpoint component with

`d_k(X_k) >= 1`,

the right-hand side tends to zero faster than an ordinary geometric sequence as the source/endpoint scale separation `k-j` grows.

This is a DERIVATION conditional on a coherent descendant/component dictionary across repeated RG steps. The source explicitly supplies the one-step inequality; the project does not yet possess a theorem identifying arbitrary CMP119 `E^(j)` descendants across all later steps.

Canonical object:

`ExtendedEGeometricTransport`.

Status:

`SOURCE-ATTESTED ONE STEP / ITERATION DICTIONARY OPEN`.

## 4. Localization geometry does not suppress a collapsed local component

The previous estimate has a decisive exception.

The tree-distance/localization metric measures spatial/polymer extent. A component that has collapsed into a single endpoint localization block can have

`d_k(X_k) = 0`

(or the corresponding minimal metric value in the exact source convention).

Then

`d_j(X_j) >= (L/2)^(k-j) * 0`

contains no scale-separation information at all.

So exponential polymer locality cannot by itself prove that an **ultra-local** UV operator disappears under repeated coarse graining.

This prevents a false inference:

`fine-to-coarse metric gain`

`does not imply`

`all source-scale E increments vanish at fixed endpoint`.

Canonical negative result:

`LocalizationMetricAloneKillsLocalUVJet = FALSE`.

The live `E` residue is therefore concentrated in the collapsed local jet.

## 5. The local residue is exactly where marginal extraction matters

For each fresh regular contribution CMP119 explicitly removes

1. the field-independent value `E^(j)(...,1)`, and
2. the designated Wilson-action term `beta_j A(phi_j,U)`.

If the still-open Paper-I extraction theorem establishes that this is the exact local projection onto the vacuum and CP-even dimension-four pure-gauge directions, then the residual local jet has neither of those components.

Gauge invariance excludes a gauge-boson mass term. In the real/reflection-even pure-gauge sector, the remaining generic local operators begin at canonical dimension six once the vacuum and `tr F^2` directions are removed; [68] is retained only as a control source for this standard dimension-six classification.

For a local operator of canonical dimension `d=6` in four dimensions, one blocking/rescaling step carries the engineering factor

`L^(4-d) = L^-2`.

Hence the expected local scale-separated law is

`||E_local,res^(j) transported to scale k||`

`<= C L^(-2(k-j)+weak anomalous correction) ||E_local,res^(j)||`.

This is a DERIVATION from exact marginal/vacuum orthogonality plus canonical local scaling. It is **not** installed as a Bałaban theorem.

Canonical object:

`CollapsedLocalEJetIrrelevance`.

Status:

`STRUCTURALLY IDENTIFIED / NATIVE THEOREM OPEN`.

## 6. R66 therefore splits ScaleSeparatedETransport into two species

The R65 object

`ScaleSeparatedETransport`

is no longer monolithic.

It decomposes into:

### A. Extended/polymer part

Controlled by source localization geometry:

`d_j >= (L/2)^(k-j) d_k`.

For positive endpoint diameter this gives very strong scale-separation suppression, conditional on a repeated-step descendant dictionary.

### B. Collapsed local part

Not controlled by polymer diameter. It requires the local Taylor/extraction theorem:

`vacuum + F^2 removed`

`=> residual local jet begins at dimension >= 6`

`=> L^-2 per scale at tree level`.

Thus the exact remaining theorem burden is much smaller than “prove the whole E sector contracts.”

Canonical retyping:

`ScaleSeparatedETransport`

`= ExtendedEGeometricTransport + CollapsedLocalEJetIrrelevance`.

## 7. Fixed-observable topology can be weaker than native-density Cauchy

Fix a finite physical reference volume and a bounded cylindrical gauge-invariant observable `F` on the endpoint lattice.

Suppose the depth-`N` and depth-`N+1` constructions have been put on the same endpoint configuration space and their normalized endpoint actions differ by `delta S_N` with

`||delta S_N||_infty <= epsilon_N`.

Let

`d nu_N / d mu_N = exp(-delta S_N) / <exp(-delta S_N)>_{mu_N}`.

Then

`exp(-2 epsilon_N) <= d nu_N/d mu_N <= exp(2 epsilon_N)`,

and therefore

`| <F>_{nu_N} - <F>_{mu_N} |`

`<= ||F||_infty (exp(2 epsilon_N)-1)`.

Consequently, if the transported extra-UV-layer endpoint defect satisfies

`sum_N epsilon_N < infinity`,

then every fixed bounded endpoint observable has a Cauchy expectation sequence.

Classification: DERIVATION at fixed finite endpoint volume. This is a sufficient observable-level criterion; it is not a source theorem and it does not address the thermodynamic limit or OS reconstruction by itself.

The significance is conceptual:

`CompleteDensityNativeNormCauchy`

is stronger than necessary. It suffices to make the **transported endpoint action defect** summable in a topology that controls the chosen observable family.

## 8. But fixed-observable locality does not remove the local-jet problem for free

One might hope that a UV component is spatially far from a fixed observable and hence harmless. That is not the generic cross-cutoff situation.

A new ultraviolet interaction can lie inside the same physical region as the endpoint observable; it is separated by **scale**, not necessarily by physical distance.

Therefore ordinary spatial polymer decay suppresses components whose coarse images have nonzero diameter or lie away from the observable, but it does not suppress a local operator inserted at the same physical point.

The local component still requires canonical irrelevance / Taylor-order control.

Using an IR clustering or mass-gap estimate here would also be circular for the eventual Clay objective, so R66 does not use it.

Canonical guardrail:

`SpatialLocality != ScaleIrrelevance`.

## 9. What the published source does and does not currently supply

Source-attested:

- regular contributions retain source index `j` inside `E_k` [59];
- vacuum and the prescribed `beta_j A` term are subtracted from each stored regular contribution [59];
- fresh regular activities satisfy localized exponential bounds [7,21,59];
- CMP116 Eq. (2.36) gives the one-step metric scale-transfer inequality `2 d_k >= L d_{k+1}` [21].

Not yet source-custodied as a Yang–Mills theorem:

- an iterated descendant map for an arbitrary `E^(j)` contribution through all later RG layers;
- an exact Paper-I projector identity proving the stored local residual has zero vacuum and zero `F^2` projection in the perturbative/Banach sense needed here;
- a source-native Taylor-order theorem saying the collapsed residual local jet starts at dimension six;
- a source-native `L^-2` (or `L^-eta`) difference/transport estimate for that local residual;
- summability of the complete transported endpoint action defect across cutoff depths.

Thus there is no basis to claim that Balaban's existing absolute E-bound already proves fixed-observable cross-cutoff convergence.

## 10. Determination

R66 establishes:

1. CMP119 keeps scale-of-origin provenance for the regular contributions `E^(j)`.
2. CMP116 contains a genuine fine-to-coarse geometric scale-transfer inequality, `2 d_k >= L d_{k+1}`, used to propagate localization through one RG step.
3. Conditional iteration of this inequality gives extremely strong ultraviolet-memory loss for source components whose endpoint descendants have positive coarse tree diameter.
4. The localization metric gives no suppression for a component that collapses to one endpoint block; scale separation and spatial diameter are different resources.
5. After vacuum and exact `F^2` extraction, the surviving local pure-gauge jet is expected to begin at dimension six and therefore to acquire an `L^-2` tree-level factor per scale, but the exact native Yang–Mills theorem implementing this remains open.
6. Hence `ScaleSeparatedETransport` splits into an extended/polymer geometry problem and a collapsed-local Taylor-jet problem. The latter is now the decisive residue.
7. At fixed finite endpoint volume, summable sup-norm endpoint action defects imply Cauchy convergence of every bounded cylindrical observable by an elementary normalized-density perturbation bound.
8. No IR mass-gap/clustering hypothesis is used; spatial locality must not be confused with scale irrelevance.

Canonical state:

`RegularScaleProvenance = CLOSED / SOURCE-ATTESTED`.

`OneStepLocalizationMetricGain = CLOSED / SOURCE-ATTESTED`.

`ExtendedEGeometricTransport = ONE-STEP CLOSED; ITERATED DESCENDANT DICTIONARY OPEN`.

`LocalizationMetricAloneKillsLocalUVJet = FALSE`.

`CollapsedLocalEJetIrrelevance = LIVE NATIVE THEOREM OBLIGATION`.

`FixedFiniteVolumeObservableCauchyFromSummableEndpointDefects = DERIVED`.

`ScaleSeparatedETransport = REDUCED TO ExtendedEGeometricTransport + CollapsedLocalEJetIrrelevance`.

`NativeComplementaryDifferenceContraction = retained as fallback, still OPEN`.

## Negative results / guardrails

- Do not infer a source-depth decay factor merely from the same-scale `E_0 exp(-kappa d_j)` bound.
- Do not apply the CMP116 metric scale gain to a zero-diameter local endpoint component and pretend it gives suppression.
- Do not promote the expected dimension-six / `L^-2` local scaling to a Bałaban theorem before the Paper-I extraction/Taylor normalization is recovered.
- Do not use spatial separation or an assumed mass gap to dispose of a UV operator inserted in the same physical region as a fixed observable.
- Do not equate fixed-finite-volume observable convergence with OS reconstruction or the infinite-volume limit.
- Do not infer continuum Yang–Mills existence or a mass gap from R66.

## Next frontier — YM-R67

`YM-R67 — Paper-I local jet / exact extraction order and canonical L^-2 scaling audit.`

Tasks:

1. recover the exact Paper-I definition of `beta_j` and determine whether it is an exact local projection onto the Wilson/`F^2` direction;
2. identify every normalization/Taylor condition imposed on the residual regular activity after vacuum and beta subtraction;
3. determine whether the native one-step rescaling theorem gives an explicit `L^-2` or other strict scale gain for the collapsed local residual;
4. separate local Taylor-jet contraction from polymer-diameter contraction;
5. if Paper I does not contain the needed jet theorem, type it as the next genuinely missing cross-cutoff compatibility theorem rather than reading it into `(I.1.18)`.

Highest cumulative reference remains [84]; [85] remains next.