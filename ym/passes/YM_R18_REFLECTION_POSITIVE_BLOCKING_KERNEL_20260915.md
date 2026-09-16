# YM-R18 — reflection-positive blocking kernel

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R19 (quadratic matching / weak-field kernel closure)
Claim status: research traversal only; no Yang–Mills solution claim.

## 1. Target

Test whether a positive local gauge-covariant blocking kernel can replace the globally overconstrained deterministic group-valued average identified in YM-R17 while preserving Osterwalder–Schrader reflection positivity and remaining compatible with weak-field constructive RG.

## 2. Correction to YM-R17 abstract kernel claim

The conditions

- `K* Theta' = Theta K*`, and
- `K*(A'_+) subset A_+`

are **not sufficient by themselves** for a stochastic/Markov blocking kernel. The reason is algebraic: unlike deterministic pullback by a map `Q`, a Markov operator `K*` is not multiplicative, so in general

`K*((Theta' F) G) != (Theta K*F)(K*G)`.

A two-spin counterexample records the failure. Take a one-point fine configuration space (hence trivially RP), and a coarse pair `(v_-,v_+) in {+1,-1}^2` with reflection exchanging the two components. Let the kernel put probability `1/2` on `(+1,-1)` and `1/2` on `(-1,+1)`. It is reflection invariant, but for the positive-side observable `F(v_+)=v_+`,

`E[F(v_-) F(v_+)] = -1`,

so coarse reflection positivity fails.

## 3. Correct sufficient criterion: reflected Gram factorization

Let

`B_mu(f,g) = integral over U of conjugate(f(theta U)) g(U) dmu(U)`

be the fine RP form. Let `K(U,dV)` be a Markov kernel and `nu = mu K` the coarse measure. A sufficient condition is the existence of a positive measure space `(Lambda,rho)` and linear maps

`L_lambda : A'_+ -> A_+`

such that for every coarse positive-side pair `F,G`,

`integral conjugate(F(theta' V)) G(V) K(U,dV)`

`= integral_Lambda conjugate((L_lambda F)(theta U)) (L_lambda G)(U) rho(dlambda)`.

Then

`B_nu(F,F) = integral_Lambda B_mu(L_lambda F,L_lambda F) rho(dlambda) >= 0`.

This is the correct stochastic replacement for multiplicative deterministic pullback.

The probabilistic/Markov role in reflection positivity is consistent with Jorgensen–Tian [63], who emphasize that a suitable Markov property implies OS positivity.

## 4. Product half-space kernel corollary

A particularly useful sufficient structure is conditional factorization across the reflection halves. Ignoring or conditioning separately on reflection-plane variables, suppose

`K(U,dV) = K_-(U_-,dV_-) K_+(U_+,dV_+)`

and reflection covariance identifies `K_-` with the reflected copy of `K_+`. For `F,G` depending only on coarse positive-side variables,

`K*((Theta' F)G)(U)`

factorizes as

`conjugate((K_+*F)(theta U)) (K_+*G)(U)`.

Since `K_+*F` depends only on fine positive-side variables, fine RP implies coarse RP.

Thus the operative kernel contract is stronger than mere reflection covariance:

**reflection covariance + positive-half-space support + conditional factorization (or, more generally, reflected Gram factorization).**

## 5. Concrete global gauge kernel

A standard soft lattice-gauge blocking form supplies a better candidate than the geodesic-distance barycenter proposed in YM-R17.

For each coarse oriented link `e=(x,y)`, choose a finite reflection-compatible family of fine paths `P_e` from `x` to `y`, with weights `w_gamma`, and set

`Q_e(U) = sum_{gamma in P_e} w_gamma U_gamma`.

Here `Q_e(U)` is a matrix, not necessarily a group element. Define

`k_e(dV_e|U) = Z_e(U)^(-1) exp[ beta kappa Re Tr(V_e Q_e(U)^dagger) ] dV_e(Haar)`

for `V_e in G`, and set

`K(dV|U) = product_e k_e(dV_e|U)`.

This is globally defined on compact `G`; no logarithm, cut locus, Karcher branch, or global deterministic group mean is required.

A closely related gauge blocking kernel is standard in the fixed-point-action literature. Holland–Ipp–Müller–Wenger [66] use

`T[U,V] = -kappa sum_e { Re Tr(V_e Q_e^dagger) - N_e }`

inside an exact RG integral, with a normalization term chosen so that integrating over coarse links preserves the partition function. Their blocked matrix `Q` is built from smeared path matrices and is explicitly noted not necessarily to lie in `SU(N)`.

