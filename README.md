# Yang–Mills — constructive renormalization-group research notes

**An independent, AI-assisted mathematical research notebook on four-dimensional pure Yang–Mills theory, focused on Bałaban's constructive renormalization-group program.**

> **Research status: OPEN / UNPROVED.** This repository does **not** claim a rigorous construction of the four-dimensional continuum Yang–Mills theory, satisfaction of the Osterwalder–Schrader axioms, or a strictly positive physical mass gap. Its numbered passes contain source audits, elementary mathematical deductions, conditional interfaces, and explicitly unresolved proof obligations. They have not been independently peer-reviewed or checked end-to-end by a formal proof assistant.

| Canonical state | Value |
| --- | --- |
| Last completed native pass | **[YM-R122](ym/passes/YM_R122_NONLINEAR_COARSE_LINK_CURVATURE_AND_TWO_STAGE_GATE_20261027.md)** — 2026-10-27 |
| Next native cursor | **YM-R123** — not yet consumed |
| Official research checkpoint | **[YM_HEAD_R122](ym/checkpoints/YM_HEAD_R122_20261027.json)** |
| Public status snapshot | **2026-10-27** (documentation update, not a new proof pass) |

## Start here

| Document | Purpose |
| --- | --- |
| **[Target scope and native proof obligation](TARGET_SCOPE.md)** | Full Clay target versus our still-uninstantiated Yang–Mills construction and admissible two-cutoff comparison |
| **[Research status and evidence ledger](RESEARCH_STATUS.md)** | Internally checked deductions, source evidence, and native open gates |
| **[Technical brief for independent review](TECHNICAL_BRIEF.md)** | One-page synopsis of the exact two-cutoff mathematical obstruction and useful review questions |
| **[YM-R122 investigation](ym/passes/YM_R122_NONLINEAR_COARSE_LINK_CURVATURE_AND_TWO_STAGE_GATE_20261027.md)** | Exact SU2 nonlinear CMP109 source M single-step and deterministic two-stage curvature bounds under full-halo and small-log chart gates; no normalized UV law |
| **[YM-R121 investigation](ym/passes/YM_R121_AFFINE_HALF_SHIFT_AND_MULTISCALE_TRANSPORT_COCYCLE_20261027.md)** | Source half-shift fine lattice aligns one-step old corner/new center blocks; scale shifts telescope; geometric two-stage path cocycle 2808 plaquettes, not RG composition |
| **[YM-R120 investigation](ym/passes/YM_R120_CMP95_CMP98_CMP109_HISTORICAL_AXIAL_PATH_AND_FRAME_TRANSPORT_20261027.md)** | CMP98 historical contour source-locked to CMP95 (1.7), old corner/new center coarse-frame transport, and conditional L13 common-cell sparse coefficient -1/114244; source affine offset and covariance remain open |
| **[YM-R119 investigation](ym/passes/YM_R119_FULL_COARSE_LINK_DERIVATIVE_CURVATURE_RESPONSE_AND_GAUGE_ACTION_20261027.md)** | Printed CMP109 full coarse-link tangent; declared L13 axial-vs-sym exact sparse response 99/28561 and curvature sup bound 10584/169; full-field vs fixed-background gauge contexts distinguished |
| **[YM-R118 investigation](ym/passes/YM_R118_CMP98_CMP99_CMP109_CONTOUR_CURVATURE_AND_GAUGE_SIGNATURE_AUDIT_20261027.md)** | Exact source-local symmetric versus single contour derivative = -1/2 plaquette curl, rational code certificate, gauge slice shear and CMP98/CMP99 averaging signature caution |
| **[YM-R117 investigation](ym/passes/YM_R117_CMP99_MULTISCALE_GAUGE_INTERTWINING_AND_COARSE_SEAM_20261027.md)** | CMP99 Q_j D=D_j Q'_j; exact one-layer gauge section; inter-block term is coarse-gauge coboundary, while old Q vs new M remains open |
| **[YM-R116 investigation](ym/passes/YM_R116_CMP99_PROJECTED_LAPLACIAN_GAUGE_RANK_AND_PRECISION_20261027.md)** | CMP99 projected Dirichlet Laplacian hard-gauge rank closed on ker Q'; source Delta_a=A on hard/fixed-average slice; L13 based/mean-zero interblock seam |
| **[YM-R115 investigation](ym/passes/YM_R115_CMP99_CMP109_HARD_SLICE_QUOTIENT_AND_PRECISION_SPLIT_20261027.md)** | Exact quotient transport between CMP99 hard RD* and CMP109 holonomy gauge slices conditional on GK rank; separate Delta_k/A_k precision gap |
| **[YM-R114 investigation](ym/passes/YM_R114_CMP109_BASED_GAUGE_QUADRATIC_EXTENSION_20261027.md)** | CMP109 printed (2.5) positive gauge quadratic, exact based gauge splitting and conditional hard-to-soft coercivity; CMP99 hard slice still open |
| **[YM-R113 investigation](ym/passes/YM_R113_CMP99_CMP109_REDUCED_PRECISION_GAUGE_FIXING_TRANSFER_20261027.md)** | Exact CMP109 (2.11) citation of CMP99 (3.156), with delta-to-exponential gauge switch; conditional coercivity bridge and CMP109 (0.29),(5.37),(5.42) original images |
| **[YM-R112 investigation](ym/passes/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_COVARIANCE_20261027.md)** | Source p267 Dh=I gives exact graph C=(I-hD)E and S=(C*AC)^-1; SU2 identity vacuum color isotropy and Maxwell cutoff tail; numerical bounds and cross-cutoff law open |
| **[YM-R111 investigation](ym/passes/YM_R111_CMP109_MONITORED_BOND_PROJECTION_GAUSSIAN_CUTOFF_20261026.md)** | Exact Ph=0 from printed CMP109: nonlinear correction only on excluded b0 bonds, so monitored Gaussian cutoff has no nonlinear shift; native covariance gate open |
| **[YM-R110 investigation](ym/passes/YM_R110_CMP109_FLUCTUATION_PULLBACK_GAUSSIAN_LAW_20261026.md)** | CMP109 pre-linearization chi pullback, real conditional Gaussian/interaction law, exact cutoff and TV bounds; true two-history transport open |
| **[YM-R109 investigation](ym/passes/YM_R109_CMP109_ORIGINAL_IMAGE_FP_NORMALIZER_SOURCE_PAIR_GATE_20261026.md)** | Printed-source verification: CMP109 local FP exponential and indicator are one unit-mass orbit identity; true remaining cutoff-law gate open |
| **[YM-R108 investigation](ym/passes/YM_R108_CMP109_GAUGE_ORBIT_CUTOFF_NORMALIZATION_AUDIT_20261026.md)** | FP orbit normalization versus cutoff selection and underlying kernel mass; actual source two-run law open |
| **[YM-R107 investigation](ym/passes/YM_R107_CMP98_CMP109_ACTUAL_AVERAGING_KERNEL_NORMALIZATION_AUDIT_20261026.md)** | CMP109 Euclidean symmetric averaging alternatives, source M^k variational data, and restricted-kernel normalization cutset; source-law transport open |
| **[YM-R106 investigation](ym/passes/YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md)** | One aligned physical Wilson loop cospan, maximal data coupling criterion and unavoidable large-field mass; no native RG-law bound |
| **[YM-R105 investigation](ym/passes/YM_R105_PAIRED_VARIATIONAL_CARRIER_LAW_SEPARATION_20261026.md)** | Refute-first cutoff-pair admissibility audit: physical-scale equality is not shared prescribed data; deterministic fiber comparisons are not normalized RG law comparisons |
| **[YM-R104 investigation](ym/passes/YM_R104_CMP99_ANALYTIC_BACKGROUND_RESPONSE_CMP116_INTERFACE_20261026.md)** | Previous analytic background response source audit, with native cutoff transfer still open |
| **[YM-R103 investigation](ym/passes/YM_R103_CMP99_DOMAIN_MARK_NONLINEAR_MINIMIZER_AUDIT_20261014.md)** | Previous domain-motion source finding, operator decomposition, conditional fixed-point interface and counterexamples |
| **[R104 source receipt](ym/source_receipts/YM_R104_CMP99_BACKGROUND_RESPONSE_RECEIPT_20261026.md)** | CMP99(3) background-resolvent and CMP116 analytic sources with exact text locators and image holds |
| **[R103 source receipt](ym/source_receipts/YM_R103_CMP99_3_MARKED_DOMAIN_RECEIPT_20261014.md)** | Earlier domain-marked comparison sources and provenance |
| **[R105 terminology](ym/terminology/YM_R105_TERMINOLOGY_REGISTRY_20261026.md)** | Paired fiber, probability law, observable cospan and exact-shell distinctions |
| **[Terminology registry (historical R103)](ym/terminology/YM_R103_TERMINOLOGY_REGISTRY_20261014.md)** | Earlier locality, minimizer and carrier terminology |
| **[External research interfaces](EXTERNAL_RECONCILIATION.md)** | Proposed comparison with new constructive Yang–Mills research; no external claim adopted as proved |
| **[Review errata and provenance](REVIEW_ERRATA_20261026.md)** | Non-destructive clarification of R103 bibliography, source status, and comparison hypotheses |
| **[Contribution and rights guidance](CONTRIBUTING.md)** | How to report a mathematical correction; [rights and licensing hold](RIGHTS_AND_ATTRIBUTION.md) |
| **[YM-R75 investigation](ym/passes/YM_R75_BETA_INDEX_SEMANTICS_PHYSICAL_SCALE_STATIONARITY_20260922.md)** | Earlier marginal-beta / vacuum-polarization source question and its conditional reduction |

