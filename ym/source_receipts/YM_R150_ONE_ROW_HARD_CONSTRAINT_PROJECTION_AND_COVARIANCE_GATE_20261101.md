# YM-R150 — Exact old hard-constraint projection of the full one-row contour defect

**Date:** 2026-11-01. **Previous merged main:** 65486015ff729b7814d1c4fb5ccbe771bf36f672 (YM-R150 153792-plaquette exact curl and covariance budget). **Type:** ORIGINAL SOURCE HYPOTHESIS + EXACT DECLARED ONE-ROW EUCLIDEAN RATIONAL PROJECTION + CONDITIONAL SOURCE COVARIANCE CONSUMER + TYPED LIMITATION. **Claim:** UNPROVED_RESEARCH_PROGRAM. Native YM-R150 IN PROGRESS/UNCONSUMED. Canonical completed machine checkpoint remains YM-R149; no mass-gap result.

## 0. Source equation and model boundary

**Original primary printed CMP99(1985) p.428 (3.155)–(3.158), user-provided typeset article:** The historical Gaussian bond fields B are required to satisfy **Q1 B=0**, source regional support conditions and its particular gauge restrictions. C_o maps independent non-special bond coordinates to this hard-constrained source B space. In source notation \`C_old^(k)=C_o(C_o* Delta_k C_o)^(-1)C_o*\`, and so \`Q1 C_old^(k)=C_old^(k) Q1*=0\`. **Primary printed p.432, Theorem 3.15:** under its regularity/smallness conditions, the same **historical** covariance has an exponential kernel bound B0 exp(-delta0 distance); previous R150 source audit derived a corresponding symbolic source-metric operator bound M_hist. The source paper does NOT state our numerical projection result or a comparison to the distinct CMP109 1987 Hessian.

**Declared finite test:** exactly the previously source-shaped unrestricted identity L=13 one-coarse-link aligned first-derivative rows \`D_o,D_n\` from the R150 full-row and plaquette certificate. Historical \`D_o\` is CMP98(15)-style descending selected contours plus R120 endpoint transport; revised \`D_n\` uses CMP109 printed (0.4). The old original CMP99 regional Q1 and new CMP109 multiple-row Qtilde, their actual Ω/Λ, gauge/collar, source metrics and multiscale composition are NOT constructed. All following numerical facts are *model* Euclidean unit-fine-bond inner products, not native unconditional source results.

## 1. Exact one-row hard-constraint projection

Write unnormalized integer coefficient vectors \`d_o=den D_o*\`, \`j=den (D_n−D_o)*\`, \`den=24*13^4=685464\` and \`κ=1/13^3=1/2197\`. All positive-oriented fine bond coefficients were enumerated, including ALL old/new shortest or selected paths; \`j\` has 210912 supported bonds. Direct exact integer dot products:

    <d_o,d_o> = 17543968513344
    <j,d_o>   = -17118520201536
    <j,j>     = 17001251020416.                       (R150.H1)

The rank-one Euclidean orthogonal projector onto the OLD one-row hard-constraint kernel is \`P_o=I−d_o d_o*/||d_o||²\` (in the ambient fine bond coefficient Hilbert space). Its action on the normalized contour-defect coefficient \`j_κ=(D_n−D_o)*/κ\` is

    P_o j_κ = ((D_n−D_o)* − β D_o*)/κ,
    β=<j,d_o>/||d_o||² = -240131/246099.          (R150.H2)

By exact fraction reduction, the fraction of squared norm removed is

    ( <j,d_o>² /(||j||²||d_o||²) )
      = 57662897161/58691166114
      ≈ 0.982480004725026.                          (R150.H3)

The retained squared norm is

    ||P_o j_κ||² = 2259106889741/738297
                ≈ 3059889.02804833,                 (R150.H4)

versus unprojected \`||j_κ||²=523953742/3≈174651247.333333\`. This is a factor **≈57.07764 reduction in squared norm**, but the residual remains millions, not small. The normalized **revised source-shaped row itself** has \`||D_n*/κ||²=3165877\`, and on \`ker D_o\` the exact identity \`(D_n−D_o)[B]=D_n[B]\` holds. Thus the projection removes the component of the contour defect that is functionally invisible to the historical one-row hard-constrained field; the large original ambient norm was partly an artifact of retaining that null-equivalent component.

For R149's second corrected observable \`j_u=j_κ+t e_z\`, where \`t=1/52\`, \`j_κ(z)=-t\` and \`D_o(z)=0\`, the same rank-one projection gives

    ||P_o j_u||² = ||P_o j_κ||² − t²
       = 6108625029121367/1996355088
       ≈ 3059889.02767851.                           (R150.H5)

The difference of about 0.00037 in **squared** norm is trivial compared with the total. No probabilistic or actual source covariance estimate follows from these bare norms alone. The [script](../computations/YM_R150_ONE_ROW_HARD_CONSTRAINT_PROJECTION_RATIONAL_20261101.py) reuses the previous full-row exact enumeration and checks H1–H5, including orthogonality.

## 2. Conditional covariance implication on a REAL source carrier

Let \`Q1\` be the *actual* historical source hard constraint and \`Sigma_o\` its full constrained covariance, so \`Sigma_o Q1*=0\` by source (3.157)–(3.158). For ANY coefficient observable \`v\` and any chosen \`a\` in the constraint-target space,

    <v,Sigma_o v>
       = <v−Q1* a,Sigma_o(v−Q1* a)>.             (R150.H6)

In a FIXED orthonormal source bond metric, the optimal ambient Euclidean representative is \`P_{ker Q1} v\`, giving

    <v,Sigma_o v>
       <= ||Sigma_o|| · ||P_{ker Q1}v||².          (R150.H7)

If a genuine source Q1 row on the legal domain matches the above declared \`D_o\` row **in the same metric**, then \`ker Q1 ⊆ ker D_o\` and

    ||P_{ker Q1} v||² <= ||P_o v||².             (R150.H8)

Under all these still-unverified identifications, Theorem 3.15's prior **historical** symbolic \`||Sigma_o||<=M_hist\` yields for the first contour observable

    d_a² <= (2259106889741/738297) M_hist,      (R150.H9)

and for R149's second corrected probe

    d_u² <= (6108625029121367/1996355088) M_hist. (R150.H10)

This is a **conditional** factor ≈57 improvement on R150.P7's crude \`(523953742/3)M_hist\` bound, but it is *not* an estimate for a genuine full CMP99/CMP109 region. The source normalized Hilbert metric, actual old \`Q1\` row incidence, full gauge and support conditions, and actual covariance contraction are NOT yet identified. M_hist's B0,δ0 are unspecified. Neither bound proves small Gaussian exit, weighted partition control, or the complete 1985→1987 Hessian relative-form rho<1.

## 3. Important negative interface: projection destroys the off-shell curl representation

The previous R150 exact one-row difference has \`∂j=0\` and admits a 153792-plaquette filling: \`j\` annihilates **all** fine pure gauge gradients. The old averaging row \`D_o\`, however, has nonzero discrete boundary at the two centered coarse-link endpoints \`s=(6,6,6,6)\`, \`s'=(19,6,6,6)\`:

    ∂(D_o*) = δ_{s'}−δ_s.                           (R150.H11)

Since β≠0, the projected representative \`j_κ−β D_o*/κ\` does NOT have zero divergence in the unrestricted ambient edge space:

    ∂(P_o j_κ) = −(β/κ)(δ_{s'}−δ_s) ≠ 0.           (R150.H12)

Thus it is invalid to apply the earlier curvature-only plaquette filling to the projected representative **without restoring the subtracted D_o term**. The two representatives agree on the one-row constrained fields B with D_o B=0, but their OFF-CONSTRAINT gauge/curl types differ. This is a precise two-carrier distinction, not a contradiction: quotient by hard constraints and quotient by gradients are different operations. Avoid claiming the projected residual is itself a curvature-only observable.

## 4. Native stopping point / next qualifying step

**CLOSED IN DECLARED MODEL:** exact old hard-row Euclidean coefficient projection, 98.248% squared norm removal, explicit same-projection treatment of the second R149 observable, explicit proof that projection breaks off-shell discrete cycle condition, and exact conditional source covariance lemma.

**NOT CLOSED:** original CMP99 Q1 all rows on a common genuine Ω/Λ/collar with matching historical selected paths and gauge/metric, actual source conditional covariance contraction of \`P_{ker Q1}j\`, complete CMP109 regional chart, **relative constrained-Hessian** rho<1, interaction weights/partition ratios, paired UV laws and spectral gap.

**Next YM-R150 subgate (still unconsumed):** reconstruct source Q1 and its bond inner-product metric on one legally admissible region with all distinguished bonds and gauge/site constraints; test whether the particular declared \`D_o\` row is actually represented, and calculate the full Q1 projection if so. Use CMP99's real covariance/random-walk operator, not a scalar synthetic Gaussian, to evaluate the **projected** quadratic \`〈v,Sigma_o v〉\`; keep the original exact curl identity and the constraint-quotient representative distinct. In parallel source-type 1985/1987 complete constrained-Hessian relative defect rho. If a source chart cannot be built, mark native SOURCE_DATA_HOLD. Do not promote historical positivity to the 1987 measure.

No new YM-R150 completion checkpoint; historical YM-R149 machine checkpoint remains canonical. No 4D YM existence or mass gap claim.
