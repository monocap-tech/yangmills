# YM-R64 — native one-step derivative / triangularity audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R65` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R63, which reduced cross-cutoff loss of memory to a stable-fiber problem and isolated a decisive native fork:

`Does the Yang–Mills coupling coordinate evolve independently of the complementary complete-density coordinates, or can E/R/B activity leak back into the marginal coordinate?`

The present pass audits that fork against the source-shaped CMP119 inductive coordinates and separates two notions that were conflated in R63:

1. **coordinate / canonical-orbit triangularity** — the published inductive chart prescribes the running coupling by a scalar recursion and stores the residual terms elsewhere;
2. **projection / Banach-map triangularity** — the coupling extracted from the RG image of an arbitrary nearby complete density is independent of its complementary coordinate, equivalently `D_K T_g = 0`.

These are not the same theorem.

Repeated literature sources: [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [22] Bałaban CMP122-II; [84] Bauerschmidt–Brydges–Slade as theorem-grammar control only.

No new bibliography item is consumed. Highest remains [84].

Source-extraction note: an independent public source-audit corpus containing locally rendered primary CMP119 pages was used only to target and cross-check the formulas below. Formal publication should still quote the primary scan directly. The literature claims remain attributed to [59], not to that auxiliary audit.

## 1. CMP119 makes the declared coupling coordinate syntactically triangular

CMP119 Sect. 2 defines the localized effective coupling by Eq. (2.24), in source-normalized form,

`1/g_{j-1}^2(x) = 1/g_j^2(x) + beta_j(g_{j-1}) phi_j(x)`.

The source-side extraction further records that `phi_j` is a smooth cutoff on the relevant regular domain and equals one on the indicated interior region.

Crucially, the displayed recursion contains:

- the previous coupling `g_{j-1}`;
- the scalar beta increment `beta_j(g_{j-1})`;
- the localization function `phi_j`;

and **does not explicitly contain** the regular activity `E`, the localized remainder `R`, or the boundary term `B`.

Thus in the coordinates used to state the CMP119 induction, the designated marginal sequence is recursively prescribed before the complementary coordinates are written.

Canonical classification:

`DeclaredCoordinateTriangularity = SOURCE-ATTESTED`.

This is stronger than the purely hypothetical fork left by R63.

## 2. Eq. (2.25) shows where the extracted marginal piece goes

Immediately after the coupling definition, CMP119 writes the regular part schematically as

`E_k(U_k)`

`= sum_{j=1}^k [ E^(j)(Lambda_j, g_{j-1}, U_k)`

`                  - E^(j)(Lambda_j, g_{j-1}, 1)`

`                  - beta_j(g_{j-1}) A(phi_j, U_k) ]`.

Thus the beta coefficient appearing in the scalar coupling recursion is also subtracted from the local regular contribution in the Wilson-action direction.

This confirms the intended coordinate architecture:

`fresh fluctuation contribution`

`= marginal A(U) piece + normalized complementary regular piece`.

The coupling coordinate and the regular coordinate are therefore not arbitrary unrelated labels. The source is explicitly organizing the local contribution by removing a beta-function multiple of the principal gauge action from `E_k`.

However, Eq. (2.25) alone does **not** establish a universal projection identity such as

`Pi_A E_residual = 0`

for every admissible complete density in a Banach neighborhood. The exact Paper-I definition of `beta_j`, including the local extraction functional that produces it, remains to be recovered.

Canonical classification:

`MarginalSubtractionArchitecture = SOURCE-ATTESTED`.

`ExactExtractionOrthogonality = OPEN SOURCE OBLIGATION`.

## 3. Why syntactic triangularity does not yet prove b_k = 0

R63 linearized a hypothetical complete-density RG map as

`delta x_{k+1} = a_k delta x_k + b_k delta K_k`,

`delta K_{k+1} = c_k delta x_k + A_k delta K_k`,

with `x=g^{-2}`.

The strong triangular statement needed to set

`b_k = D_K T_x = 0`

would mean:

> Take two arbitrary nearby admissible complete densities with the same coupling coordinate but different complementary activities. After one exact RG step and **re-extraction of the coupling coordinate**, both have exactly the same next coupling.

CMP119 Theorem 1 does not have this logical form. It says that when the coupling sequence obeys the Paper-I recursive equations and inequalities, the densities produced by successive `RT` applications from the prescribed initial density satisfy the full inductive assumptions.

That is a theorem about a **canonical generated trajectory under a prescribed coupling sequence**. It is not stated as a Fréchet theorem for the RG transformation on an open Banach ball of arbitrary `K` perturbations.

Therefore:

`DeclaredCoordinateTriangularity`

`does not imply`

`GeneralProjectionTriangularity (D_K T_x = 0)`.

The latter remains unproved.

## 4. But R63's full stable graph is no longer the default native model

Although the general Banach-map derivative remains open, the source architecture materially changes the burden.

For the **canonical Bałaban-generated density class**, the coupling sequence is carried as an external recursive coordinate and every scale contribution to `E_k` is written with its beta multiple removed.

Therefore the first native hypothesis to test is now the much simpler statement:

`CanonicalOrbitTriangularity:`

`two canonical generated trajectories that share the same coupling tail continue to use the same prescribed future coupling tail, while their E/R/B differences remain complementary.`

If this holds after the depth-`N` / depth-`N+1` constructions are aligned at their first common physical scale, then the R63 stable graph has

`H_k = 0`

on the actual cross-cutoff comparison pair, even if no universal `D_K T_x=0` theorem is available for arbitrary perturbations.

The loss-of-memory problem would then reduce to a difference theorem for the complementary coordinates along a common prescribed coupling sequence.

This is a strictly weaker target than a full stable-manifold theorem and is better matched to the published source chart.

## 5. A second triangularity issue remains: depth/index coherence

Eq. (2.24) contains a scale label `j`:

`beta_j`, `phi_j`, `Lambda_j`.

R61's abstract scalar endpoint theorem treated the beta maps as an ordered sequence and R62 compared depth `N` with depth `N+1` after one fine step.

For the scalar tails to nest exactly one needs a source-level reindexing/coherence statement of the form

`g_1^(N+1) = g_0^(N)`

and thereafter

`g_{r+1}^(N+1) = g_r^(N)`

at the same physical scales, after translating the scale/domain labels.

This does not follow merely from the algebraic appearance of Eq. (2.24). Possible sources of nontrivial index dependence include:

- finite-volume/domain boundaries;
- the localized cutoff functions `phi_j`;
- scale-dependent definitions of `beta_j`;
- the choice of the regular-domain sequence `Lambda_j`.

Thus a second independent object must be named:

`CrossDepthMarginalTailCoherence`.

Canonical status:

`CrossDepthMarginalTailCoherence = OPEN`.

This is the exact property R62 previously called `MarginalTailCoherence`, now grounded in the source indices.

## 6. Complementary coordinates are visibly coupling-dependent

Triangularity, even if exact in the coupling direction, would be one-way.

CMP119 Eq. (2.25) makes the regular contribution depend on `g_{j-1}`. The localized analytic domains in Eqs. (2.26)–(2.28) also have radii proportional to `g_j` times powers of `log g_j^{-2}`. The R-terms carry amplitudes such as

`g_j^kappa0 exp(-kappa d_j(X))`.

Hence the complementary update certainly depends on the marginal trajectory:

`D_x T_K` need not vanish.

This is harmless for the simplified cross-cutoff comparison if both trajectories have the same coupling tail: then `delta x=0`, and the `c_k delta x_k` forcing disappears.

The relevant derivative is then only the complementary one,

`D_K T_K`,

computed **along a fixed prescribed coupling trajectory**.

That is now the native loss-of-memory target.

## 7. Published activity bounds are absolute, not difference bounds

The source chain supplies strong absolute estimates:

- CMP116 Lemma 3 / Eq. (2.38) controls localized fluctuation activities `H(Z)` by exponential tree-distance decay;
- CMP116 Eqs. (2.39)–(2.41) exponentiate these into the next-scale regular action bound;
- CMP119 Eq. (2.31) gives localized `R^(j)` bounds of the form `g_j^kappa0 exp(-kappa d_j(X))`;
- CMP122-II supplies the corresponding post-R-operation localized suppression under the small-coupling hypothesis.

These estimates establish that a canonical activity remains small and localized.

They do not by their displayed logical form state

`||T_K(g,K) - T_K(g,K')||_{k+1}`

`<= q ||K-K'||_k`

with `q<1`.

Analyticity of the cluster/polymer maps can in principle provide local Lipschitz estimates by Cauchy/mean-value arguments, but strict contraction requires a quantitative scaling gain in the **difference norm**. That gain has not been source-extracted.

Therefore:

`AbsoluteIrrelevantSmallness != ComplementaryDifferenceContraction`.

Canonical status:

`NativeComplementaryDifferenceContraction = OPEN`.

## 8. The one-layer cross-cutoff defect may have an easier route than uniform q<1

R62 used a sufficient theorem with a bounded one-layer defect `D_N` and geometric propagation `Q_N`.

The source architecture suggests a second possible closure mechanism.

The extra UV layer is created at a coupling

`g_UV^(N) -> 0`.

Several native complementary terms carry explicit positive powers of this small coupling; in particular the CMP119 R-sector admits arbitrarily large `kappa0` after the other parameters are fixed.

Hence it is possible that the one-layer defect itself satisfies

`D_N -> 0`

fast enough to be summable, even if propagation through the common layers is only uniformly Lipschitz rather than strictly contractive.

But this cannot yet be promoted because the defect also contains the regular E-sector, and the exact Paper-I bound `(I.1.18)` governing that sector has not yet been extracted into the corpus.

So R64 records an alternative theorem shape without claiming it:

`small UV defect + bounded propagation`

may replace

`bounded UV defect + strict stable-fiber contraction`.

This makes the exact one-layer E/R/B amplitude a high-value source target.

## 9. Revised dependency diagram

R63's generic stable-manifold diagram is now refined to the native source architecture:

`CMP119 declared scalar recursion`

`        |`

`        +--> DeclaredCoordinateTriangularity = CLOSED`

`        |`

`        +--> ExactExtractionOrthogonality = OPEN`

`        |`

`        +--> CrossDepthMarginalTailCoherence = OPEN`

`                         |`

`                         v`

`        common prescribed coupling tail?`

`             /                 \`

`           yes                 no / unknown`

`            |                       |`

`            v                       v`

` complementary difference       full stable-graph`

` contraction / UV-defect        compensation theorem`

` smallness only`

Thus the full R63 graph is retained as the safe fallback, but it is no longer the first theorem to attack.

## 10. Determination

R64 establishes:

1. CMP119 Eq. (2.24) is triangular in its **declared inductive coordinates**: the running coupling is prescribed recursively from the previous coupling and beta/cutoff data, with no explicit E/R/B argument.
2. CMP119 Eq. (2.25) subtracts the same beta coefficient times the localized gauge action from each regular scale contribution, verifying the source's marginal-subtraction architecture.
3. These facts strongly support canonical-orbit triangularity but do not prove the general Banach-map identity `D_K T_x=0` for arbitrary perturbations.
4. The exact Paper-I extraction definition of `beta_j` is still needed to establish zero marginal projection of the residual activity.
5. Cross-cutoff use additionally requires depth/index coherence of the `beta_j`, `phi_j`, and domain sequence so that separately tuned scalar tails actually nest at common physical scales.
6. If canonical-orbit triangularity plus cross-depth tail coherence hold, the actual R62 comparison can set `delta x=0` and does not need the full R63 stable graph; only complementary loss of memory remains.
7. Published E/R/B/polymer estimates are absolute stability estimates, not a source-attested two-trajectory derivative contraction.
8. A second possible Cauchy mechanism is now visible: the extra-layer complementary defect may itself vanish with the asymptotically small UV coupling fast enough that only bounded propagation is required. The E-sector source bound is not yet extracted, so this remains an open route.

Canonical state:

`DeclaredCoordinateTriangularity = CLOSED / SOURCE-ATTESTED`.

`MarginalSubtractionArchitecture = CLOSED / SOURCE-ATTESTED`.

`GeneralProjectionTriangularity (D_K T_x=0) = OPEN`.

`ExactExtractionOrthogonality = OPEN`.

`CrossDepthMarginalTailCoherence = OPEN`.

`NativeComplementaryDifferenceContraction = OPEN`.

`UVDefectSmallnessAlternative = LIVE POSSIBLE ROUTE`.

Accordingly,

`RenormalizedStableFiberLossOfMemory`

is retyped from a monolithic missing stable-manifold theorem to a fork:

`(CanonicalTailCoherence + ComplementaryLossOfMemory)`

or, if native triangularity fails at the extraction level,

`FullStableGraphTheorem`.

## Negative results / guardrails

- Do not infer `D_K T_x=0` merely because Eq. (2.24) does not display `K`.
- Do not infer zero marginal projection of the residual E-term merely from the subtraction visible in Eq. (2.25); recover the definition of `beta_j` first.
- Do not infer cross-depth nesting from an indexed within-trajectory recursion without checking the scale/domain reindexing.
- Do not infer a strict two-trajectory contraction from absolute polymer/activity bounds.
- Do not treat the explicit `g_j^kappa0` suppression of the R-sector as a bound for the entire one-layer cross-cutoff defect; the E-sector must also be controlled.
- Do not require a full stable-manifold theorem if the canonical source coordinates already provide a triangular common-tail comparison.
- Do not infer continuum construction or a mass gap from any of these UV comparison statements.

## Next frontier — YM-R65

`YM-R65 — Paper-I beta extraction / marginal-defect orthogonality and UV-defect amplitude audit.`

Tasks:

1. recover CMP109/Paper-I definitions around equations `(0.18)`, `(0.20)` and the construction of `beta_j`;
2. determine whether `beta_j` is explicitly defined as the Wilson-action/local marginal projection of the fresh fluctuation contribution;
3. determine whether the residual after subtraction has an exact zero-marginal normalization condition or only a small marginal remainder;
4. audit the scale/index dependence needed for `CrossDepthMarginalTailCoherence`;
5. extract Paper-I inequality `(I.1.18)` sufficiently to bound the one-layer E-sector as `g_UV -> 0`;
6. decide whether `Loc_A Delta_N=0` exactly, tends to zero summably, or requires the full stable-graph compensation of R63.

Highest cumulative reference remains [84]; [85] remains next.
