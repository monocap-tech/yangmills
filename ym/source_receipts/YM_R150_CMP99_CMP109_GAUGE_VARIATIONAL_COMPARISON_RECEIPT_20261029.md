# YM-R150 — directly checked source equations for native precision transfer

**Date:** 2026-10-29. User-provided original-typeset CMP99 paper; 46 pp; SHA256 `9904f303f01e2d267a0d138d4fc08d60742086d6557fc78bef6f2d25faeaad20`; exact PDF text and equations **visually** inspected (not solely OCR). No scan is redistributed in the repo. CMP109: original scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf, printed pp.265–268, PDF indices 16–19, directly inspected.

## Original CMP99
- printed **p.420**, PDF 32, **(3.126)**: minimizer H represented as G Q* (Q G Q*)^-1; and (3.122) energy relation.
- printed **p.421**, PDF 33, **(3.127)–(3.129)**: *corrected* minimizer H₁ under nonlinear second-order terms; `H₁=G₁Q*(QG₁Q*)^-1`, and the inverse covariance source form includes the original gauge and averaging penalties; compare source Delta₁ carefully.
- printed **p.427**, PDF 39, **(3.155)**: source Gaussian integral with hard coarse bond constraint, regional Dirichlet support, H₁ and nonlinear second-order correction.
- printed **p.428**, PDF 40, **(3.156)–(3.158)**: historical quadratic form Δ_k; special-bond elimination C_old; lower-bound claim for C_old*Δ_k C_old under source assumptions. The claim does not provide the numerical lower bound or modern CMP109 K entries.
- printed **p.431**, PDF 43, **(3.178)**: transformed projected Landau gauge of the **new domain sequence**, with a tilde on R and D.
- printed **p.432**, PDF 44, **(3.183)–(3.186)**: transformed source covariance. **Critical precise rendering of (3.185): `(I+D̃μ) Q G̃₂ Q* (I+μ*D̃*)`**. The Qs in this expression are **un-tilded**, while the hard covariance conditioning in (3.186) uses **Q̃**. These have different source types. This is a direct image-verified correction to the older `YM_R150_CMP99_ORIGINAL_IMAGE_VERIFIED_20261029.md` receipt which dropped the left Q.
- printed **p.394**, PDF 6, **(3.21)**: source projection R has range Δ_U N(Q'), not N(Q'). This earlier correction remains effective.

## Original CMP109
- printed **p.265**, public scan PDF index 16, **(2.1)–(2.3)**: small-field next-step RG, axial gauge saddle and Landau conversion; not a direct source equality of historical hard and current soft precision.
- printed **p.266**, index 17, **(2.5)**: gauge function G has a nonnegative sum-of-squares quadratic part G^(2), plus cubic remainder, and (2.9) defines the monitored cutoff with special bonds excluded.
- printed **p.267**, index 18, **(2.10)–(2.11)**: current quadratic order-zero terms, nonlinear constraint linearization via `h`, H₁ response and Δ₁ action, with explicit reference back to the prior CMP99 (3.156) *after changing gauge-fixing prescription*. This is a historical mathematical dependency, **not** an identity of full reduced K without exact gauge/source chart matching.
- printed **p.268**, index 19, **(2.12)–(2.14)**: current source C_new from current background, covariance (C_new*A^(k)C_new)^-1, nonlinear Jacobian/σ, χ and normalization. Two independent UV histories are NOT delivered by these equations.

## Typed decision
CMP99 q_old and CMP109 q_new admit an **explicit formal three-term difference** only after identifying domains, metrics, all H₁, Q, reconstructed special bonds, nonlinear second jets and gauge. The only manifestly nonnegative standalone difference contribution here is G^(2), which does **not** suffice to conclude `K_new-K_old>=0` until the variational and second-jet residuals vanish (or receive certified bounds). The abstract annihilation `Q̃G̃₂=0` from (3.186) clarifies why (3.185) must use Q rather than Q̃.
