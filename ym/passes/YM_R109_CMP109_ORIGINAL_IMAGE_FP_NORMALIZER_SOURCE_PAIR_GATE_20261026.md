# YM-R109 — CMP109 printed-page Faddeev–Popov identity and native cutoff separation

**Date:** 2026-10-26. **Prior verified canonical:** [YM-R108](../checkpoints/YM_HEAD_R108_20261026.json), main at 031d92766eb90d30130114bf7bd0a59c3219f825. **Classification:** COMPLETE AS **PRIMARY PRINTED-PAGE IMAGE AUDIT**, EXACT LOCAL BASED-GAUGE NORMALIZER CALCULATION, AND R108 APPLICABILITY CORRECTION. **OPEN:** actual finite two-cutoff data laws, remaining physical/fluctuation cutoff, uniform mass/summability, OS/mass gap. **Next:** YM-R110 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. New evidence: source printed images were actually inspected

An accessible, 54-page *third-party-hosted scan of Bałaban's published printed paper* CMP109 was found at

https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf

The original **printed page image**, not merely its OCR text, was inspected at scan/PDF page indices 2,4,5,6,7,17,18,19 (zero-based), i.e. printed pp.251,253–256,266–268. The image corroborates the paper's authorship/journal and its displayed formulas. This is **visually checked primary printed-page content hosted by a third party**, not publisher-domain custody, not proof of the whole paper, and not an independent verification of all paper theorems. Exact formula-level findings and holds are listed in the [R109 receipt](../source_receipts/YM_R109_CMP109_PRINTED_IMAGE_SOURCE_RECEIPT_20261026.md). Previous attempts had found only third-party OCR; this source access is new.

