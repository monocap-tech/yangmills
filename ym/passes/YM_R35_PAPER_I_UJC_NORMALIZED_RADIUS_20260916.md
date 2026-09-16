# YM-R35 — Paper-I `U_j^c` coordinate definition / normalized-radius audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R34_CORR1_20260916.json`
Next cursor: YM-R36 (unconsumed)

## Question

R34 corrected the analytic-domain bookkeeping.  CMP119 explicitly gives

`alpha_0,j = g_j C_0 (log g_j^-2)^q_0`,
`alpha_1,j = g_j C_1 (log g_j^-2)^q_1`,

and says its localized terms extend analytically to
`U_j^c(X,alpha_0,j,alpha_1,j)`, while the exact definition of the latter is
inherited from Paper I.  R35 asks whether the Paper-I conditions (i)--(iii) can
be recovered from the accessible source corpus and, if not, what is the exact
minimum source-facing statement needed downstream.

## Durable-head and provenance preflight

The corrected R34 head was fetched before this pass.  It remains authoritative.

The external source corpus was searched for:

- `U_j^c`, `alpha_0`, `alpha_1`, `I.1.18`;
- the three conditions (i)--(iii);
- the registered CMP109 primary artifact identifier `1104116842`;
- the regular-configuration source spine.

The result is unambiguous: the public source ledger deliberately records the
Paper-I definition as an **open source target**.  The registered local artifacts
`balaban-rg-I-cmp109-1104116842.pdf` and
`text/balaban-rg-I-cmp109-1104116842.txt` exist in the external project's
private/runtime source cache, but are not committed to its GitHub tree and are
not present in this session's File Library.  Project Euclid is bibliographically
identified but the primary PDF could not be retrieved in the present harness.

Therefore R35 does not reconstruct conditions (i)--(iii) from memory, later
notation, or scalar analogues.

## Source facts that are actually available

The following are source-audited facts and may be retained:

1. CMP119 uses spaces `U_j^c(X,alpha_0,alpha_1)` defined by three multiscale
   regularity/gauge conditions (i)--(iii), with displayed bounds in the
   (2.34)--(2.39) window, and notes gauge invariance of the domain.
2. Localized regular terms `E^(j)(X,...)` have analytic extensions on those
   spaces and satisfy the Paper-I estimate `(I.1.18)`.
3. The inductive widths are

   `alpha_0,j = g_j C_0 (log g_j^-2)^q_0`,
   `alpha_1,j = g_j C_1 (log g_j^-2)^q_1`.

4. The older Bałaban regular-configuration paper, CMP 99 (1985), is an upstream
   source for gauge-invariant regularity spaces and gauge-fixing surfaces, but
   its abstract/metadata do not identify it with the exact `U_j^c` definition
   used by Paper I.  It is therefore not substituted for the missing Paper-I
   passage.

## Correct normalized-radius logic

The raw source widths shrink with `g_j`; this is not a problem by itself.
The downstream R31--R32 functional-calculus argument uses canonical variables.
Write on a fixed logarithm chart

`U = exp(g_j A)`.

Suppose one defining Paper-I condition is a local analytic functional
`F(U)` (or a finite family of such functionals) with

`F(1)=0`

and a source bound

`||F(U)|| <= alpha_r,j`,  `r in {0,1}`.

On every fixed canonical ball `||A||_N <= R`, analyticity gives

`F(exp(g_j A)) = g_j L_F(A) + O_R(g_j^2)`,

uniformly over volume whenever `F` has bounded finite-range/local
coordination.  Hence

`g_j^-1 F(exp(g_j A)) = L_F(A) + O_R(g_j)`.

The source allowance divided by the coupling is

`alpha_r,j/g_j = C_r (log g_j^-2)^q_r`.

Consequently:

- if `q_r > 0`, every fixed bounded canonical ball eventually lies strictly
  inside that condition, provided the first-order local norm of `L_F` is
  finite;
- if `q_r = 0`, a fixed ball of sufficiently small radius lies strictly inside
  whenever its linearized bound is below `C_r` by a positive margin.

