# YM-R150 — SOURCE CORRECTION: CMP99 Q1 is not the transported CMP98 introductory selected-contour row

**Date:** 2026-11-02. **Preflight main:** 678bcc1194b738094eacc92787dfbee9a808ee9c (merged PR #48). **Classification:** original-CMP99 equation-image cross-reference, original-CMP98 source OCR cross-reference and EXACT declared finite full-row negative control. **Custody:** append-only correction; prior R150 H1–H5 arithmetic remains valid for its DECLARED DIFFERENT row, but any application of its 98.248% reduction to the ORIGINAL CMP99 historical Gaussian constraint is WITHDRAWN. **Native YM-R150 remains IN PROGRESS/UNCONSUMED; R149 is last canonical completed machine checkpoint.** Claim UNPROVED_RESEARCH_PROGRAM.

## 0. Original source dictionary (important and new)

**Original user-supplied typeset CMP99 (1985), 46-page source SHA256 9904f303f01e2d267a0d138d4fc08d60742086d6557fc78bef6f2d25faeaad20, printed pp.392–393, 428**, source mathematical images inspected again 2026-11-02:

* CMP99 printed p392 explicitly says the fluctuation averaging used is the operation defined in **[5], (89)–(92)**, not simply introductory [5] Eq.(15).
* CMP99 printed p393 (3.13)–(3.15) gives the background-dependent linear operator **Q_j(U)** and identifies its one-step factor **Q(U)** by **formula (124) in [5]**. Historical Q1 in the p428 (3.155)–(3.158) constrained Gaussian is THIS source Q1, with actual source normalization, regions Ω/Λ and support.
* CMP99 printed p428 (3.155)–(3.158) imposes exactly **Q1 B=0** on its regional source-supported B. It reconstructs special bond b0 by solving (Q1 B)(c)=0.

**CMP98 [5] original-paper THIRD-PARTY OCR ONLY**, immutable repository blob **1442f25d63ef4189608e73bff05c2a359c16c01d**, path \`Docs/support/reference/balaban-source-extracts/cmp98-averaging-operations.txt\` in \`chboishabba/dashi_agda\`:
* Eq.(15) on printed p19 is an illustrative historical reference-transport selected-contour average.
* The operation ACTUALLY CITED by CMP99 is instead composed from [5] (89)–(92), and the linearization is [5] (124), printed p36.
* In (124), all source background-dependent correction terms disappear when the background \(V_0=1\): the function factors \`g(-i ad γ),g^{-1}(...),exp(i...)−1\` reduce to their identity/zero values. The remaining **main term** is [5] (125), a straight connecting-path average, of the form
      Q0 A(c) = sum_{x in B(c_-)} L^(-(d+1)) A([x,x']),
  subject to the exact source Lie-algebra and normalizations. This is a full length-L **straight bridge PATH** for every x, not simply the L³ interface-crossing edges and NOT the p19 selected-contour row. Since the question here is the kernel of ONE hard constraint row, a nonzero global scalar normalization does not change the orthogonal projector in the matching metric.

**Evidence grade:** CMP99 page images for p392–393/p428: SOURCE ORIGINAL. CMP98 exact (124)–(125): ORIGINAL-PAPER OCR, clear enough to identify its bridge-only zero-background structure but mathematical image of printed p36 is NOT independently authenticated here. The reduction Q(1)=Q0 therefore remains SOURCE-TEXT WITNESS plus algebraic interpretation, not an original CMP98 image attestation. Actual nontrivial U corrections, k>1 compositions, source Ω/gauge and Hilbert metric are NOT reconstructed.

## 1. Correct three-row distinction in declared aligned L13 patch

Let **D_n** be the CMP109 printed (0.4) symmetrized shortest-path derivative for one centered coarse e1 link on the previously declared unrestricted aligned L13 identity patch; let **D_sel** be the introductory CMP98(15)-style old selected descending-contour derivative, BEFORE R120 field-dependent endpoint path relocation; and let **T** be R120 endpoint transport derivative (two paths of total 48 fine-bond traversals). Let

    D_tau = D_sel + T,        j_tau = D_n−D_tau.          (R150.Q1)

All the previous complete-row and curl arithmetic used **D_tau**, not the source CMP99 Q1. In particular the PR #48 rank-one projector used \`P_tau = I−D_tau* (D_tau D_tau*)^-1 D_tau\`. That is an exact DECLARED Euclidean projection but is NOT, by itself, CMP99's historical hard constraint \`Q1 B=0\`.

The source-cited CMP98 (125) zero-background **Q0** gives a THIRD one-row functional \`q_src\` proportional to the sum of straight length-L connecting paths (one for each of L^4 sites). It has no selected endpoint contours. Its support in the declared aligned L13 grid contains (2L−1)L³=**54925 distinct positive e1 fine bonds**, including all 2197 interface bonds plus the interior e1 bridge segments. Thus **"straight bridge-path only" does NOT mean "only interface-crossing edges."**

In the exact conventional integer unit-fine-bond metric the q_src coefficient vector can be represented, up to the cited source's nonzero scale factor, by integer counts of path multiplicity:

    q_src(e)= #{(x,j): x in [0,12]^4, j=0,...,12,
                  e=(x+j e1, x+(j+1)e1)}.            (R150.Q2)

It has 54925 nonzero coefficients, min=1, max=13, and integer squared norm

    <q_src,q_src>=3227393.                           (R150.Q3)

**NEW EXACT NEGATIVE RESULT:** the prior source-shaped transported contour defect \`j_tau\` has nonzero support on 210912 edges and zero on every interface-crossing bridge. It is ALSO orthogonal to this complete straight-bridge source row, INCLUDING all its non-interface edges:

    <q_src,j_tau>=0.                                 (R150.Q4)

The equality is an exact integer dot product over all 13^4 fine sites and all shortest-path permutations, independently checked with [script](../computations/YM_R150_SOURCE_Q1_ROW_MISMATCH_RATIONAL_20261102.py). Hence

    P_{ker q_src} j_tau = j_tau,
    ||P_{ker q_src} (j_tau/κ)||²
       = ||j_tau/κ||²=523953742/3.                  (R150.Q5)

So **0% of squared norm is removed** by the SOURCE-SHAPED identity-background one-row historical q_src on this declared aligned graph. CMP99's actual multirow/full regional Q1 may have other constraints and may remove a component; no claim about the genuine full Q1 projection follows without constructing its complete source region and metrics.

## 2. Exact checkpoint correction to the previous 98.248%

The prior PR #48 compared j_tau to the DIFFERENT row D_tau and derived beta=−240131/246099 and 98.248% squared norm removal. That Euclidean identity remains true. It **does not** license the original-HISTORICAL-GAUSSIAN assertion \`Sigma_o D_tau*=0\`. The source only gives \`Sigma_o Q1*=0\` for its OWN Q1 on its legally admitted regional carrier. Extra field-dependent R120 endpoint paths T cannot silently be inserted into that nullspace.

For comparison, if the same transported defect j_tau is projected onto the *untransported introductory selected-contour* D_sel, the exact removal fraction is only

    236083225/52408729416 ≈ 0.45046546%.          (R150.Q6)

This intermediate percentage is ALSO **not** the CMP99 source Q1 projector, because CMP99 specifically cites [5] (124), NOT [5] introductory (15).

Conversely, projecting a DIFFERENT, untransported old-new comparison \`D_n−D_sel\` onto D_sel removes ≈92.70097% of its squared norm, but \`D_n−D_sel\` has mismatched coarse gauge endpoints and is NOT the same gauge-covariant physical comparison as j_tau. These calculations demonstrate that projection percentages are *representation sensitive*. Do not mix their domains or advertise any of these numbers as a native source covariance suppression theorem.

The operator identity itself is exact on the declared patch:

    Q1_source B=0 does NOT imply D_tau B=0.
    D_tau B = D_sel B + T B,                    (R150.Q7)

and in general neither D_sel nor T is in the row span of actual source Q1 unless a source-valid gauge/background frame transport theorem is supplied. PR #48's numerical 57x covariance improvement is therefore **NON_TRANSFER / withdrawn as CMP99 Gaussian claim**. Keep all prior historical calculations unchanged and append this correction in custody.

## 3. What the true source covariance still allows

The original CMP99 (3.157)–(3.158) and Theorem 3.15 certify historical \`Sigma_o Q1*=0\` and source exponential covariance decay. Therefore, for an actual observable v in its SOURCE space, it is legitimate to replace it by its equivalence class modulo \`ran Q1*\` and then compute \`<v,Sigma_o v>\`. However:

* On the declared one-row first-order aligned patch the source-shaped zero-background q_src is already orthogonal to j_tau; there is **no** rank-one improvement available from that row alone.
* The remaining actual Q1 rows may introduce projections, but their Gram matrix, legal Ω/collar, background U, source gauge R=Proj_{\Delta_U N(Q')}, and source Hilbert products have not been constructed.
* One must match the transported old coarse endpoint frames and constraint TARGETS (the field-dependent T) **before** treating the old covariance as a law for the transformed observable. CMP99 source historical propagation does not automatically bound the new CMP109 operator.
* Full covariance contraction \`<j_tau,Sigma_o j_tau>\` and full constrained-Hessian relative form \`rho<1\` remain separate OPEN gates. The exact raw norm ≈174.65M is not proof that the actual historical covariance contraction is large; nor does a large projection suppression follow from CMP99 original hard Q1 alone.

## 4. Next NF and STOP

**CLOSED THIS SOURCE-BOUNDARY AUDIT:** exact original CMP99 p392–393 source citation to CMP98 (89)–(92),(124); exact distinction [5] selected (15) vs source linearized (124)–(125); source-shaped complete straight-path q_src support 54925; exact zero pairing with transported contour defect; append-only correction of PR #48's invalid *SOURCE TRANSFER*, while preserving its finite arithmetic.

**OPEN:** original CMP98 p36 equation image; actual full CMP99 regional Q1 including all rows and Ω/Λ, source background and weighted inner-product metric; gauge-frame T legal transport; actual covariance contraction and multiscale random walks; 1985→1987 constrained-Hessian relative rho<1; cutoff weights/normalized two-UV laws; continuum OS and spectral mass gap.

**Next:** Obtain the original CMP98 printed p36 image or unambiguous primary typeset (124)–(125); instantiate **all source-compatible Q1 rows** on one eligible small Ω/collar with correct norm and source block incidence. Audit the nullspace of the whole Q1 on the transported v, not one arbitrary selected path. If source regional data is not legal/available, mark SOURCE_CARRIER_HOLD. Do NOT infer a small 1987 variance or gap from a model projection.

YM-R150 remains in progress / unconsumed. Canonical R149 checkpoint intact.
