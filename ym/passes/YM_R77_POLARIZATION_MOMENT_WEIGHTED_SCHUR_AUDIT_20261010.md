# YM-R77 — polarization moment frontier / weighted Schur locality audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior head: YM-R76 (028c3243c59fe77a541b566e60eb732f95dbc81f)
Status: COMPLETE AS A BOUNDED ABSTRACT AUDIT; native source gates OPEN
Next unconsumed cursor: YM-R78
Claim discipline: UNPROVED RESEARCH PROGRAM. No four-dimensional continuum Yang–Mills or positive mass-gap claim.

## 1. Cursor and evidence boundary

R76 proved the finite scalar-pivot Schur implication algebraically and derived a conditional unweighted block perturbation estimate. It established that PSD/strict coercivity by itself entails neither scale covariance, determinant agreement, exponential locality, nor positive-alpha polymer suppression. The exact Prove2Me accepted Lean theorem ID/proof remains unresolved.

R77 returns to the native paired one-step source task. The source-verified geometry inherited from R70 is a_(N,j)=L^(j-N) and a_(N+1,j+1)=a_(N,j). The CMP119 coupling recursion and regular-sector subtraction are recorded in R73-R75; the CMP109 Eqs (5.37), (5.42), (0.29) are STILL NOT primary-extracted. The R75 description of beta through a mixed second derivative of Pi-hat and the V^(j) positive-alpha bound come from the SECONDARY [85] locator, NOT direct source-verbatim evidence.

External access rechecked 2026-10-10: the Rutgers/publisher metadata identifies the 1987 CMP109 article and its small-field one-step beta architecture, but does not display required equation windows. Project Euclid's PDF/full endpoints return an iframe/security check in the available web access; Springer PDF access did not yield equation-readable text. Therefore exact signs, Fourier normalization, source tensor type, gauge convention, operator domains, polymer norms and uniform constants cannot be promoted. Sources [7], [59], [85], [86] reused, no newly numbered reference; highest remains [86].

The following independent mathematical results are deliberately stated for ABSTRACT translation-invariant kernels and lattice matrices. They must NOT be read as claims of Ward identities or of bounds already proven for Yang–Mills.

## 2. A precise mixed-momentum moment theorem — ABSTRACT-DERIVED

Let D: Z^d -> C (or finite-dimensional matrices with an entry norm) satisfy
  M_kappa(D) := sum_(z in Z^d) exp(kappa |z|_1) ||D(z)|| < infinity,
with kappa>0 and |z|_1=sum_i |z_i|. Define the dimensionless lattice Fourier transform
  Dhat(p) := sum_z exp(i p.z) D(z).
Absolute exponential summability permits differentiation term by term (indeed analyticity in a sufficiently narrow complex strip), and yields
  partial_(p_mu) partial_(p_nu) Dhat(0) = - sum_z z_mu z_nu D(z).

Using |z_mu z_nu| <= |z|_1^2 and sup_(r>=0) r^2 exp(-kappa r) = 4/(e^2 kappa^2):
  ||partial_(p_mu) partial_(p_nu) Dhat(0)||
    <= [4/(e^2 kappa^2)] M_kappa(D).

For distinct mu,nu, |z_mu z_nu| <= |z|_1^2/4 gives the sharper prefactor 1/(e^2 kappa^2). Either version is sufficient.

COROLLARY (abstract): if the complete physically aligned one-step polarization difference D_(N,j)(z) is well-defined with common Fourier conventions and M_kappa(D_(N,j)) <= eps_(N,j), and the actual marginal coefficient is a fixed, uniformly bounded linear combination of these second derivatives with appropriate fixed/source-verified normalization, then
  |delta beta_(N,j)| <= C_moment eps_(N,j).
With the R72 tail sensitivity and summability of eps, the corresponding scalar tail is summably controlled. This is a CONDITIONAL NATIVE TRANSFER, not a source theorem.

Scope boundary: the identity presupposes a source-identified Fourier convention and (if appropriate) tensor projections, momentum scaling, finite-volume extension, and gauge/Ward constraints. A continuum or physical momentum derivative may carry powers of lattice spacing. None are silently absorbed into a universal constant.

