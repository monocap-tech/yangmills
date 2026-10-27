# YM-R125 — CMP102 H_k derivative-kernel source hold and conditional winding observable law

**Date:** 2026-10-27. **Repository:** monocap-tech/yangmills. **Previous main:** b3c3483cba9a9cd81029e5a17fb7ea58a6dc0ea5; [YM-R124](../checkpoints/YM_HEAD_R124_20261027.json). **Completed:** identify original CMP102 quantitative kernel source target without claiming its numerical content, prove a kernel-to-uniform SU2 field estimate with exact row sum, and prove a conditional TWO-INDEPENDENT-CUTOFF *winding observable* Wasserstein/expectation bound with an explicit TV negative control. **Open:** actual CMP102 original Proposition 9/(190) images and chart constants, physical source normalized laws/cutoff exits, covariance, full Yang–Mills. **Next:** YM-R126 unconsumed. **Status:** UNPROVED_RESEARCH_PROGRAM.

## 0. Primary and secondary evidence boundary

The actual original source formula in printed Bałaban CMP109 p.265, after (2.3), says the fluctuation in Landau gauge is of the form exp(i eta H_k(B')) U_(k+1), with regular H_k of the same order as B', and refers its PROPERTIES to Sect. G [15]. Printed p.266 (2.9) monitors selected independent B' bonds but excludes b0(c); p.267 source h,D(B) eliminates the constrained bonds. CMP109 printed p.271 (3.8)–(3.9) invokes **Proposition 9, (190) [15]** to bound derivatives with exponential decay. These facts were checked through the source-original-paper Git OCR (blob f1aec083a3a6470c67a2c1205ca740c2583fe37a, lines 853–864,895–961,1128–1142), and earlier original CMP109 printed-image receipts in YM-R124. Do not label OCR itself image verification in this pass.

CMP109 ref [15] identifies Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP 102(2), 277–309 (1985), DOI https://doi.org/10.1007/BF01229381. Springer publisher preview confirms authorship and metadata but does NOT expose the paper's mathematical equations without subscription. The previously located Michigan deepblue PDF URL did not open through the web source. An independent Japanese-language SOURCE COMMENTARY (Rikai, 2026-10-12) maps CMP102 Sect. G (170)–(181) to analyticity and original Proposition 9 / (182)–(190) to exponential decay of functional derivatives. This commentary is **secondary and cannot certify the precise original source kernel norms, graph metric, constants or boundary conditions**. [Full receipt](../source_receipts/YM_R125_CMP102_HK_AND_WINDING_LAW_SOURCE_RECEIPT_20261027.md). In particular we DO NOT assert a value of A, kappa, an unweighted volume-independent bound, or applicability to CMP109 B' from this source alone.

## 1. Source-to-usable-norm passport, quantified but conditional

The missing native object is the derivative of the physical fine-link field H_k with respect to the **independent** source B' coordinates after the special b0(c) elimination, on every original fine bond in a required regional halo. At a real SU2 chart, suppose H(0)=0, the straight line tB' (0<=t<=1) stays in a source eligible analytic chart, and the kernel obeys for **all t** and every source physical output bond b
\[
 \|D_{B'_{b'}}H_b(tB')\|_{\rm op}
 \le A\,e^{-\kappa d_1(b,b')},\qquad \kappa>0,\tag{R125.1}
\]
where b' ranges over independent source B' bonds; the distance d1 is the ordinary l1 distance between bond lattice sites and a fixed compatible orientation class. THIS IS A SPECIFIED ENTRY HYPOTHESIS, NOT A RECOVERED CMP102 THEOREM. Assume each lattice site supports at most m independent bond variables (m<=4 for one positive-axis orientation per site), and \(\|B'_{b'}\|\le\theta_k\).

Integrate dH_b(tB')/dt along the line and sum the kernel rows. Since
\[
 \sum_{z\in\mathbb Z^4}e^{-\kappa\|z\|_1}
 =\left(1+2\sum_{n=1}^{\infty}e^{-\kappa n}\right)^4
 =\left(\frac{1+e^{-\kappa}}{1-e^{-\kappa}}\right)^4,
\]
we get the source-passport conditional estimate
\[
 \boxed{\|H(B')\|_\infty
 \le m A\,\coth(\kappa/2)^4\,\theta_k,\qquad
 C_H=mA\,\coth(\kappa/2)^4.}\tag{R125.2}
\]
This is **uniform in lattice volume** for ordinary lattice-graph distances and uniform A,kappa; it is NOT automatically uniform in cutoff k, since the source's actual rescaled distance, weighted norms, collar geometry, eta factor, A_k and kappa_k must be verified. If the kernel includes winding image terms, no simple single-distance bound may hold without an additional sum. Excluded b0(c) variables must be already accounted for by the **actual derivative** of the solved map, not set to zero or counted twice. The four per-site factor assumes 4D and the source coordinate convention.

For the illustrative exact value e^{-kappa}=1/2 and m=4, the row sum is 81 and \(C_H=324A\). This integer is an **example arithmetic test**, not a source constant. The [executable certificate](../computations/YM_R125_KERNEL_ROW_SUM_AND_WINDING_LAW_20261027.py) confirms it with exact rational arithmetic and checks finite truncation below 81.

Combining R125.2 with the proven R124 physical-link/plaquette transfer would make R122's nonlinear CMP109 M chart applicable to the fluctuated original real SU2 field IF
\[
 \boxed{666\left(\varepsilon_0\eta_k^2+
 4\eta\,mA\coth(\kappa/2)^4\theta_k\right)<1,}\tag{R125.3}
\]
with complete source Ω/Dirichlet halo support and consistent physical eta vs source eta_k. This inequality is the exact missing carrier entry condition. **It is not yet a source-verified small-field estimate.** Source analogues in CMP102 may contain polynomial prefactors, different distances or stronger derivative norms; recover original (190) before transferring.

## 2. Same prescribed coarse V can supply a common winding observable center

Let two genuinely DIFFERENT UV cutoffs i=0,1 have finite normalized conditional probability laws \(\mu_i(\,\cdot\mid V,\Omega)\) on original fine SU2 configurations and actual source-compatible multiscale histories \(U_{i,0},\ldots,U_{i,k_i}\) with each deterministic coarse link related by source M and final/coarse target \(U_{i,k_i}=V\) on the **SAME** coarse graph and prescribed Ω. These histories, normalized measures, and a common \(V,\Omega\) are **hypotheses, not built in this pass**.

Choose one actual noncontractible coarse winding loop γ(V) and fine representatives γ_i at the two UV scales. Define the scalar gauge-invariant Wilson value \(X_i(U_i)=\frac12\mathrm{ReTr}\,U_i(\gamma_i)\in[-1,1]\) and common target \(v=\frac12\mathrm{ReTr}\,V(\gamma)\).

Assume a measurable GOOD event G_i under each normalized law on which every required source ribbon/collar and logarithm chart is admissible and, for each stage j, the actual M(U) versus its fine straight lift error is bounded by \(\delta_{ij}\) uniformly over the n_{ij} coarse winding edges. The path lifts for consecutive stages must concatenate in the **same homology/winding class**. The unitary telescoping triangle inequality repeated over scales gives on G_i
\[
 \boxed{|X_i-v|\le e_i,\qquad
 e_i:=\min\{2,\sum_{j=0}^{k_i-1}n_{ij}\delta_{ij}\}.}\tag{R125.4}
\]
The abstract path count and resulting delta are source-typed only if each actual configuration satisfies R122 and each M is the true source map, not an artificial geometric lift. The R121 historical affine transport cocycle needs separate treatment if changing source corner/center frames across histories.

Let \(q_i=\mu_i(G_i^\complement\mid V,\Omega)\). Since X_i and v are in [-1,1], \(|X_i-v|\le2\) on bad events. Thus
\[
 \boxed{\mathbb E_{\mu_i}|X_i-v|\le e_i+2q_i.}\tag{R125.5}
\]
This estimate does **not** require estimating or equating source partition functions ONCE the two conditional laws exist as normalized probability measures. But it CANNOT establish normalization or a bound on q_i.

## 3. A conditional two-UV WASSERSTEIN/EXPECTATION comparison, no TV transfer

For the pushforward laws \(\nu_i=(X_i)_\#\mu_i(\cdot\mid V,\Omega)\) on common scalar [-1,1], take the product coupling (independent draws) or any coupling with these marginals. The triangle inequality through v yields
\[
 \mathbb E|X_0-X_1|
 \le \mathbb E|X_0-v|+\mathbb E|X_1-v|
 \le e_0+e_1+2(q_0+q_1).
\]
Since the 1-Wasserstein distance W1 is the infimum of such costs and any 1-Lipschitz test function f obeys |f(x)-f(y)|<=|x-y|,
\[
 \boxed{W_1(\nu_0,\nu_1)\le
 \min\{2,e_0+e_1+2(q_0+q_1)\},}\tag{R125.6}
\]
\[
 \boxed{|\mathbb E_{\mu_0}f(X_0)-\mathbb E_{\mu_1}f(X_1)|
 \le e_0+e_1+2(q_0+q_1).}\tag{R125.7}
\]
If q_i=0 this is a **bound on full normalized laws of one chosen physical winding observable** with no inter-UV coupling construction needed beyond existence of the marginals and common V. To use it as an actual native proof one still needs **source law existence, conditional disintegration, identical Ω/V, all-stage deterministic M histories, e_i→0, and q_i→0 uniformly**. None is furnished by CMP109 (2.12)–(2.13), R110, or this pass.

**Hard negative control: W1 does not imply TV.** Let v=0 and \(\nu_0=\delta_{-\epsilon}\), \(\nu_1=\delta_{+\epsilon}\), 0<epsilon<=1. Both are supported within epsilon of the prescribed common scalar v, W1=2epsilon→0, but total variation distance (supremum-event convention) is **1** for all epsilon>0. Thus no broad normalized total-variation or full-field-law result may be inferred from R125.6. The Dirac example is a general measure-theoretic counterexample, not a claim that those laws arise from Bałaban RG.

## 4. Source-specific stop / next obligation

| Carrier/claim | R125 status |
|---|---|
| CMP109 H_k(B') source link and reference to CMP102 Sect G | SOURCE PRINTED PREVIOUSLY / OCR RE-CHECKED |
| CMP102 Prop9 (190) precise derivative norm, constants, geometry | **UNRECOVERED original equation; SECONDARY CROSSWALK only** |
| Kernel-to-uniform original H_k norm | EXACT CONDITIONAL R125.2 |
| Real physical curvature/log chart entry | EXACT CONDITIONAL R125.3 |
| Flat source M retains winding | R124 proved for admissible flat source; retained |
| Multiscale winding microscopic-to-coarse target | EXACT CONDITIONAL R125.4 |
| Same prescribed Ω,V normalized scalar winding W1 law | EXACT CONDITIONAL R125.6, no source q/e estimates |
| Total variation from close winding observables | **REFUTED** by independent Dirac negative control |
| Actual two-UV probability, CMP99 reduced precision, E/determinants | OPEN |
| Full YM existence, OS, positive mass gap | UNPROVED |

**YM-R126 sole next cursor:** recover CMP102 original Sect G (170)–(190) actual derivative-kernel metrics and their dependence on scale, constrained b0, source Ω/collar; do not treat secondary exposition as original source. Identify source-supported cutoff exit q_i, normalized conditional law, and common coarse Ω,V alignment sufficient to instantiate R125.4–R125.7. CMP99 (3.157)–(3.158) reduced Gaussian precision remains separate. A source-specific FAILURE/NO-TRANSFER is a valid stop; do not repeatedly quote abstract positivity or upgrade W1 to TV. Bibliography historical highest [92] maintained.
