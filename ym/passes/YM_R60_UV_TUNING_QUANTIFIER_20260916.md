# YM-R60 — UV tuning quantifier / marginal-flow bridge audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R61` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R59 and audit the quantifiers in `CouplingWindowPersistence` before attempting to promote any exact Paper-I inequality.

R59 correctly isolated the native marginal-flow boundary, but its schematic phrase

`g_0 sufficiently small => g_k in (0,gamma] for the entire desired trajectory`

must be split into two logically different statements:

1. a **fixed-depth weak-coupling persistence theorem**, and
2. an **all-UV-depth tuning theorem** in which the bare coupling is allowed, and in fact expected, to depend on the cutoff depth.

Repeated sources: [7] Bałaban CMP109 (1987); [59] Bałaban CMP119 (1988); [31] Bałaban CMP122-II (1989); [81] Dimock Balaban overview.
No new bibliography item is consumed.

## 1. Native inverse-square coordinate fixes the direction of the bookkeeping

On an interior region where the cutoff `phi_j=1`, CMP119 Eq. (2.24) has the form

`1/g_{j-1}^2 = 1/g_j^2 + beta_j(g_{j-1})`.

Write

`x_j := g_j^{-2}`.

Then

`x_j = x_{j-1} - beta_j(g_{j-1})`.

Thus, whenever the beta increment is positive on the weak-coupling collar, forward RG evolution toward coarser scales decreases `x_j` and therefore increases `g_j`.

This is the expected asymptotic-freedom orientation: moving toward the ultraviolet requires smaller bare coupling, while moving toward the infrared increases the effective coupling.

The sign statement here is conditional on positivity of the source beta increment; the exact Paper-I positivity bound is not invented in this pass.

## 2. Fixed bare coupling cannot be the all-depth target

Assume provisionally that on the weak collar `(0,gamma]` the native beta increments satisfy a positive lower bound

`beta_j(g) >= b_- > 0`.

Then as long as the trajectory remains in that collar,

`x_N <= x_0 - N b_-`.

Consequently a single fixed finite `x_0=g_0^{-2}` cannot support arbitrarily large `N` while preserving positivity, much less the bound `g_N<=gamma`.

Therefore the all-depth theorem cannot have the quantifier pattern

`exists g_0>0 such that for all N the same g_0 stays in the weak collar through N steps`.

That is not the asymptotically-free continuum tuning problem.

Canonical negative result:

`FixedBareCouplingAllDepthPersistence = WRONG TARGET`.

## 3. Correct fixed-depth sufficient condition

Assume instead an upper beta corridor on `(0,gamma]`:

`0 <= beta_j(g) <= b_+`.

For a prescribed RG depth `N`, the recursion gives

`x_j >= x_0 - j b_+`.

Hence the sufficient condition

`x_0 >= gamma^{-2} + N b_+`

implies

`x_j >= gamma^{-2}`

and therefore

`g_j <= gamma`

for every `0<=j<=N`, provided the beta bound is valid along the recursively constructed trajectory.

Equivalently,

`g_0 <= (gamma^{-2}+N b_+)^{-1/2}`.

This is a DERIVATION from a uniform beta corridor, not a quotation of Paper-I inequality (1.0.33).

## 4. The UV tuning law is necessarily N-dependent

The previous estimate immediately yields the scale law

`g_0^(N) = O(N^{-1/2})`

when the inverse-square beta increment approaches a nonzero constant per block scale.

More precisely, if on the weak collar

`0 < b_- <= beta_j(g) <= b_+ < infinity`,

and an endpoint `g_N` is held in a fixed compact subinterval of `(0,gamma]`, then summing the recursion backward gives

`g_N^{-2} + N b_- <= (g_0^(N))^{-2} <= g_N^{-2} + N b_+`.

Hence

`(g_N^{-2}+N b_+)^{-1/2} <= g_0^(N) <= (g_N^{-2}+N b_-)^{-1/2}`,

so

`g_0^(N) ~ N^{-1/2}`

up to the beta-corridor constants.

This is exactly the discrete logarithmic/asymptotic-freedom scaling expected when one RG step represents a fixed multiplicative change of length scale: `N` is proportional to a logarithm of the UV cutoff ratio.

Again, the existence of the required positive two-sided beta corridor remains a source theorem obligation.

## 5. R59's global residue is therefore retyped

The live missing bridge is **not** uniform persistence for a fixed bare coupling.

The correct object is a tuned family

`{g_0^(N)}_{N>=1}`

