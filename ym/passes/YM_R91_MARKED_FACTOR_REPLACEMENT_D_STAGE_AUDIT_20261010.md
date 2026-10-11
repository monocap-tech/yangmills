# YM-R91 — marked factor replacement / native tagged D-stage and covariance motion audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior recorded head: YM-R90 465d8290647a8c8f2647d76b985279731f0275ca
Status: COMPLETE AS ABSTRACT POSITIVE-SERIES AUDIT; NATIVE TAGGED SOURCE GATE OPEN
Next unconsumed cursor: YM-R92
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang-Mills existence, OS reconstruction, or positive mass gap.

## 1. Preflight and exact source boundary

R90 already established a conditional tagged termwise transfer from CMP116-shaped (2.14)/(2.26) majorants through D/P/Z0/Z0' resummation. The unresolved issue is whether a tagged differentiation MULITPLIES an existing epsilon1 factor or REPLACES one. R50's previously source-audited Eq (2.26) contains a product over D-localized activities, each with an epsilon1-type factor, and positive P/weakening/volume factors. R51/R53/R54 previously audited the D-family Cammarota summability, post-P exponent budget, and Lemma-3 endpoint.

The primary publisher abstract of CMP116 [21] states that the Part-I fluctuation integral is expressed as an exponentiated cluster expansion. It does not state the new two-cutoff marked derivative theorem. No authentic primary equation text for CMP109 Eqs (5.37),(5.42),(0.29) was freshly inspected; the candidate positive-alpha source bound from secondary [85] remains unpromoted. Repeated bibliography [7],[21],[59],[85],[87], highest [87], next new [88].

## 2. Exact algebra of a replacement mark — ABSTRACT-DERIVED

Let T_D=R_D prod_(Y in D) w_Y, where R_D encompasses all other source factors and w_Y are baseline local activity factors. For a variation w_Y(t)=w_Y+t r_(x,Y) with the rest R_D fixed, differentiation gives
  d_t T_D = R_D sum_(Y in D) r_(x,Y) prod_(Y' in D, Y'!=Y) w_Y'.
No division by w_Y is used. In particular, if |w_Y|<=epsilon q_Y and |r_(x,Y)|<=u_x q_tag(x,Y), then each marked term carries u_x and |D|-1 powers of epsilon, not |D| powers.

The elementary worst-case scalar model makes the budget transparent. If the absolute n-activity majorant is bounded by K^n epsilon^n, K epsilon<1, replacing any ONE factor yields
  u_x sum_(n>=1) n K^n epsilon^(n-1)
      = K u_x / (1-K epsilon)^2.
Proof: differentiate the geometric sum sum_(n>=1)(K epsilon)^n with respect to epsilon, then multiply by u_x. Strict convergence supplies a finite marked multiplicity cost. No extra epsilon factor is justified.

This scalar identity is NOT a literal transcription of CMP116's D-family sum. To apply it, a source-correct rooted tree/Cammarota marked-family inequality must dominate the real D-indices, their support attachment and the subsequent P/Z0/Z0' sums with sufficient reserve.

## 3. Different species: a new seed versus a replacement

The marked correction may instead enter as an independent factor even when D is empty. Then it creates a new connected source seed Y0_tag including the support of x and must be indexed separately. R45's fixed local support hull suggests the right geometric construction for a bounded-support blocker insertion, but the extra-UV-layer V^(1) input is not yet shown to have the same source carrier and uniformly bounded per-anchor hull.

A pure replacement derivative cannot account for this newly adjoined-seed term because D=empty has no baseline factor to differentiate. Conversely, adding a new seed cannot be assumed equivalent to replacing a D-activity. The primary CMP109-to-CMP116 object dictionary must decide which kind occurs, possibly both.

## 4. Sufficient marked majorant after source indexing

Let I_Z^x denote the source-owned term family contributing to the tagged output H_Z, including replacement and adjoined-seed terms, and M_i^x >=0 be absolute tagged term majorants. Suppose UNIFORMLY in partial input configurations, cutoff/volume and background,
  sum_(i in I_Z^x) M_i^x
     <= C_tag u_x (1+d(Z))^p
        exp[-lambda_tag d(Z)-sigma dist(pi(x),Z)].
Then the actual tagged response obeys the same inequality by the triangle inequality. For any 0<theta<lambda_tag, the polynomial factor can be absorbed into exp(-theta d), giving
  |partial_(t_x)H_Z|
  <= C_tag C_(p,theta) u_x
       exp[-(lambda_tag-theta)d(Z)-sigma dist(pi(x),Z)].
