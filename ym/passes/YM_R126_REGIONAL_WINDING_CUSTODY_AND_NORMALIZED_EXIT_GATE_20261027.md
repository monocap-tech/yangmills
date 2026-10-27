# YM-R126 — Local V cannot determine excluded winding holonomy; normalized cutoff-exit requires weight and partition control

**Date:** 2026-10-27. **Repository:** monocap-tech/yangmills. **Resume:** [YM-R125](../checkpoints/YM_HEAD_R125_20261027.json), merged main 8b2bd3325fa84a279d07960ba27ad5312685718b. **Completed:** exact periodic SU(2) flat seam counterexample to any LOCAL-Ω,V-only identification of global winding data, precise necessary observability coverage for R125, and exact normalized bad-event probability accounting with a finite reweighting counterexample. **Not completed:** CMP102 original Section G Proposition 9/(190) source norm, actual Bałaban Ω geometry and support, numerical χ exit, paired cutoff marginal normalizers, CMP99 reduced precision or continuum YM. **Next:** YM-R127 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source custody and source limitations

**Original cited paper**: Bałaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP 102(2) 277–309 (1985), DOI https://doi.org/10.1007/BF01229381. Publisher [Springer article preview](https://link.springer.com/article/10.1007/BF01229381) identifies a subscription-controlled original paper and abstract; direct /content/pdf redirects to the preview. An [older Michigan DeepBlue URL](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46461/220_2005_Article_BF01229381.pdf?sequence=1) was inaccessible through the web reader. Rutgers bibliographic metadata confirms identity but not the numbered equations. The original mathematical **Section G Proposition 9 / (190) remains UNREAD**. Do not infer an A, κ, bond metric, Ω collar, or uniform derivative bound from a secondary exposition. No full original-paper proof claim is made.

