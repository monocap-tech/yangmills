# YM-R96 — source-backed UV-stability/mass-gap separation and finite-lattice Cauchy counterexample

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior checkpoint YM-R95 816e3152e28ac1ce04d91a6ffd7027bf47e50873
Status: PRIMARY-SOURCE-BACKED ALTERNATE FRONT + ABSTRACT NEGATIVE/SPECTRAL RESULTS; CMP109 SOURCE HOLD PERSISTS
Next live cursor YM-R97 (unconsumed); CMP109 original equation receipt held separately.
Claim: UNPROVED RESEARCH PROGRAM. No continuum 4D Yang–Mills construction or positive mass gap.

## 1. Source-first check preserves the blocked CMP109 verdict

Target original Bałaban CMP109 [7], DOI 10.1007/BF01215223; equation windows (0.29), (5.37), (5.42); local V^(j), positive alpha and beta extraction. Alternate targeted web/slow and Project Euclid PDF access in R96 again yielded metadata or iframe HTML, not a visually readable original page. Direct container HTTPS request to the Project Euclid .pdf failed with network ConnectionError. The external manifest SHA256 from R94/R95 still identifies someone else's original local source cache but NOT accessible bytes. NO new original Eq029 testimony was obtained. Do not claim positive-alpha or the R70 first-layer source dictionary closed.

Following R95's explicit instruction, this pass pivots to a DIFFERENT independently source-backed question, rather than adding another assumed tagged CMP116 theorem.

## 2. A new, visually inspected original primary source separates the proof burdens

Reference [88]: T. Balaban, J. Imbrie and A. Jaffe, *Exact Renormalization Group for Gauge Theories*, 1984 proceedings, author-hosted 25-page primary PDF at https://uva.theopenscholar.com/files/john-imbrie/files/exactrg.pdf . PDF pages 0–2 (printed 79–81) were examined as rendered ORIGINAL page images.

Printed p.79 states the presented RG block-spin procedure applies at least to the superrenormalizable case; p.80 specifies the illustrative problem as Abelian Higgs theory in 2 or 3 dimensions. The same printed page distinguishes UV stability (spacing-uniform finite-volume partition-function/correlation control) from infrared Higgs/mass-gap control (exponential observable clustering with a rate uniform in lattice spacing, volume and observable class). Printed p.81 explicitly conditions passage of bounds to corresponding limits on those limits' existence.

Therefore [88] supplies a historically direct proof-goal split. It does NOT prove anything about a mass gap for 4D nonabelian pure YM, nor does it identify Bałaban's 1987 Eq(0.29).

The 2026 peer-reviewed review by M. R. Douglas [89], *The Yang–Mills Millennium problem*, Nature Reviews Physics 8, 86–97, makes the modern continuum-existence and mass-gap components explicit and says neither is yet available in needed mathematical generality. This is context, not a new theorem.

## 3. UV density bounds alone do not yield cutoff Cauchy: exact finite gauge example

On a finite oriented link lattice containing one plaquette p, take SU(2) link variables with product normalized Haar probability nu0. Define a REAL gauge-invariant bounded observable
  F(U) = (1/2) Tr(U_p),  -1<=F<=1,
where U_p is the ordered holonomy around p. Independence and Haar invariance imply U_p itself has Haar distribution in SU(2). By fundamental SU(2) character orthogonality,
  E_nu0 F=0,    E_nu0 F^2=1/4.

Fix 0<eps<1. Define for each cutoff label N a positive density
  rho_N(U)=1+(-1)^N eps F(U)
with respect to nu0. Then
  int rho_N dnu0=1,
  1-eps <=rho_N(U)<=1+eps
uniformly in N, volume-independent for this fixed finite lattice, and every rho_N is gauge invariant. Yet
  E_(rho_N nu0) F=(-1)^N eps/4,
so the expectations are not Cauchy.

This is an exact ABSTRACT COUNTEREXAMPLE to the inference
  uniform positive normalized density bounds => convergence of a fixed gauge-invariant observable across cutoff indices.
It is NOT a Bałaban RG trajectory, not claimed RP, and does NOT refute any complete CMP122 theorem. CMP122-II [31] Theorem 1 is moreover conditional on a small-coupling interval and has additional source structure; R58/R59 already audited that. The counterexample isolates only the inequality of proof obligations, so unqualified UV-stability bounds must not be promoted to existence or observable convergence.

## 4. Uniform physical-time clustering implies a spectral gap if OS reconstruction and density hold

ABSTRACT-DERIVED spectral consumer. Suppose an OS reconstructed physical Hilbert space H_phys has vacuum Omega, nonnegative selfadjoint H with H Omega=0. Let A be a family of gauge-invariant local operators for which centered F Omega vectors span a dense subspace of Omega-perp. Assume for every such F and ALL real physical t>=0,
  0<= C_F(t)=<F Omega,e^{-tH}F Omega> <= A_F e^{-m t}
with one m>0 common to the family, and finite A_F possibly depending on F.

By the spectral theorem, C_F(t)=int_[0,infty) e^{-E t} dmu_F(E) for a finite positive measure. If mu_F([0,m-delta])>0 for some delta>0, then
  C_F(t) >=mu_F([0,m-delta])e^{-(m-delta)t},
contradicting the upper bound at sufficiently large t. Thus mu_F([0,m))=0 for each F. Density of the centered vectors and boundedness of spectral projections then show
  spec(H restricted to Omega-perp) subset [m,infty).
This is the desired ABSTRACT positive spectral gap implication.

Qualifications: just one Wilson loop or one gauge observable cannot certify a full spectral gap unless its vectors generate the relevant physical Hilbert sector. Clustering must be uniform in PHYSICAL time t, not merely in a fixed number of shrinking lattice time steps. An OS Hilbert space, continuum Schwinger function convergence/positivity and the dense gauge-invariant observable family are separate source obligations. Nothing here derives the required clustering from the native Bałaban source or establishes the 4D YM OS continuum.

## 5. R96 determination and R97 cursor

PRIMARY VISUALLY VERIFIED: [88] original 1984 primary PDF pp.79–81, clean distinction between UV stability and IR mass-gap clustering; dimensional/model scope is superrenormalizable Abelian Higgs 2D/3D.
REVIEW SUPPORTED: [89] 2026 continuum existence vs mass gap distinction.
ABSTRACT DERIVED: SU(2) gauge-invariant alternating-density finite-lattice non-Cauchy example; spectral-measure exponential-decay => uniform mass-gap theorem under dense observable/OS hypotheses.
SOURCE HELD: original CMP109 Eq(0.29)/(5.37)/(5.42), V^(1) alpha, common cutoff source type and polarization extraction, CMP116 tagged source input.
OPEN NATIVE: continuum cutoff Cauchy/OS, volume limits, uniform physical-time gauge-invariant clustering, positive spectral gap.

NEXT YM-R97 (UNCONSUMED): specifically audit the user project's reflection-positive blocking kernel (R25/R26) against the minimal OS/transfer-matrix-to-gap consumer, distinguishing reflection positivity and a finite-lattice transfer operator from a continuum cutoff/volume UNIFORM clustering theorem. Use original Osterwalder–Seiler or accessible RP sources; don't claim gap from RP itself. Keep CMP109 receipt parked, reopen only with legible primary pages.

Highest bibliography [89], next [90].
