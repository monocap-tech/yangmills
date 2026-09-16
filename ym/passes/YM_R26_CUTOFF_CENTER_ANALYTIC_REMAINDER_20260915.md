# YM-R26 — cutoff-center analytic remainder / one-step activity closure

Date: 2026-09-15
Status: COMPLETE
Claim discipline: UNPROVED_RESEARCH_PROGRAM; derivations below are local weak-field calculations, not a proof of 4d Yang–Mills.

## Target

For the global cutoff center from YM-R25,

C_e(U)=U_0 exp(sum_j w_j phi(U_0^{-1}U_j)),

with phi=log on the regular chart, compute the local analytic jet and determine whether the single-center heat-kernel blocker differs from the Bałaban Gaussian block factor by an analytic O(g_k) local term on a fixed complex tube.

## 1. Path-log expansion

On the regular chart write each fine path holonomy as

L_j(A;g):=log U_j = g X_j(A) + g^2 Y_j(A) + O(g^3),

where X_j=P_j A is the linear path integral and Y_j is the quadratic BCH/path-ordering term. For a finite path built from exp(g A_b), Y_j is a finite sum of Lie brackets of bond fields on that path. On a fixed complex ball, all derivatives of X_j,Y_j and the higher Taylor remainder are bounded by constants depending only on the fixed block/path geometry and the analytic radius, not on the RG step k.

Define Q A = sum_j w_j X_j(A) and Ybar(A)=sum_j w_j Y_j(A).

## 2. Anchor-commutator cancellation

For R_j=U_0^{-1}U_j,

log R_j = g(X_j-X_0) + g^2(Y_j-Y_0 - (1/2)[X_0,X_j]) + O(g^3).

Hence

S:=sum_j w_j log R_j
 = g(QA-X_0) + g^2(Ybar-Y_0-(1/2)[X_0,QA]) + O(g^3).

Since C=exp(L_0)exp(S), BCH gives

log C = L_0+S+(1/2)[L_0,S]+O(g^3)
      = g QA + g^2 Ybar + O(g^3).

The anchor-dependent commutators cancel at order g^2. Therefore the nonlinear center defect satisfies, on the fixed regular complex tube,

N_g(A):=log C(e^{gA})-gQA = g^2 Ybar(A)+O(g^3),

and for every fixed derivative order n,

sup_{A in D_R} ||D^n N_g(A)|| <= C_{n,R} g^2

for sufficiently small g. The cutoff chi is identically one on this tube once g is small enough, so it does not enter these Cauchy estimates.

## 3. Heat-kernel relative coordinate

Write the coarse variable V=exp(gB). Let D=B-QA. Then

W:=log(V C^{-1})
 = gD + g^2 Z_2(A,B)+O(g^3),

with

Z_2 = -Ybar(A) - (1/2)[B,QA].

For an Ad-invariant inner product,

<D,[B,QA]>=0.

Thus

||W||^2 = g^2 ||D||^2 - 2 g^3 <D,Ybar(A)> + O(g^4).

Take heat time t=g^2/a (up to the fixed convention-dependent heat-kernel normalization). The principal exponential becomes

exp[-||W||^2/(2t)]
 = exp[-(a/2)||D||^2] * exp[g a <D,Ybar(A)> + O(g^2)].

The compact-group heat-kernel Jacobian/curvature factor is analytic and equals 1+O(g^2) on the same fixed scaled tube. Therefore the exact single-link kernel factor admits

K_e = K_{e,Gauss} * exp[g F_{3,e}(A,B)+O(g^2)],

where

F_{3,e}(A,B)=a <B-QA, Ybar(A)>

up to the fixed heat-kernel convention. F_{3,e} is a local analytic cubic polynomial in canonical fields. In the Abelian case Ybar=0, so this O(g) term vanishes.

## 4. Uniform analytic bound

Because each block uses finitely many paths of bounded length (L fixed in the RG design), products over the finitely many coarse links in one local block preserve the estimate. On a fixed complex canonical-field tube D_R,

K_block/K_Gauss = 1 + E_g,

with

sup_{D_R} |E_g| <= C_R g,

and, for each fixed derivative order n,

sup_{D_R} ||D^n E_g|| <= C_{n,R} g.

Thus the preferred RP blocker is a genuinely small analytic perturbation of the Bałaban Gaussian reference factor in the asymptotically free regime.

## 5. Marginal caution

The O(g) cubic term has the same canonical field order as the Yang–Mills cubic vertex. It must not be classified as irrelevant solely from field degree. However, the blocking correction has zero quadratic soft-hard defect at this stage (the Hessian remains M+a Q^*Q), so there is no independent tree-level F^2 displacement forced by this center correction. Any Wilson-action/coupling shift generated after integrating fluctuations must still be extracted using the YM-R21 local coupling coordinate.

## 6. Source-shaped closure status

Bałaban Part II proves that the fluctuation integral is represented by an exponentiated cluster expansion whose terms satisfy the inductive assumptions; the source-extracted Lemma 3 / CMP116 Eq. (2.38) gives the localized H(Z) exponential tree-distance bound. The present derivation establishes the missing *input-sized* statement for the new blocker: before nonlocal propagator/minimizer insertion, the new raw local factor is analytic and O(g_k) on the fixed complex tube.

What is not yet proved is that adding this O(g_k) factor to Bałaban's raw interaction fits the precise epsilon_1/Cauchy budget and survives the weakening-parameter/generalized-random-walk localization with constants that feed CMP116 Lemma 3.

## Determination

YM-R26 closes the local analytic-jet obligation positively:

boxed: C(e^{gA}) = exp(gQA + g^2 Ybar(A)+O(g^3))

and

boxed: K_soft/K_Gauss = 1+O(g)

uniformly in fixed-order analytic derivatives on the regular fixed complex tube.

The next frontier is no longer the center construction or heat-kernel local asymptotics. It is the source-level smallness-budget insertion:

YM-R27 — epsilon_1 / localization-budget audit.

Questions:
1. What exact smallness power/function of g_k is epsilon_1 in Bałaban Parts I-II?
2. Can the added O(g_k) analytic local factor be absorbed into that raw activity class after Wilson-action extraction?
3. Does its finite initial support plus existing propagator random-walk localization yield the same H(Z) exponential bound with a modified constant C_3?
4. Are any additional cancellations needed to improve O(g_k) to the source-required power?

No new reference number consumed; next new source remains [76].