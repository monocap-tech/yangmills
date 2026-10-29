# YM-AUX-03 — Co-closed regional coarse-null field with nonzero normal mean and curvature

**Date:** 2026-10-28. **Parent:** merged YM-AUX-02 main a60c7a4da17ad3d7d64c41df08f7e0aaf0c0f945. **Type:** exact finite first-variation derivative, fully checked rational witness, negative result against a *naive* Landau-gauge repair of the regional carrier. **Canonical YM-R149 completed; YM-R150 UNCONSUMED / SOURCE_DATA_HOLD.** No claim of source-admissible regional gauge, native CMP99 K positivity/nonpositivity, normalized two-UV laws, continuum OS or mass gap.

## 1. Question and source boundary

AUX-01 proved that the **complete-periodic** CMP109 linearized coarse-link map D exports every constant harmonic bond mode to coarse V. AUX-02 established a regional boundary defect and a field in ker(D|Y) with nonzero regional mean, but did not determine whether ordinary gauge fixing might eliminate that witness. Here the decisive refute-first test imposes **all regional coarse-link constraints** AND the full-torus standard discrete Landau linear condition div a=0, while keeping nonzero regional normal mean.

**Verified primary source:** T. Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP 109 (1987) 249–301; printed p.252 (0.3) and p.253 (0.4), 54-page original scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . Both page images were inspected this pass (PDF indices 3 and 4). Formula (0.4) averages all centered offsets and two independently normalized shortest-permutation endpoint contours, includes the translated L-bond bridge, and uses an exterior reference U(c) factor. At U=1, its exact derivative D is the source-typed map previously established as R119.1. No original CMP99 (3.155)–(3.158) source mathematical image recovered and no numeric native K.

**Model-only constraints:** Standard discrete co-closed condition (div a)(x)=Σ_μ[a_μ(x)-a_μ(x-e_μ)]=0 is a **declared** full-torus identity-background Landau linear condition. It is NOT certified equivalent to CMP109's actual gauge-slice, CMP102's H_k derivative constraints, or CMP99 exponential-gauge fluctuation C.

## 2. Exact witness on source-sized two-dimensional torus N=L²

Set L=13, N=169, T_N²=(Z/NZ)²; Y={(0,13j): j=0,...,12} consists of one coarse x1 plane with **every** transverse coarse origin. Its fine block strip is B_Y={x: x1∈{-6,...,6} mod N}. For an oriented unit plaquette with lower-left vertex z, define the rational circulation q_z on positive-axis links by

`q_z,1(z)=1; q_z,2(z+e1)=1; q_z,1(z+e2)=-1; q_z,2(z)=-1`,

and zero otherwise. This is a single elementary *co-closed circulation*:
`div q_z ≡ 0`. It has nonzero plaquette curl; in the oriented convention
`(d q_z)_12(z)=q_1(z)+q_2(z+e1)-q_1(z+e2)-q_2(z)=4`.

Let h_1(x)=1, h_2(x)=0 be the constant harmonic horizontal field and put

`BOXED: a = h -338 Σ_{j=0}^{12} q_{(7,13j)}.`   (AUX03.1)

The plaquette supports are disjoint, at the first fine x1 column **outside** B_Y. Their horizontal coordinates all equal 7, so the regional mean of a1 over B_Y is **exactly 1**; the full-torus horizontal mean is also 1 because each circulation has zero total oriented link sum. The co-closed equation holds at **every fine site** because both h and all q_z are co-closed.

For the full source-shaped CMP109 derivative (0.4), a constant h has
`(Dh)_1(y)=13; (Dh)_2(y)=0.`
Direct exact-rational evaluation of both endpoint shortest-permutation path averages, outer reference cancellation, and length-13 bridge gives

`(Dq_{(7,13j)})_1(0,13j)=1/26`,
`(Dq_{(7,13j)})_ν(y)=0` for every *other* selected pair (y,ν), y∈Y, ν=1,2.  (AUX03.2)

The nonzero 1/26 comes from the unmatched first-direction endpoint-path term; the bridge contributions from the two horizontal plaquette edges cancel in the selected strip. Since 338/26=13, inserting (AUX03.2) yields the **exact all-constraint identity**

`BOXED: (D a)_ν(y)=0 (all y∈Y, ν=1,2), div a=0 (all x), mean_{B_Y}a1=1.` (AUX03.3)

The field is demonstrably **not pure gauge**:
`(da)_12(7,13j)=-1352 ≠ 0` for each j. Its maximum absolute link component is 339. For any λ>0, the scaled field λa retains all exact linear constraints and nonzero mean λ while ||λa||∞=339λ, so an arbitrary **tangent smallness** threshold does not force the regional mean to vanish. This observation is NOT admission to any original nonlinear source χ_k indicator.

## 3. Four-dimensional source formula lift (DERIVATION)

On T_169^4 use the coarse-origin region
`Y_4={0}×{0,13,...,156}³`.
Extend a_1,a_2 from (AUX03.1) to depend only on x1,x2, and set a3=a4=0. In every source-shortest-path average for directions 1 or 2, the field integral depends solely on the relative order of axes 1 and 2. Uniform permutations of 2–4 active axes induce exactly the d=2 marginal order distribution; displacements and bridge weights in axes 3 and 4 integrate to 1. Hence the true four-dimensional derivative D_1,D_2 restricted to Y4 agrees with (AUX03.2), not just heuristically. For directions 3 and 4, their bridge components are zero and the two endpoint path averages cancel by transverse translation invariance.

Therefore **all four coarse orientations vanish for every y∈Y4**. Full 4D div a=0 by the same 2D divergence identity, the horizontal regional mean remains 1, and plaquette curvature on x1=7 has value -1352. This is an exact symbolic dimension lift, not a 169^4 site brute force or a certified admissible CMP109 Ω/Λ region.

## 4. Independent test and residual obligation

The [standard-library exact rational certificate](../computations/YM_AUX_03_COCLOSED_REGIONAL_L169_RATIONAL_20261028.py) was run locally; [recorded log](../computations/YM_AUX_03_EXECUTION_LOG_20261028.txt) checks all **13×2 coarse constraints**, all **169² co-closed site equations**, the strip mean, curl, maximum norm, and the 4D shortest-permutation marginal combinatorics. The 4D extension is also proved mathematically as above. No numerical matrix, numerical source α, synthetic A_test or 4D actual domain is substituted for CMP99 precision.

**NEGATIVE RESULT (bounded):** even adding the ordinary full-torus Landau condition div a=0 is NOT sufficient, by itself, to repair the loss of mean orthogonality when the source-shaped coarse constraints are restricted to a single complete transverse coarse plane. The boundary circulation can exactly conceal a constant harmonic coarse response on the observed plane.

**LIMIT:** the witness is **not a null vector of the complete-torus D** (coarse links outside Y detect it); it is **not** a zero-energy vector of the full Wilson quadratic action (curvature is nonzero). It cannot prove non-coercivity of K. The precise CMP109/CMP99 gauge/C, source Ω and Dirichlet collars, fluctuations/FP/interaction weight, and two independent UV laws remain open.

**STOP:** Close AUX-03 as a targeted finite negative control. Do not open more ad hoc boundary-counterexample passes without an actual source-region/gauge passport. Canonical YM-R150 remains unconsumed under the source-data stop; no YM-R151 or proof of mass gap.
