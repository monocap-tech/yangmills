# YM-R123 — CMP109 small-field regularity feeds nonlinear M on minimizing backgrounds; fluctuation cutoff alone does not

**Date:** 2026-10-27. **Predecessor:** [YM-R122](../checkpoints/YM_HEAD_R122_20261027.json), verified main 6f1e631417330980cb069ba97562380a75eb26e4. **Completed:** native printed-source small-field carrier split and quantitative entry threshold for R122's deterministic source M bound on source-regular minimizing backgrounds; separate χk-only and regional Ω cutoff transfer remains open. **Next:** YM-R124 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source pages and exact typed targets

T. Bałaban, CMP109 (1987), [published printed PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), visually read original printed:
- p.254 / PDF index 5: (0.13)–(0.16), the FIRST integral's small-field region includes direct plaquette restriction \(\|U(\partial p)-I\|<\varepsilon_0\), alongside based-gauge contour restrictions, and gauge-invariant integration.
- p.255 / index 6: (0.17) and (0.19) have original-action integrals and cutoff χ0/χk; χk is a restricted *integral* not a free global physical small-curvature bound by itself.
- p.259 / index 10: the k-th small-field domain is defined via \(\|dU_k(V)-I\|<\varepsilon_0\eta^2\) on T_eta, plus regularity. The source's Theorem 1 is explicitly about effective actions **in the small-field approximation**, not all field sectors.
- p.260 / index 11: **(1.1)** minimizes physical A(U) with constraint \(\bar U^k=M^k(U)=V\). **(1.2)** defines regular minimizing configurations \(U_k(V)\in\mathcal U_k(\varepsilon_0)\), with \(\|U_k(V)(\partial p)-I\|<\varepsilon_0\eta_k^2\), \(\eta_k=L^{-k}\), on the indicated fine domain T; the independent J regularity also applies. The eta here is the SOURCE REGULARITY SCALE; do not silently equate it to the original bare lattice spacing ε.
- p.265 / index 16: (2.1) and following text: χk is chosen so the integration over the coarse field V is restricted to configurations for which the *minimizing background* \(U_k(V)\) belongs to \(\mathcal U_k(\varepsilon_0)\). (2.3) explicitly identifies the new critical coarse field \(V^{(k)}=M(U_{k+1}(W))\) in the source axial gauge.
- p.266 / index 17: the independent variable \(B'=(1/i)\log[V(V^{(k)})^{-1}]\), and source (2.9):
  \(\chi_k=\prod_{b\notin\{b_0(c)\}}\mathbf1_{\{\|B'(b)\|<\varepsilon_1\}}\) with optional threshold \(g_k\varepsilon_1/\gamma_k\). This monitors B' in a gauge/constraint chart, not arbitrary original-link U or every plaquette in a required R122 ribbon halo.
- p.267 / index 18: excluded \(b_0(c)\) variables are determined from the remaining B' through source constraints with a stated **O(ε1)** bound, but the exact constants, full Uk(V) nonlinear map and norm between B' and original U link fluctuations are not furnished numerically.

Original mathematical images (not just OCR) examined in this pass; [source evidence receipt](../source_receipts/YM_R123_CMP109_SMALL_FIELD_SOURCE_APPLICATION_RECEIPT_20261027.md). CMP99 later Eq.(3.157)–(3.158) original printed pages and reduced covariance normalization remain OPEN.

## 1. Two DIFFERENT smallness certificates

**S_background — physically plaquette regular**: \(\|U_k(V)(\partial p)-I\|\le x_k=\varepsilon_0\eta_k^2\) for every fine plaquette in the domain certified by CMP109 (1.2), whenever \(\chi_k\)-supported V is chosen as specified after (2.1). This is an ACTUAL SOURCE CONDITION on the minimizing background, conditional on its existence and source regularity hypotheses.

**S_fluctuation — coordinate cutoff**: monitored \(\|B'(b)\|<\theta_k\) for \(b\ne b_0(c)\), where \(\theta_k=\varepsilon_1\) or \(\theta_k=g_k\varepsilon_1/\gamma_k\), with induced excluded-bond estimates O(θk), and separate source analytic chart constraints. This is not, by equation (2.9) alone, a numerical full-plaquette bound on arbitrary U, U', or the complete R122 halo. In particular B'=0 satisfies χk while background curvature remains controlled only by its separate S_background condition. **Do not infer** η_R122≤Cθk from χk without a source operator/analytic map and boundary passport.

Source (0.16) has a first-step original-field cutoff including plaquette smallness; source (1.2)/(2.1) provides the **later step minimizing-background regularity**. Their actual carriers are not interchangeable.

## 2. Exact entry for a source REGULAR MINIMIZER into R122's nonlinear M theorem

Take a REAL SU2 background \(U=U_k(V)\) on a complete eligible R122 halo, whose plaquettes satisfy (1.2), \(x_k=\varepsilon_0\eta_k^2\). From source regularity,
\[
 \eta_{\rm halo}(U)\le x_k.\tag{R123.1}
\]
(If the halo lies outside the source regular domain, this implication is NOT certified.) Substituting in the rigorously derived R122 actual nonlinear M theorem gives:

**R123.2 — source-typed conditional background/coarse bound.** If all shortest-path ribbons for the coarse link lie in the source-regular domain and
\[
 \boxed{666\,\varepsilon_0\eta_k^2<1,}\tag{R123.2a}
\]
then
\[
 \boxed{\|M(U_k(V),c)-U_k(V)(c_{\mathrm{fine\ straight}})\|
 \le \frac{31878}{169}\frac{\varepsilon_0\eta_k^2}{1-666\varepsilon_0\eta_k^2}.}\tag{R123.2b}
\]
Here all links are real SU2, the norm is the unitary operator norm, the fine bridge is source (0.4) and the coarse object is interpreted in source gauge. It is a theorem conditional on the source defining hypotheses and the EXTRA explicit quantitative bound (R123.2a); it is not inferred directly from χk's monitored B'. For the source (2.3) critical background \(U_{k+1}(W)\), the LEFT object is the genuine coarse saddle-point configuration \(V^{(k)}\), giving the concrete source application
\[
 \|V^{(k)}(c)-U_{k+1}(W)(c_{\rm straight})\|\le \delta(\varepsilon_0\eta_{k+1}^2)
\]
whenever the same source input/hypotheses pass. This is the FIRST NATIVE BACKGROUND-to-coarse nonperturbative quantitative source link, not a two-cutoff law.

Since ηk=L^{-k}≤1, it is SUFFICIENT to restrict ε0<1/666 for every scale. CMP109 says ε0 is sufficiently small, but it does NOT print a value establishing this inequality for its fixed chosen domains. Taking a smaller ε0 produces a VALID RESTRICTED SUBDOMAIN; it does not establish the bound for every configuration in the original unspecified cutoff or preserve the original normalizing integrals automatically.

**Coverage:** a sufficient full coarse-link halo is \(\mathcal H_c=[-6,19]\times[-6,6]^3\) in L13 fine-bond units relative to y. On a full source periodic T where (1.2) holds globally, all such local plaquettes have curvature control (subject to winding/period graph consistency). Source regional X, Ω_j, Λ_j and the X^-2 interior described after (1.16) have additional support/collar restrictions: the source equations inspected do NOT establish that every desired coarse c lies at enough boundary distance for the entire halo. The regional path-containment check remains OPEN.

## 3. Explicit two-stage source-numerical threshold, with careful carrier boundary

Let \(x=\varepsilon_0\eta_k^2\), \(C=31878/169\), and \(L=13\). R122's two nested actual deterministic M applications require
\[
 x<1/666,\quad
 \widehat\eta_1(x)=169x+\frac{4Cx}{1-666x}<1/666.\tag{R123.3}
\]
Multiplying by positive \(666(1-666x)\) yields the exact inequality
\[
 \boxed{(666^2\cdot169)x^2-666(170+4C)x+1>0, \quad 0\le x<1/666.}\tag{R123.4}
\]
The admissible connected near-zero branch has \(0\le x<x_*\), where the SMALLER root is
\[
 \boxed{
 x_*=
 \frac{666(170+4C)-\sqrt{[666(170+4C)]^2-4\cdot666^2\cdot169}}
      {2\cdot666^2\cdot169}
 \simeq 1.62442843413909\times10^{-6}.}\tag{R123.5}
\]
Thus \(x\le10^{-6}\) is a simple strict SUFFICIENT choice, checked with exact Fractions; \(x=2\cdot10^{-6}\) fails this particular second-stage sufficient criterion. [Exact code](../computations/YM_R123_SMALL_FIELD_CHART_ENTRY_20261027.py).

**What this DOES and DOES NOT do:** if an actual ONE physical starting real SU2 field U0 in the legitimate source full graph satisfies eta0≤x<x*, with halos for both stages, then the deterministic nested M(M(U0)) bound R122.9 follows. If separate source minimizing backgrounds \(U_k(V)\) and \(U_{k+1}(W)\) each satisfy their own regularity bounds, this by itself does **NOT** establish \(U_{k+1}(W)=M(U_k(V))\) on an actual aligned two-UV history. Source (2.3) gives a one-step saddle link, not the external paired UV histories/partition functions. All source E/determinant and Gaussian normalization objects remain independent.

## 4. Optional fluctuation-to-curvature passport; NOT yet source instantiated

If, on a verified common eligible halo, a physical fine connection is related to a real unitary background by \(U_b=F_b U_{\rm bg,b}\) (or opposite convention) and \(\sup_b\|F_b-I\|\le\delta\), then elementary 4-link product telescoping gives
\[
 \boxed{\eta(U)\le\eta(U_{\rm bg})+4\delta.}\tag{R123.6}
\]
This is a finite real-SU2 algebraic lemma. Source χk does NOT supply δ on the physical source fine links merely by checking \(|B'(b)|<\theta_k\) on the monitored independent B' bonds. A source-valid δ would need quantitative bounds for \(B'\to H_k(B')\to U'\), special b0 constraints and gauge transformations, in the correct original-link gauge, with coverage of the entire halo. Those constants, especially across two cutoffs, are not numerical in the pages inspected.

R111's Ph=0 cutoff monitor invariance only says the *monitored* source B' cutoff is unchanged by the nonlinear constraint correction; it does NOT transport the physical-plaquette curvature condition onto all independent Gaussian coordinates.

## 5. Resolution graph / stop

| Gate | R123 |
|---|---|
| Source (1.2) background plaquette regularity | PRINTED IMAGE verified |
| Source (2.1) χk support chosen to preserve Uk(V) regularity | PRINTED IMAGE verified |
| Source (2.9) monitored independent B' only / excluded b0 | PRINTED IMAGE verified |
| Regular background enters actual nonlinear M, R123.2 | PROVED conditionally on full halo and 666 ε0 ηk²<1 |
| Background saddle \(V^{(k)}=M(U_{k+1}(W))\) | SOURCE (2.3) located; bound conditional |
| Exact stricter two-stage near-zero chart threshold | DERIVED x*≈1.624428434e-6 |
| Numerical source ε0, ε1, γk, global X/Ω collar passport | OPEN |
| χk-only→arbitrary original field curvature or fluctuation δ | NOT ESTABLISHED |
| Matching separate minimizing backgrounds / two UV histories | OPEN |
| CMP99 A_k/Δ_k and Gaussian/cutoff normalization | OPEN |
| Full Yang–Mills existence, OS and positive mass gap | UNPROVED |

**Next YM-R124 unconsumed:** Source-lock the quantitative \(B'\to H_k(B')\to U'\) chart and gauge normalizations, and calculate whether the actual monitored χk plus the source background regularity yields an ORIGINAL-FIELD complete-halo estimate at a chosen physical cutoff. Explicitly audit Ω collars and both-stage sample support. If full field transfer remains unquantified, record the hard analytic norm/jacobian gate rather than repeating small-field identities. Separately retrieve CMP99 original (3.157)–(3.158), source uniform covariance and true two-independent-UV Ω,V comparison. No continuum construction or gap theorem.

Historical bibliography highest [92]; older passes append-only and R122 fine source M theorem remains conditional.
