# YM-R36 — normalized-domain splice / hypothesis-minimization audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R35_20260916.json`
Next cursor: YM-R37 (unconsumed)

## Question

YM-R35 replaced the unavailable full Paper-I definition of
`U_j^c(X,alpha_0,j,alpha_1,j)` by a provisional theorem-shaped record
`CanonicalUjcCollar`.  That record carried:

1. fixed canonical inner/outer radii;
2. a Cauchy margin;
3. analytic local precision coefficients with uniform derivative constants;
4. a real coercivity/Green margin.

R36 asks which of those are genuinely independent source facts once the
already-custodied native precision/root machinery and the R28--R32 reductions
are spliced together.

## Preflight

The durable entry head was recovered and confirmed:

`YM-R35 COMPLETE -> YM-R36`, with R36 unconsumed.

R35 remains authoritative that the exact Paper-I conditions (i)--(iii) are
source-definition-pending, while CMP119 source-verifies

`alpha_0,j = g_j C_0 (log g_j^-2)^q_0`,
`alpha_1,j = g_j C_1 (log g_j^-2)^q_1`.

No attempt is made here to reconstruct the missing Paper-I definition.

## 1. Paper-I record minimizes to a single embedding theorem

Let `B_C(R)` denote a fixed complex canonical-field ball in the normalized
variables used after writing `U = exp(g_j A)` (and including any native source
variables required by the original activity, but no new source variables from
the RP blocker).

The only Paper-I-specific fact needed downstream is:

### `CanonicalUjcEmbedding`

There exist `R_outer > 0` and `g_* > 0`, independent of volume and UV step,
such that whenever `g_j <= g_*`,

`A in B_C(R_outer)  ->  exp(g_j A) in U_j^c(X,alpha_0,j,alpha_1,j)`

on every localization domain for which the native CMP116 activity is used.

Once this is available, choose rather than source

`R_eval = R_outer/2`.

Then the Cauchy margin is simply

`m_C = R_outer - R_eval = R_outer/2`.

Thus **inner radius and Cauchy margin are not independent source fields**.
Any other fixed fraction of `R_outer` would work equally well.

The source scaling from R34/R35 explains why this theorem is plausible but
still does not prove it:

`alpha_r,j / g_j = C_r (log g_j^-2)^q_r`.

The exact Paper-I defining functionals and their normalizations remain the
only way to verify the embedding honestly.

## 2. Precision analyticity does not belong in the Paper-I record

The covariance/root route concerns the exact gauge fluctuation precision, whose
source spine is CMP99/CMP102 (background propagator, variational Hessian and
positive quadratic form), not the definition of `U_j^c` itself.

Therefore the precision fields carried by the provisional
`CanonicalUjcCollar` must be separated into an independent native record:

### `NativeLocalPrecisionCertificate`

At source/dictionary level it must identify the actual gauge precision
`P_j(U)` and establish the source-natural local facts needed on the canonical
outer domain:

- exact source-to-project precision/Hessian identity;
- finite-range/local dependence with volume-independent coordination;
- holomorphic dependence on the local complexified background variables;
- a uniformly coercive flat/reference precision (or equivalently the native
  positive/inverse Green bound needed to produce the same margin).

A separate list of all derivative constants is unnecessary.  Once the local
coefficient maps are holomorphic on the outer ball and uniformly bounded there,
ordinary Cauchy estimates on `B_C(R_eval)` give

`||D^n P_j|| <= n! m_C^(-n) M_P`

for the derivative orders required by the weakening/root localization.

Thus **precision derivative constants are consequences, not independent
source hypotheses**.

## 3. Real and complex coercivity are also consequences

There are two equivalent sufficient native routes already visible in the
source/formal architecture.

### General local-precision route

Let `P_0,j` denote the identified flat/reference precision.  Assume its
coercivity margin is `m_0 > 0` uniformly in UV scale/volume.  Local analyticity
and `U=exp(g_j A)` imply on the fixed canonical outer ball

`||P_j(exp(g_j A)) - P_0,j|| <= C_P(R_outer) g_j`.

For sufficiently small `g_j`, choose

`C_P(R_outer) g_j <= m_0/2`.

