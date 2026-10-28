# YM-R148 — Native CMP109 conditional precision and two Gaussian cutoff gates

**Date:** 2026-10-28. **Predecessor:** YM-R147, merged main 50055f6. **Status:** COMPLETE AS SOURCE-OPERATOR REDUCTION AND CONDITIONAL GAUSSIAN/MEASURE MATHEMATICS; NATIVE NUMERICAL AND UV ESTIMATES OPEN. **Next:** YM-R149 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM. No continuum four-dimensional Yang–Mills, Osterwalder–Schrader reconstruction, or positive spectral mass-gap theorem.

## 0. Exact source and question

Printed CMP109 pp.266–268, Eqs.(2.9)–(2.14), were inspected on original paper images in https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . Eq.(2.9) monitors all fluctuation bonds *except* b0(c); p267 builds the special-bond-supported right inverse h; p268 states the reduced Gaussian covariance (C* A^(k) C)^(-1). It separately retains a background-dependent Gaussian normalizer, nonlinear Jacobian, interaction and inherited effective action. Source receipt: [YM-R148 source](../source_receipts/YM_R148_CMP109_PRECISION_CUTOFF_SOURCE_RECEIPT_20261028.md).

Native R111 proves P h=0, so nonlinear constraint-linearization does not displace monitored coordinates. R112 proves C=(I−hD)E, PC=I; at SU(2) identity the precision is Q=K⊗I3, K symmetric strictly positive on the actual finite source Gaussian carrier. R147's **declared** L13 identity five-bond test gives a monitored-coordinate shift x_a→u=x_a−t z with t=1/52. It is NOT a native two-UV or CMP99 full regional transport.

## 1. Exact conditional precision is NOT marginal covariance

Let x_a∈R³ be a monitored bond vector. In the Gaussian law with precision K⊗I3, completing the square conditional on all other monitored vectors gives

**Law(x_a | x_{−a}) = N3(m_a(x_{−a}), K_aa^(−1) I3).**  (R148.1)

The conditional mean is generally nonzero. The *marginal* variance is instead s_a²=(K^−1)_aa. These are not interchangeable. A source coercivity lower bound K≥α I gives a marginal upper-variance bound and a conditional variance **upper** bound; it does not give an upper bound on conditional precision K_aa, as shown by K=diag(M,1,...) with M→∞.

In the declared equal-interface-coefficient one-step geometry, a non-special e1 interface bond a and source special bond b have the same derivative coefficient κ=1/2197 in the same coarse-link row. Then the source graph reconstructs C e_a=e_a−e_b (in one color), so

**K_aa=<e_a−e_b, A^(k)(1)(e_a−e_b)>**,            (R148.2)

and **0<K_aa≤2||A^(k)(1)||_op** in the stated orthonormal bond metric. This identifies a *two-bond quadratic energy*, not a source-verified numerical upper bound on A^(k) or K_aa. For a generic nonidentity background the conditional covariance becomes the inverse of a 3×3 precision block, without this color-isotropic simplification.

## 2. Gate A: SU(2) three-color boundary-density bound

Use the *actual independent source Gaussian coordinates* x_a,z∈R³ with K⊗I3. Set T=θ_k/|g_k|, θ_k=ε1 or g_k ε1/γ_k (assuming positive coupling and a legal chart). Let R_sh be a common other-bond restriction, and compare

 A=R_sh∩{||x_a||<T},  B=R_sh∩{||x_a−t z||<T}.

Condition on all other bond vectors including z. Sections of the two balls along the t z direction have symmetric-difference length at most 2|t| ||z||. The conditional one-dimensional normal density is at most sqrt(K_aa/(2π)); integrate perpendicular color coordinates and then the other bond vectors. Thus

**δγ=γ(A△B)≤min{1,2|t|sqrt(K_aa/(2π)) Eγ||z||}.**  (R148.3)

At SU2 identity z has Maxwell mean 2sqrt(2/π) s_z, where s_z²=(K^−1)_zz. Therefore

**δγ≤min{1,(4|t|/π)sqrt(K_aa (K^−1)_zz)}.**     (R148.4)

This does not require bond independence. It needs an *upper conditional precision* and a marginal second moment; neither is numerically certified for CMP109 here. The t=1/52 coefficient is ONLY the prior declared sparse source-shaped model.

## 3. Gate B: rare-exit comparison avoids upper conditional precision