The historical research record remains in `ym/passes/`, `ym/checkpoints/`, `ym/references/`, `ym/source_receipts/`, and `ym/terminology/`. These documents are not intended to be read as a single, completed proof.

## Technical synopsis

The current focus is the gap between **local one-step RG estimates** and a sufficiently uniform **two-cutoff continuum comparison**. **R104** recovered CMP99(3) Theorem 3.4 and (3.64)–(3.65), (3.84)–(3.86) as a *fixed-domain, relative-background* analytic/resolvent response in its (3.37) complex chart. The source's smallness parameter is the **relative background perturbation**, not an established summable cutoff-history defect. **YM-R105** showed that the older exact physical-scale identity and independent small-field regularity do **not** supply the external draft's stipulated common layers, nested domains, or equal prescribed (V). **YM-R106** constructs a gauge-invariant finite-Wilson physical-loop observable cospan and shows the exact normalized data-matching/large-field accounting needed. **YM-R107** locates the distinct CMP98/CMP109 averaging definitions and the source kernel/normalizer cutset. **YM-R108** separates FP gauge-orbit identity, cutoff selector, and underlying kernel mass; a background-independent reference scalar cancels in normalized laws. **YM-R109** visually verifies CMP109 (0.15)–(0.17), corrects the earlier assumption that its normalized FP indicator causes independent physical reweighting, and locates the separate (2.9) fluctuation cutoff. **YM-R110** types the true post-coordinate-change fluctuation cutoff and gives exact conditional cutoff/interaction and Gaussian-TV estimates. **YM-R111** proves the nonlinear D correction is zero on (2.9)'s monitored bonds; Gaussian covariance, chart and paired-law defect are the correct remaining gates for **YM-R112**. In earlier passes, alignment of physical lattice spacing reduced the marginal-beta coherence question to an appropriate covariance or decay estimate for the freshly extracted one-step vacuum-polarization tensor. It did *not* prove that estimate.

