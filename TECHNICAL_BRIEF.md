# Technical brief for independent review

**Project:** [monocap-tech/yangmills](https://github.com/monocap-tech/yangmills)  
**Research frontier:** YM-R103 (completed 2026-10-14); YM-R104 (unconsumed).  
**Prepared:** 2026-10-26.  
**Claim level:** Independent, AI-assisted source audit and conditional mathematical research; **no claimed existence, Osterwalder–Schrader reconstruction, or positive mass-gap proof.**

## Abstract

This project investigates proof interfaces in Bałaban's constructive renormalization-group program for four-dimensional pure Yang–Mills theory. Its current focus is whether local one-step estimates suffice to compare renormalization histories started at two ultraviolet cutoffs. Earlier analysis separated the marginal vacuum-polarization coefficient from the complementary positive-exponent remainder; the current frontier is the motion of background-dependent propagators, nonlinear minimizers, weakened localization operators, and the gauge/Gaussian carriers on which two histories must be compared.

The latest source audit, [YM-R103](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md), recovered a third-party text witness of Bałaban's CMP 99(3), Theorem 3.14: for the source's admissible pair of domain sequences, common-interior random-walk terms cancel and differences of particular propagators acquire extra *spatial* distance-to-domain-change decay. The exact formula is not yet verified against the publisher image. The same source does **not** automatically control changes in background coefficients or histories, nor does it immediately transfer to the later constrained covariance.

An exact decomposition of operator motion, on a **common typed carrier**, distinguishes domain-sequence changes from background changes:

```text
ΔK = [K(Ω1,U1) − K(Ω0,U1)] + [K(Ω0,U1) − K(Ω0,U0)].
```

The project also derives an elementary but useful *conditional* fixed-point stability inequality. If `F0` and `F1` act as contractions with a **common** `q < 1` on the same complete invariant set and `d_i = F_i(d_i)`, then

```text
||d1 − d0|| ≤ ||F1(d0) − F0(d0)|| / (1 − q).
```

Its abstract proof is not a proof that a uniform source-weighted `q`, matched nonlinear charts, or appropriately marked operator differences exist for the actual two-cutoff construction. R103 gives counterexamples against making those transfers without hypotheses.

## Precise outstanding interfaces

1. **Two-cutoff identification:** Explicit common gauge constraints, fluctuation carrier, root/source normalization, and background chart for the compared cutoffs.
2. **Background-response estimate:** A native difference or derivative bound for source propagators at the same admissible domains under changed background/coupling data; ensure it uses the needed weighted norm and has uniform RG constants.
3. **Nonlinear propagation:** Uniform contraction/Lipschitz bounds for the CMP116 nonlinear field substitutions and a positive, absolutely summable marked estimate after weakening differentiation and localization.
4. **Marginal versus regular sector:** Native covariance or summable mismatch for the one-step vacuum-polarization extraction alongside a valid positive-alpha bound on the complementary Bałaban Eq. (0.29) contribution.
5. **Global completion:** Independent treatment of the large-field sector, cutoff/volume limits, physical OS reconstruction, and the positive spectral gap; small-field history control alone does not resolve these.

## Evidence anchors

- [YM-R103 canonical checkpoint](ym/checkpoints/YM_HEAD_R103_20261014.json)
- [YM-R103 detailed pass](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md)
- [CMP99(3)/CMP116 source receipt and limitations](ym/source_receipts/YM_R103_CMP99_3_MARKED_DOMAIN_RECEIPT_20261014.md)
- [YM-R75 earlier vacuum-polarization stationarity reduction](ym/passes/YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md)
- [Evidence status and explicit remaining gates](RESEARCH_STATUS.md)
- [External comparison plan](EXTERNAL_RECONCILIATION.md)

**Source boundary:** Relevant CMP99(3) and CMP116 quotations were read in third-party transcriptions, not verified original page images. Primary original-image custody remains outstanding for CMP109 Eq. (0.29), (5.37), and (5.42). No result in this brief should be interpreted as closing those holds.

## Useful feedback

Most valuable are precise corrections or confirmations of the actual Bałaban hypotheses, a theorem handling **background-dependent two-history operator movement** in a shared norm, an alternative cutoff-coherence construction that explicitly bypasses that requirement, or a counterexample to a proposed transfer. Feedback should name the exact statement, page/equation or repository commit, and which native gate it addresses.

This document is a concise entry point only. The historical pass files and checkpoint ledger remain authoritative for the project's internal claims.
