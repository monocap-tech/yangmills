# YM-R85 — additive terminology registry
Date: 2026-10-10. Previous checkpoint: YM_HEAD_R84_20261010.json.
Historical terms are unchanged.

- CommonPolymerCarrier: the same finite family of connected spatial polymers at both compared ultraviolet cutoffs, after an explicitly justified physical-scale map; absent polymers may have zero weight only if the source comparison permits this.
- HardCorePolymerWeight: complex holomorphic activity w_i(gamma,b) for a connected polymer gamma, with source b on a common radius-r polydisc. Compatibility means nonoverlap/nonadjacency in the chosen metric.
- CommonActivityMajorant: p_gamma = max(sup_b |w_0(gamma,b)|, sup_b |w_1(gamma,b)|), uniform in interpolation; separate from the difference d_gamma=sup_b|w_1-w_0|.
- WeightedRootedClusterSusceptibility: T_nu,p(gamma) = sum_{n>=1} 1/(n-1)! sum_{gamma_2,...,gamma_n} |phi_T(gamma,gamma_2,...,gamma_n)| product_{j>=2} (p_gamma_j exp(nu |gamma_j|)); rooted insertion marked at the first polymer. A bound T<=exp(a_gamma) is an explicit condition obtainable from a sufficiently strong weighted KP estimate; not assumed from bare one-step convergence.
- MarkedPolymerLipschitzTransfer: coefficientwise cluster telescoping gives a rooted log-activity difference bounded by d_gamma exp(nu |gamma|) T_nu,p(gamma) for each marked gamma.
- PreExponentActivityDifferenceBudget: delta_N = sup_z sum_{gamma:a(gamma)=z} d_gamma exp(nu|gamma|+a_gamma); an anchored difference on PRE-exponent CMP116-compatible polymer weights, not a bound presently proved by Bałaban.
- UniformKPMargin: a single majorant and connected-cluster bound valid for all w_s=(1-s)w0+s w1, for all s in [0,1] and all background b in the source complex polydisc.
- SourceHtoHardCoreDictionary: exact identification of native CMP116 connected H(Z) in (2.9)-(2.11) with CommonPolymerCarrier and weights; source-to-cross-cutoff identification OPEN.
- UVPowerNoCreation: a bounded Lipschitz transfer retains a small factor delta_N but cannot create positive ultraviolet alpha if absent upstream.
- UniformZeroDistance: separation of the partition function from its zeros implied by common absolutely convergent cluster expansion, not by endpoint nonvanishing alone.
- PrimaryEq029Gate: primary CMP109 Eq (0.29) original V^(j), norm, alpha>0 and actual one-layer difference identification; still OPEN.

Status: ABSTRACT-DERIVED for combinatorial finite-polymer implications; SOURCE-CITED for the general KP convergence theorem [87]; NATIVE-CLOSED only after actual CMP116/CMP109 source dictionaries and quantitative assumptions.
