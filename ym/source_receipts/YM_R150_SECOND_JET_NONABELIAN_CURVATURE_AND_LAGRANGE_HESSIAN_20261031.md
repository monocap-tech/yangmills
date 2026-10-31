# YM-R150 — Two-bond mixed constraint jet and constrained-Hessian transfer audit

**Date:** 2026-10-31. **Prior merged HEAD:** 876f26dbd41c68e1f991332aa091c44d1b81abe3. **Custody:** append-only source-facing R150 continuation and exact finite computation. **YM-R150 remains IN PROGRESS / UNCONSUMED**; R149 remains canonical completed pass. No native Gaussian α, paired two-UV law, continuum Yang–Mills or mass-gap theorem.

## 1. Original source and exact evidence boundary

**CMP109 primary original printed image:** T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP109 (1987), printed p253, Eq.(0.4), original paper PDF index4, https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . The revised coarse link is the product of (i) the exponential of the mean logarithm of closed loops made from independent uniformly averaged shortest left/right contour paths, fine straight bridge, and inverse coarse base path, and (ii) the coarse base-path holonomy. Its logarithm can be differentiated at the identity with BCH, on a valid local log branch. Also source printed p267, (2.10)–(2.11), contains the nonlinear coarse-constraint jet with J pairing; p266 (2.7)–(2.8) already absorbs the distinct action jet.

**Original 1985 CMP99 PDF**, user provided; original printed pp392–393 (3.13)–(3.15) were visually rechecked and confirm the fluctuation averaging is analytic and begins with a linear Q_j plus second-order C_j; CMP99 Q_j are composed old one-step averages from [5], i.e. CMP98. Printed p421 (3.127)–(3.129) and p428 (3.155)–(3.158) provide the historical action/variational and old Gaussian interfaces. **CMP98 Eq.(15)** (original-paper THIRD-PARTY transcription at chboishabba/dashi_agda, Docs/support/reference/balaban-source-extracts/cmp98-averaging-operations.txt, printed p19) defines the selected-contour predecessor by an exponential of averaged log loops against an old coarse-link base path. Original CMP98 Eq.(15) equation image was not reverified in this turn. CMP95 original axial path orientation descending d,…,1 appears in its [third-party OCR] and prior R120 source receipt.

**IMPORTANT:** The finite comparison below is exactly between the DECLARED CMP98(15)-style **selected descending contour** plus R120 gauge-endpoint transport and the original CMP109(0.4) uniformly symmetrized **one-step** path map, on an aligned periodic/corner-centered U=1 cell. It is not a full source-certified second jet of CMP99's nested, background-dependent, regional Q_j(U,ηA), and it is not a source-valid Ω/collar Gaussian.

## 2. Exact BCH two-bond second-jet certificate

Choose L=13, fine block B={0,…,12}^4, old corner y=(0,0,0,0), revised center s=(6,6,6,6), and source-aligned coarse e1 link to the neighboring block. The old endpoint frame transport uses descending-axis τ_y and τ_y' as in R120.

Put skew-Hermitian Lie-algebra field X on only the POSITIVELY oriented e2 edge
    p: (1,2,6,6)→(1,3,6,6)
and Y on only the POSITIVELY oriented e3 edge
    q: (1,1,2,6)→(1,1,3,6).
All other fine-link Lie fluctuations are zero, and take [X,Y]≠0 in su(2). Define U_p(t)=exp(tX), U_q(u)=exp(uY). (This convention removes extra i factors from the Hermitian convention used in the printed article.)

The old descending path Γ_y,x traverses its e3 and e2 segments with first-coordinate x1=0 before its final e1 segment, so neither p nor q (which have x1=1) occurs. The old right path, e1 bridge, coarse base path and both descending endpoint-transport legs also miss them. Hence the transported selected-path old coarse holonomy is identically 1 for this two-bond family.

For the revised CMP109 left shortest path s→x to encounter both links, x1=x2=1, x3∈{0,1,2}, and x4∈{0,…,12}; it must traverse e1 then e2 then e3 before e4 (if e4 is active). If x4≠6, one of 24 four-axis permutations is eligible; if x4=6, one of six 3-axis permutations is eligible. Exactly **39 endpoints** enter, and the total shortest-path average weight is
    w=3*(12/24 +1/6)=2.