**Actual verified upstream CMP109 source:** [R124](../source_receipts/YM_R124_FLUCTUATION_GLOBAL_HOLONOMY_SOURCE_RECEIPT_20261027.md) pins original printed pp.251–253,265–267 and p.299 bibliography: CMP109 (0.4) is the real nonlinear M link average, p.265 Landau fluctuation is e^{iηH_k(B')}U_bg, and p.266 (2.9) constrains independent B' coordinates excluding special b0. [R125](../source_receipts/YM_R125_CMP102_HK_AND_WINDING_LAW_SOURCE_RECEIPT_20261027.md) pins the original-paper CMP109 text p.271, citing CMP102 Proposition 9/(190). **No new CMP109 or CMP102 mathematical printed images were acquired in this pass.** The actual source topology of allowed nested Ω, Λ and Dirichlet collars is not being guessed from a generic torus model.

## 1. NEW exact flat SU(2) seam counterexample — local prescribed V is insufficient without winding coverage

Take a periodic four-dimensional lattice \(T_N=(\mathbb Z/N\mathbb Z)^4\), with \(N\) divisible by L=13. For arbitrary real θ define \(D(θ)=\mathrm{diag}(e^{iθ},e^{-iθ})\in SU(2)\). Set the positive e1 links to
\[
 U_\theta(x,e_1)=\begin{cases}D(θ),&x_1=N-1,\\I,&x_1\ne N-1,\end{cases}
 \qquad U_\theta(x,e_j)=I,\quad j=2,3,4.\tag{R126.1}
\]
The seam e1 holonomy is the SAME for all transverse x2,x3,x4. Every elementary e1/ej plaquette is identity: either both opposing e1 links are I or both equal D(θ). All other plaquettes are I. Hence
\[
 \boxed{\eta_{\rm plaquette}(U_\theta)=0 \text{ for every }\theta.}\tag{R126.2}
\]
But a positively oriented winding cycle in direction e1 crosses the seam once:
\[
 \boxed{W_1(U_\theta)=D(θ),\qquad
 \tfrac12\operatorname{ReTr}W_1(U_\theta)=\cos θ.}\tag{R126.3}
\]
The trivial field has winding trace 1. For θ=π/3 the trace is 1/2; for any arbitrarily small nonzero θ it is different from 1 while every link is arbitrarily near I.

Choose a source-style **declared** region Ω of fine bonds/plaquettes avoiding every seam-crossing e1 link. For example in N=39 choose a core with 2≤x1≤36 and choose any coarse link c whose entire CMP109 R122 halo is within this core, such as y1=10 and fine e1 halo [4,29] with its other coordinates source-admissible. On every bond of that region, \(U_\theta=U_0=I\) EXACTLY. Any coarse link averaging \(M(U,c)\) computed using paths entirely in that region therefore agrees identically for the two fields, \(M(U_\theta,c)=M(U_0,c)=I\). The same holds for arbitrary iterated local averages whose full SOURCE SUPPORTS remain there.

**Precise refutation:** *equality of merely local prescribed coarse data \(V|_\Omega\)* does NOT determine the full-torus winding Wilson value. Even \(\eta=0\) and exact local M agreement leave \(\cosθ\ne1\). This is a **counterexample to dropping the winding-coverage hypothesis**, NOT to R125 as written. R125 deliberately assumed a common V on the SAME coarse graph containing the chosen winding cycle with compatible homology/path lifts. The example is on a generic periodic SU2 graph; it has not been shown to lie in every actually allowed Bałaban multi-region Ω/χ/Dirichlet sector. No source theorem fails merely because this family exists.

**Global-holonomy class versus topological sector:** as θ varies continuously the flat family varies continuously. Do not assert disconnected sectors. As in R124, different traces prove distinct periodic gauge orbits.

**Necessary coverage passport R126.4.** To apply R125.4–R125.7 to a global winding observable through prescribed V, require a *source certified noncontractible coarse cycle γ entirely represented in the COMMON prescribed coarse-data graph* and fine representatives in the same homology class at each UV history, with all CMP109 averaging ribbons/halos and region/collar constraints admissible at every step. Local \(V|_\Omega\) or matching plaquette data alone do not suffice. The necessity is EXPLICIT, not a claim such cycles exist in Bałaban's restricted Ω.

## 2. The missing normalized EXIT q_i is a ratio, not a Gaussian tail by itself

Let \(\gamma_{i,V,\Omega}\) be an appropriate FINITE-DIMENSIONAL centered constrained Gaussian reference probability measure (if its native covariance and chart exist). Write a candidate real positive normalized source interaction law
\[
 d\mu_i=\frac{\mathbf1_{\chi_i}w_i\,d\gamma_{i,V,\Omega}}{Z_i},
 \qquad
 w_i=e^{-I_i}\ge0,\quad
 Z_i=\int\mathbf1_{\chi_i}w_i\,d\gamma_{i,V,\Omega}>0.\tag{R126.5}
\]
The exact bad event for R125 is \(G_i^c\), where G_i includes H_k bounds, physical plaquette chart, all-stage \(\Omega\) halos, winding-cycle geometry and true M identities—not merely \(\chi_i\).

Thus
\[
 \boxed{q_i=\mu_i(G_i^c)=
 \frac{\int \mathbf1_{\chi_i}\mathbf1_{G_i^c}w_i\,d\gamma_{i,V,\Omega}}
 {\int \mathbf1_{\chi_i}w_i\,d\gamma_{i,V,\Omega}}.}\tag{R126.6}
\]
By definition \(\mu_i(\chi_i^c)=0\) when the law is already normalized with χ_i. **That tautology does not give \(q_i=0\)** unless χ_i support also implies every stronger good-event passport. The existing R110/R111 χ monitor algebra does not automatically imply this.

**Explicit sufficient bound:** if on χ_i support \(0<a_i\le w_i\le b_i<\infty\) and \(\gamma_{i,V,\Omega}(\chi_i)>0\), then
\[
 \boxed{q_i\le
 \frac{b_i}{a_i}
 \frac{\gamma_{i,V,\Omega}(\chi_i\cap G_i^c)}
 {\gamma_{i,V,\Omega}(\chi_i)}.}\tag{R126.7}
\]
This elementary estimate is *not necessarily useful in volume/cutoff* unless the weight ratio and Gaussian ratio are controlled UNIFORMLY. A more flexible form requires independently \(Z_i\ge z_i>0\), \(w_i\le b_i\) on χ_i, so \(q_i\le b_i\,\gamma_i(\chi_i\cap G_i^c)/z_i\). The actual Bałaban source action, characteristic functions, FP Jacobian, inherited E and determinant may not be captured by one positive scalar w on an arbitrarily selected variable chart without further measure construction. R126.5 is a **conditional model passport**, NOT a source factorization claim.

**Rigorous negative control:** let \(\gamma(A)=\epsilon\), \(0<\epsilon<1\), χ=1, and interaction weight \(w=\epsilon^{-2}\) on A and \(w=1\) otherwise. Then
\[
 \gamma(A)=\epsilon\longrightarrow0,\qquad
 \boxed{\mu(A)=\frac{1}{1+\epsilon(1-\epsilon)}
 \longrightarrow1.}\tag{R126.8}
\]
For \(\epsilon=1/100\), \(\mu(A)=10000/10099\), while base probability=1/100. Therefore an excellent Gaussian tail on the bad event can become near certainty after weighting and normalization, even with a positive finite partition function. **An unweighted Gaussian exit estimate cannot be substituted for normalized source q_i**. This is a general two-point measure counterexample, not an actual Yang–Mills RG input.

The [exact arithmetic certificate](../computations/YM_R126_FLAT_SEAM_AND_NORMALIZED_EXIT_20261027.py) checks N=39 periodic flat seam plaquettes/winding exponent and this reweighting probability with rational arithmetic. The finite group part uses SU2 diagonal phases symbolically and Wilson trace cosθ is exact analytic.

## 3. Consequences for the R125 two-UV scalar W1 theorem

R125 conditional
\[
 W_1((X_0)_\#\mu_0,(X_1)_\#\mu_1)
 \le \min\{2,e_0+e_1+2(q_0+q_1)\}
\]
remains valid **only when both normalized marginals exist, actual Ω,V include the common winding cycle, and e_i and q_i control all-stage source M and bad-event failure**.

The seam example proves: if Ω,V are only local and exclude the winding cycle, even a flat field and identical local V do not define a COMMON center scalar \(v=\frac12\operatorname{Tr}V(\gamma)\). A proposed W1 bound with *e_i=q_i=0* based solely on local curvature/Ω data would be false, since the two Dirac measures on Wilson values \(\cos θ\) and 1 have \(W_1=1-\cos θ\ne0\). This is a **negative control against dropping R125's explicit geometry hypothesis**, not against R125 itself.

The reweighting example proves: even if a pre-interaction Gaussian estimates small failed-curvature events, the resulting source normalized failure q_i can remain order one without partition-function and weight control. Finally, even a source-valid scalar W1 does not imply total variation for full gauge fields (R125 Dirac counterexample retained).

## 4. Source obligations and mandatory STOP

| Obligation | R126 verdict |
|---|---|
| CMP102 Sect G Proposition 9/(190) ORIGINAL mathematical image and norm | **OPEN; publisher preview/paywall, external archive unavailable** |
| Source \(H_k(B')\) exponential kernel / \(A,\kappa\) | **NOT IMPORTED** |
| True Bałaban Ω, Λ, collars containing selected winding cycle | **OPEN — NECESSARY GEOMETRIC PASSPORT RECORDED** |
| Flat seam: local Ω/V fails to determine global winding | **EXACT COUNTEREXAMPLE**, not actual source admission proof |
| Exact normalized cutoff-exit ratio q_i | **IDENTITY R126.6** under explicitly modeled positive finite law |
| Gaussian tail alone ⇒ normalized q_i small | **FALSE**, exact 2-point reweighting witness |
| Source uniform lower normalizer and interaction/Jacobian weight bound | **OPEN** |
| R125 two-UV scalar W1 actual instantiation | **OPEN**, source actual Ω/V histories and q_i |
| CMP99 late Gaussian precision, inherited E/determinants | **OPEN** |
| Continuum YM, reflection positivity, mass gap | **UNPROVED** |

**YM-R127 unconsumed:** prioritize the primary CMP102 Section G original estimate (not secondary commentary) or explicitly solicit source image under lawful institutional access; source-map actual χ/Ω support to a noncontractible coarse winding loop where available, and recover an actual source expression for the positive constrained normalized density, its partition lower bound and failed good-event weight. If Ω excludes winding, route observable to a genuinely local physical Wilson square per R106 instead of inventing global V. Resolve CMP99 late (3.157)–(3.158) separately. NO_TRANSFER of source constants or theorem-level mass gap claims.

Prior pass custody append-only. Historical reference highest [92].
