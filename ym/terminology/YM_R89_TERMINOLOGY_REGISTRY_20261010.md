# YM-R89 — additive terminology registry
Date: 2026-10-10
Previous head: YM-R88 checkpoint 0fcb59699a58c32ce42159e34f8887400e2cc388.
Historical terminology unchanged.

- MicroscopicAnchorToLocalizationCube: a proposed map pi_N from extra UV microscopic roots x (spacing a_N=L^-N) to one common physically aligned CMP116 cube v. The actual CMP109/CMP116 map and volume/cutoff convention are OPEN.
- CoarseFiberMass: m_N(v)=sum_{x:pi_N(x)=v}u_(N,x), the sum of sizes of microscopic inserted inputs assigned to one localization cube. Nonnegative u_(N,x) are source input sizes, not a claimed primary V^(1) norm.
- WeightedLocalInsertionBudget: U_N(sigma)=sup_y sum_x u_(N,x) exp[-sigma d(pi_N(x),y)] on a Z4 localization-cube graph; a rooted local norm, not a global extensive sum.
- FourDimensionalAnchorConvolution: S0(sigma)=sum_{v in Z4}e^-sigma|v|_1 = ((1+e^-sigma)/(1-e^-sigma))^4.
- UniformPartialEnvironment: t=(t_x) with 0<=t_x<=1 (or any switched-on subset); input contributions scale as t_x u_x. Their rooted local budget is bounded by U_N uniformly in t.
- LocalSourceAdmissibilitySlack: a conditional statement that the source estimates remain valid when a baseline smallness parameter epsilon_base is increased by at most C_src U_N and stays below epsilon_max; CMP116 has NOT been verified to use precisely this norm/inequality.
- TaggedInputResponseAtZ: derivative partial_(t_x)H_Z(t,b) bounded by C_tag u_x exp[-mu tau(Z,pi_N(x))] uniformly in all t,b and cutoff; an independent native weakening/localization hypothesis.
- TaggedTreeToPolymerEnvelope: under TaggedInputResponseAtZ, |H_Z(t)-H_Z(0)|<=C_tag |Z| U_N(mu) exp[-mu(|Z|-1)] in unit-edge cube geometry, regardless of the number of microscopic anchors.
- StrictKPMarginBootstrap: if baseline cluster inequality has slack a-theta0>0, an explicit smallness condition on U_N ensures all t share a weighted KP majorant; depends additionally on the TAGGED response hypothesis.
- UVPerRootToCoarseBudget: abstract implication fiber count <=C a_N^-4 and u_x<=C' a_N^(4+alpha) => U_N<=C C' S0 a_N^alpha. Not a primary Eq (0.29) assertion.
- ZeroSourceGateSeparation: field analyticity on native U^c is distinct from stability under changing the interaction/potential along arbitrary partial insertion configurations.
- NativeSourceProofBoundary: original CMP109 Eq (0.29), exact V^(1)/alpha and map into inserted CMP116 activity, gauge/marginal/large-field and beta transport remain OPEN.

ABSTRACT-DERIVED means elementary estimates under declared hypotheses; CONDITIONAL NATIVE does not discharge Yang-Mills existence or the mass gap.
