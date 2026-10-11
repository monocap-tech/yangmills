# YM-R83 — additive terminology registry

Date: 2026-10-10
Prior: YM-R82 (e2514428977478a8321f26b4dd8cfc8774499271)
Historical terminology unchanged.

- CommonProductGaussianChart: finite real product standard Gaussian probability measure mu0 for both cutoff comparisons after a source-justified identification; CMP116 supplies such a chart within each step, not automatically a common cross-cutoff one.
- ProductChartInteractionW: a source-mapped function W_i(b,X) whose normalized expectation Z_i(b)=int exp(-W_i(b,X)) dmu0(X) represents the fluctuation part of the step; does not automatically equal CMP109's entire effective action.
- DeterministicCountertermK: the source-specified term K_i(b) outside -log Z_i, including any bare/marginal, chart, measure or localization terms. No native dictionary closed.
- InteractionInterpolationD: D=W1-W0 and W_s=W0+sD, s in [0,1], on a common fixed mu0 carrier.
- TiltedConnectedCumulant: covariance Cov_s(A,B)=<AB>_s-<A>_s<B>_s and third joint cumulant kappa3_s(A,B,C) under exp(-W_s)dmu0/Z_s.
- FullTwoSourceResponse: mixed derivatives partial_(b_x)partial_(b_y) of Gamma=K-log Z, including one expectation, three covariance and one third-cumulant term for a varying interaction.
- AnchoredResponseKernel: linear-in-D_z contribution F_z(x,y) to the interpolated FullTwoSourceResponse, where D=sum_z D_z and z is a source-native root, not an invented physical lattice normalization.
- RootedTwoSourceDecay: assumed bound |F_z(x,y)|<=A epsilon_N exp[-kappa(|x-z|_1+|y-z|_1)] uniformly across cutoff, background, volume and interpolation.
- SecondMomentDefectNorm: sup_x sum_y |x-y|_1^2 |Delta Gamma_xy| on the aligned four-dimensional lattice, before source-specific tensor/marginal extraction.
- UniformAnalyticCollar: a common complex polydisc of radius r>0 on which each relevant interpolated localized difference is analytic and its sup norm is controlled; not implied by smallness on real backgrounds alone.
- InterpolationZeroFreeGate: nonvanishing of each normalized Z_s(b) on the needed complex analytic domain and an unambiguous log branch, separate from endpoint nonvanishing.
- UltravioletAnchoredBudget: epsilon_N whose N-summability must be justified by native Eq (0.29) / source scaling and rooted counting, not merely an O(g_N) insertion.
- CMP116ActivityDerivativeTransfer: proposed extension from CMP116 individual H(Z) estimates to interpolation derivatives and connected two-source kernels; OPEN source-specific implication.

ABSTRACT-DERIVED indicates finite mathematical identities and implications under named assumptions. SOURCE-LOCATED refers to earlier project extraction R42-R45 / reference [21]. NATIVE-CLOSED requires verified original CMP109 objects and quantifiers. No continuum Yang-Mills or mass-gap claim.
