# YM-R83 — product-Gaussian interaction insertion / two-source cumulant and rooted moment audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior head: YM-R82 checkpoint e2514428977478a8321f26b4dd8cfc8774499271
Status: COMPLETE as abstract theorem and source-frontier audit; native R75 gates OPEN
Next cursor: YM-R84 (unconsumed)
Claim status: UNPROVED RESEARCH PROGRAM; no 4D continuum Yang-Mills or positive mass gap.

## 1. Source recovery and boundaries

R82 used the previously source-extracted CMP116 [21] product Gaussian coordinate change B'=(C^(k))^(1/2)X after conditioning in Bałaban's one-step fluctuation integration. Rechecked project YM-R42/R43: the resulting dmu0(X) is normalized; C^(k)(Z0), root, and Delta_k remain separately typed, and the source proof localizes H(Z,Z0) and H(Z), not an exact finite root-piece reconstruction.

Rechecked YM-R44/R45: an inserted fixed-support analytic O(g_k) factor is compared by an interpolation of CMP116 localized activities, with an O(g_k) exponential decay estimate conditional on uniformity of the same source weakening/localization bounds along interpolation and the fixed-source support anchor. The current R83 cross-CUTOFF comparison is NOT this O(g_k) single-step insertion theorem. It requires a summable extra-UV or aligned-defect norm with external derivatives, and cannot inherit that exponent or the required positivity/analyticity from R44 alone.

Primary CMP109 [7] article metadata confirms the four-dimensional small-field one-step scheme but original Eqs (5.37),(5.42),(0.29) and definitions were not directly recovered. Secondary [85] remains a locator only. Original CMP116 Eq 2.5-2.41 details are attributed to previous source-audited R42-R45 and [21], not freshly certified as cross-cutoff statements. No new source; highest bibliography item remains [86].

## 2. Exact two-source interaction response — ABSTRACT-DERIVED

Let mu0 be a FIXED normalized probability Gaussian on a finite real space, with background sources b_x. Let W_i(b,X), K_i(b), i=0,1, be real sufficiently smooth functions with integrability and dominated derivatives. Set
 Z_i(b)=int exp(-W_i(b,X)) dmu0(X)>0,
 Gamma_i(b)=K_i(b)-log Z_i(b).
Define D=W1-W0, W_s=W0+sD, Z_s=int exp(-W_s)dmu0 and tilted normalized expectation <F>_s.

The interpolation derivative is
  partial_s Gamma_s = Delta K + <D>_s
for K_s=K0+s DeltaK.

For source coordinates x,y, use
  partial_x <F>_s = <F_x>_s - Cov_s(F,W_(s,x)).
Differentiating once more and using the third joint cumulant yields the EXACT identity
  Delta Gamma_xy = Delta K_xy
    + int_0^1 ds [
         <D_xy>_s
         - Cov_s(D_x,W_(s,y))
         - Cov_s(D_y,W_(s,x))
         - Cov_s(D,W_(s,xy))
         + kappa3_s(D,W_(s,x),W_(s,y))
      ].
All derivatives refer to external background variables in the same identified chart. The third cumulant is <ABC>-<AB><C>-<AC><B>-<BC><A>+2<A><B><C>.

Proof: the first derivative identity follows from the quotient rule for normalized tilted expectations. Apply it to <D_x> and to Cov(D,W_(s,x)), giving the displayed second derivative. Integrate s. This is a finite-dimensional identity; it does not assume Gaussian covariance stationarity because source-root differences are represented in W_i only after a JUSTIFIED common product chart. Any b-dependent transport Jacobian not included in mu0 belongs in W_i or K_i by the exact source measure dictionary.

For complex analytic source contours the same identities hold on a common domain only where every Z_s is nonzero, logs are coherently chosen, and dominated analytic differentiation is justified. Positivity Z_s>0 holds for real W_s on real fields, NOT automatically for complex W_s.

## 3. Rooted connected-response criterion — ABSTRACT-DERIVED CONDITIONAL IMPLICATION

On finite subsets of Z^4 with l1 metric, suppose D_N=sum_z D_(N,z). By linearity in D (and its derivatives), let F_(N,z)(x,y) denote the corresponding five-term s-integrated response from the preceding formula.

Assume a UNIFORM rooted connected-correlation bound
  |F_(N,z)(x,y)| <= A epsilon_N exp[-kappa(|x-z|_1+|y-z|_1)]
with constants A,kappa>0 independent of N, volume and x,y. This is a strong two-source response hypothesis, not something CMP116 is presently shown to supply. Suppose separately
  sup_x sum_y |x-y|_1^2 |Delta K_(N,xy)| <= k_N.
Then
  sup_x sum_y |x-y|_1^2 |Delta Gamma_(N,xy)|
     <= k_N + 4 A S0(kappa) S2(kappa) epsilon_N,
where S0=sum_(u in Z4) exp(-kappa|u|_1) and
      S2=sum_(u in Z4) |u|_1^2 exp(-kappa|u|_1).
