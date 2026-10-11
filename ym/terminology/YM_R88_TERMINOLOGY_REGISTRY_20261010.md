# YM-R88 — additive terminology registry

Date: 2026-10-10. Previous canonical head: YM-R87 / YM_HEAD_R87_20261010.json. All historical definitions unchanged.

- FirstCommonScaleInsertionFamily: a finite set A_N of source-owned extra-UV-root insertions on the physically aligned first-common-scale chart; existence of an actual native CMP109/CMP116 correspondence remains OPEN.
- PartialInsertionEnvironment: a subset S of A_N already switched on, with source activity H_Z(S;b), b on a fixed complex background polydisc. Must share carrier, coupling, gauge, and other sector conventions throughout comparison.
- EnvironmentUniformSingleAnchorReplacement: for every S subset A_N and x notin S, sup_b |H_Z(S union {x};b)-H_Z(S;b)| <= C u_(N,x) exp[-mu tau(Z,x)], with all constants uniform in S,N,volume. Stronger than R44's single source-local insertion at S=empty, but does not demand holomorphy in a global Banach regular-input ball.
- AnchoredHullTreeLength: tau(Z,x) is minimal lattice tree edge count containing all sites of the connected output polymer Z and the marked input root x. Satisfies tau(Z,x)>=|Z|-1+dist(x,Z) on unit-edge lattice graphs.
- PartialInsertionTelescoping: exact sum of changes along any ordering of A_N, from H_Z(empty) to H_Z(A_N); needs uniform per-environment bounds.
- InsertedActivityWeightedBudget: delta_N(beta)=sup_z sum_(Z:anchor(Z)=z) exp(beta |Z|) sup_background |H_Z(A_N)-H_Z(empty)| on a common physical polymer carrier; beta is a weight parameter, not the running coupling beta_j.
- LatticeAnchorConvolution: S0(mu)=sum_(u in Z^4)exp(-mu |u|_1) finite, and sum_x exp(-mu dist(x,Z))<=|Z|S0(mu).
- FiniteAnimalEntropyMargin: q=C_ent exp(beta-mu)<1; yields uniform factor exp(beta)/(1-q)^2 after summing connected-polymer counts and anchor multiplicity.
- SourceInputBudget: u_* = sup_x u_(N,x), a local input-size parameter; it is NOT the microscopic spacing a_N=L^-N or R86 act_eps_N without an exact dictionary.
- SimultaneousInsertionUniformityGate: prove environment-uniform source weakening/random-walk bounds for all partial insertion environments without exiting the allowed complex field and weak-coupling region. OPEN native theorem.
- LocalVersusGlobalInputCriterion: two alternative ways to control all insertions: rooted insertion locality with uniform intermediate environment (R88), or a genuinely small total bounded potential plus controlled complex tilted normalization (R87); neither is automatically implied by Eq(0.29).
- MarginalAndSectorMatchingGate: the Wilson beta, R/B/large field and gauge/measure source differences remain separate from the regular extra-layer input.
- PrimaryEq029PositiveAlphaGate: original CMP109 V^(1), norm, alpha>0, uniform constants and one-layer identity; OPEN.

Only the abstract finite-root implications are DERIVED; CMP116 source-native uniform insertion and Eq(0.29) transfer are CONDITIONAL/OPEN. No 4D continuum Yang-Mills or mass-gap result.
