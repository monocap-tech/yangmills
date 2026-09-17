# YM-R63 — native stable-fiber / two-trajectory loss-of-memory audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R64` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R62, which reduced fixed-scale endpoint-density convergence to a one-layer cross-cutoff compatibility defect plus a theorem that subsequent RG layers forget that defect after the marginal coordinate has been correctly retuned.

The present pass asks what theorem species `RenormalizedStableFiberLossOfMemory` actually is, what minimal differential structure would imply it, and whether the published Balaban gauge spine already contains such a theorem.

Repeated sources: [7] Balaban CMP109; [21] Balaban CMP116; [59] Balaban CMP119; [22] Balaban CMP122-II; [81] Dimock Balaban overview; [82] Chatterjee ultraviolet-stability context.

New sources:

- [83] J. Dimock, *The Renormalization Group According to Balaban III. Convergence*;
- [84] Bauerschmidt–Brydges–Slade, *Structural stability of a dynamical system near a non-hyperbolic fixed point*.

## 1. The missing theorem has a standard rigorous-RG species

R62 named the residue `RenormalizedStableFiberLossOfMemory` because a perturbation in the irrelevant coordinates can regenerate a marginal Wilson-action component under nonlinear RG.

Reference [84] shows that this is a standard theorem species in rigorous renormalization-group dynamics: a nonautonomous, nonhyperbolic RG flow with marginal and stable coordinates is controlled by a mixed initial/final boundary-value problem in a weighted sequence space. The theorem gives existence, uniqueness, regularity and cutoff-time-uniform control of the tuned flow.

The source explicitly describes its main result as an analogue of a stable-manifold theorem for a nonhyperbolic dynamical system.

This does **not** solve Yang–Mills. It identifies the correct mathematical grammar of the missing bridge.

Canonical typing:

`RenormalizedStableFiberLossOfMemory = NONHYPERBOLIC RG STABLE-FIBER / MIXED-BOUNDARY THEOREM SPECIES`.

## 2. Why an ordinary contraction mapping on the whole density space is the wrong target

Let the normalized complete-density coordinate near a tuned weak trajectory be written schematically as

`X_k = (x_k, K_k)`,

where

`x_k := g_k^{-2}`

is the marginal inverse-square coupling coordinate and `K_k` denotes all normalized complementary effective-density coordinates: localized/polymer activities, boundary/large-field pieces, and other irrelevant data after the canonical local extraction.

The linearized one-step map around a reference tuned trajectory has the block form

`delta x_{k+1} = a_k delta x_k + b_k delta K_k`,

`delta K_{k+1} = c_k delta x_k + A_k delta K_k`.

The marginal multiplier `a_k` is expected to be close to one, not uniformly smaller than one. Therefore a contraction theorem on the entire `(x,K)` space is not the correct object.

The boundary condition supplied by renormalization is instead terminal/mixed:

`delta x_N = 0`

for two depth constructions normalized to the same endpoint coupling/scale, while the UV compatibility defect initially lives mainly in `delta K`.

This is precisely why stable-manifold / mixed-boundary technology is the right grammar.

## 3. Finite-horizon stable graph for the linearized cocycle

For a prescribed endpoint depth `N`, impose

`delta x_k = H_k^(N) delta K_k`

on the linearized stable fiber, with terminal condition

`H_N^(N) = 0`.

Invariance under one RG step requires

`H_{k+1}(c_k H_k + A_k) = a_k H_k + b_k`.

Whenever the scalar/operator factor `a_k - H_{k+1} c_k` is invertible, this gives the backward graph recursion

`H_k = (a_k - H_{k+1} c_k)^(-1) (H_{k+1} A_k - b_k)`.

The complementary difference then evolves by

`delta K_{k+1} = (A_k + c_k H_k) delta K_k`.

This is a DERIVATION. It is the exact finite-horizon linearized form of the compensating marginal retuning demanded qualitatively by R62.

## 4. Small-cross-coupling criterion

Suppose uniformly along the weak trajectory that

`||A_k|| <= q < 1`,

`||b_k|| <= epsilon`,

`||c_k|| <= epsilon`,

and the inverse marginal factor is uniformly controlled,

`||(a_k - H c_k)^(-1)|| <= alpha`

through the graph domain.

Then the backward graph recursion yields schematically

`||H_k|| <= alpha ( q ||H_{k+1}|| + epsilon )`.

For sufficiently small cross coupling, this gives the horizon-independent bound

`sup_k ||H_k^(N)|| <= H_* ~ alpha epsilon / (1-alpha q)`

in the simple regime `alpha q < 1` (or the corresponding weighted nonhyperbolic estimate when `alpha q` is not strictly below one).

The effective stable multiplier is then bounded by

`q_eff <= q + epsilon H_*`.

Thus if

`q_eff < 1`,

two trajectories lying on the same renormalized stable fiber lose memory geometrically in the complementary coordinate.

