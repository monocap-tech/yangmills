# YM-R97 — Wilson transfer positivity, physical-time gap, and CMP109 beta-history correction

Date: 2026-10-11
Prior certified head: YM-R96, 3fb98256761b9dc68c4e58e62b1e54b2f5c02d37
Status: COMPLETED SOURCE / ABSTRACT AUDIT; NATIVE CONTINUUM AND GAP OBLIGATIONS OPEN
Next cursor: YM-R98 (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM. No construction of 4D continuum Yang-Mills or its positive mass gap.

## 1. Repository reconciliation and two active fronts

The repository independently advanced from R76 through R96 before this run was ready to commit. R77 already audits moment-weighted Schur locality; R94–R96 preserve the original CMP109 equation source hold. R96 explicitly opens R97 for reflection-positive blocking, physical-time transfer and gap criteria. This pass uses that live cursor, preserves R77–R96, and records a newly discovered primary-paper OCR witness without claiming it is an original source-page verification.

Existing R18 supplies an ABSTRACT sufficient reflected Gram/half-space factorization for stochastic block pushforwards. R25–R26 construct a candidate global gauge/reflection-covariant heat-kernel center and weak-field local analytic jet; the complete reflection-plane Markov factorization, full Yang-Mills cutoff measure, gauge-invariant Hilbert transport, and uniform physical-time clustering are not certified.

## 2. Original and publisher-primary sources

[90] K. Osterwalder and E. Seiler (Annals of Physics 110 (1978), 440–471): the publisher abstract establishes physical positivity and a positive transfer matrix in lattice gauge/fermion settings; the distinct infinite-volume strong-coupling results are not a weak-coupling 4D continuum mass-gap theorem.

[91] M. Lüscher, Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories (Commun. Math. Phys. 54 (1977), 283–292), original DESY 76/54 preprint at https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf?version=1. Original scanned pages were inspected visually during R97: printed pp. 2–3 define gauge-invariant RP/Hilbert quotient and distinguish continuum validity; Proposition 1 at printed p. 8 supplies positive, bounded, self-adjoint finite-lattice transfer under the paper's restrictions; printed p. 10 explicitly leaves uniqueness/nondegeneracy of maximal transfer eigenvalue unsettled. Strict positivity of transfer is NOT a uniform physical energy gap.

[92] M. Lüscher and P. Weisz, Nuclear Physics B240 (1984), 349–361: publisher abstract warns that improved lattice actions may lose physical positivity, even allowing nonpositive spectral contributions/complex eigenvalues. No claim that the R25 blocking kernel actually suffers this defect; the source prevents transferring Wilson positivity automatically to arbitrary modified effective actions.

Source levels and exact URLs are recorded separately in the additive ledger [90]–[92].

## 3. A new concrete obstruction: reflection-invariant cutoff does not preserve reflection positivity

ABSTRACT THEOREM AND COUNTEREXAMPLE. Let fine spins s_- and s_+ be independent uniform {+1,-1}, reflection theta swapping them. For any complex positive-side f,
  E_mu[conj(f(s_-)) f(s_+)] = |E_mu f|^2 >= 0.
Thus the original product measure is reflection positive.

Now multiply by the nonnegative, reflection-invariant characteristic cutoff
  chi(s_-,s_+) = 1 if s_- = -s_+, else 0,
and normalize nu=2 chi mu. For F(s_+)=s_+,
  E_nu[conj((theta F)) F] = E_nu[s_- s_+] = -1.
The restricted probability measure fails reflection positivity.

Therefore original RP + a positive reflection-invariant restriction DOES NOT imply RP for the normalized restricted measure. This is not a demonstration that Bałaban's actual small-field cutoff violates RP. It identifies a native theorem obligation: prove reflected Gram factorization/compatibility for the actual full cutoff-and-block construction or avoid treating the restricted small-field sector as an OS-positive measure independently.

## 4. Exact spectral transfer criterion with physical normalization

ABSTRACT-DERIVED. For each lattice spacing a>0 suppose the gauge-invariant OS physical Hilbert space H_a has a normalized unique vacuum Omega_a. Suppose the one-step temporal transfer T_a is nonnegative self-adjoint, bounded by I, T_a Omega_a=Omega_a, and the rank-one P_a=|Omega_a><Omega_a| commutes with T_a. On Omega_a-perp let H_a=-(1/a)log T_a using functional calculus (or the positive injective restriction where needed).

For any fixed m>0,
  spec(H_a restricted to Omega_a-perp) subset [m,infinity)
  iff
  ||T_a(I-P_a)|| <= exp(-m a).
Equivalently, for every positive integer n,
  ||T_a^n (I-P_a)|| <= exp(-m a n).

Proof: the spectral functional calculus maps eigenvalue lambda of T in (0,1] to E=-(1/a) log lambda, decreasing strictly. The supremum of nonvacuum transfer spectrum is <=exp(-ma) exactly when its smallest physical energy is >=m. Uniform continuum use requires one m independent of spacing and physical volume. A fixed q<1 per microscopic step is not the appropriately normalized target for a finite limiting physical energy; exp(-ma)=1-ma+O(a^2).

STRICT POSITIVITY COUNTEREXAMPLE. On C^2 take Omega=(1,0) and T_a=diag(1,exp(-a^2)). For each a, T_a is strictly positive self-adjoint and has a unique top eigenvalue. Yet its physical Hamiltonian is H_a=diag(0,a), and the physical excitation gap a tends to zero. Its centered correlation at physical time t=na is exp(-a t), so finite-regulator RP and strictly positive T do not entail a uniform positive mass gap.

This does not instantiate pure Yang-Mills; it rules out a generic logical implication. R96 already explains the separate OS reconstruction and dense centered gauge-invariant observable-family requirements for upgrading a common physical-time decay estimate into a continuum spectral gap.

## 5. Exact status of the R18/R25/R26 RP candidate

The proposed single-center kernel k_e(dV|U)=rho_(g_k^2/c)(V C_e(U)^(-1))dV_Haar is a useful candidate because Haar translation normalizes it exactly and R25 records gauge/orientation/reflection covariance and half-space support away from the reflection plane. R26 records a regular-chart O(g_k) analytic correction relative to the Gaussian reference.

The remaining NATIVE transfer prerequisites are all distinct:
(a) a reflection plane compatible with the fine/coarse temporal lattices and support of all path families;
(b) a proof of reflected Gram/conditional-product factorization including plane-straddling/boundary links, without uncontrolled coupling between halves;
(c) exact full-measure identity for the complete RG integration and large-field sectors, rather than RP asserted for small-field terms after a cutoff;
(d) induced maps/compatibility among gauge-invariant physical Hilbert quotients and corresponding temporal transfer operators;
(e) cutoff- and physical-volume-uniform physical-time centered contraction with one m>0; and
(f) OS convergence, locality, nontriviality, dense observables and continuum reconstruction.
R18's abstract theorem supplies a sufficient algebraic test for (b) but does not prove (b)–(f) for the native construction.

## 6. NEW independent primary-paper text witness for CMP109 [7]: beta has inherited coupling history

The public repository chboishabba/dashi_agda has OCR text of the actual Bałaban CMP109 (1987) paper; exact file and provenance receipt: ym/source_receipts/YM_R97_CMP109_TEXT_EXTRACTION_RECEIPT_20261011.md. Unlike earlier R94 external manifests, the TEXT BYTES of this third-party extraction have been inspected. This is not the original publisher scanned PDF: damaged displayed equations cannot be certified from it.

Legible printed p. 298 prose following Eq. (5.42), witness lines 2494–2499, explicitly observes that beta_j, although written with argument g_(j-1), depends on all preceding coupling constants. Printed p. 257 likewise states that E_k depends on g_0,...,g_(k-1). Thus R74–R75's negative inference from the displayed argument list to exclusion of inherited history must be corrected APPEND-ONLY.

The causal semantic type is beta_j[g_0,...,g_(j-1)], not proven to factor through just (physical scale a_j,g_(j-1)). Even when a_(N+1,j+1)=a_(N,j), equality of physical lattice spacing does not align the UV histories of the two cutoff constructions. R71's backward uniqueness/cocycle theorem remains a correct CONDITIONAL theorem if the full history-sensitive maps are shown shift-covariant on the relevant canonical trajectories; source text alone does not establish this.

Other OCR text recoveries:
- (0.29) surrounding prose and Theorem 1: under sufficiently weak couplings the small-field irrelevant activity is source-claimed to be uniformly bounded with some alpha>0, but displayed exact formula/norm/quantifiers are OCR-GARBLED and ORIGINAL PDF IMAGE REMAINS HELD;
- Theorem 2 SU(2) tuned coupling on printed p.259 expressly defers its perturbative proof;
- (1.20),(1.22),(4.37),(5.8)-(5.10),(5.37),(5.38),(5.42) link the one-step resummed quadratic polarization, Ward/transversality, beta moment and higher-derivative remainder; exact displayed tensor identities/signs still require page-image inspection;
- (2.13) defines a constrained Gaussian fluctuation logarithmic integral; quadratic Schur positivity alone cannot replace its determinant, nonlinear and marked-history dependence.

This is a material increase in SOURCE-TEXT EVIDENCE, not closure of the original-equation-image gate or of NativeBetaMapShiftCovariance. History-sensitive polarization shift, not an autonomous single-argument scalar stationarity, is the more faithful native next question. No positive-alpha Yang-Mills bound is promoted from the OCR math alone.

## 7. Classifications and next frontier

SOURCE-ATTESTED within source scope: finite Wilson transfer physical positivity [90]/[91]; improved-action RP warning [92].
CERTIFIED ABSTRACT-DERIVED: reflection-invariant cutoff RP counterexample; physical-time transfer-gap equivalence under precise spectral assumptions; T_a=diag(1,exp(-a^2)) gap-collapse counterexample.
TEXT-WITNESS VERIFIED, NOT ORIGINAL-PDF-VERIFIED: CMP109 printed p.298 explicit beta coupling-history dependence.
CONDITIONAL: R25 exact full-kernel RP via reflection-plane Gram factorization; native cutoff/volume physical Hilbert maps; history-sensitive marked polarization comparison.
OPEN: original CMP109 displayed equations/quantifiers; complete historical beta shift; exact/full continuum cutoff Cauchy, volume/OS reconstruction, uniform physical-time clustering and positive mass gap.

YM-R98 UNCONSUMED: verify CMP109 original equation images against newly available OCR; reconstruct a full beta history functional and the operator norm for marked polarization history differences, distinguishing boundary locality from history dependence. In parallel, pursue source-native reflection-plane factorization and physical-time clustering without claiming that RP proves a gap. Highest reference [92]; next new ID [93].
