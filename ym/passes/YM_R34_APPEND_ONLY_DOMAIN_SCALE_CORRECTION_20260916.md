# YM-R34 — append-only source-domain scale correction and fluctuation-envelope supplement

Date: 2026-09-16
Status: CORRECTION/SUPPLEMENT TO COMPLETED YM-R34
Claim status: UNPROVED_RESEARCH_PROGRAM
Preserves unchanged:
- `ym/passes/YM_R34_SOURCE_ANALYTIC_DOMAIN_FLUCTUATION_CARRIER_20260916.md`
- `ym/checkpoints/YM_HEAD_R34_20260916.json`
Live cursor after correction: YM-R35 (unconsumed)

## Why this supplement exists

The first R34 checkpoint correctly refused to invent the coordinate definition of `U^c_{k+1}(X,alpha_0,alpha_1)`, but a deeper source-ledger audit in the same research session recovered two additional first-class facts that materially sharpen the result and correct one earlier interpretation.

This file is append-only: it does not rewrite the prior R34 record.

## 1. The analytic-domain notation is source-located in CMP119, and its radii are scale dependent

The source corpus contains a visually confirmed CMP119 record for the localized regular terms `E^(j)`:

- `E^(j)(X,U,z)` has an analytic extension on `U_j^c(X,alpha_{0,j},alpha_{1,j})`;
- the source records

  `alpha_{0,j} = g_j C_0 (log g_j^{-2})^{q_0}`,

  `alpha_{1,j} = g_j C_1 (log g_j^{-2})^{q_1}`;

- CMP119 equations (2.34)–(2.39) define `U_j^c(X,alpha_0,alpha_1)` by three multiscale regularity/gauge conditions (i)–(iii), note that the auxiliary `beta` may be chosen as a small fixed positive number such as `1/4`, and state gauge invariance of the domain. [59]

The same source record explicitly keeps open the **Paper-I definitions and hypotheses** behind `U_j^c(X,alpha_{0,j},alpha_{1,j})` and the Paper-I bound `(I.1.18)`. Thus the exact coordinate inequalities in conditions (i)–(iii) remain definition-pending; they must not be reconstructed from notation. [7][59]

## 2. Correction to the literal reading of YM-R32

YM-R32 recorded that no source evidence forced a complex analytic radius to collapse with RG depth. That is too strong if read as a statement about the raw group-coordinate widths `alpha_{0,j},alpha_{1,j}`.

The newly recovered source scaling gives

`alpha_{r,j} ~ g_j (log g_j^{-2})^{q_r}`,

so the raw widths shrink as `g_j -> 0` (for fixed logarithmic powers).

What remains structurally favorable is the **canonically normalized** interpretation. In a regular chart

`U = exp(g_j A)`, 

a raw source allowance of schematic size

`|g_j A| <= C g_j (log g_j^{-2})^q`

becomes

`|A| <= C (log g_j^{-2})^q`.

Hence the recovered source scaling does not force collapse of any fixed bounded canonical-field tube; it is compatible with a slowly growing canonical allowance. This statement is a project derivation and still awaits the exact Paper-I coordinate dictionary.

The correction also separates two radius species:

1. the inductive domain widths `alpha_{0,j},alpha_{1,j}`;
2. a smaller local Cauchy/coercivity collar chosen inside that domain.

The fixed-radius discussion in YM-R24/R32 must refer to the latter in normalized variables, not to constant raw `alpha` values.

## 3. Fluctuation support closes at the conservative-envelope level

CMP116 source extraction from the early one-step component localization states that a local term indexed by a connected component `Y0` is built from propagators and fields restricted to `Y0`, and depends only on the gauge/source variables in that localized component together with the source-prescribed base-cube enlargement. The source audit explicitly identifies this as the analogue of the project support-containment input for both active and fluctuation support. [21]

Therefore one does not need a minimal fluctuation-support equality. Introduce a source envelope

`FlucEnv(Y0,z) = Y0 plus the source base cube/collar at z`.

The correct project target is only

`fluctuationSupport(H_{Y0,z}) subset image(FlucEnv(Y0,z))`.

At the later CMP116 localization level, external support remains separately controlled by the R33 envelope

`supp_ext H(Z) subset IntBond(Z)`.

These support species must remain distinct.

## 4. Bondwise product coordinates and nonlocal root transport

CMP116 equations (2.5)–(2.6) perform the change

`B' = (C^(k))^(1/2) X`

and place `X` under the standard product Gaussian `dmu_0`. Thus the ultralocal fluctuation-coordinate species is bond-indexed Lie-algebra variables `X(b)`; the nonlocality is carried by the covariance root in the integrand. [21]

The exact support theorem therefore has the following safe architecture:

1. identify the source `Y0 + base cube/collar` bond/cube envelope;
2. map that finite envelope into project physical bonds;
3. use agreement of product-Gaussian `X(b)` coordinates on the envelope;
4. use the native resummed root-localization agreement from YM-R29–R32;
5. conclude a conservative `fluctuationSupport` inclusion.

No exact finite decomposition of `(C^(k))^(1/2)` is required or asserted.

## 5. Revised R34 determination

The two R34 branches now have different status.

### Fluctuation carrier

**STRUCTURALLY CLOSED TO A FINITE DICTIONARY.**

The source supplies the required conservative carrier shape (`Y0` plus base cube/collar, later embedded in the final localization envelope). What remains is finite source-to-project bond/cube typing, not a new analytic theorem.

### Analytic domain

**DEFINITION-PENDING BUT SCALE STRUCTURE RECOVERED.**

Known:
- source family and equation windows;
- three-condition structure;
- gauge invariance;
- small fixed `beta` option;
- `alpha_{0,j},alpha_{1,j}` scaling with `g_j log^q(g_j^-2)`.

Still missing:
- the exact Paper-I coordinate inequalities in conditions (i)–(iii);
- the exact conversion of those inequalities into canonical `A` coordinates;
- an explicit nested canonical Cauchy collar with verified margin.

## 6. Next frontier remains YM-R35

**Paper-I `U_j^c` coordinate definition / normalized-radius audit.**

The task is now narrower than the original R34 head suggested: recover the Paper-I definition-level inequalities, apply `U=exp(g_j A)` condition by condition, and determine a source-contained canonical collar suitable for the YM-R31/R32 resolvent/root-derivative chain.

No new bibliography source is consumed. Reused: [7] Bałaban CMP109, [21] Bałaban CMP116, [59] Bałaban CMP119. Highest cumulative source ID remains [79]; next new source remains [80].
