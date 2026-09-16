# YM-R58 — CMP122-II Eq. (1.101)-(1.102) post-R E/R/B return-map audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R59` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang-Mills existence or mass-gap claim.

## Target

Continue from YM-R57, which closed CMP122-II localization/exponentiation through Eq. (1.100). Audit the post-R return map:

1. recover the action split around Eqs. (1.101)-(1.102);
2. identify first-group -> boundary and second-group -> R roles;
3. determine whether the post-R density is restored to the CMP119 Sect. 2 induction class;
4. identify the next genuinely mathematical gate.

Repeated sources: [31] Balaban, *Large field renormalization II*; [59] Balaban CMP119; [22] Balaban CMP122-I.
No new bibliography item is consumed.

## 1. Source-attested post-R action split

The primary-source extraction for CMP122-II printed pp. 390-391 records the post-R action in the normalized form

`A_k((1/g_k(.))^2,U_k) = A'_k((1/g_k(.))^2,U_k) + sum_X R'^(k)(X,U_k) + sum_X B'^(k)(X,U_k)`.

The source role of the two new local families is the one established by the immediately preceding group split:

- first-group localized `R'^(k)` terms are reassigned into new boundary terms `B'^(k)`;
- second-group localized `R'^(k)` terms, disjoint from the indicated large-field region, remain the new R-sector and satisfy the canonical-metric Eq. (1.100) bound.

Thus the split is not a generic algebraic decomposition. It is the native mechanism by which the R operation returns the mixed large-field output to the two distinct CMP119 local sectors.

## 2. Return to the CMP119 action grammar

CMP119 Sect. 2 uses

`A_k = -A(g_k^-2,U_k) + E_k + R_k + B_k - mathcalE_k`.

CMP122-II Eq. (1.101) has exactly the required structural role:

- `A'_k` carries the already organized regular/background part;
- the second-group `R'^(k)` sum supplies the post-R R sector;
- the first-group contribution, renamed/reorganized as `B'^(k)`, supplies the post-R boundary sector.

The source-to-Lean equality of these objects with repository LocalActivity fields remains a formalization dictionary. It is not an unresolved mathematical decomposition theorem.

## 3. Geometric bounds survive the repartition

YM-R57 established the second-group source bound

`|R'^(k)(X,(U,J))| <= exp(-p_0(g_k)) exp(-kappa d_k(X))`.

CMP119's target R-class is

`|R^(j)(X,(U,J))| <= g_j^kappa0 exp(-kappa d_j(X))`.

The amplitudes are represented differently, but both are coupling-small amplitudes multiplying the same canonical polymer-local exponential class. The post-R second group is therefore geometrically already in the correct R-sector class.

The first group is not required to satisfy the R-sector condition because it is moved into the B sector, whose CMP119 target is a separate localized boundary estimate. This is precisely why the source performs the split.

## 4. The theorem-level return map

CMP122-II Theorem 1 provides the decisive closure statement: if the sequence of effective coupling constants remains inside `(0,gamma]` for sufficiently small positive `gamma`, then the effective densities `rho_k` have the form described in CMP119 Sect. 2 and satisfy all the conditions and bounds stated there.

Therefore the full source-level implication is

`effective-coupling window + CMP122 R operation -> CMP119 Sect.2 density class`.

This is stronger than merely checking Eq. (1.101) term-by-term: it certifies the complete induction-class return, including the density/action form and the required E/R/B conditions and bounds.

Hence the large-field return-map problem itself is CLOSED conditionally on the source's small-coupling-window hypothesis.

## 5. Eq. (1.102) / normalization status

The current extracted source packet registers Eqs. (1.101)-(1.102) jointly as the post-R action-split/handoff window but does not expose a separate exact formula for (1.102) adequate for an independent normalization theorem transcription.

This does not leave a new mathematical gate on the present critical path, because CMP122-II Theorem 1 certifies that the resulting effective densities themselves return to the full CMP119 Sect. 2 form and satisfy its conditions/bounds. Any exact equation-level dictionary for (1.102), partition-function factors, or source-to-Lean normalization fields is therefore retained as source-custody/formalization debt rather than promoted to a new theorem obligation.

If a later exact equality of partition functions or normalization constants is needed, reopen this source window specifically.

## 6. The true surviving mathematical assumption

The remaining condition is no longer local large-field control. It is the hypothesis

`0 < g_k <= gamma`

uniformly along the effective-coupling sequence, with `gamma` sufficiently small.

This is the first theorem-level condition in the now-closed small-field + large-field return architecture that is not discharged merely by local polymer estimates.

Accordingly, the critical path changes type:

`locality / resummation / R-operation`

has reached closure, and the live problem becomes

`coupling-flow / ultraviolet-window persistence`.

CMP122-II itself explicitly states Theorem 1 under the small-coupling interval rather than removing that hypothesis inside the theorem used here. Consequently we must not silently treat the interval condition as automatic.

## 7. Source-level determination

R58 closes:

1. the first-group -> `B'^(k)` and second-group -> R-sector repartition;
2. the post-R action decomposition `A'_k + sum R' + sum B'`;
3. the source-level return of the large-field R operation to the CMP119 Sect. 2 induction class, conditional on the effective-coupling interval;
4. the classification of remaining exact Eq. (1.102)/normalization dictionaries as custody/formalization work unless an exact normalization equality is later required.

Therefore:

`LargeFieldROperationReturnMap = CLOSED CONDITIONAL ON SMALL-COUPLING WINDOW`.

This is the natural STOP for the local complete-density/R-operation traversal.

## Negative results / guardrails

- Do not merge first-group B terms and second-group R terms.
- Do not identify repository LocalActivity components with source `A'_k`, `R'^(k)`, or `B'^(k)` without an explicit dictionary.
- Do not claim Eq. (1.102) has been independently transcribed when the current packet only source-locks the joint (1.101)-(1.102) handoff window.
- Do not infer that the small-coupling interval is automatically preserved.
- Do not turn the post-R polymer bound into a continuum mass-gap statement.

## Next frontier — YM-R59

`YM-R59 — effective-coupling interval / UV-window persistence audit.`

Tasks:

1. recover the precise CMP119/CMP109 coupling recursion used by the complete-density induction;
2. identify exactly what CMP122-II assumes about `{g_k}` and which source theorem, if any, proves persistence in `(0,gamma]` over the UV interval;
3. separate finite-step scheme calibration from genuine asymptotic-freedom control;
4. determine whether the RP modification changes only the finite coupling coordinate or creates any new flow obligation;
5. if the source does not remove the coupling-window assumption, isolate that as the next true theorem debt rather than hiding it inside the R-operation package.

Highest cumulative reference remains [80]; [81] remains next.