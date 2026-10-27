# YM-R106 — finite-Wilson aligned observable cospan, matching-law criterion and small-field complement

**Date:** 2026-10-26. **Prior canonical head:** [YM-R105](../checkpoints/YM_HEAD_R105_20261026.json) (GitHub main base 461b44300d80e34722a0f06c120825ffe9c58bf6). **Classification:** COMPLETE AS FINITE-WILSON TEST-CARRIER / EXACT ABSTRACT COUPLING AND NECESSARY-OBSTRUCTION AUDIT. **NOT COMPLETE:** actual Bałaban paired-domain/data construction, full-history law estimate, history summability. **Next cursor:** YM-R107, unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Refute-first question and source jurisdiction

R105 found that the external Sussman–Alpöge YM4 draft Part III §9.3 defines paired variational inputs with \(\Omega'_{j+1}=\Omega_j\) and identical prescribed \(V\) on corresponding determining layers. Neither native scale alignment \(\eta_{N+1,j+1}=\eta_{N,j}\) nor separate curvature smallness constructs that input. Background-minimizer and sandwiched covariance/root theorems at draft III:35626–35641 and 36675–36807 remain unverified, with declared incomplete dependencies (fine propagator, exact paired shells, differences of nested large-field Gaussian integrations). See [R105](YM_R105_PAIRED_VARIATIONAL_CARRIER_LAW_SEPARATION_20261026.md), [pinned receipt](../source_receipts/YM_R105_PAIRED_CARRIER_SOURCE_RECEIPT_20261026.md).

R106 tests the **observable-cospan alternative** on one explicit, aligned physical plaquette in a finite SU(2) Wilson lattice system. This is a *kinematic/finite-measure test*, not a claim that the path-product map is Bałaban's nonlinear gauge-covariant averaging \(M\), nor that the tested finite Wilson systems are already the source-defined full renormalized histories. It then proves the exact distributional prerequisite for a shared-data coupling and a necessary obstruction to globally pairing untruncated positive Wilson measures exclusively in a proper small-field sector.

## 1. One actual finite-lattice gauge-invariant observable cospan (positive typed construction)

Fix \(L\ge2\), \(N\ge j\ge0\), a finite four-dimensional periodic cubical volume of physical side lengths compatible with both grids, and microscopic spacings \(\eta_N=L^{-N}\), \(\eta_{N+1}=L^{-(N+1)}\). Pick a geometric square \(\gamma\) with side \(a=L^j\eta_N=L^{j+1}\eta_{N+1}\), strictly inside a chosen physical block. Its oriented perimeter has \(4L^j\) microscopic edges in depth-\(N\) coordinates and \(4L^{j+1}\) microscopic edges in depth-\(N+1\) coordinates (ignore degenerate winding geometries). This is a *single physical loop*, not an equality of microscopic edge sets.

Let \(E_N,V_N\) be edges and vertices, \(X_N=SU(2)^{E_N}\) with product Haar measure \(H_N\), gauge group \(\mathcal G_N=SU(2)^{V_N}\), and finite-volume Wilson density
\[
 d\mu_N(U)=Z_N^{-1}e^{-S_{W,N}(U)}\,dH_N(U),
 \qquad 0<Z_N=\int e^{-S_{W,N}}dH_N<\infty.
\]
The action may use a cutoff-dependent but finite positive bare coupling; the only facts used are its finite real continuous value, gauge invariance and strictly positive density on the compact finite configuration space. Define \(\mu_{N+1}\) analogously. No equality of couplings/actions is assumed.

For each cutoff, let \(\gamma_N,\gamma_{N+1}\) be the edge-perimeter approximations of the **same** \(\gamma\). Define
\[
 w_N(U)=\tfrac12\operatorname{ReTr}\!\left(\overrightarrow{\prod_{e\in\gamma_N}}U_e^{\pm1}\right),
 \quad
 w_{N+1}(U')=\tfrac12\operatorname{ReTr}\!\left(\overrightarrow{\prod_{e\in\gamma_{N+1}}}(U'_e)^{\pm1}\right).
\]
The target is \(E_{\rm obs}=[-1,1]\). Both \(w_i:X_i\to E_{\rm obs}\) are continuous, Borel and gauge invariant: the path holonomy transforms by conjugation at its basepoint, and trace is invariant. Their exact normalized observable laws are \(\lambda_i=(w_i)_*\mu_i\).

