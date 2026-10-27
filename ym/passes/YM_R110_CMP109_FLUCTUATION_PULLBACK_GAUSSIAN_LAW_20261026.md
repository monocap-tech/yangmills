# YM-R110 — CMP109 fluctuation-cutoff pullback and normalized Gaussian law

**Date:** 2026-10-26. **Prior canonical:** [R109](../checkpoints/YM_HEAD_R109_20261026.json), main 909d0061a13d9b1e0eaee3594d8e3283caca2400. **Status:** COMPLETE AS EXACT ONE-STEP MEASURE INTERFACE AND CONDITIONAL ERROR BOUNDS; NOT A TWO-CUTOFF YANG–MILLS LAW THEOREM. **Next:** YM-R111 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 1. Source object and the first type correction

Direct printed-image checks of Bałaban CMP109 (1987), pp.255, 265–268, equations (0.17), (0.19), (2.1), (2.3), (2.9)–(2.13), through its 54-page [printed PDF scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), zero-based indices 6,16–19. See [source receipt](../source_receipts/YM_R110_CMP109_FLUCTUATION_SOURCE_RECEIPT_20261026.md). R109's FP identity (0.15)–(0.16) remains proved; do NOT count its internal indicator as a separate physical cutoff.

In (2.9) the genuine characteristic function is initially defined on independent gauge-fixed **pre-linearization coordinates** B'(b), excluding special b0(c). The source offers fixed threshold epsilon1 or the alternate threshold g_k*epsilon1/gamma_k. It then performs nonlinear constraint linearization, removal of b0(c), and coupling rescaling before reaching the Gaussian B variables in (2.12)–(2.13). The Gaussian covariance is explicitly C^(k)=(C* A^(k) C)^(-1) on the remaining coordinates (printed p.268).

**Therefore source chi_k in (2.13) is the pullback of the original cutoff under the source coordinate changes, not automatically the same coordinatewise box in final Gaussian B.** Call that composite inverse-coordinate map Phi_{k,U}; whether its chart is defined and its nonlinear error controlled is a separate SOURCE-NATIVE obligation.

## 2. Exact normalized fixed-background fluctuation law

Fix an eligible **real** background U and the source's independent finite-dimensional real Gaussian measure gamma_{k,U}=mu_{C^(k)(U)}. Write
  chi_hat(B)=chi_pre(Phi_{k,U}(B)),
and R_{k,U}(B)=the COMPLETE real exponential expression from (2.13), including the P^(k) and bracketed terms (Jacobian, gauge, action remainder, inherited E). Require 0<Z_{k,U}<infinity. Define

  Z_{k,U}=integral chi_hat(B)*exp(R(B)) gamma_{k,U}(dB),
  nu_{k,U}(dB)=chi_hat(B)*exp(R(B))/Z_{k,U} * gamma_{k,U}(dB).      (R110.1)

This is the correctly typed normalized *one-step conditional fluctuation law* extracted from the named source integral. It is NOT the full normalized Wilson cutoff law, NOT the V-output distribution and NOT a two-cutoff coupling. Source analytical extensions to complex backgrounds are not claimed to be probability measures.

Let p=gamma(chi_hat=1)>0, q=1-p, and gamma_chi=gamma conditioned on chi_hat=1. Exact partition factorization:

  Z=p * E_{gamma_chi}[exp(R)],
  log Z=log p + log E_{gamma_chi}[exp(R)].                          (R110.2)

Thus cutoff probability and nonlinear interaction are distinct contributions. Without bounds, neither is certified small.

## 3. Exact total-variation comparison and conditional Gaussian tail gate

If R has finite essential oscillation omega on gamma_chi, then

  TV(nu,gamma)<=q+tanh(omega/4).                                    (R110.3)

Proof: TV(gamma_chi,gamma)=q. An exponential tilt with weights within [a,b] has TV from its unweighted reference at most (sqrt(b)-sqrt(a))/(sqrt(b)+sqrt(a))=tanh(log(b/a)/4). Apply the triangle inequality. If omega infinite, use TV<=1 rather than this bound.

