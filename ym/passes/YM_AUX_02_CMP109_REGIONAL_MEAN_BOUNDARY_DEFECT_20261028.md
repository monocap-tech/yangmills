# YM-AUX-02 — Exact CMP109 regional mean defect, anisotropic cancellation, and full-constraint counterexample

**Date:** 2026-10-28. **Predecessor:** YM-AUX-01 merged main b10dc06f4e0e12d2452a45b48bdc2c08812f7185. **Type:** derived source-shaped finite identity, explicit rational negative control, conditional geometry gate. **Native cursor:** YM-R150 UNCONSUMED under SOURCE_DATA_HOLD. **Claim:** UNPROVED_RESEARCH_PROGRAM, not a four-dimensional continuum YM/mass gap theorem.

## 0. Question / source boundary

R119 and AUX-01 proved the complete-periodic identity-background derivative of Bałaban CMP109 (0.4) obeys mean(Da)_μ = L mean(a_μ) and hence removes constant Lie-algebra modes from the full-periodic fixed-coarse-average tangent. Is the same statement valid after the coarse links are restricted to a regional set Y? This pass constructs the *exact* boundary defect and an example in the kernel of **all** selected coarse directions with nonzero regional mean.

**Primary paper image inspected for this pass:** CMP109, *Renormalization Group Approach to Lattice Gauge Field Theories I*, printed p.252 PDF index 3 (0.3) and p.253 PDF index 4 (0.4), https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . The true equation defines centered blocks, shortest-order independent endpoint contour averages, an L-long translated bridge, and the outer U(c) factor. The identity-background linearization is the previously derived R119.1; the results below are **new derivations**, not claims printed by Bałaban. We do NOT know that arbitrary Y below is source-admissible CMP109 Ω/Λ, nor have we recovered CMP99 original (3.155)–(3.158).

## 1. Exact regional boundary identity (DERIVATION)

Let L=13, r=6, d=4 or any d≥2, torus T_N^d=(Z/NZ)^d with L|N and enough room for the regions below. Coarse origins are (LZ/NZ)^d and the centered offsets O={-r,...,r}^d. Fine Lie-bond a_μ(x) uses the ordinary positively oriented edge coordinate; all source paths are defined on the **full torus**. For any set Y of coarse origins, B_Y is the disjoint union of fine-site blocks y+O.

Set
`P_a(y)=L^{-d} Σ_{n∈O} av_{π∈G(y,y+n)} a(Γ_{y,y+n})`.
Translation covariance identifies the same function for the endpoint family at y+Le_μ. The exact **full** CMP109 derivative reads
`(Da)_μ(y)=P_a(y)-P_a(y+Le_μ)+L^{-d} Σ_{n∈O}Σ_{j=0}^{L-1} a_μ(y+n+je_μ)` (AUX02.1).

For every Y, including a proper region, the exact finite equality is
```
Σ_{y∈Y}(Da)_μ(y) = L^{1-d} Σ_{x∈B_Y} a_μ(x) + E_{Y,μ}(a),
E_{Y,μ}(a) = E_path+E_bridge,
E_path   = Σ_{y∈Y}[P_a(y)-P_a(y+Le_μ)],
E_bridge = L^{-d} Σ_{x∈B_Y}Σ_{j=0}^{L-1}[a_μ(x+je_μ)-a_μ(x)] .
```
(AUX02.2–3). This uses only the partition of fine sites by centered blocks: every (y,n) appears exactly once. In indicator language,
`E_path=Σ_{z coarse} [1_Y(z)-1_Y(z-Le_μ)]P_a(z)`
and
`E_bridge=L^{-d} Σ_{j=0}^{L-1}Σ_{u fine} [1_{B_Y}(u-je_μ)-1_{B_Y}(u)]a_μ(u)`.
The defects are supported on **coarse-translation boundary** and **fine-bridge boundary**, respectively. This is a *source-map* identity, not the CMP99 Gaussian regional Hessian or a claim of permitted Dirichlet extension.

## 2. Exact rectangular-strip specialization and a surface estimate

Choose μ=1, and Y=I×(LZ/NZ)^{d-1}, where I consists of k consecutive coarse origins in the first direction, with 1≤k≤N/L−1. Let C_⊥=(N/L)^{d-1} be the number of coarse transverse origins. B_Y is then a fine strip of length kL covering **all transverse fine sites**. Translation by L in e1 produces exactly two coarse boundary faces, each with C_⊥ coarse sites. Hence |Y△(Y+Le1)|=2 C_⊥. For each bridge shift j=0,...,L−1, |B_Y△(B_Y+je1)|=2j N^{d-1}; both kL and its complement have length ≥ L.

For any fine Lie field bounded by ||a||_∞ (any norm with triangle inequality), normalized shortest paths give
`||P_a(y)|| ≤ E_n Σ_{ν=1}^d |n_ν| ||a||_∞ = d [r(r+1)/L] ||a||_∞`.
By the exact boundary indicators above,
`||E_path|| ≤ 2 C_⊥ d [r(r+1)/L] ||a||_∞`,
`||E_bridge|| ≤ (L−1) C_⊥ ||a||_∞`.
Therefore
`||E_{Y,1}(a)|| ≤ C_⊥ [(L−1)+2d r(r+1)/L] ||a||_∞`. (AUX02.4)

