# YM-R113 — source-locked CMP99/CMP109 precision provenance and gauge-fixing transfer gate

**Date:** 2026-10-27. **Native predecessor:** [YM-R112](../checkpoints/YM_HEAD_R112_20261027.json), main 7fa4c438d7f14b2d5d8b5cb9ea70f5ef7a6fc428. **Status:** COMPLETE AS PRINTED CMP109-TO-CMP99 DIRECT REFERENCE AUDIT, QUANTIFIED POSITIVITY TRANSFER TEST, AND ORIGINAL CMP109 EQUATION-IMAGE RECOVERY; SOURCE GAUGE-FIXING EQUIVALENCE AND TWO-CUTOFF LAW OPEN. **Next:** YM-R114 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Recovery and evidence discipline

The authoritative append-only protocol requires that source equations, independent deductions, counterexamples and open transfers remain separate. R112 gave actual CMP109 reduced Gaussian precision Q=C* A^(k) C on the source constraint graph, with C=(I-hD)E and PC=I. At SU(2) identity background Q=K tensor I3, and each monitored Gaussian Lie-bond has an exact Maxwell radial tail conditional on the true inverse diagonal of K.

**PRIMARY PRINTED CMP109 images directly reinspected:** original published pages 267, 268, 258, 297, 299, from the [54-page third-party scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), zero-based PDF indices 18,19,9,48,50. See [R113 source receipt](../source_receipts/YM_R113_CMP99_PRECISION_SOURCE_AND_CMP109_IMAGE_RECEIPT_20261027.md). **CMP99** mathematical equations were read in the pinned original-paper third-party OCR blob ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743; original printed CMP99 equation images remain UNVERIFIED. Neither is the same custody level as a publisher-hosted source. Historical repository R81/R82 covariance audits were reread, not replaced.

## 1. A newly decisive direct source provenance

**SOURCE-VERIFIED printed CMP109 p.267:** the quadratic form in the fine fluctuation B' is the operator A^(k), and it is identified by a direct citation to equation (3.156) of **paper [13]**, with the paper's delta-function gauge fixing replaced by exponential gauge fixing.

**SOURCE-VERIFIED printed CMP109 p.299 bibliography:** reference [13] is T. Bałaban, *Propagators for lattice gauge theories in a background field*, CMP **99(3)** (1985), 389–434, DOI 10.1007/BF01240355. Reference [15] is *The variational problem and background fields*, CMP102(2) (1985), 277–309. Thus this is not a conjectural shared-name inference. The actual chain is:

  CMP99 [13] quadratic precision Eq.(3.156)
     -- change delta-function gauge fixing to exponential -->
  CMP109 Eq.(2.11) quadratic form A^(k)
     -- restrict by CMP109 linearized source constraint C -->
  Q_109 = C* A^(k) C.

The source link does NOT state that the change of gauge-fixing prescription leaves Q, its lower bound or its normalized measure unchanged. Moreover it does NOT justify identifying CMP102's Delta_1 with CMP99 Delta_a by equal numerical subscripts; the earlier R39/R81 holds remain respected.

**ORIGINAL-PAPER CMP99 OCR witness:** CMP99 at OCR lines 1895–1938 contains (3.155) Gaussian integrals, (3.156) quadratic form on an explicitly constrained/gauge-fixed subspace, (3.157)–(3.158) reduced covariance definitions, and prose that the operator C*Delta_k C has a positive lower bound gamma0>0 independent of k and regular U when M alpha0 is sufficiently small. The source attributes its vacuum bound to an earlier lemma and nontrivial-background extension to localization/regularity arguments. CMP99 OCR lines 2090–2117 locate its constrained covariance representation (3.185) and Theorem 3.15, with a spatial exponential-decay bound and constants depending on d,L. **Exact CMP99 symbolic definitions and theorem hypotheses have not been original-image verified.** The CMP99 covariance on a delta-gauge slice, the later exponential-gauge representation and CMP109's Q must not be equated without reconstructing the gauge/chart/normalization transfer.

**New source result:** the prior *operator provenance* gap is closed at the precise level of a cited predecessor; the *quantitative positivity transfer* remains the single typed seam rather than an unlocated parallel operator.

## 2. Exact finite-dimensional sufficient transfer inequality (DERIVED, not source-established)

Let Q_* be the positive self-adjoint source comparator precision, on an explicitly identified finite real independent-coordinate Hilbert space, with Q_* >= gamma0 I for gamma0>0. Let T map current CMP109 independent coordinates into the comparator coordinates and be injective with ||Tx||>=t||x||, t>0. Define the self-adjoint source gauge/chart defect
  R = Q_109 - T* Q_* T.

If R>=-delta I and delta<gamma0*t*t, then
\[
 \boxed{Q_{109}\succeq(\gamma_0t^2-\delta)I,\qquad
        \|Q_{109}^{-1}\|_{\rm op}\le(\gamma_0t^2-\delta)^{-1}.}\tag{R113.1}
\]
**Proof:** for every x, <x,Q109 x>=<Tx,Q*Tx>+<x,Rx> >= gamma0||Tx||²-delta||x||² >=(gamma0 t²-delta)||x||². Invert via spectral calculus. On a truly identical graph, T=I, but this equality is not established by sharing the term “propagator”.

