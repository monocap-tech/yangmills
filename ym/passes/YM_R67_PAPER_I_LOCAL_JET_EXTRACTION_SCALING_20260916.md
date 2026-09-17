# YM-R67 — Paper-I local jet / exact extraction order and canonical L^-2 scaling audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R68` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R66, which split source-scale regular-action memory into:

1. an extended/polymer component with a source-attested one-step geometric scale gain, and
2. a collapsed local component for which polymer diameter gives no suppression.

R67 audits the second component. The questions are:

- does Paper I define `beta_j` by an exact local projection onto the Wilson / `F^2` direction?
- after vacuum and marginal subtraction, what is the first symmetry-allowed local operator order?
- what is the correct one-step object whose norm should gain `L^-2`?

Repeated sources: [7] Bałaban CMP109; [21] Bałaban CMP116; [59] Bałaban CMP119; [68] Curci–Menotti–Paffuti / Symanzik pure-gauge dimension-six control source. No new bibliography item is consumed. Highest remains [84].

Source-access note: the primary CMP109 publication record verifies that Paper I constructs beta functions and defines coupling renormalization by recursive RG equations. The currently available full source-extraction corpus still marks the exact CMP109 one-step fluctuation identity / beta-extraction definition as pending. The public Project Euclid endpoint is presently blocked by its anti-bot layer and Springer exposes only subscription preview text in this environment. Therefore the exact Paper-I projector must remain OPEN rather than reconstructed.

## 1. The collapsed local residue must be treated in the interior bulk chart

CMP119 defines the localized coupling by

`1/g_{j-1}^2(x) = 1/g_j^2(x) + beta_j(g_{j-1}) phi_j(x)`

and the regular part by the scale sum

`E_k(U_k) = sum_j [ E^(j)(Lambda_j,g_{j-1},U_k)`

`                    - E^(j)(Lambda_j,g_{j-1},1)`

`                    - beta_j(g_{j-1}) A(phi_j,U_k) ]`.

On the interior region where `phi_j=1`, the local question is therefore cleanly separated from boundary/collar effects. Define schematically

`K_j^loc := Local[ E^(j)(U) - E^(j)(1) - beta_j A(U) ]`.

Any terms created by derivatives/variation of `phi_j` near the regular-domain boundary belong to the multiscale boundary architecture rather than to the translationally/hypercubically symmetric interior local jet.

Thus R67 restricts the canonical local-operator audit to the interior bulk chart.

## 2. Exact beta extraction remains the only missing marginal-orthogonality source fact

The source-attested subtraction proves

`fresh local contribution -> vacuum-subtracted contribution -> subtract beta_j A`.

What is still not source-custodied is an exact local functional `Loc_A` for which

`beta_j = Loc_A( E^(j) - E^(j)(1) )`

and hence

`Loc_A K_j^loc = 0`.

This is the narrow residue left from R64–R66.

Canonical source classification:

`PrescribedBetaASubtraction = CLOSED / SOURCE-ATTESTED`.

`PaperIBulkWilsonProjectionIdentity = OPEN SOURCE EXTRACTION`.

The primary Paper-I abstract confirms construction of beta-functions and coupling renormalization, but it does not expose the exact projection definition in the accessible preview.

## 3. Field polynomial degree is not the correct irrelevance criterion

A local term cannot be typed as irrelevant merely because it is cubic or quartic in the gauge potential.

The marginal Yang–Mills operator

`tr F^2`

contains quadratic, cubic and quartic gauge-potential vertices.

Conversely, a dimension-six operator can have a quadratic piece, for example a schematic

`A partial^4 A`.

Therefore the required extraction is not

`remove all field monomials up to some degree`,

but rather

`remove all symmetry-allowed local operator directions of canonical dimension <=4`.

This preserves the distinction already established in YM-R20/R21.

## 4. Conditional local-operator classification after exact extraction

Assume the interior local residual is:

- gauge invariant;
- real / reflection even (hence CP-even for the present local classification);
- hypercubic invariant in the bulk;
- vacuum normalized;
- exactly orthogonal to the Wilson / `F^2` marginal direction.

Then in four dimensions the local operator classification through dimension four is exhausted, for the present pure-gauge even sector, by:

1. the dimension-zero vacuum term — already removed;
2. no gauge-boson mass term — excluded by gauge invariance;
3. the CP-even dimension-four `tr F^2` direction — removed by exact Wilson/F^2 extraction;
4. the CP-odd topological density `tr F F~` — excluded by the reflection-even/real sector.

Different local lattice loop representatives of the CP-even dimension-four continuum operator do not create new independent marginal directions: after matching their common `F^2` leading term, their difference begins at the usual higher-dimension lattice-artifact order.

Reference [68] supplies the control classification that the leading pure-gauge lattice artifacts after the dimension-four action are dimension-six / `O(a^2)` corrections.

Hence, conditional on exact bulk Wilson projection,

