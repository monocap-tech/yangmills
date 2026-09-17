# YM-R61 — tuned endpoint / physical-scale normalization audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R62` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R60, which corrected the all-depth coupling quantifier and replaced fixed-bare-coupling persistence by an `N`-dependent tuned family.

The present pass asks what is actually held fixed while the UV depth `N -> infinity`, whether endpoint tuning can be formulated as a well-posed scalar theorem in the inverse-square coupling coordinate, and how this normalization relates to the RG-invariant `Lambda` scale already identified in YM-R4.

Repeated sources: [7] Bałaban CMP109 (1987); [59] Bałaban CMP119 (1988); [31] Bałaban CMP122-II (1989); [51] Dalla Brida–Ramos (2019) on the Yang–Mills Lambda parameter / scheme conversion; [81] Dimock Balaban overview.

No new bibliography item is consumed.

## 1. A terminal dimensionless coupling by itself is under-typed

R60 wrote the tuned trajectory as

`g_0^(N), g_1^(N), ..., g_N^(N)`

with a terminal weak coupling `g_N` held fixed while the microscopic starting scale moves farther into the ultraviolet.

But a dimensionless value `g_N = g_*` has no scale meaning by itself. A renormalized coupling is defined at a renormalization scale in a specified scheme.

The correctly typed endpoint datum is therefore

`RenormalizationCondition_* := (scheme, mu_*, g_*)`,

with `mu_*` fixed as `N` changes.

If one RG step changes length by a fixed factor `L`, the corresponding ultraviolet starting scale is

`mu_UV^(N) = L^N mu_*`.

The continuum tuning problem is then:

`for each N, choose g_0^(N) at mu_UV^(N) so that after N RG steps the effective coupling at mu_* equals g_*`,

while the whole trajectory remains inside the weak-coupling jurisdiction required by the source induction.

This is the discrete constructive analogue of fixing a renormalization condition at a physical reference scale while removing the UV cutoff.

## 2. The endpoint pair and Lambda are two parameterizations of one RG trajectory

Reference [51] gives the standard Yang–Mills RG organization: a renormalized coupling `gbar(mu)` is scale dependent, whereas the scheme-dependent `Lambda` parameter is RG invariant; once the beta function is known, `Lambda` determines the running coupling as a function of `mu/Lambda`.

Thus, after a coupling scheme and beta flow have been fixed, one may label a trajectory either by

`(mu_*, g_*)`

or equivalently by

`Lambda_scheme`.

This equivalence is conceptual and does not identify Bałaban's lattice coupling numerically with a modern gradient-flow or MS-bar coupling. A finite scheme change changes the numerical Lambda parameter by a finite multiplicative factor.

Therefore the project must distinguish:

`endpoint renormalization condition`

from

`scheme-independent physical claim`.

The first is a coordinate choice on the renormalized trajectory. The second must be stated in terms invariant under finite scheme changes, for example positivity of a ratio such as `M_gap / Lambda` or `M_gap L_*` after a continuum theory exists.

## 3. Constant-drift model makes the scale relation explicit

Write again

`x_j := g_j^{-2}`.

In the simplest autonomous weak-coupling model, suppose one coarse-graining step satisfies

`x_j = x_{j-1} - b`

with `b>0` constant, while the energy scale changes by

`mu_j = mu_{j-1}/L`.

Then

`x_0^(N) = x_* + N b`,

where `x_* = g_*^{-2}` is fixed at `mu_*`.

Since

`mu_UV^(N) = L^N mu_*`,

the combination

`Lambda_disc := mu exp[-(log L / b) x]`

is exactly invariant under the discrete step:

`mu_{j-1} exp[-(log L/b) x_{j-1}] = mu_j exp[-(log L/b) x_j]`.

Hence

`Lambda_disc = mu_* exp[-(log L/b) g_*^{-2}]`

`= mu_UV^(N) exp[-(log L/b) (g_0^(N))^{-2}]`.

This is a DERIVATION in the constant-drift toy model. It is not promoted as Bałaban's exact Lambda parameter or exact beta coefficient.

