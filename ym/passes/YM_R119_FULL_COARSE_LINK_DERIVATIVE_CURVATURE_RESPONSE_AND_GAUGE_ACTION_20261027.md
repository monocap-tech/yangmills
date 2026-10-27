# YM-R119 — complete coarse-link derivative, transverse curvature response, and gauge-action context passport

**Date:** 2026-10-27. **Predecessor:** [YM-R118](../checkpoints/YM_HEAD_R118_20261027.json), merged main 9170c7d93326b898fec7cba0904b3ab504c89123. **Result:** Completed as an exact FIRST-ORDER full-source coarse-link derivative, a declared old-path-vs-new source-specific L=13 rational example, and a conditional curvature sup-norm bound; CMP98/CMP99 apparently conflicting gauge signatures are correctly separated by their transformation inputs. **Still OPEN:** the precise historically selected paths actually used for all CMP98 (15) bonds, CMP99 full regional Q' / operator A_k–Delta_k, uniform source covariance, two UV laws and continuum mass gap. **Next:** YM-R120 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source custody and precise output

**CMP109 printed original pages directly visually checked** from [54-page third-party scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf): zero-based PDF indices **3 (printed p.252), 4 (printed p.253), 5 (printed p.254)**; source (0.3) defines centered L-block B(y) and shortest coordinate-order permutation contours G(y,x), and **(0.4)** explicitly sums over BOTH independent sets of shortest paths Gamma:y→x and Gamma':y'→x', together with parallel translated [x,x'] and inverse coarse bond (-c). The gauge-invariant group average axiom (0.8) has arithmetic Lie-algebra derivative, so no unknown first-order group-average coefficient enters.

**CMP98 original-paper third-party OCR**, immutable Git blob **1442f25d63ef4189608e73bff05c2a359c16c01d**, lines 94–146 (source selected-contour group average (15), first-order (14) and coarse-endpoint covariance (11)); lines 365–377 give a **descending-coordinate axial gauge path** as one explicit ordered-coordinate contour used in its estimates. This does NOT establish that the particular selected Gamma in (15) must equal that descending path for every source c,x; the comparison below explicitly DECLARES that permissible older-style axial choice, not a recovered globally mandated CMP98 path. Refs in [R119 receipt](../source_receipts/YM_R119_PRINTED_FULL_LINK_AND_BACKGROUND_GAUGE_RECEIPT_20261027.md).

**CMP99 original-paper third-party OCR**, immutable blob **ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743**, lines 1427–1463: source (3.113) transforms the **relative fluctuation U' against an external background U**; the one-step induced site gauge is R(U)u, and differentiation (3.114)–(3.115) yields the historical Q_j D = D_j Q'_j. This is not the same type of gauge action as CMP98's full-connection U→U^u with coarse endpoint u(y). Background U is held fixed in the relative fluctuation comparison. No source contradiction follows from displaying the two formulas side-by-side. The actual Q'_j and CMP109 M charts and covariance remain unaligned.

## 1. SOURCE LINEARIZATION — whole CMP109 (0.4) coarse bond, not an isolated contour

Fix the legal odd scale L=13, dimension d=4, group SU(2), and the identity connection. Let c=(y,y') be a coarse horizontal bond with y=0, y'=Le1, and for each x∈B(y) set x'=x+Le1. For fine one-parameter fields U_b(t)=exp(tA_b), define the first variation of any oriented path Gamma by the signed sum a(Gamma)=Σ_{b∈Gamma} ±A_b, with all A_b Lie algebra valued. Define the translated bond path [x,x'] parallel to c.

