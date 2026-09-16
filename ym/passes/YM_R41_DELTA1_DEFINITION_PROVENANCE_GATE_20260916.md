# YM-R41 — direct `Delta_1` definition provenance / record-B closure gate

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R40_20260916.json`
Next cursor: YM-R42 (unconsumed)

## Question

Can the first primary CMP102 definition of `Delta_1` now be recovered strongly enough to classify it as:

1. literal `Delta_a` at `a=1`;
2. an explicit restriction/conjugation of that operator; or
3. a genuinely different Hessian/precision operator?

## Repository preflight

The canonical repository head before this pass was R40. R37--R40 have now been append-only custodied, restoring the conversational traversal to repository authority before consuming R41.

Existing source custody still records only the endpoints:

- CMP99: `Delta_a(U)` and `G(U)=(Delta_a|Omega_0)^(-1)`, plus positivity/background-field bounds;
- CMP102: Eqs. (44)--(46) for the variational/linearizing construction and Eq. (142) for the positive quadratic form `(1/2)<A',Delta_1 A'>`.

The literal first definition of `Delta_1` is not present in the committed source extract.

## Direct provenance attempt

Public bibliographic/metadata access confirms the CMP102 article and its dependence on the CMP99 background-propagator paper, but the openly retrievable web body does not expose the internal definition window needed to identify `Delta_1` exactly.

The existing independent source-audit corpus likewise continues to mark the `Delta_1`/`Delta_a` source dictionary as open rather than source-verified.

Therefore none of outcomes (1)--(3) can honestly be promoted to a LITERATURE FACT from the presently retrievable primary body.

## Important correction to R39's notation inference

R39 recorded `Delta_1 = Delta_a|_{a=1}` as a strong candidate while explicitly keeping it unverified. R41 tightens that guardrail.

A separate Balaban-group exposition of exact RG uses subscripts such as `Delta_1` for first-step/effective quadratic forms produced after constrained minimization and block-field splitting. That is not evidence about the CMP102 definition itself, but it is sufficient to show that **the subscript `1` cannot be interpreted as the parameter value `a=1` by notation alone**.

Hence the R39 candidate is downgraded from "notation-strong" to:

`plausible dictionary candidate; no evidentiary weight from the subscript itself`.

This is a NEGATIVE RESULT about an inference route, not a new theorem about CMP102.

## Consequence for record B

`NativeLocalPrecisionCertificate` does **not** close in R41.

What is closed:

- the analytic-output minimization from R37;
- the native-domain/projector typing from R38;
- the coordinate-transport warning from R39;
- the homogeneous `A'` tangent-slice derivation from R40, conditional on the translation definition.

What remains open:

- the exact source identity between CMP102 `Delta_1` and CMP99 `Delta_a/G(U)`;
- the local source estimate/identity sufficient to instantiate the project `P_j(exp(g_j A))-P_0,j = O(g_j)` defect on the same operator.

Thus the remaining blocker is still source/operator custody, not generic functional analysis.

## Bounded determination

R41 reaches a hard provenance boundary: the available extracted primary windows are insufficient to classify the `Delta_1` definition. The correct result is **not** to guess the missing line.

The direct-definition route remains open, but the investigation need not stall on it. The already-numbered one-step RG sources downstream of CMP102 can be audited for the actual fluctuation precision/covariance used in the Gaussian integral and its back-reference to the background-field propagator. If that downstream paper gives an explicit operator formula/dictionary, record B may close without relying on the missing definition page.

## Negative results / guardrails

- Do not infer `Delta_1 = Delta_a|_{a=1}` from the subscript `1`.
- Do not mark record B closed from shared positivity/propagator estimates alone.
- Do not invent the missing CMP102 definition from later notation.
- Do not consume a new bibliography source merely to compensate for inaccessible primary body while already-numbered downstream Bałaban sources may contain the needed dictionary.

## Next frontier — YM-R42

**Downstream one-step precision back-reference audit (CMP109/CMP116).**

Use the already-custodied one-step RG source spine to identify the exact precision/covariance entering the fluctuation Gaussian and determine whether it explicitly back-references CMP99/CMP102 in a way that fixes:

1. the operator identity;
2. the native gauge/block domain;
3. the covariance inverse relation;
4. the small-background/locality estimate needed by R37.

This route may close record B without a new source and without guessing the inaccessible CMP102 definition.

YM-R42 is unconsumed here.

## References

Reused existing CMP99/CMP102/CMP109/CMP116 custody. A public secondary Balaban-group exposition was consulted only as an inference guardrail and is **not** promoted into the cumulative bibliography or used to establish a CMP102 fact. No new cumulative source is consumed. Highest source ID remains **[79]**; next new source is **[80]**.
