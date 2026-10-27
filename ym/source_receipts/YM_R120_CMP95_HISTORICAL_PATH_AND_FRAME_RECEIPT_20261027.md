# YM-R120 — original axial contour source ancestry and distinct coarse frames

**Date:** 2026-10-27. [Native pass](../passes/YM_R120_CMP95_CMP98_CMP109_HISTORICAL_AXIAL_PATH_AND_FRAME_TRANSPORT_20261027.md). Precise evidence grades, including remaining page-image holds.

### CMP95 (1984) original-paper third-party OCR — not printed-page image

T. Bałaban, *Propagators and Renormalization Transformations for Lattice Gauge Theories. I*, *Communications in Mathematical Physics* **95** (1984), 17–40, DOI https://doi.org/10.1007/BF01215753. Original-paper OCR in chboishabba/dashi_agda, source path Docs/support/reference/balaban-source-extracts/cmp95-propagators-i.txt, pinned immutable Git blob **5cb604bd3d4a5d5cc4ff274750e0f7221273310b**. Directly read lines **80–105**, published pp.18–19: Eq.(1.6) blocks B(y) anchored at corner y; Eq.(1.7) defines the concrete contour Γ_(y,x) by following coordinate d, then d−1, ... ,1 (in d=4 the order is **4,3,2,1**); Eq.(1.8) gives an earlier unit-lattice-rescaled linear average. **Do not transfer the old linear L-scaling without reconciling coarse link group normalization and rescaling.** CMP95 original equation-page scan was not obtained; text symbols might contain OCR errors, but the coordinate path is clearly spelled out.

### CMP98 (1985) original-paper third-party OCR — not printed-page image

T. Bałaban, *Averaging Operations for Lattice Gauge Theories*, CMP **98(1)** (1985), 17–51, DOI https://doi.org/10.1007/BF01211042; pinned blob **1442f25d63ef4189608e73bff05c2a359c16c01d** from same source repository.
- Lines **29–40** Eq.(1)–(3): earlier one-sided/corner-anchored blocks.
- Lines **122–148** Eq.(14)–(15): full nonlinear selected-contour group average; text after (14) refers readers to earlier paper [2] for contour symbols.
- Lines **1662–1667**, bibliography [2]: explicitly identifies the earlier paper as CMP95, *Propagators and Renormalization Transformations for Lattice Gauge Theories. I*, 95 (1984), 17–40. Thus the descending-contour precedent in CMP95 (1.7) is a directly source-identified old contour family. Exact inclusive/exclusive integer endpoint conventions in the 1985 source block remain insufficiently confirmed from OCR; no universal 1985 path theorem beyond the ancestry is claimed.

### CMP109 (1987) original published printed page-image check

T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories. I*, CMP **109(2)** (1987), 249–301, DOI https://doi.org/10.1007/BF01215223. [Readable 54-page published-print PDF scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), third-party hosted. **Visually inspected in this pass:** PDF indices **2,3,4**, published printed pp.251,252,253. P.251 source fine-lattice centers/torus and odd L>11, p.252 Eq.(0.3) **B^k(y) cube centered at y** and G(y,x) all shortest axis permutations; p.253 (0.4) genuine full coarse-link group average, both endpoint paths and translated bridge. The center versus corner discrepancy is SOURCE EVIDENCE, not a conjectured computational convenience. This is original published mathematical image evidence, though hosted by a third party, not Springer-domain custody.

### Independent finite source-shaped calculation

On the **DECLARED** fine integer cell {0,...,12}^4 with old corner (0,0,0,0), new center (6,6,6,6), coarse e1-bond length 13, and matching source-descending transport paths τ, the gauge-covariant old coarse-link anchor change is
\(\bar M_{old}=U(\tau_y)^{-1}M_{old}U(\tau_{y'})\). At linearized identity it adds -a(τ_y)+a(τ_{y'}). It has the SAME pure-gauge endpoint signature as the new centered coarse link.

Sparse unit su(2) e3 bond A on (0,1,0,0)→(0,1,1,0): old selected descending paths, bridge and transport have zero response; centered shortest-path mean has a contribution only at x=(0,1,0,0), where 6 of 24 permutations traverse the edge in negative orientation. Thus the full frame-corrected new-old test coefficient is \(-1/(4·13^4)=-1/114244\), checked by independent 13^4 site and path enumeration and [auditable Python code](../computations/YM_R120_CORNER_CENTER_LINK_FRAME_L13_20261027.py). **This does not supplant R119's 99/28561, which used a different shared-centered-frame test.** It is not a theorem of source native UV law: CMP98/CMP109 native half-lattice offsets, inclusive block boundary and regional Ω/collar still need exact source transport.

**Original images still OPEN:** CMP95 (1.6)–(1.8); CMP98 (14)–(15); CMP99 (3.157)–(3.158) precision normalizer and full multiscale Q'_j rank. **Other open:** actual matched source old/new nonlinear \(M\) law, background/rescaling/volume, gauge fixings/Jacobian/determinants, two independently truncated UV histories, OS and positive mass gap.

Existing historical cumulative bibliography highest [92] preserved; no guessed PDF download path or invented citation.
