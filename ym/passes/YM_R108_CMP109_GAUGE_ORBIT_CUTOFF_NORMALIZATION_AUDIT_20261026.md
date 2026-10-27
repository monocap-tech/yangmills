# YM-R108 — CMP109 gauge-orbit identity versus restricted probability-law normalization

**Date:** 2026-10-26. **Previous certified:** [R107](../checkpoints/YM_HEAD_R107_20261026.json), main 0d1105761245569a842d2cd1fc7bd4186f81c668. **Status:** COMPLETE AS SOURCE-PROSE / EXACT CONDITIONAL NORMALIZATION AUDIT; source-native kernel law, image equations and cross-cutoff transport OPEN. **Next:** YM-R109 (unconsumed). **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source and evidence boundary

The pinned original-paper *third-party OCR* for Bałaban CMP109, SHA f1aec083a3a6470c67a2c1205ca740c2583fe37a, was re-read at lines 277–339, printed pp.254–255. (0.13) defines a general gauge-invariant kernel; (0.14) an exponential gauge-fixing factor; source prose calls (0.15) an **identity** with normalizer z. Lines 310–314 insert it under the integral, invoke Faddeev–Popov rearrangement and a based gauge group fixing coarse vertices, and explicitly state that the gauge-transformation integral equals one. (0.16) additionally imposes a small-field characteristic restriction. (0.17) defines N0 by evaluation of the corresponding action integral at V=1.

Original-page images of these formulas remain **NOT INSPECTED**: Springer/Project Euclid PDF routes were unavailable to the web tool, and container network retrieval failed. No exact source prefactors, matrix ordering, FP Jacobians or image-level theorem custody are asserted. CMP109 (0.4) versus alternative (0.12), CMP102b fixed-average equations, and CMP109 (0.29)/(5.37)/(5.42) remain source holds. See [source receipt](../source_receipts/YM_R108_CMP109_FP_ORBIT_SOURCE_RECEIPT_20261026.md).

## 1. Gauge-fixing identity is not automatically a physical input tilt

**R108.1, exact orbit identity.** Let compact H act measurably on standard Borel X, let probability mu be H-invariant, normalized Haar dh, and w≥0 measurable with \(\int_H w(hx)\,dh=1\) for mu-a.e. x. For every bounded H-invariant F,
\[
 \boxed{\int F(x)w(x)\,d\mu(x)=\int F(x)\,d\mu(x).}
 \tag{R108.1}
\]
*Proof:* average the left-hand integral over H by invariance of F and mu and use Tonelli and the orbit normalization. The orbit condition also ensures integrability of w.

Therefore a gauge-fixing weight normalized as an **exact orbit identity** leaves a gauge-invariant integral unchanged, despite w varying strongly pointwise. A source kernel t(V,x) invariant under H at fixed coarse V is eligible for this argument for each V. The native source (0.15) normalization must be reconstructed from original equations and checked in every actual gauge/collar domain; the conditional theorem is **not** a certification of CMP109's exact w.

## 2. Distinct small-field selector survives orbit averaging

For measurable 0≤chi≤1 (possibly non-invariant under H), define
\[
 \sigma(x)=\int_Hw(hx)\chi(hx)\,dh.
\]
It is H-invariant, \(0\le\sigma\le1\), and for bounded invariant F,
\[
 \boxed{\int Fw\chi\,d\mu=\int F\sigma\,d\mu.}\tag{R108.2}
\]
*Proof:* average the left integral over H. If chi=1, sigma=1. If chi is itself H-invariant, sigma=chi. Otherwise it is invalid to replace the physical gauge-invariant restriction by raw gauge-slice chi without its orbit mean.

This is the precise abstract consumer of source prose about insertion of identity (0.15) and additional cutoff (0.16). Actual CMP109 chi and w remain image-open.

## 3. Separate gauge fixing, cutoff and kernel fiber mass