Thus the cospan
\[
 (X_N,\mu_N)\xrightarrow{w_N}E_{\rm obs}
 \xleftarrow{w_{N+1}}(X_{N+1},\mu_{N+1})
\]
is an explicit lawful **common gauge-invariant observable carrier** at one physical block. For every bounded Borel \(f:[-1,1]\to\mathbb R\),
\[
 \Delta_{N,\gamma}(f)
 =\int f(w_{N+1})\,d\mu_{N+1}-\int f(w_N)\,d\mu_N
 =\int f\,d(\lambda_{N+1}-\lambda_N).
\]
This is a well-defined exact comparison of **normalized laws**, *not* an estimate on its magnitude, not a projective pushforward under Bałaban \(M\), and not an identification with CMP109 one-step beta. Its importance is that it needs **no unproved global gauge section or fluctuation covariance identification**. For higher nontrivial compact simple groups use a normalized real character in place of the SU(2) trace, with a properly specified bounded range; the present concrete test makes no group-uniform claim.

## 2. Exact shared-data coupling criterion (independent abstract theorem)

Suppose, additionally, two actual cutoff systems are furnished with **measurable maps on the same standard Borel target** \(D_i:X_i\to E_{\rm data}\), containing the source-required domain/layer geometry and gauge-compatible prescribed shared data in a specified common chart or intrinsic equivalence class. Put \(\rho_i=(D_i)_*\mu_i\), and define \(\|\rho_0-\rho_1\|_{\rm TV}=\sup_A|\rho_0(A)-\rho_1(A)|\).

**Lemma (complete coupling criterion).** For standard Borel \(X_i,E_{\rm data}\),
\[
 \sup_{\pi\in\Pi(\mu_0,\mu_1)}
 \pi\{(x,y):D_0(x)=D_1(y)\}
 =1-\|\rho_0-\rho_1\|_{\rm TV}.
\]
In particular there exists a coupling with *almost-sure exact data equality* if and only if \(\rho_0=\rho_1\).

**Proof.** Every coupling of \(\mu_i\) induces a coupling of \(\rho_i\); the diagonal match mass of any such coupling is at most the mass of the common part \(\rho_0\wedge\rho_1\), namely \(1-\|\rho_0-\rho_1\|_{\rm TV}\). By maximal coupling of \(\rho_0,\rho_1\), attain this diagonal mass. Standard-Borel disintegrations \(\mu_i(dx\mid D_i=e_i)\) lift the paired data to a coupling of the original fields with the same match probability. Exact match almost surely is equivalent to zero TV. □

**Jurisdiction:** The lemma is abstract/proved internally, not a statement that the native Bałaban determining-data maps \(D_i\) have been constructed, or that they are gauge-chart compatible. Equality of *gauge-invariant observables* \(w_N=w_{N+1}\) is weaker than equality of the entire source prescribed field \(V\). An arbitrary choice of an \(E_{\rm data}\) convenient for coupling does not establish draft §9.3 admissibility.

## 3. Exact finite-Wilson obstruction to full-law, small-field-only support

Fix any actual plaquette \(p\) in one SU(2) lattice. For a threshold \(0<\varepsilon<2\) in operator norm, let
\[
 G_{\varepsilon,p}=\{U:\|I-U(\partial p)\|<\varepsilon\}.
\]
Its complement contains a nonempty open set: take one link on \(\partial p\) near \(-I\), the other links near \(I\), so the plaquette holonomy is near \(-I\) with distance near 2. A nonempty open set has positive product-Haar measure; the finite Wilson density is strictly positive and continuous. Consequently,
\[
 \boxed{\mu_N(G_{\varepsilon,p}^c)>0.}
\]
Any *more restrictive* all-plaquette small-field event \(G_N\subseteq G_{\varepsilon,p}\) likewise has \(\mu_N(G_N^c)>0\). Therefore **no coupling with the FULL finite-volume Wilson \(\mu_N,\mu_{N+1}\) as marginals can be supported exclusively on a pair of such proper small-field sectors**: its marginal would incorrectly assign zero mass to a positive-probability complement.

This is a precise source-shaped obstruction to the shortcut “prove paired small-field theorem => global normalized Wilson law comparison.” It does **not** say that the source's determining data \(V\) literally equal microscopic plaquette fields, or that Bałaban's large-field treatment cannot control this mass; nor does it quantify the large-field probability uniformly in \(N\), volume or coupling.

## 4. Normalized good-sector coupling inequality and exact residual

