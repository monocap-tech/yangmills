# YM-R48 — Paper-I normalized-domain extraction / append-only correction

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R47_20260916.json`
Next cursor: YM-R49 (unconsumed)

## Question

R47 reduced the native analytic gate to `CanonicalUjcEmbedding` and proposed recovering CMP119 (2.34)--(2.39). R48 asks for the actual source definition of the analytic domain, its coordinate normalization, and whether a fixed canonical field ball can be embedded with scale/volume-uniform constants.

## Preflight and append-only correction

The durable R47 head was recovered. During the present source pass, the primary CMP109/Paper-I text became directly inspectable. This changes two earlier provenance statements and must be recorded append-only rather than silently rewriting them.

1. R35 said the exact Paper-I definition was inaccessible. That is no longer true in the present source environment.
2. R47 treated CMP119 (2.34)--(2.39) as if it were the direct three-condition definition to use for `CanonicalUjcEmbedding`. The more precise source picture is: Paper I gives the fundamental single-scale `U_j^c` definition with four conditions; CMP119 gives a later multiscale refinement/generalization for the B/boundary sector.

## 1. Paper I gives the fundamental four-condition domain

Paper I [7], printed pp. 262--263, defines the complex regularity space `U_j^c(X,alpha_0,alpha_1,gamma_0)` as a union of complex gauge orbits of configurations `(mathcal U,J)` satisfying four conditions. In ordinary applications `gamma_0` is taken with the same smallness scale as `alpha_0`.

### (i) Regular real base field

The complex field is factored as

`mathcal U = U' U`,

with `U` G-valued. The real base satisfies the small plaquette-curvature condition (1.11). On every source cube of fixed `O(LM)` size there is a G-valued gauge transformation putting the base field in a logarithmic coordinate

`U^u = exp(i xi A)`,

with the source-normalized potential and first-difference bounds of (1.12). The important structural feature is the explicit lattice-spacing normalization: the dimensionless quantities are `xi A` and `xi^2 nabla^xi A` (up to the fixed source convention/constants), rather than an unweighted bond sup norm.

### (ii) Complex displacement

The complex factor is written

`U' = exp(i xi A')`,

with `A'` in the complexified Lie algebra, and (1.13) bounds the same source-normalized potential/first-difference quantities by `alpha_1`.

### (iii) Full complex field and source

The full complex configuration satisfies the small plaquette-curvature bound (1.14) at scale `alpha_0` together with a source bound `|J| < gamma_0` on X.

### (iv) Multiscale coarse-field regularity

From the original configuration the source constructs the successive coarse/axial-gauge fields up to level j. Equation (1.16) requires the corresponding coarse fields and sources to obey scale-normalized regularity bounds on a two-layer-shrunken domain. This is the multiscale compatibility condition hidden by the earlier three-condition summary.

## 2. Paper I immediately supplies an interior-space criterion

The paragraph following the definition is decisive. Paper I explicitly notes that there are simple/natural spaces contained in `U_j^c`. If conditions (i)--(iii) hold with smaller constants `alpha_0' < alpha_0` and `alpha_1' < alpha_1`, then Proposition 9 of the cited upstream source supplies the coarse-field estimates; for `alpha_0'` sufficiently small, condition (iv) follows. Therefore condition (iv) is not an independent embedding theorem once a strict first-three margin has been established. [7]

The same passage states that the localized regular activities are analytic on `U_j^c(X,alpha_0,alpha_1)` for positive absolute `alpha_0,alpha_1` independent of X and j and satisfy the uniform Paper-I bound (1.18). This is stronger source evidence for a fixed normalized analytic jurisdiction than the previous theorem-shaped `CanonicalUjcEmbedding` placeholder.

## 3. CMP119 is a multiscale refinement, not a replacement definition

CMP119 [59] later introduces a multiscale analyticity space for the B/boundary terms around (2.34)--(2.39). Its three displayed conditions are a scale-resolved refinement of the same architecture: real-background regularity/source control, local gauge logarithmic coordinates with `L^n eta A` and `(L^n eta)^2 nabla^eta A`, and complex displacement bounds with the analogous scaling.

The admissible margins include

`m_{j,n} = 1 - beta (1 - 2^{-(j-n)})`,

and the text allows, for example, `beta=1/4`. Hence

`m_{j,n} >= 1-beta = 3/4`

uniformly in j,n. Thus the multiscale continuation itself carries a fixed fractional analytic reserve rather than a collapsing collar.