## 3. NEW COUNTEREXAMPLE — operator norm cannot replace the moment norm

Let d>=2, v=e_1+e_2 and n>=1. On l^2(Z^d) let T_w be translation by w, and set
  K_n := (T_(nv)+T_(-nv))/(2 n^2).
Then K_n is a real self-adjoint convolution operator with Fourier multiplier
  Khat_n(p) = cos[n(p_1+p_2)] / n^2,
so ||K_n||_op = n^(-2) -> 0.
But
  partial_(p_1) partial_(p_2) Khat_n(0) = -1
for every n.

Let P_0=2I and P_n=2I+K_n. These are strictly positive and uniformly coercive (P_n >= I for n>=1), and ||P_n-P_0||_op -> 0, while their mixed second-momentum derivatives differ by 1.

Hence:
  UniformStrictPositivity + OperatorNormCutoffCloseness
  DOES NOT imply
  MixedMomentumJetCloseness.

This falsifies an otherwise tempting promotion from R76's unweighted Schur perturbation estimate to the beta/F^2 extraction. It is a counterexample to the GENERIC IMPLICATION, not a gauge/Ward-compatible Yang–Mills example. The latter needs its own native assumptions.

## 4. Weighted Schur transfer — a genuinely adequate quadratic locality interface

Let I be a finite metric lattice with d(x,z)<=d(x,y)+d(y,z). For compatible matrices of finite-dimensional blocks define
  ||M||_kappa = max(
     sup_x sum_y exp(kappa d(x,y)) ||M_xy||,
     sup_y sum_x exp(kappa d(x,y)) ||M_xy||
  ).
The triangle inequality for d implies ||MN||_kappa <= ||M||_kappa ||N||_kappa; the norm is invariant under adjoint if compatible site metrics are used.

For two physically aligned block Hessians H_i=[[A_i,B_i],[B_i*,C_i]], i=0,1, on a COMMON source-identified retained/eliminated carrier, assume:
  C_i invertible on that carrier;
  ||C_i^(-1)||_kappa <= R;
  ||B_i||_kappa <= K;
  delta A=||A_1-A_0||_kappa, delta B=||B_1-B_0||_kappa, delta C=||C_1-C_0||_kappa.
Write S_i=A_i-B_i C_i^(-1)B_i*. The resolvent identity and a three-term telescoping product give
  ||S_1-S_0||_kappa
    <= delta A + 2 K R delta B + K^2 R^2 delta C.

Proof: add/subtract B_0 C_1^(-1) B_1* and B_0 C_0^(-1) B_1*, use C_1^(-1)-C_0^(-1)=C_1^(-1)(C_0-C_1)C_0^(-1), and the weighted-algebra submultiplicativity. The operator-norm estimate in R76 is the corresponding unweighted version.

A differentiated (momentum-jet) version can be set up with a truncated degree-2 Taylor-jet norm
  J_2(M) := sum_(|alpha|<=2) ||partial_p^alpha M(0)||_kappa / alpha!,
when all objects depend C^2 on momentum in the same coordinate chart. Leibniz' rule makes this a submultiplicative truncated jet algebra. If uniform jet bounds for B_i and C_i^(-1), plus aligned jet differences for A,B,C, hold, the same telescoping formula controls J_2(S_1-S_0). The inverse jet bounds are ADDITIONAL; they follow from differentiation identities only if the weighted inverse itself and its differentiated C data are bounded.

CONSEQUENCE: the proper Schur-locality bridge is
  source-identified block + weighted inverse locality + compatible C^2 jets
  => weighted Schur/jet mismatch control.
Finite PSD and even C_i>=cI do NOT supply the uniform weighted inverse bound R or the differentiated localization data. Neither does the abstract Schur estimate control the background-dependent log det C, gauge Jacobian, vertices, cumulants, or whole polarization tensor.

This places Schur as a conditional auxiliary for one quadratic contribution rather than as a substitute for the primary vacuum-polarization construction.