For nonnegative H-invariant kernel t(V,x), let \(\kappa_t(x)=\int t(V,x)dV\), and \(K_t(dV|x)=t(V,x)dV/\kappa_t(x)\) where positive. If \(0<\int\kappa_t\sigma\,d\mu<\infty\), the **normalized** output represented by t(V,x)w(x)chi(x) is
\[
 \boxed{\nu=\int K_t(\cdot|x)\,
 \frac{\kappa_t(x)\sigma(x)\mu(dx)}
 {\int\kappa_t\sigma\,d\mu}.}\tag{R108.3}
\]
This follows from R108.2 applied pointwise to t and then the R107 positive-kernel identity. The physical reweighting channels are source **kernel mass** kappa_t and **genuine cutoff/orbit selection** sigma, not w alone. Without chi, sigma=1 and proper FP insertion contributes no additional tilt.

If t is Markov (kappa_t=1), with c=E_mu sigma>0, then \(\nu=K_{t*}(\sigma\mu/c)\), and
\[
 \|\nu-K_{t*}\mu\|_{\rm TV}\le 1-c.\tag{R108.4}
\]
*Proof:* \(\mu=c(\sigma\mu/c)+(1-c)((1-\sigma)\mu/(1-c))\) for c<1, and Markov pushforward contracts total variation. c=1 is immediate. There is **no native uniform bound on c_N**, hence no summability statement.

The ideal delta kernel \(t(V,x)=\delta(VM(x)^{-1})\), for a lawful globally defined M and normalized compact-group Haar delta, has kappa_t=1 and yields the conditional distribution \(M_*(\sigma\mu/c)\). This is a *separate ideal CMP98-style example*, NOT verified CMP109 (0.17) with its actual gauge and sharp-field restrictions.

## 4. Reference-background scalar cancellation

Let unnormalized density q(V)≥0 integrate to 0<Z<∞. For a positive constant N_ref independent of V,
\[
 \frac{q(V)/N_{\rm ref}}{\int q(W)/N_{\rm ref}\,dW}
 =\frac{q(V)}{Z}.\tag{R108.5}
\]
Thus a source-action scalar evaluated at the fixed V=1 background is **not by itself** an obstruction to correctly normalized observable laws. R107's warning that N_ref is not automatically the *partition function* remains valid, but it would be false to infer a nonzero normalized-law defect solely from a different N_ref. Absolute partition/free-energy comparisons and background-dependent counterterms remain separate.

## 5. Refute-first verdict

| Gate | R108 result |
|---|---|
| CMP109 (0.15) identity / FP step | SOURCE ORIGINAL-PAPER OCR PROSE, image OPEN |
| Nonconstant gauge-fixing w always causes physical-law tilt | REFUTED if orbit-normalized, R108.1 |
| Additional (0.16) cutoff | CONDITIONAL orbit-averaged selection sigma, R108.2 |
| Effective source-shaped law | CONDITIONAL exact kappa_t*sigma decomposition, R108.3 |
| Markov cutoff TV defect | CONDITIONAL bound 1-c, R108.4; native c OPEN |
| Background-independent N_ref forces a law defect | REFUTED for normalized laws, R108.5 |
| Actual native CMP109 w, chi, t, M, kappa_t, sigma, c | OPEN |
| Actual paired Omega,V and cross-cutoff observable laws | OPEN |
| CMP102b/CMP109 original image formulas, beta/Eq.(0.29) | OPEN |
| Four-dimensional continuum YM, OS reconstruction, physical gap | UNPROVED |

**Stop / YM-R109 next:** recover actual publisher equations (0.15)–(0.17) or record exact access obstruction, reconstruct based gauge-group action and w orbit normalizer, classify the source chi and choose operative (0.4)/(0.12) M and t on one eligible aligned block, then compute kappa_t, sigma, c and source M-derived prescribed-data laws for two actual histories. No external Yang–Mills theorem is adopted. Highest numbered bibliography [92] unchanged.
