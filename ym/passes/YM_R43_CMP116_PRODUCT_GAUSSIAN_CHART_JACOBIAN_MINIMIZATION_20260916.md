# YM-R43 — CMP116 product-Gaussian chart / Jacobian minimization

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R42_20260916.json`
Next cursor: YM-R44 (unconsumed)

## Question

R42 replaced the blocker-critical precision-first route by the source-native covariance/root route. R43 asks whether CMP116 (2.5)--(2.7) itself contains enough normalized coordinate structure for the reflection-positive blocker, and in particular whether determinant/Jacobian normalization is a new blocker-specific theorem debt.

## Preflight

The durable repository head was recovered as

`YM-R42 COMPLETE -> YM-R43`, with R43 unconsumed.

No new bibliography source is introduced. The controlling primary source remains cumulative [21], Balaban CMP116, with [7] as the Part-I handoff and [79] retained for the non-critical CMP99 covariance/propagator side record.

## 1. What CMP116 (2.5)--(2.6) source-identifies

The already-custodied primary-source extraction gives the following source-internal structure.

For a term already localized by the D/Y0 decomposition, with the bond set `Y0^{c,*}` and smallest localization domain `Z0`, the correlated fluctuation integral is first represented after conditioning on `Z0^c`. Balaban then makes the linear covariance-root change

`B' = (C^(k))^(1/2) X`.

Equation (2.6) writes the resulting integral against the product standard Gaussian `dmu0(X)`. The displayed one-coordinate density is

`dX(b) exp(-|X(b)|^2/2) / (2*pi)^(dim(g)/2)`.

Thus the source-native integration variable is a finite product of Lie-algebra coordinates `X(b)`, with covariance/root dependence moved into the transformed integrand through `(C^(k))^(1/2)` and the function `G`.

This is stronger than merely knowing that a covariance exists: CMP116 itself chooses product-Gaussian coordinates before the root-localization step.

## 2. `C^(k)(Z0)` must remain typed as a conditioned/localized covariance datum

The source extraction records that the term is conditioned on `Z0^c` before the `B'` change and that the post-(2.6) integrand contains

`G(Z0, X, C^(k)(Z0), (C^(k))^(1/2), Delta_k)`.

Therefore R43 does not identify `C^(k)(Z0)` with a naive matrix compression such as `1_Z0 C^(k) 1_Z0`, nor with the inverse of `Delta_k`. It is the covariance datum produced by the source conditioning/localization convention.

The exact source-to-project finite carrier and restriction map remain part of the native support/coordinate dictionary. No extra analytic theorem is inferred from the notation.

## 3. Source-internal normalization versus project-level pushforward

Two distinct statements must not be conflated.

### Source-internal statement

CMP116 already displays the transformed integral in the normalized product measure `dmu0(X)` after the covariance-root change. At the level of the native source calculation, the determinant/Jacobian required for the change of variables has therefore already been accounted for in the equality leading to (2.6).

One may use the source representation

`integral in B' = integral in X against dmu0`

as the native starting chart for the subsequent cluster expansion.

### Project-transport statement

A stronger repository theorem of the form

`balabanCMP116Dmu0.map (D.gaussianRootMap root) = physicalGaussian`

still requires three dictionary facts:

1. Balaban's source map `X -> B' = (C^(k))^(1/2)X` equals the project root-coordinate map;
2. the source correlated `B'` law equals the repository object called `physicalGaussian`;
3. the determinant/Jacobian-normalized source pushforward equals that law with the repository normalization conventions.

The external formal source audit correctly leaves these as separate source records. The visual display of (2.5)--(2.6) alone does not prove the project pushforward equality.

Hence the determinant/Jacobian is **open as transport custody**, but not as a missing normalization inside Balaban's own Eq. (2.6) representation.

## 4. The RP blocker does not require the stronger transport theorem

R26 established on the regular canonical tube that the preferred exact blocker factors relative to the chosen Gaussian reference as

`K_soft / K_Gauss = exp(V_soft)`

with `V_soft = O(g_k)` in the required fixed-order analytic norms (equivalently `1 + O(g_k)` before taking the local logarithm).

Therefore, once the native CMP116 Gaussian chart is used, the modified integral has the schematic form

