# YM-R86 — native CMP116 Lemma-3 decay reserve / explicit common KP and difference scalar gates

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior checkpoint: YM-R85 4a00ff4c618b3adda145468baec4532a591e04e1
Status: COMPLETE as bounded source audit and abstract weighted-KP theorem. Native cutoff difference and Eq(0.29) gates OPEN.
Next cursor: YM-R87 (unconsumed)
Claim boundary: UNPROVED RESEARCH PROGRAM; no Yang-Mills continuum existence or mass gap.

## 1. Source recovery: CMP116 already has a concrete exponentiation margin

The previously committed primary-page audits are now reexamined in the repository: YM-R50 locks the CMP116 (2.9)-(2.13) H(Z) hard-core polymer activity and subsequent exponentiation; YM-R51 derives D-family connected animal/cardinality summation and the metric relation d_k(Y)>=c_M |Y|, c_M=(24 M^4)^-1; YM-R52 audits the P-family entropy and source threshold; YM-R53 reads CMP116 printed pp.19-20 (2.32)-(2.38) and records
  |H(Z)|<=h exp[-lambda_H d_(k+1)(Z)],
  h=C3 epsilon1, lambda_H=((1-8 delta)/2)L kappa.
YM-R54 reads printed p.21 (2.39)-(2.41) and records that cluster exponentiation returns a next-scale effective-action estimate with coefficient
  lambda_eff=((1-10 delta)/2)L kappa,
and a smallness budget O(1) C3 epsilon1<=E0/2. Therefore lambda_H-lambda_eff=delta L kappa>0. This is a SOURCE-LOCATED SINGLE-TRAJECTORY exponent reserve, not an inferred two-cutoff difference theorem. The prior source audits were used, not a newly examined CMP116 original PDF.

The general Kotecky-Preiss abstract theorem remains reference [87], with original peer-reviewed DOI 10.1007/BF01211762 and the explicit 2026 restatement previously cited. The CMP116 abstract independently confirms that its exponentiated cluster expansion represents the Part-I fluctuation integral. The exact original CMP109 Eqs (5.37),(5.42),(0.29) were NOT recovered from publisher/Project Euclid equation pages; its positive-alpha irrelevance bound remains a SECONDARY locator [85], not a primary theorem in this project. Reused [7],[21],[59],[80],[85],[87]; no new numbered reference; highest [87].

## 2. Explicit common weighted KP sufficient condition — ABSTRACT-DERIVED

Let P be the hard-core polymer family of finite connected cube-unions Z at a FIXED scale in a bounded-degree localization graph. Write n=|Z|. Assume uniformly:
 (A) every polymer X has at most B |X| potential incompatible root cubes (including boundary adjacency);
 (B) for each root cube there are at most C_ent^(n-1) connected size-n polymers containing it;
 (C) d_(k+1)(Z)>=c_M |Z|, c_M=1/(24 M^4);
 (D) two endpoint analytic weights on the SAME polymer carrier and complex field chart satisfy sup_b |w_i(Z,b)|<= h exp[-lambda_H d_(k+1)(Z)], i=0,1, with h and lambda_H uniform in scale/volume; lambda_H and h are the R53 source-shaped quantities under source admissibility.

For positive parameters a and nu define t=exp[-(lambda_H c_M-a-nu)]. Then for any X,
 sum_(Z incompatible with X) p_Z exp[(a+nu)|Z|]
 <= B |X| h sum_(n>=1) C_ent^(n-1) t^n
 = B |X| h t/(1-C_ent t),
where p_Z=max_i sup_b|w_i(Z,b)| (not a sum). Therefore the sufficient scalar conditions
  C_ent t < 1,
  B h t/(1-C_ent t) <= a
yield
  sum_(Z incompatible X) p_Z exp[(a+nu)|Z|] <= a |X|,
the common weighted KP hypothesis. All affine interpolants w_s=(1-s)w_0+s w_1 satisfy |w_s|<=p, so the same analytic cluster convergence and zero-free margin holds for all s and b in the common chart.

This is a quantitative sufficient check, NOT a claim that the source automatically satisfies the inequalities for every preassigned parameter choice. In particular, the original source parameter hierarchy (large kappa, fixed L,M, small epsilon1, small alpha_j, weak g_j) and coupling-window persistence must allow the selected a,nu and fixed source exponent reserve simultaneously. Native successful exponentiation is strong evidence that a positive reserve exists; equality of the paper's specific exponentiation threshold and this new weighted-KP scalar test still requires checking the exact native constants.

