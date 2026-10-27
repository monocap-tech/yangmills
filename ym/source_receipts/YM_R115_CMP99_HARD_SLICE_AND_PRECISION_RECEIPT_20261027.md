# YM-R115 — CMP99 gauge-slice / quadratic-form provenance receipt

**Date:** 2026-10-27. [Research pass](../passes/YM_R115_CMP99_CMP109_HARD_SLICE_QUOTIENT_AND_PRECISION_SPLIT_20261027.md).

**Original-paper source text, third-party OCR, NOT original printed equation images:** T. Bałaban, *Propagators for lattice gauge theories in a background field*, CMP99(3) (1985), 389–434, DOI https://doi.org/10.1007/BF01240355. Git repository chboishabba/dashi_agda, text path Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt, pinned Git blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**.

Directly inspected source OCR lines:
- **1384–1419**, printed pp.417–418: (3.110) linearized averaging conditions and hard R(U)D*A=0 gauge; (3.112) hard delta_R(RD*A) in a Gaussian/variational integral with source Dirichlet boundaries.
- **1895–1938**, printed pp.427–428: (3.155) Gaussian integral, (3.156) A_k quadratic form on prescribed fixed-average/gauge constrained domain, (3.157)–(3.158) covariance representation; positivity lower-bound prose after (3.158) names **C*Delta_k C**, not literally A_k. OCR equation signs/exponents/normalizers unreadable; the operator relationship is OPEN, not source verified.
- **1990–2040**, printed pp.429–430: (3.169) path-related source mu(B), changing gauge coordinates, (3.170) hard RD* gauge, and text explicitly describing Faddeev–Popov replacement of a delta gauge expression by exponential gauge density around (3.171).
- **2090–2117**, printed p.432: (3.185) constrained covariance representation and Theorem 3.15 locality/decay prose, which requires precise source assumptions.

**CMP109 original printed images**, not CMP99: [54-page scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), displayed and checked pp.254,266–268, PDF indices 5,17–19: source based u(y)=1 and contour holonomy, positive quadratic holonomy gauge penalty (2.5), source A^(k) CMP99 cross-reference (2.11), covariance inverse (2.12). These support only the CMP109 side of the interface.

**Independent mathematics:** if the actual CMP99 hard gauge linear functional G has an invertible GK on the *same* based gauge parameter E, the quotient maps P_G=I-K(GK)^-1G and P_F=I-KF give exact hard-slice isomorphism R115.1. If the same physical Hessian H0 obeys a hard-slice bound on that chart, the explicit transfer R115.2 and R115.3 follows. No source operator bound or F coefficient count is supplied. The independent comparator precision mismatch C*Delta_k C versus physical H0/A_k remains an OPEN, separately typed gate.

**Access hold:** Springer/Rutgers/Euclid metadata do not provide original CMP99 printed formula images in this pass; no CMP99 equation screenshot inspected, so mathematical claims are not promoted beyond source OCR + independently proved conditional lemmas.

Historical bibliography [92] preserved. No two UV cutoff law, OS construction or positive mass-gap claim.