With a separately verified CMP116 metric/cube-tree dictionary this feeds R88/R89. It does NOT require the stronger prefactor h*u_x.

The unresolved SOURCE theorem is exactly the displayed sum-of-tagged-majorants inequality. The previous source unmarked |H(Z)| endpoint and R44 fixed insertion do not verify it for the true CMP109 extra-layer input in all partial environments.

## 5. Moving Gaussian/chart contribution is independent

For a fixed linear localization operator L and G_t=G0 exp(-sum_x t_x v_x), d_t L(G_t)=L(d_t G_t). For a moving L_t, the derivative is
  d_t[L_t(G_t)]=L_t(d_t G_t)+(d_t L_t)(G_t).
The second term may contain covariance, conditioning, cutoff, gauge and source-index changes. It cannot be absorbed into a tagged V^(1) estimate without a new native proof.

For a finite, smoothly varying SPD Gaussian covariance C_t and integrable differentiable F_t, Gaussian integration by parts gives the exact identity
  d_t E_{N(0,C_t)}[F_t]
  = E_{C_t}[d_t F_t]
    +(1/2)sum_(a,b)(d_t C_t)_(a,b) E_{C_t}[partial_a partial_b F_t].
This supplies an explicit candidate for the moving covariance part but does not give its spatial decay or cutoff smallness. The CMP99/CMP116 covariance identity and cross-cutoff comparison remain source-open.

## 6. A potentially weaker alternative to explicit marked-family enumeration

If for each tagged x, with ALL other insertion parameters fixed, H_Z extends holomorphically in t_x to a complex disk centered at each real t_x of radius c/u_x, and is bounded there by h exp[-lambda d(Z)], Cauchy's estimate implies |partial_(t_x)H_Z|<= h u_x exp[-lambda d(Z)]/c. This avoids a global Banach regular-input ball. It does not by itself supply attachment decay from x to Z; that requires source ownership/decay of the tag in the localized term. Uniform analytic extension of the interaction-perturbed CMP116 chart on such disks is NOT source-attested; source field analyticity U^c is a different variable. This is an OPTIONAL sufficient route for YM-R92, not an R91 native closure.

## 7. Sharp negative controls

(i) Extra epsilon smallness is false in general. For T(t)=epsilon+t u_x, d_t T=u_x, which cannot be uniformly bounded by C epsilon u_x as epsilon->0 with fixed C.

(ii) An original D-family with no marked source family cannot detect a new-seed term: H_empty(t)=t u_x has a tag effect but no baseline D factors.

(iii) A bounded unmarked positive sum need not bound derivatives when insertion dependence is not quantitative: H(t)=h sin(t/u) is bounded for real t but has derivative h/u at zero.

(iv) Uniform single-trajectory decay and even a common KP margin do not prove cutoff difference smallness; the actual u_x and moving operator/sector differences must decay after source physical-scale normalization.

## 8. Determination

ABSTRACT-DERIVED: factor replacement derivative and squared-denominator scalar majorant; two distinct mark species; conditional absolute-tagged-positive-resummation transfer; exact moving Gaussian covariance derivative; optional one-coordinate analytic alternative.

SOURCE-LOCATED PREVIOUSLY: CMP116 original unmarked (2.14),(2.26), D/P/Z0/Z0' and Lemma-3 route (R50-R54), single bounded-support RP insertions (R44/R45). Not source-attested: the new cross-cutoff V^(1) marked estimate, replacement/adjoined-seed ownership, moving covariance/gauge effects, or primary Eq (0.29).

OPEN NATIVE: exact CMP109 V^(1) and alpha>0; source differentiated CMP116 term with true tagged index carrier, extra UV root support and absolute majorants; uniform partial-environment control; marginal beta/coupling, large-field/boundary and normalization; full polarization source projection.

NEXT YM-R92 (UNCONSUMED): establish the source-native marked D-family sum by a one-marked version of the already-used Cammarota tree/leaf argument, with the mark REPLACING a baseline epsilon1 factor and allowing a newly adjoined seed. Determine the exact strength of the original CMP116 D/P/Z0/Z0' reserve and whether a one-coordinate analytic parameter method can replace direct index-level marking without assuming a stronger source hypothesis. Continue original CMP109 (5.37),(5.42),(0.29) retrieval and one-layer marginal matching. No native Yang-Mills theorem gate is closed.
