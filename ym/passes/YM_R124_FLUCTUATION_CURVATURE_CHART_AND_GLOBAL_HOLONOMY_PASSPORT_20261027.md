# YM-R124 — source fluctuation curvature chart and global winding-holonomy custody

**Repository:** monocap-tech/yangmills. **Date:** 2026-10-27. **Previous authoritative checkpoint:** [YM-R123](../checkpoints/YM_HEAD_R123_20261027.json), main e88cecf7e4a1e76b7f71868199d7848619401eb2. **Disposition:** completed as (i) exact SU2 source-typed curvature transfer conditional on a quantitative H_k(B') bound, (ii) global flat-holonomy noninjectivity witness, (iii) exact flat-field source M holonomy retention, and (iv) winding-loop error accumulation from R122. **UNPROVED_RESEARCH_PROGRAM**; YM-R125 is the only unconsumed next cursor.

## 0. Original-paper evidence boundary

Source: T. Bałaban, CMP 109 (1987), 249–301, DOI https://doi.org/10.1007/BF01215223, original printed [54-page PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). Original page screenshots inspected: **PDF index 2 / printed p.251**, torus and half-shifted periodic lattice (0.1); **3–4 / pp.252–253**, shortest-path averaging (0.3),(0.4); **16 / p.265**, source (2.1)–(2.3), gauge change and Landau field \(\exp(i\eta H_k(B'))U_{k+1}\); **17 / p.266**, (2.4)–(2.9), \(\chi_k\) on selected B' bonds; **18 / p.267**, source h,D(B), projected constraints and covariance precursor. CMP109 explicitly says H_k(B') is regular and **of the same order as B'**, but sends its PROPERTIES to Sect. G of its reference [15]. The printed p.299 bibliography identifies [15] as Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP **102**, 277–309 (1985), DOI https://doi.org/10.1007/BF01229381. Its quantitative source operator norm on all source halo bonds was not extracted or visually verified in this pass. [R124 receipt](../source_receipts/YM_R124_FLUCTUATION_GLOBAL_HOLONOMY_SOURCE_RECEIPT_20261027.md).

Existing completed R106 creates one aligned finite plaquette Wilson-observable cospan but explicitly **excludes winding geometries**; [R106](YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md). [R122](YM_R122_NONLINEAR_COARSE_LINK_CURVATURE_AND_TWO_STAGE_GATE_20261027.md) proves a nonlinear source coarse-link curvature estimate on contractible admissible plaquette ribbons, and [R123](YM_R123_SOURCE_REGULARITY_TO_NONLINEAR_M_ENTRY_AND_FLUCTUATION_SEAM_20261027.md) separates minimizing-background regularity from \(\chi_k\)'s selected bond cutoff. Do NOT rewrite R106 or R122 retroactively.

## 1. Actual source fluctuation identity, gauge-quotient simplification

The source p.265 states that after changing the fluctuation from axial to Landau gauge,
\[
 \boxed{U_{\rm fluctuated}^{\,u}(b)
 =\exp(i\eta H_k(B')(b))U_{\rm bg}(b),\quad U_{\rm bg}=U_{k+1}.}\tag{R124.1}
\]
Here \(\eta\) is the source fine spacing at this transformation and H is Hermitian (or equivalently choose skew-Hermitian convention), **not** automatically the regularity exponent \(\eta_k=L^{-k}\) without a source chart. The source also asserts H is analytic/regular and of the same order as B', with quantitative estimates in CMP102 [15]. The source p.266 (2.9) only monitors \(B'(b)\) on a selected independent subset excluding b0(c), with threshold \(\theta_k=\varepsilon_1\) or \(g_k\varepsilon_1/\gamma_k\). The omitted b0(c) bond is constrained/nonlinearly solved; the source says O(ε1), NOT equal to zero. After linearization p.267, \(B'=B-h\widetilde D(B)\), \(B=g_kB_{\mathrm{rescaled}}\), and \(\widetilde D(B)\) begins at quadratic order. These maps are different stages and must not have their scalar factors silently conflated.

**Exact gauge-invariant lemma R124.2.** Let on a common finite physical fine graph \(\widetilde U(b)=F(b)U_{\rm bg}(b)\) with all \(F(b)\in SU(2)\), and \(\sup_b\|F(b)-I\|_{\rm op}\le d\) on each edge in a selected plaquette/halo. A plaquette product changes by at most 4d under four unitary factor replacements, including reversed edges. With \(\eta_{\rm bg}=\sup_p\|U_{\rm bg}(\partial p)-I\|\),
\[
 \boxed{\eta_{\rm physical}\le\eta_{\rm bg}+4d.}\tag{R124.2}
\]
A local gauge transformation conjugates each based closed plaquette holonomy and does NOT change its unitary operator norm distance to identity. Thus **there is no need to bound the intermediate axial-to-Landau gauge transformation itself for this curvature comparison.** The appropriate missing SOURCE input is a quantitative norm estimate on **H_k(B') on all needed physical fine bonds**, in a source-supported chart and including the constrained b0(c).

If the source can supply \(\sup_{\rm halo}\|H_k(B')\|\le C_{H,k,\Omega}\theta_k\) under its cutoff and regularity hypotheses, then for real SU2 and \(\exp(i\eta H)\) unitary,
\[
 d\le\eta C_{H,k,\Omega}\theta_k,\quad
 \boxed{\eta_{\rm physical}\le
  \varepsilon_0\eta_k^2+4\eta C_{H,k,\Omega}\theta_k.}\tag{R124.3}
\]
For each eligible halo, R122 actual nonlinear M enters its log chart when
\[
 \boxed{666\left(\varepsilon_0\eta_k^2+
 4\eta C_{H,k,\Omega}\theta_k\right)<1.}\tag{R124.4}
\]
This is a **precise SOURCE NORM ENTRY GATE**, not a derived actual Bałaban constant. CMP109 printed p.265 only says “same order”, no numeric \(C_H\), no full regional halo coverage, no demonstrated two-cutoff uniform bound. A paper making either claim must first recover CMP102 Sect. G [15] and verify its conditions, and the source B' constraints/Hk range.

The source's background regularity \(\eta_{\rm bg}\le\varepsilon_0\eta_k^2\) is itself conditional on \(\chi_k\)-supported regular minimizers as shown in R123. A B' bound alone does not imply it.

## 2. Flat periodic SU2 family: curvature does NOT identify gauge orbit

On a periodic d=4 lattice with \(N\) fine links around e1, define
\[
 U_1(b)=D(\theta/N)=\operatorname{diag}(e^{i\theta/N},e^{-i\theta/N})
\]
on every positively oriented e1 edge, with all other edges identity. All plaquettes are I because link matrices commute and are constant. Therefore \(\eta_{\rm plaquette}=0\) for every \(\theta\), but the positively oriented winding cycle \(\gamma_1\) has
\[
 \boxed{W_{\theta}(\gamma_1)=D(\theta),\quad
 w_{\gamma_1}(U)=\tfrac12{\rm ReTr}\,W_\theta=\cos\theta.}\tag{R124.5}
\]
For \(\theta=\pi/3\), the Wilson trace is 1/2 versus 1 at trivial connection, even though both have \(\eta=0\). Periodic gauge transformations conjugate W at its basepoint, hence cannot equate different traces. **Flat holonomy classes are not necessarily DISCONNECTED topological sectors**; this SU2 family varies continuously with \(\theta\). The flat family can satisfy arbitrarily stringent LOCAL contour bounds by making \(N\) sufficiently large (e.g. N divisible by L), but source eligibility as an actual prescribed minimizing background/χk or Ω-region remains an independent test.

**Linearized source warning:** on a periodic torus, constant Cartan-valued 1-forms are closed but not derivatives of periodic site-gauge parameters, yielding \(\ker d\supsetneq\mathrm{im}\,d\). Curvature-only quadratic coercivity cannot control them without additional determining data/gauge constraints. This does NOT refute the actual CMP99 reduced precision; source coarse-average Q could remove them.

[Exact executable finite-lattice witness](../computations/YM_R124_FLAT_WINDING_AND_CURVATURE_TRANSFER_20261027.py) checks plaquettes, winding trace, M-flat straight coarse links for compatible L,N, and simple R122 winding-error telescoping. No new physics assertion is inferred from the code.

## 3. Source M PRESERVES the global holonomy on eligible flat fields

**Theorem R124.6 — exact flat-sector retention.** Suppose all CMP109 (0.4) source loops \(X_{x,\Gamma,\Gamma'}=H_{x,\Gamma,\Gamma'}(U)U(c)^{-1}\) bound contractible plaquette ribbons in an admissible periodic source region (the R122 source halo assumption). If every relevant plaquette is flat, each ribbon has holonomy I, hence \(X=I\). The actual NONLINEAR CMP109 map satisfies
\[
 \boxed{M(U,c)=U(c_{\rm straight\ fine})\quad\text{for every source coarse bond}.}\tag{R124.6}
\]
If a periodic winding cycle on the COARSE graph lifts to the same physical winding cycle of straight fine paths, multiplication of all coarse links gives
\[
 \boxed{W_{\gamma}(M(U))=W_{\gamma_{\rm fine}}(U)}\tag{R124.7}
\]
as matrices in the corresponding basepoint frame, and therefore identical gauge-invariant Wilson traces. For the explicit \(D(\theta/N)\) family with \(L\mid N\), each coarse e1 link becomes \(D(L\theta/N)\), and \(N/L\) of them multiply to \(D(\theta)\). Therefore **the source coarse field V=M(U) carries the winding Wilson information in this EXACT flat family.** Local curvature-only summaries would discard it; the correct full V does not.

This positive result is restricted to flat eligible source ribbons and aligned winding loops. It does NOT prove that the source paired histories with prescribed V and Ω actually exist, or that their normalized laws agree, or that every nonflat global mode is controlled.

## 4. Quantitative winding-loop retention for near-flat eligible fields

Assume the source real SU2 field U obeys the R122 halo/chart conditions for EVERY coarse link of a selected noncontractible winding cycle \(\gamma\), giving the UNIFORM local bound
\[
 \|M(U,c)-U(c_{\rm fine\ straight})\|\le\delta
 :=\frac{31878}{169}\frac{\eta}{1-666\eta},\quad 666\eta<1.\tag{R124.8}
\]
If the coarse cycle has n bonds, and their straight fine lifts concatenate to the same winding \(\gamma_{\rm fine}\), sequentially replacing one unitary factor at a time gives
\[
 \boxed{\|W_\gamma(M(U))-W_{\gamma_{\rm fine}}(U)\|
 \le\min\{2,n\delta\},\qquad
 |w_\gamma(M(U))-w_{\gamma_{\rm fine}}(U)|
 \le\min\{2,n\delta\}.}\tag{R124.9}
\]
The scalar Wilson values individually lie in [-1,1]. This is a **REAL source one-step geometric-to-global bound** for a physical winding loop, CONDITIONAL ON FULL CYCLE COVERAGE and the local chart, not a normalized measure comparison.

If additionally \(\eta\le\varepsilon_0h^2\), the corresponding physical period is \(\ell\), and each coarse link has length Lh so \(n=\ell/(Lh)\) is an integer, then
\[
 \boxed{n\delta\le
 \frac{\ell}{Lh}\frac{(31878/169)\varepsilon_0h^2}{1-666\varepsilon_0h^2}
 =\frac{(31878/169)\varepsilon_0\ell\,h}{L(1-666\varepsilon_0h^2)}.}\tag{R124.10}
\]
This tends to zero at fixed physical period \(\ell\), fixed L=13, fixed \(\varepsilon_0\) when h→0, **provided the same local curvature bound and complete winding-cycle halos are uniform at each step and source link identification holds**. The one-step statement does NOT compare independently normalized two-cutoff histories; the physical h and source \(\eta_k\) scaling must actually be matched before using (R124.10) inside CMP109's own iterative notation.

For two *actual independent* UV histories \(U_N,U_{N+1}\), with a verified common coarse determining field V on aligned winding cycles and one-step R122 errors n_Nδ_N and n_{N+1}δ_{N+1}, triangle inequality gives at most their SUM for the difference of their microscopic winding Wilson values. **Those two histories and their same-V coupling/conditional laws are NOT constructed.** Their winding-observable laws could differ even if the individual geometric tests succeed. This extends the *kind* of gauge-invariant observable cospan in R106 from a contractible square to winding cycles, but does not inherit a source coupling or uniform total-variation estimate.

## 5. Obligation graph / source stop

| Obligation | R124 status |
|---|---|
| CMP109 actual Landau link \(e^{i\eta H_k(B')}U_{\rm bg}\) | ORIGINAL PRINTED p.265 VERIFIED |
| Gauge invariance of plaquette norm and 4-link difference | EXACT; avoids intermediate gauge-move norm |
| Uniform source \(\|H_k(B')\|\le C_H\theta_k\) on ALL halo links | OPEN: CMP102 Sect G source constant/domain, b0 and Ω |
| Physical R122 entry after fluctuation | EXACT CONDITIONAL R124.4 |
| Periodic flat local curvature non-injectivity | EXACT R124.5 |
| CMP109 M retention of winding holonomy on flat eligible source | EXACT R124.6–R124.7 |
| Nonflat winding-loop error from R122 | EXACT CONDITIONAL R124.9 |
| Continuum-style \(O(h)\) bound at fixed period | CONDITIONAL on physical h source correspondence/halo R124.10 |
| Actual source coarse V, paired Ω, winding-sector coupling and normalized laws | OPEN |
| CMP99 later reduced Gaussian precision, harmonic-mode elimination | OPEN |
| Yang–Mills existence, OS reconstruction, positive physical gap | UNPROVED |

**YM-R125 — sole unconsumed successor:** source-recover CMP102 (1985) Sect. G, specifically bounds and domain of H_k(B'), including source Lemma/Proposition 9 and its exponential decay/regularity, and match their norms to the monitored source \(\chi_k\) bond cutoff plus special b0 constraint on complete R122 halos. Separately verify if the actual fixed coarse V and Ω prescribed layers can transport winding Wilson observables in two independently truncated UV histories; use R124.9 as a candidate conditional observable error, not an invented probability-law estimate. CMP99 later (3.157)–(3.158) source precision and full Gaussian normalizers remain open. No new independent branch and no physical mass gap claim.

Bibliography highest project [92] unchanged, source receipt append-only.
