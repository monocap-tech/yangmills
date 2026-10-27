# YM-R115 — CMP99/CMP109 gauge-slice transport and distinct reduced-precision gap

**Date:** 2026-10-27. **Prior certified:** [R114](../checkpoints/YM_HEAD_R114_20261027.json), merge e8300f6152b68e73fed95b508e7d027dde1c73d9. **Status:** COMPLETE AS SOURCE-TYPED GAUGE-QUOTIENT TRANSPORT AND TWO-OBLIGATION AUDIT, NOT ACTUAL SOURCE COERCIVITY OR TWO-UV LAW. **Next:** YM-R116 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Primary-source evidence and prior state

R114 verified CMP109 (2.5) positive quadratic gauge penalty and a conditional hard-gauge-to-soft-gauge vacuum coercivity theorem. Its missing input was the CMP99 hard-slice physical Hessian on the same source constraint space. This pass reads the exact candidate CMP99 source instead of assuming both “hard gauges” mean the same object.

T. Bałaban, *Propagators for lattice gauge theories in a background field*, CMP99(3), 389–434 (1985), DOI 10.1007/BF01240355, original-paper third-party OCR blob SHA **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**, path Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt in chboishabba/dashi_agda.

Reexamined OCR source locations:
- **1384–1419** (printed pp.417–418): CMP99 linearized averaging and hard gauge constraint R(U)D*A=0 in (3.110), and delta_R(RD*A) in (3.112), with Dirichlet boundary conditions. This is a distinct written gauge selector from CMP109's path-holonomy F.
- **1895–1938** (printed pp.427–428): (3.155) Gaussian integral, (3.156) source quadratic **A_k**, (3.157)–(3.158) its covariance relation, and a sentence claiming positive lower bound gamma0 for **C*Delta_k C** under specified regularity. The text does NOT literally assign gamma0 to a CMP109 soft gauge Hessian. OCR damaged equation (3.157)/(3.158) matrix symbols.
- **1990–2040** (printed pp.429–430): a gauge change B to B+D mu, the source's path-based site variable mu(B) (3.169), retention of R D*A (3.170) and prose describing a Faddeev–Popov delta-to-exponential replacement.
- **2090–2117** (printed p.432): constrained propagator representation (3.185), Theorem 3.15 decay.

CMP99 original printed mathematical images could not be obtained in R114 and remain UNVERIFIED. Do not upgrade third-party OCR to original-image status. CMP109 printed (0.15), (2.5), (2.11), (2.12) remain visually checked in the [54-page scanned source](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). [R115 receipt](../source_receipts/YM_R115_CMP99_HARD_SLICE_AND_PRECISION_RECEIPT_20261027.md).

Declared one-block test remains SU(2), legal L=13, averaging (0.4), source identity background and real finite-dimensional tangent W=ker D. It is not a source-verified two-independent-UV history pair.

## 1. Exact quotient-gauge slice transport (DERIVED)

Let E be the based infinitesimal Lie-site gauge space, W=ker D the constrained bond tangent, K:E->W its based gradient and F:W->E its source holonomy gauge coordinates. At the source identity vacuum R114 obtains FK=I (up to fixed orientation). Let G:W->E be the **candidate CMP99 hard gauge functional**, source-shaped by RD*, but its exact codomain, regional boundary and rank need direct certification.

Assume GK:E->E is invertible. Define
\[
 P_F=I_W-KF,\qquad P_G=I_W-K(GK)^{-1}G.
\]
Each is idempotent, annihilates im K, and has image respectively \(W_F=W\cap\ker F\) and \(W_G=W\cap\ker G\). Consequently
\[
 \boxed{T_{G\to F}=P_F|_{W_G}:W_G\xrightarrow{\cong}W_F,\qquad
 T_{G\to F}^{-1}=P_G|_{W_F}.}\tag{R115.1}
\]
**Proof:** for v_G∈W_G, F(P_Fv_G)=0 and P_G P_Fv_G=P_Gv_G=v_G since P_Fv_G-v_G is a gauge vector; similarly P_F P_Gv_F=v_F. The quotient section map is exact and need not be orthogonal.

**Native rank gate:** if actual CMP99 G has different dimension/rank from E, or GK is singular on its regional/based boundary, R115.1 cannot be promoted to the native source. Similar names, equal coarse lattice spacing or gauge covariance are insufficient to establish GK invertibility.

## 2. Quantitative hard physical Hessian transfer (DERIVED CONDITIONAL)

