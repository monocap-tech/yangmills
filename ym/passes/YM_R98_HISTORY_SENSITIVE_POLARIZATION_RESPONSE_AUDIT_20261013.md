# YM-R98 — history-sensitive polarization / source-scale covariance correction

Date: 2026-10-13
Previous authoritative head: YM-R97 e74f67062a8d580a4ae397bb6a5632160ccf98de
Status: COMPLETE AS SOURCE-SEMANTIC AND ABSTRACT MATHEMATICAL AUDIT; NATIVE BETA COVARIANCE AND EQ029 OPEN
Next unconsumed cursor: YM-R99
Claim discipline: UNPROVED RESEARCH PROGRAM. No 4D Yang–Mills continuum construction, OS reconstruction, or positive mass gap.

## 0. Preflight / source receipts

The main branch was confirmed at YM-R97 before authoring this pass; R77-R96 were preserved. R97 recorded a third-party OCR transcript of the primary Bałaban CMP109 [7]. Current page-image retrieval via Project Euclid still yields a single iframe rather than PDF data, Springer content PDF access is unavailable, and the external repository does not contain the original CMP109 PDF. The third-party text source remains Git blob f1aec083a3a6470c67a2c1205ca740c2583fe37a at:
https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp109-effective-actions-part-i.txt
It cannot be treated as an image-verified original. OCR-damaged exact tensor signs, Eq(0.29) activity powers and norm, and primary numerical constants remain ORIGINAL-PAGE-OPEN. No new bibliography source is numbered; reuse [7], [21], [59], [85], [90]-[92].

Unambiguous prose in printed p.298, OCR lines 2494–2499, says that beta_j written with explicit argument g_(j-1) ALSO DEPENDS ON ALL PRECEDING COUPLINGS. Printed p.257, OCR lines 398–403, similarly names E_k dependence on g0,...,g_(k-1). This CORRECTS an inference in R74/R75; their physically aligned spacing a_(N+1,j+1)=a_(N,j) is still exact. Their abstract backward scalar cocycle remains logically valid only under the added effective-history-identification or history-decoupling hypotheses.

The source geometry of CMP109 Eq(4.37) (third-party OCR lines 2092–2098) gives polarization Pi as a sum of quadratic localized activity kernels; printed p.293 Eq(5.8)-(5.10) gives translation symmetry, Ward/transversality and spatial exponential decay of the single constructed polarization. Printed p.297 Eq(5.37)-(5.38) describes marginal transverse and third-lattice-difference remainder; p.264 Eq(1.22) gives beta through a mixed zero-momentum second derivative / spatial moment. This is SOURCE-TEXT-WITNESS only for intact prose; original exact display still requires image custody. Source-attested SINGLE-TRAJECTORY spatial locality is NOT a difference or historical response bound.

The independent dashi_agda file BalabanCMP109DirectBetaSourceCutsetExact.agda explicitly types "historyResponseDecay" as a CONDITIONAL field rather than a constructed physical proof. It is an independent research ledger, not a theorem in Yang-Mills and not an additional verified result.

## 1. Correct history type and exact aligned-scale insertion dictionary

Use a_(N,j)=L^(j-N), a_(N+1,j+1)=a_(N,j). For beta at depth N scale j, the semantically sufficient input must be permitted to contain
  h_(N,j)=(g_0^(N),...,g_(j-1)^(N)),
and for depth N+1 at scale j+1,
  h_(N+1,j+1)=(g_0^(N+1),...,g_j^(N+1)).
The exact source index/normalization map still requires the original PDF. No independence from background, volume, or boundary is asserted just because arguments are suppressed.

Fix one explicit reference prefix c_* in the admissible weak corridor and define the aligned-history embedding
  iota_j(h_(N,j))=(c_*,g_0^(N),...,g_(j-1)^(N)).
This is a DEFINED COMPARISON DEVICE, not a source construction. Need all interpolated histories admissible on the source analytic corridor.

Let b_(N,j)(h) be the marginal beta extraction on the actual source carrier after all gauge, Fourier and normalization identifications, and define
  tau_(N,j)(h)=|b_(N+1,j+1)(iota_j(h))-b_(N,j)(h)|.
This is the "prefix insertion / operator geometry" mismatch at aligned history. It includes any remaining source regulator, domain, cutoff chart and normalization difference. Physical-scale equality alone does not make tau vanish.

Define
  Delta_r = g_(r+1)^(N+1)-g_r^(N), r=0,...,j-1,
  Delta_prefix = g_0^(N+1)-c_*.
Then b_(N+1,j+1)(h_(N+1,j+1))-b_(N,j)(h_(N,j)) is split EXACTLY into an aligned-history variation plus the source-geometry/prefix insertion discrepancy tau. This prevents an extra UV layer from disappearing by notational reindexing.