Classification: DERIVATION / sufficient linearized criterion. It is not attributed to Balaban.

## 5. The nonhyperbolic case requires weighted sequence control, not the toy alpha-q condition

The previous finite-dimensional estimate is pedagogical. In an asymptotically free marginal flow the center/marginal direction is only logarithmically controlled and the natural spaces and norms change with scale.

Reference [84] is important precisely because it treats a nonhyperbolic, scale-dependent RG system rather than assuming a uniform spectral gap in the full linearized map. Its proof uses carefully weighted sequence spaces and mixed initial/final boundary conditions, and its estimates are uniform in the cutoff time required by the RG application.

Therefore the actual Yang–Mills target should not be stated as a naive autonomous stable-manifold theorem.

The native theorem must allow:

- a scale-dependent complete-density Banach/chart;
- a marginal asymptotically-free coupling flow;
- contracting irrelevant/polymer coordinates;
- mixed UV/endpoint boundary data;
- scale-uniform differentiability/Lipschitz estimates;
- large-field/localization components in the same norm system.

## 6. Pure Yang–Mills makes the possible stable-fiber codimension unusually small

Earlier pass YM-R21 identified, under the project’s gauge/reflection/CP-even jurisdiction, one physical dimension-four marginal gauge coordinate: the Wilson/Yang–Mills action coefficient `g^{-2}`. Gauge invariance excludes a gauge-boson mass coordinate; vacuum energy disappears from normalized expectations.

Thus, after normalization, the expected physical noncontracting coordinate count in the weak pure-gauge chart is only one: the running gauge coupling.

This does not prove a stable manifold. But it means that if the source RG chart is complete and no hidden marginal coordinate appears, the cross-cutoff stable fiber should be locally codimension one in the normalized complete-density space.

That is materially simpler than scalar theories with an additional relevant mass counterterm.

Canonical working statement:

`NormalizedPureYMStableFiber = codimension-one candidate over the marginal coupling trajectory`.

Status: WORKING HYPOTHESIS supported by the prior symmetry/local-extraction audit, not a source theorem.

## 7. Crucial fork: exact triangularity would simplify the theorem drastically

The linearized block `b_k` measures leakage

`irrelevant/complementary perturbation -> next-step marginal coupling`.

There are two possible native architectures.

### Route T — exact triangular extraction

If Balaban’s coupling coordinate and local-extraction convention are defined so that the exact one-step recursion has the form

`x_{k+1} = f_k(x_k)`

independently of the normalized complementary activity, then

`b_k = 0`

in the native coordinates.

Two trajectories with the same marginal tail then satisfy `delta x_k=0` at all shared scales, and the stable-fiber problem reduces to

`delta K_{k+1} = A_k delta K_k`.

The missing theorem would then be essentially a strict difference contraction in the complete complementary norm.

### Route G — genuine marginal leakage

If instead the exact extracted coupling depends on the full effective density,

`x_{k+1} = f_k(x_k,K_k)`,

then `b_k != 0` in general, and the stable graph / mixed-boundary compensation is essential.

R63 cannot decide which route is native because the exact Paper-I recursion and extraction rules have still not been transcribed at sufficient equation-level precision.

This fork is now the highest-value source question.

## 8. Why CMP116/CMP119 absolute estimates are not automatically derivative estimates

CMP116 [21] proves that the cluster-expansion terms satisfy the inductive assumptions.

CMP119 [59] introduces complete effective densities, including large-field domains, and proves preservation of their form under the RG when the coupling hypotheses hold.

CMP122-II [22] supplies the large-field R-operation bounds needed for ultraviolet stability.

These source statements control the size/form of one trajectory. R63 requires bounds on the derivative or difference map, such as

`||D_K T_k|| <= q < 1`

on the renormalized fiber, together with bounds on

`D_K x_{k+1}` and `D_x K_{k+1}`.

Analyticity of the effective activities makes such estimates plausible via Cauchy/difference bounds, but analyticity plus boundedness alone does not guarantee a strict contraction constant below one in the needed complete-density norm.

Therefore:

`AnalyticInductiveBounds != StableFiberDerivativeBounds`.

## 9. Dimock III: “convergence” is not the convergence R62 needs

Reference [83] is a useful terminology control.

Dimock’s Part III is an exposition of Balaban’s method for the scalar phi^4 model in d=3. It states that it demonstrates convergence of the expansion and completes the proof of a stability bound. The setup tunes counterterms so that the partition function has bounds uniform in the ultraviolet cutoff, and the final stability corollary is a cutoff-uniform partition-function estimate.

Thus the word “convergence” there means convergence of the large-field/cluster expansion used to establish ultraviolet stability.

It does **not** by itself mean

`rho_*^(N) -> rho_*`

for separately tuned Yang–Mills cutoff states.

Canonical negative result:

`DimockIIIConvergence != CrossCutoffStateConvergence`.

## 10. Stable-manifold technology exists, but Yang–Mills hypotheses remain the problem