The nonlinear cutoff pullback produces a necessary quantitative entry gate. Let m=dim Lie algebra, n=number of independent pre-cutoff bond coordinates. Suppose a source-verified chart event D and defined linear H satisfy

  max_b ||Phi(B)_b - g_k*(H B)_b|| <= delta < theta_k  on D,

where theta_k is the source's selected cutoff threshold. Let v=max_{b,a} Var_gamma[(HB)_{b,a}]>0. Then elementary Gaussian tails and the union bound yield

  q <= gamma(D^c) + 2*m*n*exp(-(theta_k-delta)^2/(2*m*g_k^2*v)).    (R110.4)

Proof: on D, failure of |Phi_b|<theta implies |g_k(HB)_b|>=theta-delta; at least one Lie coordinate exceeds (theta-delta)/sqrt(m). Use centered Gaussian scalar tail bounds and add chart exit. **The hypotheses are NOT yet supplied by the source for an actual paired block**, so no number or summable rate is claimed.

For fixed theta=epsilon1, a fixed-volume Gaussian tail may have exp(-c/g_k^2) behavior if uniform chart/covariance constants can be proved. For alternate theta=g_k*epsilon1/gamma_k, the g_k scaling cancels in the nominal linear exponent, so the same exp(-c/g_k^2) inference is INVALID. Bond count, covariance variance, gamma_k and chart exit all require source estimates. Large field/complement control is not closed.

## 4. Conditional same-coordinate two-law gate

If two admissible fluctuation constructions have ACTUALLY been transported to the **same d-dimensional centered Gaussian coordinate space**, with positive definite C0,C1 and parameters q0,q1,omega0,omega1, then by R110.3, Gaussian relative entropy, and Pinsker:

  TV(nu1,nu0) <= q0+q1+tanh(omega0/4)+tanh(omega1/4)
      + 1/2 sqrt(tr(C0^(-1)*C1)-d-log det(C0^(-1)*C1)).           (R110.5)

Proof: triangle through both base Gaussians; KL(gamma1||gamma0)=1/2*[trace-d-logdet]. This is a CONDITIONAL test, capped by trivial TV<=1. **There is no established coordinate identification between independent N,j and N+1,j+1 source histories**. Aligned physical spacing does not supply one; in general chart dimensions, Ω, prescribed V and inherited E differ. The alternative is a real common gauge-invariant observable pushforward, not a fabricated Gaussian identity.

## 5. Background determinant is not a removable source-normalization scalar

Source Eq. (2.12) separately contains log Z^(k)(U_{k+1}) - log Z^(k)(1), where the Gaussian normalization Z^(k)(U) depends on the constrained background. At fixed U it is a scalar and cancels if one normalizes conditional B expectations. But as U=U_{k+1}(V) varies, the term is V-dependent and survives in the induced coarse action/law. Likewise source inherited E_k carries previous integration history. R108's reference-normalizer cancellation applies only to a constant independent of V, not this determinant.

Hence: normalized fixed-background fluctuation law != normalized coarse V law != actual comparison of two UV cutoff Wilson/RG histories. The typed source components R110.1–R110.5 do not prove physical Cauchy coherence.

## 6. Stop and successor

**Closed:** precise source one-step Gaussian/interaction/cutoff-carrier dictionary; source cutoff nonlinear-pullback obligation; exact conditional partition and TV inequalities; warning on threshold branches and V-dependent determinant. **Open:** source legal choice (0.4)/(0.12) averaging, Phi error delta and chart exit, v and bond-count uniformity, Ω/V paired admissibility, true two-history common distribution/observable carrier and estimates, Eq.(0.29)/(5.37)/(5.42), OS existence and mass gap.

**YM-R111 unconsumed:** select one CMP109 M, legal odd L>11, and *actual* aligned block. Recover Phi and analytic domain including quadratic D correction; test delta,v and chart-exit in R110.4, source threshold branch, inherited E and background determinant; then construct/obstruct a legitimate two-cutoff law cospan. No new generic positivity lemma or inferred universal mass-gap claim. Historical bibliography [92] unchanged.
