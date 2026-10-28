# YM-R146 — Cutoff-aware pivot exchange and constrained Gaussian coordinate custody

**Date:** 2026-10-28. **Previous conversational:** YM-R145 (retrospectively archived). **Canonical predecessor:** YM-R126, commit 7860c7c, with R127–R145 now separately recorded as typed retrospective passes on this branch. **Current cursor:** YM-R146; **next:** YM-R147 (not consumed). **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Target and evidence boundary

R143 showed an exact common distinguished-bond coefficient on a declared aligned identity-background L=13 one-step model; R145 showed that the old transverse pivot a and the native CMP109 center pivot b are distinct and that simply copying the same coordinate-box cutoff is invalid. R146 asks: *what is the exact chart transition on a single constrained bond space, what happens to Gaussian determinants, and which cutoff event is preserved?*

Primary Bałaban CMP109 original printed pages **266–268**, equations (2.9)–(2.14), rechecked by printed-page images in the 54-page third-party-hosted scan: https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . Eq. (2.9) monitors B′ on all fine bonds **excluding b0(c)**; p.267 builds h supported on those b0 bonds and a linearized δ constraint; p.268 eliminates b0 and uses a Gaussian covariance `(C* A^(k) C)^(-1)`, retained nonlinear χ, Jacobian, interaction and background-dependent normalization. This is image evidence for SOURCE TYPES, not a proof of two-history measure equivalence.

Historical CMP95 (1.7)–(1.8), CMP98 (14)–(15), and CMP99(3) (3.155)–(3.158) are third-party original-paper transcriptions, **not independently original-image-verified here**; the CMP99 precision symbols in (3.157)–(3.158) are damaged. Source histories' Ω/collar, exact old/current gauge and nonlinear charts remain unconstructed.

**Jurisdiction correction:** An exact pivot change for ONE fixed linear constraint D is not the same map as R143's S between *different* old/new constraint maps. R146 does NOT identify historical CMP99 χ with the hypothetical box deleting a.

## 1. Exact pivot-exchange theorem on a fixed constrained carrier

Let H be a finite-dimensional real bond-coordinate space (one color component initially), D:H→R a surjective scalar linearized coarse constraint. Select distinct bond variables a,b with nonzero D coefficients κ_a, κ_b. Let z denote all remaining coordinates. In components,

  D(B)=κ_a B_a+κ_b B_b+ℓ(z).

Chart X eliminates a: x=(B_b,z) and solves

  B_a=−(κ_b/κ_a) B_b−ℓ(z)/κ_a.

Chart Y eliminates b: y=(B_a,z) and solves

  B_b=−(κ_a/κ_b) B_a−ℓ(z)/κ_b.

On the SAME physical slice ker D, the chart change y=T x is exactly

  T(B_b,z)=(−(κ_b/κ_a)B_b−ℓ(z)/κ_a,z).      (R146.1)

The matrix is triangular with

  det T = −κ_b/κ_a,   |det T|=|κ_b/κ_a|.      (R146.2)

Both charts are bijective since κ_aκ_b≠0. For su(2) at the identity, each coefficient acts on three real colors; the total real Jacobian magnitude is |κ_b/κ_a|^3 for this one-bond pivot exchange. For multiple disjoint coarse constraints, these factors multiply *only if* the full pivot block system is actually diagonal/triangular; CMP99's nested regional pivot system is not established.

For the one-step aligned interface model, κ_a=κ_b=1/L³, L=13; hence

  |det T|=1,  L³=2197.                          (R146.3)

This is an exact finite-coordinate statement in the declared model; the native CMP99→CMP109 two-constraint chart is NOT identified by (R146.3).

## 2. Quantitative norm obstruction despite determinant one

Restrict to the N=L³ crossing e1 bonds of a coarse interface, all having coefficient 1/N, and zero out all other fine bonds. In chart X there are N−1 retained crossing components: x=(x_b,z_1,…,z_{N−2}); chart Y is

  y=(-x_b−sum_i z_i,z_1,…,z_{N−2}).

The singular values of this Euclidean chart-change matrix are 1 with multiplicity N−3 (when N≥3), and sqrt(λ_±), where

  λ_± = [N ± sqrt(N²−4)]/2,  λ_+λ_−=1.      (R146.4)

Proof: on the z-direction orthogonal to the all-ones vector T is the identity; on span(x_b, mean z), T has matrix [[-1,-sqrt(N−2)],[0,1]], whose T*T has trace N, determinant 1. At N=2197,

  ||T||_2 = sqrt([2197+sqrt(2197²−4)]/2) ≈ 46.87216.

Thus an ambient chart Jacobian magnitude 1 is not a near-isometry. On the FULL source bond chart, additional contour coefficients may enlarge the norm; the interface restriction only gives a lower bound. Since L=13 is fixed, this does not by itself prove UV-depth growth, but it forbids claiming a depth-uniform bound merely from determinant one.