At the actual R112 SU(2) identity-background Gaussian, if the source hypotheses R113.1 hold and a=gamma0*t²-delta>0, then every Maxwell scale s_b²=(K^-1)_bb <=a^-1, so its cutoff failure satisfies
\[
 q\le \min\{1,n\,\mathcal Q_3(\theta_k\sqrt a/|g_k|)\},\quad
 \mathcal Q_3(z)=\operatorname{erfc}(z/\sqrt2)+\sqrt{2/\pi}\,z e^{-z^2/2}.
 \tag{R113.2}
\]
Proof: monotonicity of the radial survival function and R112's exact bond Gaussian reduction. For the alternate source threshold theta_k=g_k*epsilon1/gamma_k, the g_k again cancels from the argument. The required native delta,t,gamma0 identification, n and volume-uniform control remain **UNESTABLISHED**, so (R113.2) is not an actual source-number certificate.

**Required computational/source passport:** native common real Hilbert metric and background; comparator Eq.(3.156) and (3.158) precision on its delta-slice; current A^(k) from CMP109 (2.11) with exponential gauge; source graph C0,C1 and chart T; sign or norm of R on that common chart; actual gamma0 and any uniformity; determinants and inherited effective E. The words “with gauge fixing replaced” do not supply this passport.

## 3. NEGATIVE CONTROL: hard-gauge covariance cannot directly dominate soft-gauge covariance

On H=R² with coordinates (x,y), consider positive soft-gauge precision
\[
 A_\epsilon=\begin{pmatrix}1&\sqrt{1-\epsilon}\\
                       \sqrt{1-\epsilon}&1\end{pmatrix},
 \quad 0<\epsilon<1.
\]
On the hard gauge slice y=0, the normalized x-Gaussian has precision 1 and variance 1, independent of epsilon. Integrating over y instead yields the soft-gauge marginal x variance
\((A_\epsilon^{-1})_{xx}=1/\epsilon\to\infty\).

This proves that a positive and even uniformly coercive *hard-slice precision* does NOT by itself imply a uniform bound after replacing the gauge constraint by a soft Gaussian weighting. The example is elementary and is **NOT a CMP109 configuration**; it only refutes an invalid automatic inference. Additional Ward/constraint decoupling or operator form estimates may rule it out in the true theory, but those must be source-derived, not presumed.

This warns against an incorrect shortcut from CMP99 Theorem 3.15 to Q_109, especially before proving the equality of gauge-fixed domains and source normalizers. Spatially localized covariance bounds likewise need a localized R and transported Green representation; R113.1 alone gives a diagonal variance bound, not exponential spatial decay or the weighted second moments of R81.

## 4. CMP109 original-image holds resolved, NOT cross-cutoff theorem closure

Direct printed CMP109 images have now been inspected for **all three** historical equations:
- **(0.29), printed p.258, PDF index 9:** source positive-alpha irrelevant polymer activity bound |V^(j)(X,U_k)| <= O(1)(L^j eta)^(4+alpha) exp[-kappa d_j(X)] with alpha>0; it enters a one-trajectory sum and depends on the prescribed small-field/coupling hypotheses. It is NOT an actual N versus N+1 summable difference.
- **(5.37), printed p.297, PDF index 48:** polarization tensor Pi_mu,nu(p) splits into beta times the gauge-invariant lattice differential symbol and an analytic third-derivative remainder Pi'. Does not equate Pi in independently chosen cutoff histories.
- **(5.42), printed p.297, PDF index 48:** beta=-partial_{p1}partial_{p2} Pi_12(0), equivalently the discrete spatial mixed second moment sum_x Pi_12(x)*x1*x2 with source Fourier convention; the covariance/interaction/normalizer differences necessary to compare those moments are still open.

**Evidence custody change:** the three displayed original-paper equations are no longer *image-unread*; their hypothesis/domain applicability, summability across independent bare choices and quantitative RG comparison remain OPEN. This is neither a four-dimensional existence theorem nor a positive mass gap, and it does not transfer the cited external Sussman–Alpöge pair theorem.

## 5. Verdict and exact stopping point

| Gate | YM-R113 |
|---|---|
| CMP109 A^(k) exact predecessor reference | SOURCE-PRINTED DIRECT CROSS-REFERENCE to CMP99 [13] (3.156), with explicit changed gauge-fixing |
| CMP99 bounded reduced precision and covariance localization | ORIGINAL-PAPER OCR PROSE/EQUATION LOCATED; source original image open |
| Literal Q_109 equality to CMP99 delta-gauge covariance precision | NOT ESTABLISHED; gauge/chart transfer needed |
| Conditional coercivity bridge | DERIVED R113.1 with explicit t,delta and gamma0 |
| Conditional SU2 Maxwell tail with comparator bound | DERIVED R113.2; no numeric/current source a |
| Hard-slice positivity automatically implies soft-gauge covariance bound | REFUTED by finite 2x2 example |
| CMP109 (0.29),(5.37),(5.42) | PRINTED ORIGINAL EQUATION IMAGES INSPECTED; cross-UV estimates OPEN |
| Source uniform Q eigenvalue/diagonal, native Omega/V, full normalized two-cutoff law | OPEN |
| Continuum four-dimensional Yang–Mills, OS, positive gap | UNPROVED |

**YM-R114 unconsumed:** inspect actual original CMP99 (3.156)–(3.158), theorem 3.15 hypotheses if accessible, and reconstruct the exact *gauge-fixing replacement* form between the CMP99 reduced operator and CMP109's Q on a common legal identity-background finite block. Test a sign/relative bound for R, or exhibit a source-specific obstruction; use actual T, gamma0, chart and determinant. Only afterward pursue vacuum variance/volume and two independent Omega/V histories. The three CMP109 primary formula-image holds are now closed as image evidence, not as theorem gates. No invented numeric covariance rate. Historical highest bibliography reference [92] unchanged.
