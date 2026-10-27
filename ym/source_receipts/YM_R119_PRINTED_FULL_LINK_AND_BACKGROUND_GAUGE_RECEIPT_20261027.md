# YM-R119 — printed full coarse-link and fixed-background gauge-action source receipt

**Date:** 2026-10-27. [Native R119](../passes/YM_R119_FULL_COARSE_LINK_DERIVATIVE_CURVATURE_RESPONSE_AND_GAUGE_ACTION_20261027.md). Evidence grades distinguished below; do not promote scanned-third-party or OCR to publisher manuscript custody.

## Original printed CMP109 mathematical images, VERIFIED in this pass

T. Bałaban, *Renormalization group approach to lattice gauge field theories I*, *Commun. Math. Phys.* 109(2), 249–301 (1987), DOI https://doi.org/10.1007/BF01215223. Full 54-page published-paper scan (third-party hosted): https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . Viewed **PDF index 3/p.252**, source (0.3) centered odd-L cubic block B(y), family G(y,x) of shortest coordinate permutation contours; **PDF index 4/p.253**, source (0.4) FULL coarse-link average across x in B(c_-), all Gamma and Gamma' contours at both ends and parallel transported fine c path [x,x']; source (0.8) first-order arithmetic group average and (0.11) contour holonomy average; **PDF index 5/p.254**, (0.12) alternate average and (0.13)–(0.15) fine based gauge transformation. The source defines L odd >11 on earlier p.251; our choice L=13 is legal. Original publisher-domain PDF not acquired. All calculations here are in SU(2) real identity-background Lie algebra.

**Source-image-to-derivation interface:** the log in (0.4) includes U(-c), whose first variation -A(c) cancels the exterior +A(c) of U(c). Thus the actual complete coarse-link derivative is the uniformly weighted left path + fine translated bridge - right path, R119.1; this is NOT only the local gauge fixing (0.11).

## CMP98 original-paper OCR, lower evidence grade

T. Bałaban, *Averaging operations for lattice gauge theories*, *CMP* 98(1), 17–51 (1985), DOI https://doi.org/10.1007/BF01211042. OCR as original-paper transcription in chboishabba/dashi_agda, Git blob **1442f25d63ef4189608e73bff05c2a359c16c01d**:
- lines 94–146: source (11) full gauge covariance by coarse endpoint u values, (14)/(15) selected-contour full averaged group link formula; OCR obscures some mathematical factors but prose is clear.
- lines 365–377, p.24: source uses explicit descending-coordinate axial gauge paths in a local estimate, via path y→(y1,...,y_d-1,x_d)→...→x. This is evidence that a descending axis path is a legitimate source-style choice; it is NOT evidence that (15)'s unique reference contour is that order everywhere.
- lines 339–360 (42),(43): composition and one-step old averaging.
No original CMP98 printed equation images were newly viewed. The old selected bridge/contour used in R119.2 is declared as an exact matching TEST CHOICE; not source-attested universal uniqueness.

## CMP99 source background action, lower evidence grade

T. Bałaban, *Propagators for lattice gauge theories in a background field*, *CMP* 99(3), 389–434 (1985), DOI https://doi.org/10.1007/BF01240355. Third-party original-paper OCR Git blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**, lines **1427–1463**, source (3.113)–(3.115): first transforms a relative gauge/fluctuation field U' around a specified external background U, with U'=1 in the gauge-change probe; the induced site gauge parameter is averaged via R(U)u. This yields Q_jD=D_j Q'_j. This is a FIXED-BACKGROUND FLUCTUATION transformation type, not directly the CMP98 full connection U→U^u transformation of (11). Therefore the apparent R118 source-signature contradiction is rejected as a same-type source assertion. Actual chart equivalence and Q_j source covariances remain open.
- CMP99 later (3.157)–(3.158) source original printed images remain UNAVAILABLE; no reduced precision normalization transferred.

## Independent calculation, exact and narrow

[Executable Python](../computations/YM_R119_FULL_LINK_FIRST_VARIATION_L13_20261027.py) uses only Fraction, permutations, and integer combinatorics for the source-shaped full link and a **declared descending-coordinate old axial path**: coarse c 0→13e1, centered x∈[-6,6]^4, unit Lie-algebra A supported on positive e3 edge (0,1,0,0)→(0,1,1,0). Old left path response=0, new symmetric left response=99/28561, right paths/bridge zero. Independent runtime test PASS. Gauge gradients telescope to coarse endpoint difference in the complete coarse-link derivative. A simple plaquette-chain adjacent-transposition bound, averaged over both coarse endpoint path sets, gives 6(42/13)^2=10584/169 in front of ||dA||∞ under fixed monotone chosen axis orders. Neither result is an actual two-cutoff measure estimate, a source K-inverse bound or a proof of continuum Yang–Mills.

**Open source holds:** CMP98 uniquely selected actual Γ_(y,x) and parent-paper convention; CMP99 late original-page (3.157)/(3.158), complete nested regional Q'_j ranks, full CMP99↔CMP109 fixed-background derivative/coarse coordinate transport, normalized paired Ω,V inherited action/Jacobian/determinant, and physical mass gap. Historical bibliography highest [92] unchanged.
