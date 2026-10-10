# YM-R82 — additive terminology registry

Date: 2026-10-10. Prior head YM-R81 (5a4e9377094b04664859f4201d9235c0f5780f6e). All historical entries retained.

- NativeCovarianceFirstRoute: use the source-normalized fluctuation Gaussian C^(k) and its root in the CMP116 (2.5)–(2.7) chart, rather than requiring prior equality of the CMP99 Delta_a and CMP102 Delta_1 precision operators. This is a route minimization, not a new source theorem.
- NormalizedGaussianPartition: Z(C,V;b)=E_{Y~N(0,C(b))}[exp(-V(b,Y))] on a finite real SPD carrier with positive integrable partition. The Gaussian is a probability law, so its determinant is already normalized.
- CovarianceResponseInsertion: L_ab(C,V;b)=E_{C,V}[partial_a V partial_b V - partial_ab V], where E_{C,V} uses tilted normalized density exp(-V)/Z, and a,b denote fluctuation coordinates, not momentum components.
- CovariancePotentialSplit: exact algebraic comparison of two normalized Gaussian partition functions by first changing C with V fixed, then changing V with C fixed; valid only on a common identified finite carrier.
- TransportedGaussianChart: an orthogonal change U(b) of fluctuation coordinates with covariance C_1=U C_0 U*, interaction V_1(b,y)=V_0(b,U*y), and consistently transported external directions. Such a change alone leaves Z unchanged even if raw matrices are not close.
- SourceCountertermChannel: any b-dependent deterministic/bare/localization/gauge-measure term K(b) outside a normalized Gaussian integral in the source one-step action. Never silently omit from a full polarization comparison.
- ContractedResponseBudget: directly controls sum_ab (partial_b^alpha Delta C_ab)(partial_b^beta L_ab) with correct volume/source normalization, rather than demanding separately identical Hessians/projectors.
- NonGaussianInteractionDefect: V_1-V_0 after honest source transport, including source-prescribed vertices/cumulants; its tilted-expectation interpolation is independent of Gaussian covariance mismatch.
- CovarianceOnlyObstruction: identical C is insufficient for matching the full background polarization if V or K differs.
- CMP99CMP102PrecisionSideGate: the unresolved Delta_a/Delta_1 identity retained for full Hessian provenance, but previously demoted by YM-R42 from CMP116 covariance-root critical path.
- PrimaryCMP109SourceGate: original (5.37),(5.42),(0.29), with definition/normalization/quantifier windows; remains uninspected.

ABSTRACT-DERIVED results may be rigorous finite-dimensional equalities but are NOT an applied native Yang-Mills theorem. SOURCE-LOCATED refers to prior repository source audits (R42/R43) and does not imply fresh original-page inspection.