## 2. Certified abstract history-response transfer lemma

Assume the finer beta functional b_(N+1,j+1)(u_0,...,u_j) is continuously differentiable on every segment between its actual history and iota_j(h_(N,j)), with coordinate-wise sensitivity
  |partial_(u_s) b_(N+1,j+1)(u)| <= A theta^(j-s),
  s=0,...,j,
where A>=0 and 0<=theta<1 are uniform in cutoff depth, volume, admissible gauge/background, and weak-coupling corridor (or with quantified dependencies as appropriate).

The fundamental theorem of calculus along the straight segment plus the exact triangle decomposition above yields
  |delta beta_(N,j)|
   <= tau_(N,j)
      + A theta^j |g_0^(N+1)-c_*|
      + A sum_(r=0)^(j-1) theta^(j-r-1)
              |g_(r+1)^(N+1)-g_r^(N)|.              (R98.1)

This is a CERTIFIED MATHEMATICAL IMPLICATION WITH EXPLICIT HYPOTHESES, not a Yang–Mills bound. All three terms are distinct native obligations.

If j=N-k with fixed k and the prefix couplings stay uniformly bounded, the isolated prefix term A theta^(N-k)|g_0^(N+1)-c_*| is geometrically summable in N. This statement does NOT control tau or the aligned-coupling mismatch sum. If j is fixed while N grows, theta^j supplies NO N-decay; one cannot sum over cutoff depths without more geometry. If theta=1, no geometric history suppression follows even at fixed physical endpoint k.

More generally, if native scalar endpoint sensitivity weights w_(N,j)>=0 from R72 obey
  sum_N sum_j w_(N,j) [
       tau_(N,j)+A theta^j |Delta_prefix|
       +A sum_(r<j) theta^(j-r-1)|Delta_r| ] < infinity,
then the weighted beta-map mismatch is summable by (R98.1). This is an abstract sufficient criterion, not verified in the native Bałaban trajectory and not a substitute for convergence of complementary sectors. A bare O(g_0^(N+1)) bound with g_0~N^(-1/2) would not be summable by itself.

## 3. Native polarization second-moment interface

For lattice Pi_(N,j)(z;h) in a COMMON source-normalized Fourier chart with beta extraction
  beta= -partial_(p_mu) partial_(p_nu) Pihat_(mu nu)(0)
for distinct mu,nu (as located by CMP109 Eq(1.22)/(5.42)), and an absolutely summable second spatial moment, the exact Fourier identity in R77 gives
  |delta beta| <= sum_(z in Z4) |z_mu z_nu| |delta Pi_mu nu(z)|
under compatible signs and source normalizations.

If source response kernels satisfy, for 0<=s<=j,
  sum_z |z_mu z_nu|
      |partial_(u_s) Pi_(N+1,j+1)(z;u)| <= A theta^(j-s),
then the beta sensitivity hypothesis of Section 2 follows immediately by termwise differentiation. This is the bridge:
  SOURCE-IDENTIFIED marked historical polarization
  + uniform mixed-moment response decay
  + controlled prefix source insertion geometry
  => (R98.1).

A spatial bound for Pi_(N,j)(z) separately, or for a same-background boundary-domain difference, does not establish response with respect to the EARLIER COUPLING HISTORY. The CMP99 "marked domain" source Theorem 3.14 / (3.154) may provide a factorwise method, but it is a SPATIAL DOMAIN mark, not automatically a coupling-history mark; assigning it theta^(j-s) would be a source-unsupplied promotion. The full log normalization, interacting Gaussian, localization cutoffs, deterministic marginal subtraction and inherited history are all relevant. The exact native derivatives must act on the full source functional, not just its Gaussian Schur block.

## 4. Certified counterexample: spatially finite-range, PSD, Ward transverse but no historical decay

Let d>=2 and p in [-pi,pi]^d. Set
  d_mu(p)=exp(i p_mu)-1,
  S(p)=sum_rho |d_rho(p)|^2,
  W_mu nu(p)=delta_mu nu S(p)-d_mu(p) conjugate(d_nu(p)).
For every real p and complex v,
  v*W(p)v=S(p)||v||^2 - |d(p)* v|^2 >=0
by Cauchy–Schwarz. Thus W is Hermitian PSD. Moreover
  sum_mu conjugate(d_mu(p)) W_mu nu(p)=0,
so it has the lattice Ward-transverse structure. All its entries are trigonometric polynomials, so W has a finite-range translation-invariant position-space kernel and satisfies every standard spatial exponential moment norm with fixed constants.

For mu != nu, W_mu nu(p)=-d_mu(p)conjugate(d_nu(p)) and
  -partial_(p_mu)partial_(p_nu) W_mu nu(0)=1.
