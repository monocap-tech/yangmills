# YM-R118 — original-source contour and gauge signature witness

**Date:** 2026-10-27. [Pass](../passes/YM_R118_CMP98_CMP99_CMP109_CONTOUR_CURVATURE_AND_GAUGE_SIGNATURE_AUDIT_20261027.md). This receipt separates original-paper text evidence from exact derived arithmetic.

## CMP98 original-paper source OCR (not new page images)

T. Bałaban, CMP 98(1), 17–51 (1985), DOI https://doi.org/10.1007/BF01211042. Third-party original-paper OCR in chboishabba/dashi_agda, path Docs/support/reference/balaban-source-extracts/cmp98-averaging-operations.txt, pinned Git blob **1442f25d63ef4189608e73bff05c2a359c16c01d**:
- lines **69–91** original (8)–(9): standard gauge transformation and contour holonomy.
- lines **94–146** original (10),(11),(14),(15): explicit coarse-endpoint gauge covariance and nonlinear averaging with selected reference path \(\Gamma_{y,x}\).
- lines **339–360** original (42)–(43): one-step averaging and compositions.
No CMP98 source-original page screenshot was newly verified; source OCR may corrupt the coefficient in (14)/(15). The selected-path topology is clear in surrounding prose.

## CMP99 original-paper source OCR (still no readable mathematical image)

T. Bałaban, CMP 99(3), 389–434 (1985), DOI https://doi.org/10.1007/BF01240355. Third-party original-paper OCR, same external repository, blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**:
- lines **192–263** original (3.13)–(3.21): source older [5] averaging, multiscale Omega_j and annular output Lambda_j, gauge-site averages Q'_j(y), R projecting onto Delta ker Q'.
- lines **1427–1463** original (3.114)–(3.115): Q_j D = D_j Q'_j from gauge transformed background/fluctuation; later claims of ker Q' invariance.
- lines **1903–1938** original (3.156)–(3.158): later A_k and Delta_k covariance forms, exact notation OCR corrupted and **image hold still OPEN**.
- lines **2183–2185** CMP99 bibliography **[5] is Bałaban, *Averaging operations for lattice gauge theories*, Harvard HUTMP B147, later CMP98**.
The CMP98 coarse-endpoint statement and CMP99 induced averaged gauge-parameter square cannot be assumed to have identical background/gauge inputs. If asserted literally identical their differentiation would require d_c(E-Q')=0; a two-block uniform-average gauge model violates that. This is a conditional source-type consistency test, NOT an accusation of source contradiction.

## CMP109 published page images previously checked, original-paper OCR re-read now

T. Bałaban, CMP 109(2), 249–301 (1987), DOI https://doi.org/10.1007/BF01215223. Readable **third-party-hosted printed page PDF** https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf, printed pp.252–255 (PDF indices 3–6), previously visually checked R107–R109. Text witness in external Git repo blob **f1aec083a3a6470c67a2c1205ca740c2583fe37a**, lines **175–273**, **287–319**:
- (0.4) Euclidean-symmetric average over shortest contour permutations, changing prior source definition.
- (0.8) axiom: group average linearization is arithmetic mean in Lie algebra.
- (0.11) symmetric gauge-fixing contour variable from averaging \(\{U(\Gamma)\}_{\Gamma\in G(y,x)}\); for a 1-by-1 displacement in two coordinate directions, exactly two paths xy/yx.
- (0.12) separate permissible averaging choice; (0.13)–(0.16) based gauge invariance/FP identity.
The R118 4-edge \(-\frac12 dA(p)\) calculation applies to that **selected-path contour coordinate versus the symmetric (0.11) contour coordinate**, NOT to the full M derivative (0.4).

## Independently executed exact calculation

[Rational Python test](../computations/YM_R118_CONTOUR_CURVATURE_MATRIX_20261027.py): on a four-edge plaquette, \(\mathrm{curl}=(1,1,-1,-1)\), \(P_{xy}=(1,1,0,0)\), \(P_{\rm sym}=(1/2,1/2,1/2,1/2)\); difference \(-\mathrm{curl}/2\), curl times gradient =0. Norm² single row =2, symmetric row =1; the test field (0,1,0,0) yields -1/2 difference. Executed with Python standard-library Fraction; **PASS**. This tests a local exact identity; no source renormalization operator, eigenvalue, TV defect, mass gap or continuum existence is inferred.

**Open:** actual CMP99 nested Q' gauge lift ranks, source old-vs-new full average linearization and gauge-action normalization, CMP99 (3.157)–(3.158) original images, uniform covariance, paired Omega/V laws, inherited E and determinant and full YM existence/gap.