CMP109 printed (0.4) is a coarse connection M(U,c)= exp[ average of logarithms of
 U(Gamma)U([x,x'])U(-Gamma')U(-c) ] U(c), where x runs over the L^4 centered fine sites and Gamma,Gamma' are **separately** averaged uniformly over shortest-coordinate permutations. Lie-group logarithm, exponential and axiom (0.8) all have identity differential at zero (appropriate source convention of i in Lie algebra).

Differentiation at U=1 gives, **EXACTLY**,
\[
 \boxed{
 (DM_{109})_{\mathbf1}[A](c)=
 L^{-4}\sum_{x\in B(y)}
  \left[\operatorname{av}_{\Gamma\in G(y,x)}a(\Gamma)
       +a([x,x'])
       -\operatorname{av}_{\Gamma'\in G(y',x')}a(\Gamma')\right].
 }\tag{R119.1}
\]
The -a(c) from the inner log cancels the +a(c) from the outer U(c) because every normalized path/site average has unit mass. **This is a full coarse-link derivative**, not a gauge-fixing coordinate.

For CMP98 source (15) with **a declared fixed selected contour family** \(\Gamma^0_{y,x}\), the corresponding full link derivative is
\[
 \boxed{
 (DM_{98}^{\Gamma^0})_{\mathbf1}[A](c)=
 L^{-4}\sum_{x\in B(y)}
 \left[a(\Gamma^0_{y,x})+a([x,x'])-a(\Gamma^0_{y',x'})\right].
 }\tag{R119.2}
\]
Both use the same declared bridge [x,x']; this exact matching is a SOURCE CHOICE CONDITION, not a claim that the original historical implementations are already identified across every boundary.

Subtracting cancels **the full bridge**, leaving
\[
 \boxed{
 \Delta_c[A]=L^{-4}\sum_x
   [(\operatorname{av}a(\Gamma)-a(\Gamma^0_{y,x}))
    -(\operatorname{av}a(\Gamma')-a(\Gamma^0_{y',x'}))].
 }\tag{R119.3}
\]
This replaces R118's merely local contour-coordinate formula with the exact full coarse-link *difference formula* under explicit CMP98 selected-path and endpoint-bridge conventions.

## 2. EXACT gauge-direction compatibility on the actual full coarse-link operators

For every site gauge parameter lambda and A=d lambda, any path sum telescopes:
a(Gamma)=lambda(x)-lambda(y), a([x,x'])=lambda(x')-lambda(x), a(Gamma')=lambda(x')-lambda(y'). Hence **each individual** summand in R119.1 and R119.2 equals
\[
 \lambda(y')-\lambda(y).
\]
It follows with no Gaussian/renormalization assumptions that
\[
 \boxed{DM_{109}[d\lambda](c)
       =DM_{98}^{\Gamma^0}[d\lambda](c)
       =\lambda(y')-\lambda(y),\quad
       \Delta_c[d\lambda]=0.}\tag{R119.4}
\]
Thus on this correctly shared **full-connection gauge action**, the difference is a transverse/curl-functional, rather than the coarse representative mismatch previously considered under CMP99's relative-background action. R117's fixed-representative seam is still real when comparing two differently constrained RG histories, but it is **not an intrinsic contradiction between CMP98 and CMP109 full-connection covariance**.

## 3. REAL L13 SOURCE-SHAPED SPARSE RESPONSE — nonzero whole-link difference

Use centered fine block B(0)={-6,-5,...,6}^4, coarse c:0→13e1, left and right shortest paths from (0,0,0,0) and (13,0,0,0), and select an older-style **descending axial coordinate order 4,3,2,1**. CMP98 explicitly uses this type of descending-coordinate axial path in its local estimate (OCR around p.24). We do NOT assert without an original source path table that this is the unique CMP98 (15) Gamma for every c,x.

Set A to one unit Lie-algebra component on the **positive e3 fine bond**
\(b_*:(0,1,0,0)\to(0,1,1,0)\), and zero elsewhere. This edge is fully within the left block; the right endpoint paths have first coordinate at least 7 and the bridge [x,x'] consists of e1 bonds, so NEITHER can encounter b*. The selected descending path reaches its e3 displacement BEFORE its e2 displacement, and never traverses b*, which sits at e2=1. Therefore \((DM_{98}^{\Gamma^0})[A](c)=0\).

The symmetric new path traverses b* precisely for sample sites x=(x1,1,x3,x4) with x3=1,...,6, arbitrary x1,x4∈[-6,6], and a permutation of active coordinate directions with 2 before 3 and any present 1 or 4 AFTER 3. The probability among active-coordinate permutations is:
- x1=x4=0: 1/2;
- exactly one of x1,x4 nonzero (24 choices): 1/6;
- both nonzero (144 choices): 1/12.

For EACH x3 there are therefore 1/2+24/6+144/12=33/2 expected traversals. With x3=1,...,6 this is 99. Dividing by L^4=13^4=28561 gives
\[
 \boxed{
 (DM_{109}-DM_{98}^{\Gamma^0})[A](c)=99/28561\neq0.
 }\tag{R119.5}
\]
This is an **exact coefficient of a specified full coarse-link derivative** for the declared admissible selected axial path family. It does not establish the actual historical CMP98 path in every source context, nor an absolute norm difference of the complete operator or an RG law.

[Executable exact rational test](../computations/YM_R119_FULL_LINK_FIRST_VARIATION_L13_20261027.py), Python standard library only, enumerates the relevant shortest-path permutations. Independently run in the runtime: PASS; old coefficient=0, new coefficient=99/28561. It also checks the curvature-weight upper-bound arithmetic below.

## 4. DERIVED finite-block curvature-Lipschitz bound, not a renormalization contraction

In a simply connected cubic fine block, replacing a selected monotone shortest coordinate-order path \(\Gamma^0\) by another permutation \(\Gamma\) changes the path integral by the flux of an integral 2-chain of plaquettes. A swap of two coordinate-direction segments i,j contributes at most |xi||xj| elementary plaquettes; bubble-sort between the orderings has no more than one swap per pair of active axes. Consequently
\[
 |\operatorname{av}_{\Gamma}a(\Gamma)-a(\Gamma^0)|
 \le\frac12\sum_{1\le i<j\le4}|x_i x_j|\,\|dA\|_{\infty},\tag{R119.6}
\]
because for uniformly distributed permutations each ordered pair is inverted relative to a fixed selected order with probability exactly 1/2. The right endpoint has the SAME displacement x, and a second contribution of the same magnitude. Averaging x over the centered L^4 hypercube,
\[
 |\Delta_c[A]|
 \le \left(\sum_{i<j}\mathbb E_{x\in B(0)}|x_i x_j|\right)\|dA\|_{\infty}.
\]
The coordinates are independent uniform integers in {-6,...,6}, giving \(\mathbb E|x_i|=42/13\). Thus
\[
 \boxed{
 \|\Delta A\|_{\ell^\infty(\text{coarse links})}
 \le 6(42/13)^2\,\|dA\|_{\ell^\infty(\text{fine plaquettes})}
 =\frac{10584}{169}\|dA\|_{\infty}.
 }\tag{R119.7}
\]
All norms use the same Lie-algebra norm, vector triangle inequality and **monotone fixed axis-order selected paths at BOTH endpoints** on legal contractible centered blocks. Formula R119.7 is a finite-block L13 FIRST-ORDER response bound that is independent of the NUMBER of disjoint blocks. It is not an RG contraction (coefficient >1), a uniform covariance bound, a large-field estimate, or a common normalized probability law. It does not extend automatically to topologically nontrivial regional contours or other selections that are not monotone coordinate permutations.

For a general odd L with r=(L-1)/2, the same calculation gives \(6[r(r+1)/L]^2\); the bound grows with L and cannot be invoked uniformly over L→∞. The present native source scale L=13 is fixed, but UV/history control remains unsolved.

## 5. CORRECTION to R117/R118 apparent CMP98/CMP99 gauge-signature conflict

CMP98 (11) concerns the **complete gauge connection U** and transforms it by arbitrary fine gauge u; covariance of the coarse link involves coarse endpoint values \(u(y),u(y')\). This is exactly what R119.4 shows after differentiation for CMP98 and CMP109 full-link maps.

CMP99 (3.113) instead studies a **relative fluctuation U' around a specified background U**, with U' initially set to identity in a gauge-change calculation and the background held as a specified external datum. The induced transformation of the coarse relative fluctuation is by the **averaged site variable R(U)u**; its derivative is CMP99 (3.114)–(3.115), \(Q_jD=D_jQ'_j\). This is not literally the same input transformation as full-connection covariance of CMP98 (11). An identity \(\operatorname{DM}_{98}d=d_cE_y\) for full fine gauge and an identity \(Q_jD=D_jQ'_j\) for a fixed-background fluctuation are therefore **not contradictory**; R118's two-block “signature contradiction” was an explicitly conditional type test, not evidence the source papers conflict. R119 **closes that apparent source contradiction at the transformation-context level** while retaining the actual background-to-full-field derivative dictionary as an open construction.

This distinction does NOT identify the full historical Q_j with revised CMP109 M, nor does it establish the mixed-background covariant derivative or the nested regional gauge-domain passport needed by source covariance comparisons.

## 6. Open obligation graph / stop

| Gate | YM-R119 verdict |
|---|---|
| CMP109 printed full (0.4) first variation | EXACT R119.1, original paper image checked |
| CMP98 (15) selected-family full first variation | EXACT R119.2 conditional on stated older-style path/bridge |
| Difference of full coarse links | EXACT source-shaped R119.3 |
| Pure gauge compatibility | EXACT R119.4 on common full-connection tangent |
| L13 sparse transverse source-shaped coefficient | EXACT 99/28561 for declared descending selected axial path; certified by reproducible rational test |
| One-link local curvature sup bound | EXACT 10584/169 for fixed monotone selected axis orders; not summability |
| CMP98 full vs CMP99 fixed-background source gauge action | APPARENT CONTRADICTION RESOLVED AT TRANSFORMATION TYPE |
| Historical actual CMP98 \(\Gamma_{y,x}\) unique source convention | OPEN; R119 descending choice is a declared CMP98-style axial path |
| CMP99 full nested Q' source rank / Ω collars | OPEN |
| CMP99 (3.157)–(3.158) precision/covariance original page | OPEN |
| Source CMP109 Hessian native gamma and two-UV law | OPEN |
| Continuum OS Yang–Mills physical gap | UNPROVED |

**YM-R120 unconsumed:** recover the exact source-selected old contour family in CMP98 (15) including the parent paper [2] and bridge choice; compute the *actual* same-background full old/new link difference with its transverse plaquette-chain operator on a legal block, then match CMP99 fluctuation-versus-complete-connection derivatives with a verified background chart. Examine annular Q'_nested ranks and source (3.157)–(3.158) before any covariance constant. Finally return to two independent UV histories, their Ω,V and inherited determinant/E law. A computational local coefficient is not a Yang–Mills theorem.

Highest project bibliography reference [92] preserved; append-only custody and stop maintained.