For **d=4, L=13**, r(r+1)/L=42/13, giving
`BOXED: ||E_{Y,1}(a)|| ≤ (492/13) C_⊥ ||a||_∞.` (AUX02.5)
If all selected first-direction coarse constraints vanish on Y, then |Y|=k C_⊥ and the exact L^{1-d} factor yields
`BOXED: ||mean_{x∈B_Y} a_1(x)|| ≤ 492/(169 k) ||a||_∞.` (AUX02.6)
This is an **O(surface/volume)** necessary bound, not an exact zero, a scale-uniform source estimate, or a uniform spectral gap. In particular k may stay bounded in source regional constructions, and constants alone do not control K.

**Anisotropic exact cancellation:** If ν≠1, Y is invariant under coarse translation by Le_ν and B_Y under fine translations by je_ν. Both defects then vanish exactly:
`Σ_{y∈Y}(Da)_ν(y)=L^{1-d} Σ_{x∈B_Y} a_ν(x)`. (AUX02.7)
Thus transverse constrained means vanish identically, whereas a boundary-normal constrained mean need not.

## 3. Full-selected-constraint counterexample (EXACT NEGATIVE CONTROL)

In d=2 on T_39² with L=13, take **all transverse coarse origins** Y={(0,0),(0,13),(0,26)} and a real Lie-algebra component only in μ=1. Set
`a_1(6,0)=19`, `a_1(7,0)=-13`, all other a_ν(x)=0.
Here (6,0)∈B_Y but (7,0)∉B_Y. Evaluating both normalized shortest endpoint permutations in the **full** linearized CMP109 (0.4) gives the nonzero source-link coefficients at y=(0,0):
`(D δ_{(6,0),1})_1(0,0)=13/169` and
`(D δ_{(7,0),1})_1(0,0)=19/169`.
Both source-link delta fields contribute **zero** to all selected direction-2 coarse links, and to direction-1 coarse links at y=(0,13),(0,26). Thus
`BOXED: (Da)_ν(y)=0 for every y∈Y and BOTH ν=1,2`.
Nevertheless B_Y consists of 13×39=507 fine sites, and
`BOXED: mean_{B_Y} a_1=19/507 ≠ 0`. (AUX02.8)

This is a **complete-kernel** counterexample to directly replacing the *full-periodic* AUX-01 orthogonality statement by a *proper-regional* one. It does NOT show a zero eigenvalue of CMP99 source K and does NOT prove Y is among Balaban's admissible Ω/Λ regions.

[Exact standard-library Fraction certificate](../computations/YM_AUX_02_REGIONAL_MEAN_DEFECT_RATIONAL_20261028.py) has been **executed**, with test output retained separately. It independently tests the full source-shaped 2D D, equality of E_path+E_bridge with the regional defect on a nonconstant field, transverse exact cancellation, the all-direction counterexample, and the 4D surface coefficient.

### 3.1 Four-dimensional lift to **all** coarse orientations (DERIVATION)

The counterexample is not confined to dimension 2. Set N=39 and d=4; take Y={0}×{0,13,26}³ and a fixed nonzero Lie generator T∈su(2). Let the ONLY nonzero bond component be
`a_1(x_1,x_2,x_3,x_4) = [19·1_{(x_1,x_2)=(6,0)} − 13·1_{(x_1,x_2)=(7,0)}]T`
for **every** pair (x_3,x_4), and set a_2=a_3=a_4=0.

Every source shortest path's a_1 integral depends only on the relative order of axes 1 and 2; axes 3 and 4 make no contribution and do not alter (x_1,x_2). The uniform permutation average induces equal probabilities for axis 1 before or after axis 2 when both are active, *regardless of the other active axes*. Thus the d=4 first-variation path average reduces **exactly** to the d=2 one for these fields. Its bridge average also reduces, since the field is independent of x_3,x_4. For coarse directions 3 or 4, the two endpoint averages cancel pointwise by translation invariance, and their bridge components vanish. The previously calculated two-dimensional constraints show D_1a=D_2a=0 at every origin of Y.

Therefore `(Da)_μ(y)=0` for **ALL four directions μ=1,2,3,4 and all y∈Y**, while `mean_{B_Y}a_1=(19/507)T ≠0`. This is an **exact 4D linearized full-source-M counterexample on a declared full torus with selected coarse origins**, *not* an assertion of original-source admissible regional gauge conditions. The 4D reduction is a mathematical permutation/translation proof, not a 39⁴ numerical enumeration. The certificate additionally checks the uniform relative-order permutation combinatorics over all active-axis subsets.

## 4. Operator/jurisdiction cut and next source test

AUX-01 (full periodic): ker D ⟂ constant Lie modes. AUX-02 (proper strip): regional ker(D|Y) need not be orthogonal to constant modes restricted to B_Y; its mean can leak through two explicit interface faces. This **does not resurrect** the constant harmonic whole-torus mode as an exact global null of full D; these are different constraint operators and carriers.

The remaining native transfer must instantiate (i) legal CMP109 Ω, Λ, collars and boundary condition, (ii) full source regional constraint/gauge map and whether its kernel inherits a boundary summation identity, (iii) norm/decay of source extensions across the interface, and (iv) actual exponential-gauge Gaussian precision C* A^(k) C, not merely a projection, along with normalized two-UV laws. None of the original CMP99 operator equations (3.155)–(3.158) were recovered. The finite surface estimate is **not** a regional coercivity proof and has no right to be inserted into the source exponent.

**Disposition:** AUX-02 finite derivation and negative control COMPLETE. Canonical YM-R149 checkpoint stays intact, **YM-R150 unconsumed on SOURCE_DATA_HOLD**. No independent new YM-R151, no physical Yang–Mills existence or mass-gap claim. Paused at **source-region admission and source-precision** boundary.
