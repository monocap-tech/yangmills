# YM-R150 continuation — Directional source-covariance transfer for R149's two solves

**Date:** 2026-10-31. **Previous merged HEAD:** d34f324cebfba268f42a59b71fdb8b0efa572ad3 (R150 historical Theorem 3.15 covariance). **Custody:** SOURCE-BOUNDED CONDITIONAL DERIVATION + exact finite L13 coordinate check. **Native YM-R150 IN PROGRESS/UNCONSUMED**; R149 remains last canonical completed checkpoint. Four-dimensional continuum Yang–Mills, OS and a positive physical mass gap remain UNPROVED.

## 0. Source and the previous transfer gate

**ORIGINAL PRINTED CMP99 SOURCE:** user-provided original typeset 46-page *Propagators for lattice gauge theories in a background field*, CMP99 (1985), printed p428 Eqs.(3.155)–(3.158) and p432 Eqs.(3.185)–(3.187), Theorem 3.15. The source historical independent-bond covariance is \`Sigma_o=(C_o* Delta_k C_o)^(-1)=P_o C^(k)(Lambda) P_o*\`. The full historical covariance kernel satisfies \`||C^(k)(Lambda;y,y')||<=B0 exp(-delta0 |y-y'|)\` under Bałaban's source hypotheses, with unspecified B0,delta0 depending only on d,L. Original equation images were inspected; neither the source PDF nor its pages are redistributed to the repository.

**NEW 1987 SOURCE:** CMP109 original printed pp266–268 (2.9)–(2.14), previously image-verified in R111–R112/R148–R149. Its reduced Gaussian precision is **a different native object**, \`K_n=C_n* A^(k) C_n\`. Its source independent-coordinate chart and normalization cannot be replaced by those of 1985 without a justified transfer.

**Previous R150 sufficient global gate:** \`K_n >= (s²/M_hist - eta)I\` if a source-valid chart F has global minimum singular value s and full constrained-Hessian defect norm <=eta. Those quantities remain OPEN. This new note derives a potentially sharper **directional covariance consumer** which does NOT first require global \`s\` or the full old precision to be assembled. A global positive comparison is still needed.

## 1. The exact relative-form transfer theorem

**DERIVATION (finite-dimensional, source-compatible hypotheses only):** Suppose a true shared admissible regional/gauge/background/scale chart is constructed. Let Ko>0 be the 1985 reduced precision in its source Hilbert metric, F an invertible coordinate map **new independent coordinates -> old independent coordinates**, and Kn the actual CMP109 reduced complete constrained-Hessian precision (action Hessian minus multiplier times full coarse-constraint Hessian, with all source gauge/collar terms).

Define A=F* Ko F, E=Kn−A. Assume the **complete relative form bound**
    -rho A <= E <= rho A,  0<=rho<1.                 (R150.D1)
Equivalently, \`||A^(-1/2) E A^(-1/2)||<=rho\`, with self-adjoint E and matched Hilbert structures. Then
    Kn >= (1-rho)F*KoF>0,                            (R150.D2)
    Sigma_n=Kn^(-1)
       <= (1-rho)^(-1) F^(-1) Sigma_o F^(-*) .      (R150.D3)
Proof: order inequality R150.D2, inversion reverses Loewner order, and \`(F*KoF)^(-1)=F^(-1)Sigma_o F^(-*)\`. This is algebraic; **rho is NOT source-certified**, nor is F on the complete CMP99/CMP109 regional carrier.

For a particular new-source monitored observable w (a coefficient vector in the real scalar per-bond identity-background chart), set the old *dual-pulled* observable v=F^(-*)w. Then
    Var_n(w*x) <= (1-rho)^(-1) <v,Sigma_o v>.        (R150.D4)
This is the key shift from requiring a global \`sigma_min(F)\` to requiring source-local control of **only the dual transported directions used in R149**, conditional on the global form bound rho<1.

## 2. Direct use of original 1985 exponential covariance decay

The printed CMP99 kernel estimate gives, in compatible source unit-lattice bond metrics,
    <v,Sigma_o v> <= B_* Sum_{i,j}|v_i||v_j|e^(-delta0 d(i,j))
                  <= B_* ||v||_1²,                 (R150.D5)
where \`B_*=3 B0\` is a deliberately conservative SU(2) color-block component convention (if source |.| already means 3x3 operator norm, B0 itself suffices). Source Theorem 3.15 requires its domain/collar, background regularity, M alpha0 smallness, and source metric; no external physical cutoff or interaction weight has been included.

Hence
    Var_n(w*x) <= B_* ||F^(-*)w||_1²/(1-rho).       (R150.D6)
At the SU(2) identity, when source charts commute with global color rotations, the same bound controls the full 3-vector color covariance, so the centered-Gaussian radial tail is bounded by
    P_n(||w*x||>=T)
      <= Q3(T sqrt(1-rho)/(sqrt(B_*)||F^(-*)w||_1)), (R150.D7)
where \`Q3(r)=erfc(r/sqrt(2))+sqrt(2/pi) r exp(-r²/2)\`. For a nonidentity background, R150.D7 still follows from a bound on the full 3x3 covariance operator by coupling to an isotropic standard Gaussian; it must not be asserted merely from an identity-background F.

**Crucial:** The required full source-region F may have nonlocal dual inverse, and its \`||F^(-*)w||_1\` could grow with RG depth. The one-step computation below does NOT certify any uniform source-local bound. Historical B0/δ0 have no numerical values; rho is OPEN.

## 3. Exact source-shaped L13 two-direction simplification

Use only the previously DECLARED identity-background one-step aligned R147 sparse five-bond constraint comparison, with new independent coordinates \`x=(a,w1,w2,z)\` and old independent coordinates \`y=(b,w1,w2,z)\`. Its algebraic composite map is
    F = [[-1,-1,-1,t],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    t=1/52, F²=I, det F=-1.                        (R150.D8)
Here old/new averaging restrictions and four additional original source bond directions are **not** a fully source-native regional CMP99/CMP109 chart. R120's sparse coefficient and R143's bridge coefficient are source-shaped, with explicitly chosen path/bridge/cell conventions.

R149's two new-coordinate variance directions are
    w_a=e_a,          w_u=e_a−t e_z.
By exact rational dual transport,
    v_a=F^(-T)w_a=(-1,-1,-1,t),   ||v_a||_1=157/52,
    v_u=F^(-T)w_u=(-1,-1,-1,0),  ||v_u||_1=3.       (R150.D9)
**The curvature-sensitive t exactly cancels in the second backward direction.** This cancellation is an algebraic property of this finite declared chart, not a claim that the 1987 field's nonlinear curvature or complete Hessian defect vanishes.

If AND ONLY IF the source region, metric and full second variation supply R150.D1 and the finite F extends correctly to the source observables (with no additional dual coefficients), the conservative one-coordinate variance consumers become
    s_a² <= [B_*/(1-rho)](157/52)²,
    s_u² <= [B_*/(1-rho)] 9.                         (R150.D10)
With actual CMP109 cutoff rescaling \`T=theta_k/|g_k|\` from R148, Gaussian Gate B would then have the conditional bound
    delta_gamma <= min{1,
      Q3(T sqrt(1-rho)/(sqrt(B_*) (157/52)))
      + Q3(T sqrt(1-rho)/(3 sqrt(B_*)))}.            (R150.D11)

**This is a conditional template only.** In the full source map, F may mix many other fine bonds, while the sparse F was computed after setting those bond components to zero. Restriction to an illustrative subspace does not determine the *inverse transpose* on the full space; in particular R150.D10 and D11 are NOT numerical or source-certified CMP109 estimates.

The finite identities \`F²=I\`, dual transports and norm lengths are checked with exact fractions in [reproducible certificate](../computations/YM_R150_DIRECTIONAL_TRANSFER_RATIONAL_20261031.py). The script also uses an explicitly synthetic old Ko=I and E=−(1/4)F*F as a sanity check; this is NOT the actual source Hessian or rho.

## 4. What can be omitted and what cannot

**Legitimately avoided:** reconstructing all of historical Ko numerically, finding a global lower singular-value s of F *before* controlling these two observable covariances, and using a blunt \`M_hist\` when historical covariance entries directly control a local v.

**NOT AVOIDED:** constructing an actual legal old/new source Ω/collar carrier; establishing that F transports the source's independent-coordinate/gauge fields; bounding full relative constrained-Hessian defect rho (not only a jet or local matrix entry); controlling full dual supports of both observables; source normalized interaction W and partition masses; the independent two-UV history pair.

**Priority for next R150 step:** use primary source CMP99 (3.155)–(3.158),(3.185) and CMP109 (2.9)–(2.12) to type a concrete regional F, and identify its dual action on w_a,w_u (including all bond supports). Separately prove or obstruct an actual source-relative form defect rho<1 using complete action/gauge/constraint Hessian, not an action-jet-only estimate. If one cannot do so, STOP at that source obstacle; do not insert guessed B0, rho or a full F from the toy matrix.

**Pass status:** R150 IN PROGRESS / UNCONSUMED. Canonical R149 checkpoint untouched. No four-dimensional continuum Yang–Mills construction or mass-gap theorem.
