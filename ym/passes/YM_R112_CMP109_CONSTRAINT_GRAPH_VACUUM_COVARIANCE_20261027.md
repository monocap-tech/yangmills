# YM-R112 — exact CMP109 constraint graph and SU(2) vacuum covariance reduction

**Date:** 2026-10-27. **Prior main:** [YM-R111](../checkpoints/YM_HEAD_R111_20261026.json), merge 7b4f4eea1f0f6ee36887f58e3169fb6b937014d8. **Determination:** COMPLETE AS PRINTED-SOURCE LINEAR-CONSTRAINT GRAPH RECONSTRUCTION AND EXACT ONE-BACKGROUND COLOR-ISOTROPIC TAIL FORMULA; NO COMPUTED SOURCE UNIFORM COVARIANCE BOUND OR TWO-CUTOFF LAW. **Next native cursor:** YM-R113 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 1. Source, test carrier and exact scope

Primary text: Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP 109(2) (1987), DOI https://doi.org/10.1007/BF01215223. Direct visually inspected published printed-page images through a third-party-hosted [54-page scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), zero-based PDF pages **2, 4, 5, 16, 17, 18, 19, 20**, printed pp.251,253,254,265–269. [Dedicated receipt](../source_receipts/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_SOURCE_RECEIPT_20261027.md).

Test carrier: the source-permitted Euclidean average (0.4), compact G=SU(2), permitted odd L=13, and **one fixed identity coarse background U=1** (which is regular and has source average M(1)=1). The identity field supplies an actual lawful local reference background in the small-field chart. The choice does **not** instantiate an independently normalized full bare RG history, nor a paired N,j and N+1,j+1 sequence satisfying matching Ω,V and inherited E.

R111 verified χ_k (2.9) monitors precisely the bonds other than distinguished b0(c), while the nonlinear shift h*Dtilde is supported only on b0(c). R112 now reads the **linearized constraint equation** itself and constructs C directly instead of carrying an unspecified embedding map.

## 2. EXACT SOURCE/DERIVATION — explicit constraint graph operator C

Let \(\mathcal H=\mathfrak{su}(2)^{\mathcal B}\) be a finite real Lie-algebra bond space, \(\mathcal M=\mathfrak{su}(2)^{\mathcal B\setminus\mathcal B_0}\) the independent monitored bonds, and \(\mathcal J\) the source coarse constraint coordinates. The source p.267 uses the linear term \(D=L\widetilde Q:\mathcal H\to\mathcal J\), and constructs a **right inverse** \(h:\mathcal J\to\mathcal H\) with
\[
 Dh=I_{\mathcal J},\qquad (hz)(b)=0\quad(b\notin\mathcal B_0).
\]
Write \(P:\mathcal H\to\mathcal M\) for coordinate deletion of \(\mathcal B_0\), and \(E=P^*:\mathcal M\to\mathcal H\) for zero-extension on distinguished bonds. Then
\(PE=I_{\mathcal M}\), \(Ph=0\).