It explains why the `N^{-1/2}` tuning law of R60 and dimensional transmutation are the same bookkeeping seen in two coordinate systems: linear growth of `g^{-2}` in RG depth becomes exponential scale separation in physical units.

## 4. Minimal abstract endpoint-tuning theorem

The scalar tuning problem can be stated without assuming constant beta drift.

Fix a weak endpoint `0 < g_* <= gamma` and set

`x_* := g_*^{-2}`.

For each RG step define on `x >= x_*`

`B_j(x) := beta_j(x^{-1/2})`

and the forward inverse-square map

`F_j(x) := x - B_j(x)`.

Assume, for each relevant `j`:

1. `B_j` is continuous on `[x_*, infinity)`;
2. `0 < b_- <= B_j(x) <= b_+ < infinity` uniformly;
3. `F_j` is strictly increasing on `[x_*, infinity)`;
4. `F_j(x) -> infinity` as `x -> infinity`.

Then for every prescribed depth `N` there exists a unique backward-tuned sequence

`x_0^(N), x_1^(N), ..., x_N^(N)=x_*`

satisfying

`x_j^(N) = F_j(x_{j-1}^(N))`.

Proof: because `F_j(x_*) = x_* - B_j(x_*) < x_* <= x_j` and `F_j -> infinity`, continuity and strict monotonicity give a unique preimage `x_{j-1}>x_*`. Iterating backward yields the unique sequence.

Moreover

`x_j + b_- <= x_{j-1} <= x_j + b_+`,

so

`x_* + N b_- <= x_0^(N) <= x_* + N b_+`.

Equivalently,

`(x_* + N b_+)^{-1/2} <= g_0^(N) <= (x_* + N b_-)^{-1/2}`.

And because

`x_0 > x_1 > ... > x_N=x_*`,

one has

`0 < g_0 < g_1 < ... < g_N=g_* <= gamma`.

Thus a weak terminal endpoint automatically keeps the entire backward-tuned scalar trajectory inside the weak collar under these hypotheses.

Classification: DERIVATION from an abstract positive invertible beta corridor. This is not claimed to be a theorem printed in CMP109.

## 5. What exact source recovery must establish

The abstract theorem identifies the exact properties needed from the native Paper-I coupling map:

- positivity of the inverse-square increment on the weak collar;
- uniform upper/lower bounds sufficient for tuning estimates;
- invertibility/monotonicity of the one-step scalar map, or another source mechanism selecting the backward trajectory;
- enough uniformity in the scale index to let `N` grow.

CMP109 source metadata verifies construction of beta functions and recursive coupling renormalization, while CMP119 imports the Paper-I RG equations and inequalities as hypotheses. CMP122-II still assumes the effective couplings stay in a sufficiently small interval. The exact printed equations `(0.18)`, `(0.20)`, `(1.0.33)` therefore remain a source-extraction obligation rather than something reconstructed here.

Reference [81] independently supports the historical boundary that the intended stronger second-order coupling-flow paper was not part of the completed published chain.

## 6. Do not identify endpoint normalization with mass generation

YM-R4 already established the crucial distinction:

`Lambda_YM fixes the permitted physical scale of a gap; it does not prove that a gap exists.`

R61 strengthens that statement at the RG-trajectory level.

Fixing `(mu_*, g_*)` or `Lambda_scheme` answers:

`which renormalized trajectory are we attempting to construct?`

It does not answer:

`does the continuum theory on that trajectory have a positive Hamiltonian spectral gap?`

Likewise, a weak endpoint `g_* <= gamma` remains inside the Bałaban weak-coupling jurisdiction. It does not by itself establish entry into the massive strong-coupling basin studied in YM-R10--R13.

Therefore two distinct continuations remain possible in principle:

1. construct the continuum theory normalized at a weak reference scale and later prove a positive dimensionless ratio such as `M_gap/Lambda` or `M_gap L_*`; or
2. prove an additional RG continuation/handoff from the weak endpoint to an IR massive basin.

Neither continuation is supplied by scalar coupling tuning alone.

