# YM-AUX-05 original-paper source receipt: projected Landau ≠ ordinary divergence

**Date:** 2026-10-28. **Evidence:** original CMP99 article in third-party OCR; ORIGINAL MATHEMATICAL PAGE IMAGES NOT RECOVERED. This is not independent primary-page image verification.

**Bibliographic fact:** T. Balaban, *Propagators for lattice gauge theories in a background field*, *Communications in Mathematical Physics* 99(3), 389–434 (1985), DOI https://doi.org/10.1007/BF01240355 . Publisher and Rutgers metadata corroborate title, year, pages.

**Immutable OCR:** repository `chboishabba/dashi_agda`, path `Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt`, Git blob `ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743`. Printed page references below are from text page headers; OCR index is not printed pagination. Consult source Git blob rather than treating transcription as an equation image.

**Read during this pass:**
- printed pp.392–394 around (3.13)–(3.21): historical bond averaging `Q_j(U)` is the *linearization of group-valued block averaging* (3.14)–(3.15); separately **site-gauge** averaging `Q'_j(U)` is defined (3.18)–(3.19). The latter is a parallel-transported block-site average; at identity, a declared one-step specialization is centered arithmetic average. The source describes `R` as the orthogonal projection onto `N(Q')` in the site-gauge Hilbert space at (3.20)–(3.22).
- printed pp.394–395 around (3.24)–(3.27): source `R` is used to define projected gauge regularization and a covariance with Dirichlet domain. This does not mean `R=I`.
- printed pp.427–428 around (3.155)–(3.158): **bond** Gaussian supported in regional domain A with independent variable elimination on special bonds via `C`, and `Q_1 B=0`. The precise operator indices, sign and quadratic form symbols are damaged in OCR.
- printed pp.429–432 around (3.159)–(3.183): multiple gauge changes and the source statement that the *transformed A integral* uses the **Landau gauge condition `R D^* A=0`** near (3.178). Thus A, B and original/new gauge variables must not be silently identified.

**New internal derivation:** `R D^*a=0 iff D^*a∈ran Q'^*` for *finite-dimensional orthogonal projection* onto ker Q'. The normal flux increment equals `−⟨Q'1_s,λ⟩` when `D^*a=Q'^*λ`, using ordinary periodic unit-spacing adjoints. This is not printed verbatim in CMP99.

**Independent model:** exactly normalized identity single-scale Qsite with L=13,N=169; projected gauge and strict support do not imply conserved normal flux. It does NOT instantiate the entire historical multiscale Q', the source B constraint `Q_1B=0`, or CMP109 exponential-gauge precision K.

**Source TODO:** legitimately retrieve original CMP99 printed mathematical images pp.393–395 AND pp.427–432, especially equations (3.21),(3.26),(3.155)–(3.159),(3.178). Audit actual Hilbert inner products, region/collar and A←→B transformation in the paper. Separately connect original source bond Q1 and its constrained C to CMP109 nonlinear averaging and gauge. The source-data stop at native YM-R150 is not lifted.
