# YM-R55 — CMP119 complete-density entry / E–R–B handoff architecture

Date: 2026-09-16
Status: COMPLETE
Claim status: UNPROVED_RESEARCH_PROGRAM
Prior canonical head: `ym/checkpoints/YM_HEAD_R54_20260916.json`
Next cursor: YM-R56 (unconsumed)

## Question

R54 closed the Paper-I/II regular small-field one-step mechanism for the present RP-compatibility traversal and moved the mathematical cursor into the complete-density problem. R55 asks what CMP119 actually adds around (2.18)–(2.23): what object is propagated, what the `T_k` operation carries, how the action splits into `E/R/B`, which sector receives the already-closed CMP116 small-field output, and where the first genuinely new large-field theorem begins.

## Preflight

The R54 checkpoint was recovered first. It records `YM-R55` as unconsumed and explicitly separates the closed regular small-field one-step from the still-open complete-density/large-field problem. No CMP116 formalization dictionary is reopened here.

Primary source locators reused from the external extraction corpus:

- CMP119 (2.17)–(2.18), printed p.257: complete effective-density form;
- CMP119 (2.19)–(2.23), printed pp.257–258: `T_k` factorization and effective-action decomposition;
- CMP119 (2.24)–(2.29), printed pp.259–260: regular `E` sector and localized running coupling;
- CMP119 (2.31), printed p.260: localized `R` bound;
- CMP119 (2.34)–(2.42), printed pp.260–262: boundary/large-field `B` sector;
- paragraph before CMP119 Theorem 1, printed p.262: improved reserve for newly generated terms;
- CMP122-I (1.70) and CMP122-II Theorem 1 / (1.98)–(1.101) remain the next large-field spine.

## 1. CMP119's propagated object is the complete effective density

**LITERATURE FACT.** CMP119 writes the effective density in the normalized structural form

`rho_k(V_k) = sum chi_k(Omega_k) * T_k * exp(A_k)`

with the sum running over the admissible large-/small-field domain data of the induction. [59]

This is the first important change of object relative to CMP116. CMP116 closes the regular fluctuation integration on a prescribed small-field domain. CMP119's object is a density that simultaneously remembers:

1. characteristic functions selecting admissible field-domain configurations;
2. the accumulated large-field integration operation `T_k`;
3. the local effective action `A_k`.

Thus the complete-density problem is not “prove a stronger version of Lemma 3.” It is to propagate the *decomposition of configuration space itself* together with the regular action.

## 2. `T_k` is the carrier of large-field geometry

**LITERATURE FACT.** CMP119 (2.19) states that if the last large-field region decomposes into disjoint components

`Z_k = X_1 union ... union X_n`,

then

`T_k(Z_k) = product_i T_k(X_i)`.

Equation (2.20) further factorizes each component through the scale history:

`T_k(X) = product_{j=k-1}^{0} T^(j)(Z_{j+1} cap X)`

with the product understood in the source's ordered scale convention. [59]

**LITERATURE FACT.** The (2.21)–(2.22) window describes each one-step operation as integrating the appropriate gauge variables on the complementary part of the next domain and fluctuation variables on the localized interior part, together with the characteristic and quadratic factors. The paper notes that the general form survives the later `R` operation, although the characteristic functions are changed. [59]

### Determination A

`T_k` is not another regular polymer activity. It is a **domain-history/integration carrier**. It records where the induction has left the regular small-field chart and how those large-field components are processed scale by scale.

This means our RP modification does not need a new `T_k` theorem merely because its regular block kernel changed: R46–R54 already show the modification remains inside the native regular one-step class. What must still be checked is how the native large-field operation acts on the complete-density class containing that regular sector.

## 3. Eq. (2.23) is the action-side E/R/B split

**LITERATURE FACT.** CMP119 writes the effective action in the form

`A_k(1/g_k^2,U_k)`
` = - A(1/g_k^2,U_k)`
`   + E_k(U_k)`
`   + R_k(U_k)`
`   + B_k(U_k,A)`
`   - mathcalE_k`.

