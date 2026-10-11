# YM-R88 — uniform single-anchor replacement and many-UV-insertion stability

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior head: YM-R87, commit 6e96ed4709edddc6a371ade200f96a02a7fcb3ec
Status: COMPLETE AS ABSTRACT MANY-ANCHOR THEOREM AND NATIVE EVIDENCE AUDIT
Next cursor: YM-R89 (unconsumed)
Claim: UNPROVED RESEARCH PROGRAM. No Yang-Mills continuum construction, OS reconstruction or mass-gap proof.

## 1. Recover R44/R45 source relevance without overpromoting it

R44/R45 (September 16) constructed an activity-level *single bounded-support* analytic insertion into Bałaban's CMP116 post-product-Gaussian integrand, with fixed source-owned anchoring Y0/Z0 and a conditional H_soft(Z)=O(g_k) exp(-mu' d_k(Z)). Their stated uniformity requires the insertion and its support to be admitted in the same source analytic/localization regime. R47/R50/R53-R54 previously audited CMP116's complex field-uniform cluster bounds and the native H(Z) activity/connected-exponentiation route. CMP116's published abstract supports the fact that Part I's one-step fluctuation integral is represented by an exponentiated cluster expansion [21].

The new cross-cutoff problem differs from the RP blocker: the extra ultraviolet layer may contribute an increasing set A_N of physical roots, and the effect of one input is evaluated while many other inputs are active. Neither R44 nor its primary CMP116 source window states uniformity over arbitrary partial insertion environments. A source-identified common carrier, coupling, background chart, and uniform weakness/analyticity still need proof.

Primary CMP109 (1987), Eqs (5.37),(5.42),(0.29), remains unavailable in equation-readable form. Its identity and small-field beta-function architecture are source-bibliographic facts [7], but [85]'s schematic a_N^(4+alpha) bound is a SECONDARY locator only. No alpha is promoted. Existing references [7],[21],[59],[85],[87] reused; highest [87], next new [88].

## 2. Many-anchor replacement theorem — ABSTRACT-DERIVED, with explicit constants

Let Lambda be a finite region of Z^4 with the nearest-neighbor graph, A a finite set of potential input anchors x, and P the finite collection of connected, nonempty output polymers Z. A designated anchor a(Z) belongs to Z. Write n=|Z| and dist(x,Z)=min_(u in Z) |x-u|_1.

For every S subset A, let H_Z(S;b) be holomorphic in background b on one common radius-r complex polydisc. Assume, for all S and x notin S, the UNIFORM SINGLE-ANCHOR REPLACEMENT estimate
  sup_b |H_Z(S union {x};b)-H_Z(S;b)|
  <= C u_x exp[-mu tau(Z,x)],
where u_x>=0, C,mu>0 are independent of S,A,volume and UV depth, and tau(Z,x) denotes the minimum number of lattice edges in a tree containing every site of Z and x. Let u_* = sup_x u_x.

Because Z is connected and the shortest tree path from x to Z has length >=dist(x,Z) with at least dist(x,Z) additional non-Z vertices,
  tau(Z,x) >= (|Z|-1)+dist(x,Z).
This is a graph-combinatorial theorem for unit-edge lattice connectivity, NOT yet an equality for Balaban's d_k metric.

Order A arbitrarily as x_1,...,x_m and S_j={x_1,...,x_j}. Exact telescoping gives
  H_Z(A)-H_Z(empty)
   =sum_(j=1)^m [H_Z(S_j)-H_Z(S_(j-1))].
Hence
  sup_b |Delta H_Z|
    <= C sum_x u_x exp[-mu tau(Z,x)]
    <= C u_* exp[-mu(|Z|-1)] sum_x exp[-mu dist(x,Z)].

Set S0(mu)=sum_(v in Z^4) exp(-mu |v|_1)<infinity. Since exp[-mu dist(x,Z)] <= sum_(u in Z) exp(-mu|x-u|_1),
  sum_x exp[-mu dist(x,Z)] <= |Z| S0(mu).
Consequently
  sup_b |Delta H_Z|
   <= C u_* |Z| S0(mu) exp[-mu(|Z|-1)].

Suppose for every root z there are at most C_ent^(n-1) connected n-site Z containing z, with C_ent fixed independently of volume. For a weight beta>0 define
  delta_A(beta)=sup_z sum_(Z:a(Z)=z) exp(beta |Z|) sup_b |Delta H_Z|.
Let q=C_ent exp(beta-mu). If q<1, then
  delta_A(beta)
    <= C u_* S0(mu) sum_(n>=1) n C_ent^(n-1) exp(beta n) exp[-mu(n-1)]
    = C u_* S0(mu) exp(beta)/(1-q)^2.

BOXED ABSTRACT THEOREM:
  EnvironmentUniformSingleAnchorReplacement + q<1
  => delta_A(beta) <= C mu,beta,geometry * u_*,
with NO factor proportional to the total number |A| of UV input anchors. The two powers of (1-q)^(-1) account for connected-polymer enumeration and anchor multiplicity.

The formula is in a fixed microscopic graph normalization. To identify delta_A(beta) with R85/R86's native CMP116 weighted activity-difference norm one needs the exact source tree metric, anchor definition, scale conversion and coupling/gauge chart. R86's parameters a,nu can be used by beta=a+nu ONLY after that source dictionary and common KP margin are verified.

