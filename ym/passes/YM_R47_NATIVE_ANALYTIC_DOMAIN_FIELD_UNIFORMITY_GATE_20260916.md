# YM-R47 — native analytic-domain / field-uniformity gate

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R46_20260916.json`
Next cursor: YM-R48 (unconsumed)

## Question

R46 ended the RP-specific audit and returned the live cursor to the native
Bałaban source baseline. R47 asks whether a fixed normalized canonical-field
ball can be inserted into the native analytic domain strongly enough that the
CMP116 termwise/localization estimates are uniform in RG scale and volume.

The two issues are deliberately separated:

1. **native field-uniformity once the field belongs to the source domain**;
2. **the coordinate/domain embedding that puts a fixed canonical ball into that
   source domain**.

## Preflight

The durable R46 checkpoint was recovered first. It records `YM-R47` as
unconsumed and keeps `CanonicalUjcEmbedding` plus CMP116 field-uniformity as
native source obligations. No RP-specific theorem debt is reopened here.

## 1. CMP116 itself supplies the field-uniform estimate mechanism

The primary CMP116 pages 15--17 were inspected directly. Printed page 15 states
that the activities under consideration are analytic functions of `(U,J)` on
`U^c_{k+1}(X,alpha_0,alpha_1)`. It then uses the **definition of that space** to
write the configuration in a complex small-field coordinate and records that
the corresponding complex gauge-field variables and `J` are small, with the
field bounds controlled by `alpha_1` and `alpha_0` respectively. [21]

This is followed by explicit perturbative estimates. In particular, the
operator error in (2.16) has kernel size of the form

`[O(1) exp(-c M) + O(alpha_0 + alpha_1)] exp(-c' distance)`.

The other quadratic/bilinear-form errors are estimated by the same source
quantity in (2.21). Equation (2.22) separately supplies the Gaussian/cutoff
suppression for the `P`-bond variables. [21]

On printed page 17 these bounds are gathered into the source parameter

`alpha_5 = O(1) exp(-c M) + O(alpha_0 + alpha_1) + O(1) alpha_4 + gamma_2`,

followed by the requirement that `alpha_5` be sufficiently small. The resulting
bound (2.26) is then used for the `D/P/Z0/Z0'` resummations leading to Lemma 3.
[21]

Thus the source proof does **not** introduce a volume-dependent field constant.
The field dependence is compressed into the native small parameters and local
geometry. Once `(U,J)` lies in the stated `U^c` domain and the native parameter
hierarchy is satisfied, the estimate is uniform over the allowed fields at
that scale.

### Determination A

The previously isolated object

`CMP116FieldUniformity`

is not an additional theorem beyond the native termwise estimate. It is part of
the source statement/proof architecture itself:

`membership in U^c + native parameter hierarchy -> uniform local termwise bounds`.

The exact source-to-project summand/field dictionary remains open as a
formalization task, but no separate mathematical field-uniformity hypothesis is
needed.

## 2. The width scaling is favorable to scale uniformity

CMP119 source-verifies that its localized regular terms have analytic
extensions on `U_j^c(X,alpha_0,j,alpha_1,j)` and that

`alpha_0,j = g_j C_0 (log g_j^-2)^q_0`,
`alpha_1,j = g_j C_1 (log g_j^-2)^q_1`.

The same source record locates the actual definition of `U_j^c` in the
multiscale regularity/gauge conditions around CMP119 (2.34)--(2.39). [59]

For fixed finite `q_r`, the raw widths tend to zero as `g_j -> 0`, but the
normalized allowances satisfy

`alpha_r,j / g_j = C_r (log g_j^-2)^q_r`.

Therefore the R35 normalized-radius criterion remains valid: after writing the
relevant source coordinates as analytic functions of `U = exp(g_j A)`, any
defining functional with first-order size `O(g_j ||A||)` admits a fixed
canonical ball whenever its normalized first-order bound fits the corresponding
source constant; for positive `q_r` the logarithmic allowance grows. This is a
DERIVATION criterion, not yet the missing source verification.

## 3. What remains open is now a finite definition/coordinate check

R35 treated the Paper-I definition as broadly inaccessible. R47 sharpens that
status. The external source ledger has a visual/source-verified locator in
CMP119 itself for the three defining multiscale regularity/gauge conditions of
`U_j^c`, around equations (2.34)--(2.39). What remains unavailable in our
current committed source packet is a faithful transcription of the actual
three defining inequalities together with the precise coordinate normalization
that relates Balaban's small complex field to the project's canonical
`U = exp(g_j A)` variable. [59]

CMP116 printed page 15 makes this coordinate seam visible: the source writes the
allowed configuration as a small complex fluctuation about a reference field,
with an exponential containing its own lattice/coupling normalization. It is
therefore unsafe to identify the source small field with the project `A` merely
from notation.

The remaining `CanonicalUjcEmbedding` obligation is consequently reduced to a
finite checklist:

1. transcribe the three CMP119 conditions (2.34)--(2.39) exactly;
2. identify the source small-field coordinate and its `L/eta/g_j` scaling;
3. substitute `U = exp(g_j A)` (and the native source/J variables) into each
   defining condition;
4. prove each condition on one fixed canonical ball using the displayed
   `alpha_0,j, alpha_1,j` scaling;
5. check that all constants are independent of volume and UV step once the
   fixed RG block parameters are chosen.

No broad new analytic theorem is indicated.

## 4. Native Cauchy/analytic reserve

CMP116 does not merely evaluate at isolated real configurations: printed page
15 explicitly treats the activities as analytic functions on the full complex
`U^c_{k+1}(X,alpha_0,alpha_1)` domain and estimates the complex perturbation
from the real/reference configuration by the source small parameters. Hence,
once `CanonicalUjcEmbedding` is proved with a strict normalized margin, the
Cauchy reserve used by the RP interpolation is source-compatible rather than a
new blocker-specific assumption. [21]

R47 does not claim a numerical collar before the exact CMP119 inequalities are
transcribed.

## Negative results / guardrails

- Do not infer a fixed canonical ball merely from the scaling of `alpha_0,j`
  and `alpha_1,j`; the exact defining source functionals and coordinate factors
  must be checked.
- Do not treat CMP116 field-uniformity as a new theorem separate from its native
  termwise estimate; the proof explicitly controls the field errors by the
  source small parameters.
- Do not confuse the CMP116 equations (2.20)/(2.22) on printed page 16 with the
  unrelated CMP119 equations carrying the same numbers.
- Do not identify Balaban's small complex field coordinate with project `A`
  until the `eta/L/g_j` normalization is extracted.
- Do not reopen RP-specific precision/root/Jacobian obligations.

## Determination

R47 closes the **field-uniformity half** of the native analytic gate at source
architecture level:

`U^c membership + native small-parameter hierarchy -> scale/volume-local field-uniform CMP116 estimate`.

The only remaining analytic-domain gate is `CanonicalUjcEmbedding`, now reduced
from a broad theorem search to a finite source-definition and coordinate
normalization audit.

In particular, the target is no longer “prove CMP116 is uniform on a fixed
ball.” The target is:

`fixed canonical ball -> CMP119/CMP116 U^c domain`.

Once that inclusion is source-locked, the native CMP116 termwise estimates
already carry the required field uniformity.

## Next frontier — YM-R48

**CMP119 (2.34)--(2.39) explicit normalized-domain inequality extraction.**

Recover the three defining conditions of `U_j^c(X,alpha_0,j,alpha_1,j)` from
CMP119, extract the exact small-field coordinate normalization, and test each
condition under `U = exp(g_j A)` on a fixed canonical ball. This is the direct
closure gate for `CanonicalUjcEmbedding`.

## References

Reused: [7] CMP109 / Paper I; [21] CMP116; [59] CMP119. No new cumulative
source consumed. Highest source ID remains **[79]**; next new source is **[80]**.
