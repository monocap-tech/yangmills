# YM-R150 — Full one-coarse-link dual support, bridge cancellation, and historical-contour defect

**Date:** 2026-10-31. **Predecessor:** merged R150 directional transfer PR #45, main 2fd97ba00ed05d80a022c031c9c73f19d6b220e0. **Claim type:** exact rational/combinatorial source-shaped one-step calculation and CONDITIONAL covariance consumer; explicit negative correction to treating the sparse F as the full chart. **Native YM-R150 IN PROGRESS/UNCONSUMED; R149 is still the canonical machine checkpoint.** No 4D continuum Yang–Mills or spectral mass gap claimed.

## 0. Source geometry and jurisdiction

Primary printed CMP109(1987) p253 (0.4): nearest-bridge coarse link with independently symmetrized shortest contours on centered L^4 blocks; printed pp266–268 (2.9)–(2.12): source special-bond omission and constrained Gaussian. Earlier original-image receipts R120–R121 and R148 cover these definitions. Historical CMP98(1985) p19 (15) selects old paths; CMP95 (1984) (1.7) gives descending axes d,...,1; these old formulas were retrieved in third-party original-paper OCR and are not claimed original-image rechecked this turn. R120 defines old-to-center endpoint paths tau. User-provided ORIGINAL CMP99 printed p428 (3.155)–(3.158) and p432 Theorem 3.15 (3.185)–(3.187) certify the **historical** graph B=C_o y and full covariance C_old^(k)(Lambda) with exponential decay, under the paper hypotheses.

**This calculation is the full FIRST-DERIVATIVE ROW of ONE unrestricted, aligned, identity-background CMP109 coarse e1 link, and its R120 old selected-contour comparator.** It does NOT construct the full regional Ω/Λ multi-row, multiscale, gauge-fixed CMP99/CMP109 averaging operators; nor does it justify treating arbitrary regional old/new kernels as identical. L=13 with common integer fine blocks [0,12]^4, old corner y=0, new center s=(6,6,6,6), and chosen R120 descending endpoint transports. Positive oriented bonds and one orthonormal real SU(2) color are the coefficient convention. Set κ=1/L³=1/2197 and z=(0,1,0,0)→(0,1,1,0) as in R120.

## 1. Exact full one-row revised averaging derivative

At U=1, differentiate the printed CMP109 (0.4). For each x in [0,L−1]^4, source path formula yields:

D_n[B] = L^(−4) Sum_x { average_shortest ∫(s→x) B
                          + ∫(x→x+Le1) B
                          − average_shortest ∫(s+Le1→x+Le1) B }. (R150.F1)

The printed coarse-base holonomy cancels at first derivative between the log-loop and outer factor. Every left/right endpoint contour is confined to its own block. Thus the **only** contribution to fine e1 edges crossing the interface from x1=L−1 to x1=L comes from the bridge. There are N=L³=2197 such positive crossing fine bonds, indexed by transverse triples (t2,t3,t4); for each there are exactly L endpoint sites x with that transverse triple, and exactly one crossing in its length-L bridge. Therefore

 D_n[e_(L−1,t2,t3,t4; e1)] = L/L⁴ = κ,
 for every transverse triple.                            (R150.F2)

The old descended selected-contour formula with R120 endpoint transports gives the **same bridge coefficient** on all N bonds, because old endpoint contours and endpoint transports do not cross the interface. Hence

 (D_n−D_o)|_{interface bridge} = 0 identically.       (R150.F3)

The exact complete-row enumeration in [R150 computation](../computations/YM_R150_FULL_ONE_ROW_BOND_COEFFICIENT_AND_DEFECT_20261031.py), with all 13⁴ sites, all symmetrized shortest-path permutations, old descending left/right paths and tau legs, verifies:
- κ=1/2197 on each of 2197 interface-crossing bonds in both rows;
- D_n(z)=−1/114244=−κ/52, D_o(z)=0, so t=1/52;
- D_n has **213109** nonzero positive-oriented fine bond coefficients; D_o has **32959**; their difference Δ=D_n−D_o has **210912** nonzero coefficients, and NONE on the 2197 crossing bridges.
These support counts and rational sums are for the declared source-shaped one-link model, not the source's admitted regional Ω or its entire Q_j.

## 2. Correction to R150.D9: the sparse dual cancellation does not imply sparse full support

Consider the **ONE-ROW** new constraint ker D_n and old ker D_o on this common unrestricted bond carrier; select the historically distinguished bond a at transverse (0,0,0) and the revised distinguished bond b at (6,6,6), both among the crossing bridges. Suppose old/new chart graph elimination for this ONE ROW is permitted. The source-shaped composite shear uses old pivot a and takes the new b-deleted independent coordinates x=(x_a,x_r) to old a-deleted coordinates y=(y_b,y_r). Since D_n a=D_n b=κ and both pivots have coefficient κ, the one-row map has matrix form

 F = [ −1   −q^T ; 0  I ],     q_r=D_n(r)/κ
 for r running over ALL remaining bonds except a,b,    (R150.F4)
and F²=I on this declared one-row algebraic coordinate space.

R149 variance probes w_a=e_a and w_u=e_a−t e_z have dual historical-coordinate pullbacks

 v_a=F^(−T)w_a=−κ^(−1) P_a D_n* e_c,                  (R150.F5)
 v_u=v_a−t e_z.                                    (R150.F6)

On every crossing bridge except old a, v_a and v_u have coefficient **−1**, including old coordinate b. This gives

 ||v_a||_1,||v_u||_1 >= L³−1=2196,
 ||v_a||_2²,||v_u||_2² >= L³−1=2196.              (R150.F7)

