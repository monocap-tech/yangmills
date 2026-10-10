# YM-R77 — additive terminology registry

Date: 2026-10-10
Prior head: YM-R76. The historical registry is unchanged. Definitions below precede or accompany load-bearing use in R77.

- PhysicalAlignmentMap: the source-independent indexing equality a_(N+1,j+1)=a_(N,j)=L^(j-N); equality of spacings, not of effective actions.
- FullPolarizationDifference: the difference of the COMPLETE one-step polarization tensors after a specified physical-scale identification, including all determinant, gauge, Jacobian, interaction and localization contributions. No native source definition reconstructed in R77.
- MixedMomentExtractor: for a translation-invariant kernel D(z) with absolutely summable second moment, the functional -sum_z z_mu z_nu D(z), equal to partial_pmu partial_pnu Dhat(0) for Dhat(p)=sum_z exp(i p.z)D(z).
- ExponentialKernelNorm: ||D||_(kappa,1)=sum_z exp(kappa |z|_1)|D(z)|, requiring kappa>0 and a fixed normalized lattice-coordinate convention.
- WeightedSchurAlgebra: matrices on a finite metric lattice with weighted row-and-column sum norm max{sup_x sum_y exp(kappa d(x,y))||M_xy||, sup_y sum_x exp(kappa d(x,y))||M_xy||}. The norm is submultiplicative under compatible multiplication.
- WeightedSchurTransfer: a conditional quantitative mismatch estimate for S_i=A_i-B_i C_i^(-1) B_i* in WeightedSchurAlgebra, requiring separate inverse-locality bounds on C_i^(-1).
- PolarizationMomentObstruction: unweighted operator-norm closeness, even for uniformly positive translation-invariant convolution operators, need not imply convergence of the mixed second-momentum extraction.
- PairedSourceProjection: the still-to-be-source-identified exact split of the complete scale-j correction into an F^2 marginal contribution and its complementary polymer remainder. Not an asserted theorem.
- PrimaryEquationAccessGate: direct equation-level reading of Bałaban CMP109 (5.37), (5.42), (0.29) with definitions, domain, normalization, signs and quantifiers; OPEN.

Proof labels: ABSTRACT-DERIVED is a mathematical implication under explicit hypotheses; SOURCE-ATTESTED requires direct primary equation inspection; NATIVE-CLOSED requires the actual Yang–Mills dictionary and hypotheses. The abstract results below do not close native YM gates.
