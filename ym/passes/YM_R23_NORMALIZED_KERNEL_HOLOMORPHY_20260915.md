# YM-R23 — normalized-kernel holomorphy / zero-free-radius audit

Date: 2026-09-15
Status: COMPLETE -> YM-R24
Claim status: unproved research program

## Target
Test whether the field-dependent normalization problem in the holomorphic matrix-Fisher blocking kernel can be removed by a normalized-by-construction compact-group heat-kernel block map while preserving reflection positivity, gauge covariance, weak-field control, and the Bałaban analytic/polymer architecture.

## A. Heat-kernel mixture candidate
For a coarse oriented link e=(x,y), choose reflection-aligned fine paths gamma_j with the same endpoints and weights w_j>=0, sum_j w_j=1. Let rho_t be the normalized central heat kernel on compact G. Define

K_e(dV_e|U) = sum_j w_j rho_{t_k}(V_e U_{gamma_j}^{-1}) dV_e^Haar,

and K=product_e K_e.

On the physical compact group this is exactly Markov-normalized because each translated heat kernel integrates to one. There is no field-dependent normalizer Z(U), hence no zero-free-normalization obligation.

Gauge covariance follows from endpoint covariance of U_gamma and centrality of rho_t. Reflection covariance follows from inversion symmetry of the heat kernel and a reflected choice of path families. If positive coarse links use only fine paths in the positive half-space, the product kernel conditionally factorizes across the reflection plane, so the reflected-Gram/conditional-factorization criterion from YM-R18 applies.

Hall's compact-group Segal-Bargmann theory supplies holomorphic continuation of rho_t from G to its complexification G_C. Consequently every factor rho_t(V U_gamma^{-1}), and hence the finite convex mixture, has a holomorphic continuation in the complexified link variables. This removes the dagger/Re defect of the matrix-Fisher notation without introducing a U-dependent normalization.

## B. Important analytic convention
Do not require a pointwise holomorphic logarithm of the mixture. The mixture may acquire zeros after complexification. The useful constructive object is the analytic kernel density itself, inserted as a raw local factor/activity before connected-cluster exponentiation. Thus the matrix-Fisher zero-free-log problem is not intrinsic if the RG is organized at density/activity level.

## C. Weak-field expansion
Write U=exp(g_k A), V=exp(g_k B). Let P_j be the linear path-integration operator associated with gamma_j. Choose

t_k = g_k^2/a

(up to the convention-dependent factor in the heat operator), with fixed a>0. The compact-group small-time heat kernel is locally Gaussian, hence

rho_{t_k}(V U_{gamma_j}^{-1}) ~ C_k exp[-(a/2)||B-P_j A||^2] (1 + higher terms).

At quadratic order, because all summands coincide at A=B=0,

S_K^(2)(A,B) = (a/2) sum_j w_j ||B-P_j A||^2.

Define

Q = sum_j w_j P_j,
D = sum_j w_j P_j^*P_j - Q^*Q
  = (1/2) sum_{i,j} w_i w_j (P_i-P_j)^*(P_i-P_j) >= 0.

Then

S_K^(2) = (a/2)||B-QA||^2 + (a/2)<A,DA>.

Thus the normalized heat-kernel mixture does not reproduce the pure M+aQ^*Q Hessian from YM-R19. It adds a positive fine-field path-variance operator D.

## D. Gauge typing of D
For a pure linearized gauge field A=d lambda, every path with the same endpoints has the same integral:

P_j d lambda = lambda(y)-lambda(x).

Therefore (P_i-P_j)d lambda=0 and D annihilates gauge directions. D is a local gauge-invariant curvature-sensitive quadratic form.

For distinct paths, P_i-P_j is the circulation around the closed loop gamma_i gamma_j^{-1}; for smooth fields its first term is a surface integral of F. Hence D generally begins at F^2, i.e. canonical dimension four, not six. With a hypercubic/reflection-symmetric family its dimension-four projection belongs to the same Wilson/F^2 marginal coordinate identified in YM-R21. After that local extraction, the remaining derivative/discretization part begins at dimension six.

This is the price of exact Markov normalization by convex mixing: the zero-free normalizer is removed, but a tree-level marginal normalization generally appears.

## E. Coupling calibration consequence
The heat-kernel mixture may therefore require a tree-level field/coupling calibration before the running coupling coordinate is tangent to the standard Bałaban convention. This is stronger than the O(g^3) finite scheme shift found for the matrix-Fisher candidate. It does not create a new gauge-invariant marginal direction, but it must be explicitly extracted and normalized once.

## F. Small-time holomorphic-growth tradeoff
The new first analytic obligation is not zero-freeness but growth of the holomorphic heat kernel as t_k -> 0. Hall/Driver-Hall-Kemp establish holomorphic continuation to G_C for each t>0. Locally, the Euclidean model shows that continuation in an imaginary Lie-algebra direction Y carries Gaussian growth on the scale exp(C |Y|^2/t).

For complexified group variables exp(g_k(A+iY)) and t_k=g_k^2/a, the g_k factors cancel and the growth scale is schematically

exp(C a ||Y||^2).

Therefore a fixed canonical complex radius is compatible with fixed a. If the Bałaban analytic radius R_k grows with the small-field threshold, the required bound becomes exp(C a R_k^2) and must fit inside the same Cauchy/polymer budget. This has not yet been proved from the primary 4d source.

Making t_k much larger suppresses holomorphic growth but sets a_k=g_k^2/t_k small and weakens the Q^*Q coercive mass used in the Gaussian/random-walk localization. Hence there is a genuine coercivity-versus-holomorphy parameter window.

## Determination
Option B succeeds in eliminating the field-dependent normalization and zero-free-log obstruction:

normalized heat kernel + Haar translation + convex path mixture
=> global Markov normalization
=> holomorphic raw density
=> gauge/reflection covariance
=> reflected half-space factorization.

But two new quantitative obligations remain:

1. extract/calibrate the dimension-four path-variance operator D into the Wilson coupling coordinate;
2. prove a complex-tube heat-kernel growth bound compatible simultaneously with fixed coercive a>0 and Bałaban's analytic Cauchy radius.

The second is now the sharper UV interface.

## Next frontier
YM-R24 — coercivity / complex-tube window audit.

Determine the actual scale dependence of Bałaban's complex analytic field radius and ask whether there exists a fixed or slowly varying a_k such that

(a) M_k + a_k Q_k^*Q_k remains uniformly coercive/localizable,
(b) the holomorphic heat-kernel factors are uniformly bounded on the required complex tube,
(c) the D marginal extraction is uniformly controlled,
(d) the resulting raw activity satisfies the CMP116 Lemma-3 polymer decay budget.
