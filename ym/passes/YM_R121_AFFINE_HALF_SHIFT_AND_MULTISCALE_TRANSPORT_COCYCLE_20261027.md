# YM-R121 — exact half-shift cell dictionary and multiscale holonomy cocycle

**Date:** 2026-10-27. **Verified predecessor:** [YM-R120](../checkpoints/YM_HEAD_R120_20261027.json), main f78844c0c55a81b25b4ba607f51d144a0890fa86. **Disposition:** COMPLETE as source-based one-step affine/combinatorial alignment on equal-period tori and an exact, finite two-stage lifted-path holonomy/curl bound. Not complete as actual nonlinear Bałaban RG-history transport, source-uniform covariance or mass gap. **Next:** YM-R122 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Primary source and evidence grade

SOURCE ORIGINAL PRINTED CMP109 IMAGES visually rechecked: T. Bałaban, *Renormalization group approach to lattice gauge field theories I*, CMP109 (1987), 249–301, DOI https://doi.org/10.1007/BF01215223. Third-party hosted [54-page printed-paper scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), zero-based PDF indexes **2** (printed p.251: source (0.1) fine lattice \(T_h\subset h(\mathbb Z^4+\frac12\mathbf1)\), coarser \(T_{Lh}\subset Lh(\mathbb Z^4+\frac12\mathbf1)\), L odd >11 and natural cubical subdivision), **3** (p.252, source (0.3) continuous cube centered at coarse y and size Lh, shortest contour permutations), **4** (p.253 source (0.4) full coarse link with two independent endpoint contour means and bridge). This is genuine equation-image inspection, not mere mangled text extraction.

PREDECESSOR original-paper third-party OCR, immutable Git blobs in chboishabba/dashi_agda: CMP95 (1984) SHA **5cb604bd3d4a5d5cc4ff274750e0f7221273310b**, lines 40–49, 80–105, original printed pp.17–19: fine sites \(h\mathbb Z^4\), coarse sites \(Lh\mathbb Z^4\), old corner block Eq.(1.6) and descending axial path Eq.(1.7). CMP98 (1985) SHA **1442f25d63ef4189608e73bff05c2a359c16c01d**, lines 29–40 and 122–148: old corner cube Eq.(2) and selected-path average (14)–(15) with reference [2]=CMP95. Their precise inequality symbols and boundary-half-open conventions are OCR-degraded; ORIGINAL CMP95/CMP98 mathematical page images NOT inspected. Source bibliography identities are publisher-verifiable. [R121 evidence receipt](../source_receipts/YM_R121_SOURCE_AFFINE_HALF_SHIFT_AND_COCYCLE_RECEIPT_20261027.md).

**Important source-type caution:** An affine TRANSLATION of fine-site labels is a graph isomorphism, not a claim that old and new fields are literally the same physical field without pushforward. An RG coarse action and coarse connection are not the same as a geometric fine-lattice holonomy.

## 1. Exact one-step affine cell identification

Fix real fine spacing h, odd L=2r+1 (native legal L=13, r=6), and a common periodic torus of a matching physical period in each axis (e.g., periods integer multiples of Lh). For an old fine grid \(V_{\rm old}=h\mathbb Z^4\), new grid \(V_{\rm new}=h(\mathbb Z^4+\frac12\mathbf1)\), define the affine graph map
\[
 \boxed{\iota_h(x)=x+\tfrac h2\mathbf1.}\tag{R121.1}
\]
Translate old oriented bonds/plaquettes with the same displacement; incidence, orientations, curl, gauge gradients and plaquette holonomies are preserved under pushforward.