Every such path crosses the positive edges in NEGATIVE orientation, so the supported path factor is exp(-tX)exp(-uY). Its log has mixed tu coefficient +(1/2)[X,Y]. The right paths, bridges and base path never meet p or q; the endpoint-permutation averages factor out.

Thus in local logarithmic coordinates at U=1:
    ∂t∂u log M_109(U(t,u),c)|0 = (w/(2L^4))[X,Y]
                                = (1/28561)[X,Y],        (R150.MJ1)
whereas
    ∂t∂u log M_98^τ(U(t,u),c)|0 = 0.                   (R150.MJ2)

This exact, nonzero **mixed Hessian difference on a declared one-step aligned model** is reproducibly enumerated with rational weights in [certificate](../computations/YM_R150_BCH_MIXED_SECOND_JET_L13_20261031.py). A path-level commutator is the direct source of the mixed jet. No numeric positivity bound follows.

If all fields lie in the SAME abelian one-parameter subalgebra, every path product and coarse exponential is the exponential of a LINEAR sum of link variables near the identity, so **both second jets vanish there**. Earlier one-color scalar coefficient tests cannot detect this non-Abelian constraint-curvature contribution. This does NOT imply that non-Abelian mixed jets cancel after source gauge, Ω/collar or multiplier contractions.

## 3. Correct nonlinear transport and constrained-Hessian combination

**Abstract derivation, only if actual finite source charts exist:** Let F_o,F_n:E→Y be smooth constraints at a common zero with first derivatives D_o,D_n and second derivatives B_o,B_n. Let a proposed nonlinear transport be
    T(x)=Sx +(1/2)T_2(x,x)+O(||x||³)
with D_o S=D_n. Chain rule yields the **exact 2-jet compatibility condition**
    B_n[u,v]=B_o[Su,Sv]+D_o T_2[u,v].                 (R150.MJ3)
Therefore matching linear constraints alone does not match their second jets. When D_o has a chosen right inverse h_o, the formal candidate
    T_2[u,v]=h_o(B_n[u,v]-B_o[Su,Sv])
solves (R150.MJ3) algebraically, but need not respect gauge covariance, actual regional support/collars, locality, source cutoff or measures. **The finite commutator witness is not a general obstruction to the existence of a nonlinear reparametrization.**

Let a smooth action S_phys have gradient j=D*λ at a constrained critical point F=0 and choose any local constrained chart b(x)=Cx+(1/2)b_2(x,x)+…, with DC=0, Db_2[u,v]=-F''[Cu,Cv]. Then exact differentiation gives the **constrained Hessian**
    D²(S_phys∘b)[u,v]
     = S_phys''[Cu,Cv] - <λ,F''[Cu,Cv]>.             (R150.MJ4)
The two pieces can shift under nonlinear coordinate changes, while their total on the true constrained manifold is the invariant quantity. This is the abstract geometric interpretation of CMP109 (2.11)'s constraint-straightening correction. It does NOT give an identification of the 1985 and 1987 physical action/gauge domains.

**At U=1:** original Wilson-action J(1)=0 implies the associated CMP109 source λ=0 on any legally matched surjective chart. Therefore the *J-weighted* constraint-jet contribution is zero even though (R150.MJ1) is nonzero. The mixed jet discrepancy alone does not prove K_new−K_old≠0 or failure of historical coercivity. At nonidentity constrained backgrounds λ need not be zero.

## 4. Typed stop / next qualifying calculation

**Verified:** source CMP109 (0.4) path-averaging structure, original CMP99 (3.13)–(3.15) analyticity and old ancestry; exact nonzero SU2 mixed second jet for the declared one-step old selected versus new symmetrized path comparison; commutator-only/abelian null phenomenon; exact second-order chain rule and constrained-Hessian formula. **Unverified:** full CMP99 nonlinear Q_j(U) source regional second jet, old/new second-jet transport on one actual Ω/Λ, target space identification, source multiplier sizes, numerical Hessian coercivity and interaction/partition normalization.

**Next source gate within YM-R150 (UNCONSUMED):** exhibit a legal shared source Ω/collar and actual full CMP99 and CMP109 nonlinear constraints, compute their **second derivatives with all background transports** and the associated multiplier pairings after the required source gauge/cutoff chart; verify the *whole constrained Hessian* on the same space or bound its residual. Do not use the displayed nonzero mixed jet as a source physical-Hessian defect without J and C. R149 canonical checkpoint unchanged. Claim UNPROVED_RESEARCH_PROGRAM.