This is a **criterion**, not an attribution to Paper I.  It identifies exactly
what the missing source definition must be checked against.

## Minimal source-facing contract

The R31--R32 branch does not need the full historical definition once the
following theorem-shaped contract is established from it.

### `CanonicalUjcCollar`

There exist constants

`R_eval < R_Cauchy`, `g_* > 0`, and `m_collar > 0`,

independent of volume and UV step, such that for every scale with `g_j <= g_*`:

1. every canonical field in the outer ball
   `B_N(R_Cauchy)` is mapped by `A -> exp(g_j A)` into
   `U_j^c(X,alpha_0,j,alpha_1,j)` on the relevant localization domain;
2. the inner evaluation ball `B_N(R_eval)` has distance at least
   `m_collar` from the boundary of the chosen canonical outer ball;
3. the identified gauge precision and its local coefficients are analytic on
   the outer ball with scale/volume-uniform local derivative constants;
4. the real slice has the uniform coercivity/Green margin used in R32.

Then ordinary Cauchy estimates give, for fixed derivative order `n`,

`||D^n F||_{R_eval} <= n! m_collar^-n ||F||_{R_Cauchy}`,

with constants independent of the RG step.  R32 gives the uniformly sectorial
complex precision on a possibly smaller fixed outer ball, and R31 then gives

`||D_{b_1}...D_{b_n} C_j^(1/2)(x,y)||
   <= n! K^n exp(-mu T(x,y,b_1,...,b_n))`.

Thus the entire root-localization analytic interface is reduced to
`CanonicalUjcCollar` plus the finite source dictionaries already isolated.

## Why the contract is source-shaped rather than an invented assumption

The known source scaling is favorable to the contract:

`alpha_r,j/g_j = C_r (log g_j^-2)^q_r`.

The available source description also says the domain is given by finitely
many multiscale regularity/gauge conditions and is gauge invariant.  Nothing in
the inspected record forces a canonical width tending to zero.

But without the exact Paper-I conditions it remains possible in principle that
one condition contains a nonhomogeneous normalization or another scale factor
not visible in the later summary.  `CanonicalUjcCollar` therefore remains
**source-pending**, not proved by notation alone.

## Fluctuation carrier status

No new work is required on the blocker-specific fluctuation carrier in this
cursor.  R34 already reduced it to a finite dictionary:

- product coordinates are bond-indexed `X(b)`;
- source local terms use a connected component plus a base-cube/collar
  enlargement;
- the project consumes a conservative `fluctuationSupport` inclusion;
- native covariance-root agreement remains resummed/localized, not a finite
  exact root decomposition.

That dictionary is orthogonal to the Paper-I analytic-domain cursor.

## Determination

R35 reaches a bounded negative/positive result.

**Negative:** the exact Paper-I conditions (i)--(iii) are not accessible in the
current corpus, so they cannot be honestly transcribed or claimed closed.

**Positive:** the only downstream analytic information required from those
conditions is now isolated as the theorem-shaped `CanonicalUjcCollar` contract.
The source width scaling shows why a fixed canonical collar is plausible and
why shrinking raw `alpha` parameters do not imply shrinking normalized
analytic jurisdiction.

No new obstruction from the RP blocker appears.

## Next frontier — YM-R36

**Normalized-domain splice / hypothesis-minimization audit.**

Treat `CanonicalUjcCollar` as the single explicitly source-pending analytic
record and test the complete R31 -> R28 chain under it.  The objective is to
show exactly which remaining obligations are genuinely Paper-I/source facts
and which are already derivable, so that source recovery later requires the
smallest possible theorem packet rather than another broad traversal.

## References

No new cumulative source is consumed.  Reuse [7] (CMP109 Paper I), [59]
(CMP119), [76]--[79], and the existing external source-audit records.  The
1985 regular-configuration paper was consulted only as upstream bibliographic
context and is not assigned a new source ID because it did not supply the
missing definition-level theorem.

Highest source ID remains **[79]**; next new source remains **[80]**.
