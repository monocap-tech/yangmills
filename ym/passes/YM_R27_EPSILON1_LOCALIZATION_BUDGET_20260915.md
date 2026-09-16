# YM-R27 — epsilon_1 / localization-budget audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R28 (unconsumed)
Claim status: UNPROVED_RESEARCH_PROGRAM

## Target
Determine whether the new reflection-positive single-center heat-kernel blocker, whose raw weak-field local factor differs from the Bałaban Gaussian blocker by `1 + O(g_k)`, fits the actual CMP 116 smallness parameter `epsilon_1`, or whether the source induction requires a parametrically smaller remainder.

## Source-shaped CMP 116 constraints
The visually extracted/source-audited CMP 116 Lemma-3 package gives the following relevant formulas and restrictions (primary source is cumulative reference [21], Bałaban CMP 116):

1. Lemma 3 amplitude:

`|H(Z)| <= C_3 epsilon_1 exp(-(1-8 delta)(L kappa/2) d_{k+1}(Z))`.

2. Post-Lemma-3 effective-action closure requires, among other fixed-parameter restrictions, `O(1) C_3 epsilon_1 <= E_0/2`.

3. The proof defines

`epsilon_2 = K_2 epsilon_1`,

where `K_2 = 2 E_0 C_1 alpha_4^{-1} alpha_6^{-1} M^q exp(C_2 kappa_1)` once the other inductive parameters are fixed, and requires `epsilon_2`, `(L+2)^4 O(1) epsilon_2`, and `2(L+2)^4 O(1) epsilon_2 exp(5 kappa)` to be small.

Thus these restrictions supply an absolute upper bound

`epsilon_1 <= epsilon_*`

for some positive fixed `epsilon_*` after the non-running induction parameters are chosen.

4. CMP 116 Eq. (2.31) uses the rate

`rho = gamma_2 epsilon_1^2 / (20 g_k^2)`

and the exact displayed entropy bracket is equivalent to the source condition

`4 M^4 exp(-gamma_2 epsilon_1^2/(10 g_k^2)) <= gamma_2 epsilon_1^2/(20 g_k^2)`.

Set

`r_k = epsilon_1/g_k`,
`x_k = gamma_2 r_k^2 / 20`.

Then the source condition becomes

`4 M^4 exp(-2 x_k) <= x_k`.

For fixed positive `gamma_2` and `M`, there is a finite threshold `x_*` (hence finite `r_*`) above which this holds. Therefore the source entropy estimate does NOT demand `epsilon_1 = o(g_k)`; rather it enforces a lower comparison of the form

`epsilon_1 >= r_* g_k`

(up to the exact chosen source constants).

## Parameter wedge
Combining the lower entropy constraint and the absolute activity-smallness constraint gives the source-shaped window

`r_* g_k <= epsilon_1 <= epsilon_*`.

For sufficiently small `g_k`, this interval is nonempty.

In particular, one may choose a fixed finite ratio `r > r_*` and set schematically

`epsilon_1 = r g_k`

through the weak-coupling step, provided the remaining source constants are chosen so the absolute smallness conditions hold. More generally, any scale choice with `epsilon_1 -> 0` and `epsilon_1/g_k` uniformly above the entropy threshold is parametrically compatible with these displayed restrictions.

## Comparison with the new blocker
YM-R26 derived on the fixed complex canonical-field tube

`K_soft/K_Gauss = 1 + E_soft`,
`||E_soft||_an <= C_soft g_k`

for a finite scale-independent constant `C_soft` (at each fixed derivative order), before fluctuation/random-walk localization.

Therefore the new local factor has the SAME admissible parametric size as the lower edge of the CMP 116 `epsilon_1` window. It is not too large by power counting.

If the source induction has reserve fraction `0 < eta < 1` available for the new activity, choosing the finite ratio `r` so that

`C_soft <= eta r`

makes

`C_soft g_k <= eta epsilon_1`.

The exact constants still have to be re-run through the source inequalities, but no extra cancellation from `O(g_k)` to `O(g_k^{1+eta})` is forced by the CMP 116 parameter scaling.

## Important qualification
This does NOT prove one can simply add `C_soft g_k` to Bałaban's existing activity without redoing the constants. `epsilon_1` is already used by the original one-step fluctuation integral, and the source proof has a finite smallness margin. The rigorous modified induction must either:

- allocate part of the existing `epsilon_1` budget to the new blocker term, or
- replace `epsilon_1` by a slightly enlarged `tilde epsilon_1 = epsilon_1 + C_soft g_k` and verify every CMP 116 smallness/entropy inequality with the modified constants.

The result of this pass is PARAMETRIC COMPATIBILITY, not constant-level closure.

## Coupling extraction
The `O(g_k)` local factor contains a cubic gauge-invariant interaction and can feed the Wilson-action marginal coordinate after Gaussian integration. As established in YM-R21, the Wilson-action projection must be extracted into the running coupling. The remaining complementary activity may still be `O(g_k)` in amplitude; CMP 116 does not require it to start at a higher power merely to fit the `epsilon_1` scale.

## Determination
The epsilon_1 question does not obstruct the reflection-positive blocker at the level of coupling powers.

The source inequalities have the characteristic double requirement

`g_k \lesssim epsilon_1 \ll 1`,

not `epsilon_1 = o(g_k)`.

Hence the YM-R26 analytic `O(g_k)` raw factor is parametrically admissible. The live deficit has moved from amplitude scaling to CONSTANT-LEVEL STABILITY of the full CMP 116 Lemma-3 localization chain under the extra local activity.

## Next frontier — YM-R28
Stability of the CMP 116 Lemma-3 proof under an added local analytic activity.

Concrete task:

1. introduce an additional raw local term with analytic norm `<= C_soft g_k` and bounded block support;
2. carry it through the product-Gaussian change, weakening parameters, generalized random-walk expansions, and the D/P/Z0/Z0' resummations;
3. identify exactly where the constants `epsilon_2`, `C_3`, `alpha_6`, and the Eq. (2.31) entropy rate change;
4. determine whether the proof is Lipschitz/stable under this perturbation, i.e. whether one obtains a modified bound

`|H_new(Z)| <= C_3' (epsilon_1 + C_soft g_k) exp(-c' d(Z))`

with `C_3'`, `c'` uniform in the UV step and enough reserve to close the next inductive action.

No new bibliography source was consumed. Primary source ownership remains [21] plus the previously custodied equation-level extraction ledger; next new reference remains [76].