# YM-R112 — source constraint-graph and vacuum color covariance registry

**Date:** 2026-10-27. [R112 pass](../passes/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_COVARIANCE_20261027.md). Previous registries append-only.

- **LinearSourceConstraintD** — D=L Qtilde from printed CMP109 p.267, map full fine Lie-bond coordinates to the source linear coarse constraint coordinates; h is a supported right inverse Dh=I on distinguished bonds b0(c).
- **ZeroExtensionE** — inject non-b0 coordinates into the full bond field with zeros on the distinguished bonds; with monitored restriction P, PE=I, Ph=0.
- **ExactSourceConstraintGraphC** — C=(I-hD)E with DC=0, PC=I, image C=ker D. Identifies the source embedding after delta elimination. Real finite-dimensional graph, not full nonlinear M beyond chart.
- **ReducedSourcePrecisionQ** — Q=C* A^(k) C = A_mm + A_md T + T* A_dm + T* A_dd T with T=-D_d^-1 D_m, positive on eligible Gaussian coordinates. Its genuine numeric entries and uniform spectral lower bound OPEN.
- **ProjectionCancellation** — because PC=I, R111's monitored covariance S=P C Q^-1 C* P* equals Q^-1. No separate projected-inverse norm estimate needed.
- **VacuumGlobalConjugation** — at identity SU(2) background, source (0.4), gauge fixing and action commute with simultaneous Ad_SU2, yielding Q=K tensor I3 for the bond-index matrix K. Does NOT extend unchanged to a general nontrivial background.
- **SU2MaxwellGaussianTail** — at vacuum bond b, s_b²=(K^-1)_bb and P(||g_k Z_b||>=theta)=erfc(theta/(sqrt2 |g_k|s_b))+sqrt(2/pi)*theta/(|g_k|s_b)*exp[-theta²/(2g_k²s_b²)]. Union across bonds without independence gives R112.7.
- **AmbientConditionalInverseGate** — optional formula A^-1-A^-1 D*(D A^-1D*)^-1 D A^-1 if ambient A>0; cannot assume when only constrained Q>0.
- **NativeVarianceSourceLock** — archived CMP99/CMP116 covariance positivity/decay is a potentially relevant source, but equality with R112 exact Q/K and its normalization must be established; no rate by similarity.
- **YM-R113** — acquire source-positive exact reduced Hessian/Green inverse dictionary at the SU2 identity background, derive actual diagonal and volume bounds; then admissible Ω,V two-cutoff data and law transfer.
