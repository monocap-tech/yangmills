# YM-R120 — CMP95 source path recovered; CMP98 corner to CMP109 center is an independent transport obligation

**Date:** 2026-10-27. **Previous canonical checkpoint:** [YM-R119](../checkpoints/YM_HEAD_R119_20261027.json), main 5bb4a81a3fd61698d154e61f5ee131afe680c0d1. **Status:** COMPLETE AS HISTORICAL AXIAL-PATH SOURCE RECONCILIATION, GAUGE-COVARIANT COARSE ENDPOINT FRAME MAP, AND EXACT NEW FRAME-CORRECTED L13 SPARSE COEFFICIENT. **Not proved:** a unique native common affine lattice/edge endpoint convention, CMP99 multiscale Q' / later covariance, source uniform coercivity, paired UV probability law, continuum YM or physical mass gap. **Next:** YM-R121, unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Targets, sources and custody

R119 derived the complete first variation of CMP109 printed (0.4) and compared it to a declared descending-coordinate CMP98-style chosen contour on one COMMON CENTERED block. It produced 99/28561 for a sparse transverse fine-bond fluctuation, with the correct label: a shared-centered-frame test, **not** the complete historical CMP98 geometry. The next task was to recover the actual source-selected path and normalize the relative coarse frames.

**Original-paper text witness, THIRD-PARTY OCR, not original page screenshot:**
- CMP95: T. Bałaban, *Propagators and renormalization transformations for lattice gauge theories. I*, CMP 95, 17–40 (1984), DOI https://doi.org/10.1007/BF01215753. Git immutable blob **5cb604bd3d4a5d5cc4ff274750e0f7221273310b** from chboishabba/dashi_agda, Docs/support/reference/balaban-source-extracts/cmp95-propagators-i.txt. Directly inspected lines **80–105**, original printed pp.18–19: (1.6) block with corner-anchored y, **(1.7) path y→x with descending coordinate order d,d−1,...,1**, and (1.8) linear bond average with its own rescaling.
- CMP98: T. Bałaban, *Averaging operations for lattice gauge theories*, CMP 98, 17–51 (1985), DOI https://doi.org/10.1007/BF01211042. Immutable OCR blob **1442f25d63ef4189608e73bff05c2a359c16c01d**, source (1)–(3) lines **29–40**, and source (14)–(15) lines **122–148**, original pp.17–19; numbered reference [2] lines **1662–1667** points **directly to CMP95**. Source Eq.(14) explicitly refers to parent [2] for its contour symbols. Thus the descending-coordinate selection in R119 is not an arbitrary convenient path: it is an **actual historical source ancestor** of CMP98 Eq.(15). This does NOT, by itself, verify unique path details on all nested boundaries or the fine-lattice half-site convention.
- CMP109: T. Bałaban, *Renormalization group approach to lattice gauge field theories. I*, CMP 109, 249–301 (1987), DOI https://doi.org/10.1007/BF01215223. Original published printed page images directly **reinspected** in third-party full [54-page scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), PDF indices 2,3,4 / printed pp.251–253. Source p.251 sets odd L>11 and centered-lattice system; (0.3) p.252 defines blocks by a cube with **center at y**; (0.4) p.253 uses independent sets of uniformly weighted shortest-permutation paths from both centers, plus a parallel transported bridge. CMP98/CMP95 corner-anchored geometry is **not the same** as CMP109 centered geometry.

[Source receipt](../source_receipts/YM_R120_CMP95_HISTORICAL_PATH_AND_FRAME_RECEIPT_20261027.md). No new CMP95 or CMP98 mathematical PDF image was acquired; their equations remain original-paper OCR. Correct numerical output is NOT more source-certified than its input geometry.

## 1. Source-recovered actual descending axial path

**LITERATURE SOURCE FACT (original-paper OCR):** CMP95 (1.7) explicitly defines the path \(\Gamma_{y,x}\) by joining y to the point with coordinates \((y_1,\dots,y_{d-1},x_d)\), then to the point with \(x_{d-1},x_d\), and continuing until x. Hence on d=4 it traverses axes \(4\to3\to2\to1\), using oriented coordinate segments. CMP98 (14)–(15) uses the \(\Gamma\) notation and directs the reader to CMP95 [2], thereby fixing a direct **source ancestry** for R119's descending selected-path rule.

**CRITICAL CUSTODY CORRECTION:** R119's 99/28561 assumes the old descending path but evaluates it on the *new centered* 13^4 sampling block with both coarse endpoints y and y'=y+13e1 held fixed. This is an explicitly shared-frame comparison with an imported old path rule, **not the historical CMP98 corner-based one-step map**. The coefficient remains exactly correct for its declared test, but must not be relabeled as the original old-versus-new native map difference. R119 historical passage was appropriately marked conditional. The stronger source-ancestry resolution does not erase that remaining geometry distinction.

