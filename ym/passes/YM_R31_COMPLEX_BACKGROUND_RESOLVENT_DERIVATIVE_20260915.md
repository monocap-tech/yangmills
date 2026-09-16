# YM-R31 — complex-background resolvent derivative / weakening-interpolation audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R32
Claim status: UNPROVED_RESEARCH_PROGRAM

## Entry state

YM-R30 decomposed the native covariance-root localization obligation into three pieces:

1. root-kernel off-diagonal decay;
2. background-field quasi-locality / weakening derivatives;
3. the source-to-project support/enlargement dictionary.

The R31 target is the second piece.

## 1. Functional-calculus reduction

Let `A_k(U)` denote the gauge-fixed local precision operator on the weak-field complex chart, and let

`R_z(U) = (z - A_k(U))^{-1}`.

For `f(lambda)=lambda^{-1/2}`, the covariance root is

`C_k(U)^(1/2) = f(A_k(U))`

through the analytic functional calculus on a contour Gamma enclosing the spectrum and avoiding the negative/zero branch region:

`f(A) = (1/(2 pi i)) integral_Gamma f(z) (z-A)^(-1) dz`.

The first background variation in a local direction `H = D A[delta U]` is

`D f(A)[H] = (1/(2 pi i)) integral_Gamma f(z) R_z H R_z dz`.

Higher variations are finite sums of resolvent chains. If `A(U)` is nonlinear in the link variables, the chain rule adds higher local derivatives `D^m A`; schematically,

`D^n f(A) = sum R_z (D^{m_1}A) R_z ... (D^{m_r}A) R_z`,

with `m_1+...+m_r=n`, summed over the relevant partitions/orderings. Higham–Relton [78] is used only as a general matrix-function control source for existence/continuity of higher Fréchet derivatives; the lattice locality statement below is a project derivation.

## 2. Local insertions force tree decay

Assume on the complex small-field tube:

- `A_k(U)` has finite interaction range uniformly in scale;
- each link derivative `D^m A_k(U)[b_1,...,b_m]` is supported in a bounded neighborhood of the insertion bonds;
- the contour resolvent has a uniform weighted kernel bound

  `|| chi_x R_z(U) chi_y || <= C_R exp(-mu d(x,y))`

  for `z in Gamma`, all admissible complex `U`, and all UV scales under consideration.

Then a resolvent chain with insertions supported near `b_1,...,b_n` is bounded by a product of exponential factors along an ordered route through the endpoints and insertion neighborhoods. The length of any such ordered route dominates the minimal tree length `T(x,y,b_1,...,b_n)` connecting those sets. Summing the finitely many partitions and permutations therefore yields, after an arbitrarily small decay-margin loss,

`|| D_{b_1}...D_{b_n} C_k(U)^(1/2)(x,y) ||`

`<= n! K^n exp(-mu' T(x,y,b_1,...,b_n))`,

for some `mu'<mu` and scale-uniform `K`, provided the local derivative norms of `A_k(U)` are uniformly bounded.

The factorial growth is the expected analytic growth. In the weakening/Taylor interpolation, the corresponding `1/n!` coefficients cancel it, leaving a geometric/tree expansion controlled by the exponential weights.

## 3. Complex-background resolvent gap

For real weak backgrounds, Bałaban’s propagator program already supplies positivity/Green-function decay inputs; the project source ledger also records CMP99 Theorem 3.12 as external-gauge-field propagator stability under its regularity conditions, and Theorem 3.15 as exponential covariance decay.

The complexified problem can be reduced to a small operator-norm perturbation if the precision depends analytically and locally on the links. If the real precision satisfies

`A_k(U_real) >= m I`

with `m>0` uniform in the weak-field induction, and

`|| A_k(U_complex)-A_k(U_real) || <= c delta`

on a complex tube of radius `delta`, then choosing `c delta < m/2` gives a volume-uniform resolvent contour separated from zero by a fixed margin. Finite range/local bounded coordination is essential here: a sup-norm link perturbation changes the operator norm by an `O(delta)` amount independent of volume.

This provides the correct abstract mechanism for extending the resolvent-chain bounds from real regular fields to a fixed complex tube. R31 does not source-verify that all these operator-norm hypotheses have already been proved for the exact 4d Bałaban Yang–Mills precision.

## 4. What CMP116 still adds

The calculus above shows that, once the uniform complex resolvent estimate and local precision-derivative bounds are available, the background derivatives of the covariance root automatically have the tree-decay structure needed by a weakening expansion.

Therefore the CMP116 localization step is no longer an independent mysterious square-root theorem. Its genuinely model/source-specific content is narrowed to:

- the exact complex weak-field regularity/coercivity domain for the 4d gauge precision;
- uniform local derivative bounds for that precision and its restricted versions;
- the chosen weakening/interpolation variables and their domain-enlargement convention;
- the summability constants translating tree-decaying root derivatives into `H(Z,Z0)` and `H(Z)`;
- the exact source-to-project support dictionary.

## 5. Source alignment

The existing source ledger is consistent with this decomposition:

- CMP99 defines the background-field propagator `G(U)=(Delta_a|Omega_0)^(-1)` and records Green-function estimates;
- CMP99 Theorem 3.12 is visually/source-confirmed as an external-field stability theorem under regularity assumptions;
- CMP99 Theorem 3.15 is recorded as exponential covariance decay;
- CMP116 (2.7)–(2.10) performs the actual external-field localization with interpolation/random-walk/resolvent machinery and constructs `H(Z,Z0)` and `H(Z)`;
- the project correctly keeps `covariance_root_certificate` and `root_localization` as separate source fields because the exact 4d dictionary and constants are not yet installed.

No claim is made that the generic functional-calculus argument substitutes for those primary-source constants.

## Determination

R31 closes the *mechanism* of background-root differentiation:

`uniform complex resolvent decay + local precision derivatives`

`=> factorially analytic tree-decaying derivatives of A^(-1/2)`

`=> weakening/Taylor localization with no loss of coupling power`.

Thus no new analytic species is required for the covariance root. The live obstruction is now upstream: establishing/source-identifying a UV-uniform complex coercivity/resolvent certificate and local derivative bounds for the exact Bałaban 4d gauge precision.

The support/enlargement dictionary remains downstream and untouched.

## Negative results / guardrails

- Do not infer complex-background resolvent bounds merely from real positivity; a fixed complex-tube perturbation theorem is still required.
- Do not identify off-diagonal root decay with external-field support locality.
- Do not assert an exact finite root-piece decomposition; CMP116 uses an infinite/resummed weakening/random-walk construction.
- Do not use Higham–Relton [78] as a Yang–Mills locality theorem; it supplies only general matrix-function derivative regularity.

## Next frontier — YM-R32

**Complex precision/coercivity / exact source-domain audit.**

Extract the actual Bałaban small-field complex domain for the 4d gauge precision and determine whether there is a scale/volume-uniform constant `m>0` and tube radius `delta>0` such that:

`Re <v, A_k(U) v> >= m ||v||^2`

(or an equivalent resolvent-sector bound) for all admissible complex `U`, together with local analytic derivative bounds on `A_k(U)`.

If this closes, R31 turns the covariance-root weakening derivative estimates into a derived package; the remaining native root frontier would then be almost entirely the source support/enlargement dictionary.

Highest reference ID: [78]. Next new source: [79].
