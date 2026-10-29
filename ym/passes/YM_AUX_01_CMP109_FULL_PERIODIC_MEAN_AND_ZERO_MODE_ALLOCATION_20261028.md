# YM-AUX-01 — Complete-periodic CMP109 fixed-average zero-mode allocation

**Date:** 2026-10-28. **Status:** EXACT LINEARIZED SOURCE-MAP DERIVATION on a full regular periodic identity-background lattice; no regional or Gaussian-coercivity claim. **Previous:** R119 full source derivative, R124 flat winding retention, R126 topology negative control, R149 precision source hold, EXT-02 flow-stationary flat seam. **Canonical YM-R150 remains UNCONSUMED.** No four-dimensional continuum YM, OS reconstruction or mass gap.

## 0. Question

The earlier flat SU(2) torus witness exhibits nonzero winding holonomy with all plaquettes trivial, even under Wilson gradient flow. Does that *necessarily* leave an unlifted harmonic zero vector inside the constrained CMP109 Gaussian `K=C* A^(k) C`? No: the full coarse field and fixed-average fluctuation are different carriers. R124 §2 warned that coarse averaging *could* remove harmonic modes; this audit resolves that implication **exactly for a complete periodic torus at U=1**.

**Primary printed evidence, original image checked 2026-10-28:** Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP 109 (1987) pp.252–253, (0.3) and (0.4), 54-page source scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf , PDF index 3–4. (0.3) defines centered L blocks and all shortest coordinate-order permutations; (0.4) uses two separately normalized endpoint contour averages, an L-long translated bridge, subtracts the fine reference coarse-length bond in the loop and multiplies by it outside the exponential. Earlier R119.1 derived the exact derivative, and R124.6–R124.7 derived full flat-sector holonomy retention. No new original CMP99 images recovered.

## 1. Complete periodic arithmetic mean identity (DERIVATION)

Use full `T_N^d=(Z/NZ)^d`, odd `L=13` dividing `N` (in the native power-period setting `N=L^m`), and the ordinary real Lie-algebra-valued **positive-axis fine-bond coordinate** `a_mu(x)`. Coarse origins `y` run over `L Z^d/NZ^d`; offsets `n` run over `{-6,...,6}^d`. The maps `(y,n) -> x=y+n` partition the fine sites bijectively. Let `c=(y,y+Le_mu)` and `x'=x+Le_mu`. Assume all source paths and bridges lie on this **complete periodic domain**.

At identity background, R119.1 gives

`(Da)_mu(y)=L^(-d) sum_n { av_Gamma a(Gamma_{y,y+n}) + sum_{j=0}^{L-1} a_mu(y+n+j e_mu) - av_Gamma' a(Gamma'_{y+Le_mu,y+Le_mu+n}) }.`  (AUX01.1)

The two endpoint-path sums cancel **after summing over all coarse origins y**, by translation `y -> y+Le_mu`, and because both use the same normalized source shortest-path families. This cancellation is *not* an individual-path cancellation for arbitrary nonconstant a. Each fine positive-axis `mu` bond occurs in the bridge sum exactly L times: given endpoint bond origin u and j, there is one x=u-j e_mu, and unique (y,n) with x=y+n. Therefore the exact finite identity is

`sum_{y coarse}(Da)_mu(y) = L^(1-d) sum_{x fine} a_mu(x).`   (AUX01.2)

There are `(N/L)^d` coarse sites and `N^d` fine sites, hence, in normalized means,

`BOXED: mean_y (Da)_mu(y) = L * mean_x a_mu(x).`            (AUX01.3)

The equality holds **componentwise in su(2)**, indeed for any real Lie algebra, for every fine-bond a in the identity tangent without any Gaussian measure or Wilson-Hessian assumptions. It is a direct full-source derivative identity, not a putative CMP99 operator identity.

## 2. Exact separation of constant harmonic and constrained Gaussian carriers

