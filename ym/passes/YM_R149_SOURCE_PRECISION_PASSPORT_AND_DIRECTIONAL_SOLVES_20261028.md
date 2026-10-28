# YM-R149 — Source-exact monitored precision passport, directional inverse, and bounded source stop

**Date:** 2026-10-28. **Predecessor:** YM-R148 (main `5e1377a2`). **Status:** COMPLETED AS A BOUNDED SOURCE-DATA AUDIT AND EXACT CONDITIONAL DERIVATIONS; NATIVE K/COERCIVITY NOT CERTIFIED. **Next:** YM-R150 unconsumed, strictly source-first. **Claim:** UNPROVED_RESEARCH_PROGRAM. No 4D continuum Yang–Mills construction, OS reconstruction, or positive mass gap.

## 0. Objective and direct evidence

R148's pending task is not another Gaussian inequality. It is to obtain an **actual CMP109 identity-background reduced precision** on one admissible L=13 source region (or a source-valid coercivity bound) and the corresponding physical cutoff. This pass reopens the source operator and tests whether the files presently in custody suffice.

**Original CMP109 printed equation images re-inspected:** T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, *Commun. Math. Phys.* 109 (1987), pp. 249–301, PDF https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf : printed p.266 Eq.(2.9), p.267 Eqs.(2.10)–(2.11), p.268 Eqs.(2.12)–(2.14). The paper excludes distinguished b0(c) bonds from monitored cutoff, defines special-bond-supported h and a quadratic A^(k) by direct referral to earlier CMP99(3) Eq.(3.156) with **exponential replacing delta gauge fixing**, and identifies covariance as **(C* A^(k) C)^(-1)** after deleting distinguished coordinates. The PDF original printed p.266–268 was visually inspected this pass. CMP109 does **not** print an evaluated finite L13 matrix K or numerical coercivity constant in those equations.

**Lower-grade CMP99 source:** *Propagators for Lattice Gauge Theories in a Background Field*, *CMP* 99(3) (1985), pp.389–434, DOI 10.1007/BF01240355, original-paper third-party OCR `chboishabba/dashi_agda:Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt`, pinned blob `ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743`, region around printed pp.427–428 Eq.(3.155)–(3.158). OCR renders (3.156) as a compound background-dependent form with propagator/gauge pieces, and the prose after (3.158) states positivity of **C*Delta_k C**, not automatically CMP109's exp-gauge **C*A^(k) C**. The printed CMP99 equation image was **not** independently recovered. The OCR crosswalk is source text, not a native numerical matrix.

## 1. Minimal source-operator passport and failed native entry

On an *actual* admitted finite region `R` with SU2 background U=1 and an actual stage k, the input required by R148 is:

- an explicitly enumerated independent monitored-bond carrier, graph map C_R=(I-h_R D_R)E_R with the source special b0(c) locations, and the source Hilbert metric;
- the full source operator A_R^(k)(1), **including** its background-minimizer response H1, quadratic action Delta_1, path-holonomy gauge term, regional Dirichlet/collar and covariance normalizations, so that K_R is the exact color-scalar part of C_R* A_R^(k)(1) C_R;
- one physical choice of cutoff branch `theta_k=epsilon1` or `theta_k=g_k epsilon1/gamma_k`, giving T=theta_k/|g_k|, with the actual admissibility conditions and stage-dependent parameters;
- an admissible region embedding for the declared L=13 sparse bonds and, for any later CMP99 comparison, an *actual* old/new regional chart with matching gauge and source history.

**Current disposition:** the existing R120/R147 five-bond L=13 example fixes the averaging derivative and curvature shift `t=1/52`, **not** the ambient Hessian. R148's K from `A_test=I` is synthetic. The checked CMP109 page images identify the operator and its provenance but do not supply its entries, a finite regional boundary matrix, an independently certified positive alpha, a selected k/coupling/threshold, or a lawfully matching CMP99 Ω/Λ chart. CMP99 OCR cannot be promoted to an original-image-checked operator identity. Therefore **no native numerical s_a, s_u, alpha, or Gaussian cutoff probability is certified**. A standalone five-bond subspace is not silently substituted for a legal full CMP109 region.

This is a **SOURCE-DATA HOLD**, not a negative claim about whether the true finite Hessian exists or is positive.

## 2. Exact two-solve certificate: no full K inverse required (DERIVATION)