## 3. How this avoids R87's artificial global-input analytic ball

The theorem does NOT require holomorphy of the complete one-step map F(v) on a fixed Banach ball of arbitrary irrelevant inputs. It requires only a one-anchor estimate valid in each of the finitely many partial insertion environments. Equivalently, if H_Z(t;b) is differentiable for t in [0,1]^A, it suffices to prove
  sup_(t,b)|partial_(t_x)H_Z(t;b)| <= C u_x exp[-mu tau(Z,x)]
and integrate along the diagonal t_x=s. This is a quantitative LOCALIZED source insertion theorem. The differential formulation still requires uniformity when all other inputs are on, and does not assert it from endpoint bounds.

COUNTEREXAMPLE showing why R44 at an empty environment is insufficient: take A with m>=2 roots and one formal output activity H_Z(t)=c product_(x in A) t_x. Every single derivative at t=0 vanishes, but H_Z(1)-H_Z(0)=c. Knowing the unmodified one-insertion response at the baseline does not control the simultaneous insertion difference. This example is abstract and need not satisfy the desired spatial tether; that is exactly why the tether is an additional hypothesis.

## 4. Physical UV scaling and alternative local finite-volume consumer

If an ORIGINAL source theorem and first-common-scale dictionary give u_*=O(a_N^(4+alpha)), a_N=L^-N and alpha>0, R88's MICROSCOPIC rooted estimate yields delta_A(beta)=O(a_N^(4+alpha)) in its microscopic root-coordinate norm. For a fixed physical four-volume with at most C_V a_N^-4 input roots, the worst-case total sum is O(a_N^alpha), summable in N. The norm conversion to physical beta/F^2 moments can contain powers of a_N and cannot be assumed from this counting; source roots, output localizations, gauge/measure sectors and marginal corrections still need verification.

One weaker, different conditional consumer uses R87 directly: if the complete transported extra-layer regular perturbation is pointwise bounded as a normalized finite-volume potential d_N(b,Y), with sup_complex |d_N|<=C a_N^alpha and uniform tilted normalization Q, then R87 bounds the log-partition response on the common analytic collar. That global sup bound is often too strong for unbounded Gaussian fluctuation fields and is NOT furnished by the schematic polymer V bound. The rooted insertion theorem is the more source-shaped route if such pointwise global boundedness fails.

## 5. Full first-common-scale compatibility still separate

As in R70/R87, after one RG step at the finer depth the first common-scale difference decomposes schematically into vacuum, marginal Wilson, regular V^(1), and R/B/large-field/measure/chart contributions. A bound on V^(1) even if strong and source-primary-verified does not imply marginal-tail coherence or large-field compatibility.

CMP119 source-attests only that E^(j)(1) and beta_j A are explicitly subtracted. The exact CMP109 extraction projector, Eq(0.29) V^(1) sign/normalization and relation to the CMP116 H(Z) input are not yet source-locked. An irrelevant activity could also be regenerated into a marginal coefficient downstream unless the native beta-map covariance or a summable projection estimate is established.

Therefore R88's mathematical local many-anchor transfer is a CONDITIONAL interface, not a Yang-Mills convergence proof.

## 6. Evidence determination and next cursor

ABSTRACT-DERIVED:
- exact arbitrary-order telescoping over finitely many anchors;
- graph-tree tether tau(Z,x)>=|Z|-1+dist(x,Z);
- exponential anchor convolution and finite animal-entropy sum with explicit (1-q)^(-2);
- uniform per-environment replacement yields a cutoff-volume-independent rooted output bound;
- baseline-only derivatives fail to control collective changes (counterexample).

PREVIOUS SOURCE-LOCATED:
- R44/R45 fixed-support inserted CMP116 H(Z) construction, source Y0/Z0 hull and analytic input qualifications;
- R47/R50/R53/R54 native CMP116 field analytic, H(Z), and cluster/resummation estimates;
- R70/R87 source-scale alignment and CMP119 vacuum/beta subtraction.

OPEN NATIVE:
1. Show the actual extra finest-layer source correction is representable as a sum of anchored local inputs on a common CMP116 chart after scalar marginal matching and source measure normalization.
2. Prove environment-uniform marked activity replacement, tethered to the inserted root, along ALL partial insertion environments, with constants independent of UV cutoff, volume and common weak-coupling trajectory.
3. Match Balaban's tree metric d_k, coarse-root cover and physical-volume counting to the abstract lattice tree/animal bound.
4. Establish the primary CMP109 Eq(0.29) V^(1) norm with alpha>0, exact one-layer identity, and any input amplitude u_* implied by it; do not treat secondary [85] as primary.
5. Control boundary/large-field and Wilson marginal-tail sectors, and source full Pi beta/F^2 normalization.

Next YM-R89 (UNCONSUMED): audit the native CMP116 weakening/localization functional in the presence of arbitrary prior bounded-seed insertions; test a bootstrap smallness condition ensuring every partial environment stays in the same complex admissible class, possibly using a total physical-volume alpha-budget. Examine how the R44 one-insertion estimate differentiates with respect to each tagged root, and whether a tagged connected-polymer tree bound survives the D/P/Z0/Z0' resummation uniformly. Separately continue direct primary Eq(0.29) recovery and marginal-tail checking. No claim of native mass-gap progress from abstract bounds alone.