For an old corner block with full \(L^4\) half-open integer-cell convention
\[
 B_{\rm old}(Lm)=\{h(Lm+i):i_\mu=0,\ldots,L-1\}
\]
the translated fine sites are \(\{h(Lm+i+\frac12\mathbf1)\}\). The CMP109 printed centered coarse site is
\(s_m=hL(m+\frac12\mathbf1)\), so its printed (0.3) centered block has sites
\[
 B_{\rm new}(s_m)=\{s_m+h(i-r\mathbf1):i_\mu=0,\ldots,L-1\}.
\]
Since \(L/2=r+1/2\),
\[
 \boxed{\iota_h B_{\rm old}(Lm)=B_{\rm new}(s_m),
 \quad s_m-\iota_h(hLm)=rh\mathbf1.}\tag{R121.2}
\]
The equality is an EXACT finite-graph lattice-combinatorial theorem for the stated old full L^4 partition / equal-period torus; the translation works modulo the common torus period. It is not a separate approximate “six-step overlap.” At L13 the center displacement has **six fine bonds in each of four coordinates**. The source CMP95/CMP98 OCR does not resolve every endpoint inclusion by itself; the conventional L^4 partition is an explicitly named OLD-SOURCE BOUNDARY HYPOTHESIS. Full regional Ω/Dirichlet/collar boundary transport is not established.

This now grounds R120's declared integer cell \(\{0,\ldots,12\}^4\): it is the correct one-step coordinate chart after translating the old fine sites by h/2, under the stated block convention. R120's -1/114244 remains a sparse test dependent additionally on the chosen transport path τ and matching bridge, not an unconditional full historical probability-law coefficient.

## 2. Affine translations compose exactly in the REGULAR periodic hierarchy

Let \(h_j=L^jh\), old scale-j lattice \(h_j\mathbb Z^4\), new scale-j lattice \(h_j(\mathbb Z^4+\frac12\mathbf1)\). The levelwise translations are \(s_j=\frac{h_j}{2}\mathbf1\), so the difference of affine placements at adjacent levels is
\[
 \boxed{t_j=s_{j+1}-s_j=\frac{L-1}{2}h_j\mathbf1=rh_j\mathbf1.}\tag{R121.3}
\]
Each \(t_j\) is a vector of INTEGER FINE BONDS of scale h_j (because L odd). More generally,
\[
 \boxed{\sum_{j=a}^{b-1}t_j=\frac{h_b-h_a}{2}\mathbf1.}\tag{R121.4}
\]
Thus the **unrestricted periodic lattice sites** admit a consistent affine hierarchical alignment; no cumulative site-translation mismatch exists. Source prescribed Ω_j, Λ_j, and Dirichlet/collar restrictions can break the admissible path/domain match, so there is no assertion that the *regional gauge/averaging hierarchy* is already source-equivalent.

## 3. New explicit two-stage transport PATH cocycle

A lattice connection transports along PATHS, not solely endpoint displacements. For a concrete geometric comparison, L13 at finest scale h=1 yields t0=(6,6,6,6), t1=(78,78,78,78), and total=(84,84,84,84), in finest-bond units. **This explicitly lifts** the second stage's coarse-scale axis displacements to fine steps on the same graph; it is NOT the actual first-stage RG coarse-field variable.

Choose descending coordinate order 4,3,2,1. Let P_staged be the descending path of t0 followed by the descending path of t1; let P_direct be a single descending path of total displacement t0+t1. To reorder P_staged into P_direct, each earlier low-axis run of r fine steps must pass each later higher-axis run of Lr fine steps, for each unordered axis pair. Exactly
\[
 \boxed{N_{\square}=\binom42 r(Lr)=6Lr^2
 =2808\quad(L=13,r=6).}\tag{R121.5}
\]
elementary adjacent-axis plaquette swaps suffice. The count is also NECESSARY for this restricted swap reordering because it is the inversion number of the two ordered runs.