## 7. The next defect is not scalar tuning but endpoint-density convergence

There is a second quantifier shift hidden by the notation `g_0^(N)`.

For different UV depths `N`, the bare couplings are different. Hence the microscopic measures are different theories at the regulator level. Exact RG pushforward within one fixed `N` does not by itself imply that the fixed-scale effective densities obtained from the `N`- and `(N+1)`-level bare models coincide or converge.

Even if the scalar endpoint is forced to satisfy

`g_N^(N) = g_*`

for every `N`, the irrelevant/localized coordinates may retain `N`-dependence:

`rho_*^(N) = rho_*(g_*, E_*^(N), R_*^(N), B_*^(N), ...)`.

A continuum construction therefore needs a stronger statement than endpoint coupling tuning:

`rho_*^(N) -> rho_*^(infinity)`

in a topology strong enough to control the intended observables / OS reconstruction, or an equivalent Cauchy/compactness statement.

This is not the same as the scale-by-scale induction theorem. It compares different regulator depths after each has been separately tuned.

Canonical new object:

`EndpointDensityConvergence`.

This is the first cross-`N` obligation after the scalar trajectory has been correctly normalized.

## 8. Determination

R61 establishes:

1. A terminal dimensionless coupling alone is under-typed; the fixed datum is `(scheme, mu_*, g_*)`.
2. Once the beta flow is known, this endpoint condition is equivalent to choosing the scheme-dependent RG-invariant `Lambda` parameter.
3. In the constant inverse-square-drift model, the exact discrete invariant is `Lambda_disc = mu exp[-(log L/b) g^{-2}]`, making dimensional transmutation explicit.
4. Under a positive bounded beta corridor plus one-step invertibility, every weak endpoint admits a unique depth-`N` backward-tuned bare coupling, with `g_0^(N) ~ N^{-1/2}` and the whole scalar trajectory remaining weak.
5. These are abstract derivations, not promotions of the still-unextracted CMP109 equations.
6. Endpoint normalization selects the renormalized trajectory; it does not establish mass generation.
7. Fixing the endpoint coupling across `N` does not imply convergence of the full endpoint effective density because the irrelevant coordinates may depend on the UV depth.

Canonical state:

`TunedUVWeakCouplingTrajectory`

`= SCALAR PROBLEM ABSTRACTLY CLOSED under PositiveInvertibleBetaCorridor`

but

`NativePositiveInvertibleBetaCorridor = OPEN SOURCE/THEOREM OBLIGATION`,

and independently

`EndpointDensityConvergence = LIVE CROSS-CUTOFF OBLIGATION`.

The latter is logically stronger than `g_N^(N)=g_*` and is the next native continuum-construction seam.

## Negative results / guardrails

- Do not hold `g_*` fixed without also fixing its renormalization scale and scheme.
- Do not identify Bałaban's lattice coupling numerically with a modern continuum scheme without an explicit matching theorem.
- Do not call the constant-drift `Lambda_disc` Bałaban's exact Lambda parameter.
- Do not infer a mass gap from existence of an RG-invariant scale.
- Do not infer cross-cutoff convergence from within-cutoff exact RG identities.
- Do not infer convergence of all irrelevant coordinates merely because the marginal coupling is tuned to the same endpoint value.

## Next frontier — YM-R62

`YM-R62 — endpoint-density Cauchy / cross-cutoff compatibility audit.`

Tasks:

1. compare the depth-`N` and depth-`N+1` tuned constructions at the same reference scale `mu_*`;
2. identify which effective-density coordinates are forced to agree by the renormalization condition and which remain free / regulator-dependent;
3. determine whether CMP119/CMP122 estimates are uniform enough in `N` to yield a Cauchy, compactness, or subsequential convergence statement for fixed-scale effective densities / observables;
4. distinguish partition-function stability, normalized-measure tightness, local-observable convergence, and OS-positive continuum reconstruction;
5. keep the later IR/mass-generation handoff separate from this UV cross-cutoff comparison.

Highest cumulative reference remains [81]; [82] remains next.