Directly checked:
- p.251, (0.1) and surrounding text: in the considered CMP109 torus geometry **L is an odd integer greater than 11**, with lattice spacing epsilon=L^{-K}. R106's arbitrary L>=2 finite-Wilson example is a legitimate kinematic test, but not automatically an instantiation of CMP109 source geometry. L=13 is an admissible elementary scale choice, subject to all other source hypotheses.
- p.253 (0.4), p.254 (0.12): two displayed nonlinear gauge-field block-averaging options, with (0.12) explicitly an eligible alternative; neither is a raw path-product Wilson-loop map.
- pp.254–255 (0.13)–(0.17), especially (0.15)–(0.16): an **exact normalized based-gauge orbit identity** whose exponential and near-identity characteristic indicator appear together inside the SAME local integral.
- p.255 (0.17) and (0.19): delta constraints \(\prod_c\delta(\bar U(c)V(c)^{-1})\), characteristic factors \(\chi_0,\chi_k\), source gauge/exponential and background reference normalizers \(N_0,N_k\).
- p.256 (0.21): source variational constraint \(M^k(U)=V\); inherited \(E_k\) depends on preceding effective couplings (0.22)–(0.23).
- p.266 (2.9): a separate **fluctuation-coordinate** sharp cutoff \(\chi_k=\prod_{b\in T^{(k)}\setminus\{b_0(c):c\in T^{(k+1)}\}}\mathbf1_{\{|B'(b)|<\varepsilon_1\}}\), with a source-mentioned alternative coupling-dependent threshold.
- pp.267–268 (2.10), (2.12)–(2.13): constrained/linearized fluctuation integral, independent Gaussian coordinates, covariance, background-dependent Gaussian normalization and nonlinear interaction/characteristic factor.

**Important limit:** This pass has NOT inspected publisher original image for CMP98, CMP102b, or CMP109 (0.29),(5.37),(5.42), and has not selected an actual two-history \(M\) or established two-cutoff equality of prescribed \(V,\Omega\).

## 1. The critical R108 correction: the indicator of (0.16) is part of the identity

On the printed p.254, Eq. (0.15) reads, for each coarse center \(y\), internal site \(x\ne y\), and contour mean \(U(y,x)\), in the paper's normalized trace convention:
\[
 \frac1z\int_G du(x)\,
 \exp\!\left[-\frac1\alpha(1-\operatorname{Re}\operatorname{tr}(U(y,x)u(x)^{-1}))\right]\,
 {\bf1}_{\{|U(y,x)u(x)^{-1}-1|<\varepsilon_0\}}
\]
\[
 =\frac1z\int_G du(x)\,
 \exp\!\left[-\frac1\alpha(1-\operatorname{Re}\operatorname{tr}u(x))\right]\,
 {\bf1}_{\{|u(x)-1|<\varepsilon_0\}}
 =1.\tag{R109.1 / source 0.15}
\]
Here \(du\) is normalized compact-group Haar and \(z\) is **exactly** the final positive Haar integral. The step is right-translation and inversion invariance of Haar measure. Define
\[
 f_{\alpha,\varepsilon_0}(g)
 =e^{-\alpha^{-1}(1-\operatorname{Re}\operatorname{tr}g)}{\bf1}_{\{|g-1|<\varepsilon_0\}},
 \quad z_{\alpha,\varepsilon_0}=\int_G f_{\alpha,\varepsilon_0}(g)dg>0,\quad
 w_{\mathrm{FP}}(g)=f_{\alpha,\varepsilon_0}(g)/z_{\alpha,\varepsilon_0}.
\]
Then the **entire combined exponential-and-indicator** satisfies
\[
 \int_G w_{\mathrm{FP}}(U(y,x)u(x)^{-1})du(x)=1.\tag{R109.2}
\]
The positivity statement assumes \(\varepsilon_0>0\) and an admissible group norm/near-identity neighborhood; the identity is exact and independent of \(U(y,x)\).

Under the source based-gauge transformations \(u(y)=1\) on the coarse lattice, the contour variable transforms at each internal endpoint \(x\) by \(U(y,x)\mapsto U(y,x)u(x)^{-1}\). With one independent Haar variable at each internal fine site and the source's nonoverlapping blocks, Fubini gives
\[
 \int_H\prod_{y\in T^{(1)}}\prod_{x\in B(y),\,x\ne y}
 w_{\mathrm{FP}}(U^u(y,x))\,dh(u)=1.\tag{R109.3}
\]
**Exact local native computation:** the orbit-fiber mass of the **complete (0.15)–(0.16) factor is one**, even though its near-identity indicator is nontrivial pointwise. A product of \(z^{-1}\) factors carries only a field-independent scalar as long as the count and source parameters are fixed; reference scalar normalization cancels from properly normalized laws as shown in R108.5.

**R108 correction:** R108 was mathematically right that a *separately imposed* small-field cutoff can create an orbit-averaged selector \(\sigma<1\). But it left open whether the literal (0.16) characteristic function was such a separate cutoff. The printed (0.15) proves **it is not**: the displayed indicator is built into an exact normalized FP identity. It would be wrong to charge a \(1-c\) probability-law defect for this factor. R108 remains valid as an abstract lemma, not as a source-certified extra physical defect of (0.16).

## 2. Actual source kernel splits: delta constraint and genuine cutoff still must be distinguished

Printed p.255 (0.17) visibly uses a **source averaging** \(\bar U=M(U)\) and
\[
  \prod_{c\in T^{(1)}}\delta(\bar U(c)V(c)^{-1}),
\]
inside a Wilson-action-dependent integral; (0.19) repeats its form on the later lattice, with \(\chi_0\) or \(\chi_k\) and the gauge-fixing exponential. Both formulas normalize their action by evaluation of the integral at \(V=1\), not by declaring a normalized full probability law.

For a compact product-Haar target and a well-defined measurable source \(M:X\to Y\) on an **actually eligible** source domain, the pure graph kernel \(K_M(dV\mid U)=\delta_{M(U)}(dV)\) has
\[
 \kappa_M(U)=\int_Y K_M(dV\mid U)=1.
\]
This is the correct delta constraint component, **not a hypothetical raw Wilson-loop path map**. For a based-gauge-invariant test \(F(M(U))\) and an invariant input weight supported on the domain, the source gauge identity (R109.3) permits integrating the *combined* local FP factors away without changing the integral. This is a precise source-specific removal of one normalization obstruction.

**But:** The original small-field restriction stated before (0.13) (regular plaquettes, chart admissibility) and the compound \(\chi_0\) of (0.17) have NOT been decomposed in this audit into exactly invariant physical selection versus normalized FP factors. The true output full partition function/conditional law still depends on these restrictions and the action. Therefore \(\kappa_M=1\) for the source graph constraint and \(\kappa_{\mathrm{FP}}=1\) on the based orbit do **not** together imply that the entire cutoff RG kernel is Markov on the original full Wilson law.

At a later step, the visibly separate Eq. (2.9) characteristic cutoff on the independent gauge-fixed variables \(B'(b)\) is a genuine fluctuation restriction. It is not the indicator in (0.15), and it is not discharged by Eq. (0.15)'s normalized orbit identity. Its changed coordinate chart \(B'\), eliminated \(b_0(c)\), boundary and coupling parameters must be compared in the actual two-cutoff construction. The covariance and interaction/normalization terms in (2.12)–(2.13) also remain distinct.

## 3. Concrete first-block source passport

For a legal scale choice such as \(L=13\) and fixed compact semisimple \(G\), on one coarse block centered at y:
1. The source \(M(U,c)\) is a nonlinear parallel-transport/logarithmic average of the (0.4) or (0.12) family, not R106's physical-loop trace. The source permits both alternatives; choose/verify the one consumed by the specific RG stage before matching histories.
2. The residual gauge group at the step consists of functions \(u\) on fine vertices with \(u(y)=1\) at coarse vertices. The \((0.15)\) local orbit factor has known exact \(\kappa_{\mathrm{FP}}=1\), with no unidentified field-dependent z.
3. The product \(\delta(M(U,c)V(c)^{-1})\) is a proper source graph constraint (on its admissible domain) whose compact Haar integral is one; this does not validate globally defining M outside its complex/log neighbourhood.
4. The source's \(\chi_0\) or \(\chi_k\) includes sector/chart/fluctuation restrictions not **all** identified with normalized orbit gauge fixing, and (2.9) shows an explicit independent fluctuation coordinate cutoff. The sector probability, normalization, and their difference between two actual cutoff histories are not bounded.
5. Both histories still need admissible, paired \(\Omega\) and prescribed V, correct gauge/covariance carriers, and the inherited coupling/source E. Nothing in the one-block FP identity constructs the required nested pair.

## 4. Refute-first verdict and next cursor

| Obligation | R109 outcome |
|---|---|
| CMP109 printed Eq. (0.4),(0.12),(0.15)–(0.17),(0.19),(0.21),(2.9),(2.12)–(2.13) | PRINTED-PAGE IMAGE INSPECTED (third-party scan) |
| CMP109 p.251 L odd >11 | IMAGE-VERIFIED source geometry |
| FP local exponential *and indicator* in (0.15) | SAME EXACT ORBIT IDENTITY; local Haar mass =1 |
| Treat literal (0.16) indicator as independently physically truncating | **INVALID**; explicit source correction to R108 application |
| Delta source averaging constraint fiber mass | =1 **where source M is a lawful graph and group Haar normalized** |
| Entire source \(\chi_0,\chi_k\) equals FP identity / full Markov kernel | NOT SHOWN; genuine physical/fluctuation restrictions remain |
| Actual two-cutoff data distribution TV, matched-fiber defect and large-field complement | OPEN |
| CMP102b and CMP98 exact original-image equations; CMP109 (0.29),(5.37),(5.42) | OPEN |
| Continuum Yang–Mills existence, OS, positive gap | UNPROVED |

**Stopping determination:** R109 closes the narrow original-image and local FP-normalization gates. R107's general positive-kernel distinction survives, but the suspected additional physical law tilt from **the specific Eq. (0.16) gauge-fixing indicator** has been refuted by direct source inspection. No summable two-cutoff law defect is established.

**YM-R110 (unconsumed):** first choose one source-native CMP109 \(M\) and a legal \(L\), then recover the source's actual **non-FP** \(\chi_0,\chi_k\) and fluctuation charts in (0.17),(0.19),(2.9)–(2.13). Use the verified (0.15) identity to strip pure gauge factors, determine the exact remaining sector/interaction mass and whether the source can be expressed as a conditional \(M\)-pushforward on an admissible block. Construct or obstruct the actual \(N,j\) versus \(N+1,j+1\) prescribed \(V,\Omega\) data law and its defect. Do not invent a positive-alpha/historical summability rate; preserve Eq.(0.29) and remaining printed-source holds.

Highest historical numbered bibliography remains [92]. Historical passes and source receipts are append-only.