CMP119 also source-verifies

`alpha_0,j = g_j C_0 (log g_j^-2)^q_0`,
`alpha_1,j = g_j C_1 (log g_j^-2)^q_1`,

with positive logarithmic powers in the displayed parameter choice. [59]

## 4. Correct canonical norm

R35's phrase “fixed canonical ball” must now be typed correctly. A raw unweighted bond sup norm is insufficient because Paper-I conditions include scaled first differences/plaquette curvature and, when present, the source J.

Define the project canonical norm so that its local components dominate the source-normalized quantities appearing in (i)--(iii), schematically

`||a||_can,X = max{ ||a||, ||xi nabla^xi a||, ||curv_lin(a)||, source component }`,

with fixed finite local-coordinate comparison constants. This is a coordinate dictionary, not a new source theorem.

For a complex perturbation written in project variables as

`mathcal U = exp(i g_j a)`

(or the corresponding perturbation of a native real background), the source logarithmic coordinate satisfies

`xi A' = g_j a`

up to the fixed convention/coordinate map. Therefore every source-normalized potential/derivative functional is `O(g_j ||a||_can)` on a fixed canonical ball; the full plaquette condition is likewise `O(g_j ||a||_can)` by the finite local BCH expansion.

Consequently a fixed `||a||_can <= R` is admitted whenever

`C_can R g_j <= alpha_r,j`

for r=0,1 and the relevant source/source-field component. Since

`alpha_r,j/g_j = C_r (log g_j^-2)^q_r`,

any fixed R lies strictly inside the domain for sufficiently weak coupling when `q_r>0`; if a source width has zero log power, choose R below the corresponding fixed source constant. This comparison is local and therefore volume-independent.

Once the first three conditions hold with a fixed strict margin, Paper I's interior-space criterion supplies condition (iv). An inner Cauchy ball can then be chosen as any fixed fraction of the outer canonical ball; no additional source theorem is required.

## 5. Status of CanonicalUjcEmbedding

The broad source-theorem obligation introduced in R35/R36 is removed.

At the mathematical/source level the needed mechanism is now present:

`Paper-I four-condition definition`
`+ strict first-three normalized bounds`
`+ Paper-I smaller-space/interior criterion`
`+ alpha/g logarithmic scaling`
`-> fixed normalized canonical domain for sufficiently weak coupling`.

What remains is only a finite project/source coordinate lock: define the project `CanonicalFieldNorm` and, where the project carries J independently, its source normalization so that the displayed source quantities are dominated with explicit fixed constants.

Therefore the correct status is

`CanonicalUjcEmbedding: CLOSED UP TO FINITE COORDINATE DICTIONARY`.

This is custody/dictionary debt, not a missing analytic theorem.

## Negative results / guardrails

- Do not retain the R35 statement that the exact Paper-I definition is inaccessible; R48 supersedes it append-only.
- Do not describe Paper I's fundamental domain as having only three conditions; it has four.
- Do not treat CMP119 (2.34)--(2.39) as a verbatim substitute for the Paper-I definition; it is a multiscale refinement/generalization used in the complete-density/B-sector architecture.
- Do not use a raw unscaled bond sup ball as `CanonicalFieldNorm`; the source controls scaled potential, derivative/curvature, and source quantities.
- Do not claim condition (iv) automatically for arbitrary configurations; its discharge uses the Paper-I smaller-constants/interior criterion.
- Do not claim the full Yang-Mills construction or continuum mass gap is proved.

## Determination

R48 removes the last apparent *source theorem* behind `CanonicalUjcEmbedding`. The source itself supplies the regularity domain, a strict interior-space mechanism, scale/volume-independent analytic constants, and the multiscale fixed-fraction reserve. The remaining seam is a finite coordinate dictionary identifying the project's canonical norm with Paper-I's normalized field/derivative/curvature/source variables.

## Next frontier — YM-R49

**Canonical norm / source-coordinate dictionary lock.**

Define the project `CanonicalFieldNorm` directly from the Paper-I (1.11)--(1.16) normalized quantities (and the CMP119 multiscale version when needed), record the fixed comparison constants for `mathcal U=exp(i g_j a)`, and close `CanonicalUjcEmbedding` without a remaining source hypothesis.

## References

Reused: [7] CMP109/Paper I; [59] CMP119; [21] CMP116 for downstream consumption. No new cumulative source is consumed. Highest source ID remains **[79]**; next new source is **[80]**.
