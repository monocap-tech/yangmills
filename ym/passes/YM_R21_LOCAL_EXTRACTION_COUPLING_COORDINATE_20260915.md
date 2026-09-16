# YM-R21 — local extraction / coupling-coordinate audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: `YM-R22` (unconsumed)
Claim status: research reduction; no Yang–Mills existence or mass-gap proof claimed.

## Target

Determine the actual marginal coordinate used by Bałaban in the 4d weak-field RG, place the reflection-positive soft-kernel perturbation in that same coordinate system, and separate the coupling shift from the genuinely irrelevant remainder.

## 1. Source-attested Bałaban coordinate

Bałaban CMP 109 (1987) studies four-dimensional pure gauge theory in the small-field region, constructs localized effective actions, constructs beta functions, and defines coupling renormalization by recursive RG equations. The principal local gauge term is the lattice Wilson action `A(U)` with coefficient `g_k^{-2}`. An equation-level secondary audit of the primary paper reports the effective-action leading term as `g_k^{-2} A(U_k)` (CMP 109 eq. (1.3)) and the coupling recursion in the inverse-square coordinate (CMP 109 eq. (0.20)). Because direct PDF extraction was blocked in the present tool environment, equation numbers are retained as a source-targeting note rather than promoted beyond what has been independently verified from the primary metadata/abstract.

Thus the marginal coordinate relevant to this project is not an abstract continuum `∫ tr F^2` coefficient imposed from outside. It is the coefficient of the canonical lattice gauge action already built into Bałaban's inductive representation:

`S_k(U_k) = g_k^{-2} A(U_k) + E_k(U_k)`

with the localized remainder carried separately.

## 2. Local extraction for the soft kernel

Write the one-step soft-kernel contribution after the Gaussian principal part has been separated as

`R_soft(U) = local part + polymer/localized remainder`.

The appropriate marginal extraction is therefore

`Loc_4 R_soft = δc_k A(U_k) + δE_k |Λ_k|`,

where `δE_k` is a vacuum-energy shift and `δc_k` is the coefficient in the same Wilson-action coordinate as `g_k^{-2}`. Define

`R_soft^irr = R_soft - Loc_4 R_soft`.

This is the correct lattice version of the R20 decomposition

`R_soft = δc tr F^2 + R_irr + vacuum`.

## 3. Why there is no tree-level coupling displacement

R19 found for the quadratic soft-hard difference

`E_a(p) = -a^{-1} Δ_∞(p)^2 (I + a^{-1}Δ_∞(p))^{-1}`

and hence

`E_a(p) = O(p^4)`

at small momentum. The Wilson/Yang–Mills principal quadratic term is `O(p^2)`. Therefore the softening defect has zero tree-level projection onto the marginal kinetic/Wilson direction:

`Loc_4 E_a = 0` at the classical quadratic level.

This is stronger than merely saying `E_a` is canonically dimension six: it says the kernel modification does not change the principal coupling coordinate before fluctuations are integrated.

## 4. Expected form of the marginal shift after integration

Quantum/fluctuation integration can regenerate a local `A(U_k)` component from the cubic and quartic soft-kernel vertices. In the inverse-square coordinate the resulting local extraction should have the form

`g_{k,new}^{-2} = g_k^{-2} + δc_k(g_k,a)`.

If `δc_k(g,a)` is analytic at `g=0` with a finite constant term,

`δc_k(g,a) = c_0(a) + c_1(a) g^2 + ...`,

then in the ordinary coupling coordinate

`g_new = g - (1/2)c_0(a) g^3 + O(g^5)`.

Thus a finite change of the `g^{-2}` coefficient is exactly an analytic finite coupling redefinition. It can alter nonuniversal higher beta-function data but not the universal asymptotic-freedom coefficients under the usual scheme-equivalence hypotheses.

## 5. Uniqueness of the marginal even gauge coordinate

For a local, gauge-invariant, hypercubic/reflection-even pure-gauge functional in four dimensions, the CP-even dimension-four direction is represented by `tr F^2`, whose lattice representative in this inductive chart is `A(U)`. The CP-odd topological density is excluded by the real/reflection-even blocking kernel. Gauge invariance excludes a mass term. Other local loop representatives differ at small lattice spacing by the same dimension-four continuum operator plus dimension-six-and-higher corrections.

Therefore the soft kernel does not require a new marginal coordinate: after vacuum normalization, its only allowed marginal local projection is the existing Wilson-action coefficient.

## 6. What remains genuinely irrelevant

After the Wilson-action extraction,

`R_soft^irr = (1-Loc_4)R_soft`

has no vacuum term and no dimension-four CP-even pure-gauge component. Its local Taylor expansion therefore begins in the dimension-six operator sector, plus exponentially/localized polymer tails. Canonical scaling gives the expected tree-level gain `L^{-2}` for the local dimension-six jet.

This does not yet establish the Bałaban norm estimate. The remaining theorem is quantitative:

`||(1-Loc_4) R_soft||_{Bal,k+1} <= C L^{-2+O(g_k^2)} ||R_soft||_{analytic/local,k}`

with constants uniform over the UV window, together with the corresponding localized/polymer support bounds.

## 7. Crucial distinction: extraction versus truncation

The exact reflection-positive blocked measure must not be replaced by the truncated action

`g_new^{-2} A + dimension-six terms`.

`Loc_4` is only an analytic bookkeeping/extraction map used to define the running coupling and prove contraction of the complementary activity. Reflection positivity remains custodied by the exact half-space-factorized kernel from R18.

## 8. Bounded determination

R21 resolves the coupling-coordinate ambiguity:

1. Bałaban's running coordinate is the coefficient `g_k^{-2}` multiplying the lattice Wilson action `A(U_k)`.
2. The soft kernel has no tree-level projection onto that marginal direction because its quadratic defect starts at `p^4`.
3. Fluctuations may generate a finite local shift `δc_k A(U_k)`; this is an ordinary coupling-scheme redefinition in the inverse-square coordinate.
4. After subtracting vacuum energy and the `A(U)` projection, the local soft-kernel jet begins at canonical dimension six.
5. The unresolved problem is not identifying the marginal coordinate but proving the complementary localized activity satisfies Bałaban's precise analytic/polymer norm gains.

## Next frontier — YM-R22

`YM-R22: analytic-jet / polymer-norm closure.`

Extract the actual analytic field domain and localized activity norms used in Bałaban Parts I–II, then prove or falsify that the reflection-adapted soft-kernel remainder satisfies them after the `A(U)` marginal extraction. In particular track Cauchy radii, support diameter, derivatives in the background field, and the scale factor corresponding to the dimension-six gain.

## Source custody

Repeated sources reused: [7] Bałaban CMP 109 (1987); [21] Bałaban CMP 116 (1988); [11] Lüscher–Weisz positivity caution; [51] scheme/Lambda control; [68] Symanzik dimension-six classification source.

No new reference ID assigned in R21. Highest remains [68].
