# YM-R112 — CMP109 graph-constraint and SU(2) vacuum covariance receipt

**Date:** 2026-10-27. [Native analysis](../passes/YM_R112_CMP109_CONSTRAINT_GRAPH_VACUUM_COVARIANCE_20261027.md). **Evidence boundary:** original printed mathematical page images visually checked through third-party PDF host, not directly from Springer, and not a numerical evaluation of the printed propagator.

**T. Bałaban**, *Renormalization Group Approach to Lattice Gauge Field Theories I*, Commun. Math. Phys. 109(2), 249–301 (1987), DOI https://doi.org/10.1007/BF01215223. Visually inspected source: https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf , 54-page printed-paper scan. **Zero-based PDF indices** with printed pages:
- PDF 2, printed p.251: L an odd integer greater than 11; L=13 qualifies as a scale choice.
- PDF 4, printed p.253, Eq.(0.4): selected conjugation-covariant nonlinear source averaging M; on identity connections M(1)=1. Alternative averaging at PDF 5, p.254 (0.12) not selected.
- PDF 16, printed p.265, Eq.(2.1)–(2.3): regular coarse backgrounds, small field and source-prescribed minimum; no pair across independent UV cutoffs.
- PDF 17, printed p.266, Eq.(2.9): chi monitors independent B'(b) outside special b0(c); two cutoff threshold alternatives.
- **PDF 18, printed p.267, decisive equation and prose:** the linearized block constraint is L Qtilde B', h maps coarse constraint variables to fine distinguished bonds, is zero on all other bonds, and L Qtilde h=I. Nonlinear substitution B_old=B_new-h Dtilde(B_new); its quadratic analytic correction starts in second order.
- **PDF 19, printed p.268:** delta constraint eliminates B'(b0(c)), remaining variables B, full embedding B'=C B, and Gaussian covariance is (C* A^(k) C)^(-1). Equation (2.12) retains background-dependent Gaussian determinant and nonlinear Jacobian/action; (2.13) restricts via chi and tilts by interaction.
- PDF 20, printed p.269, Eq.(2.16) and nearby prose: local adjoint gauge covariance, chi gauge invariance under orthogonal transforms, action gauge covariance/invariance; supports simultaneous constant-conjugation equivariance at the identity background.
- PDF 11, printed p.260, source explicitly states SU(2) is adopted to simplify calculations and its discussion retains a compact gauge-group setting.

**Independently proved algebra (not verbatim source theorem):** source D=L Qtilde, based h with Dh=I, monitored restriction P and zero-extension E give the exact constraint graph C=(I-hD)E, DC=0, PC=I; the reduced covariance's monitored projection S=PC(C*AC)^-1 C*P* collapses to (C*AC)^-1. The reduced Hessian graph expansion follows by writing distinguished coordinates T=-D_d^-1 D_m.

**Independently derived fixed identity-background SU(2) result:** global adjoint conjugation at U=1 forces every bond-to-bond Lie-color block of the real reduced Hessian to be a scalar multiple of I3. Thus reduced precision Q=K tensor I3 and covariance K^-1 tensor I3, when strictly positive in the source Gaussian real domain. Each monitored Lie-vector has a radial 3D Gaussian law, giving the Maxwell survival function erfc(t/sqrt2)+sqrt(2/pi)t exp(-t^2/2). Union bound is valid regardless of bond correlations. No actual K, source eigenvalue, diagonal, volume rate or full RG physical law was calculated.

**Prior repo source lock:** [YM-R81](../passes/YM_R81_MOVING_PROJECTOR_SOURCE_COVARIANCE_AUDIT_20261010.md) and [YM-R82](../passes/YM_R82_COVARIANCE_FIRST_INTERPOLATION_AUDIT_20261010.md) contain existing CMP99/102/116 source-propagator and variance candidates; none was automatically identified with the CMP109 reduced precision C*AC.

**Unverified:** CMP98/CMP102b original printed page equations; CMP109 (0.29),(5.37),(5.42) original image checks; actual background transport/paired Omega,V, determinant/E coupling, Gaussian eigenvalue and two-history normalized defect. No continuum Yang–Mills existence, OS reconstruction or mass-gap theorem. No added numbered bibliography beyond [92].
