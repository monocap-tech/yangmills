# YM-R114 — the positive exponential-gauge quadratic and a vacuum gauge-extension coercivity gate

**Date:** 2026-10-27. **Resumed from:** [YM-R113](../checkpoints/YM_HEAD_R113_20261027.json); verified main 08718aae3c786b8ad8f8dc09010ceccb55aa8078. **Status:** COMPLETE AS PRIMARY CMP109 GAUGE QUADRATIC IMAGE AUDIT AND EXACT CONDITIONAL VACUUM GAUGE-EXTENSION THEOREM. **Not complete:** CMP99 original-page equation custody, actual hard-slice matching/coercivity, two-UV normalized-law estimates or mass gap. **Next:** YM-R115 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Research target and evidence boundary

R112 constructed CMP109's source linear graph C=(I-hD)E with DC=0, PC=I, source reduced precision Q=C*AC and SU(2) vacuum color isotropy. R113 located the published paper's explicit reference from CMP109 (2.11) to CMP99 (3.156), with *hard delta* versus *exponential* gauge fixing, and the CMP99 OCR lower-bound claim on its own reduced operator. R114 tests what that difference does in the source's actual local vacuum geometry rather than supposing an arbitrary negative Hessian defect.

**Direct original printed-page CMP109 visual checks** in third-party 54-page [scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf):
- PDF index 5, printed p.254, (0.13)–(0.15): under the based gauge group u(y)=1 on coarse vertices, the path holonomy U(y,x) transforms by a right endpoint u(x)^(-1). Exponential gauge factors are Haar normalized; this is an exact FP identity, not a physical cutoff loss.
- PDF index 17, printed p.266, **(2.5)**: G(B')=1/2 sum over coarse y and internal fine sites x of ||Btilde(y,x)||² + G_3(B'), where Btilde(y,x) is LINEAR in B' and G_3 begins at cubic order. This explicitly shows **nonnegative quadratic gauge-fixing precision** on the real chart.
- PDF index 18, printed p.267, (2.10)–(2.11): expansion separates gauge-fixing G and action Hessian, then forms A^(k), with the hard-delta-to-exponential source change noted at (2.11).
- PDF index 19, printed p.268, (2.12): source reduced Gaussian covariance (C* A^(k) C)^(-1) and retained determinants/nonlinear interactions.
- PDF index 16, p.265, (2.1)–(2.3): regular small-field source data and stationary constrained background.

**CMP99 original-page search:** Springer DOI content PDF 10.1007/BF01240355.pdf redirected to subscription preview, Project Euclid direct route and guessed UM DeepBlue PDF handles were inaccessible; no original printed CMP99 equation images were actually seen. Original-paper OCR blob ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743 remains a *lower custody level*, with (3.156)–(3.158), (3.185), Thm 3.15 at recorded line locations. These source holds do not license assigning its gamma0 to CMP109.

## 1. SOURCE-SHAPED exact based gauge coordinate and positivity

At the identity SU(2) vacuum in a single legal L=13 block, let H be the real finite-dimensional full bond fluctuation Hilbert space, W=ker D the **source linearized fixed-average** tangent space, and E_site the Lie-algebra-valued functions lambda(x) vanishing at coarse centers. Let K:E_site -> H be the infinitesimal based gauge gradient: (K lambda)(b)=lambda(b_+)-lambda(b_-), up to the standard orientation sign. By gauge covariance of source averaging under u(y)=1 at coarse vertices, **D K=0**, so im K is contained in W.

Let F:H -> E_site be the linearization of the source holonomy gauge coordinate Btilde(y,x) of (2.5). Under a based gauge u(y)=1, U(y,x) -> U(y,x)u(x)^(-1), hence differentiation at U=1 gives **F K=-I** for the orientation above. Replace K by -K if necessary so that
\[
 \boxed{DK=0,\qquad FK=I.}\tag{R114.1}
\]
The mathematical statement is local to the based-gauge transformation and source block, not a global gauge chart. It requires a unique fine-site assignment to its coarse center in the source block cover.