such that, for each cutoff depth `N`, the recursively generated trajectory

`g_0^(N), g_1^(N), ..., g_N^(N)`

remains inside the jurisdiction required by CMP119/CMP122-II, with enough uniformity in the other inductive constants to pass to the intended UV limit.

Thus:

`CouplingWindowPersistence`

is replaced canonically by the more precise object

`TunedUVWeakCouplingTrajectory`.

Its logical shape is

`for each N, choose g_0^(N) -> 0 so that max_{0<=j<=N} g_j^(N) <= gamma`,

plus whatever endpoint/physical-scale normalization is required.

## 6. What CMP109 definitely supplies, and what remains unextracted

The title and abstract of CMP109 explicitly state that Paper I constructs beta-functions and defines coupling-constant renormalization by a recursive system of renormalization-group equations. [7]

CMP119 then imports Paper-I equations `(0.18)`, `(0.20)` and inequalities `(1.0.33)` as hypotheses for its complete-density induction. [59]

CMP122-II retains the small-coupling-window assumption and states that the stronger second-order perturbative theorem intended to remove that assumption is not supplied there. [31]

Dimock's later overview independently records the historical publication boundary: the effective-density/stability machinery exists, while the coupling-constant-flow paper in second-order perturbation theory is missing. [81]

What is **not yet source-custodied** in this repository is the exact printed content of CMP109 `(0.18)`, `(0.20)`, `(1.0.33)`, including the precise beta sign, constants, error terms and any N-dependent tuning statement.

Those details must remain OPEN rather than reconstructed from secondary modern claims.

## 7. Published-spine search

The published Balaban Yang–Mills spine located in the standard bibliographic record remains:

- CMP109 (1987), small-field effective actions and coupling renormalization;
- CMP116 (1988), cluster expansions;
- CMP119 (1988), convergent renormalization expansions;
- CMP122-I/II (1989), large-field R operation.

The present search found no later Bałaban paper in that spine that can presently be source-attested as the missing all-depth second-order coupling-flow theorem.

This does not prove nonexistence of an unpublished manuscript or inaccessible preprint; it establishes only the present published-source boundary.

## 8. Determination

R60 establishes the following bounded retyping:

1. The natural running coordinate is `x=g^{-2}`.
2. Positive inverse-square beta drift means the effective coupling grows toward coarser scales.
3. A single fixed bare coupling is therefore not the correct all-depth UV target.
4. For fixed depth `N`, an upper beta corridor gives the sufficient margin
   `g_0 <= (gamma^{-2}+N b_+)^{-1/2}`.
5. With a positive two-sided beta corridor, keeping a fixed weak endpoint forces
   `g_0^(N) ~ N^{-1/2}`.
6. The native global object is an N-dependent tuned family of weak trajectories, not fixed-bare-coupling persistence.
7. The exact Paper-I inequalities and beta bounds remain unextracted and must not be invented.
8. No source-attested later published theorem has yet been located that removes the CMP122-II coupling-window hypothesis.

Canonical state:

`LargeFieldROperationReturnMap = CLOSED conditional on TunedUVWeakCouplingTrajectory`.

`TunedUVWeakCouplingTrajectory = LIVE NATIVE MARGINAL-FLOW OBLIGATION`.

## Negative results / guardrails

- Do not require one fixed `g_0` to remain weak for arbitrarily many RG steps.
- Do not identify the derived `N^{-1/2}` law with Bałaban's exact theorem until the beta corridor is source-extracted.
- Do not import a modern perturbative coefficient as though it were the exact CMP109 normalization.
- Do not infer that the missing published second-order paper means the recursive Paper-I coupling construction is absent; it is present.
- Do not infer continuum existence or a mass gap from the tuned weak-coupling trajectory alone.

## Next frontier — YM-R61

`YM-R61 — tuned endpoint / physical-scale normalization audit.`

Tasks:

1. determine what endpoint quantity should be held fixed while `N->infinity`: terminal effective coupling, RG-invariant scale, or another Paper-I normalization;
2. derive the minimal abstract theorem for existence/uniqueness of a tuned bare sequence from a positive continuous beta corridor without overclaiming source support;
3. continue exact-source recovery of CMP109 `(0.18)`, `(0.20)`, `(1.0.33)` and replace corridor hypotheses with printed bounds if recovered;
4. keep the distinction `finite-depth trajectory existence` vs `uniform inductive constants` vs `continuum observable convergence` explicit.

Highest cumulative reference is [81]; [82] remains next.