Both sums are finite.

Proof: substitute q=z-x, r=y-z; |y-x|_1^2<=2(|q|_1^2+|r|_1^2) and sum the factorized exponential over q,r. The resulting bound is 4 S0 S2. Restriction to finite volumes only decreases the sum.

If sum_N(k_N+epsilon_N)<infinity, the aligned response defects are summable in this second-spatial-moment norm. With an independently verified source tensor/Fourier/marginal dictionary and uniform conversion constants, R77 then gives a summable beta-type extraction. No native CMP109 full-Pi theorem is claimed here.

This criterion uses already normalized ROOT coordinates. At microscopic spacing a_N, physical-to-lattice momentum factors, the density of N-dependent anchors (order a_N^-4 in 4D), and any polymer entropy must be restored by a source-verified normalization before applying it to a physical cutoff comparison. A hypothetical per-UV-root O(a_N^(4+alpha)) with alpha>0 leaves O(a_N^alpha) only if the source root counting and support dictionary actually apply. The Eq (0.29) bound and first-common-scale identification still require original-page verification.

## 4. Analytic derivative and zero-free gates

REAL-SMALLNESS COUNTEREXAMPLE: f_n(b_x,b_y)=n^-2 sin(n b_x)sin(n b_y) satisfies sup_{real b}|f_n|<=n^-2, but partial_xy f_n(0)=1 for all n. Thus an H(Z) amplitude bound on real b does NOT control the polarization second derivative. Under a FIXED complex bidisc radius r and sup |f_n|<=epsilon_n, two-variable Cauchy gives |partial_xy f_n(0)|<=epsilon_n/r^2 instead. Native uniform complex collar and analytic estimates (including the R36 embedding gate) are essential.

COMPLEX-INTERPOLATION COUNTEREXAMPLE: let Y be a symmetric standard Gaussian and W_s(Y)=i pi s tanh(kY). Then Z_s=E[cos(pi s tanh(kY))] is real continuous with Z_0=1. For large k, Z_1 approaches -1 by dominated convergence, so Z_1<0 and some intermediate s has Z_s=0. The endpoints are nonzero and W_s is smooth and bounded in real Y, yet log Z_s cannot be differentiated along the entire complex-valued interpolation. An explicit uniform nonvanishing/cluster-exponentiation argument is therefore needed for complex source applications.

UV-SUMMABILITY COUNTEREXAMPLE: a fixed-support analytic difference D_N=(1/N)b_x b_y (constant in X) has response defect 1/N. Every step is localized and each defect tends to zero, but the absolute UV sum diverges. CMP116 locality plus O(g_N) does NOT establish the required epsilon_N summability without source-native extra scale decay or cancellation.

## 5. Native source consumer and exclusions

To consume R83 in Bałaban's actual construction, verify:
(A) the source-native CMP116 product-Gaussian chart and a cross-cutoff conditioning/extra-shell map, with all source normalizations;
(B) W0,W1,K0,K1 in ONE aligned physical chart and the exact background/tensor source projection, including the root/measure dependence;
(C) the interpolation remains in the primary complex admissible domain and has nonvanishing partition functions;
(D) uniform analytic/cumulant insertion estimates connecting an ultraviolet defect anchored at z to TWO external background insertions x,y (not merely a single localized H(Z) bound);
(E) a genuinely summable epsilon_N, proper UV anchor count, and independent k_N counterterm budget;
(F) original CMP109 (5.37),(5.42),(0.29), exact V^(j), positive-alpha norm and the first-common-scale one-layer correspondence.

CMP116 is known to produce localized one-step cluster activities under its assumptions; this alone does not prove (A)-(F). The previous R44 soft-blocker O(g_k) insertion has a different comparison geometry. Exact Schur theorem Lean UUID [86] remains separate and non-load-bearing for this frontier.

ABSTRACT-DERIVED: exact two-source tilted cumulant identity; rooted second-moment implication; real-derivative and complex-zero counterexamples.
PREVIOUS SOURCE-LOCATED: CMP116 product Gaussian, localization and H(Z) architecture [21], R42-R45.
CONDITIONAL NATIVE: uniform two-source connected-response estimate plus actual scale/root count and full beta projection.
OPEN PRIMARY/NATIVE: CMP109 original Eq windows, Eq(0.29), cross-cutoff source chart, non-Gaussian derivative localization and ultraviolet summability.

Next YM-R84 (UNCONSUMED): pursue CMP116 Lemma 3/H(Z) analytic source norms and two-marked insertion/derivative stability; identify the minimum primary estimate for a cross-cutoff ultraviolet insertion that pays a^{4+alpha} after fixed volume root counting. Verify interpolation zero-freeness and the source Cauchy collar; separately seek genuine original CMP109 (5.37),(5.42),(0.29) and the exact first-common-scale V^(j) dictionary. No native Yang-Mills obligation closes in R83.