From printed source (2.5), the real quadratic gauge contribution is \(G^{(2)}(B)=\frac12\|FB\|^2\). In the Gaussian precision after the source g_k scaling this contributes \(F^*F\succeq0\) (or a positive coefficient beta times that form if a different source gauge parameter convention is used); the cubic G3 is **not** a quadratic precision and belongs to the R110 interaction. A nonnegative source quadratic term does not by itself bound all transverse modes, and the Haar normalization of the group gauge identity does not remove this quadratic from the *gauge-fixed coordinate representation*.

## 2. Exact splitting theorem, quantitative vacuum coercivity

**Theorem R114.2 — based-gauge extension.** Suppose:
(A) W=ker D is a finite-dimensional real Hilbert space with a based gradient K:E_site -> W and a bounded linear F:W -> E_site satisfying FK=I;
(B) H0 is a self-adjoint real quadratic-form operator on W with H0>=0, and H0 K=0 in quadratic-form/polarization sense (gauge invariance at a stationary identity vacuum);
(C) on the hard-gauge slice \(W_0=W\cap\ker F\) we have
\[
 \langle v,H_0v\rangle\ge\gamma\|v\|^2\quad(v\in W_0),\quad \gamma>0;
\]
(D) the exponential gauge-fixed precision is \(Q_{\rm soft}=H_0+\beta F^*F\) on W with beta>0 and no omitted quadratic chart term.

For every B in W, set lambda=FB and v=B-K lambda. By FK=I, Fv=0; by DK=0 both v and K lambda are in W. Hence
\[
 \boxed{W=W_0\oplus\operatorname{im}K,\qquad
        B=v+K\lambda,\quad\lambda=FB.}\tag{R114.2}
\]
The splitting is algebraic, not necessarily orthogonal. Gauge-Hessian invariance gives H0(B)=H0(v); gauge penalty is beta||lambda||², so
\[
 Q_{\rm soft}[B]\ge\gamma\|v\|^2+\beta\|\lambda\|^2.
\]
Using \(\|B\|^2\le2\|v\|^2+2\|K\|^2\|\lambda\|^2\),
\[
 \boxed{
 Q_{\rm soft}\succeq
 \frac12\min\{\gamma,\beta/\|K\|^2\}I_W.}\tag{R114.3}
\]
Proof is the preceding calculation. If W is restricted to an actual CMP109 graph C with PC=I and the full inner product is the ordinary real bond sum, then \(\|Cb\|\ge\|b\|\) and the reduced Q=C* Qsoft C has the SAME lower bound on independent monitored coordinates.

**Dimension-explicit incidence bound:** on a d-dimensional oriented nearest-neighbor hypercubic lattice with one copy of each edge, a site lambda (zero on coarse sites) obeys
\(\sum_b\|\lambda(b_+)-\lambda(b_-)\|^2
\le2\sum_b[\|\lambda(b_+)\|^2+\|\lambda(b_-)\|^2]
\le4d\sum_x\|\lambda(x)\|^2\).
Thus \(\|K\|\le2\sqrt d\), and at source d=4
\[
 \boxed{Q_{\rm soft}\succeq
    \min\{\gamma/2,\beta/32\}I,\quad\text{on the stated source-compatible block}.}\tag{R114.4}
\]
This lower bound has *no volume factor from K*, but the unverified gamma may depend on source hypotheses, chart, boundary and L. Equation R114.4 is a **conditional theorem**, NOT proof of a new uniform Yang–Mills source gamma.

This gate is strictly better typed than R113's general arbitrary negative-defect R: the **actual gauge sector of the vacuum source has a positive quadratic penalty** and need not be modeled as an uncontrolled negative perturbation *if* the source hard/soft slices match.

## 3. Missing source CMP99 interface is narrower, not discharged

CMP99 original-paper OCR around (3.156)–(3.158) reports a uniform lower bound gamma0>0 for a constrained precision denoted C*Delta_k C under earlier source regularity conditions. But R114 cannot identify that operator's hard gauge slice and Hilbert norm with W0 of Theorem R114.2 merely from the common labels delta gauge and (3.156).