Then on the complex evaluation tube

`Re <v,P_j v> >= (m_0/2)||v||^2`,

and hence

`||(P_j+r)^(-1)|| <= (m_0/2+r)^(-1)` for `r >= 0`.

So **complex coercivity/resolvent norm is derived** from the flat native margin
plus local analytic dependence; it need not be carried by Paper I.

### Normalized local-SPD route

The external formal source-independent layer already exhibits the stronger
sufficient shell

`precision = scale * (id - normalizedPerturbation)`,
`||normalizedPerturbation|| <= operatorRatio < 1`,

with finite-range kernel majorant data.  From that record it derives the real
coercivity constant

`scale * (1 - operatorRatio)`,

the spectral upper bound, exact finite range, Neumann-resolvent exponential
decay, and inverse-square-root kernel tail bounds.  The external implementation
still leaves exact operator root semantics/kernel identification as separate
fields, but mathematically R31 supplies those through analytic functional
calculus once the complex domain is available.

This confirms the logical minimization: carrying both a domain collar and
independent coercivity/root-decay hypotheses duplicates information.

## 4. Root bounds are downstream consequences

Under `CanonicalUjcEmbedding + NativeLocalPrecisionCertificate`, R32 gives a
uniform complex resolvent subdomain.  R31 then gives, for background insertions
`b_1,...,b_n`,

`||D_{b_1}...D_{b_n} P_j^(-1/2)(x,y)||
  <= n! K^n exp(-mu T(x,y,b_1,...,b_n))`

with a finite loss in spatial exponent.

Benzi--Razouk [76] and Higham--Relton [78] remain model-independent controls
for the decay/analytic matrix-function mechanism; no new source is needed.

Therefore the following are **not independent source hypotheses** once the
native precision certificate is established:

- covariance/root operator norm bounds;
- exponential root kernel decay;
- higher background derivative bounds;
- the factorial analytic growth used by weakening interpolation.

## 5. Hidden fluctuation-variable issue: the Gaussian field is unbounded

The fixed Paper-I/Cauchy ball controls external/background canonical fields.
CMP116's product-Gaussian variable `X(b)` is integrated over an unbounded
finite-dimensional Gaussian space, so it would be incorrect to require the
same pointwise fixed tube in `X`.

This does not create a new source hypothesis for the RP blocker.

R26 gives the local jet, schematically on a chart,

`K_soft/K_Gauss = exp[g_j F_3(A,B) + O(g_j^2 poly(A,B))]`,

where `F_3` is a fixed local polynomial and the initial support is finite.
Choose a moderate-fluctuation threshold

`|X| <= g_j^(-sigma)`,  with `0 < sigma < 1`.

On this region `g_j X -> 0`, so the logarithm/chart expansion remains inside
the regular group neighborhood for small `g_j`; the activity admits a
polynomial Gaussian majorant of the form

`|V_soft(A,X)| <= C g_j (1+|X|^m) exp(c g_j(1+|X|^m))`

for fixed local degree/order after possibly reducing the moderate exponent.
Standard Gaussian moments then preserve the `O(g_j)` integrated amplitude.

On the complementary region, Gaussian concentration gives a tail of the form

`P(|X| > g_j^(-sigma)) <= C exp(-c g_j^(-2 sigma))`,

which is smaller than every positive power of `g_j`.  The exact compact-group
heat-kernel factor remains the underlying object there; one does not need to
extend the local logarithm branch pointwise throughout the Gaussian tail.

Hence the correct norm before CMP116 localization is a **mixed
analytic/Gaussian-integrable norm**, not a supremum over all `X`.
The product-Gaussian interface is already native/source-identified, so this
moderate/tail split is a derived estimate rather than a new Paper-I theorem.

This refines R26/R29: their fixed-tube statement is sufficient for external
fields and moderate fluctuations, while the unbounded Gaussian tail must be
handled by Gaussian integrability rather than by a global pointwise log.

## 6. Splice through R29 and R28

With the native covariance-root localization available, R29 applies the same
weakening/random-walk machinery to the `O(g_j)` local soft activity and yields