## 2. Gauge-covariant transport of historical coarse endpoints

Let a **common physical fine block** be specified, with old coarse corner y and revised CMP109 coarse center \(s_y\) of that block. Let \(\tau_y:y\to s_y\) be an explicitly selected fine-lattice path (source-compatible axial choice permitted). For a coarse bond c=(y,y') and matching new bond \(\hat c=(s_y,s_{y'})\), define
\[
 \boxed{\bar M_{98}^{\tau}(U,\hat c)
   :=U(\tau_y)^{-1}\,M_{98}(U,c)\,U(\tau_{y'}).}\tag{R120.1}
\]
With connection convention \(U(\gamma)\mapsto g(\gamma_-)U(\gamma)g(\gamma_+)^{-1}\), this transforms as
\(\bar M_{98}^{\tau}\mapsto
g(s_y)\bar M_{98}^{\tau}g(s_{y'})^{-1}\), i.e. EXACTLY like CMP109's center-anchored coarse link, provided the source **same fine connection and matching graph** are used. This is an exact finite lattice group-theoretic deduction, not a claim that the old and new RG probability-law maps coincide.

At U=1, differentiate:
\[
 (D\bar M_{98}^{\tau})_{\bf1}[A](\hat c)
 =-a(\tau_y)+(DM_{98})_{\bf1}[A](c)+a(\tau_{y'}).\tag{R120.2}
\]
For any fine pure gradient \(A=d\lambda\), old source full-link covariance gives
\(DM_{98}[d\lambda]=\lambda(y')-\lambda(y)\), and path telescoping gives
\[
 \boxed{D\bar M_{98}^{\tau}[d\lambda](\hat c)
 =\lambda(s_{y'})-\lambda(s_y)
 =DM_{109}[d\lambda](\hat c).}\tag{R120.3}
\]
Thus the transported old-new difference annihilates all complete-connection gauge gradients on a **correctly shared fine bond Hilbert space**; no false coarse-gauge mismatch is introduced by a necessary basepoint relocation.

For each x in the *common physical fine block*, let \(\Gamma^0_{y,x}\) be CMP95's old descending path and \(\Gamma_{s_y,x}\) a CMP109 shortest path. If the two source block sampling sets and bridge routes are matched, the first-order difference of the full links is
\[
 \boxed{
 \begin{aligned}
 \Delta^\tau_{\hat c}[A]
 =L^{-4}\sum_x\Big[
 &\operatorname{av}_{\Gamma_{s_y,x}}a(\Gamma_{s_y,x})
 +a(\tau_y)-a(\Gamma^0_{y,x})\\
 {}-&\operatorname{av}_{\Gamma_{s_{y'},x'}}a(\Gamma_{s_{y'},x'})
 -a(\tau_{y'})+a(\Gamma^0_{y',x'})
 \Big].
 \end{aligned}}\tag{R120.4}
\]
Each bracket is a closed fine-lattice path integral (equivalent signs and origins chosen by orientation), hence an integer-plaquette-curl functional **inside a contractible common block**, barring a nontrivial source regional topology. The bridge cancels only if the **same** [x,x'] is genuinely source permissible at both frames.

**No source numeric operator norm or contraction** follows from R120.4. The earlier R119 curvature bound 10584/169 was for common center basepoints and cannot be applied unchanged after adding the two \(\tau\) legs and changing source block geometry. A new plaquette-chain count and exact boundary check are required.

## 3. Exact corner/center L13 model with independently executed sparse certificate

**DERIVED DECLARED FINITE MODEL, not automatic global original-paper geometry.** Choose integer site coordinates on the fine block \(\mathcal B=\{0,1,\dots,12\}^4\), old coarse corner \(y=(0,0,0,0)\) and right corner \(y'=y+13e_1\), new centers \(s=(6,6,6,6)\), \(s'=s+13e_1\), all on a common 4D fine integer grid. A full specification of the source torus half-spacing, inclusive/exclusive block endpoints and regional collars has NOT been recovered at printable-image fidelity, so this is a declared exact common-cell realization of the geometric comparison, not the unique native source lattice.

Use CMP95 (1.7) descending-coordinate paths for all old \(\Gamma^0\), CMP109 (0.3) uniformly averaged shortest axis permutations for the new \(\Gamma\), identical fine e1 bridges [x,x+13e1], and transport paths \(\tau_y,\tau_{y'}\) ALSO in the source-descending coordinate order. Let the fine fluctuation A be a unit fixed SU(2) Lie component on the single positive e3 edge
\[
 b_*:(0,1,0,0)\to(0,1,1,0),\qquad A=0\ \text{elsewhere}.
\]
The old left path traverses axis 3 before axis 2, hence never meets b* at transverse e2-coordinate 1; the old right paths, both e1 bridges and both transport legs similarly have ZERO coefficient. Thus \(D\bar M_{98}^{\tau}[A]=0\).

For the new left centered path s→x, to traverse b* in the negative e3 direction, all coordinates other than e3 must already be at their endpoints (0,1,0), and the e3 segment must reach 0. This happens at **exactly one site** x=(0,1,0,0). All four coordinate axes are active and axis 3 must be LAST. There are 3!=6 such permutations among 4!=24, contributing signed mean \(-6/24=-1/4\). The new right paths cannot meet e1=0. Therefore
\[
 \boxed{
 (DM_{109}-D\bar M_{98}^{\tau})_{\bf1}[A](\hat c)
 =-\frac{1}{4\cdot13^4}=-\frac{1}{114244}.}\tag{R120.5}
\]
This is DIFFERENT from R119's 99/28561 shared-centered-frame coefficient, with no contradiction: their source geometry passports differ. Both are finite-dimensional exact results with declared sampling/boundary conventions; neither computes an actual two-cutoff RG measure defect.

[Exact rational integer-block certificate](../computations/YM_R120_CORNER_CENTER_LINK_FRAME_L13_20261027.py) checks R120.5 over the complete 13^4 fine-site cell and all active-axis permutations, source-descending old paths and transport legs, plus the sign and pure-gauge endpoint identity. Independently executed with PASS. No scipy, no floating precision.

**Important countercheck:** \(\tau\) is not a scalar normalization or an independent cutoff factor. It is a field-dependent fine holonomy; dropping it would change the coarse gauge endpoints and violate R120.3 for arbitrary \(\lambda\). Replacing the common physical block by unrelated centered and corner sampling sets without this transport changes the operator for reasons other than contour permutations. Therefore do not transfer R119 numerical operators or bounds to the full historical source maps solely by matching the name “average”.

## 4. Source genealogy and remaining independent objects

The CMP95 path Γ from (1.7), CMP98 use of Γ in (14)/(15), and CMP109 Euclidean-symmetrized (0.3)/(0.4) now form a direct source ancestry. **The selected contour order is SOURCE-RECOVERED; the actual regional geometry/affine chart is NOT fully reconciled.** The finite frame transport shows how to avoid conflating these.

CMP99 (3.113)–(3.115) operates on a relative fluctuation \(U'\) with an external background \(U\) fixed and produces induced site gauge averaging \(Q'_j(U)\); CMP98/CMP109 (11)/(0.4) act on whole connections under endpoint gauge. R119's transformation-type resolution stands. A full background \(U'U\mapsto M(U'U)\) derivative and the CMP99 fluctuation Jacobian / gauge-averaging source dictionary are still open.

CMP99 original-paper OCR (3.157)–(3.158) remains damaged; original printed equation images and exact \(A_k\leftrightarrow\Delta_k\) source covariance normalizer not obtained. Full nested annular \(Q'_j\) rank on \(\Omega\)/Dirichlet collars, uniform CMP109 Gaussian precision, actual legal two-independent UV histories with prescribed \(\Omega,V\), normalized physical laws, summable cutoff difference, OS and continuum spectral gap are all open. The complete source-specific positivity/measure obligation must not be demoted to an apparently harmless finite contour difference.

## 5. STOP / YM-R121 unconsumed

| Item | R120 disposition |
|---|---|
| CMP98 chosen contour historical antecedent | SOURCE OCR CMP98 [2] → CMP95 (1.7), descending 4,3,2,1 |
| Historical CMP95/CMP98 block vs CMP109 block | CORNER vs CENTER source geometry explicitly recognized |
| Coarse-link frame transport | EXACT group covariance R120.1, first variation R120.2 |
| Common-fine-chart pure gauge | EXACT equality R120.3 |
| Complete first-order frame-corrected difference | EXACT R120.4 conditional on matched physical site set/bridges |
| Declared L13 four-dimensional integer common cell | Exact sparse new minus transported old = -1/114244; executable certificate |
| R119 99/28561 | CORRECT for its shared-centered-frame model, not a native corner-center source coefficient |
| Historical exact torus offset/collar/normalization | OPEN; no unconditional old/new source operator identification |
| Uniform source covariance or old/new law summability | OPEN |
| CMP99 Q'_nested, \(\Delta_k/A_k\), \(\Omega/V\), OS continuum gap | OPEN |

**YM-R121** must recover the affine fine-lattice offset/normalizations, original CMP95/CMP98 block endpoint conventions, CMP109 center lattice and actual common torus frame, then construct the exact corresponding operator between common physical bond Hilbert spaces (including the two \(\tau\) legs and any boundary terms). Compute its plaquette-chain coefficient bounds on that native geometry before claiming uniformity. In parallel, source-recover CMP99 (3.157)–(3.158) original equation and multiscale \(Q'_j\) ranks to return to the true covariance and two-UV-probability obligations. No theorem-level Yang–Mills mass gap.
