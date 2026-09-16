# YM-R28 — Lemma-3 perturbative stability / constant-level localization audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R29 (unconsumed)

## Entry state

Canonical entry:

`YM-R27 COMPLETE -> YM-R28`

R27 established that the RP-compatible single-center heat-kernel blocker contributes a raw local analytic factor of size `C_soft g_k`, and that CMP116 admits a parametric wedge `r_* g_k <= epsilon_1 <= epsilon_*`.

## Constant-level substitution

Define the total raw activity budget

`epsilon_tilde := epsilon_1 + C_soft g_k`.

The CMP116 Lemma-3 source chain is stable at the scalar-constant level under this substitution, provided the added activity can be localized with the same geometric weight.

### D-stage / Eq. (2.28)-(2.29)

The source smallness condition preceding the D-sum is linear in epsilon_1:

`2 E0 epsilon_1 C1 alpha4^{-1} alpha6^{-1} M^q exp(C2 kappa1) exp(5 kappa) <= 1`.

Replacing epsilon_1 by epsilon_tilde only consumes linear smallness reserve. The D-family summability Eq. (2.29) itself depends on alpha6, delta, kappa and geometry, not on epsilon_1, so the decay geometry is unchanged once the stronger linear smallness condition is met.

### P-stage / Eq. (2.31)

The source rate is

`rho = gamma2 epsilon_1^2 / (20 g_k^2)`.

With epsilon_tilde >= epsilon_1, rho increases. The source bracket `4 M^4 exp(-2 rho) <= rho` is monotone favorable in rho: the left side decreases and the right side increases. Therefore adding positive activity budget does not worsen the P-entropy condition.

### epsilon_2 and C3

The source extraction records

`epsilon_2 = 2 E0 epsilon_1 C1 alpha4^{-1} alpha6^{-1} M^q exp(C2 kappa1)`

and

`C3 = 2 (L+2)^4 O(1) 2 E0 C1 alpha4^{-1} alpha6^{-1} M^q exp(C2 kappa1)`.

Thus epsilon_2 scales linearly with the substituted amplitude, while C3 itself is independent of epsilon_1. The Lemma-3 endpoint becomes

`|H_new(Z)| <= C3 epsilon_tilde exp(-(1-8 delta)(L kappa/2) d_{k+1}(Z))`

provided the new activity enters the same source localization class.

### Post-Lemma-3 exponentiation

The effective-action closure condition is linear in epsilon_1, schematically `O(1) C3 epsilon_1 <= E0/2`. Replacing epsilon_1 by epsilon_tilde consumes a finite reserve but does not alter the decay exponent or C3. If epsilon_tilde = r g_k with finite r, the condition holds for sufficiently small g_k.

## Two-parameter hierarchy

Choose a finite ratio r satisfying both:

1. the Eq. (2.31) lower threshold in epsilon/g;
2. `r > C_soft` plus the pre-existing activity ratio needed by the original one-step bound.

Then choose g_k small enough that every linear smallness condition involving epsilon_tilde = r g_k is satisfied. Hence any finite C_soft can be absorbed parametrically without demanding an additional power of g_k.

## Determination

At the constant/combinatorial level, the CMP116 Lemma-3 proof is perturbatively open under a bounded-support analytic activity of size O(g_k). The substitution

`epsilon_1 -> epsilon_tilde = epsilon_1 + C_soft g_k`

preserves the source decay exponent and C3; D-stage conditions worsen only linearly, P-stage entropy improves, and post-Lemma-3 closure is recovered by taking g_k smaller.

This does **not** yet prove closure of the RP blocker. The remaining nontrivial edge is before Lemma 3: the new local factor must be transported through the product-Gaussian covariance-root change and weakening/random-walk localization into an activity with the same source support/decay geometry. Existing source audits identify this root-localization/support dictionary as a genuinely nontrivial interface even for the source-shaped formalization.

## Negative results / guardrails

- Do not claim `H_new` satisfies Lemma 3 merely from scalar amplitude replacement; the geometric localization hypothesis must be proved.
- Do not change alpha6 or the decay exponent unless required; fixed source choices suffice if g_k is made small enough.
- Do not treat the P-stage as a smallness obstruction: increasing epsilon/g improves its entropy rate.
- Do not truncate the exact RP kernel measure. The local logarithm/activity is only a small-field analytic proof coordinate.

## Next frontier

`YM-R29 — local-log / covariance-root localization audit`

Target: on the fixed complex tube, use `K_soft/K_Gauss = 1 + E_soft`, `||E_soft|| <= C_soft g_k`, to define a local analytic `V_soft = log(1+E_soft)` for sufficiently small g_k; then prove that after the CMP116 covariance-root change and weakening/random-walk expansion, `V_soft` produces localized pieces with exponential root/support decay compatible with the source `H(Z,Z0)` / `H(Z)` construction.

No new source ID consumed. Next new cumulative source remains [76].