`K_j^loc = sum_{alpha} c_{6,alpha}^{(j)} O_{6,alpha} + sum_{d>=8,alpha} c_{d,alpha}^{(j)} O_{d,alpha}`

at the level of the local continuum/Symanzik jet.

Classification:

`BulkLocalJetStartsAtDimensionSix = DERIVED conditional on PaperIBulkWilsonProjectionIdentity + source symmetries`.

This is not promoted as a verbatim theorem of CMP109.

## 5. Canonical one-step scale gain

For a local operator of canonical dimension `d` in four dimensions, a block/rescaling step with length factor `L` gives the engineering coefficient multiplier

`L^(4-d)`.

Therefore for every residual operator with `d>=6`,

`|L^(4-d)| <= L^-2`.

At tree level the collapsed local residual consequently obeys the target

`||K_{j+1}^loc|| <= C L^-2 ||K_j^loc||`

in a local operator coefficient norm.

Along a weak interacting trajectory, the correct robust target is not to assert the exact exponent `-2`, but a strict gain of the form

`q_j <= C L^(-2 + epsilon_j)`

with `epsilon_j -> 0` as `g_j -> 0`, or any uniform `q_j<1` in the weak-coupling jurisdiction.

Classification:

`TreeLevelCollapsedJetGain = L^-2 (DERIVATION)`.

`NativeInteractingCollapsedJetGain = OPEN THEOREM`.

## 6. Nonlinear RG forces scale-by-scale re-extraction

A crucial correction to a naive R66 interpretation is that an initially dimension-six residual need not remain exactly orthogonal to `F^2` under nonlinear RG.

Irrelevant local operators can generate a fresh marginal component after integrating another fluctuation shell. That is precisely why a running coupling and repeated local extraction are present.

Therefore the correct dynamical object is not a one-time remainder `K_j^loc` transported unchanged through all later scales.

At every scale one must re-extract the vacuum and marginal components.

Let `J_j` denote the local analytic jet space and let `Loc_j` denote the still-to-be-source-identified projection onto the vacuum plus Wilson direction. Define either

`J_j^irr := ker Loc_j`

or equivalently the quotient

`J_j / span{1,A}`.

If `T_j` is the one-step local RG map, the native irrelevant local map is

`T_hat_j := (1 - Loc_{j+1}) T_j |_{J_j^irr}`.

The theorem actually needed by R66 is

`|| T_hat_j K ||_{j+1} <= q_j ||K||_j`,

with

`q_j <= C L^(-2+epsilon_j) < 1`.

Canonical name:

`RenormalizedLocalJetQuotientContraction`.

This is the precise local analogue of the stable-fiber idea from R63, but because the source already carries the marginal coordinate separately, it is a codimension-one projected contraction rather than a full stable-manifold theorem.

## 7. Why this quotient resolves marginal regeneration

Suppose an irrelevant input `K_j` generates after one RG step

`T_j K_j = delta e_j * 1 + delta beta_j * A + K_{j+1}^irr`.

The vacuum piece is removed by normalization and `delta beta_j` is absorbed into the running coupling coordinate.

Only

`K_{j+1}^irr`

must be contracted.

Thus marginal leakage is not itself an obstruction if the extraction map is exact and the projected complement contracts.

This gives a cleaner architecture than demanding

`D_K T_g = 0`

for arbitrary perturbations. General projection triangularity may fail while the **quotient flow** is still strictly stable after retuning.

R63's full stable graph is therefore further demoted: for the canonical source architecture, the natural theorem is repeated extraction plus quotient contraction.

## 8. Minimal abstract local-jet theorem

The following sufficient theorem is now isolated.

Assume for each weak RG scale `j`:

A. `Loc_j` is a bounded local extraction map onto `span{1,A}`;

B. `Loc_j K_j = 0` for the stored residual local jet;

C. the one-step local RG map can be decomposed as

`T_j K = Loc_{j+1}(T_j K) + (1-Loc_{j+1})(T_j K)`;

D. on the projected complement,

`||(1-Loc_{j+1}) T_j K||_{j+1} <= q_j ||K||_j`

with `q_j <= q < 1`.

Then a source-scale local defect created at scale `j` satisfies after repeated re-extraction

`||K_k^irr||_k <= (product_{r=j}^{k-1} q_r) ||K_j^irr||_j`.

If `q_r <= C L^(-2+epsilon_*) < 1`, then

`||K_k^irr||_k <= q^(k-j) ||K_j^irr||_j`.

This makes the collapsed local contribution summable in source-depth separation and closes the local half of `ScaleSeparatedETransport`.

Classification: DERIVATION / theorem target, not a source theorem.

## 9. Analyticity alone does not supply the L^-2 factor

CMP119/CMP116 provide analytic complex domains and Cauchy-type control of local activities.

Those properties can give bounded derivatives / local Lipschitz estimates, but they do not by themselves imply that the projected local map has operator norm `<1`.

The strict gain comes from **canonical dimension after local subtraction and rescaling**, not from holomorphy alone.

Therefore:

