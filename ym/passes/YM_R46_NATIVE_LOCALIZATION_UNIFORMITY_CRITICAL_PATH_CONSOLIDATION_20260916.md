# YM-R46 — native-localization uniformity / critical-path consolidation

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R45_20260916.json`
Next cursor: YM-R47 (unconsumed)

## Question

R36--R45 repeatedly minimized apparent analytic/source obligations introduced by the reflection-positive (RP) blocking modification. R46 asks for the final dependency classification:

1. which obligations are already obligations of the native Bałaban one-step/complete-density construction;
2. which obligations are genuinely introduced by the RP modification;
3. whether the remaining interpolation/localization uniformity is a new source theorem or only a derived use of the native uniform estimates.

## Canonical preflight

Repository authority confirms:

`YM-R45 COMPLETE -> YM-R46`, with R46 unconsumed.

R45 removed blocker support anchoring as an independent source theorem: the blocker path family is design data with a fixed localization-cube cover, which can be adjoined to the native Y0 seed before CMP116's existing minimal-Z0 construction. Anchor multiplicity is absorbed by a finite loss in the native decay exponent.

## 1. Modification-internal results already established

The RP modification itself now contributes the following internally derived/design facts.

### M1. Exact global RP-compatible blocking kernel

R25 constructs a globally defined gauge/orientation/reflection-covariant center `C_e(U)` using a cutoff logarithm around a distinguished path and defines the exact normalized translated heat-kernel kernel

`K_e(dV|U) = rho_{t_k}(V C_e(U)^(-1)) dV_Haar`.

Haar translation gives exact normalization, and reflection-aligned path design gives the half-space locality needed for the conditional RP factorization. This is modification-specific mathematics, but it is not an external source hypothesis.

### M2. Local analytic weak-field jet

R26 derives on the fixed regular chart

`K_soft / K_Gauss = exp(V_soft)`,

with `V_soft = O(g_k)` in the fixed-order analytic/Cauchy norms required by the later localization argument. The unbounded product-Gaussian tail is handled by the R36 moderate-field/Gaussian-tail split rather than by a global pointwise logarithm.

### M3. Scalar Lemma-3 budget stability

R28 shows that replacing the native raw amplitude `epsilon_1` by

`epsilon_tilde = epsilon_1 + C_soft g_k`

costs only finite linear reserve at the D-stage, improves the P-stage entropy rate, leaves `C_3` unchanged, and preserves post-Lemma-3 closure for sufficiently small `g_k`, conditional on the new term entering the native localization class.

### M4. Native activity-level insertion stability

R43--R44 avoid project-level Gaussian/root reconstruction. CMP116 already works in the product-Gaussian chart after `B'=(C^(k))^(1/2)X` and then localizes the native post-(2.6) integrand to `H(Z,Z0)` and `H(Z)`.

Define

`G_t = G_native * exp(t V_soft)`,  `0 <= t <= 1`,

and let `H_t` be the native CMP116 localization applied to `G_t`. Then one t-derivative inserts one bounded-support `O(g_k)` analytic factor. The same native weakening/random-walk connectivity gives

`|H_1(Z)-H_0(Z)| <= C_soft' g_k exp(-mu' d_k(Z))`

after a finite exponent loss, provided the native localization estimates are uniform on the source analytic domain.

### M5. Finite support anchoring

R45 shows the blocker support can be covered by a fixed finite number of native localization cubes around each anchor. Adjoining that cover to the native seed changes only fixed geometry and anchor multiplicity is absorbed into a finite decay-margin loss.

These five items exhaust the modification-specific mechanics needed by the one-step splice.

## 2. The remaining uniformity is native, not new modification debt

The interpolation `G_t` does not require a new source theorem if the native CMP116 termwise/localization estimates are uniform for fields in the source analytic domain.

The independent source audit identifies precisely this native field-uniformity seam: CMP116 printed p.15 places the termwise estimate window on `U^c_{k+1}(X, alpha_0, alpha_1)`, while printed p.16 around (2.20)/(2.22) contains the field-dependent estimates that still require exact source-to-project matching. This field-uniformity dictionary is already open for the unmodified Bałaban formalization.

Given native uniformity on that domain, `exp(t V_soft)` contributes only a uniformly bounded multiplicative analytic factor for all `t in [0,1]`, and `d/dt` contributes the already-proved `O(g_k)` insertion. Hence interpolation uniformity is derived from:

`CanonicalUjcEmbedding + native CMP116 field-uniformity + R26 bound`.

There is no independent `t`-uniformity source theorem.

## 3. Native Bałaban obligations that remain

