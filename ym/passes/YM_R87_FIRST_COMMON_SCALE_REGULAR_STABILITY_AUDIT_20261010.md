# YM-R87 — first-common-scale V^(1) comparison / analytic activity stability and missing-sector audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior head: YM-R86 9c3bfec3392832e5dc2c65a1d9149b02e8740fed
Status: BOUNDED ABSTRACT THEOREMS AND NEGATIVE NATIVE SOURCE AUDIT COMPLETE; original R75 gates OPEN
Next unconsumed cursor: YM-R88
Claim discipline: UNPROVED RESEARCH PROGRAM; no 4D continuum Yang-Mills or positive mass gap.

## 1. What R70 actually identifies at the first common scale

Return to R62/R65/R66/R70, not just R85/R86. With microscopic eta_N=L^(-N) and a_(N,j)=L^(j-N), the finer theory's first blocked scale equals the coarser bare scale:
  a_(N+1,1)=a_(N,0)=L^(-N).
This is an exact indexing identity only.

CMP119 (2.24)-(2.25), source-audited in R65/R70, separately stores the vacuum subtraction, Wilson marginal beta_j A subtraction, and source-labelled regular E^(j) history. At first common scale the prospective difference of complete density/action has schematically:
  DeltaAction_N = c_N*1 + m_N*A + v_N + q_N,
where v_N is the first-layer regular remainder ONLY after the CMP109 native source convention has been verified; q_N contains boundary/large-field, gauge/measure, other residual and transport effects. Vacuum c_N can cancel in normalized ratios if the measures and charts match. The marginal coefficient m_N and q_N do not cancel merely because physical spacings match.

Source [85] points to a *candidate* CMP109 Eq(0.29) bound with per source root scale a_N^(4+alpha), alpha>0, but the original Eq (0.29), its exact V^(j) definition, sign and quantifiers still have not been inspected in this environment. The publisher/Rutgers records attest the paper and the small-field beta-function architecture, not this exact bound. No change in source custody: [7],[21],[59],[85],[87] reused; no new reference; highest [87].

## 2. Analytic one-step activity transfer — ABSTRACT-DERIVED

Let B be a complex Banach space of regular/irrelevant source inputs, and A a Banach space of exponentially weighted polymer activities with norm ||.||_A. Fix coupling, gauge chart, background and other sector coordinates, including the common physical carrier.

Suppose the exact one-step activity assignment F:B(0,rho)->A is Frechet holomorphic and satisfies
  sup_{||v||_B<rho} ||F(v)||_A <= h
with h,rho>0 UNIFORM in UV depth and volume. For two inputs v0,v1 with ||v_i||<=rho/2, let D=v1-v0. On any segment v_t=v0+tD, the complex line v_t+z D/||D|| remains in the radius-rho ball for |z|<rho/2. Vector-valued Cauchy gives
  ||DF(v_t)[D]||_A <= (2h/rho)||D||_B.
Integrate t:
  ||F(v1)-F(v0)||_A <= (2h/rho)||v1-v0||_B.
The same estimate holds for a chosen component's weighted activity norm if F is uniformly bounded in that norm. This derives a source-input -> polymer-output Lipschitz bound from holomorphy, rather than postulating an arbitrary stable-fiber theorem.

The hypothesis is NOT furnished merely by CMP116's analyticity in the external field U^c. One needs a common analytic BALL in the *regular-input* coordinate and a uniform output majorant when the inserted source action varies on that ball. Different cutoff carriers require source conditioning/transport before F can be treated as a common map.

If an actual source dictionary identifies v0=0 and v1=V_N^(1), and a primary theorem yields ||V_N^(1)||_B<=b_N, then its regular contribution obeys
  ||Delta w_N||_A <= (2h/rho)b_N,
provided the other channels are exactly matched. This is a CONDITIONAL NATIVE TRANSFER, not a source theorem.

## 3. A second exact stability lemma directly in normalized local Gaussian coordinates

Let mu0 be a fixed normalized real Gaussian, and W0(b,y) holomorphic in external source b on a radius-r polydisc such that Z0(b)=int exp(-W0) dmu0 is holomorphic and nonzero. Let d(b,y) be a source perturbation holomorphic in b and uniformly bounded |d|<=epsilon over all y and b. Write
  Z1(b)=int exp[-W0(b,y)-d(b,y)] dmu0(y).
Assume
  Q=sup_b [int |exp(-W0(b,y))| dmu0(y)]/|Z0(b)| < infinity.
Then
  |Z1/Z0 -1| <= Q(exp(epsilon)-1) =:q.
If q<1, the ratio has a common holomorphic log and
  |log(Z1/Z0)| <= -log(1-q).
For any two distinct external coordinates x,y, Cauchy's estimate at the center gives
  |partial_x partial_y log(Z1/Z0)(0)| <= [-log(1-q)]/r^2;