The symmetric difference obeys the set inclusion

**A△B ⊂ {||x_a||≥T} ∪ {||x_a−t z||≥T}.**

Both linear combinations are centered isotropic three-dimensional Gaussians at U=1. Define

 s_a²=(K^−1)_aa,
 s_z²=(K^−1)_zz,
 s_u²=(K^−1)_aa+t²(K^−1)_zz−2t(K^−1)_az.

With Q3(r)=erfc(r/√2)+sqrt(2/π) r exp(−r²/2), the Maxwell survival function,

**δγ≤min{1,Q3(T/s_a)+Q3(T/s_u)}**               (R148.5)

for positive s_a,s_u; degenerate cases use the obvious deterministic limits. Via Gaussian covariance Cauchy–Schwarz, s_u≤s_a+|t|s_z. If a native coercivity estimate K≥α I holds *on precisely this source carrier and normalization*, then

**δγ≤min{1,Q3(T sqrt(α))+Q3(T sqrt(α)/(1+|t|))}.**  (R148.6)

This uses lower precision/coercivity, not an upper conditional precision. It can outperform Gate A when the physical cutoff lies far into the Gaussian tail. Critical scaling warning: θ_k=ε1 gives T=ε1/|g_k|; the alternate θ_k=g_k ε1/γ_k gives T=ε1/γ_k (g_k>0), so no g_k improvement follows automatically.

**No full-volume or UV theorem:** these bounds concern ONE localized shifted monitor event. Summing an uncontrolled number of events or replacing increasing coarsening index k by UV refinement N is invalid. The actual source K numerical covariance/eigenvalue and Ω/gauge validity remain OPEN.

## 4. Positive weights and normalized cutoff laws

Fix ONE source-compatible Gaussian reference γ and ONE common positive measurable weight W, representing the same-history interaction/Jacobian terms, with finite positive truncated masses Z_A=∫_A Wdγ and Z_B=∫_B Wdγ. Put c=∫_{A∩B}Wdγ, a=∫_{A\B}Wdγ, b=∫_{B\A}Wdγ. Then

**TV(1_A Wγ/Z_A,1_B Wγ/Z_B)=max(a,b)/max(Z_A,Z_B).**    (R148.7)

Proof: the common part has normalized density W/max(Z_A,Z_B) on A∩B, so the overlap mass is c/max Z and TV=1−c/max Z=max(a,b)/max Z. This is exact and includes the normalizer movement.

For W∈L²(γ), Cauchy–Schwarz yields

**TV≤min{1, sqrt(Eγ[W²] δγ)/max(Z_A,Z_B)}.**        (R148.8)

Both positive partition masses are required. For two distinct UV histories, their W, covariance, inherited actions and backgrounds generally differ: R148.7–R148.8 are NOT yet a comparison of complete physical laws. The source does not currently supply the needed native W second moment or partition lower bound.

## 5. Exact rational reference control and stop

Choose A_test=I5 on the **declared five-bond model**, a synthetic test and explicitly NOT CMP109 A^(k). Construct C_n^b from R147, Q_test=C* C and Σ_test=Q_test^−1. The standard-library [rational certificate](../computations/YM_R148_GAUSSIAN_BOUNDARY_PRECISION_RATIONAL_20261028.py) verifies

 K_aa=2, Σ_aa=8113/10817, Σ_zz=10816/10817,
 Σ_az=52/10817, Var(x_a−z/52)=8115/10817.

In the corresponding SU2-color-isotropic Gaussian the Gate A bound is 0.03463; Gate B gives 0.01478 at T=3 and 0.000180 at T=4. These are *upper bounds for a synthetic Gaussian*, not probabilities calculated from Bałaban's actual source.

**Closed here:** real 3D Gaussian conditional-precision identity, two alternative source-shaped event bounds, exact positive-weight normalized-event TV identity, and independent rational reference checks. **Open:** actual CMP109 K entries/uniformity and thresholds on an eligible region, physical Ω/collar, source χ interactions and normalizers, CMP99 full chart, two UV histories, OS/mass gap.

**YM-R149 unconsumed:** prioritize source-compatible finite identity CMP109 reduced K entries or coercivity under one declared legal Ω and actual scale-dependent T. If no recoverable A^(k) coefficients or source-valid region are available, record this obstruction; do not start another generic probability-inequality loop.