Let \(G_i\subseteq X_i\) have \(0<\mu_i(G_i)\le1\), \(b_i=\mu_i(G_i^c)\), and \(\mu_i^G=\mu_i(\cdot\mid G_i)\), explicitly **normalized**. Let \(F_i:X_i\to\mathbb R\) be bounded Borel observables, \(|F_i|\le M\), and \(\pi^G\in\Pi(\mu_0^G,\mu_1^G)\) any coupling with correct conditional marginals. Direct conditioning and coupling give the exact general estimate
\[
 \left|\mathbb E_{\mu_1}F_1-\mathbb E_{\mu_0}F_0\right|
 \le\int|F_1(y)-F_0(x)|\,d\pi^G(x,y)
 +2M(b_0+b_1). \tag{R106.1}
\]
Indeed \(|\mathbb E_{\mu_i}F_i-\mathbb E_{\mu_i^G}F_i|\le 2Mb_i\); couple the conditioned expectations, then use the triangle inequality.

If the source data maps \(D_i\) are lawful on \(G_i\) and on *data-matched* paired fibers a **verified** source-compatible response gives \(|F_1(y)-F_0(x)|\le a_N\), a maximal data coupling lifted as in §2 has mismatch probability \(t_N=\|(D_0)_*\mu_0^G-(D_1)_*\mu_1^G\|_{\rm TV}\). It follows that
\[
 \left|\mathbb E_{\mu_1}F_1-\mathbb E_{\mu_0}F_0\right|
 \le a_N+2M t_N+2M(b_0+b_1). \tag{R106.2}
\]
R106.2 is a **conditional consumer**: it requires an actual common data carrier, legitimate conditional coupling on eligible fibers, matched-fiber observable bound and correct physical observable comparison. No numerical or summable bound on \(a_N,t_N,b_i\) is present.

**Negative control:** Setting \(a_N=0\) because pointwise minimizers or covariance roots are paired, without proving a bound for the **integrated observable \(F_i\)**, is invalid. Likewise \(t_N\) is unknown from physical-scale alignment, and strictly positive \(b_i\) need not decay with \(N\).

## 5. Refute-first evidence ledger

| Interface | R106 result | Native consequence |
|---|---|---|
| Same physical square at \((N,j)\) and \((N+1,j+1)\) | **EXPLICIT FINITE-WILSON TEST** using \(4L^j\) and \(4L^{j+1}\) edge perimeters | Gauge-invariant \(E_{\rm obs}=[-1,1]\) cospan exists; NOT Bałaban's \(M^j\) |
| Normalized law comparison for \(f\circ w_i\) | **WELL-TYPED EXACT IDENTITY** | Magnitude/summability OPEN |
| Exact shared source-data coupling | **ABSTRACT NECESSARY AND SUFFICIENT TV CRITERION** | Actual \(D_i,\rho_i\), nested \(\Omega,V\) OPEN |
| Full positive finite-Wilson law wholly inside proper small-field event | **REFUTED** | Must pay or separately integrate large-field complement |
| Good-sector bound R106.1 | **ABSTRACT PROVED** | Useful with valid conditional marginals and \(b_i\) estimates |
| Data-matched response R106.2 | **CONDITIONAL PROVED** | Requires source-compatible \(a_N\), \(t_N\) and complement mass |
| Draft YM4 minimizer / covariance-root / exact shell and fine propagators | **UNVERIFIED** | No imported theorem |
| CMP102b original images, CMP109 Eq(0.29),(5.37),(5.42) | **OPEN SOURCE HOLDS** | No formula promotion |
| Full RG-beta, inherited E, OS and positive gap | **OPEN** | No existence or gap claim |

## 6. Exact stopping determination and YM-R107 frontier

**R106 is complete only in its stated jurisdiction:** one explicit finite-Wilson physical-square gauge-invariant observable cospan has been constructed; the normalized-law matching criterion and good-sector + complement accounting are self-contained; a coupling of full positive Wilson laws supported only on proper small-field sectors is impossible. This satisfies the *observable-cospan/necessary-obstruction* alternative to R105's next test, but does **not** certify native Bałaban RG-law closeness or the external paired-variational theorem's input membership.

**YM-R107 (unconsumed): source-native determination map and first quantitative defect.** Recover at one precise CMP98 averaging / CMP102b variational / CMP109–CMP116 RG block the actual prescribed data \(D_N,D_{N+1}\), their gauge-chart and nested-domain rules, and the induced normalized conditional distributions. Compare the **true** \(M\)-image with the Wilson-loop test cospan; do not substitute path-product holonomy for \(M\). Prove a source-admissible matched-fiber \(a_N\), a quantitative \(t_N\), or a genuinely source-specific obstruction. Separately obtain sufficient large-field \(b_N\) bounds for a summable physical-observable defect, preserving normalizations, histories, root factors, and the original-page image holds. Exact global coupling equality is neither assumed nor required.

Highest prior Bałaban reference number remains [92]; no new numbered bibliography entry. No continuum Yang–Mills construction, OS axioms or positive physical mass gap is established.
