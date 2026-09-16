# YM-R38 — `Delta_1/Delta_a/P_j` gauge-slice and normalization dictionary

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R37_20260916.json`
Next cursor: YM-R39 (unconsumed)

## Question

What part of the remaining CMP99/CMP102 precision seam is a genuine theorem obligation, and what part disappears once the source domain and coordinate transport are typed correctly?

## Source-attested facts already in custody

The CMP99 extraction records

`G(U) = (Delta_a(U) | Omega_0)^(-1)`

as a Dirichlet inverse on the stated source domain, together with positivity/background-field estimates. The source audit specifically warns against silently replacing the `Omega_0` domain by a different complement or ambient space.

CMP102 separately records the positive second-variation quadratic form with operator `Delta_1` at the transformed critical/background configuration.

The exact equality/transport between `Delta_1` and `Delta_a` is not yet source-extracted.

## 1. Native-space typing removes an independent projector hypothesis

The clean native object is not an inverse on the unrestricted physical bond space. Define the source fluctuation space `V_j` to be the actual gauge-fixed/Dirichlet domain on which the CMP99 Green operator acts.

On `V_j`, the native contract has the ordinary form

`G_j(U) = Delta_j(U)^(-1)`.

Only after embedding/restricting between `V_j` and an ambient physical-cochain space do projectors appear. Hence an identity-versus-projector distinction on the ambient space is a transport/typing issue unless the source itself only gives a projected inverse even on its native domain.

No separate projector theorem should be carried before that source-domain question is settled.

## 2. Normalization is dictionary data

CMP102 writes its quadratic Hessian contribution with the conventional one-half factor. Any coupling, lattice-spacing, block-scale, sign or inner-product discrepancy between source coordinates and the project precision must therefore be recorded by an explicit coordinate/normalization map.

If `T_j` is the source-to-project coordinate map, the project precision is of transported form

`P_j = T_j^(-*) Delta_src T_j^(-1)`

with any positive scalar convention written explicitly rather than promoted to an analytic theorem hypothesis.

Thus sign/normalization belongs to the source dictionary, not to a second coercivity theorem.

## 3. The remaining common-operator seam

After typing the native domain and transport, the only nontrivial source-facing bridge is

`CMP102 Delta_1  <->  CMP99 Delta_a(U) | V_j`.

The propagator side is already native to CMP99 once the operator is correctly identified; the Hessian side is already native to CMP102. R38 therefore splits record B into:

- a native background-propagator record (`Delta_a`, its domain, `G` and source bounds), and
- a Wilson-Hessian identification record establishing that CMP102's second variation is the same precision after the declared restriction/coordinate transport.

## Determination

Record B is no longer an independent analytic package. It is an operator-identity/typing problem plus the local small-background estimate isolated in R37.

Projector and free normalization fields should not survive as theorem hypotheses unless the primary source forces them after the native space is fixed.

## Negative results / guardrails

- Do not write `Delta_1 = Delta_a = P_j` on the unrestricted ambient cochain space.
- Do not replace CMP99's recorded Dirichlet domain by an inferred complement.
- Do not promote scale/sign/one-half conventions to analytic theorem debt; encode them in the coordinate dictionary.
- Do not close record B until the CMP102-Hessian/CMP99-precision bridge is actually source-locked.

## Next frontier — YM-R39

**Hessian/propagator common-operator extraction.**

Inspect whether CMP102 explicitly builds `Delta_1` from the CMP99 `Delta_a` family or whether an intermediate restriction/conjugation occurs.

## References

Reused existing CMP99/CMP102 custody. No new cumulative source is consumed. Highest source ID remains **[79]**; next new source is **[80]**.