For *native use*, it remains necessary to prove all of:
1. The actual CMP99 [13] hard delta constraints and boundary/collar geometry can be transported to the same W=ker D as CMP109 source choice (0.4), based gauge K and F; no hidden extra R D* gauge condition changes W0.
2. The positive CMP99 comparator lower bound, with the correct source lattice metric and normalization, applies to the physical Wilson/action Hessian H0 restricted to precisely W0, not a differently completed precision including extra penalties.
3. The **actual** source Eq.(2.11) Qsoft on W is exactly H0+beta F*F at U=1, with no additional quadratic measure/Jacobian term and beta of the stated sign/normalization; the source images show the G quadratic, but the full CMP99 Hessian equality still needs the original equation.
4. The geometry and constants remain valid for each genuinely admissible source block, not merely at the identity test. Establish any extension to nontrivial U using native positivity/analyticity rather than vacuum conjugation.
5. Finally, the Gaussian cutoff, chart/Jacobian, inherited effective E and background determinant must be transported along *two distinct UV histories* and not confused with a single-block positive Hessian.

**NEW REFUTE-FIRST DETERMINATION:** The generic concern that the gauge change must introduce an arbitrary negative quadratic defect is excessive for the source identity vacuum: the displayed gauge penalty is positive, and the necessary source transfer reduces to hard-slice identification and Hessian matching. But it is invalid to conclude “CMP99 gamma0 implies CMP109 a” before these matches.

## 4. Source-shaped vacuum tail remains conditional

If Theorem R114.2 hypotheses are verified natively with a positive lower bound a for the true reduced CMP109 Q at SU(2) identity, then R112's color isotropy gives the exact finite-volume tail comparison
\[
 q\le\min\{1,n\mathcal Q_3(\theta_k\sqrt a/|g_k|)\},\quad
 \mathcal Q_3(t)=\operatorname{erfc}(t/\sqrt2)+\sqrt{2/\pi}t e^{-t^2/2}.
\]
This is derived, not a source-certified numeric result. For theta_k=g_k epsilon1/gamma_k the coupling cancels. Neither n nor full chart exit, interactions, or two-history covariance differences have a proved summable bound.

## 5. Gate ledger / bounded stop

| Gate | YM-R114 |
|---|---|
| Actual CMP109 exp gauge quadratic | PRINTED (2.5) POSITIVE SUM OF SQUARES; G3 at cubic order |
| Based gauge coordinate FK=±I, DK=0 | EXACT DIFFERENTIAL CONSEQUENCE of source block holonomy/gauge covariance at vacuum |
| Full tangent hard/gauge splitting | R114.2 DERIVED under source-compatible W,K,F |
| Explicit d=4 soft coercivity lower bound | R114.4 CONDITIONAL on same hard-gauge Hessian gamma and no other quadratic term |
| Source CMP99 original printed (3.156)–(3.158), Thm.3.15 | ATTEMPTED; publisher preview, Project Euclid/DeepBlue inaccessible; OCR-only |
| CMP99 gamma0 on exactly W0 of CMP109 | NOT ESTABLISHED |
| Genuine CMP109 a_k and normalized two-UV Gaussian law | OPEN |
| CMP109 (0.29),(5.37),(5.42) printed image holds | CLOSED as evidence in R113; cross-UV estimates OPEN |
| 4D continuum YM / OS / positive mass gap | UNPROVED |

**Next YM-R115 unconsumed:** inspect the *actual* CMP99 Eq.(3.156)–(3.158) printed image if an accessible scan appears, and construct the *same-chart* W0 hard-gauge source datum for CMP109 L=13 choice (0.4). Prove/refute H0|W0=source comparator and check all hidden gauge constraints/normalizations; only then apply R114.4 and count monitored bonds in one real finite source torus and pair. Do not repeat abstract gauge positivity or infer global continuum claims.

Source numbered bibliography upper bound [92] retained. Earlier checkpoints append-only.
