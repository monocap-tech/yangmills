# YM-R92 — one-marked rooted tree/Cammarota and ghost-seed polymer comparison

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior checkpoint: YM-R91 edfc40c6339e152866eb69250d9ae83eb3f5bd7a
Status: ABSTRACT MARKED REPLACEMENT AND GHOST-SEED TRANSFER DERIVED; CMP116 NATIVE TAG SOURCE OPEN
Next cursor: YM-R93 (unconsumed)
Claim: UNPROVED RESEARCH PROGRAM, no continuum 4D Yang–Mills construction, OS reconstruction or mass gap.

## 1. Source accounting: distinct D and connected-log summability layers

The repo R50/R51/R53/R54 source audits establish CMP116 [21]: (2.14) original D/P/Z0 term, (2.26) absolute unmarked majorant, (2.29) rooted D-family summation using modified Cammarota [80] theorem 2, (2.31) P-family entropy, (2.32)-(2.37) later resummation, (2.38) H(Z), then (2.39)-(2.41) exponentiation. R91 showed that marking a D-factor REPLACES one original epsilon1 factor, not necessarily multiplies it, and an adjoined seed can occur with D empty.

Original Cammarota [80] general polymer Mayer theorem is a source-used tree/leaf convergence control; KP [87] proves generic hard-core connected-log convergence, with an explicitly stated weighted theorem in Cannon–Helmuth–Perkins (CMP 2026, Theorem 4.2, DOI 10.1007/s00220-026-05623-3). The two are mathematically related but are NOT the same source Eq(2.29) summand, and the KP theorem is not a native CMP116 marked derivative. A fresh primary Bałaban CMP109 Eq(0.29) page transcription was not obtained; Rutgers/publisher abstract attests beta functions and small-field one-step construction only. [85]'s alpha>0 wording stays SECONDARY. No new numbered source; highest [87].

Quantifier caution in older R51: a positive D-family bound <=1 cannot apply to an unrestricted family including empty D plus positive nonempty families. It must be read with its actual fixed-nonempty-Y0/source-constrained index; do not promote an unqualified full-powerset inequality. This does not undermine the older finite rooted animal count but matters for tagged differentiation.

## 2. One-marked replacement theorem in abstract hard-core cluster language

Let P be finite connected cube-polymers Y in Z4, with usual overlap/adjacency incompatibility, and common holomorphic weights w_s(Y,b) for any partial insertion environment s, on one common background polydisc. Assume sup_(s,b)|w_s(Y,b)|<=p_Y. For nu>0 set
 T_(nu,p)(Y)
 = sum_(n>=1) 1/(n-1)! sum_(Y2,...,Yn)
   |phi_T(Y,Y2,...,Yn)| product_(j>=2)[p_(Yj) exp(nu|Yj|)].
Assume a ROOTED weighted cluster susceptibility bound T_(nu,p)(Y)<=exp(a|Y|), uniform in cutoff and volume, for some a>=0. This follows from a sufficiently strong compatible weighted KP margin but is NOT inferred from CMP116 Eq (2.29) merely saying the unmarked sum is <=1.

Suppose one tagged input at microscopic/coarse root x changes the ordinary polymer weight with
 |r_x(Y)|=|partial_(s_x)w_s(Y)|
   <=u_x exp[-lambda_m |Y|-sigma dist(x,Y)],
uniformly over all other insertion settings, with lambda_m,sigma>0.

Differentiating the absolutely convergent connected-log cluster series marks one factor. Exchange symmetry cancels n/n!, giving the coefficient 1/(n-1)! and an exact expression
  partial_(s_x) log Xi(w_s)
  =sum_Y r_x(Y) sum_(n>=1) 1/(n-1)! sum_(Y2,...,Yn)
       phi_T(Y,Y2,...,Yn) product_(j>=2)w_s(Yj).
There is no division by a possibly zero w_s(Y) and no extra baseline epsilon1 factor.

For any z in the marked polymer Y, dist(x,z)<=dist(x,Y)+|Y|-1. Select 0<theta<=sigma and let
  t=exp[-(lambda_m-a-nu-theta)],
  q=C_ent*t<1,
where the animal count for connected n-cube Y containing fixed z is <=C_ent^(n-1). Then the absolute marked CONNECTED-LOG contribution rooted at z, with exp(nu|Y|) reserve for the polymer-union size, is bounded by
  u_x exp[-theta dist(x,z)] * t/(1-q).
Proof: multiply the derivative bound by exp((nu+a)|Y|), spend theta of distance/size to extract exp[-theta dist(x,z)], then sum the geometric animal series. The attached unmarked cluster part is already accounted for by T_(nu,p).

