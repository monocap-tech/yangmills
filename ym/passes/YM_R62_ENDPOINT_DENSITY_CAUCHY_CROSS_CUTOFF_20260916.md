# YM-R62 — endpoint-density Cauchy / cross-cutoff compatibility audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R63` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R61, which separated scalar endpoint tuning from convergence of the complete effective density.

The present pass compares the separately tuned depth-`N` and depth-`N+1` constructions at the same fixed reference scale `mu_*`, asks what ultraviolet stability actually supplies, and identifies the minimal additional estimate that would make the endpoint sequence Cauchy.

Repeated sources: [5] Jaffe–Witten official Yang–Mills problem statement; [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [22] Bałaban CMP122-II; [81] Dimock overview.

New source: [82] Sourav Chatterjee, *The leading term of the Yang–Mills free energy* (2016), used only to clarify the standard meaning of ultraviolet stability versus continuum convergence.

### Reference-custody correction

The frozen source ledger assigns CMP122-II to `[22]` and CMP122-I to `[31]`. R59–R61 accidentally used `[31]` when referring to CMP122-II. Historical pass files are preserved; the append-only correction is custodied separately in `YM_REFERENCE_CORRECTION_022_031_20260916.md`. R62 resumes the canonical IDs.

## 1. Align the two cutoff depths at their first common scale

Fix a physical reference scale `mu_*` and a UV depth `N`.

The depth-`N` theory starts at

`mu_UV^(N) = L^N mu_*`

with tuned bare density `B_N`.

The depth-`N+1` theory starts one scale finer, at

`mu_UV^(N+1) = L^(N+1) mu_*`

with tuned bare density `B_{N+1}`.

After one RG step, `B_{N+1}` lives at the same lattice scale as `B_N`. This produces the canonical cross-cutoff comparison object:

`Delta_N := Normalize( R_{-N-1}(B_{N+1}) ) - Normalize(B_N)`

written in a common Banach/chart of normalized effective densities at scale `-N`.

`Normalize` means that physically irrelevant overall vacuum normalization is removed before comparing probability densities / observables. Partition-function normalization may be custodied separately.

This is the **one-layer compatibility defect**.

The depth-`N` and depth-`N+1` endpoint densities can then be written schematically as

`rho_*^(N)     = Phi_N( B_N )`,

`rho_*^(N+1)   = Phi_N( B_N + Delta_N )`,

where `Phi_N` is the common composite of the remaining `N` RG layers, after all fields have been identified at the same scale.

Thus the entire cross-cutoff problem is reduced to the fate of one defect inserted at the earliest common scale.

## 2. Exact cylindrical consistency would solve the problem, but Wilson bare actions do not have it

The strongest possible condition would be

`Normalize( R(B_{N+1}) ) = Normalize(B_N)`.

Then `Delta_N=0`, and every endpoint density would agree exactly.

But this is not the native Wilson situation. A block transformation of a one-plaquette Wilson action generates a complete effective density containing localized / polymer / extended interactions. The next member of the bare family is again a specially chosen Wilson density, not the exact one-step image of the finer Wilson density.

Therefore:

`ExactCrossCutoffCylindricalConsistency = FALSE TARGET for the bare Wilson family`.

The right question is whether the mismatch is confined to directions that the subsequent RG forgets.

## 3. What scalar tuning can align

In the source chart, the pure-gauge density has at least the decomposition

`effective density = vacuum + g^{-2} A(U) + irrelevant/localized activity`.

Gauge invariance removes a gauge-boson mass coordinate; the vacuum term affects the partition function but disappears from normalized expectations; the Wilson-action coefficient is the marginal coupling coordinate.

If the native coupling maps are depth-coherent and the backward endpoint tuning of R61 is unique, then the depth-`N+1` tuned scalar trajectory should nest with the depth-`N` trajectory after the first step:

`g_1^(N+1) = g_0^(N)`

at the common scale.

Under that additional **MarginalTailCoherence** property, extracting the vacuum and Wilson-action pieces from `Delta_N` leaves a defect in the complementary effective-density directions.

But endpoint equality `g_N^(N)=g_N^(N+1)=g_*` by itself does **not** prove this nesting. Scale-index dependence, finite-volume dependence, localized coupling functions, or dependence of the extracted beta coordinate on other density coordinates can spoil a naive scalar semigroup picture.

Hence:

`EndpointCouplingEquality != MarginalTailCoherence`.

The latter is part of the cross-cutoff theorem obligation.

## 4. The one-layer defect is naturally an irrelevant/stable-fiber candidate

At the common scale, `R(B_{N+1})` differs from the Wilson bare ansatz by the very structures the Bałaban effective-density machinery was built to accommodate: local higher-order terms, localized polymer activities, and large-field contributions, after vacuum and marginal extraction.

Power counting and earlier project passes make it structurally plausible that the local residual begins in irrelevant directions after the `A(U)` extraction. But this is not enough for cross-cutoff convergence.

Two additional facts are needed:

1. `Delta_N` must be uniformly bounded in the **native complete-density norm**, including the large-field/localization bookkeeping;
2. the RG must contract **differences of two admissible trajectories**, not merely keep each trajectory individually inside the inductive domain.

This distinction is the main result of R62.

## 5. Minimal abstract Cauchy theorem

Let `X_k` denote normalized complete-density coordinates at scale `k`, decomposed schematically into the tuned marginal coordinate and a complementary coordinate `K_k`.

Assume there is a renormalized fiber / chart in which the following hold.

### A. Cross-depth marginal coherence

The depth-`N` and depth-`N+1` constructions, after one fine step, are compared on the same prescribed marginal trajectory. Any vacuum shift is removed by normalization.

### B. One-layer defect bound

The complementary defect satisfies

`||Delta_N||_{-N} <= D_N`.

### C. Two-trajectory loss of memory

For two admissible densities `X,Y` lying on the same renormalized marginal fiber, one step satisfies a difference estimate

`|| T_k(X) - T_k(Y) ||_{k+1} <= q_k ||X-Y||_k`,

with `0 <= q_k < 1` in the relevant weak-coupling region.

This is stronger than an absolute inductive estimate on `||K_k||`.

### D. Summability

Write

`Q_N := product_{r=1}^N q_r`.

If

`sum_N D_N Q_N < infinity`,

then

`||rho_*^(N+1)-rho_*^(N)|| <= D_N Q_N`,

so the endpoint sequence is Cauchy by telescoping.

In the uniform case

`q_k <= q < 1`, `D_N <= D`,

one gets the geometric estimate

`||rho_*^(N+1)-rho_*^(N)|| <= D q^N`

and hence

`||rho_*^(M)-rho_*^(N)|| <= D q^N/(1-q)`

for `M>N`.

Classification: **DERIVATION**. This is a sufficient abstract theorem, not a theorem attributed to Bałaban.

## 6. Why absolute ultraviolet stability is not this theorem

CMP119 [59] gives an inductive description of complete effective densities, including large-field domains, and shows that the RG preserves the form of densities satisfying its hypotheses.

CMP122-II [22] completes the stated four-dimensional ultraviolet-stability architecture, conditional on its small-effective-coupling hypothesis.

Those are powerful **one-trajectory stability / boundedness** statements. They do not have the logical form

`distance between two separately tuned cutoff trajectories contracts by q<1`.

Uniform control of each member of a sequence gives

`||rho_*^(N)|| <= C`,

but this alone says nothing like

`||rho_*^(N+1)-rho_*^(N)|| -> 0`.

The distinction is elementary but decisive:

`bounded orbit != Cauchy orbit`.

Likewise, preservation of an inductive class is not automatically a stable-foliation theorem.

## 7. Literature status: ultraviolet stability is a precursor, not the continuum observable limit

The official Jaffe–Witten problem discussion [5] describes Bałaban's effective-action estimates as uniform in lattice spacing and as an important step toward a continuum limit on compactified space-time, while separately stating that one must obtain limits of expectations of gauge-invariant observables and that the existing results need extension in that direction.

Chatterjee [82] later describes ultraviolet stability of the effective action as compactness/stability with respect to the ultraviolet cutoff and, in the same discussion, emphasizes that rigorous construction of non-Abelian Yang–Mills in three and four continuum dimensions remains unresolved.

This confirms the typing needed here:

`UltravioletStability != ContinuumStateConvergence`.

It does not diminish the former; it identifies the missing map from bounded effective actions to a unique regulator-independent state / observable functional.

## 8. Compactness is cheaper than Cauchy convergence

At a **fixed finite physical volume and fixed endpoint lattice**, the gauge configuration space is a finite product `G^{E_*}` of a compact gauge group.

Therefore any sequence of normalized endpoint probability measures is automatically tight and has weakly convergent subsequences.

So a statement such as

`there exists a subsequence rho_*^(N_j) converging weakly`

is far too weak to close the continuum-construction seam at this stage.

It gives neither:

- uniqueness of the subsequential limit;
- convergence of the full cutoff sequence;
- regulator independence;
- compatibility as the reference lattice itself is refined;
- the complete family of Schwinger / gauge-invariant observable limits;
- the infinite-volume limit.

The genuinely useful target is therefore a **loss-of-UV-memory** estimate or another uniqueness mechanism, not mere tightness.

## 9. Hierarchy of statements that must not be conflated

R62 fixes the following hierarchy.

### Level 1 — partition-function / free-energy stability

Controls a scalar normalization or its density in volume.

This does not determine normalized local observables.

### Level 2 — effective-density ultraviolet stability

Keeps the renormalized density/action inside a controlled class uniformly as the cutoff is moved.

This does not imply different cutoff trajectories approach one another.

### Level 3 — fixed-scale subsequential compactness

At finite compact endpoint lattice, this is comparatively cheap and may even be automatic after normalization.

This does not imply uniqueness.

### Level 4 — cross-cutoff Cauchy / uniqueness

Requires comparison of separately tuned regulator depths and loss of the extra UV layer's irrelevant information.

This is the live R62 residue.

### Level 5 — convergence of gauge-invariant local observables / compatible states

Requires a topology or projective family strong enough to define the continuum Euclidean state.

### Level 6 — OS-positive continuum reconstruction

Additionally requires the relevant reflection positivity, Euclidean covariance, regularity and consistency properties to survive the limit.

### Level 7 — infinite volume and mass gap

Separate IR obligations. They are not part of R62.

## 10. A subtlety: irrelevant defects can leak back into the marginal coordinate

It is tempting to say:

`Delta_N is irrelevant => it contracts`.

That is still too fast.

Under a nonlinear RG, a perturbation in complementary coordinates can regenerate a local `A(U)` component at a later scale. The running coupling is defined precisely by repeatedly extracting such marginal pieces.

Therefore the needed two-trajectory theorem must either:

- prove contraction on a genuine **renormalized stable fiber** where induced marginal shifts are compensated by the tuning condition; or
- prove a coupled difference system controlling both marginal and irrelevant deviations and show that the endpoint boundary condition kills the marginal mode.

Canonical name:

`RenormalizedStableFiberLossOfMemory`.

This is stronger and more accurate than a bare engineering-dimension statement.

## 11. Determination

R62 establishes:

1. The depth-`N` and depth-`N+1` cutoff theories have a canonical first common scale, at which their difference is represented by a one-layer compatibility defect `Delta_N`.
2. Exact cylindrical consistency of the Wilson bare family is not expected because one RG step generates the full effective-density interaction class.
3. Endpoint equality of the scalar coupling does not by itself imply that the two scalar trajectories nest at the common scale; a depth-coherent marginal-flow property is required.
4. After vacuum/marginal alignment, the one-layer mismatch is the natural candidate for an irrelevant/stable-fiber defect.
5. A uniform **two-trajectory contraction** plus a bounded one-layer defect gives a geometric/summable Cauchy theorem for endpoint densities.
6. Bałaban's published ultraviolet-stability chain gives one-trajectory effective-density control, not by logical form the required cross-cutoff difference contraction.
7. Fixed-lattice subsequential compactness is too weak; on compact finite gauge configuration space it is essentially automatic after normalization.
8. The missing continuum bridge is therefore a loss-of-regulator-memory / stable-fiber theorem, not another absolute stability bound.

Canonical state:

`EndpointDensityConvergence`

`= REDUCED TO CrossCutoffCompatibility + RenormalizedStableFiberLossOfMemory`.

More precisely:

`CrossCutoffCompatibilityDefect = STRUCTURALLY IDENTIFIED`,

`MarginalTailCoherence = OPEN`,

`NativeTwoTrajectoryContraction = OPEN`,

`FixedEndpointWeakSubsequence = CHEAP / INSUFFICIENT`,

`FullEndpointCauchy = OPEN`.

## Negative results / guardrails

- Do not infer Cauchy convergence from uniform bounds on each effective density.
- Do not infer full-sequence convergence from compactness or existence of a subsequence.
- Do not demand exact RG closure of the one-plaquette Wilson bare family; the effective action necessarily leaves that family.
- Do not assume endpoint coupling equality forces the depth-`N` trajectory to be the tail of the depth-`N+1` trajectory without a depth-coherence theorem.
- Do not call an engineering-dimension estimate a two-trajectory contraction theorem.
- Do not ignore marginal leakage generated by nonlinear RG from an initially irrelevant defect.
- Do not promote ultraviolet stability to convergence of gauge-invariant expectations; the literature itself distinguishes these tasks.
- Do not mix the present fixed-volume UV comparison with the thermodynamic limit or mass-gap problem.

## Next frontier — YM-R63

`YM-R63 — native stable-fiber / two-trajectory loss-of-memory audit.`

Tasks:

1. inspect CMP109/CMP119/CMP122 for any estimate on differences / Fréchet derivatives of the RG map, not merely absolute bounds on a single density;
2. determine whether the local extraction map makes the RG block-triangular enough to construct a stable fiber around the tuned coupling trajectory;
3. quantify marginal leakage produced by a complementary density perturbation and whether backward endpoint tuning cancels it;
4. bound the one-layer Wilson-to-effective compatibility defect in the native complete-density norm;
5. if a uniform contraction is unavailable, test weaker summable loss-of-memory mechanisms sufficient for endpoint Cauchy convergence.

Highest cumulative reference is [82]; [83] remains next.