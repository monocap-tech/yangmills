# YM-R17 — global averaging / branch-domain audit

Date: 2026-09-15
Status: COMPLETE
Next cursor: YM-R18 (unconsumed)
Claim status: UNPROVED_RESEARCH_PROGRAM

## Target

Determine whether the non-Abelian block average used in the Bałaban program can be treated as a globally defined deterministic map with all of the properties needed for reflection-positive RG:

1. gauge covariance;
2. reflection covariance;
3. positive-half-space support;
4. global definition/measurability through large-field sectors;
5. compatibility with the regular small-field analytic chart.

## Source-attested facts

### [35] Bałaban CMP 98 (1985)

Bałaban's averaging paper studies averaging operations for lattice gauge fields and gauge transformations and explicitly emphasizes characterization of classes of field configurations on which the operations are regular/analytic. This is evidence for a distinguished regular chart, not by itself a global reflection-positivity theorem.

### [60] Federbush (1987)

Federbush describes a block-spin transformation built from finitely many path holonomies associated with a coarse edge. He states that in small-field regions the transformation uses 'Balaban averaging' (with a definition differing slightly from Bałaban's original one), and that a suitable continuous extension is used in large-field regions. In the small-field regime, the coarse group element is characterized as the minimizer of the sum of squared invariant distances to the path holonomies. The construction therefore exhibits an explicit small-field Karcher/Frechet-type mean plus a global continuous extension, but it does not identify that extension with Bałaban's original CMP 98 map.

### [62] Bałaban CMP 99 (1985)

Bałaban's regular-configuration paper works with gauge-invariant regularity conditions and proves smallness/regularity after suitable gauge fixing. This confirms that the analytic machinery is intentionally charted on a regular sector.

## Small-field derivation

Let the path holonomies entering one coarse bond be g_1,...,g_n in a compact Lie group G, and let d be the distance from a bi-invariant metric. On a sufficiently small geodesically convex neighborhood, define q(g_1,...,g_n) as the unique minimizer of

    Phi(h) = sum_i d(h,g_i)^2.

Then uniqueness plus bi-invariance gives the desired covariance properties on the regular chart:

- common left/right endpoint gauge action:

    q(a g_1 b^{-1},...,a g_n b^{-1}) = a q(g_1,...,g_n) b^{-1};

- inversion/orientation reversal:

    q(g_1^{-1},...,g_n^{-1}) = q(g_1,...,g_n)^{-1};

- conjugation covariance as a special case.

If the block/path geometry is chosen equivariantly under the Euclidean time reflection Theta, these identities imply conditionally on the regular chart

    Q Theta = Theta Q.

If the reflection plane is aligned with block boundaries and every coarse bond in the positive algebra is built only from fine paths lying in the positive half-space, then also

    Q^* A'_+ subset A_+.

Hence the regular-chart reflection-positive pushforward is structurally unobstructed.

## Global extension: what is and is not established

Federbush supplies evidence that a continuous extension to large fields can be chosen for a closely related block-spin map. However:

1. his definition is explicitly stated to differ slightly from Bałaban's original averaging;
2. continuity alone does not imply gauge covariance, reflection covariance, or preservation of all path/lattice symmetries;
3. the accessible Bałaban CMP 98 record does not install a global theorem giving a deterministic Q on all configurations with the full reflection-support contract.

Therefore the strong statement

    'Bałaban CMP 98 already supplies a global deterministic RP-compatible Q'

is NOT INSTALLED.

## Topological obstruction to an overstrong global mean

A useful negative result follows independently of the detailed Bałaban formula.

Assume one asks for a continuous, permutation-symmetric, idempotent n-ary mean

    m : G^n -> G,
    m(g,...,g)=g,

which is conjugation covariant. Restrict the inputs to a maximal torus T of a compact connected simple G. Since every input tuple in T^n is fixed by conjugation by T, conjugation covariance forces the output to lie in the centralizer of T, namely T. Thus m restricts to

    m_T : T^n -> T.

On pi_1(T) ~= Z^r, continuity gives a homomorphism

    (m_T)_* : (Z^r)^n -> Z^r.

Permutation symmetry forces all n coordinate homomorphisms to be the same integer endomorphism A. Idempotency on the diagonal forces

    n A = I_(Z^r),

which is impossible for n>1 over integer matrices.

Therefore no globally continuous fully symmetric idempotent mean of this type exists.

This is consistent with the classical topological-mean literature [61], which records the nonexistence of continuous symmetric means already on spheres/circles.

## Interpretation

This does NOT obstruct a global RG map. It rules out an unnecessarily strong global specification.

A deterministic extension can evade the no-go by breaking full permutation/hypercubic symmetry away from the regular chart, by weakening continuity to measurability, or by using a noncanonical selection. A blocking kernel can evade it more naturally while retaining all symmetries statistically.

Thus the correct RP custody target should not be 'a canonical global continuous mean'. It should be one of:

1. a globally measurable local map Q with only the symmetries actually required by gauge covariance and the chosen reflection; or
2. a positive local blocking kernel K(dV|U) whose pullback intertwines reflection and maps the positive coarse algebra into the positive fine algebra.

## Correction to YM-R16 / [59]

The CMP 119 (1988) complete-density paper establishes an inductive description including large-field domains and preservation of density form. Its abstract says that this completes the RG analysis and yields convergent expansions in the superrenormalizable case. It must NOT be promoted, by itself, to a theorem that the full four-dimensional Yang-Mills RG construction is globally completed. The correct use in this project is narrower: it shows that large-field sectors can be retained inside an exact complete-density formalism, so the 1987 small-field approximation is not the whole density architecture.

## Determination

YM-R17 closes with:

    regular-chart deterministic averaging: structurally compatible with gauge/reflection covariance;
    global continuous fully symmetric averaging: topologically overconstrained;
    global Bałaban-original deterministic RP map: not established in the corpus;
    globally covariant blocking kernel: viable next object.

The first unresolved issue is therefore no longer a branch cut in the logarithm alone. It is the design of a GLOBAL POSITIVE BLOCKING OPERATOR whose symmetry/support properties are exact and whose weak-field limit is compatible with the Bałaban estimates.

## Next frontier — YM-R18

Kernel replacement / reflection-positive blocking:

- formulate K(V|U) globally on compact G;
- require K to be gauge covariant, reflection covariant, local in the positive half-space, normalized and positive;
- prove that K^* intertwines reflection and preserves the positive-time algebra, hence maps RP measures to RP measures;
- test a concrete invariant-distance/Haar kernel;
- determine whether replacing Bałaban's hard delta constraint by such a kernel preserves the ultraviolet inductive estimates or changes the RG problem materially.

No pointer beyond YM-R17 is consumed here.