## 5. Paired marginal/residual bookkeeping: what can and cannot be combined

A complete one-step correction E_j would need a PRIMARY source-defined marginal functional P_j and complementary remainder R_j with
  E_j = [P_j E_j] A_j + R_j E_j,
where A_j is the correctly normalized gauge/Wilson F^2 operator, and the identified coefficient equals the beta extracted from the FULL one-step polarization Pi_j.

Only after that exact source object dictionary may one test, separately:
  (A) physical-scale covariance or summable mixed-jet error for P_j E_j;
  (B) a uniform positive-alpha polymer/locality bound for R_j E_j;
  (C) the first-common-scale interpretation of the extra finest-layer correction, including all normalization, marginal retuning and boundary effects.

The generic 4D root count from R69 remains: under a true native polymer estimate C a^(4+alpha) exp(-kappa d_j(X)), a uniform rooted-polymer summability and root density O(a^-4) produce C' a^alpha for a fixed physical region. This is conditional and cannot be obtained from any Hessian/Schur estimate alone. Source [85] supplies only a SECONDARY candidate, not primary closure.

## 6. Findings and evidence classification

ABSTRACT-DERIVED:
- The mixed-momentum second derivative equals a second spatial moment under weighted summability.
- ExponentialKernelNorm controls the derivative with explicit O(kappa^-2) constant.
- Uniform strict positivity + operator-norm convergence do NOT imply beta-type jet convergence (explicit 4D-compatible translation-convolution example).
- WeightedSchurTransfer and the corresponding jet-algebra conditional estimate follow by algebra.

CONDITIONAL NATIVE:
- Complete-polarization weighted-mismatch => beta mismatch, if the primary tensor, Fourier extraction and uniform source normalization match.
- Weighted gauge-fixed inverse/locality bounds + full block/jet dictionary => quadratic Schur mismatch control.
- Positive-alpha V bound + actual one-layer dictionary + rooted summability => regular endpoint summability.

OPEN PRIMARY/NATIVE:
- Direct CMP109 Eqs (5.37), (5.42), (0.29) extraction and exact domains/quantifiers.
- Full Pi_(N,j) including normalized Gaussian determinant and interaction/cumulants, gauge and localization terms.
- Physical alignment identification of Fourier momentum and source projection; uniform finite-volume jets.
- Native weighted mismatch or exact stationarity for full Pi, not just its reduced Hessian.
- Native Eq029 V definition and alpha>0, and mapping to first-common-scale extra-layer correction.
- Exact P2M theorem UUID/Lean proof custody from [86].

OBSTRUCTED AS GENERIC IMPLICATION:
- finite Schur PSD alone => beta-map covariance;
- unweighted operator-norm closeness of Hessian/polarization => mixed C^2 beta extraction;
- positive Schur Hessian => positive-alpha nonlinear polymer residual.

## 7. Bounded next frontier — YM-R78 (unconsumed)

1. Obtain equation-readable primary CMP109 windows for (5.37), (5.42), (0.29), ideally original page images from the existing source archive, and verify signs, definitions, source normalization and constants; do NOT infer text from secondary [85].
2. Construct a native Pi_j input ledger: fluctuation covariance on gauge slice, determinant, vertex/cumulant contributions, local Taylor/Ward projection, boundary localization, and physically aligned momentum variable.
3. Determine whether the primary proof gives a weighted exponential (or just finite second-moment) control for the FULL one-step polarization and its cross-depth difference. The least demanding sufficient Gate-A input is a summable SECOND-MOMENT defect, not necessarily an exponential norm.
4. Check whether the same Taylor/Ward split identifies the Eq029 complement, its actual alpha and polymer norm, and the one-layer map.
5. Use weighted Schur locality only if native inverse bounds and source operator identifications are supplied; otherwise retain as a non-load-bearing abstraction.
6. Resolve [86] P2M URI/declaration separately; its outcome does not automatically affect Gate A or B.

No continuum existence, OS-axiom verification, or strictly positive mass gap follows. Highest reference remains [86]; next newly introduced source would be [87]. Historical R76 and earlier records remain unchanged.
