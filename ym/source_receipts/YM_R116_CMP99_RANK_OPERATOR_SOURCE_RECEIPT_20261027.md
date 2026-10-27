# YM-R116 — CMP99 hard gauge projected Laplacian, source-completion and block-interface receipt

**Date:** 2026-10-27. [Full R116](../passes/YM_R116_CMP99_PROJECTED_LAPLACIAN_GAUGE_RANK_AND_PRECISION_20261027.md). SOURCE PROVENANCE = third-party original-paper OCR text for CMP99, **not** a visually inspected original mathematical page scan. Printed-image CMP99 (3.157)/(3.158) remains OPEN.

**Source:** T. Bałaban, *Propagators for lattice gauge theories in a background field*, *Communications in Mathematical Physics* 99(3), 389–434 (1985), DOI https://doi.org/10.1007/BF01240355. Source-extract repository chboishabba/dashi_agda, Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt, pinned blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**.

Directly inspected original-paper OCR line ranges:
- **227–263**, printed pp.393–394: Q' site-function averaging under (3.18)/(3.19); (3.20)/(3.21) **R is the orthogonal projector onto Delta N(Q')**, with E=N(Q'), not a projector simply onto E.
- **264–312**, printed pp.394–395: covariant Dirichlet site Laplacian Delta=D*D (3.23); regularized source inverse and R formula (3.25); **bond completion Delta_a=A+D R D*+Q* a Q** (3.26), its regional Dirichlet inverse (3.27). Exact source factors a and lattice weights should be taken from images when available; on simultaneous QB=RD*B=0, both nonnegative completion terms vanish regardless of coefficients.
- **1384–1419**, printed pp.417–418: source variation (3.110), hard RD* gauge, (3.112) hard delta gauge.
- **1479–1506**, pp.418–419: source uses **R Delta lambda=Delta lambda** for lambda in N(Q') and (3.119) gauge completion at hard representative B-D G' R D*B; the *G'* here is a source regularized inverse, not our abstract normalized gauge functional.
- **1895–1938**, printed pp.427–428: (3.155)–(3.158), later covariance objects A_k, Delta_k, C, and source positivity prose for C*Delta_k C. Symbolic (3.157)–(3.158) OCR corrupted; do NOT claim to have reconstructed this equality.
- **1990–2040**, printed pp.429–430: (3.169) the source's explicit gauge function mu(B), source FP delta-to-exponential manipulations and regional based gauge issues.

Mathematical deductions, **not verbatim source theorems**:
1. Since Delta is invertible on a finite Dirichlet site region, the source image-valued RD*D: E→Delta E is an isomorphism with inverse Delta^-1 restricted to Delta E. The correctly typed normalized hard gauge selector is Ghat=Delta^-1 R D*: bonds→E, with Ghat D|E=I and P_hard=I-DGhat an idempotent projection onto ker(RD*).
2. Since Delta_a=A+D R D*+Q*aQ in the source, the restricted quadratic form agrees **exactly** with A on the simultaneous hard/fixed-average slice. This does not identify source later Delta_k, the A_k referenced by CMP109, nor the physical H0 normalization.
3. In the **declared elementary disjoint-block uniform-site-average model only**, E_based={lambda(y)=0}, E_mean={sum lambda=0}, Jlambda=lambda-mean(lambda)1, J^-1mu=mu-mu(y)1. For L=13 and n=L^4=28561, exact operator norms are ||J||=1 and ||J^-1||=sqrt(n)=169 (unweighted sites); a blockwise constant shift produces an uncompensated cross-block gradient equal to the difference of block averages. The actual multiscale source Q' is not identified with this elementary model.
4. No numerical gamma0, upper bound for Delta^-1 uniform in volume, covariance or interaction/partition normalizer, two independent Ω,V UV pair or OS/mass gap follows.

The source-original printed equation images were searched earlier and remain inaccessible; this pass makes no screenshot-verification claim and keeps the lower evidence grade explicit. Project bibliography highest [92].