## 3. Gaussian coordinate and determinant identities

Let C_a,C_b be the linear embeddings of the two coordinate charts into the same physical slice, so B=C_a x=C_b y and C_a=C_b T. Let H₀ be any fixed positive quadratic form on this slice, with reduced precision Q_a=C_a* H₀ C_a, Q_b=C_b* H₀ C_b. Then exactly

  Q_a=T*Q_b T,  det Q_a=|det T|² det Q_b.      (R146.5)

For any measurable full-bond function F with integrability,

  ∫ F(C_a x)e^{−x*Q_a x/2}dx
   = |det T|^{−1}∫F(C_b y)e^{−y*Q_b y/2}dy.  (R146.6)

The factor is correct because dy=|det T|dx. After including the Gaussian normalizers det(Q_i)^{1/2}/(2π)^{n/2}, the induced normalized Gaussian law of the SAME full field B is identical in either chart. In the L13 one-step equal-pivot case |det T|=1. The induced Euclidean slice-volume factor sqrt(det C* C) also transforms by |det T| and does not create a physical discrepancy when carried consistently.

Crucially these are **coordinate-invariance identities**, not equality of Gaussian laws from two different source histories or differently gauge-fixed Hessians. The CMP109 V-dependent Gaussian factor `Z^(k)(U_{k+1})/Z^(k)(1)` and the full nonlinear fluctuation integral still enter the coarse effective action.

## 4. Physical cutoff pullback is not a second coordinate box

Source CMP109 χ_b removes its SOURCE pivot b and bounds every other monitored B′ bond. Its representation in chart X is

  χ_b(C_a x) = 1{ |B_a(x)|<θ } · product_{e≠a,b}1{ |B_e(x)|<θ },   (R146.7)

with the actual Lie norm and all source bonds understood. Here B_a(x) is the linear combination in (R146.1); it is not an independent coordinate box. A HYPOTHETICAL χ_a omitting a instead would be 1{|B_b|<θ}·product_{e≠a,b}1{|B_e|<θ}.

On four crossing bonds a,b,z₁,z₂, with all other components zero and one common Lie color,

  (a,b,z₁,z₂) = (6/5,0,−3/5,−3/5)θ,  D(B)=0.

Then χ_a(B)=1, χ_b(B)=0 strictly. The inequalities have slack, so this difference contains a relative-open set of the constraint slice and has positive probability under EVERY nondegenerate centered Gaussian on that slice. Neither Gaussian coordinate equality nor a unit Jacobian makes the two hard cutoff events equal.

This is a negative control **between a hypothetical old-pivot box and the literal CMP109 omitted-bond pattern**, not a claim that CMP99 defines χ_a or that the actual old/new physical laws differ this way. The source χ_b can be transported EXACTLY by its pullback (R146.7); one may NOT replace it by χ_a as a convenience without estimating the induced probability defect.

## 5. Relation to R142–R145 and native stopping point

- R142/R143's S maps between two *different* constraint functions under a common chosen right inverse. R146's T changes *which variable is eliminated* on one fixed constraint slice. An actual CMP99→CMP109 probabilistic comparison needs both maps on a common physical graph and all coarea/FP/interaction weights.
- R143's statement P S=P is true for its chosen old-pivot P and h, but says nothing about the SOURCE CMP109 projection deleting b. The earlier wording must not be read as preserving both.
- R144's determinant-one tower under common per-scale inverses remains a conditional abstract theorem. It cannot be promoted to measure transport without the actual Ω/Λ shell incidence, cutoff pullbacks and chart norms.
- R145's witness remains valid with its explicitly hypothetical χ_a reading, and is strengthened to a positive-measure discrepancy under any full-support Gaussian on the fixed slice.

**Closed in this pass:** exact one-slice pivot-exchange, Jacobian, reduced-Gaussian congruence, cutoff pullback, norm and four-bond negative controls. The [computation](../computations/YM_R146_PIVOT_EXCHANGE_RATIONAL_20261028.py) independently checks the finite arithmetic and 3×3 chart involution.

**OPEN native gates:** actual CMP99/CMP109 old/new common physical chart and full regional Ω; CMP99 precise (3.157)–(3.158) reduced precision; native nonlinear gauge-change Jacobian; full truncated source mass / cutoff exit and background action; two distinct UV histories' relative E/determinants; the four-dimensional continuum theory and positive mass gap.

**Next YM-R147 (not consumed):** construct the source-exact composite transport *between both constraints and both native deleted-bond conventions* on a full eligible regional block. Explicitly pull back CMP109 χ (2.9) and quantify its normalization alongside CMP99's true gauge/precision law. Do not infer a two-UV physical probability statement from the one-step finite model.
