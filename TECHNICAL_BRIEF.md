# Technical brief for independent review

**Project:** [monocap-tech/yangmills](https://github.com/monocap-tech/yangmills)  
**Research frontier:** YM-R105 (completed as applicability/negative-control audit on 2026-10-26); YM-R106 (unconsumed).  
**Prepared:** 2026-10-26.  
**Claim level:** Independent, AI-assisted source audit and conditional mathematical research; **no claimed existence, Osterwalder–Schrader reconstruction, or positive mass-gap proof.**

## Abstract

This project investigates proof interfaces in Bałaban's constructive renormalization-group program for four-dimensional pure Yang–Mills theory. Its current focus is whether local one-step estimates suffice to compare renormalization histories started at two ultraviolet cutoffs. Earlier analysis separated the marginal vacuum-polarization coefficient from the complementary positive-exponent remainder; the current frontier is the motion of background-dependent propagators, nonlinear minimizers, weakened localization operators, and the gauge/Gaussian carriers on which two histories must be compared.

The prior internally reviewed source audit, [YM-R103](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md), recovered a third-party text witness of Bałaban's CMP 99(3), Theorem 3.14: for the source's admissible pair of domain sequences, common-interior random-walk terms cancel and differences of particular propagators acquire extra *spatial* distance-to-domain-change decay. The exact formula is not yet verified against the publisher image. The same source does **not** automatically control changes in background coefficients or histories, nor does it immediately transfer to the later constrained covariance.

The subsequent [YM-R104](ym/passes/YM_R104_CMP99_ANALYTIC_BACKGROUND_RESPONSE_CMP116_INTERFACE_20261026.md) located source-text analyticity and same-domain relative-background resolvent response in CMP99(3) (3.37), Theorem 3.4 and (3.64)–(3.65), (3.84)–(3.86). This gives a perturbation smallness parameter for eligible propagators **only when both backgrounds occupy the required source chart**. No actual cutoff-pair relative amplitude or common gauge/Gaussian carrier has been constructed. [YM-R105](ym/passes/YM_R105_PAIRED_VARIATIONAL_CARRIER_LAW_SEPARATION_20261026.md) then identified the missing **paired-input construction**: physical-scale equality and independent curvature bounds do not imply equal prescribed gauge data on nested domain layers. It also shows that pointwise matching of variational fibers cannot replace a law-level comparison of normalized Yang–Mills cutoff measures.

An algebraic decomposition of operator motion is available **only where all three operators live on a common typed space, including a defined and admissible intermediate K(Ω0,U1)**:

```text
ΔK = [K(Ω1,U1) − K(Ω0,U1)] + [K(Ω0,U1) − K(Ω0,U0)].
```

The displayed identity alone is **not a native comparison theorem**. The CMP99(3) two-domain estimate would additionally require both domain sequences to satisfy the source hypotheses at the same background U1; the background-motion bracket and any gauge/Gaussian carrier transport require separate control. See [TARGET_SCOPE.md](TARGET_SCOPE.md).

The project also derives an elementary but useful *conditional* fixed-point stability inequality. If `F0` and `F1` act as contractions with a **common** `q < 1` on the same complete invariant set and `d_i = F_i(d_i)`, then

```text
||d1 − d0|| ≤ ||F1(d0) − F0(d0)|| / (1 − q).
```

Its abstract proof is not a proof that a uniform source-weighted `q`, matched nonlinear charts, or appropriately marked operator differences exist for the actual two-cutoff construction. R103 gives counterexamples against making those transfers without hypotheses.

## Target-specification hold

The full Clay problem concerns each compact simple gauge group. This project's particular group, cutoff measures, observables, norms, and UV/volume limit topology have **not** all been instantiated in a single audited target theorem. The present native question is narrower: establishing a lawfully **paired actual two-cutoff fiber** (nested Ω and shared V, or a quantified alternative), comparing normalized cutoff **observable laws**, then deriving quantitative history-response estimates. See [TARGET_SCOPE.md](TARGET_SCOPE.md).

## Precise outstanding interfaces

1. **Two-cutoff identification:** Explicit common gauge constraints, fluctuation carrier, root/source normalization, and background chart for the compared cutoffs.
2. **Background-response estimate:** A native difference or derivative bound for source propagators at the same admissible domains under changed background/coupling data; ensure it uses the needed weighted norm and has uniform RG constants.
3. **Nonlinear propagation:** Uniform contraction/Lipschitz bounds for the CMP116 nonlinear field substitutions and a positive, absolutely summable marked estimate after weakening differentiation and localization.
4. **Marginal versus regular sector:** Native covariance or summable mismatch for the one-step vacuum-polarization extraction alongside a valid positive-alpha bound on the complementary Bałaban Eq. (0.29) contribution.
5. **Global completion:** Independent treatment of the large-field sector, cutoff/volume limits, physical OS reconstruction, and the positive spectral gap; small-field history control alone does not resolve these.

## Evidence anchors

- [YM-R105 canonical checkpoint](ym/checkpoints/YM_HEAD_R105_20261026.json)
- [YM-R105 native pair/law test](ym/passes/YM_R105_PAIRED_VARIATIONAL_CARRIER_LAW_SEPARATION_20261026.md)
- [YM-R105 pinned source receipt](ym/source_receipts/YM_R105_PAIRED_CARRIER_SOURCE_RECEIPT_20261026.md)
- [YM-R104 canonical checkpoint (historical)](ym/checkpoints/YM_HEAD_R104_20261026.json)
- [YM-R104 source text and transfer cutset](ym/passes/YM_R104_CMP99_ANALYTIC_BACKGROUND_RESPONSE_CMP116_INTERFACE_20261026.md)
- [YM-R104 source receipt](ym/source_receipts/YM_R104_CMP99_BACKGROUND_RESPONSE_RECEIPT_20261026.md)
- [YM-R103 canonical checkpoint (historical)](ym/checkpoints/YM_HEAD_R103_20261014.json)
- [YM-R103 detailed pass](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md)
- [CMP99(3)/CMP116 source receipt and limitations](ym/source_receipts/YM_R103_CMP99_3_MARKED_DOMAIN_RECEIPT_20261014.md)
- [YM-R75 earlier vacuum-polarization stationarity reduction](ym/passes/YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md)
- [Evidence status and explicit remaining gates](RESEARCH_STATUS.md)
- [R103 editorial and evidence errata](REVIEW_ERRATA_20261026.md)
- [Typed target scope](TARGET_SCOPE.md)
- [External comparison plan](EXTERNAL_RECONCILIATION.md)

**Source boundary:** Relevant CMP99(3) and CMP116 quotations were read in third-party transcriptions, not verified original page images. Primary original-image custody remains outstanding for CMP109 Eq. (0.29), (5.37), and (5.42). No result in this brief should be interpreted as closing those holds.

## Useful feedback

Most valuable are precise corrections or confirmations of the actual Bałaban hypotheses, a theorem handling **background-dependent two-history operator movement** in a shared norm, an alternative cutoff-coherence construction that explicitly bypasses that requirement, or a counterexample to a proposed transfer. Feedback should name the exact statement, page/equation or repository commit, and which native gate it addresses.

The current source extracts and algebra have **not** undergone end-to-end independent mathematical verification. This document is a concise entry point only. The historical pass files and checkpoint ledger remain authoritative for the project's internal claims.
