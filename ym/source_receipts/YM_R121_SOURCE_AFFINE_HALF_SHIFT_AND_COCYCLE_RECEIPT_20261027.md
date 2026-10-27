# YM-R121 source receipt — half-shifted CMP109 centers versus old corners

**Date:** 2026-10-27. [R121 investigation](../passes/YM_R121_AFFINE_HALF_SHIFT_AND_MULTISCALE_TRANSPORT_COCYCLE_20261027.md). This receipt distinguishes visual original print (CMP109) from lower-confidence original-paper OCR (CMP95/CMP98), exact derivation, and code.

## Original printed CMP109 source pages, viewed

T. Bałaban, *Renormalization group approach to lattice gauge field theories I*, *Communications in Mathematical Physics* 109 (1987), 249–301, DOI https://doi.org/10.1007/BF01215223. Full original printed 54-page mathematical scan on third-party SciSpace https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf .

- PDF index **2**, printed **p.251**, original **(0.1)** and preceding prose: odd L>11, initial torus lattice \(h\mathbb Z^4+\frac h2\mathbf1\), coarser \(Lh\mathbb Z^4+\frac{Lh}{2}\mathbf1\), periodic torus/cubic center lattice. This is the decisive original-picture half-offset source.
- PDF index **3**, printed **p.252**, **(0.3)**: block \(B(y)=\Delta(y)\cap T_{\rm fine}\) with continuous cube centered at y, of size Lh, plus shortest monotone coordinate-order contours and translated coarse-link bridge [x,x'].
- PDF index **4**, printed **p.253**, **(0.4)**: nonlinear full coarse-link M(U) (not a product along one fine path), left and right independent shortest paths and bridge, with logarithmic averaging. This is why two-stage geometric fine-holonomy comparison is NOT automatically an RG-map comparison.

These are actual images of published pages in a third-party scan, not publisher-hosted archival images.

## Earlier CMP95 and CMP98 source text, NOT mathematical page images

T. Bałaban, CMP95 (1984) *Propagators and renormalization transformations for lattice gauge theories I*, DOI https://doi.org/10.1007/BF01215753, original-paper transcription Git repository chboishabba/dashi_agda, pinned blob **5cb604bd3d4a5d5cc4ff274750e0f7221273310b**, direct OCR lines **40–49**, **80–105**: fine hZ^d torus, coarse LhZ^d, corner-anchored old L block (1.6) and descending coordinate-axis path (1.7).

T. Bałaban, CMP98 (1985), *Averaging operations for lattice gauge theories*, DOI https://doi.org/10.1007/BF01211042, original-paper OCR Git blob **1442f25d63ef4189608e73bff05c2a359c16c01d**, direct lines **29–40**, **122–148**: old corner block Eq.(2) and selected-path nonlinear averaging (14)–(15), citing CMP95 [2]. OCR corrupts strict/weak inequality glyphs at the old block boundary, so **the old full L^4 half-open partition convention is declared as an explicit assumption** in R121. Original printed CMP95/CMP98 equation images NOT independently viewed; do not upgrade evidence grade.

## Independent derivations and exact code

For odd L=2r+1 and equal-period finite periodic graph, affine translation old hZ^4→new h(Z^4+1/2 1) by h/2 per coordinate maps L^4 old corner-block sites to the centered new source cube sites, with new coarse basepoint r fine steps farther. Across scale j the affine offset difference is t_j=r h_j; telescopes exactly across all scales. This is a graph/site equality after DECLARED translation, not identity of physical fields without pushforward, and not validity of Ω/Dirichlet path restrictions.

[Exact Python test](../computations/YM_R121_AFFINE_HALF_SHIFT_AND_PATH_COCYCLE_20261027.py) independently executed with PASS: one-cell 28,561 site bijection; affine multi-level shifts; two successive descending lifted-geometry paths t0=(6,6,6,6), t1=(78,78,78,78) versus direct (84,84,84,84); 336 fine steps either way; each of six coordinate planes has signed area 468, giving exactly 2808 elementary plaquette swaps. With SU2 unitary links, each elementary plaquette swap changes product norm by no more than \(\max_p\|U(\partial p)-I\|\), hence \(\min(2,2808\eta)\) is a genuine FINE-PATH bound. Stage-2 coarse M(U) is not the fine lifted path holonomy; the inequality is not a bound on two RG maps.

**Unresolved source passports:** CMP95/CMP98 original printed inequalities, exact Ω/Λ and Dirichlet collars at every scale, multiscale group gauge action and CMP99 Q'_nested rank, coarse M(U) versus fine-lift defect, CMP99 (3.157)–(3.158) original-image covariance normalization, source-uniform mass/covariance and two independent UV probability laws. Project bibliography historical highest [92] retained.