Let H0 be the *same real physical Wilson/action Hessian* on W, nonnegative and gauge Ward-invariant H0 K=0. Assume
\[
 \langle u,H_0u\rangle\ge\gamma_G\|u\|^2,\qquad u\in W_G.
\]
For v_F∈W_F take u=P_G v_F. Then v_F=P_Fu and H0[v_F]=H0[u]. Hence
\[
 \boxed{
 H_0|_{W_F}\succeq {\gamma_G\over\|P_F\|^2} I
 \succeq {\gamma_G\over(1+\|K\|\|F\|)^2}I.}\tag{R115.2}
\]
On ordinary oriented d=4 nearest-neighbor sites/links, R114 proved ||K||≤4. If the *entire real source soft precision* is exactly H0+beta F*F with beta>0, R114 then yields
\[
 \boxed{
 Q_{\rm soft}\succeq
 \min\left\{{\gamma_G\over2(1+4\|F\|)^2},{\beta\over32}\right\}I_W.}\tag{R115.3}
\]
No CMP99 numerical gamma_G is inserted. The norm F is also not yet source-computed. A future source-specific Schur bound is ||F||≤sqrt(rho_F*kappa_F) if its path-holonomy linear matrix has absolute row/column sums bounded respectively by rho_F and kappa_F, uniformly on the actual L=13 blocks. The correct coefficients and boundary/collar identifications remain open.

**Improvement over R114:** literal equality of hard gauge slices is unnecessary. A controlled section of the SAME gauge quotient suffices, if the CMP99 comparator is genuinely the physical H0 and its hard-slice estimate is native.

## 3. Second, independent operator/normalization mismatch

CMP99 OCR after (3.158) explicitly says the **positive lower bound is on C*Delta_k C**; (3.156) uses a differently named quadratic **A_k**. The precise (3.157)–(3.158) inverse relation is OCR-damaged. The source does not justify replacing the lower-bound object by \(H_0|_{W_G}\), by \(C^*A_k C\), or by CMP109 \(Q=C^*A^{(k)}C\) by citation alone.

In particular
\[
 C^*\Delta_k C\succeq\gamma_0 I
 \quad\not\Rightarrow\quad
 H_0|_{W_G}\succeq\gamma_G I
\]
without a genuinely source-verified form relation.

**Negative control:** W=R², K(lambda)=(0,lambda), F(x,y)=G(x,y)=y. Then W_F=W_G and GK=1: gauge slice matching is perfect. Let C*Delta C=I on this slice while physical H0=0. The comparator positive bound still says nothing about hard-slice H0 coercivity. This is a logical counterexample, not a CMP99 or CMP109 configuration.

Therefore two separate obligations remain, not one:
- **A — gauge topology:** verify actual CMP99 G, gauge functions E, boundary, GK rank and explicit controlled F transport;
- **B — precision custody:** image-recover exact CMP99 (3.155)–(3.158), identify Delta_k, A_k, its hard physical H0 and normalization/Jacobian on the transported same source slice.

CMP99's own Faddeev–Popov manipulations around (3.169)–(3.183) might furnish an exact connection, but they have not been reconstructed at original-image fidelity or on CMP109's actual boundaries.

## 4. Consequences and stop

| Gate | R115 |
|---|---|
| CMP99 hard RD* and CMP109 based F written selectors | SOURCE LOCATIONS RECOVERED; exact chart not matched |
| CMP99 own delta-to-exponential gauge manipulation | ORIGINAL-PAPER OCR WITNESS; image OPEN |
| Gauge-section isomorphism R115.1 | PROVED GIVEN GK INVERTIBLE |
| Hard physical Hessian transfer R115.2 and soft coercivity R115.3 | PROVED CONDITIONAL; actual gamma_G, F norm, full Hessian equality OPEN |
| CMP99 uniform lower bound on source Delta_k vs needed A_k/H0 | DISTINCT PRECISION TYPE GAP |
| Actual source K inverse, volume, cutoff threshold response | OPEN |
| True paired Omega/V, inherited E/determinant, normalized two-UV law | OPEN |
| Continuum YM, OS, physical mass gap | UNPROVED |

**Next YM-R116 unconsumed:** reconstruct source exact CMP99 quadratic Eq.(3.155)–(3.158) and its earlier unit-lattice [4] (2.154)–(2.155) reference with printed images if obtainable; type both precision and gauge section at source L=13 identity. Audit GK source rank and F locality and either prove a native hard physical gamma or certify the precise obstruction. Do not transfer the Thm 3.15 decay without operator normalization, and do not infer a two-cutoff mass-gap theorem.

Historical bibliography highest [92], append-only custody intact.
