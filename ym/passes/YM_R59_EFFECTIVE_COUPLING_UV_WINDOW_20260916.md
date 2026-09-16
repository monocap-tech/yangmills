# YM-R59 — effective-coupling interval / UV-window persistence audit

Date: 2026-09-16
Status: COMPLETE
Next cursor: `YM-R60` (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills existence or mass-gap claim.

## Target

Continue from YM-R58, which closed the CMP122-II post-R E/R/B return map conditional on the source hypothesis that the effective coupling sequence remains in a sufficiently small interval `(0,gamma]`.

Audit whether that coupling-window hypothesis is actually discharged by the published CMP109/CMP119/CMP122 chain, and separate native coupling-flow control from the RP modification's finite coupling-coordinate shift.

Repeated sources: [7] Bałaban CMP109 (1987); [59] Bałaban CMP119 (1988); [31] Bałaban CMP122-II (1989).
No new bibliography item is consumed.

## 1. Native coupling recursion is source-attested

CMP119 Eq. (2.24) defines the localized running coupling recursively in inverse-square coordinates:

`1 / g_{j-1}^2(x) = 1 / g_j^2(x) + beta_j(g_{j-1}) phi_j(x)`,

with `phi_j` a smooth cutoff supported in the scale-j regular domain and equal to one on the indicated interior region.

This is the complete-density version of the coupling recursion already constructed in Paper I. It confirms the structural point from YM-R21: the natural marginal coordinate is `g^{-2}`, not `g` itself.

The recursion is therefore not missing. What is at issue is whether its solutions remain inside the small-coupling jurisdiction required by the complete-density induction.

## 2. CMP119 Theorem 1 is conditional on coupling inequalities

CMP119 Theorem 1 states, in source-normalized form:

`({g_k} satisfies Paper-I RG equations (0.18),(0.20) and inequalities (1.0.33))`

`=> rho_k = RT^k(rho_0) satisfies all CMP119 inductive assumptions.`

Thus the theorem is an induction-preservation theorem for a coupling trajectory satisfying the source coupling conditions. It does not, by its logical form alone, prove that every solution of the recursion automatically satisfies the required inequalities for arbitrarily many steps.

The exact printed list of inequalities (1.0.33) has not yet been transcribed into the present project corpus. That is a source-extraction/custody item. But the more important logical point is already source-attested: the coupling conditions are hypotheses of the complete-density induction.

## 3. CMP122-II does not remove the coupling-window hypothesis

CMP122-II Theorem 1 states that if the effective coupling constants are contained in `(0,gamma]`, for sufficiently small positive `gamma`, then the effective densities have the CMP119 Sect. 2 form and satisfy all its conditions and bounds.

Crucially, the source explicitly says this small-coupling assumption is retained because the second-order perturbative theorem intended to remove it was not published in that paper.

Therefore the published CMP119/CMP122 large-field chain does **not** supply an unconditional theorem of the form

`g_0 sufficiently small => g_k in (0,gamma] for the entire desired trajectory`

without additional coupling-flow input.

This is a genuine theorem boundary in the published source architecture, not a missing polymer estimate.

## 4. What can be said for a finite prescribed window

For a fixed finite number of RG steps, persistence inside a small interval is an elementary consequence once one has uniform local bounds on the beta increments and chooses the initial/bare coupling with sufficient margin.

Schematically, on a region where `phi_j=1`,

`1/g_j^2 = 1/g_{j-1}^2 - beta_j(g_{j-1})`.

If, on a prescribed weak-coupling interval, `|beta_j(g)| <= B` uniformly, then over `N` steps

`1/g_N^2 >= 1/g_0^2 - N B`.

Hence the finite-window condition `g_j <= gamma` is ensured by the sufficient margin

`1/g_0^2 >= gamma^{-2} + N B`.

This is an elementary conditional derivation, not promoted as Bałaban's exact inequality (1.0.33), because the exact source beta bounds and inequalities have not yet been extracted.

It shows why the problem is not finite-step existence but **uniform/tuned control of the marginal trajectory as the UV depth changes**.

## 5. Marginal flow: do not demand geometric decay of g_k

The four-dimensional gauge coupling is marginal. The inverse-square recursion produces logarithmic/asymptotic-freedom-type running rather than a geometric law `g_k <= C r^k`.

Therefore the large-field/localized remainder bounds

`g_j^kappa0 exp(-kappa d_j(X))`

and

`exp(-p_0(g_k)) exp(-kappa d_k(X))`

must not be reinterpreted as evidence that the coupling itself contracts geometrically per RG step.

The geometric contraction resource belongs to irrelevant/polymer geometry; the coupling is a separate marginal coordinate.

## 6. RP finite coupling shift is not a new window theorem

YM-R21 identified the RP soft-kernel marginal correction as an ordinary finite redefinition in the inverse-square coordinate:

`g_RP^{-2} = g^{-2} + delta c(g)`.

Equivalently, for small `g`,

`g_RP = g + O(g^3)`.

Suppose on the relevant weak-coupling interval

`|g_RP - g| <= C_RP g^3`.

Then for `g <= gamma/2` and `C_RP gamma^2 <= 1`,

`0 < g_RP <= gamma/2 + C_RP gamma^3/8 < gamma`.

So a finite analytic scheme shift only shrinks the native small-coupling collar. It does not require a new asymptotic-freedom theorem.

Hence:

`native coupling-window persistence => RP-modified coupling-window persistence after a fixed collar shrink`.

The exact numerical RP shift remains optional scheme/Lambda-calibration data.

## 7. Source-level determination

R59 establishes:

1. The effective coupling recursion is explicitly present in CMP119/Paper I in inverse-square coordinates.
2. CMP119 Theorem 1 preserves the complete-density induction only for trajectories satisfying the source RG coupling equations and inequalities.
3. CMP122-II Theorem 1 retains the explicit small-coupling interval assumption.
4. CMP122-II itself states that the stronger perturbative theorem intended to remove that assumption is not published there.
5. Therefore published complete-density/R-operation closure is conditional on coupling-window persistence.
6. Finite prescribed RG windows can be kept weak by ordinary margin/tuning once uniform beta bounds are supplied; this does not solve the uniform UV-depth problem.
7. The RP modification contributes only a finite `O(g^3)` scheme displacement and can be absorbed by shrinking the weak-coupling collar.

Canonical classification:

`LargeFieldROperationReturnMap = CLOSED conditional on CouplingWindowPersistence`.

`CouplingWindowPersistence = LIVE NATIVE THEOREM OBLIGATION / PUBLISHED-SOURCE BOUNDARY`.

This is the first point after the small-field and large-field local machinery where the traversal encounters a genuinely global marginal-flow issue rather than a localization/resummation issue.

## Negative results / guardrails

- Do not claim CMP122-II proves the small-coupling interval from the bare coupling alone.
- Do not treat CMP119 Eq. (2.24) as itself a proof of trajectory persistence.
- Do not invent the exact content of Paper-I inequalities (1.0.33); extract them next.
- Do not impose geometric decay on the four-dimensional marginal coupling.
- Do not confuse finite RP scheme calibration with native asymptotic-freedom/window control.
- Do not infer continuum existence or a mass gap from conditional ultraviolet stability.

## Next frontier — YM-R60

`YM-R60 — Paper-I beta-function / coupling-inequality extraction and UV tuning audit.`

Tasks:

1. extract Paper-I equations (0.18), (0.20), and inequalities (1.0.33) exactly enough to identify the native coupling-window criterion;
2. recover the source bounds/sign/leading behavior of `beta_j(g)` used in the recursion;
3. determine whether Paper I proves a uniform finite-N tuning theorem and what depends on N;
4. search the published Balaban spine for any later theorem actually removing the CMP122-II small-coupling assumption;
5. if no published theorem exists, type the residue precisely as a missing global marginal-flow bridge rather than a local RG-density defect.

Highest cumulative reference remains [80]; [81] remains next.