for repeated x=y use 2[-log(1-q)]/r^2.
For REAL W0,d the normalized positive tilted law has Q=1 and the stronger bound |log(Z1/Z0)|<=epsilon pointwise on real sources.

PROOF: Z1/Z0-1 is the tilted expectation of exp(-d)-1, bounded in absolute value by Q(exp(epsilon)-1). The disk of radius q<1 about 1 avoids zero, so the holomorphic logarithm and the stated sup bound follow from the power series; apply bidisc Cauchy.

This is an exact finite-integral control for one bounded inserted potential. It is NOT volume-uniform without a source bound on Q, and a global sum over O(a_N^-4) insertions need not have ||d||_infinity small even when each per-root activity is tiny. To control a growing polymer family, the anchored/KP estimates of R85/R86 are the appropriate consumer.

## 4. Counterexamples identify indispensable matching and radius hypotheses

A. Residual V=0 while marginal mismatch persists. Let a source background coordinate b have Wilson-model quadratic A(b)=b^2. Compare normalized actions S0=0 and S1=lambda b^2. Both have zero *complementary* regular residual after designated marginal extraction, yet the second background response differs by 2 lambda. Hence a V^(1) norm bound, even V^(1)=0, cannot control the full cross-cutoff polarization without marginal/counterterm alignment. This is a generic mathematical counterexample, not a native Bałaban counterexample.

B. Shrinking source-input analytic radius destroys perturbation smallness. Put rho_N=L^-N(4+alpha) (a positive number) and define F_N(v)=h v/rho_N for |v|<rho_N, uniformly bounded |F_N|<=h there. Choose v_N=rho_N/2->0. Then |F_N(v_N)-F_N(0)|=h/2, not vanishing. Thus a per-source small V bound cannot be propagated to a small activity difference solely by scale-dependent analyticity; rho must be uniform in the appropriate *normalized* input norm, or a quantitative derivative bound must replace it.

C. Even if the marginal coefficients are matched, another sector q_N=lambda b^2 or a change in chart normalization can produce an O(1) external response while V=0. The complete E/R/B/source measure comparison must remain separated.

## 5. Correct four-dimensional scale bookkeeping

At first common scale a_N=L^-N the candidate per microscopic-root bound would be O(a_N^(4+alpha)). A fixed 4D physical region contains O(a_N^-4) such roots, so its total contribution is O(a_N^alpha), geometrically summable for alpha>0. This is CONDITIONAL on the norm, rooted combinatorics, source-scale metric, and physical normalization.

R86's act_eps_N is instead the activity-difference prefactor in a common CMP116 output norm. It cannot be identified with a_N^(4+alpha) or a_N^alpha until the exact source-to-output map, changes of lattice coordinate and anchor count are shown.

There is also no extra geometric factor on the SHARED shifted tail: a_(N+1,j+1)=a_(N,j) exactly, per R70. Only the genuinely additional fine layer can supply a new suppression factor.

## 6. Current theorem chain and native obligations

Mathematically sufficient route, with every arrow separately conditioned:
  Original CMP109 first-layer remainder bound b_N
    + exact marginal/vacuum/source-gauge matching
    + common holomorphic regular-input ball rho>0 and uniform activity bound h
  => activity difference O(b_N)
    + common weighted KP margin (R86)
  => rooted connected-log difference (R85)
    + common analytic external collar and rooted geometry (R84)
  => two-marked second-moment bound
    + source beta/F2 operator and physical normalization
  => controlled scalar marginal response.

This route does NOT automatically incorporate R/B, large fields, coupling flow, or gauge normalization. Their bounds must be added to the actual complete-density comparison.

ABSTRACT-DERIVED: Banach-holomorphic Lipschitz bound 2h/rho, normalized Gaussian ratio/response lemma, and counterexamples showing residual-only/missing-radius insufficiency.
PREVIOUS SOURCE-ATTESTED: CMP119 vacuum/beta subtraction [59], first-common-scale geometric alignment from R70, native CMP116 localized activity mechanism [21].
OPEN PRIMARY: CMP109 (5.37),(5.42),(0.29), V^(1) sign/norm/alpha, exact beta extraction and same-scale two-cutoff translation.
OPEN NATIVE: marginal-tail flow coherence, source gauge/domain transport, uniform regular-input analytic radius/output norm, q_N sector matching, actual activity-difference transfer and full physical-response normalization.

NEXT YM-R88 (UNCONSUMED): minimize the source-input regular stability hypothesis. Does CMP116's source localization/weakening provide a native Lipschitz comparison for a marginal-subtracted extra-layer input WITHOUT requiring an invented full Banach holomorphic ball? Distinguish local finite-support insertion (R44/R45, source-native) from global growing-UV-root perturbation, with exact anchor counting. Continue primary CMP109 Eq(0.29) source inspection and scalar marginal-tail comparison; if unavailable record the irreducible source evidence gate.

No proof of 4D Yang-Mills existence or positive mass gap.