`|H_soft(Z)| <= C_soft' g_j exp(-mu' d(Z))`.

No inverse power of `g_j` is introduced.

R28 then substitutes

`epsilon_tilde = epsilon_1 + C_soft' g_j`.

The D-stage spends only linear smallness reserve, the P-stage entropy rate
improves as `epsilon_tilde/g_j` increases, `C_3` is unchanged, and the
post-Lemma-3 amplitude closes for sufficiently weak `g_j`.

Therefore `CanonicalUjcEmbedding` plus the **native** precision/localization
package is enough to splice the preferred RP blocker through the complete
R31 -> R28 chain.

## 7. Hypothesis-minimization result

The provisional R35 record

`CanonicalUjcCollar = {outer radius, inner radius, margin,
                       precision derivative constants,
                       real coercivity/Green margin}`

is over-specified.

The genuinely independent source-facing packet separates by provenance:

### A. Paper-I analytic-domain fact

`CanonicalUjcEmbedding`

- one fixed canonical outer radius;
- one weak-coupling threshold;
- inclusion into the source `U_j^c` domain.

Nothing else belongs in the Paper-I packet.

### B. Native gauge-precision fact

`NativeLocalPrecisionCertificate`

- exact CMP99/CMP102 precision/Hessian dictionary;
- local finite-range holomorphic dependence;
- flat/reference uniform coercivity (or equivalent Green/inverse bound).

Cauchy derivatives, complex coercivity, resolvent/root decay and higher root
jets are downstream consequences.

### C. Native CMP116 support dictionary

The already-separated finite map from source localization domains/bonds to
external and fluctuation-support envelopes.  This remains orthogonal to A/B.

### D. No new blocker-specific source theorem

The RP blocker contributes internally established facts:

- exact reflection-positive compact-group kernel;
- globally defined anchored center;
- local `O(g_j)` analytic jet;
- finite initial support;
- Gaussian-tail integrability as above.

Once A--C close for the native Bałaban step, R28--R29 show that the blocker
needs **no additional source theorem**.  In that precise relative sense, the
RP modification is hypothesis-neutral with respect to the native one-step
cluster expansion.

## Negative results / guardrails

- Do not keep coercivity/root-decay fields inside the Paper-I domain record.
- Do not demand a pointwise fixed complex tube for the unbounded Gaussian
  fluctuation variable `X`; use moderate/tail Gaussian control.
- Do not claim the external formal local-SPD shell has already identified the
  physical Wilson Hessian; that dictionary remains source-open.
- Do not claim `CanonicalUjcEmbedding` proved until the exact Paper-I
  conditions are recovered.
- Do not conflate the finite support dictionary with analytic-domain or
  precision hypotheses.

## Determination

R36 closes the hypothesis-minimization audit.

The only Paper-I-specific analytic assumption required downstream is the
single canonical-domain embedding theorem.  The former collar/coercivity/root
fields are either chosen geometrically or derived from the independent native
precision certificate.  The unbounded product-Gaussian variable introduces no
new source theorem after a moderate-field/Gaussian-tail split.

Thus the preferred reflection-positive blocker branch adds **zero independent
source hypotheses** beyond the native Bałaban closure package; it only adds
new derived estimates that have now been isolated.

## Next frontier — YM-R37

**Exact precision identity / small-background defect audit.**

The inaccessible Paper-I definition can remain a provenance task.  The next
available analytic frontier is the other independent record B above:

1. identify CMP102 `Delta_1` / CMP99 `Delta_a,G(U)` with the exact project
   fluctuation precision;
2. extract the flat/reference coercivity normalization;
3. prove/source the local small-background defect
   `P_j(exp(g_j A)) - P_0,j = O(g_j)` in a finite-range operator/kernel norm;
4. determine whether this directly instantiates the native local-SPD/weighted
   resolvent certificate without additional hypotheses.

YM-R37 is unconsumed here.

## References

Reused: [7] CMP109/Paper I; [21] CMP116; [59] CMP119; [76] Benzi--Razouk;
[78] Higham--Relton; [79] CMP99 background propagator.  No new cumulative
source is consumed.  Highest source ID remains **[79]**; next new source is
**[80]**.