The full exact one-row coefficient enumeration is considerably larger:
 ||v_a||_1=1033788/13≈79522.15,
 ||v_a||_2²=3165876;
 ||v_u||_1=4135151/52≈79522.13,
 ||v_u||_2²=8560528703/2704≈3165876.00.        (R150.F8)

The previously recorded R150.D9 finite *four-coordinate restriction* gave norms 157/52 and 3. Those fractions were correct for the restricted test but cannot be used as the full one-row observable norms. Nor does this one-row F determine the **inverse transpose of the full multi-row regional** constraint chart. Equation R150.D11 is therefore not a source-native cutoff bound. This is an explicit quantified obstruction to the shortcut "two targeted observables are automatically local."

## 3. The important rescue: the 2197 bridge coefficients CANCEL IN THE CONTOUR DEFECT

The unhelpfully large raw coefficients do NOT imply the historical physical Gaussian observable has large variance. CMP99's **full covariance** already includes the strong correlations forced by the old hard constraint.

Define Δ=D_n−D_o on the same one-row ambient space. For any old admissible B_o in ker D_o, with its distinguished special bond a reconstructed by C_o, the one-row composite chart gives the exact identity

 x_a^(new) = B_o(a) − κ^(−1) Δ[B_o].               (R150.F9)

For the second R149 probe, the one special off-bridge z coefficient cancels:

 u^(new)=x_a^(new)−t B_o(z)
        =B_o(a)−κ^(−1)(Δ+κ t e_z*)[B_o].          (R150.F10)

Here Δ(a)=Δ(b)=0 on all crossing bridges, and Δ(z)=−κt. The term Δ+κt e_z* removes precisely the z contribution. **Neither residual is zero**: Δ has 210912 other nonzero bonds in the declared one-link model.

Write Σ_full,o=C_o K_o^(−1) C_o* for the ORIGINAL HISTORICAL constrained Gaussian field covariance, and define under its stated source hypotheses

 d_a²=κ^(−2)〈Δ,Σ_full,o Δ〉,
 d_u²=κ^(−2)〈Δ+κt e_z*,Σ_full,o(Δ+κt e_z*)〉.   (R150.F11)

Since Σ_full,o(a,a) is a source propagator entry, CMP99 Theorem 3.15 bounds its variance by a source constant B_* (conservatively 3B0 for SU2 color conventions). Minkowski's L² inequality now gives

 Var_o(v_a*y)^(1/2) <= sqrt(B_*)+d_a,
 Var_o(v_u*y)^(1/2) <= sqrt(B_*)+d_u.           (R150.F12)

If IN ADDITION a legitimate full old/new **regional F** is constructed and its COMPLETE constrained-Hessian relative-form defect obeys the previous R150.D1 bound rho<1, then the CMP109 single-color variances obey

 s_a² <= (sqrt(B_*)+d_a)²/(1−rho),
 s_u² <= (sqrt(B_*)+d_u)²/(1−rho).             (R150.F13)

At U=1 with color-isotropic source law these can feed the three-component Maxwell tail of R148. For nonidentity U require full color covariance control. **These are strictly conditional templates.** Neither d_a,d_u nor rho, nor the source-valid full Ω/Λ transport, are certified. No numerical small-bound is implied.

The old Theorem 3.15's exponential kernel could in principle be applied to the explicit Δ coefficients to bound d_a,d_u, but the source's unspecified δ0/B0 and regional collar/metric keep a useful numerical bound open. The generic bound with raw ||v_a||_1 is very wasteful because it discards old constraint correlations. R150.F9 is the better mathematical carrier.

## 4. Relative Hessian determination

Nothing in the path-level first derivative enumeration, its exact bridge cancellation, or the source historical Theorem 3.15 proves the *separate* complete constrained-Hessian form bound rho<1. That gate still requires matching:
1. actual two source regional Ω/Λ domains and their constraints Q/Q' plus gauges;
2. full action Hessians, including CMP109 new gauge-fixing and source current-multiplier constraint jet;
3. the source Hilbert metrics, independent-coordinate graph embeddings and normalization.

The commutator mixed second-jet witness from the preceding R150 pass survives on a declared non-Abelian one-step subspace but does not determine a physical Hessian defect at U=1, where J=0. This pass does not recycle a toy positivity result into the missing form estimate.

## 5. Exact next research gate and custody

**Closed:** entire one-link unrestricted source-shaped D_n and transported old D_o coefficient enumeration; bridge count 2197, interface Δ cancellation; 210912 supported contour-defect coefficients; exact one-row v_a,v_u support and norms; nonlocality correction to the previous sparse-dual interpretation; algebraic decomposition into historically controlled full-field pivot B_o(a) plus the actual contour defect.

**OPEN:** admitted CMP99/CMP109 full regional Q_j and gauge chart, source-legal covariance contraction d_a,d_u, complete constrained-Hessian rho<1, scale-uniform normalized interacting cutoff and independent UV-history comparison, continuum OS/mass gap.

**Next bounded YM-R150 continuation (NOT CONSUMED):** certify a source-compatible regional realization of Δ on the historical hard-constraint/gauge space, exploit its plaquette-curl representation plus CMP99 actual random-walk covariance to bound d_a,d_u (or expose an obstruction). In parallel recover the fully matched source Hessian defect rho rather than assuming the pivot shear is an energy isometry. Keep the historical R149 machine checkpoint intact and append-only corrections.