`integral K_Gauss(B') * exp(V_soft(B')) * F(B') dB'`.

Applying the *same already-existing* source change of variables

`B' = R_k X`,  `R_k = (C^(k))^(1/2)`,

gives

`integral exp(V_soft(R_k X)) * F(R_k X) dmu0(X)`.

The extra multiplicative factor does not alter the coordinate map and creates no second Jacobian. The only new work is localization/estimation of the composed activity `V_soft(R_k X)`, which is exactly the R29 obligation already reduced to native root localization.

Thus the blocker does not need a separately sourced theorem identifying a repository `physicalGaussian` measure.

## 5. Critical-path object minimizes again

R42's provisional

`NativeFluctuationCovarianceCertificate`

is still stronger than what the blocker itself consumes.

For the blocker-critical splice it can be replaced by the source-native object

### `CMP116ProductGaussianChart`

consisting of:

- the conditioned/localized fluctuation chart associated with `Z0`;
- the product standard Gaussian measure `dmu0(X)`;
- the native source map `B' = (C^(k))^(1/2) X`;
- the fact that the post-change integrand contains the same covariance-root object to which CMP116 (2.7)--(2.10) applies.

The project-level covariance/root coordinate equivalence and correlated-Gaussian pushforward theorem remain useful for an independent formal reconstruction, but they are not prerequisites for inserting the RP soft activity into Balaban's native cluster-expansion chart.

## 6. What remains source-native and blocker-critical

The actual blocker-critical debt after R43 is now:

1. `CanonicalUjcEmbedding` — the Paper-I analytic-domain inclusion;
2. the native CMP116 product-Gaussian chart just described (already source-attested at the representation level);
3. the CMP116 (2.7)--(2.10) root/localization-domain dictionary needed to transfer the local factor to localized `H(Z)` activities;
4. the finite support/domain dictionary mapping Balaban's localization domains to the project activity support notions.

The following are no longer blocker-critical:

- exact CMP102 `Delta_1` / CMP99 `Delta_a` / project precision identity;
- project-level `physicalGaussian` pushforward equality;
- an independently sourced determinant/Jacobian formula beyond the native Eq. (2.6) rewrite;
- the local `O(g_j)` precision-defect theorem.

Those remain legitimate side-record obligations for a fully reconstructed physical operator/measure dictionary.

## 7. Negative results / guardrails

- Do not claim `C^(k)(Z0)` is simple coordinate restriction unless the source definition says so.
- Do not infer `Delta_k = (C^(k))^-1` from the post-(2.6) argument list.
- Do not claim the source Eq. (2.6) display proves the repository pushforward equality to `physicalGaussian`.
- Do not introduce a second Jacobian for the RP factor: multiplication of the integrand commutes with the already-fixed source change of variables by composition.
- Do not require a project covariance/Hessian reconstruction before using the native CMP116 product-Gaussian chart.

## Determination

R43 closes the blocker-specific Jacobian question.

The determinant/Jacobian normalization is already spent inside Balaban's native (2.5)--(2.6) transformation to `dmu0`; it remains open only when one insists on transporting that source identity into a separately named project `physicalGaussian` measure.

Because the RP blocker is an analytic multiplicative correction relative to the same Gaussian reference factor, its insertion leaves the native change of variables untouched and introduces no new measure-normalization theorem.

Accordingly:

`RP local factor -> compose with B'=(C^(k))^(1/2)X -> dmu0 product Gaussian -> native root localization`

is the minimized blocker-critical route.

## Next frontier — YM-R44

**CMP116 (2.7)--(2.10) localization-domain dictionary minimization.**

Determine whether the remaining root-localization/support debt can likewise be stated source-natively at the level of the already-produced activities `H(Z,Z0)` and `H(Z)`, rather than requiring an exact project reconstruction of `(C^(k))^(1/2)` into root pieces. In particular, isolate the minimal theorem needed to show that multiplying the native post-(2.6) integrand by a bounded-support analytic `O(g_k)` factor preserves the source `H(Z)` localization/decay class.

YM-R44 is unconsumed here.

## References

Reused: [7] CMP109; [21] CMP116; [79] CMP99 only as a non-critical side-record reference. No new source ID consumed. Highest remains [79]; [80] remains next.
