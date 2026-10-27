# YM-R116 — CMP99 projected-Laplacian hard gauge rank and exact gauge-penalty cancellation

**Date:** 2026-10-27. **Prior canonical:** [YM-R115](../checkpoints/YM_HEAD_R115_20261027.json), main 05a9836a23237db6cc488540c8b18d8ada5c12ff. **Completed as:** SOURCE-TYPED CMP99 RANK/DOMAIN CORRECTION, EXACT SOURCE QUADRATIC RESTRICTION IDENTITY, FINITE-BLOCK GAUGE-PARAMETER COMPARISON, AND REMAINING PRECISION LOCK. **Next:** YM-R117 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM. No two-cutoff law, continuum Yang–Mills or gap theorem.

## 1. Custody and target

YM-R115 proposed a hard-gauge operator G=R D* and required GK to be invertible on the CMP109 based Lie-site parameter space. The **source actually gives an image-valued operator**, so that criterion must be retyped *before* trying to prove it.

**Original-paper CMP99 text witness (NOT printed-image verified):** T. Bałaban, *Propagators for lattice gauge theories in a background field*, CMP 99(3) (1985), 389–434, DOI https://doi.org/10.1007/BF01240355. Source: original-paper third-party OCR text in chboishabba/dashi_agda, blob ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743, path Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt. Newly inspected line ranges **227–312**, **1384–1419**, **1479–1506**, **1895–1938**, **1990–2040**. Corresponding printed pages pp.393–395,417–419,427–430. The exact OCR formulas (3.157)–(3.158) remain illegible, and no original printed CMP99 equation screenshot was obtained. See [source receipt](../source_receipts/YM_R116_CMP99_RANK_OPERATOR_SOURCE_RECEIPT_20261027.md).