Let K=K_R be real symmetric strictly positive on the **actual** independent source coordinates, if recovered. With a monitored a and shifted companion z, put v_a=e_a and v_u=e_a-t e_z, where t is the physically certified chart shift (the 1/52 value is only for R147's declared sparse test). For SU2 identity color isotropy,

`s_a²=v_a* K^(-1) v_a`, `s_u²=v_u* K^(-1) v_u`.

Only two linear solves `K h_a=v_a` and `K h_u=v_u` are needed to extract both source marginal Maxwell scales. This is a *source-computation reduction*, not a proof of K or an independent two-UV comparison.

For any approximate rational/numerical solve h of `K h=v`, define `r=v-Kh` and `L(v,h)=2<v,h>-<h,Kh>`. Completing the square gives the **exact identity**

`v*K^(-1)v = L(v,h) + r*K^(-1)r.`                         (R149.1)

If a **certified** coercivity `K>=alpha I`, alpha>0, is available on exactly this metric and region, then

`L(v,h) <= v*K^(-1)v <= L(v,h) + ||r||²/alpha.`          (R149.2)

Thus a source numerical candidate has a reproducible residual-to-variance enclosure without a huge explicit matrix inverse. With no certified alpha, the upper endpoint is **OPEN**; merely reporting small solver residuals is not a proof. Exact rational LDL on a genuinely finite explicit K could alternatively certify positivity without a preexisting analytic uniform alpha, but neither K nor the legal region has been recovered.

## 3. Sharpen R148's coercivity-only rare-exit gate (DERIVATION)

For K>=alpha I on the actual identity color-scalar carrier, the R148 directional combination obeys the *direct Rayleigh estimate*

`s_u²=(e_a-t e_z)*K^(-1)(e_a-t e_z) <= (1+t²)/alpha,`

because a and z are **distinct independent coordinates** with orthonormal basis in the stated metric. This is sharper than R148's Cauchy bound `s_u<=(1+|t|)/sqrt(alpha)`. With `Q3` the exact 3D Gaussian/Maxwell survival used in R148, the corrected sharper **sufficient** bound is

`delta_gamma <= min{1,Q3(T sqrt(alpha)) + Q3(T sqrt(alpha)/sqrt(1+t²))}.` (R149.3)

The original R148.6 remains a valid weaker bound, not an erroneous one. For the *declared synthetic* t=1/52 and dimensionless T sqrt(alpha)=4, R148.6 yields approximately 0.00263747, whereas R149.3 yields approximately 0.00227114. These are **conditional universal upper bounds**, not estimates for CMP109's uncomputed alpha. The source alternative threshold `theta_k=g_k epsilon1/gamma_k` makes `T=epsilon1/gamma_k` for positive g_k; small coupling alone cannot force tails small.

## 4. Synthetic exact-rational independent check, not native data

The attached standard-library computation reuses R148's **synthetic** five-bond model `A_test=I` and checks exact rational K, K^-1, two source-shaped variance functionals, the residual enclosure (R149.1)–(R149.2) with a valid rational alpha from inverse row sums, and the improvement in R149.3. Its exact synthetic variances are `s_a²=8113/10817`, `s_u²=8115/10817`. **Nothing in this arithmetic represents numerical CMP109 A^(k)**. [Certificate](../computations/YM_R149_TWO_SOLVE_RESIDUAL_AND_RAYLEIGH_20261028.py).

## 5. Closed, open, and stopping jurisdiction

**Closed in R149:** printed CMP109 operator provenance rechecked; original-paper CMP99 OCR constraint confirmed at lower evidence level; minimum data passport enumerated; exact two-solve/residual certificate proved; R148 coercivity bound sharpened without requiring upper conditional precision; independent synthetic arithmetic passed.

**OPEN, NOT PROMOTED:** original CMP99 (3.156)–(3.158) equation images and hard/soft gauge map; an admissible single CMP109 Ω/Λ region and actual ambient A^(k)(1); K spectral or directional bounds with certified metric/threshold; normalization `W,Z`; true old/new independent-UV source laws; global winding coverage; volume/cutoff summability; continuum, OS, spectral gap.

**Typed stop:** The source-data entry gate for **native numerical K** is **NOT MET**. Do **not** recursively generate another generic Gaussian bound or assign synthetic entries to the source. The next valid move is a *source artifact*, not a theorem-like inference from the current matrix proxy.

**YM-R150 (unconsumed, source-first):** seek/read an actual publisher-image-quality CMP99 (3.156)–(3.158) and/or a complete native CMP109 finite identity operator and admissible Ω/Λ specification; recover H1/Delta1, source gauge, Dirichlet boundaries and normalizations. If these cannot be obtained, preserve the SOURCE-DATA HOLD and pause this branch instead of consuming R150 on mathematics independent of the carrier. No mass gap established.