R102–R103 separate two effects that would otherwise be conflated:

- **Spatial-domain motion:** for certain source operators, a third-party text transcription of Bałaban's CMP 99(3), Theorem 3.14, supports an extra distance-to-domain-change factor from random-walk cancellation, subject to its stated hypotheses.
- **Background, coupling-history, and carrier motion:** comparing genuinely different ultraviolet-cutoff histories also changes operator coefficients, nonlinear minimizers, source charts, gauge constraints, and possibly Gaussian carriers. A spatial domain mark does **not** automatically control those changes.

The basic **algebraic** decomposition, only when all operators and the intermediate term are defined on an admissible common space, is

```text
K(Ω₁,U₁) − K(Ω₀,U₀)
  = [K(Ω₁,U₁) − K(Ω₀,U₁)]
  + [K(Ω₀,U₁) − K(Ω₀,U₀)],
```

**This is not itself a source theorem.** In addition to identifying a common carrier, the intermediate term K(Ω₀,U₁) must exist in the required source domain; both domain sequences must satisfy the comparison theorem's hypotheses at the same background U₁. Separately controlling the second bracket and transporting gauge/Gaussian carriers may add further defects. The first bracket is domain motion; the second is background/coefficient motion. See [TARGET_SCOPE.md](TARGET_SCOPE.md). R103 also proves an abstract fixed-point difference inequality when two maps share a uniform contraction factor, but no suitable common weighted contraction margin has yet been certified for the actual two-cutoff Yang–Mills data.

