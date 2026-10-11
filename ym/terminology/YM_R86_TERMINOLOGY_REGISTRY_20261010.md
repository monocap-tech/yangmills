# YM-R86 — additive terminology registry

Date: 2026-10-10. Previous checkpoint: YM_HEAD_R85_20261010.json, commit 4a00ff4c618b3adda145468baec4532a591e04e1.
Append-only; no historical term redefinition.

- NativeLemma3DecayCoefficient: lambda_H=((1-8 delta)/2)L kappa in CMP116 Eq (2.38) as source-audited in YM-R53, attached to tree metric d_(k+1)(Z).
- NativePostExponentDecayCoefficient: lambda_eff=((1-10 delta)/2)L kappa in CMP116 (2.39)-(2.41), as source-audited in YM-R54; the difference delta L kappa is a REAL source reserve for single-trajectory exponentiation, not a cross-cutoff bound.
- RootedPolymerAnimalEntropy: connected n-cube domain count N_n(x)<=C_ent^(n-1) on fixed four-dimensional localization adjacency graph, with an incompatibility root-neighborhood factor B; independent of lattice volume/depth.
- TreeToCubeCoefficient: c_M=1/(24 M^4), used in previous R51 to bound d_(k+1)(Z)>=c_M |Z|; applies only if exact source metrics and parameters agree.
- ExplicitWeightedKPScalarGate: with activity |w(Z)|<=h exp(-lambda_H d(Z)), choose a>0 and nu>0; let t=exp[-(lambda_H c_M-a-nu)]; require C_ent t<1 and B h t/(1-C_ent t)<=a. This implies an abstract common weighted KP bound for two activities with that SAME verified majorant on one polymer carrier.
- CommonActivityEnvelope: p_gamma=max_i sup_complex |w_i(gamma)|, not the sum; endpoint bounds of the same source form may dominate all affine interpolants if the backgrounds, carriers and collars have been identified.
- RootedDifferenceEnvelope: d_(N,gamma)=sup_complex |w_(N+1,shifted)(gamma)-w_(N)(gamma)|<=act_eps_N exp(-lambda_D d(gamma)), a separate comparison hypothesis.
- DifferenceEntropyScalarGate: when lambda_D c_M>a+nu+log C_ent, act_eps_N controls delta_N by t_D/(1-C_ent t_D), with t_D=exp[-(lambda_D c_M-a-nu)].
- UVGapIndependence: small h, positive lambda_H and common KP margin do NOT imply act_eps_N->0, much less sum_N act_eps_N<infty.
- CouplingWindowUniformity: both physically aligned RG trajectories must remain in the source admissible weak-coupling region with common fixed smallness parameters; R59/R75 did not prove unconditional persistence.
- PrimaryEq029AlphaGate: source verification of CMP109 Eq (0.29), exact V^(j) and first-common-scale difference mapping; OPEN.

Classification: SOURCE-LOCATED for R51/R53/R54 prior primary audit, ABSTRACT-DERIVED for the explicit general KP threshold, CONDITIONAL-NATIVE for using it on two actual Yang-Mills cutoff trajectories.

Clarification: act_eps_N denotes the nonnegative *activity-difference prefactor*; it is NOT the microscopic lattice spacing eta_N=L^(-N) used in R70.
