# YM-R80 — additive terminology registry

Date: 2026-10-10
Prior cursor: YM-R80 from ym/checkpoints/YM_HEAD_R79_20261010.json
Rule: historical terminology unchanged; new definitions entered with first load-bearing use.

- FinitePropagationPrecision: a finite-dimensional self-adjoint lattice precision C with C_xy=0 whenever metric separation d(x,y)>ell_C. This is distinct from merely sparse representations in arbitrary coordinates.
- UniformSpectralCorridor: m I <= C <= M I with 0<m<=M independent of cutoff depth, volume and permitted backgrounds in one fixed canonical normalization. Both lower and upper estimates matter.
- ConstrainedProjectorP: a fixed orthogonal projection onto the actual homogeneous gauge/block fluctuation slice, expressed in the physical site/bond Hilbert space. A local constraint operator Q does not imply its kernel projector P is local.
- FinitePropagationProjector: ConstrainedProjectorP with P_xy=0 when d(x,y)>ell_P, ell_P uniformly bounded. This is a sufficient condition, not asserted to hold in Bałaban's gauge choice.
- AugmentedConstrainedPrecision: A=P C P+(I-P), positive on the full ambient Hilbert space and block diagonal with respect to ran P and ker P.
- EmbeddedConstrainedCovariance: X_P=P A^-1 P, the inverse of C restricted to ran P, embedded back into the physical site/bond carrier.
- NeumannLocalInverseEstimate: spectral corridor plus finite propagation gives block decay of A^-1 via the uniformly convergent geometric expansion (1/M') sum_(k>=0)(I-A/M')^k.
- AlignedPrecisionDefect: epsilon_N=||C_(N+1,j+1)-C_(N,j)|| on a source-identified common physical carrier and fixed projector, NOT implied by the equality of physical spacings.
- ConstraintProjectionLocalityGate: verify locality (finite propagation or quantitatively sufficient decay) of the native gauge/block-slice projector or obtain an alternative direct constrained-propagator estimate. OPEN for the native Yang–Mills model.
- LocalConstraintNonlocalProjectorObstruction: a nearest-neighbor difference constraint has a global constant-field kernel projector; local constraints plus ambient positivity do not imply local constrained Gaussian polarization.
- PrimaryCMP109EquationWindow: authentic original equations (5.37), (5.42), (0.29), adjoining definitions and parameters; still uninspected in this pass.

Status labels: ABSTRACT-DERIVED applies only to proved finite-dimensional math with explicit hypotheses; CONDITIONAL-NATIVE requires verified CMP109 source carrier, constraint and constants; OPEN-PRIMARY means no equation-level primary text recovered. No mass gap or continuum existence claim.