**Source facts:**
- (3.18)–(3.19) define the *site-gauge averaging operator* Q' and N(Q')={lambda:Q'lambda=0} under source nested geometry.
- (3.20)–(3.23) define R as the **orthogonal projection onto the subspace Delta N(Q')**, where Delta=D*D is the positive Dirichlet covariant site Laplacian (on the source regional Dirichlet domain). Thus R is a projector on the **site Hilbert space**, but its *range* is **Delta E**, E=N(Q'), not E itself.
- (3.25) gives a source representation of R via regularized Laplacian inverse, subject to regularity/positivity. This formula is OCR damaged; our derivation uses only the clearly attested range and projector property.
- (3.26) defines the source positive completed quadratic **Delta_a = A + D R D* + Q* a Q** on the full bond Hilbert space, with specified source normalization; the notation here is site versus bond covariant D. (3.27) defines its regional Dirichlet inverse.
- (3.110),(3.112) enforce the **hard RD* condition** plus block-average constraints and regional Dirichlet data; (3.118)–(3.119) build a gauge-invariant completion with the hard-gauge representative \(B-DG'RD^*B\) using a DIFFERENT source inverse notation G'; do not confuse that inverse with the elementary Dirichlet Delta inverse.
- (3.155)–(3.158) define later Gaussian quadratic A_k and covariances; the prose after (3.158) specifically identifies positivity of **C*Delta_k C**. The literal Delta_k-to-A_k identity remains unverified at original equation image level, so neither receives an unconditional CMP109 coercivity transfer.

## 2. Exact source hard-gauge rank on the PROPER gauge carrier

Let \(\mathcal E=\ker Q'\) within the source site Dirichlet Hilbert space. Let \(\Delta=D^*D\) be strictly positive on \(\mathcal E\) (for a fixed finite source Dirichlet region; when bounding uniformly the minimal eigenvalue remains an independent quantitative matter). Let \(R\) denote the **orthogonal projection onto \(\Delta\mathcal E\)**, exactly as in CMP99 (3.21). Then for lambda in E,
\[
 \boxed{R D^*D\lambda=R\Delta\lambda=\Delta\lambda.}\tag{R116.1}
\]
The image-valued hard FP operator \(R D^*D:\mathcal E\to\Delta\mathcal E\) is an **isomorphism**, with inverse \(\Delta^{-1}\) restricted to that image. This is a true **source-specific algebraic rank closure on CMP99's gauge parameter E**. It is not a claim of a UV-uniform bound for \(\|\Delta^{-1}\|\).

Define the normalized hard-gauge coordinate operator, as a typed map from full bond fields into E:
\[
 \widehat G:=\left.\Delta^{-1}\right|_{\Delta\mathcal E} R D^*,
 \quad\widehat G:\mathcal H_{\mathrm{bonds}}\to\mathcal E.
\]
Then
\[
 \boxed{\widehat G D|_{\mathcal E}=I_{\mathcal E},\qquad
 P_{\rm hard}=I-D\widehat G,\quad P_{\rm hard}^2=P_{\rm hard}.}\tag{R116.2}
\]
Proof: RΔlambda=Δlambda, and the inverse maps the image to E. Moreover \(\ker\widehat G=\ker(RD^*)\), because restricted Delta^{-1} is one-to-one. Therefore P_hard is the algebraic gauge-orbit section onto the **source hard RD* slice**, annihilating gauge gradients of lambda in E. These identities depend only on the source projector (3.21), Dirichlet positivity and the correct site-gauge E, not an unproved source spectral gamma0.

**Explicit correction to R115:** \(G=RD^*\) naturally has codomain \(\Delta\mathcal E\), so writing \(GK:\mathcal E\to\mathcal E\) as an endomorphism was a type shortcut. R115's abstract lemma remains valid when G is replaced by the normalized \(\widehat G\) *and* K is the gradient on precisely E. It cannot be directly applied to CMP109's distinct based site gauge functions just because their dimensions sometimes agree.

## 3. Original source quadratic restricts EXACTLY on simultaneous hard/fixed-average slice

CMP99 (3.26) is:
\[
 \Delta_a=A+D R D^*+Q^*aQ,\quad a\succeq0.\tag{R116.3}
\]
Let \(W_{G,Q}=\{B:QB=0,\ RD^*B=0\}\), with the source Dirichlet bonds and real inner product. Then for all \(B\in W_{G,Q}\),
\[
 \boxed{\langle B,\Delta_a B\rangle=\langle B,A B\rangle.}\tag{R116.4}
\]
**Proof:** \(\langle B,DRD^*B\rangle=\langle D^*B,RD^*B\rangle=\|RD^*B\|^2=0\) (R is orthogonal projector); and \(\langle B,Q^*aQB\rangle=\langle QB,aQB\rangle=0\). Polarization also gives equality of restricted bilinear forms, not only diagonal values.

This refutes a *part* of R115's loose “positive completion cannot imply physical H0” concern: for the actual source **Delta_a** completion, there is a direct exact equality on the simultaneous hard/fixed-average slice. The R115 abstract counterexample still cautions against applying an *unrelated* comparator to H0. The remaining source gap is more precise: the gamma0 claim after CMP99 (3.158) is about a **later Delta_k** and reduced C, while CMP109 cites a quadratic \(A^{(k)}\) via CMP99 (3.156). R116.4 alone does NOT prove Delta_k=Delta_a, nor A_k=the restricted physical Hessian, nor that CMP99/CMP109 use identical C and boundary conditions.

This **operator-level improvement is independent** of gauge-quotient section normalization: source Delta_a agrees on the *source hard slice* with A, whether or not that slice matches CMP109 based holonomy F.

## 4. Exact one-block mean-zero/based parameter comparison and its interface failure

**DERIVED FINITE BLOCK, NOT A FULL CMP99 SOURCE GEOMETRY CLAIM.** At SU(2) identity take one disjoint interior block with n=L^4 fine vertices (declared L=13, n=28,561). If the chosen source Q' restriction on this ONE isolated block is the uniform site average (source (3.19) at identity in this elementary block model), define:
\[
 E_{\rm based}=\{\lambda:\lambda(y)=0\},\qquad
 E_{\rm mean}=\{\mu:\textstyle\sum_{x\in B}\mu(x)=0\}.
\]
They are NOT identical subspaces. The change-of-section
\[
 J\lambda=\lambda-\bar\lambda\,{\bf1},\qquad
 J^{-1}\mu=\mu-\mu(y){\bf1}\tag{R116.5}
\]
is bijective. For n>=3, with the ordinary unweighted site ℓ² norms,
\[
 \boxed{\|J\|=1,\quad \|J^{-1}\|=\sqrt n=L^2=169.}\tag{R116.6}
\]
Proof: J is mean-zero orthogonal projection restricted to the based hyperplane, attaining norm 1 on nonzero based mean-zero vectors. For mean-zero μ,
\(\|\mu-\mu(y){\bf1}\|^2=\|\mu\|^2+n\|\mu(y)\|^2\) and the sharp evaluation bound for a mean-zero n-vector is \(\|\mu(y)\|^2\le(n-1)\|\mu\|^2/n\), attained along the centered center-delta direction; hence norm √n. Tensoring with three SU(2) colors does not change this operator norm.

The map is uniformly bounded in **number of blocks when L is fixed**, but its inverse norm is strongly L-dependent; R115 should not assume T=I or a bound of 1 for either direction.

**Important inter-block obstruction:** If one subtracts the mean independently on each block B, then for an internal bond e=(x,x') lying in the same block, \((dJ\lambda)(e)=(d\lambda)(e)\). For a bond joining distinct blocks B and B', however,
\[
 \boxed{(dJ\lambda)(e)-(d\lambda)(e)
       =-\bigl(\bar\lambda_{B'}-\bar\lambda_B\bigr).}\tag{R116.7}
\]
This is a concrete **interface-supported gauge-gradient discrepancy**, not a norm-small error established by source hypotheses. The CMP99 nested Q', its Ω collars/Dirichlet boundary and CMP109 coarse-fixed gauge group cannot be identified by isolated-block mean subtraction on *all* bonds without an additional interface/boundary transport. Actual CMP99 \(\ker Q'\) may involve several scales and is not asserted to equal the elementary one-block E_mean. R116.5–R116.7 are tests/obstructions at an explicitly declared local model, not a certified counterexample inside the entire Balaban geometry.

## 5. Remaining exact native passport

| Gate | R116 status |
|---|---|
| CMP99 hard-gauge R range and gauge-parameter E | ORIGINAL-PAPER OCR source-located: range R=Delta ker Q' |
| CMP99 hard-GK rank on E | **EXACT SOURCE-SPECIFIC DERIVATION R116.1–R116.2** assuming stated finite Dirichlet positivity |
| R115 incorrect raw codomain | RE-TYPED as \(\widehat G:\mathcal H_{\rm bond}\to\ker Q'\) |
| CMP99 Delta_a vs physical A on simultaneous hard/fixed-average slice | **EXACT equality of quadratic forms** R116.4 from (3.26) |
| CMP99 later Delta_k and A_k/(3.156) reduced covariance | OPEN; original CMP99 (3.157)–(3.158) images unavailable |
| One isolated L13 block based/mean-zero site sections | EXACT change J and sharp inverse norm 169 in declared uniform-average model |
| Whole regional/nested site gauge and CMP109 based fine gauge identification | OPEN; explicit inter-block gradient discrepancy |
| CMP109 full reduced Q source-uniform coercivity, volume cutoff tail | OPEN |
| Paired Ω,V, inherited E/background determinant, normalized two-UV law | OPEN |
| Continuum YM existence / OS / positive mass gap | UNPROVED |

## 6. Stop and YM-R117 (unconsumed)

The **source's own hard gauge rank** and **basic positive-completion restriction** are not generic missing lemmas anymore; their operators are explicit. **YM-R117:** recover the actual *multiscale* CMP99 Q' nested/regional parameter space and its coarse-site relation to CMP109 based gauge at interfaces (not a crude one-block J); and recover original-page (3.157)–(3.158) to determine Delta_k/A_k and normalized Gaussian covariance transport. Then test whether the CMP99 uniform positivity lower bound feeds CMP109's actual reduced Q on a truly common finite regional chart. Only after that revisit source two-UV Ω,V and law estimates. No numerical gamma, polymer/coercivity convergence or positive physical mass gap declared.

Historical bibliography highest project [92] unchanged, past checkpoint append-only.
