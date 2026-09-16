# YM-R52 — CMP116 Eq. (2.31) P-family carrier/count and entropy audit

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R51_20260916.json`
Next cursor: YM-R53 (unconsumed)

## Question

Determine the source-native carrier behind the CMP116 Eq. (2.31) P-sum, decide whether the native count is the four-positive-direction carrier or the source-neutral eight-incidence fallback, and close the scalar entropy bracket with the source rate

`rho = gamma2 * epsilon1^2 / (20 * gk^2)`.

## Source facts

The source-audit corpus visually confirms that on CMP116 page 12:

- `Y0^{c,*}` is the set of T(k)-bonds contained in `Y0^c`, excluding special `b0(c)` bonds;
- Eq. (2.3) sums over `P` subsets of `Y0^{c,*}`;
- `Z0` is the smallest localization domain containing `Y0` and `P`;
- each P-bond lies in the interior of `Z0` and does not intersect `dZ0`.

CMP109 supplies the ambient nearest-neighbor bond convention `b=(b_-,b_+)` and positive orientation.

CMP116 pages 18-19 visually confirm the Eq. (2.31) P-sum with

`rho = gamma2*epsilon1^2/(20*gk^2)`,

source gap mass

`G = M^(-4) * |Z0 \ Y0|`,

and the scalar bracket

`4*M^4*exp(-2*rho) <= rho`.

## Native carrier

Because a source-admissible P-bond is contained in `Y0^c` and is also contained in the interior of `Z0`, both endpoints of the bond lie in `Z0 \ Y0`. After choosing the standard positive orientation, every bond is uniquely determined by:

1. its positive tail/base cube in `Z0 \ Y0`;
2. one of the four positive coordinate directions in dimension four.

Therefore the native eligible-bond carrier has cardinality at most

`4 * |Z0 \ Y0|`.

The factor-eight incidence carrier constructed in the independent formalization repository is a conservative representation fallback only. It is needed there because the source-to-Lean statement `encoded first coordinate = source positive tail` was deliberately left unpromoted. That encoding seam is not a mathematical source obstruction once source bonds are typed by their positive orientation.

## Powerset entropy

Let

`N = |EligibleCarrier(Z0,Y0)| <= 4*|Z0 \ Y0|`.

Then

`sum_{P subset EligibleCarrier} exp(-2*rho*|P|)`
`= (1 + exp(-2*rho))^N`
`<= exp(N*exp(-2*rho))`
`<= exp(4*|Z0 \ Y0|*exp(-2*rho))`.

Multiplying by the source gap factor

`exp(-rho*M^(-4)*|Z0 \ Y0|)`

gives

`exp(-(rho*M^(-4) - 4*exp(-2*rho))*|Z0 \ Y0|)`.

Thus the source bracket

`4*M^4*exp(-2*rho) <= rho`

implies the fixed-Z0 P-sum is at most one.

This reproduces the CMP116 Eq. (2.31) entropy mechanism exactly at source level.

## Parameter hierarchy

The primary scalar gate is the source bracket itself. A simple stronger sufficient condition is

`rho >= 4*M^4`,

because `exp(-2*rho) <= 1`. In source variables this is implied by

`80*M^4*gk^2 <= gamma2*epsilon1^2`.

This stronger inequality is only a convenient reducer; it must not replace the native bracket in custody.

## Determination

The native P-stage carrier is the four-positive-direction carrier, not the factor-eight incidence fallback. The source entropy calculation is closed by the displayed Eq. (2.31) bracket. Remaining `PIndex`/encoded-first-coordinate fields in the independent Lean formalization are project dictionary debt, not mathematical source debt.

Therefore:

`CMP116Eq231CarrierCount: CLOSED (source/mathematical level)`

`CMP116Eq231EntropyBracket: CLOSED`

`CMP116 Eq. (2.31) P-stage combinatorial sum: CLOSED`

The next native seam is the post-P/fixed-Z0' geometry and exponent reserve in Eq. (2.32)-(2.37).

## Negative results / guardrails

- Do not replace the native factor 4 by factor 8 merely because a source-neutral Lean incidence carrier exists.
- Do not use the Eq. (2.31) lower bound on `|P|` as the carrier upper bound; carrier count comes from positive-oriented bonds over `Z0 \ Y0`.
- Do not replace the primary source bracket `4*M^4*exp(-2*rho) <= rho` by the stronger sufficient inequality `rho >= 4*M^4`.
- Do not infer that the remaining post-P resummation is closed; Eq. (2.32)-(2.37) remains live.
- No Yang-Mills existence or continuum mass-gap theorem is claimed.

## References

Reused: [21] CMP116 and [7] CMP109. No new cumulative source consumed. Highest source ID remains [80]; next new source is [81].
