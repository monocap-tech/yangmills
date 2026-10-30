# YM-R150 — Original-source variational excess and gauge-residual identity

**Date:** 2026-10-29. **Classification:** SOURCE-ATTESTED LITERATURE DEFINITIONS + EXACT CONDITIONAL DERIVATION + NEGATIVE TRANSFER GATE. **Existing canonical cursor:** YM-R150 IN PROGRESS / UNCONSUMED. This is an append-only R150 micro-audit, **not a finished new pass or mass-gap claim**. Prior source crosswalk: [YM-R150 crosswalk](YM_R150_CMP99_CMP109_NATIVE_PRECISION_SOURCE_CROSSWALK_20261029.md).

## 1. Exact printed source receipts

User-supplied original typeset T. Balaban *Propagators for Lattice Gauge Theories in a Background Field*, CMP 99 (1985) PDF, printed **p.421**, Eqs **(3.127)–(3.129)**, was directly inspected. Eq(3.127) introduces the physical/hard-gauge variational quadratic
\`f(X)=<X,Delta X>-2<H C^(2)(X),J>\` in full quadratic normalization. Eq(3.128) builds the strictly positive completed quadratic G1^(-1) from a gauge-invariant extension of f and adds **||R D*X||² + a||QX||²**. The second line of (3.128) gives the gauge-fixed representative explicitly. Eq(3.129) states
\`H1 B=G1 Q*(QG1Q*)^(-1) B\`.

Printed **p.428** Eq(3.156) identifies the historical reduced coarse quadratic
\`q_old(B)=<B,(QG1Q*)^(-1)B>-a||B||²-2<H1 Dtilde^(2)(B),J>\`,
on its stated constrained regional coarse-bond domain; (3.157)–(3.158) parameterize via C and assert source lower positivity for the historical C*Delta_k C **under stated source hypotheses**. Printed p.428 original equation symbols are readable; no OCR-based substitute is used.

CMP109 (1987), original printed **p.266** Eq(2.7), expressly refers to CMP99 (3.127),(3.128) when grouping the quadratic action about the minimizer, and printed **p.267** Eq(2.11) has the changed source gauge quadratic G^(2), H1B/Delta1 term, and changed nonlinear jet h Ctilde^(2). Source images inspected in https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf . This direct citation validates *source lineage*, but NOT equality of old/new Q,H1,Delta1,J, background, domains, normalization, or jets.

## 2. Exact variational identity on ONE FIXED source-compatible carrier

Work on a finite real Hilbert space \`V\` equipped with the actual source inner product and **one fixed** source background, Dirichlet region and set of gauge constraints. Let G1 be self-adjoint strictly positive, Q:V→Y surjective, M=QG1Q* positive, and H1=G1Q*M^(-1). Then, algebraically,
\`QH1=I\` and \`G1^(-1)H1=Q*M^(-1)\`.
For **any** X in V with QX=B, set Y=X-H1B, so QY=0. The mixed quadratic term vanishes:
\`<Y,G1^(-1)H1B>=<QY,M^(-1)B>=0\`.
Consequently
\`<X,G1^(-1)X> = <B,M^(-1)B> + <Y,G1^(-1)Y>\`.        **(R150.V1)**

This is an exact minimizer excess identity, not an estimate and not an assumption that different source histories use the same H1. In particular it proves the minimized completed energy equals the historical inverse-average energy on that carrier. It also shows that a transported *admissible competitor* need not equal the old minimizer for a one-sided lower comparison.

## 3. Exact residual of the HISTORICAL physical/hard-gauge form

Define on the SAME carrier the historical **gauge-invariantly extended** quadratic
\`f_ext(X):=<X,G1^(-1)X>-||R D*X||²-a||QX||²\`,
as dictated by the first line of original source Eq(3.128). The original hard-gauge quadratic from (3.127) agrees with f_ext for \`RD*X=0\` (the full background nonlinear C^(2) term is already included in f_ext; this is NOT bare Wilson Hessian).

For any \`X\` satisfying \`QX=B\`, (R150.V1) gives
\`f_ext(X) - [<B,M^(-1)B>-a||B||²]\`
\`= <X-H1B,G1^(-1)(X-H1B)> - ||RD*X||².\`        **(R150.V2)**

Thus:
- If **B and X are on the historical prescribed source support**, QX=B, **and** RD*X=0, the variational difference is **nonnegative**, exactly \`||X-H1B||_{G1^-1}²\`. A new candidate on this SAME historical hard-gauge/average slice can only have greater or equal historical physical variational energy; equality is not required.
- If X is not in that hard-gauge slice, the exact term \`-||RD*X||²\` remains. No sign follows from completed positivity alone. Do NOT replace the historical gauge projector R by \`Proj ker Q'\`; the corrected source R is \`Proj_{Delta_U ker Q'}\` (R150 original-image correction).
- If X fails the source average or is on a different Ω/Λ or background Hilbert space, (R150.V1)–(R150.V2) **do not apply as written**. Arbitrary artificial frame transport, a disjoint cutoff or a synthetic identity Hessian is not an admissibility certificate.

## 4. Consequence for the already-open old/new source crosswalk

The R150 crosswalk previously introduced, **only conditionally on matched objects**,
\`q_new-q_old = G^(2) + E_var + E_jet\`,
where CMP109 (2.5) gives \`G^(2)>=0\` as an explicit squared gauge term.
R150.V2 now specifies the **source-historical** candidate variational defect for any X that has been legitimately placed in that same historical variational system:
\`E_var = ||X-H1B||_{G1^-1}² - ||RD*X||²\`.       **(R150.V3)**

In particular, once **actual source gauge/average admissibility** is proved for the transferred new candidate X and the quadratic Δ1 identifies with f_ext, E_var is NONNEGATIVE and **does not have to vanish** to preserve a lower bound. That would remove a falsely strong requirement from the earlier proposed promotion gate. The only potentially negative part would then be the nonlinear jet correction E_jet (plus any residual operator/metric/coarse-chart differences not already discharged).

**Do not promote this to native CMP109 K>=gamma0:** the 1985 and 1987 source histories demonstrably use different averaging and pivot conventions. The actual CMP109 H1, Δ1, current background, Ω/Λ, normalization, C, and historical RD* condition are not yet identified with the above fixed-carrier objects. In particular no evidence here establishes \`RD* X_new=0\` in the *historical* gauge, or even \`Q_old X_new=B\`.

## 5. Bounded determination and next source obligation

**Completed:** original-page variational expansion rechecked, exact (R150.V1)/(R150.V2) with correct gauge residual derived, and previous *conditional* transfer requirement sharpened: matching the historical minimizer exactly is UNNECESSARY if a new candidate lies on the same historical affine hard-gauge slice. **OPEN:** actual old/new source operator and support passport, current-to-old Q/gauge membership, E_jet estimate/vanishing, C and Hilbert metric transformation, full K numerics, cutoff-weighted normalization, 2 UV histories, OS axioms and mass gap.

**YM-R150 remains IN PROGRESS, NOT CONSUMED.** Next qualifying native action: source-test \`Q_old X_new=B\` and \`R_old D_old* X_new=0\` on a real matched regional configuration. If the gauge condition is not satisfied, quantify the negative residual rather than asserting positivity. No separate YM-R151 pass is opened.
