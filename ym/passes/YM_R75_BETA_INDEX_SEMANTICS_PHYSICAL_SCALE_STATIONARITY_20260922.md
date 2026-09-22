# YM-R75 — beta-index semantics / physical-scale stationarity audit

Date: 2026-09-22
Status: COMPLETE
Next cursor: YM-R76 (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R74, which reduced the canonical scalar cross-cutoff problem to one source question:

What does the index j in beta_j(g) actually parameterize?

If it is only a blocking/physical-scale label, then R70 physical-scale alignment should make the depth-N and depth-(N+1) beta families shift-covariant. If it hides absolute regulator depth or unrelated history, a genuine scalar mismatch can remain.

Repeated sources: [7] Bałaban CMP109; [59] Bałaban CMP119; [85] Eriksson traceability manuscript as a secondary locator only.

No new bibliography item is consumed. Highest remains [85].

## 1. The secondary equation-level locator makes the intended index semantics explicit

Reference [85] defines the microscopic spacing by

eta = L^(-N)

and the blocked spacing by

eta_k := L^k eta,

explicitly calling k the blocking level.

The same locator states that beta_j(g) denotes the scale-dependent coefficients in Bałaban's small-field coupling recursion.

Thus at the equation-traceability level the index is typed as a blocking/source-scale label, not as the total ultraviolet depth N.

Canonical locator-level classification:

BetaIndexSemanticType = BLOCKING LEVEL / SOURCE SCALE.

This is not yet promoted to primary-source custody because [85] remains a secondary conditional traceability manuscript.

## 2. The beta coefficient is traced to the vacuum-polarization tensor at the new scale

The same locator traces CMP109 Eq. (5.42) in the form

beta_(j+1)(g_j)
= - [ partial_(p_mu) partial_(p_nu) PiHat_(j+1,mu nu) ]_(p=0)

for mu != nu, equivalently through the second moment of the position-space vacuum-polarization tensor.

The key type information is more important than the exact sign convention:

beta born at scale j+1 = local marginal coefficient extracted from Pi_(j+1).

Hence the index on beta is inherited from the scale of the fresh vacuum-polarization contribution.

The source-labelled regular contribution, vacuum polarization, and beta extraction are therefore aligned as:

fresh scale-(j+1) fluctuation contribution
-> Pi_(j+1)
-> beta_(j+1)(g_j)
-> Wilson/F^2 subtraction at scale j+1.

This sharply refines R74's generic {j,g} typing.

## 3. Absolute cutoff depth N enters the locator through eta, not as a separate beta argument

In [85]'s notation the total ultraviolet depth N appears through

eta = L^(-N).

The blocking index then produces

eta_k = L^k eta.

No separate argument beta_(N,k)(g;N) is introduced.

Thus the secondary traced architecture is consistent with

beta_k^(N)(g) = mathfrak beta(eta_k,g)

or with the stronger autonomous form

beta_k^(N)(g)=beta(g).

It is not presented as an arbitrary absolute-depth family.

Classification:

NoSeparateAbsoluteDepthArgument = SECONDARY-LOCATOR EVIDENCE.

This does not yet prove exact primary stationarity.

## 4. R70 now aligns the actual beta-extraction scales exactly

R70 proved

a_(N+1,j+1)=a_(N,j)

with

a_(N,j)=L^j eta_N.

Therefore the scale-j vacuum polarization in the depth-N construction and the scale-(j+1) vacuum polarization in the depth-(N+1) construction are formed at the same physical lattice spacing.

The beta-map comparison can therefore be pushed one level below the scalar coefficient:

beta shift covariance

is implied by

vacuum-polarization extraction covariance at aligned physical scales.

This gives the new canonical object:

OneStepVacuumPolarizationRescalingCovariance.

## 5. Exact theorem reduction

Let Pi_(N,j)[g] denote the canonical one-step vacuum-polarization tensor whose local quadratic coefficient defines the beta increment at depth N, blocking scale j.

Let Loc_F2 be the source extraction functional represented schematically by the zero-momentum second derivative in the traced Eq. (5.42).

Then

B_(N,j)(g) = Loc_F2(Pi_(N,j)[g]).

If aligned physical scales satisfy

Pi_(N+1,j+1)[g] = ScaleIdentify(Pi_(N,j)[g])

and Loc_F2 is invariant under that canonical scale identification, then

B_(N+1,j+1)(g)=B_(N,j)(g).

Hence:

OneStepVacuumPolarizationRescalingCovariance
=> NativeBetaMapShiftCovariance.

Combining with R71:

OneStepVacuumPolarizationRescalingCovariance
+ EndpointCondition
+ BackwardScalarUniqueness
=> CrossDepthMarginalTailCoherence.

Classification: DERIVATION.

The scalar cocycle problem is now reduced to equality of one fresh local one-step object rather than equality of two entire cutoff histories.

## 6. Why this is a much stronger structural simplification

Before R75 the index j might have hidden arbitrary history.

The traced Eq. (5.42) instead ties it to the scale-labelled vacuum polarization of the fresh one-step fluctuation contribution.

This removes several hypothetical hidden-data channels:

- total UV depth is not an explicit extraction argument;
- inherited E/R/B/V history is not an explicit extraction argument;
- domain and large-field history are not displayed in the coefficient;
- position localization remains external through phi_j;
- the scale label is inherited from the fresh source contribution itself.

Thus any remaining absolute-depth dependence would have to enter through failure of the one-step local fluctuation/vacuum-polarization problem to be covariant under the canonical rescaling between aligned lattices.

That is a much narrower source theorem.

## 7. One-step RG architecture supports, but does not primary-prove, stationarity

CMP109's peer-reviewed abstract states that the localized effective actions are constructed by cluster expansions in one-step renormalization transformations, and that beta-functions and coupling renormalization are then constructed recursively [7].

This is structurally consistent with a repeated local one-step extraction after blocking/rescaling.

The secondary locator likewise defines the RG geometry through the blocked spacings eta_k=L^k eta and traces the beta coefficient to the scale-k vacuum polarization.

However, the project still lacks a directly extracted primary theorem saying:

the scale-k vacuum-polarization functional, after canonical rescaling to the aligned lattice, is independent of the total initial depth N.

Therefore:

PrimaryOneStepVacuumPolarizationStationarity = OPEN SOURCE GATE.

R75 does not turn structural consistency into theorem custody.

## 8. The beta-index semantics question is therefore substantially answered

R74 left three possibilities:

A. pure step label;
B. physical-scale label;
C. absolute-depth/history label.

The available equation-level locator explicitly supports A/B:

- k is a blocking level;
- eta_k=L^k eta;
- beta_(j+1) is extracted from Pi_(j+1).

There is no explicit source-locator support for C.

Hence:

BetaIndexSemantics = BLOCKING/SOURCE-SCALE LABEL

at the secondary equation-traceability level.

The residual open issue is no longer semantic classification. It is primary verification of scale-stationarity/covariance of the one-step vacuum-polarization extraction.

Canonical retyping:

BetaIndexSemantics = LOCATOR-LEVEL CLOSED / PRIMARY CONFIRMATION PENDING.

BetaPhysicalScaleStationarity = LIVE PRIMARY THEOREM OBLIGATION.

## 9. Exact stationarity is again stronger than necessary

If the aligned vacuum polarizations are not exactly equal but obey

||Pi_(N+1,j+1)-Pi_(N,j)||_jet <= epsilon_(N,j)

and the F^2 extraction functional is bounded,

|Loc_F2(Pi)-Loc_F2(Pi')| <= C_Loc ||Pi-Pi'||_jet,

then

|delta beta_(N,j)| <= C_Loc epsilon_(N,j).

Thus R72's summable mismatch route becomes:

SummableVacuumPolarizationShiftDefect
+ BoundedF2Extraction
=> SummableBetaMapShiftDefect
=> SummableMarginalTailMismatch.

This is an ABSTRACT DERIVATION.

If a source-depth positive-alpha estimate controls the difference of the aligned one-step polarization tensors, the same geometric factor would be sufficient.

No such primary theorem is claimed here.

## 10. Relation to the regular-sector Eq. (0.29) gate

The beta and regular-residual source questions are now adjacent pieces of the same local Taylor/Ward construction:

E^(j)
-> Taylor/Ward decomposition
-> Pi_j
-> beta_j A + V^(j).

The beta branch asks for scale covariance of the marginal projection.

The regular branch asks for the positive-alpha bound on the complementary residual V^(j).

Thus the two remaining primary gates are naturally paired:

1. PrimaryVacuumPolarizationScaleCovariance;
2. PrimaryEq029PositiveAlphaBound.

If both hold in the needed uniform form, the entire canonical small-field E/marginal cross-cutoff defect is summable or exactly coherent without invoking the generic stable-fiber theorem.

## 11. Determination

R75 establishes:

1. Secondary equation-level traceability explicitly defines eta_k=L^k eta and calls k the blocking level.
2. The same locator types beta_j as scale-dependent coefficients and traces beta_(j+1)(g_j) to the scale-(j+1) vacuum-polarization tensor through CMP109 Eq. (5.42).
3. Therefore the intended index semantics is blocking/source scale, not a separately displayed total UV-depth variable.
4. Total cutoff depth enters the locator through eta=L^-N; the scale-k extraction lives at eta_k=L^k eta.
5. R70 exact physical-scale alignment consequently reduces beta-map shift covariance to rescaling covariance/stationarity of the one-step vacuum-polarization extraction.
6. The peer-reviewed CMP109 abstract supports the repeated one-step RG architecture but does not by itself prove this exact stationarity theorem.
7. BetaIndexSemantics is therefore closed at the secondary traceability level but awaits direct primary confirmation.
8. The remaining scalar theorem is PrimaryOneStepVacuumPolarizationStationarity, with summable vacuum-polarization mismatch as the weaker fallback.
9. The beta stationarity gate and the Eq. (0.29) positive-alpha residual gate are two outputs of the same local Taylor/Ward/vacuum-polarization decomposition.

Canonical state:

BetaIndexSemantics = BLOCKING/SOURCE-SCALE LABEL at secondary traceability level.

NoSeparateAbsoluteDepthArgument = SUPPORTED at locator level.

OneStepVacuumPolarizationRescalingCovariance => NativeBetaMapShiftCovariance = DERIVED.

PrimaryOneStepVacuumPolarizationStationarity = LIVE SOURCE GATE.

SummableVacuumPolarizationShiftDefect = LIVE FALLBACK.

PrimaryEq029PositiveAlphaBound = independently OPEN.

GeneralStableFiberTheorem = retained only as fallback.

## Negative results / guardrails

- Do not promote [85]'s equation transcription to primary Bałaban theorem custody.
- Do not infer exact stationarity merely because k is called a blocking level.
- Do not treat total UV depth N as a beta argument when the traced notation introduces it only through the microscopic spacing eta.
- Do not conflate equality of physical lattice spacing with equality of the one-step fluctuation/vacuum-polarization functional without the rescaling-covariance theorem.
- Do not infer a continuum theory or mass gap from small-field scalar coherence.

## Next frontier — YM-R76

YM-R76 — one-step vacuum-polarization rescaling covariance / paired marginal-residual audit.

Tasks:

1. reconstruct the scale-j vacuum-polarization object from the traced CMP109 equations (5.37), (5.42) and the one-step RG geometry;
2. determine whether its definition is dimensionless after canonical lattice rescaling;
3. identify every scale-dependent input to Pi_j and test invariance under (N,j)->(N+1,j+1);
4. pair the marginal projection with the complementary V^(j) Eq. (0.29) residue so the entire local Taylor/Ward split is audited at once;
5. retain summable polarization mismatch and the generic stable-fiber theorem as fallbacks.

Highest cumulative reference remains [85]; [86] remains next.