Hence one rooted replacement mark costs O(u_x), has positive x-to-z decay and needs only a strict entropy-versus-decay margin. No invented extra epsilon1 factor is present. This is a GENERAL hard-core linked-cluster theorem under the stated assumptions, not a source-certified CMP116 D/P/Z0/Z0' marked bound. The choice of z and physical source-cube metric still needs native identification.

## 3. Independent marked seed: exact ghost-polymer identity

Let Xi(w)=sum over compatible subsets of ordinary hard-core polymers product of w(Y). Adjoin an OPTIONAL one-use ghost g_x with activity v_x and declared compatibility relation to ordinary polymers (typically incompatible with ordinary Y meeting a fixed support halo of x). Then EXACTLY
  Xi_aug = Xi(w) + v_x Xi_compatible(g_x)(w).
If Xi and Xi_compatible are nonzero in the common complex domain, set R_g=Xi_compatible/Xi and obtain
  log Xi_aug-log Xi = log(1+v_x R_g),
on a coherent log branch.

Assume an independent connected-cluster/rooted-g bound gives
  |log Xi_compatible-log Xi|<=A_g,
uniformly in the complex background and partial insertion settings. Then |R_g|<=exp(A_g). If |v_x|exp(A_g)<1,
  |log Xi_aug-log Xi|
  <= -log(1-|v_x|exp(A_g)).
For |v_x|exp(A_g)<=1/2 this is <=2 exp(A_g)|v_x|: one small mark, not epsilon1*v_x. The existing weighted KP theory can provide A_g when the ghost incompatibility-neighborhood and ordinary activity sums obey its condition, but R51's unmarked D-stage bound does NOT automatically do so.

IMPORTANT LIMIT: this ghost identity controls a global log-ratio. It does not on its own establish that the *localized* CMP116 H(Z) derivative is spatially attached to x with rate sigma>0. That needs a source-correct localization of ghost-connected clusters, including the D-empty seed and weakened covariance paths.

## 4. Exact gap between general combinatorics and native CMP116

To apply R92, the source must supply:
(1) A common physically aligned CMP116 hard-core polymer carrier for two UV depths, with fields/gauge/conditional Gaussian chart and source coupling matched, or an explicit moving-chart defect term.
(2) A source-owned tagged D-activity r_x(Y) or new-seed weight v_x, with quantitative O(u_x) bounds in the complex source collar, and real x-to-Y or ghost-to-Z tree attachment.
(3) Uniform rooted weighted KP/Cammarota margins for ALL partial insertion environments, with correct C_ent, source d_k metric, epsilon1 replacement and D-index convention.
(4) Tagged P,Z0,Z0' resummation using a POSITIVE marked majorant; the generic rooted connected-log proof does not commute automatically with those source steps.
(5) Original CMP109 (5.37),(5.42),(0.29), precise V^(1) definition, sign, normalization, alpha>0, actual first-layer identification; also marginal beta/coherent coupling, R/B boundary/large-field and complete polarization source projection.

No source text presently identifies original Eq (0.29) with the new tagged input u_x or proves u_x=O(a_N^(4+alpha)). R70 conditional four-dimensional counting remains a CONDITIONAL scaling implication only.

## 5. Rejected shortcuts and next cursor

- CMP116 Eq(2.29) unmarked <=1 and its Cammarota proof do NOT control insertion derivatives at fixed x. A family of bounded holomorphic endpoints can have unbounded insertion derivatives absent an input radius or direct tagged activity estimate.
- A replacement mark cannot capture a fresh tagged seed when D is empty; the ghost construction is an explicit alternative abstract index.
- A ghost-marked partition ratio is not itself CMP116's pre-exponent H(Z) tagged localization.
- A fixed coupling/source chart leaves open real cross-cutoff changes of covariance and gauge measure, whose derivative was separated in R90/R91.
- Do not claim R92 closes native Yang-Mills tagged estimates, UV irrelevance or a continuum mass gap.

ABSTRACT DERIVED: rooted one-marked hard-core log-cluster transfer with explicit animal-series constant and spatial decay; ghost seed exact partition ratio and uniform log estimate.
SOURCE-CITED: general Cammarota [80] and KP [87] frameworks; prior CMP116 unmarked source extraction R50-R54.
OPEN NATIVE: native one-marked D-family index/root and quantitative majorant, P/Z0/Z0' tag preservation, actual CMP109 Eq(0.29), coupling/sector transport, full beta/F2 response.

NEXT YM-R93 (UNCONSUMED): choose whether the *source* tagged CMP116 object should be differentiated at its D-family activity input or inserted before conditioning as a new seed; obtain exact seed/index and weakening-root ownership for each. Try to reconstruct the primary CMP109 Eq(0.29) from a verified full-text source before adding more generic transfer theorems. Where source access remains blocked, stop deriving increasingly conditional variants and report the source/type bottleneck concretely.