The linear constraint is \(DB'=0\). Its **unique graph extension at specified independent coordinates** is
\[
 \boxed{C=(I_{\mathcal H}-hD)E.}\tag{R112.1}
\]
Indeed \(DC=DE-(Dh)DE=0\), \(PC=PE-(Ph)DE=I\). If \(x\in\ker D\), then
\(C(Px)=EPx-hDEPx=EPx+hD(I-EP)x=x\): on the distinguished-only vector \((I-EP)x\), the source's right inverse h is the inverse of D, so \(hD(I-EP)x=(I-EP)x\). Equivalently \(x-EPx\in\operatorname{im}h\) and \(Dx=0\). This uniqueness uses the source's precise statement that the distinguished-bond coefficients are invertible; a right inverse merely supported there and one source constraint per distinguished coordinate supplies that property.

Consequences:
\[
 \boxed{DC=0,\qquad PC=I,\qquad
       \operatorname{im}C=\ker D,\qquad C^*C\succeq I.}\tag{R112.2}
\]
The second and fourth results use the real orthonormal coordinate inner products. This is the **exact source algebraic reconstruction** of the otherwise opaque C appearing on printed p.268: after delta elimination, the remaining independent variables B have full linear fluctuation \(B'=CB\).

The nonlinear source change on printed p.267 is \(B'_{\rm old}=X-h\widetilde D(X)\), where \(\widetilde D\) starts quadratically. Since \(Ph=0\), this has *no effect* on the monitored coordinates (R111); the nonlinear map and its Jacobian remain genuine components of the full fluctuation integral.

## 3. Exact reduced Gaussian precision, not an invented numerical covariance

Let \(A^{(k)}(U)\) be the real symmetric quadratic fluctuation operator in CMP109 (2.11)–(2.12), on the source's gauge-fixed bond space. The reduced precision and covariance are
\[
 Q_{k,U}=C_{k,U}^*A^{(k)}(U)C_{k,U},\qquad
 \Sigma_{k,U}=Q_{k,U}^{-1},\tag{R112.3}
\]
whenever this reduced form is positive definite on the eligible real finite-dimensional chart. By (R112.2),
\[
 \boxed{S_{k,U}=PC\Sigma C^*P^*=\Sigma_{k,U}.}\tag{R112.4}
\]
The monitored covariance IS the independent-coordinate covariance. Thus R111's proposed extra projection S introduces no additional operator/estimate.

**Computable graph precision form:** order full bond coordinates as (monitored m, distinguished d). Let source D have blocks \(D_m,D_d\) with invertible local \(D_d\). The graph correction is \(T=-D_d^{-1}D_m\); \(C=\binom I T\). Hence
\[
 \boxed{Q_{k,U}=A_{mm}+A_{md}T+T^*A_{dm}+T^*A_{dd}T.}\tag{R112.5}
\]
All terms are restrictions of the actual source quadratic operator, not toy coefficients. This provides an explicit finite-matrix recipe without constructing or inverting a full-dimensional Gaussian covariance. The actual source entries, size and a numerically verified coercivity bound have **not** been computed.

For a monitored unit coordinate e, the variance
\[
 v_e=e^*Q^{-1}e=\sup_{x\ne0}\frac{|\langle e,x\rangle|^2}{\langle x,Qx\rangle}.
\]
If one subsequently proves **source-native** coercivity \(\langle x,Qx\rangle\ge a_{k,U}\|x\|^2\), then \(v_e\le 1/a_{k,U}\). The finite-volume value \(a_{k,U}>0\) does not imply a cutoff-independent lower bound. In particular the finite-dimensional positive matrix \(Q=\epsilon I\) shows that symmetry/positivity alone allows variance \(1/\epsilon\to\infty\). This is a *logical negative control*, not a claim about Bałaban's Q.

**Optional stronger identity only if the ambient A is strictly positive:** \[
 C(C^*AC)^{-1}C^*
 =A^{-1}-A^{-1}D^*(DA^{-1}D^*)^{-1}DA^{-1}.
\]
This is the Gaussian conditional covariance given \(DB'=0\); then monitored covariance is bounded by \(PA^{-1}P^*\). Do NOT invoke that comparison unless ambient positive invertibility, not merely positivity on the constrained slice, has been source-certified.

## 4. SU(2) identity-background COLOR REDUCTION — genuine new fixed-reference calculation

At U=1 and with the source's conjugation-equivariant averaging (0.4), an arbitrary global \(g\in SU(2)\) acts on every Lie-algebra bond coordinate by the same adjoint rotation \(R_g\in SO(3)\). At this background, the Wilson action, Haar/trace gauge fixing, linearized constraint D, distinguished-bond right inverse h, and quadratic action operator A are all globally color-equivariant; the source explicitly records gauge covariance/invariance of the cutoff and one-step action at (2.16) on p.269. Thus the reduced real Hessian Q commutes with **every** simultaneous \(R_g\).

The real 3-dimensional adjoint representation of SU(2) is irreducible and its commutant consists only of real scalars. Applying this to every pair of monitored bonds yields
\[
 \boxed{Q_{k,\mathbf1}=K_k\otimes I_3,\qquad
 \Sigma_{k,\mathbf1}=K_k^{-1}\otimes I_3.}\tag{R112.6}
\]
Here K_k is an *unknown positive-definite real bond-index matrix*. Color isotropy is exact; numerical eigenvalues of K_k and cross-depth compatibility are OPEN. No color-isotropy claim is made at a generic nontrivial external background where conjugation rotates U as well.

For each monitored bond b, let \(s_b^2=(K_k^{-1})_{bb}\). Its Gaussian Lie-algebra vector is \(Z_b\sim N(0,s_b^2 I_3)\); different bonds can remain correlated. Source cutoff (2.9), after R111's exact monitored projection, requires \(\|g_kZ_b\|<\theta_k\). The 3D Maxwell/chi-distribution survival function is
\[
 \mathcal Q_3(t)=
 \operatorname{erfc}(t/\sqrt2)+
 \sqrt{2/\pi}\,t\,e^{-t^2/2}.
\]
Therefore on this one identity-background Gaussian carrier
\[
 \boxed{q_{k,\mathbf1}
 \le\min\left\{1,\sum_{b\in\mathcal B_{\rm mon}}
 \mathcal Q_3\!\left({\theta_k\over |g_k|s_b}\right)\right\}.}\tag{R112.7}
\]
**Proof:** \(s_b^{-2}\|Z_b\|^2\sim\chi_3^2\); integrate the radial Gaussian density and union bound. No cross-bond independence is required. Compared with the general R111 bound \(2(3)n\exp[-\theta^2/(6g^2v)]\), this retains the correct 3D radial exponent \(-\theta^2/(2g^2s_b^2)\) (with a polynomial prefactor). It is a genuine improvement at the identity reference, not an asserted uniform probability estimate.

Threshold branches remain distinct: at \(\theta_k=\varepsilon_1\) the argument is \(\varepsilon_1/(|g_k|s_b)\); for \(\theta_k=g_k\varepsilon_1/\gamma_k\) and positive g_k it is \(\varepsilon_1/(\gamma_k s_b)\). Again the alternate branch **does not automatically improve as \(g_k\downarrow0\)**.

The formal Gaussian cutoff event includes an open neighborhood of B=0. For any finite positive covariance and positive threshold its Gaussian probability p is strictly positive; the full interaction-weighted Z of CMP109 (2.13) still requires source integrability/chart verification.

## 5. Actual source-to-source gap after R112

Previous archived native [YM-R81](YM_R81_MOVING_PROJECTOR_SOURCE_COVARIANCE_AUDIT_20261010.md) and [YM-R82](YM_R82_COVARIANCE_FIRST_INTERPOLATION_AUDIT_20261010.md) already distinguish CMP99 background Green/covariance decay, CMP116 product Gaussian/root, and the CMP109/CMP102 precision choices. Their source theorems **must not** be silently identified with \(Q=C^*AC\) or K_k. An actual numerical/uniform variance result requires establishing the corresponding operator dictionary, verifying source regularity/positivity domains, and obtaining a bound on \(K_k^{-1}\)'s diagonals on the chosen geometry.

| Gate | R112 result |
|---|---|
| Source D,h/P,E graph | EXACT C=(I-hD)E on valid chart |
| Monitored covariance | EXACT S=Σ=(C*AC)^-1 |
| Reduced Hessian | EXPLICIT source block-operator recipe Q=A_mm+A_md T+T* A_dm+T*A_dd*T |
| SU2 identity background | Q=K tensor I3, exact color-isotropy reduction |
| Three-component vacuum Gaussian tail | Exact Maxwell-marginal formula and union estimate, conditional on source Gaussian |
| Numerical/varying-cutoff a_k, s_b and n | NOT CERTIFIED |
| Analytic chart, nonlinear Jacobian and inherited E/determinant | OPEN |
| Actual admissible N,j vs N+1,j+1 Omega,V and laws | OPEN |
| Original CMP98/CMP102b, CMP109 (0.29),(5.37),(5.42) image holds | OPEN |
| YM continuum existence, OS axioms, positive spectral gap | UNPROVED |

## 6. STOP — YM-R113 unconsumed

Use (R112.1)/(R112.5) as the **minimal operator passport**. Next, recover from source [13] CMP99 and [15] CMP102b or the existing source-native CMP116 representation a correctly typed positivity/locality estimate **for this exact Q**, ideally in the trivial SU2 vacuum as first anchored case. Then compute or bound actual K inverse diagonal/n versus the source selected threshold and chart conditions. Only after that seek an aligned pair of actual prescribed V,Omega histories, inherited E/determinant transport and summable observable law difference. Do not spend another pass bounding the nonexistent cutoff displacement or assert that a bounded fixed-background Gaussian tail proves 4D Yang–Mills construction.

Bibliography remains through reference [92]; repo append-only custody preserved.
