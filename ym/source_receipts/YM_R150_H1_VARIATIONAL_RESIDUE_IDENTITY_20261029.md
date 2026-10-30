# YM-R150 continuation — variational residue identity from CMP99 (3.128), not a positivity transfer

**Date:** 2026-10-29. **Canonical predecessor:** merged source-crosswalk audit on main fc8f77bed6bfbb970c03d5478bfa68d057c64e0f. **Disposition:** bounded exact source-facing algebra, YM-R150 still IN PROGRESS/UNCONSUMED. No numerical K, new alpha, two-UV law or Yang–Mills gap claim.

## Original source jurisdiction

Source: user's original 46-page typeset CMP99 paper, printed p421, equation (3.128) and p428 (3.156)–(3.158), plus CMP109 printed pp266–268 (2.5), (2.11)–(2.12), previously verified in source receipts. Historical H1 is the minimizer of (3.127), (3.110), with representation (3.129). This note does **not** equate the CMP99 and CMP109 backgrounds, regional domains, Hilbert structures, H1 operators or coarse-coordinate embeddings.

Define the historical core quadratic q_core(A) by the first two terms of the original CMP99 (3.128):
q_core(A)=<A−DG'RD*A, A_action(A−DG'RD*A)>−2<H C^(2)(A−DG'RD*A),J>.
Here A_action is the source quadratic action operator, H is the source linear minimizer, and C^(2) is the historical nonlinear averaging second-order piece. By source (3.128),

  <A,G1^(-1)A> = q_core(A)+||RD*A||²+a||QA||².   (R150.V1)

For a source-admitted historical H1B with QH1B=B and RD*H1B=0,

  <H1B,G1^(-1)H1B> = q_core(H1B)+a||B||².       (R150.V2)

The source minimizer formula H1=G1Q*(QG1Q*)^(-1), under the same positive finite source metric, gives by direct multiplication

  <H1B,G1^(-1)H1B>=<B,(QG1Q*)^(-1)B>.         (R150.V3)

Therefore the **exact source historical identity**, with the specified metric, is

  <B,(QG1Q*)^(-1)B>−a||B||²=q_core(H1B).     (R150.V4)

This is stronger than merely proposing E_var=0: it identifies the *entire historical variational combination* as q_core evaluated on the actual H1 minimizer. In a CMP99/CMP109 common-carrier comparison where CMP109 uses precisely the same H1, set

  E_var(B)=<H1B,Delta1 H1B>−<B,(QG1Q*)^(-1)B>+a||B||².

Then (R150.V4) yields the exact **residual form**

  E_var(B)=<H1B,Delta1 H1B>−q_core(H1B).    (R150.V5)

It is ZERO only if the source **CMP109** Delta1 quadratic restricted to its H1B image equals the historical q_core, including the old nonlinear averaging correction and field J, at matched scale/domain. Merely matching the Wilson Hessian is not sufficient if q_core includes the -2<HC^(2),J> contribution. Thus *do not* infer cancellation solely from RD*H1=0 and QH1=B.

## Separate nonlinear-jet residue and conditional transfer criterion

Retain the crosswalk's conditional same-carrier decomposition:

  q_new(B)-q_old(B)=G^(2)(B)+E_var(B)+E_jet(B),
  E_jet(B)=-2<H1(h Ctilde^(2)(B)-Dtilde^(2)(B)),J>.

After inserting (R150.V5), the two residuals remain typed separately. If source-matched coordinates yield E_var(B) >= -eps_var||B||², E_jet(B)>=-eps_jet||B||² and a bounded common-coordinate embedding/metric (with old K_old>=gamma0 I), then on the *same independent coordinate space* and after exact C transport,

  K_new >= (gamma0-eps_var-eps_jet) I,       (R150.V6)

provided the positive G^(2) contribution is retained and gamma0>eps_var+eps_jet. This conclusion is **conditional** and depends on isometric shared coordinates; for a non-isometric transport, gamma0 must be adjusted by the minimum singular value of that transport rather than copied literally.

No eps_var, eps_jet, matching C/H1/Delta1 or native gamma0 have been certified here. Source CMP99 original positive lower bound is qualitative and remains tied to its own C_old and assumptions. No physical CMP109 K positivity or Gaussian cutoff probability is promoted.

## Stopping point

**Source-resolved:** historical variational combination equals q_core(H1B), original (3.128)–(3.129), and the new variational mismatch can be tested specifically as CMP109 Delta1 versus q_core on the H1 image. **Unresolved:** whether CMP109's Delta1 includes/omits the historical nonlinear jet, and whether E_jet double-counts or cancels any part of that difference when the nonlinear coordinate charts are truly matched. Before using (R150.V5) as a source comparison, recover exact definitions for Delta1 and the two C^(2) operators on a common source Ω and check the order of linearization.

**Next bounded move within YM-R150:** type the CMP109 Delta1 definition and the CMP99 q_core pieces on the exact same regional quadratic functional; do not begin synthetic finite-matrix computation. YM-R150 remains UNCONSUMED, repo status/checkpoint unchanged.
