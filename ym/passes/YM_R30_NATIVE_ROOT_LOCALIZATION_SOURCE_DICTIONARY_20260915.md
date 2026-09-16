# YM-R30 — native root-localization / source-dictionary audit

Date: 2026-09-15
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Parent: YM-R29
Next cursor: YM-R31

## Question

Can the native Bałaban covariance-root localization package be reduced to already established operator facts, and what exact source/dictionary obligation remains after that reduction?

## Source spine

1. Bałaban CMP89 (1983) proves positivity and exponential decay for Green functions of lattice covariant Laplace operators with external gauge fields, with bounds uniform in lattice spacing. [77]
2. Bałaban CMP95 (1984) studies the Gaussian vector-field theory underlying lattice gauge RG; CMP96 extends the results to restrictions on different scales and to RG transformations of different orders. Existing traversal refs for CMP95/96 remain authoritative.
3. CMP116 (1988), after the product-Gaussian change (2.5)–(2.6), explicitly notes that the integrand remains nonlocal through propagators/operators; it introduces interpolation/weakening parameters, generalized random-walk expansions and a resolvent/series expansion of `(C^(k))^(1/2)`, then defines localized `H(Z,Z0)` and `H(Z)` in (2.8)–(2.10). The external source audit marks this equation range as source-extracted but not yet a completed source-to-project support theorem.
4. Generic analytic matrix-function theory shows that analytic `f(A)` of uniformly sparse/banded matrices inherits exponential off-diagonal decay. [76]

## Operator-level reduction

Let `A_k` denote the gauge-fixed fluctuation precision and `C_k=A_k^{-1}` the covariance. Suppose on the relevant small-field complex domain:

- `A_k=A_k^*` on the real slice;
- `m I <= A_k <= M I` with `0<m<M<infinity`, uniformly in scale/volume;
- `A_k` has uniformly bounded interaction range `R` (or a uniformly exponentially localized kernel);
- the coefficients depend analytically and locally on the background field.

Then

`C_k^(1/2) = A_k^(-1/2)`.

The function `f(z)=z^(-1/2)` is analytic on a neighborhood of `[m,M]`. Polynomial approximation gives polynomials `p_n` with

`sup_[m,M] |f-p_n| <= C q^n`, `0<q<1`.

For finite-range `A_k`, `p_n(A_k)(x,y)=0` whenever `d(x,y)>nR`. Choosing `n` proportional to `d(x,y)` yields

`|C_k^(1/2)(x,y)| <= C' exp(-mu d(x,y))`,

with constants depending only on `m,M,R`, hence uniform if those inputs are uniform. This is the same structural conclusion supplied by general decay theorems for analytic matrix functions. [76]

Thus **off-diagonal root decay is not an independent mystery theorem** once a uniform local/coercive precision certificate is available.

## Stronger background-locality issue

However, CMP116 needs more than kernel decay in `(x,y)`.

A kernel entry `A_k(U)^(-1/2)(x,y)` can depend on background links `U(b)` far from both `x` and `y`. Exponential off-diagonal decay alone does not imply that the dependence on a distant background variable is small or localizable.

For analytic functional calculus,

`f(A) = (2 pi i)^(-1) integral_Gamma f(z) (z-A)^(-1) dz`.

A first background variation in a local precision perturbation `H_b = dA/dU(b)` has the source-shaped form

`D f(A)[H_b] = (2 pi i)^(-1) integral_Gamma f(z) (z-A)^(-1) H_b (z-A)^(-1) dz`.

If the contour resolvents have uniform exponential kernel decay and `H_b` is supported near the bond/block `b`, then the derivative is exponentially small in the distance needed to connect `x`, `y`, and `b`. Higher derivatives give chains of resolvents and local insertions, hence tree-like exponential decay.

This is precisely the analytic mechanism that weakening/interpolation expansions can convert into localized polymer pieces. It explains why CMP116 introduces weakening parameters and generalized random-walk expansions after (2.6), rather than relying merely on an off-diagonal bound for the square root.

## Source-dictionary split

The former single field `root_localization` should be regarded as two logically distinct obligations:

### A. Root operator quasi-locality

Required inputs:

- exact identification of the CMP116 covariance/precision with the CMP95/96 operator family;
- uniform coercivity/spectral window;
- uniform finite-range or exponentially localized precision/resolvent constants;
- normalized square-root convention.

Given these, root kernel decay is derivable by analytic functional calculus rather than requiring a separate finite root-piece identity.

### B. External-background localization and support dictionary

Still required:

- uniform complex-background resolvent bounds under weakening parameters;
- locality of precision derivatives with respect to background links;
- summable higher derivative/tree bounds;
- exact enlargement convention for the domain `Z`/special domain containing `Z0`;
- map from Bałaban's localized external-field dependence to project `activeSupport`, `fluctuationSupport`, and polymer metric;
- component factorization corresponding to CMP116 (2.10).

This second package is not supplied by CMP89/CMP95/CMP96 off-diagonal Green decay alone.

## Negative result

Do not identify `exponential kernel decay of C^(1/2)` with the full CMP116 `root_localization` hypothesis. The latter includes localization of dependence on external gauge fields and support/enlargement data.

Do not assert an exact finite decomposition of the square root. CMP116 uses an infinite/resummed generalized random-walk/resolvent expansion.

## Determination

The native root-localization deficit has been reduced from one opaque theorem to:

`uniform complex resolvent/precision locality`
`+`
`weakening-derivative/tree decay`
`+`
`support/enlargement dictionary`.

The first spatial root-decay component is structurally derivable from uniform coercivity/locality and analytic functional calculus. The real remaining mathematical/source interface is **background-field quasi-locality under weakening** and its exact conversion into CMP116 localization domains.

## Next frontier

YM-R31 — complex-background resolvent derivative / weakening-interpolation audit.

Tasks:

1. Extract the complex-background propagator/resolvent bounds from CMP95/96/99 and determine their uniform spectral domain.
2. Differentiate the precision/resolvent with respect to a local background link and obtain one-insertion exponential decay.
3. Extend to multiple weakening/background derivatives and identify the tree metric generated by the resolvent chain.
4. Compare that tree metric and enlargement to CMP116 (2.7)–(2.10) `Z0 -> Z` localization.
5. Determine whether this closes `root_localization` up to only a finite source-to-project support dictionary.
6. New references begin at [78].

## Safety boundary

No proof of 4d Yang–Mills existence or mass gap is claimed. R30 is a source/functional-calculus reduction of one constructive-RG interface.