Here the first term is the canonical lattice gauge action in the running-coupling coordinate, `mathcalE_k` is the scalar/vacuum normalization, and `E_k`, `R_k`, `B_k` are distinct localized sectors. [59]

This decomposition should not be collapsed to a generic “remainder.” The three pieces have different jurisdictions.

### `E_k`: regular/small-field effective-action sector

**LITERATURE FACT.** CMP119 (2.24)–(2.29) organizes `E_k` in localized regular pieces `E^(j)(X,U,z)`, with the paper's analyticity, gauge invariance/covariance, Euclidean covariance, support/locality and localized-running-coupling structure. Equation (2.24) defines the localized coupling function `g_j(x)` recursively; (2.29) records Euclidean covariance for the unrestricted localized sum. [59]

**DERIVATION / HANDOFF.** This is the sector into which the now-closed CMP116 regular one-step output feeds. CMP116 (2.39)–(2.41) already takes the localized `H(Z)` cluster estimate and returns a next-scale regular effective-action term satisfying the Paper-I inductive shape. R54 closed that interface. Therefore `E_k` is not a new large-field theorem obligation for the RP branch; it is the regular component carried inside the larger CMP119 density.

This does **not** identify every CMP119 `E^(j)` index with a project `LocalActivity` field. That remains formalization dictionary work.

### `R_k`: very small localized remainder sector

**LITERATURE FACT.** CMP119 (2.31) gives

`|R^(j)(X,(U,J))| <= g_j^kappa0 * exp(-kappa d_j(X))`,

with `kappa0` selectable large in the source hierarchy. [59]

So `R_k` is already typed as a polymer-local remainder with both coupling suppression and geometric decay. The source does not support replacing this by a bare scalar recurrence `R_k <= M r^k`; its localization metric and domain dependence are essential.

The new question is not the *definition* of `R_k`, but preservation/regeneration of this class when a large-field `R` operation is executed.

### `B_k`: boundary / large-field local sector

**LITERATURE FACT.** CMP119's (2.34)–(2.42) window defines the multiscale analytic domain needed for the boundary terms and gives the localized source bound

`|B^(j)(X,(U,J),A,{S_i cap X})| < B_0 * exp(-kappa d_j(X))`.

The term depends additionally on the large-field/boundary geometry represented by the source sets `S_i`. [59]

This is the first sector that is intrinsically absent from the pure regular CMP116 calculation. It exists because the complete density must remember interfaces between regular regions and regions removed into the large-field operation.

## 4. The source deliberately builds decay reserve before the R operation

**LITERATURE FACT.** Immediately before CMP119 Theorem 1, the paper states that the older-index expressions satisfy the induction assumptions while the newly generated `E^(k)`, `R^(k)` and `B^(k)` expressions are available on slightly enlarged spaces with stronger decay; the extraction ledger records the representative replacement

`kappa -> (1 + 4 beta) kappa`.

This is specifically reserve for the subsequent `R` operation. [59]

That source fact is structurally decisive: the complete-density induction is designed as

`regular RT production -> stronger fresh decay reserve -> R operation -> restore canonical E/R/B class`.

The large-field stage is therefore a **decay-spending return map**, not an independent alternative RG flow.

## 5. Where the genuinely new mathematics begins

R54 leaves us with the regular return map

`small-field input -> CMP116 H -> next E-sector output`.

R55 identifies the complete-density envelope:

`rho_k`
`  -> domain sum / characteristic functions`
`  -> T_k large-field carrier`
`  -> exp[-A + E_k + R_k + B_k - mathcalE_k]`.

The first genuinely new mathematical obligation is now:

**OPEN OBLIGATION — LargeFieldROperationReturnMap**

Given a CMP119 complete density whose fresh terms carry the required extra decay reserve, prove that the large-field `R` operation produces a new density of the same CMP119 form with:

1. the `T_k`/domain decomposition updated correctly;
2. regular pieces returned to `E`;
3. post-R localized remainder pieces satisfying the required `R` bound;
4. boundary pieces satisfying the required `B` bound;
5. the source small-coupling and enlarged-domain hierarchy preserved.

