# YM-R16 — exact-pushforward custody

Date: 2026-09-15
Status: COMPLETE
Claim discipline: unproved research program; no Yang–Mills existence or continuum mass-gap theorem claimed.
Prior canonical cursor: `YM-R16`, unconsumed.
Next cursor: `YM-R17`.

## Target

Audit one Bałaban non-Abelian RG step for the reflection-positivity custody question isolated in YM-R15:

1. whether the exact nonlinear block average can satisfy reflection covariance and positive-half-space support;
2. whether later gauge/background/cluster/R manipulations are exact reparametrizations or genuine approximations;
3. where the first remaining RP obligation actually sits.

## Source-attested facts

### [35] Bałaban, *Averaging operations for lattice gauge theories* (CMP 98, 1985)

Bałaban studies averaging operations for lattice gauge fields and gauge transformations and characterizes classes of configurations on which those operations are regular/analytic. The averaging map is nonlinear and gauge-covariant. The primary paper is the controlling source for the exact map and its regularity domain.

### [7], [21] — 4d small-field RG and cluster expansion

Bałaban's 4d Part I explicitly works in the small-field approximation and constructs localized effective actions, the beta function and recursive coupling renormalization. Part II exponentiates the fluctuation-field cluster expansion and proves that its terms satisfy the inductive assumptions required for further RG steps.

### [22], [31] — large-field R-operation

The large-field papers add the machinery required to control the field regions omitted from the small-field chart. Their role is not a numerical truncation but a constructive decomposition/localization/bound on the large-field contributions.

### [59] Bałaban, *Convergent renormalization expansions for lattice gauge theories* (CMP 119, 1988)

The abstract states that the paper introduces an inductive description of the **complete effective densities including large field domains** and proves that the renormalization transformations preserve the form of those densities. This is the key source for distinguishing the complete program from the earlier small-field-only approximation.

### [40], [41]

The background minimizer and background-field propagator are nonlocal/quasi-local analytic coordinates used to control the exact coarse density. Their nonlocality does not by itself imply loss of reflection positivity of the underlying measure.

### [42] Dimock exposition

In the abelian/expository implementation, one RG step is written with a delta constraint `delta(A_1-QA_0)` and partial axial gauge; the integral is preserved and iterated delta constraints compose exactly. This is used only as an explanatory model for the algebraic distinction between the exact coarse measure and its later analytic representation, not as a substitute for a missing 4d non-Abelian theorem.

## Reflection-covariance derivation

Let `Theta` be a lattice time reflection and let `Q` be the exact nonlinear block map. If the block partition and every path/reference object entering the definition of `Q` are chosen `Theta`-equivariantly, then on any regularity domain where the nonlinear group operations use a reflection-compatible logarithm branch one expects

`Q Theta = Theta Q`.

For a reflection plane placed on block boundaries (with odd blocking factor, as in the standard block geometry), a coarse bond strictly in the positive half-space can be represented using only fine links in positive blocks. Under that geometric condition,

`Q^*(A'_+) subset A_+`.

These two identities imply the standard pushforward lemma:

if `mu` is reflection positive and `mu' = Q_* mu`, then `mu'` is reflection positive.

This is a DERIVATION conditional on the exact Bałaban map satisfying the stated support/branch hypotheses. It is **not** installed as a theorem extracted from [35].

## Important limitation: regularity domain

[35] is explicitly concerned with classes of gauge configurations on which the averaging operations are regular/analytic. The current source extraction does not yet justify promoting the small-field analytic formula to a globally reflection-equivariant deterministic map on every large-field configuration.

Therefore YM-R16 does **not** close global RP preservation for the complete 4d flow.

The remaining local question is whether the exact nonlinear averaging operation has a globally measurable/reflection-equivariant extension compatible with the large-field decomposition, or whether the complete RG should instead be formulated as an RP-preserving blocking kernel rather than a single deterministic map.

## Exactness classification

| operation | status in constructive architecture | RP consequence |
|---|---|---|
| coarse-field delta/blocking constraint | exact definition of RG/pushforward or constrained integration | this is the operation whose reflection support matters directly |
| partial axial-gauge insertion | exact gauge-fixing identity when normalization/Jacobian is retained | need not be RP term-by-term if total integral is unchanged |
| Landau/background change of coordinates | exact analytic change on its regular domain with Jacobian/remainder retained | non-half-space-local coordinates do not by themselves destroy RP |
| background/Taylor expansion | exact only when nonlinear remainder is retained | truncating would be a new approximation; constructive treatment keeps controlled remainder |
| Part-I small-field restriction | genuinely restricted scope, not the complete measure | cannot alone custody RP of the full theory |
| small/large-field decomposition | exact partition/decomposition in complete-density program | positivity need only hold for recombined measure |
| localization / convergent cluster expansion | exact convergent reorganization on its domain | individual polymer terms need not be RP |
| R-operation | constructive localization/exponentiation/reorganization of large-field terms | no separate termwise RP theorem required if recombination is exact |
| CMP 119 complete density | restores full large-field-aware inductive density and preserves its form under RG | removes the hypothesis that the only RP threat is an uncontrolled approximation |

## Negative result

The search for a first **approximation error** that breaks reflection positivity did not find one in the complete Bałaban architecture. Treating the 1987 small-field paper as the whole theory would be incorrect; the later complete-density/large-field papers exist precisely to reinsert the omitted sectors.

## Bounded determination

YM-R16 changes the live interface from

`RP measure -> exact Q pushforward -> maybe broken by later nonlocal analysis`

to

`RP measure -> GLOBAL Q/KERNEL CUSTODY -> exact complete-density analysis`.

The later background, propagator, cluster, localization and R machinery can be nonlocal or non-manifestly positive without destroying RP provided they are exact representations of the same blocked measure.

The first unresolved RP obligation is therefore the **global blocking operation itself**:

- reflection covariance,
- positive-half-space support,
- gauge covariance,
- global measurability/definition across large-field sectors,
- and compatibility with the exact complete-density transformation.

## Next frontier — YM-R17

**Global averaging / branch-domain audit.**

Determine whether the Bałaban nonlinear average admits a globally defined measurable, gauge-covariant, reflection-equivariant, block-local extension `Qhat` satisfying

`Qhat Theta = Theta Qhat`,

`Qhat^*(A'_+) subset A_+`,

and agreeing with the analytic Bałaban average on the regular small-field domain.

If yes, reflection positivity of every exact coarse pushforward follows essentially formally. If no, identify the minimal RP-preserving stochastic/blocking kernel replacing deterministic `Q`.

## References used

Existing: [7], [21], [22], [31], [35], [40], [41], [42].
New: [59].