Reference [84] proves the theorem species needed in another rigorous RG setting. It gives mixed-boundary existence/uniqueness and regular dependence for scale-dependent nonhyperbolic flows.

This establishes that R62 did not invent an unnatural target. The gap is jurisdictional:

`generic/other-model rigorous stable-manifold machinery`

must not be silently promoted to

`Balaban 4d non-Abelian complete-density stable fiber`.

To instantiate the theorem for the present project one still needs source-native estimates establishing the appropriate derivative structure of the gauge RG map.

## 11. Cross-cutoff Cauchy theorem after stable-fiber closure

Return to the one-layer compatibility defect from R62:

`Delta_N = Normalize(R(B_{N+1})) - Normalize(B_N)`.

Suppose endpoint/marginal retuning places this defect on the finite-horizon stable fiber and suppose the stable transfer satisfies

`||A_k + c_k H_k|| <= q_eff < 1`

uniformly through the remaining `N` layers.

If

`||Delta_N|| <= D`

uniformly in the common-scale norm, then

`||rho_*^(N+1)-rho_*^(N)|| <= C D q_eff^N`

for a chart-equivalence constant `C`.

Therefore the endpoint sequence is geometrically Cauchy.

This recovers R62’s abstract Cauchy condition from a more precise stable-fiber mechanism.

## 12. Determination

R63 establishes:

1. `RenormalizedStableFiberLossOfMemory` is a standard nonhyperbolic stable-manifold / mixed-boundary theorem species in rigorous RG, not a new mathematical category.
2. The whole density map should not be expected to contract because the gauge coupling is marginal; contraction is required transverse to the tuned marginal trajectory.
3. The finite-horizon linearized stable fiber is represented by a graph `delta x = H_k delta K` satisfying a backward Riccati-type recursion.
4. Small cross derivatives plus strict contraction of the complementary block yield an effective stable contraction after marginal compensation.
5. A genuine nonhyperbolic theorem needs weighted scale-dependent sequence spaces; [84] provides a control example of this exact proof grammar in other 4d RG models.
6. Pure Yang–Mills appears to have only one normalized physical marginal coordinate in the audited symmetry class, so the expected stable fiber is locally codimension one if the native chart is complete.
7. The highest-value unresolved source fork is whether Balaban’s coupling extraction makes the RG map exactly triangular in `(g,K)` or whether complementary activities leak into the coupling coordinate and require a nontrivial graph transform.
8. Published CMP116/CMP119/CMP122 absolute inductive estimates are not, by their stated logical form, the derivative/two-trajectory estimates required for stable-fiber contraction.
9. Dimock III’s “convergence” is convergence of the RG expansion yielding a stability bound in scalar phi^4_3; it does not close Yang–Mills cross-cutoff state convergence.

Canonical state:

`RenormalizedStableFiberLossOfMemory`

`= THEOREM SPECIES IDENTIFIED`

and more precisely

`= NativeTriangularity + IrrelevantDifferenceContraction`

or, in the general case,

`= MarginalBoundarySolvability + StableGraphExistence + TransverseDifferenceContraction`.

Current unresolved components:

`NativeTriangularity = OPEN SOURCE QUESTION`,

`D_K T strict contraction = OPEN SOURCE/THEOREM QUESTION`,

`cross derivative bounds b_k,c_k = OPEN SOURCE/THEOREM QUESTION`,

`YangMillsStableFiber = NOT YET PROVED`.

## Negative results / guardrails

- Do not demand contraction in the marginal coupling direction.
- Do not call one-trajectory boundedness a stable-manifold theorem.
- Do not infer `||D T||<1` from analyticity or from an absolute activity bound alone.
- Do not import the Bauerschmidt–Brydges–Slade stable-manifold theorem into Yang–Mills without verifying its hypotheses in the native gauge complete-density chart.
- Do not read “convergence” in Dimock III as convergence of separately tuned regulator states.
- Do not assume the stable fiber is exactly codimension one until hidden marginal/relevant source coordinates are ruled out in the full complete-density representation.
- Do not infer continuum Yang–Mills construction or mass generation from stable-fiber closure alone.

## Next frontier — YM-R64

`YM-R64 — native one-step derivative / triangularity audit.`

Tasks:

1. extract the exact Paper-I/CMP119 coupling update strongly enough to decide whether `g_{k+1}` is independent of the complementary activity after the native local extraction;
2. identify the normalization conditions imposed on `E/R/B` or polymer activities that kill their local marginal projection;
3. inspect CMP116/CMP119 analytic estimates for a source-level difference or Fréchet-derivative bound on one RG step;
4. determine whether the irrelevant gain is strong enough to give a strict derivative contraction in a smaller common analytic domain;
5. if exact triangularity fails, quantify the activity-to-coupling and coupling-to-activity cross derivatives needed for the stable-graph recursion.

Highest cumulative reference is [84]; [85] remains next.