The native frontier therefore remains: **background-sensitive propagator and nonlinear-minimizer response, actual gauge/carrier identification, rooted historical decay, and the marginal/remainder source estimates**. Large-field closure, continuum/OS construction, and the spectral mass gap remain separate unresolved requirements. See the [complete gate ledger](RESEARCH_STATUS.md).

## Evidence discipline

We distinguish:

- **Source-text witness** from **original publisher-image verification**; OCR can corrupt mathematical symbols and hypotheses.
- **Abstract mathematical deductions** from a **proof that their hypotheses hold** for the lattice-gauge construction.
- **A result about one RG trajectory** from **a uniform estimate comparing two trajectories**.
- **Domain-distance decay** from **decay in inherited coupling-history age**.
- **External announcements or draft manuscripts** from **independently verifiable theorems**.

The project retains failed transfers and counterexamples rather than silently promoting conditional reasoning to closure. The [status ledger](RESEARCH_STATUS.md) gives the operational evidence categories and gate-closure criteria.

## Relationship to newer work

On 2026-10-26, OpenAI [announced](https://openai.com/index/building-scientific-understanding-with-academic-communities/) an AI-generated Yang–Mills **existence** result built on Bałaban's approach; its physics proof artifacts were not publicly released in that announcement, and it did not claim a positive mass gap. The [Sussman–Alpöge research repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) and [Armstrong's O(N) formalization](https://github.com/scottnarmstrong/balaban-lean) offer separate public lines of investigation. They are **leads for precise comparison**, not results incorporated into this project's theorem ledger.

See [External research interfaces](EXTERNAL_RECONCILIATION.md) for the comparison protocol. **[YM-EXT-01's focused crosswalk](ym/external/YM_EXT_01_EXTERNAL_YM4_NATIVE_CROSSWALK_20261026.md)** identifies a candidate two-cutoff covariance/root theorem in the public Sussman–Alpöge account and explicit unproved upstream obligations; its [source receipt](ym/external/YM_EXT_01_SOURCE_RECEIPT_20261026.md) pins the inspected TeX blobs. This is **completed external source auditing, not native theorem closure**, and its conditional covariance/root candidate remains unverified.

## Scope and contributions

This is an **inspectable research and source-audit trail**, not an end-to-end reproduced proof, a priority assertion, or a proof announcement. The target gauge group, observables, norms, and limit topology are not yet instantiated in a source-native theorem statement. Contributions are most useful when they cite an exact pass, theorem, page, norm, assumption, and counterexample-sensitive transfer step. In particular, source-image corrections, independent checks of the two-cutoff interface, and sharply stated obstructions are welcome research inputs. Reviewers can follow [CONTRIBUTING.md](CONTRIBUTING.md). A project-wide reuse license has not yet been selected; see [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md).

**Local documentation check:** run `python3 scripts/check_public_docs.py` from a checkout (links and snapshot consistency only; [source file](scripts/check_public_docs.py)).

**Last public-status review:** 2026-10-27. **Research frontier as recorded:** 2026-10-27, YM-R122 (conditional nonlinear source M curvature certificate and deterministic two-stage bound); **YM-R123 unconsumed**. **Documentation handoff:** [DOCUMENTATION_STOP_ADVISORY.md](DOCUMENTATION_STOP_ADVISORY.md).