Define `H_const={ a_mu(x)=xi_mu for all x, xi_mu in su(2) }`. This is a 12-real-dimensional subspace in 4D SU(2). For a constant field, each source endpoint contour has displacement n, so their contributions in (AUX01.1) cancel **pointwise**, leaving

`(D a)_mu(y)=L xi_mu`.                                          (AUX01.4)

Consequently `H_const intersect ker D = {0}`. More strongly, for *arbitrary* a in `W=ker D`, (AUX01.3) gives `sum_x a_mu(x)=0` for each direction and each color. Thus with the standard translation-invariant positive-bond `ell^2` metric,

`BOXED: ker D is orthogonal to H_const.`                       (AUX01.5)

This is an **exact assignment of the zero-Fourier harmonic sector to the coarse average rather than the fixed-average fluctuation**. It does not assert that *every* infinitesimal winding-loop variation is removed: a nonconstant zero-mean field can still affect an individual loop, and nothing here proves that the source reduced K has a uniform spectral gap on W.

R124 already proved that for a source-admissible **commuting flat field** `U_mu=exp(xi_mu)` (all xi commute), the nonlinear M retains straight L-link holonomy and the complete winding Wilson trace. Thus the two carriers are consistent: global flat holonomy is recorded in full coarse V, while the linearized fixed-V Gaussian excludes the uniform shift. The physical map's nontrivial topology is not itself a covariance singularity.

## 3. Boundary failure and coercivity non-transfer (NEGATIVE CONTROLS)

1. If the source region is a strict Ω/Λ subdomain rather than the whole torus, the endpoint contour translation `y -> y+Le_mu` may leave the eligible origin set, the (y,n) partition may break, and bridge counts acquire **boundary/collar remainders**. Hence (AUX01.3)–(AUX01.5) cannot be copied to CMP99 regional Gaussian or arbitrary CMP109 χ-supported histories without exact Ω/Dirichlet/transport specifications.
2. Fixed-average zero-mode elimination does **not** give quantitative lower coercivity. On any nontrivial finite W one may choose a positive quadratic form `epsilon I_W` with epsilon>0 arbitrarily small; no positive alpha uniform in epsilon follows merely from W being orthogonal to H_const. This is a *logical algebraic counterexample*, not source A^(k).

No claim is made that flat seam witness U^V and trivial U^I are two histories conditioned on **the same full coarse V**. On source-admissible flat fields the full coarse M retains their different holonomies. R126's obstruction targets *local/projection-only data* that omit the relevant global cycle, not the exact full V on a complete eligible coarse torus.

## 4. Executable verification and precise stop

[Certificate](../computations/YM_AUX_01_FULL_PERIODIC_MEAN_AND_CONSTANT_MODE_20261028.py) uses exact fractions, completely evaluates a source-shaped **2D periodic** derivative with normalized shortest-permutation paths on an arbitrary nonconstant fine field, and confirms the aggregate mean identity; it separately checks all `13^4` offsets for the 4D constant-mode pointwise derivative and the general cardinality relation for N=L². The 2D example is a dimensional reduction of the same formula, **not** a 4D native regional proof; the 4D full-periodic argument is the exact counting proof above.

**CLOSED (bounded):** full-torus identity-background, full-source linearized M mean relation and orthogonality of ker D to constant harmonic directions. **NOT CLOSED:** CMP99 original pp427–431 images, actual regional Q'/Ω gauge mean transport, full source K/coercivity, true Gaussian/FP/weight normalizations, two distinct UV histories, continuum OS and positive physical gap.

**Operating decision:** retain R149's canonical checkpoint and **YM-R150 unconsumed SOURCE_DATA_HOLD**. This auxiliary result prevents incorrectly using the global flat-connection witness as a refutation of constrained Gaussian positivity; the remaining numerical source K and regional transfer obligations remain exactly live. Stop auxiliary derivations here rather than manufacturing an R150 checkpoint.
