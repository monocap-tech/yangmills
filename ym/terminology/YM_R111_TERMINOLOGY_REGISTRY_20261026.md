# YM-R111 — source monitored-bond projection and covariance types

2026-10-26. [R111](../passes/YM_R111_CMP109_MONITORED_BOND_PROJECTION_GAUSSIAN_CUTOFF_20261026.md). Historical registries preserved; this file corrects applicability of R110's general nonlinear cutoff delta obligation for CMP109 (2.9).

- **LegalLocalTestChoice** — G=SU(2), source block scale L=13 (odd >11), and CMP109 Euclidean averaging (0.4) chosen explicitly to pin a test *type*, NOT a constructed source UV input pair.
- **DistinguishedBondSet** — \(\mathcal B_0=\{b_0(c)\}\), one bond per source coarse constraint, eliminated after the nonlinear constraint linearization.
- **MonitoredBondProjection** — P restricts a full fine-bond Lie field to bonds outside \(\mathcal B_0\), exactly the bonds in χ_k (2.9).
- **SourceLinearizationSupport** — source h is supported only on \(\mathcal B_0\), hence Ph=0. For exact nonlinear substitution B_old=B_new-h D(B_new), P B_old=P B_new without needing a norm bound on D.
- **R110CutoffDeltaCorrection** — the hypothetical nonlinear chi-pullback displacement δ of R110 is exactly ZERO on the actual (2.9) monitor seminorm. D still affects eliminated bonds, full Jacobian, interaction and chart validity. Do not confuse these obligations.
- **LinearGaussianCutoffCarrier** — after rescaling and independent-variable elimination, χ_k(B)=product over non-b0 bonds of 1[|g_k(C B)(b)|<theta_k], with C the source *linear embedding* and B the final constrained Gaussian coordinates.
- **MonitoredCovariance** — \(S=P C(C^*A^{(k)}C)^{-1}C^*P^*\), the source Gaussian covariance of the actual χ-monitored Lie coordinates; not necessarily diagonal.
- **DirectGaussianTailGate** — cutoff failure q ≤ min(1,2mn exp(-theta_k²/(2m*g_k²*v))), with m=dim Lie algebra, n=monitored bonds, v=max real coordinate variance from S. No independence assumption; source uniform variance/volume bounds OPEN.
- **ThresholdBranchSplit** — theta=epsilon1 yields a 1/g_k² exponent, theta=g_k epsilon1/gamma_k cancels g_k in the exponent. Neither implies native summability without source covariance/chart/volume controls.
- **MinimalMarginalPassport** — compare true *common* monitored Gaussian marginals on physically identified bonds via S0,S1, rather than requiring identical full Gaussian coordinate systems; those coordinates are gauge-fixed, not automatically gauge invariant.
- **NativeR112** — source construct/evaluate C, A, S and admissible chart for declared (0.4), odd L=13 test; then investigate actual Ω,V pairing and inherited background determinant/E, no invented quantitative rates.