For any SU(2) UNITARY fine-link connection on an eligible periodic patch containing those paths and their plaquettes, with operator norm and \(\eta=\sup_{p\ \text{in patch}}\|U(\partial p)-I\|_{\rm op}\), a swap changes a path product by two factors related by one elementary plaquette. Since outside products are unitary, the operator norm difference is at most η. Applying triangle inequality along the 2808 swaps proves the NONPERTURBATIVE bound
\[
 \boxed{\|U(P_{\rm staged})-U(P_{\rm direct})\|_{\rm op}
 \le\min\{2,2808\eta\}.}\tag{R121.6}
\]
The bound is a **fine-graph holonomy comparison**; the trivial 2 cap follows because SU2 matrices are unitary. When η=0 on the patch, these two holonomies agree. In general they NEED NOT agree because the difference encloses curvature.

The source-shaped **signed projection** to each (i,j) coordinate plane has area \(r(Lr)=468\). This can be witnessed without matrix exponentials by the discrete Abelian test potential \(A_j(x)=x_iT\) for an su(2) one-parameter generator T, with other components zero: the staged path integral exceeds direct by \(468T\), hence SU2 holonomies generally differ at small nonzero field. Six coordinate planes yield the combinatorial total 2808. This is an explicit nonvanishing curvature/path holonomy cocycle, not a source coupling constant renormalization.

[Independent exact certificate](../computations/YM_R121_AFFINE_HALF_SHIFT_AND_PATH_COCYCLE_20261027.py) verifies all 13^4 one-step site images, shifts, staged/direct endpoints/length 336 and six signed areas 468, total 2808. Executed using Python standard library: PASS.

**The actual RG-stage caution:** After one Bałaban renormalization step, its coarse link is **M(U,c)** (with integration, gauge fixing, normalizers and interactions for laws), not the direct product of the 13 underlying fine-link holonomies. Thus R121.6 is not automatically a bound on the composition of two RG averaging steps. To use it on the native full-history carrier, a quantified source relation between each coarse M(U) and the fine geometric lift (with its transverse curvature, local nonlinear remainder, gauge and determinant) must first be proved. The large factor 2808 is not a small-contraction estimate.

## 4. Exact boundary of R121 and new obligations

| Gate | R121 |
|---|---|
| CMP109 half-shifted lattice and centered cube | ORIGINAL PRINTED (0.1),(0.3) IMAGE VERIFIED |
| CMP95/CMP98 corner site and axial source | ORIGINAL-PAPER OCR LOCATED, OLD EQ IMAGE OPEN |
| One-step periodic fine-site/bond/plaquette graph | EXACT affine isomorphism under equal period and conventional half-open L^4 block |
| Corner to center offset | EXACT r fine bonds per axis; R120 τ now geometric source passport |
| Unrestricted hierarchy affine offsets | EXACT telescoping R121.3–R121.4 |
| Two-stage lifted shortest path cocycle | EXACT 2808 plaquette swaps and SU2 norm bound |
| R120 sparse -1/114244 | RETAINED as chosen τ/bridge COMMON GRID result, not generic RG history |
| Actual multiscale regional Ω/Λ collars / nested Q'_j | OPEN |
| Native coarse M(U) versus fine lifted τ composition | OPEN |
| CMP99 original (3.157)–(3.158) A_k/Δ_k covariance | OPEN |
| Source uniform coercivity/covariance and two-UV normalized laws | OPEN |
| Continuum YM, OS, positive gap | UNPROVED |

## 5. YM-R122 unconsumed

**Do not grind another abstract gauge positivity pass.** YM-R122 must identify the source-permitted actual τ and bridge paths on CMP109 Ω/Λ regional/boundary graphs and the matched corner-partition incidence at each nested scale, then derive the **nonlinear source coarse-link defect** \(M(U,c)\) versus its fine-lift holonomy, including dependence on source plaquette curvature and gauge choice. Separately retrieve original CMP99 (3.157)–(3.158) covariance normalization and full Q'_nested rank and return to the actual two-cutoff normalized RG law. One-step exact geometry and a 2808 fine-path norm bound are mathematical prerequisites, NOT a continuum existence or spectral mass-gap theorem.

Historical cumulative project bibliography highest [92]. Source-image and OCR receipts append-only, no silent reclassification.