## 6. Gauge covariance

If path holonomies transform at the endpoints as

`Q_e(U^g) = g_x Q_e(U) g_y^(-1)`,

then simultaneous change of variable

`V_e -> g_x V_e g_y^(-1)`

leaves Haar measure invariant and preserves

`Re Tr(V_e Q_e^dagger)`.

Hence the kernel is exactly endpoint-gauge covariant.

## 7. Reflection covariance and half-space support

Choose the block lattice and path families so that

`Q_{theta e}(theta U) = Q_e(U)^dagger`

with the appropriate orientation convention. Since

`Re Tr(V^dagger Q) = Re Tr(V Q^dagger)`,

the one-link kernel is reflection covariant.

If every positive coarse link uses only fine paths lying in the positive half-space, then the product kernel separates into positive and negative coarse-link factors. The product-half-space corollary then proves preservation of RP.

This condition must be checked for the actual block geometry. The RGT-III example in [66] receives contributions from all gauge links in an associated hypercube, so that published implementation is evidence for a global gauge-covariant soft kernel, **not** by itself a proof of the required half-space support.

## 8. Weak-field scaling

The soft kernel automatically hardens in the asymptotically free regime because the blocking term is multiplied by `beta ~ g^(-2)`.

Near a regular weak-field configuration, write the maximizing coarse group element as `q_e` and `V_e=q_e exp(X_e)`. If `Q_e` is close to a positive scalar multiple `c_e q_e`, then

`Re Tr(V_e Q_e^dagger)`

has a nondegenerate maximum at `X_e=0` and

`- beta kappa Re Tr(V_e Q_e^dagger) = const + (beta kappa c_e/2) ||X_e||^2 + higher local terms`.

Thus the conditional width is

`||X_e|| = O((beta kappa)^(-1/2)) = O(g)`

for fixed positive `kappa`.

At quadratic order in Lie-algebra variables this is a Gaussian block penalty of the form

`(beta kappa c/2) || B - Q_lin A ||^2`,

which is exactly the structural form used in rigorous Gaussian block-spin RG. Balaban–Feldman–Knörrer–Trubowitz [64] explicitly implement block spin by inserting a normalized Gaussian integral coupling the next-scale field to the averaged current-scale field.

The fixed-point gauge literature likewise states that the `beta -> infinity` limit of the soft blocking integral becomes the corresponding saddle-point/minimization equation [66].

## 9. Soft versus hard blocking precedent

Soft blocking is not intrinsically hostile to rigorous locality. In an exact free-fermion comparison, Balaban–O'Carroll–Schor [65] treat both exponential-weight and delta-function block averaging; the exponential-weight RGT has the expected scale-uniform exponential decay after rescaling, whereas the delta-function version does not have uniform exponential decay.

This is not a theorem for non-Abelian Yang–Mills. It is evidence that replacing a hard constraint by a normalized soft kernel can improve, rather than automatically degrade, RG locality.

## 10. Bounded determination

YM-R18 establishes:

1. The naive stochastic RP theorem from YM-R17 was too weak; covariance and positive-side mapping alone do not suffice.
2. A reflected Gram-factorization / half-space Markov-factorization criterion does suffice.
3. A globally defined gauge-covariant soft matrix kernel exists in a standard lattice-gauge RG form and evades the global group-mean topology obstruction.
4. With reflection-aligned local path support, that kernel satisfies the sufficient RP factorization criterion.
5. Its weak-field width is naturally of order `g`, and its quadratic expansion has the expected Gaussian block-spin structure.
6. No theorem in the audited literature shows that substituting this reflection-adapted soft gauge kernel into Bałaban's four-dimensional non-Abelian constructive RG preserves the full inductive estimates.

The remaining obstruction has therefore moved from global definition/RP to **weak-field closure of the modified kernel inside the constructive RG norm**.

## 11. Next frontier — YM-R19

**Quadratic matching / weak-field kernel closure.**

Audit the linearized Bałaban gauge block transformation and compare it directly with the Hessian of the soft matrix kernel. Required checks:

- exact quadratic coefficient and normalization;
- gauge-zero-mode handling / gauge fixing;
- induced covariance and Schur-complement operator;
- reflection-aligned support of the linear averaging map;
- size and locality of cubic/higher nonlinear remainders;
- whether those remainders fit the Bałaban inductive polymer/action norms with cutoff-uniform constants.

Canonical transition:

`YM-R18 COMPLETE -> YM-R19`.