This is exactly the jurisdiction of Balaban's CMP122-I/II program. CMP122-II Theorem 1 states the endpoint: if the effective couplings remain in a sufficiently small interval `(0,gamma]`, then the resulting effective densities have the CMP119 Sect. 2 form and satisfy its conditions and bounds. [31]

Thus the new problem is not hypothetical; the literature already supplies a claimed native closure architecture. Our task is now to audit its internal obligations and identify which ones matter to the present traversal.

## 6. First CMP122 aperture

The chronological entry is CMP122-I, where the basic `R` operation generates intermediate large-field objects. The source-extracted Eq. (1.70) gives the representative bound

`|C_k^(n)(X,(U,J))| <= C_0 * exp(-(1 + 3 beta) kappa d_m(X))`,

for the stated localization domains. [22]

CMP122-II then localizes/exponentiates the post-R objects. Its (1.98)–(1.100) route produces an exponentiated `R'^(k)` family and, for the second group, the sharp bound

`|R'^(k)(X,(U,J))| <= exp(-p_0(g_k)) * exp(-kappa d_k(X))`,

before (1.101)–(1.102) repartition the post-R action into boundary and `R` pieces. [31]

Those are the first objects R56 should enter. R55 does not yet declare their proof chain exhausted.

## 7. Dependency classification after R55

### Closed / inherited on the mathematical critical path

- RP-specific regular-kernel compatibility through the Paper-I/II small-field one-step;
- canonical analytic-domain embedding;
- CMP116 `H(Z)` localization and Lemma-3 resummation;
- post-Lemma-3 return to the regular `E`-sector class;
- the *statement/form* of CMP119's complete density, `T_k` factorization, E/R/B action decomposition, R bound and B bound.

### Newly live mathematical obligations

- construction and control of the large-field `R` operation;
- decay-reserve bookkeeping through CMP122-I/II;
- post-R split returning to the CMP119 E/R/B class;
- small-effective-coupling hypothesis/flow compatibility required by CMP122-II Theorem 1.

### Side records, not current mathematical blockers

- exact source-to-Lean `LocalActivity.globalEval` dictionaries for E/R/B;
- repository encodings of CMP119 domain families and `T_k`;
- CMP116 Gaussian/Hessian/root dictionaries;
- numerical RP coupling-scheme calibration unless a later exact Lambda comparison requires it.

## Negative results / guardrails

- Do not identify `E_k`, `R_k`, and `B_k` as three names for one generic remainder.
- Do not treat `T_k` as a local polymer activity; it carries the large-field domain/integration history.
- Do not reopen CMP116 because CMP119 introduces a complete density; the regular sector is an input to, not replaced by, the complete-density construction.
- Do not infer CMP122 closure merely from CMP119's target bounds. The `R` operation is the new theorem-bearing stage.
- Do not replace the source polymer-local `R` bounds by an unsourced scalar geometric recursion.
- Do not infer continuum Yang-Mills existence or a mass gap from closure of either the small-field or complete-density lattice induction.

## Determination

R55 resolves the complete-density handoff architecture:

`CMP116 regular one-step CLOSED`
` -> CMP119 E-sector`
` + T_k large-field carrier`
` + localized R-sector`
` + boundary B-sector`.

The first genuinely new large-field theorem is the **R-operation return map** that spends the fresh `(1+4 beta) kappa`-type reserve and restores the canonical CMP119 E/R/B induction class. That moves the cursor decisively into CMP122-I/II.

## Next frontier — YM-R56

**CMP122-I basic R-operation entry / intermediate `C_k^(n)` large-field suppression audit.**

Recover the construction around the basic R-operation leading to Eq. (1.70), determine what `C_k^(n)` measures, which geometry/metric it uses, how the `(1+3 beta) kappa` decay is obtained from the CMP119 reserve, and identify the exact handoff from CMP122-I into the CMP122-II exponentiation/localization stage.

## References

Reused: [7] CMP109; [21] CMP116; [59] CMP119; [22] CMP122-I; [31] CMP122-II; [80] Cammarota remains in prior CMP116 summability custody. No new cumulative source consumed. Highest source ID remains **[80]**; next new source is **[81]**.