The surviving source-facing obligations are all native to the baseline construction or to its exact formal reconstruction.

### N1. Paper-I analytic-domain embedding

`CanonicalUjcEmbedding` remains source-open:

there must exist a fixed canonical outer radius and weak-coupling threshold such that the normalized background chart maps into the native `U_j^c` domain uniformly in scale/volume.

This is a Paper-I/CMP109 analytic-domain fact. It was already needed to justify the native small-field analytic estimates; the RP blocker does not create a new domain species. [7]

### N2. CMP116 field-uniform termwise/localization package

The exact source/dictionary data around the native `H(Z,Z0)` / `H(Z)` construction remain partly open:

- the native index stack and summand identity;
- field uniformity on `U^c_{k+1}(X,alpha_0,alpha_1)`, including the (2.20)/(2.22) estimates;
- termwise majorants feeding Lemma 3;
- component-factorization translation;
- support/measurability translation;
- the D/P/Z0/Z0' resummation dictionaries and threshold dependencies where not yet source-locked.

These are obligations of the unmodified CMP116 cluster-expansion step itself. [21]

### N3. Native covariance/root and Gaussian coordinate dictionaries

CMP99/CMP102/CMP116 covariance/root/Hessian/Gaussian transport remains useful for a complete source-to-project reconstruction, including the unresolved `Delta_1/Delta_a/P_j` identification and project-level Gaussian pushforward normalization.

R42--R44 show these are not blocker gates when the comparison is kept in native CMP116 coordinates. They therefore remain side-record native reconstruction obligations, not RP-modification source debt. [40], [41], [21]

### N4. Complete-density / large-field closure

The full program still depends on the native complete-density and large-field machinery that restores the sectors outside the small-field chart and preserves the inductive form under RG. Those obligations belong to the baseline Bałaban program, not to the RP modification. [59], [22], [31]

## 4. Classification

### Independent source-facing RP-modification obligations

`EMPTY`.

More precisely: after R25--R45, the RP modification introduces no additional external theorem/source hypothesis beyond the native Bałaban domain/localization/complete-density package.

### RP-modification derivations/design obligations

Not empty historically, but already traversed:

- reflected-half-space kernel factorization;
- global gauge/reflection-covariant center;
- local `O(g_k)` analytic jet;
- Gaussian-tail integrability;
- scalar Lemma-3 reserve absorption;
- activity-level interpolation stability;
- bounded support anchoring and anchor multiplicity.

These remain research derivations to formalize if a proof artifact is desired, but they are not unresolved literature assumptions.

### Native source obligations

Nonempty:

- `CanonicalUjcEmbedding`;
- CMP116 analytic-field uniformity / termwise / support / resummation dictionaries;
- side-record covariance/root/Hessian/Gaussian dictionaries;
- complete-density/large-field native closure.

## 5. Strong determination

The correct statement is therefore not

`the RP branch is fully proved`.

It is:

`relative to the native Bałaban one-step and complete-density hypotheses, the RP modification is source-hypothesis neutral`.

Equivalently,

`Native Bałaban closure package -> RP-modified closure`

requires only the modification-internal derivations already isolated in R25--R45 and no new external source theorem.

This upgrades the provisional R36 statement after the intervening precision/covariance/root/support audits: the apparent extra requirements were artifacts of reconstructing source-native coordinates too aggressively.

## 6. Critical-path reset

The RP-specific audit has reached a natural STOP. Continuing to refine `Delta_1`, the physical Gaussian transport, exact root pieces, or project support objects would now be off-critical-path for the blocker.

The next useful cursor returns to the native source baseline and attacks the first unresolved source gate that actually controls the conditional splice.

## Next frontier — YM-R47

**Native analytic-domain / field-uniformity gate.**

Audit the narrow native implication

`CanonicalUjcEmbedding -> CMP116 p.15-p.16 field-uniform estimates (2.20)/(2.22)`

and determine whether the source already supplies one fixed normalized canonical ball on which the termwise localization estimates are uniform.

If this closes, the R44 interpolation is uniformly admissible without any additional modification-specific assumption.

## References

Reused only: [7] CMP109/Paper I; [21] CMP116; [22]/[31] large-field R-operation; [40] CMP99; [41] CMP102; [59] CMP119. No new source ID consumed. Highest remains [79]; [80] remains next.

## Safety boundary

No proof of four-dimensional continuum Yang-Mills existence or a positive continuum mass gap is claimed. R46 is a dependency-classification result: it shows that the RP modification adds no independent source-facing theorem hypothesis relative to the native Bałaban closure package, while that native package itself remains incompletely source-instantiated in this project.