One may choose nu small enough that it consumes only a portion of the source decay reserve delta L kappa in d_(k+1) units, provided the remaining entropy and a|Z| allowances fit; the margin may NOT be spent twice.

## 3. Separate cross-cutoff activity-difference criterion — ABSTRACT-DERIVED

Suppose on that SAME source-identified carrier the physically aligned pre-exponent activity difference satisfies
  d_(N,Z)=sup_b|w_(N+1,shifted)(Z,b)-w_N(Z,b)|
           <= eta_N exp[-lambda_D d_(k+1)(Z)].
Put t_D=exp[-(lambda_D c_M-a-nu)]. If C_ent t_D<1, the R85 anchored difference norm obeys
  delta_N = sup_z sum_(Z: anchor(Z)=z) d_(N,Z) exp[(a+nu)|Z|]
          <= eta_N t_D/(1-C_ent t_D),
because the number of anchored n-polymers is bounded by C_ent^(n-1).

Combining with R85 (common KP => connected-log E_N<=delta_N) and R84 gives, for uniform complex Cauchy radius r and halo R,
  ||DeltaGamma_N||M2
    <= k_N + [8 exp(nu R)/r^2]S0(nu/2)S2(nu/2)
          [t_D/(1-C_ent t_D)] eta_N.
Hence sum_N(k_N+eta_N)<infty is a sufficient abstract route to summable polarization-type moments. Exact physical source beta/F2 projection and scale/volume normalization remain separate assumptions.

The generic CMP116 one-step endpoint bounds give only
  d_(N,Z) <= 2 h exp[-lambda_H d(Z)],
so the evident eta_N is at best 2h, which need not tend to zero. They DO NOT supply a summable cross-cutoff difference. A per-root CMP109 Eq (0.29) bound with extra UV power a_N^(4+alpha) would be a candidate if its norm, marginal subtraction, first-common-scale identity, and 4D physical root count are primary-verified; no such promotion occurs here.

## 4. Negative controls, including moving carriers and coupling window

(1) Identical one-step KP envelopes can conceal an O(h) aligned cutoff difference: a single polymer has w_0=0, w_1=h/2 at every N. All analytic bounds and KP conditions are uniform, but logZ difference log(1+h/2) never vanishes. Decay reserve and KP alone cannot generate eta_N.
(2) Distinct source polymer carriers cannot be compared by zero extension without a verified conditioning/extra-shell embedding, because missing degrees of freedom and changed gauge charts may alter weights, normalizations and counterterms.
(3) Even if a common KP threshold can be met within one weak-coupling region, the R59/R75 coupling-persistence gate is not automatically settled. The RG trajectories being compared must actually remain in that region.
(4) A counterterm/marginal difference k_N and the full Pi/Ward Fourier second-moment normalization are independent of activity KP convergence.

## 5. Determination

CLOSED ABSTRACT: explicit sufficient common weighted KP scalar inequalities from CMP116-shaped activity exponential decay and bounded-degree polymer counting; explicit eta_N-to-delta_N entropy transfer; composition with R85/R84 to two-mark moment consumer.
PREVIOUSLY SOURCE-LOCATED: CMP116 Lemma 3 endpoint (2.38), post-exponentiation margin (2.39)-(2.41), D/P/Z0/Z0' resummation and Cammarota threshold (R50-R54).
CONDITIONAL NATIVE: actual H_(N,j)(Z), H_(N+1,j+1)(Z) source-identical carrier/complex domain/parameter ceiling and direct common KP scalar inequalities.
OPEN NATIVE: epsilon/eta_N ultraviolet suppression on the actual first-common-scale activity difference; CMP109 (0.29) original bound and relation to V^(j), full beta/F2 normalization and all deterministic sector defects; coupling-window uniformity.

Next YM-R87 (UNCONSUMED): source-test the first-common-scale ONE-LAYER COMPARISON, especially whether CMP109 source marginal subtraction isolates an irrelevant V^(1) defect meeting a scale-power and whether the CMP116 cluster transform is Lipschitz for that defect on its actual conditioned/gauge carrier. Alternatively prove that the candidate V^(j) estimate is insufficient to control the source activity difference without a further coupling/sector match. Continue source access to exact CMP109 (0.29), including alpha and uniform quantifiers; no invented alpha.

No continuum Yang-Mills existence, Osterwalder-Schrader reconstruction, or positive mass gap is claimed.
