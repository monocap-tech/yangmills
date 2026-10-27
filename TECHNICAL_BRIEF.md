# Technical brief for independent review

**Project:** [monocap-tech/yangmills](https://github.com/monocap-tech/yangmills)  
**Research frontier:** YM-R124 (source Landau fluctuation curvature and global winding Wilson preservation, 2026-10-27); YM-R125 (unconsumed).  
**Prepared:** 2026-10-27.  
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

**YM-R106 addition:** an explicit aligned SU(2) finite-Wilson loop observable cospan compares two full normalized cutoff laws through their gauge-invariant half-trace, while an exact abstract coupling criterion requires equality of the *distributions* of the shared source data (or pays their TV mismatch). Proper small-field sectors have positive full Wilson complement probability. The joint-law inequality must keep matched-fiber response, data-law TV and complement masses separate; **none has a native uniform bound yet**. See [YM-R106](ym/passes/YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md).

**YM-R107 source correction:** CMP109 explicitly modifies CMP98's logarithmic contour average to restore Euclidean lattice symmetry and permits two source averaging alternatives; the fixed-average variational data are M^k(U)=V. CMP109 (0.13)–(0.17) supplies a regularity-restricted, gauge-fixed kernel and reference action normalization, not automatically a normalized physical-law pushforward. The abstract positive-kernel formula exposes a fiber-mass/input-tilt term unless a Markov identity is justified. Actual two-cutoff data laws remain open. [Full R107 record](ym/passes/YM_R107_CMP98_CMP109_ACTUAL_AVERAGING_KERNEL_NORMALIZATION_AUDIT_20261026.md).

**R108 refinement:** CMP109 (0.15)-(0.16) separates an FP gauge-orbit identity from an additional cutoff. Exact orbit normalization preserves invariant integrals, a cutoff induces orbit-averaged sigma, and positive kernel t may separately carry mass kappa. Scalar N0 cancels for normalized laws. No native w/chi/kappa or source-image formulas certified. [R108](ym/passes/YM_R108_CMP109_GAUGE_ORBIT_CUTOFF_NORMALIZATION_AUDIT_20261026.md).

**R109 correction:** CMP109 printed (0.15) contains an exponential AND near-identity indicator inside the same z-normalized FP orbit identity. The corresponding (0.16) factor does not independently reweight the invariant law. Its true later fluctuation cutoff (2.9), source composite chi0/chik, and two-run data compatibility remain unproved. Printed source also demands odd L>11. [R109 record](ym/passes/YM_R109_CMP109_ORIGINAL_IMAGE_FP_NORMALIZER_SOURCE_PAIR_GATE_20261026.md).

**YM-R110 source-law correction:** CMP109 (2.9) defines chi_k in pre-linearization B', whereas (2.13) is in final constrained Gaussian B after a nonlinear coordinate change and rescaling. The true chi is therefore pulled back. At fixed admissible real background the law is chi_hat e^R Gaussian/Z; its cutoff mass, interaction oscillation, chart exit and covariance are explicit quantitative gates. Source Z^(k)(U(V)) remains V-dependent in the coarse action and cannot be canceled as a fixed reference scalar. No two-UV-history normalizer or observable-law bound certified. [R110 pass](ym/passes/YM_R110_CMP109_FLUCTUATION_PULLBACK_GAUSSIAN_LAW_20261026.md).

**R111 correction to R110:** CMP109 p.267 defines h supported only on b0(c), which Eq. (2.9) explicitly excludes from the cutoff. Therefore the nonlinear correction B_old=B_new-h D(B_new) has exactly zero restriction to χ-monitored bonds (P h=0). The cutoff under final constrained Gaussian variables is the LINEAR event |g_k P C B|<theta. Its covariance S=P C(C* A C)^-1 C*P* and remaining uniform variance, valid chart/Jacobian, V-dependent determinant and paired histories remain open. [R111 source audit](ym/passes/YM_R111_CMP109_MONITORED_BOND_PROJECTION_GAUSSIAN_CUTOFF_20261026.md).

**YM-R112 source operator upgrade:** CMP109 p267 Dh=I and h supported on b0 imply the exact graph C=(I-hD)E, P C=I, so the monitored covariance is exactly (C* A C)^-1. The reduced Hessian is a finite block graph form. At SU2 identity background the Hessian is K tensor I3 by global Ad SU2 symmetry; each monitored bond has an exact three-dimensional radial Gaussian survival function. CMP99/CMP116 decay does not transfer without a source operator dictionary; numeric source K, coercivity, growing bond counts, chart/Jacobian, V-dependent determinant and genuine cross-UV-law remain OPEN. [R112 pass](ym/passes/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_COVARIANCE_20261027.md).

**YM-R113 predecessor source lock:** printed CMP109 (2.11) directly cites its quadratic form from CMP99 [13] (3.156) but **replaces delta-function gauge fixing with exponential fixing**. CMP99 original-paper OCR locates a regular-background uniform bound for its own constrained precision and Thm.3.15 covariance decay; neither can transfer to Q=C* A C without source gauge/coordinate form comparison. Abstract transfer requires bounded negative gauge defect R and quantitatively identified T. The printed CMP109 (0.29) positive-alpha irrelevant-polymer bound and (5.37),(5.42) polarization/beta formulas were directly viewed; their two-UV estimates remain open. [R113](ym/passes/YM_R113_CMP99_CMP109_REDUCED_PRECISION_GAUGE_FIXING_TRANSFER_20261027.md).

**YM-R114 source refinement:** printed CMP109 (2.5) gives a positive real exponential-gauge quadratic plus cubic corrections, not a generic negative-form perturbation. Based gauge FK=I and DK=0 yield W=(W intersect ker F) plus im K. If source CMP99 hard-slice positive gamma and exact quadratic form match, the four-dimensional soft gauge Hessian has conditional lower bound min(gamma/2,beta/32). CMP99 original printed (3.156)-(3.158) and shared hard slice still need proof; neither covariance constant nor physical UV convergence follows. [R114](ym/passes/YM_R114_CMP109_BASED_GAUGE_QUADRATIC_EXTENSION_20261027.md).

**YM-R115 source and theorem:** CMP99 (3.110),(3.112) OCR uses hard R D* gauge, while CMP109 (2.5) uses based holonomy F. A common based gradient K and invertible GK give exact quotient section map W∩ker G to W∩ker F. Conditional coercivity of the SAME H0 transfers through gauge projection norm, then the positive exponential penalty. The CMP99 reported gamma0, however, explicitly concerns a different written precision C*Delta_k C than (3.156)'s A_k. Matching gauge sections does NOT settle this second covariance operator relation; exact (3.157)–(3.158), source norm and two-UV histories remain open. [R115](ym/passes/YM_R115_CMP99_CMP109_HARD_SLICE_QUOTIENT_AND_PRECISION_SPLIT_20261027.md).

**YM-R116 precision/rank correction:** CMP99 (3.21) gives R as projection onto Δ ker Q', so RD*D:E→ΔE is the Dirichlet Laplacian isomorphism and Ghat=Δ^-1 R D* is the correctly typed hard-gauge coordinate. CMP99 (3.26) Δ_a=A+D R D*+Q*aQ equals A on simultaneous hard/fixed-average constraints. Neither fact identifies later Δ_k from (3.158) with CMP109 A^(k). At isolated L13 identity uniform-average block, based/mean-zero site sections differ by a mean-subtraction map with inverse norm 169, and their gradients differ on interfaces. Native multiscale Ω/V and source numerical gamma remain open. [R116](ym/passes/YM_R116_CMP99_PROJECTED_LAPLACIAN_GAUGE_RANK_AND_PRECISION_20261027.md).

## Target-specification hold

The full Clay problem concerns each compact simple gauge group. This project's particular group, cutoff measures, observables, norms, and UV/volume limit topology have **not** all been instantiated in a single audited target theorem. The present native question is narrower: establishing a lawfully **paired actual two-cutoff fiber** (nested Ω and shared V, or a quantified alternative), comparing normalized cutoff **observable laws**, then deriving quantitative history-response estimates. See [TARGET_SCOPE.md](TARGET_SCOPE.md).

## Precise outstanding interfaces

1. **Two-cutoff identification:** Explicit common gauge constraints, fluctuation carrier, root/source normalization, and background chart for the compared cutoffs.
2. **Background-response estimate:** A native difference or derivative bound for source propagators at the same admissible domains under changed background/coupling data; ensure it uses the needed weighted norm and has uniform RG constants.
3. **Nonlinear propagation:** Uniform contraction/Lipschitz bounds for the CMP116 nonlinear field substitutions and a positive, absolutely summable marked estimate after weakening differentiation and localization.
4. **Marginal versus regular sector:** Native covariance or summable mismatch for the one-step vacuum-polarization extraction alongside a valid positive-alpha bound on the complementary Bałaban Eq. (0.29) contribution.
5. **Global completion:** Independent treatment of the large-field sector, cutoff/volume limits, physical OS reconstruction, and the positive spectral gap; small-field history control alone does not resolve these.

**R124 physical/global source caution:** On a legal real SU2 original fine field after the source Landau gauge change, ηphysical≤ηbackground+4η||Hk||∞. Hk≤CH θk on all original bonds is still a CMP102 source obligation; no numeric CH or uniform Ω halo is certified. Independently flat periodic SU2 configurations share η=0 yet differ in winding Wilson trace. The genuine CMP109 M preserves flat winding exactly when source ribbons are contractible; near-flat aligned winding error ≤n times the R122 local bound. Global winding data should be preserved via the full V, not by curvature-only labels. [R124](ym/passes/YM_R124_FLUCTUATION_CURVATURE_CHART_AND_GLOBAL_HOLONOMY_PASSPORT_20261027.md).

## Evidence anchors

- [YM-R124 checkpoint](ym/checkpoints/YM_HEAD_R124_20261027.json)
- [YM-R124 physical and winding audit](ym/passes/YM_R124_FLUCTUATION_CURVATURE_CHART_AND_GLOBAL_HOLONOMY_PASSPORT_20261027.md)
- [YM-R124 flat Wilson computation](ym/computations/YM_R124_FLAT_WINDING_AND_CURVATURE_TRANSFER_20261027.py)

- [YM-R123 checkpoint](ym/checkpoints/YM_HEAD_R123_20261027.json)
- [YM-R123 source small-field analysis](ym/passes/YM_R123_SOURCE_REGULARITY_TO_NONLINEAR_M_ENTRY_AND_FLUCTUATION_SEAM_20261027.md)
- [YM-R123 chart threshold computation](ym/computations/YM_R123_SMALL_FIELD_CHART_ENTRY_20261027.py)

- [YM-R122 checkpoint](ym/checkpoints/YM_HEAD_R122_20261027.json)
- [YM-R122 nonlinear source curvature pass](ym/passes/YM_R122_NONLINEAR_COARSE_LINK_CURVATURE_AND_TWO_STAGE_GATE_20261027.md)
- [YM-R122 exact arithmetic](ym/computations/YM_R122_NONLINEAR_RIBBON_AND_TWO_STAGE_20261027.py)

- [YM-R121 checkpoint](ym/checkpoints/YM_HEAD_R121_20261027.json)
- [YM-R121 affine/holonomy investigation](ym/passes/YM_R121_AFFINE_HALF_SHIFT_AND_MULTISCALE_TRANSPORT_COCYCLE_20261027.md)
- [YM-R121 exact test](ym/computations/YM_R121_AFFINE_HALF_SHIFT_AND_PATH_COCYCLE_20261027.py)

- [YM-R120 checkpoint](ym/checkpoints/YM_HEAD_R120_20261027.json)
- [YM-R120 historical source/frame audit](ym/passes/YM_R120_CMP95_CMP98_CMP109_HISTORICAL_AXIAL_PATH_AND_FRAME_TRANSPORT_20261027.md)
- [YM-R120 rational common-cell certificate](ym/computations/YM_R120_CORNER_CENTER_LINK_FRAME_L13_20261027.py)

- [YM-R119 checkpoint](ym/checkpoints/YM_HEAD_R119_20261027.json)
- [YM-R119 full coarse-link audit](ym/passes/YM_R119_FULL_COARSE_LINK_DERIVATIVE_CURVATURE_RESPONSE_AND_GAUGE_ACTION_20261027.md)
- [YM-R119 rational full-link test](ym/computations/YM_R119_FULL_LINK_FIRST_VARIATION_L13_20261027.py)

- [YM-R118 checkpoint](ym/checkpoints/YM_HEAD_R118_20261027.json)
- [YM-R118 contour/source-signature audit](ym/passes/YM_R118_CMP98_CMP99_CMP109_CONTOUR_CURVATURE_AND_GAUGE_SIGNATURE_AUDIT_20261027.md)
- [YM-R118 rational test](ym/computations/YM_R118_CONTOUR_CURVATURE_MATRIX_20261027.py)

- [YM-R116 checkpoint](ym/checkpoints/YM_HEAD_R116_20261027.json)
- [YM-R116 projected-Laplacian and interface audit](ym/passes/YM_R116_CMP99_PROJECTED_LAPLACIAN_GAUGE_RANK_AND_PRECISION_20261027.md)

- [YM-R115 checkpoint](ym/checkpoints/YM_HEAD_R115_20261027.json)
- [YM-R115 quotient/precision split](ym/passes/YM_R115_CMP99_CMP109_HARD_SLICE_QUOTIENT_AND_PRECISION_SPLIT_20261027.md)

- [YM-R114 checkpoint](ym/checkpoints/YM_HEAD_R114_20261027.json)
- [YM-R114 positive gauge analysis](ym/passes/YM_R114_CMP109_BASED_GAUGE_QUADRATIC_EXTENSION_20261027.md)

- [YM-R113 checkpoint](ym/checkpoints/YM_HEAD_R113_20261027.json)
- [YM-R113 source-gauge transfer audit](ym/passes/YM_R113_CMP99_CMP109_REDUCED_PRECISION_GAUGE_FIXING_TRANSFER_20261027.md)

- [YM-R112 checkpoint](ym/checkpoints/YM_HEAD_R112_20261027.json)
- [YM-R112 source graph and vacuum analysis](ym/passes/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_COVARIANCE_20261027.md)

- [YM-R111 checkpoint](ym/checkpoints/YM_HEAD_R111_20261026.json)
- [YM-R111 monitored cutoff correction](ym/passes/YM_R111_CMP109_MONITORED_BOND_PROJECTION_GAUSSIAN_CUTOFF_20261026.md)

- [YM-R110 checkpoint](ym/checkpoints/YM_HEAD_R110_20261026.json)
- [YM-R110 source-constrained fluctuation analysis](ym/passes/YM_R110_CMP109_FLUCTUATION_PULLBACK_GAUSSIAN_LAW_20261026.md)

- [YM-R109 checkpoint](ym/checkpoints/YM_HEAD_R109_20261026.json)
- [YM-R109 printed source and FP audit](ym/passes/YM_R109_CMP109_ORIGINAL_IMAGE_FP_NORMALIZER_SOURCE_PAIR_GATE_20261026.md)

- [YM-R108 checkpoint](ym/checkpoints/YM_HEAD_R108_20261026.json)
- [YM-R108 orbit/cutoff audit](ym/passes/YM_R108_CMP109_GAUGE_ORBIT_CUTOFF_NORMALIZATION_AUDIT_20261026.md)

- [YM-R107 canonical checkpoint](ym/checkpoints/YM_HEAD_R107_20261026.json)
- [YM-R107 source averaging/kernel audit](ym/passes/YM_R107_CMP98_CMP109_ACTUAL_AVERAGING_KERNEL_NORMALIZATION_AUDIT_20261026.md)

- [YM-R106 canonical checkpoint](ym/checkpoints/YM_HEAD_R106_20261026.json)
- [YM-R106 finite-Wilson observable cospan and coupling cutset](ym/passes/YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md)

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
