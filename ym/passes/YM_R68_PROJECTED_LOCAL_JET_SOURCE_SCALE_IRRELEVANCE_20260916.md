# YM-R68 — projected local-jet norm / source-scale irrelevance audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R69` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R67, which retyped the collapsed local regular sector as a repeatedly projected quotient flow

`J_j^irr ~= J_j / span{1,A}`

with candidate projected map

`T_hat_j = (1-Loc_{j+1}) T_j | J_j^irr`.

R67 proposed the sharp native target

`||T_hat_j K|| <= L^(-2+epsilon_j) ||K||`

based on dimension-six power counting after vacuum/Wilson extraction.

R68 asks whether the published Bałaban architecture actually needs or supplies such a one-step quotient operator contraction, or whether a weaker **source-scale irrelevance estimate on the generated scale-j activity itself** is the more faithful object.

Repeated primary/control sources: [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [68] Curci–Menotti–Paffuti / Symanzik dimension-six control source.

New secondary locator: [85] Eriksson, *The Balaban–Dimock Structural Package*. It is used only to target exact CMP109 equations and is explicitly **not** installed as primary evidence. AIRR labels the record a historical import, not correctness-assessed, and the manuscript's v2 changes its status from unconditional to traceable/conditional.

## 1. CMP116 does not visibly provide the sharp quotient contraction

CMP116's source-attested cluster step starts from localized activity bounds and uses the fine-to-coarse geometry, including Eq. (2.36),

`2 d_k(Z_i) >= L d_{k+1}(Z_i')`,

then spends part of the resulting exponential gain on polymer entropy, localization losses and exponentiation.

The end product is restored to the next inductive class with a regular-action amplitude fitting the prescribed `E_0` budget.

This has the logical form

`admissible E_k -> admissible E_{k+1}`

with a uniform absolute bound.

It is not visibly of the form

`|| (1-Loc) T(K) || <= q ||K||, q<1`

for arbitrary local quotient perturbations.

Thus:

`CMP116AbsoluteClosure != ProjectedLocalJetOperatorContraction`.

Canonical status:

`SharpNativeLminus2QuotientContraction = NOT SOURCE-EXTRACTED`.

## 2. A secondary traceability manuscript points to a stronger-looking Paper-I source-scale estimate

Reference [85] is an AI-assisted secondary traceability manuscript, not a primary theorem source. Its value for the present traversal is that it identifies a concrete CMP109 equation chain that was not previously in the project source cursor.

It attributes the following roles to CMP109:

- Eq. `(3.34)`: local Taylor expansion of small-polymer activities to finite order;
- Eqs. `(4.14)`–`(4.15)`: Ward/gauge identities removing forbidden low-order local structures and constraining the Taylor coefficients;
- Eq. `(5.37)`: decomposition of the quadratic polarization tensor into the canonical transverse/Wilson direction plus a higher-derivative remainder;
- Eq. `(5.42)`: definition/extraction of the beta coefficient;
- Eq. `(0.29)`: an irrelevance estimate for the marginal-subtracted small-polymer contribution with a positive extra power of the source lattice spacing.

The secondary normalized shape reported for the last item is

`|V^(j)(X,U_k)| <= C (L^j eta)^(4+alpha) exp(-kappa d_j(X))`

for some `alpha>0`.

This formula is **not promoted here as primary-verified CMP109 text**. The exact symbol `V^(j)`, allowed polymer class, range of `alpha`, scale convention, constants, hypotheses and norm must all be checked against [7].

Canonical status:

`PaperISourceScaleIrrelevanceBound = LOCATED VIA SECONDARY TRACEABILITY / PRIMARY VERIFICATION OPEN`.

## 3. If the candidate Paper-I bound is correct, the sharp L^-2 target was over-specified

Let `a_j` denote the physical lattice spacing at the source scale of a fresh marginal-subtracted regular contribution, with `a_j -> 0` as that source scale is moved into the ultraviolet.

Assume the primary source ultimately verifies a bound of the form

`|V_j(X)| <= C a_j^(4+alpha) exp(-kappa d_j(X))`,

with `alpha>0`, together with a uniform rooted polymer summability estimate

`sup_b sum_{X contains b} exp(-kappa d_j(X)) <= C_kappa`.

Fix a physical region `O`. The number of scale-j lattice cells/bonds needed to cover `O` is `O(a_j^-4)` in four dimensions.

Then

`sum_{X: X intersects O} |V_j(X)|`

is bounded by rooting every contributing polymer at a cell/bond of `O`:

`<= C a_j^(4+alpha) * (# roots in O) * C_kappa`

`<= C_O C C_kappa a_j^alpha`.

Therefore

`|| V_j ||_{fixed physical region} = O(a_j^alpha) -> 0`.

Classification: **DERIVATION**, conditional on the candidate primary bound and rooted polymer summability.

The dimension-four counting factor cancels the `a_j^4` part of the native activity estimate; only the strictly positive irrelevance exponent `alpha` is needed.

This is the key R68 simplification:

`alpha>0 is sufficient`.

There is no need for a sharp operator eigenvalue corresponding to `alpha=2`.

## 4. Geometric summability follows immediately under fixed-ratio UV refinement

Suppose successive ultraviolet depths change the microscopic spacing by the fixed block factor `L>1`:

`a_UV^(N) = a_* L^(-N)`

at a fixed reference physical scale.

Then the previous estimate gives

`epsilon_N^E <= C_O a_*^alpha L^(-alpha N)`.

Hence

`sum_N epsilon_N^E < infinity`

for every `alpha>0`.

Combining with the elementary R66 normalized-density perturbation estimate yields Cauchy convergence of every bounded fixed-endpoint cylindrical observable with respect to this E-sector defect.

Thus the source-scale estimate, if primary-verified, is stronger for the cross-cutoff problem than a same-scale statement `||E_j|| <= E_0`: it encodes ultraviolet provenance directly in the coefficient.

## 5. This is not the same theorem as one-step contraction

The candidate Eq. `(0.29)` object and the R67 quotient map answer different questions.

### Quotient operator contraction

`||T_hat_j K|| <= q ||K||`

compares arbitrary nearby quotient perturbations under one RG step.

### Source-scale irrelevance

`|V^(j)(X,U_k)| <= C a_j^(4+alpha) exp(-kappa d_j(X))`

bounds the actual fresh scale-j contribution produced by the canonical construction, retaining its source-scale label even when evaluated in later variables.

The second may be enough for the **specific cross-cutoff difference generated by one extra ultraviolet layer**, even if the first is unavailable as a Banach-space theorem.

Accordingly:

`RenormalizedLocalJetQuotientContraction`

is retained as a powerful sufficient theorem but is no longer the minimal native target.

Canonical retyping:

`SharpLminus2ProjectedContraction = OVER-SPECIFIED SUFFICIENT TARGET`.

`PositiveAlphaSourceScaleIrrelevance = MINIMAL CANDIDATE NATIVE TARGET`.

## 6. The secondary locator also supports the exact projection route, but primary verification remains mandatory

Reference [85] reports a source chain in which the local Taylor expansion is constrained by gauge/Ward identities, the quadratic polarization is decomposed into a canonical transverse part plus higher-derivative remainder, and the beta coefficient is extracted from that transverse part.

If the primary equations `(5.37)` and `(5.42)` confirm this description in the needed normalization, they would substantially close the R64–R67 object

`PaperIBulkWilsonProjectionIdentity`.

But the project presently does not possess the primary CMP109 equation pages in the `yangmills` repository or File Library, and the auxiliary public source-audit corpus keeps its primary CMP109 PDF in an uncommitted/private source cache.

Therefore:

`PaperIBulkWilsonProjectionIdentity = STILL OPEN`.

The secondary equation map changes the **location** of the source boundary, not its epistemic status.

## 7. Why the candidate exponent need not equal the engineering value two

R67 derived `L^-2` from the generic dimension-six continuum classification after exact removal of vacuum and `F^2`.

A rigorous constructive bound may deliberately lose part of this sharp engineering exponent because of:

- analytic-domain/Cauchy losses;
- localization enlargement;
- polymer counting;
- background-field and gauge-coordinate estimates;
- finite Taylor remainder bookkeeping.

A source theorem with only some `alpha>0` is therefore entirely adequate for ultraviolet-memory loss.

The right proof obligation is not

`prove alpha=2`,

but

`prove alpha is uniformly positive under the native Paper-I hypotheses`.

This makes the canonical target substantially more robust.

## 8. Relation to the R66 extended/local split

R66 split the regular sector into:

`ExtendedEGeometricTransport`

and

`CollapsedLocalEJetIrrelevance`.

A primary-verified source-scale bound of the candidate `(0.29)` form would partly supersede this split for the small-polymer sector.

The factor `exp(-kappa d_j(X))` controls polymer extension while the factor `a_j^(4+alpha)` controls source-scale irrelevance, including the zero-diameter local case after fixed-region counting.

Thus one source estimate could carry both resources:

`space localization * scale irrelevance`.

However large-field/boundary components remain separately typed; R68 does not infer their convergence from the small-polymer candidate bound.

## 9. Minimal conditional E-sector Cauchy theorem

The R68 derivation can be stated independently of the disputed equation locator.

Assume for every fresh ultraviolet E-activity at spacing `a_N`:

1. `|V_N(X)| <= C a_N^(4+alpha) exp(-kappa d_N(X))`, with `alpha>0`;
2. `sup_b sum_{X contains b} exp(-kappa d_N(X)) <= C_kappa` uniformly in `N`;
3. a fixed physical endpoint region `O` contains at most `C_O a_N^-4` scale-N roots;
4. the source-scale activity is transported into the fixed endpoint action without losing the positive power `a_N^alpha`.

Then the endpoint E-defect obeys

`epsilon_N^E <= C C_kappa C_O a_N^alpha`.

If `a_N <= C_a L^-N`,

`epsilon_N^E <= C' L^(-alpha N)`

and

`sum_N epsilon_N^E < infinity`.

Therefore every fixed bounded endpoint observable has a Cauchy expectation sequence with respect to the E-sector correction.

Classification: **DERIVATION / CONDITIONAL THEOREM SHAPE**.

Condition 4 is exactly what the primary meaning of the claimed `V^(j)(X,U_k)` formula must settle. It must not be silently assumed.

## 10. Determination

R68 establishes:

1. CMP116's published cluster closure restores the regular activity to the admissible `E_0` class; it is not presently source-extracted as a strict quotient operator contraction.
2. A secondary traceability manuscript [85] identifies a concrete CMP109 primary-source chain, culminating in a claimed source-scale irrelevance estimate Eq. `(0.29)` with a positive exponent `alpha`.
3. [85] is explicitly historical/not correctness-assessed by AIRR and v2 downgrades its own status to traceable/conditional; it is therefore a locator, not theorem evidence.
4. Conditional on a primary bound `C a^(4+alpha) e^-kappa d` and uniform rooted polymer summability, fixed-physical-region E-defects are `O(a^alpha)` in four dimensions.
5. Under fixed-ratio UV refinement this is geometrically summable for every `alpha>0`.
6. Therefore the sharp `L^-2` projected contraction target of R67 is sufficient but over-specified for the cross-cutoff E-memory problem.
7. The more faithful minimal target is a source-scale irrelevance theorem with any uniform positive exponent.
8. The exact Paper-I beta/Wilson projection identity remains open until CMP109 Eqs. `(5.37)` and `(5.42)` are checked against the primary source.
9. Large-field/boundary terms remain separate and are not closed by this E-sector analysis.

Canonical state:

`SharpNativeLminus2QuotientContraction = NOT SOURCE-EXTRACTED / OVER-SPECIFIED`.

`PaperISourceScaleIrrelevanceBound = LOCATED VIA [85]; PRIMARY VERIFICATION OPEN`.

`PositiveAlphaSourceScaleIrrelevance => FixedRegionEUVMemoryLoss = DERIVED`.

`FixedRatioUVRefinement => EDefectSummability = DERIVED`.

`PaperIBulkWilsonProjectionIdentity = OPEN PRIMARY-SOURCE BOUNDARY`.

`CollapsedLocalEJetIrrelevance = CONDITIONALLY REDUCED TO PaperISourceScaleIrrelevanceBound`.

`NativeComplementaryDifferenceContraction = retained as fallback; still OPEN`.

## Negative results / guardrails

- Do not cite [85] as proof of CMP109 Eq. `(0.29)` or the beta extraction; use it only as a primary-source locator until the scan is checked.
- Do not retain the v1 claim of an unconditional discharge; v2 explicitly retracts that status.
- Do not reverse the UV/IR direction of the irrelevance factor. The useful small parameter is the source spacing approaching zero toward the ultraviolet cutoff removal.
- Do not demand the sharp engineering exponent `alpha=2`; any uniform `alpha>0` suffices for the fixed-region summability argument.
- Do not confuse a source-scale bound on canonical generated activities with a Fréchet contraction theorem for arbitrary quotient perturbations.
- Do not infer boundary/large-field convergence from the small-polymer E estimate.
- Do not infer continuum Yang–Mills existence, OS reconstruction, infinite-volume convergence, or a mass gap from R68.

## Next frontier — YM-R69

`YM-R69 — primary CMP109 irrelevance-chain extraction / custody audit.`

Tasks:

1. obtain and inspect the primary CMP109 pages containing Eqs. `(0.29)`, `(3.34)`, `(4.14)`–`(4.15)`, `(5.37)`, `(5.42)`;
2. verify the exact definition of `V^(j)`, its polymer/domain class, analytic norm and dependence on the later field `U_k`;
3. verify the sign, normalization and exact extraction definition of `beta_j` and whether it is the bulk Wilson/`F^2` projection needed by R64–R67;
4. verify the precise `alpha>0` statement, constant dependencies, scale orientation, finite-volume uniformity and allowed RG window in Eq. `(0.29)`;
5. if verified, promote the fixed-region `O(a^alpha)` E-sector summability lemma from conditional to source-fed and reconnect it to the R62 cross-cutoff defect;
6. if the secondary locator is inaccurate, revoke the route immediately and return to the projected local-jet difference-contraction fallback.

Highest cumulative reference is [85]; [86] remains next.