For any earlier-coupling history h=(h_0,...,h_(j-1)), define
  Pi^(j)_mu nu(p;h)=h_0 W_mu nu(p),  h_0 in [0,gamma].
Then beta_j(h)=h_0 and partial_(h_0) beta_j=1 for EVERY j. No estimate
  |partial_(h_0) beta_j|<=A theta^j, theta<1,
can hold for arbitrarily large j with fixed A.

This is a CERTIFIED ABSTRACT COUNTEREXAMPLE:
  even positivity + Ward transversality + finite-range spatial locality
  DOES NOT imply decay of sensitivity to remote RG coupling history.
It does not claim the particular toy Pi is generated by Balaban's RG or satisfies all its nonlinear identities. The counterexample is stronger than an arbitrary nonlocal kernel because it honors the quadratic symmetries and spatial locality relevant to the source. It proves that the missing theta-like property is new dynamical information rather than an algebraic corollary of (5.9)-(5.10).

## 5. What source Eq(0.29) actually contributes and does not

The third-party transcript has legible p.258–259 prose indicating Taylor/Ward extraction, higher-order local residues, a strictly positive excess exponent alpha, and Theorem 1 conditional on all effective couplings lying in a sufficiently small interval. But Eq(0.29) itself is OCR-broken; its exact V^(j), norm, domain quantifiers and constants are not verified as ORIGINAL FORMULA. R69's conditional fixed-region root count remains correct under the candidate source-normalized C a^(4+alpha) e^(-kappa d_j(X)) and source-uniform rooted polymer sum.

Even a fully verified absolute Eq(0.29) bound on the GENERATED irrelevant output V_j would not alone imply (R98.1): it is an amplitude/locality estimate on a marginal-subtracted residual, not a derivative of Pi with respect to earlier beta-driving couplings. Likewise a marked CMP116 activity difference still requires actual source input transport; R77–R93 abstract transfer chain remains conditional. The beta history comparison and irrelevant remainder are STILL distinct native gates despite sharing Taylor/Ward machinery.

## 6. Exact obligation table / negative results

CERTIFIED ABSTRACT:
- History insertion identity and inequality (R98.1) under explicitly stated derivative/geometry bounds;
- polarization second-moment => beta response transfer with uniform source normalization;
- lattice PSD/Ward-transverse/finite-range counterexample disproving automatic history response decay.

SOURCE-TEXT-WITNESS:
- CMP109 [7] beta history dependence printed p.298, third-party OCR; original PDF image not available;
- CMP109 single-trajectory Pi spatial Ward/decay and small-field theorem context in the same OCR witness, not original exact equation proof custody.

CONDITIONAL NATIVE:
- uniform derivative bound A theta^(j-s) for actual history-dependent resummed full Pi;
- source-defined prefix insertion tau and admissible interpolation of histories;
- R72 scalar tail sensitivity weights and a summability theorem for the full RG comparison;
- source-compatible mixed-momentum Fourier normalization and gauge/chart transport.

OBSTRUCTED AS A GENERIC INFERENCE:
- aligned physical spacing => equal beta maps;
- source notation beta_j(g_(j-1)) => no preceding history;
- spatial Ward / positive Hessian / finite-range locality => scale-history contraction;
- Eq(0.29) absolute irrelevant amplitude => marginal beta-history response.

OPEN NATIVE:
- original image-verified CMP109 Eq(0.29),(5.37),(5.42), exact V definition and positive alpha/norm/quantifiers;
- history-response derivatives or summable marked polarization difference for actual cutoff pair;
- full coupling alignment under nonautonomous/history-sensitive maps, including extra UV prefix;
- native CMP116 V^(1)-to-activity dictionary, moving chart/covariance, R/B/large-field;
- complete state Cauchy, OS and physical gap.

## 7. Next frontier YM-R99 (unconsumed)

Make the actual source-history derivative concrete at its origin:
1. start with the CMP109 (1.3),(1.6),(1.20),(2.13) division between Gaussian normalization and inherited interaction; write the exact formal derivative of one-step Pi with respect to a past coupling and identify every explicit and implicit dependence;
2. compare whether any source theorem gives a positive decay reserve with HISTORY AGE (j-s), as opposed to spatial distance, or whether only a fixed-endpoint polarization defect is attainable;
3. identify the source admissibility of history interpolation, after gauge, finite-volume and complex tube domain choices;
4. keep original CMP109 scan acquisition and Eq029 original-image verification as a separate hard source gate;
5. retain parallel OS/physical time clustering work only if a source-native independent theorem can be advanced without confusing UV-stability with a mass gap.

Highest cumulative bibliography remains [92], next new source [93]. No continuum YM, reflection-positive continuum limit, or gap is asserted.