`Analyticity + Cauchy bounds != RenormalizedLocalJetQuotientContraction`.

The remaining source theorem must include the scale normalization / Taylor-order information that turns exact extraction into an `L^-2`-type gain.

## 10. Boundary terms remain outside this closure

The argument above is a bulk local statement on the region where `phi_j=1`.

The `B` sector records boundary / large-field interfaces and is not automatically controlled by the same hypercubic local operator quotient.

Thus even if `RenormalizedLocalJetQuotientContraction` is proved, the full cross-cutoff theorem still needs the separately typed boundary-memory control unless the fixed observable eventually lies in an interior region where those contributions can be shown absent or negligible.

R67 does not absorb the `B` sector into the local-jet theorem.

## 11. Source-recovery result

The exact CMP109 beta-extraction definition was not recovered in this pass.

What can be source-attested is:

- Paper I constructs beta-functions and defines coupling renormalization recursively [7];
- CMP119 uses `beta_j(g_{j-1})` in the scalar coupling recursion and subtracts the same coefficient times the localized gauge action from each regular contribution [59];
- the dedicated external source audit still classifies the exact CMP109 one-step fluctuation identity / defining sections as extraction-pending rather than theorem-fed.

Therefore the project must not replace the missing source definition by the physically natural projection formula without checking the primary text.

Canonical status:

`PaperIBulkWilsonProjectionIdentity = SOURCE BOUNDARY / OPEN`.

No new source number is consumed.

## 12. Determination

R67 establishes:

1. The collapsed local `E` problem should be posed in the interior bulk chart where `phi_j=1`; boundary/collar terms belong to the separate `B` architecture.
2. The exact remaining marginal source question is whether Paper I defines `beta_j` by a bounded local projection onto the Wilson/`F^2` direction.
3. Field polynomial degree is not the relevant classification; the extraction must be by canonical local operator dimension/symmetry.
4. Conditional on exact vacuum + `F^2` projection and the source symmetries, the bulk pure-gauge residual local jet begins at canonical dimension six.
5. Dimension six gives the tree-level coefficient gain `L^-2` per RG step; a native weak-coupling theorem should yield `L^-2+weak correction` or at least a uniform strict contraction.
6. Nonlinear RG can regenerate a marginal term, so the correct dynamic object is not a once-subtracted jet but the scale-by-scale quotient modulo `{1,A}`.
7. The exact theorem needed is `RenormalizedLocalJetQuotientContraction`: after each RG step, re-extract vacuum/marginal components and strictly contract the projected complement.
8. This projected theorem is weaker and more native than the full stable-manifold theorem retained from R63.
9. Analyticity/Cauchy control alone does not prove the scale gain; canonical scaling after exact extraction must be quantified in the native norm.
10. The boundary `B` sector remains a separate cross-cutoff memory obligation.

Canonical state:

`PaperIBulkWilsonProjectionIdentity = OPEN SOURCE EXTRACTION`.

`BulkLocalJetStartsAtDimensionSix = CONDITIONALLY DERIVED`.

`TreeLevelCollapsedJetGain = L^-2 DERIVED`.

`RenormalizedLocalJetQuotientContraction = LIVE NATIVE THEOREM OBLIGATION`.

`CollapsedLocalEJetIrrelevance = REDUCED TO PaperIBulkWilsonProjectionIdentity + RenormalizedLocalJetQuotientContraction`.

`ExtendedEGeometricTransport = retained from R66, one-step source mechanism closed / repeated dictionary open`.

`NativeComplementaryDifferenceContraction = fallback, no longer default local attack`.

## Negative results / guardrails

- Do not identify `beta_j` with an exact projection functional until the Paper-I definition is recovered.
- Do not use polynomial degree in the gauge potential as a synonym for canonical irrelevance.
- Do not assume a once-dimension-six operator can never regenerate `F^2`; re-extraction is required at every step.
- Do not infer `L^-2` from analyticity or exponential polymer locality alone.
- Do not apply the bulk hypercubic local classification to boundary/collar `B` terms without a separate theorem.
- Do not call the quotient contraction a source theorem before its native norm estimate is extracted/proved.
- Do not infer continuum Yang–Mills construction or a mass gap from local-jet contraction alone.

## Next frontier — YM-R68

`YM-R68 — projected local-jet norm / one-step quotient contraction audit.`

Tasks:

1. inspect CMP109/CMP116 local rescaling and Taylor/Cauchy estimates for an explicit scale factor after vacuum/Wilson extraction;
2. formulate the weakest source-compatible norm on `J_j / span{1,A}` in which the canonical `L^-2` gain can be proved;
3. determine whether interaction corrections remain uniformly below the two units of canonical irrelevance throughout the weak-coupling window;
4. keep boundary `B` memory and cross-depth marginal-tail coherence separate;
5. if no native quotient estimate is recoverable, return to the two-trajectory complementary contraction route with the local quotient as one block.

Highest cumulative reference remains [84]; [85] remains next.
