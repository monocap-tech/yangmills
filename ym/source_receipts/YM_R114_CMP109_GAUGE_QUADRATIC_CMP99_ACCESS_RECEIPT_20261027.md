# YM-R114 — CMP109 positive exponential-gauge Hessian source image and CMP99 access

**Date:** 2026-10-27. [Pass](../passes/YM_R114_CMP109_BASED_GAUGE_QUADRATIC_EXTENSION_20261027.md). Exact evidence boundary: published CMP109 printed images through a third-party scan; CMP99 original-paper OCR plus publisher metadata, no independently viewed original CMP99 equation image.

## Printed source checks, CMP109
T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, *CMP* 109 (1987), 249–301; DOI https://doi.org/10.1007/BF01215223. 54-page scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf ; zero-based PDF page indices:
- **5 / printed p254, (0.13)–(0.15):** based gauge transformations u(y)=1 on coarse vertices; source U(y,x) path holonomy and an exact Haar-normalized exponential+indicator gauge identity. Differentiating endpoint action gives FK=±I in based site variables at the identity background; gauge covariance of coarse average gives DK=0. The differentiation and splitting in R114 are OUR DERIVATIONS, not verbatim source theorems.
- **16 / p265, (2.1)–(2.3):** small-field restricted action and constrained stationary/identity reference, not a two-cutoff probability law.
- **17 / p266, (2.5):** the actual source gauge-fixing term G(B') is an explicitly **nonnegative sum of one-half squared linear holonomy coordinates**, plus an analytic remainder G3 starting at degree three. This is the decisive source sign and order observation. The source cutoff (2.9) is separate from the FP gauge identity.
- **18 / p267, (2.10)–(2.11):** quadratic source A^(k), original printed direct cross-reference to CMP99 [13] (3.156) with delta gauge fixing replaced by exponential; linearized source h/D and nonlinear higher corrections.
- **19 / p268, (2.12):** constrained Gaussian covariance (C* A^(k) C)^-1; nonlinear Jacobian, determinant and inherited effective E are distinct.

## CMP99 original-page access attempt (NOT verified)

T. Bałaban, *Propagators for Lattice Gauge Theories in a Background Field*, CMP 99(3) (1985), 389–434; DOI https://doi.org/10.1007/BF01240355.

- Publisher URL https://link.springer.com/content/pdf/10.1007/BF01240355.pdf redirected to a subscription page, not a PDF readable through web inspection.
- Project Euclid full-article path for the target paper was not accessible.
- University of Michigan DeepBlue guessed PDF handle paths could not be opened; do not treat guesses as URLs of verified sources.
- Rutgers bibliographic metadata and Springer abstract confirm paper identity but **do not supply equation images**.
- Existing original-paper third-party OCR text in chboishabba/dashi_agda, path Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt, pinned Git blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743** remains the source for (3.155)–(3.158) at OCR lines 1895–1938, original p427–428, and (3.185) plus Theorem 3.15 at OCR lines 2090–2117, p432. Formula signs/gauge domain/strongest theorem quantifiers remain image-open. Exact equality with CMP109 Q not verified.

## Mathematical derivation and its hypotheses

R114.1 source-shaped based gauge identities DK=0 and FK=±I at identity; R114.2 algebraic splitting W=(W cap ker F) plus im K; R114.3 explicit conditional coercivity of H0+beta F*F given hard-slice H0>=gamma and gauge Hessian Ward identity; R114.4 d=4 nearest-neighbor incidence ||K||<=4 and conditional reduced bound min(gamma/2,beta/32). These are mathematical deductions, not CMP99 or CMP109 verbatim universal estimates.

**Hold:** identification of CMP99 positive form on exactly CMP109 W cap ker F with unchanged lattice normalization, boundaries, constraints, and correct source A^(k); real-positive Gaussian chart, source uniform constants, UV pair Omega/V, inherited E and determinant, source beta/polarization difference and physical continuum gap all OPEN.

Historical reference [13] of CMP109 is not a new cumulative project bibliography entry; highest project bibliography remains [92].
