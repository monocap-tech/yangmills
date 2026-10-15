# YM-R103 — CMP99(3) domain-marked propagator comparison / CMP116 nonlinear minimizer stability cutset

Date: 2026-10-14
Repository: monocap-tech/yangmills
Prior verified head: YM-R102 cbc8f9091ca72bc20899e91ccb6a49a604cfe9e7
Status: COMPLETE AS SOURCE-TEXT THEOREM RECOVERY AND CONDITIONAL MATHEMATICAL INTERFACE; NATIVE TWO-CUTOFF HISTORY RESPONSE OPEN
Next unconsumed cursor: YM-R104
Research status: UNPROVED. No continuum 4D Yang–Mills existence, physical OS limit or positive mass gap.

## 0. Repository and evidence boundary

At start, main was verified at YM-R102, whose live cursor is YM-R103. R101–R102 have already separated the source input E_k, the pre-Mayer CMP116 V'_k potential, the full V_k potential and the moving-localization operator defect. R80 and R82 distinguish constrained covariance locality from aligned covariance difference. R98–R100 prohibit deriving historical coupling sensitivity from spatial locality or a formal off-trajectory history interpolation.

This pass reads an actual full-text third-party OCR extraction of:
[? existing bibliography for CMP99(3); reuse its existing source reference rather than create or guess a number] T. Bałaban, "Propagators for Lattice Gauge Theories in a Background Field," Communications in Mathematical Physics 99(3) (1985), 389–434, DOI 10.1007/BF01240355.
Text witness: https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp99-background-propagators.txt
Observed Git blob ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743, 130782 content characters, 2202 split lines.

Also re-read CMP116 (1988) [21] full paper via:
https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp116-effective-actions-part-ii.txt
Git blob 2de28469578fcdc14270f57516b190234f9c8812.
These are PRIMARY-PAPER TRANSCRIPTIONS hosted in a third-party repository, not original PDF/page image checks. The external README expressly disclaims their replacement of the PDFs; signs and constants damaged by OCR are NOT promoted as original-image-certified. The original CMP109 [7] Eq(0.29),(5.37),(5.42) image gate remains open. The highest cumulative numbered reference remains [92], next [93]; no new numbered reference created.

Crucial CMP99 disambiguation: CMP99(1) 75–102 = regular configuration/gauge-fixing, DOI 10.1007/BF01466594; CMP99(3) 389–434 = background propagators, DOI 10.1007/BF01240355. Theorem 3.14 and Eq(3.154) belong to CMP99(3) ONLY.

## 1. SOURCE TEXT WITNESS: CMP99(3) Theorem 3.14 genuinely supplies domain-motion decay

At printed pp.426–427 (OCR lines 1840–1869), the source considers TWO admissible sequences of localization domains {Omega_j} and {Omega'_j}, with M,R sufficiently large and the paper's regular background/operator hypotheses. It sets Omega = Omega_k intersect Omega'_k. For already constructed source propagator/operator types (including G', G, G1, H and related inverse blocks described just before the theorem), the difference satisfies its usual operator norm/decay inequalities with an ADDITIONAL exponential factor of the schematic form

  exp[-delta_0 d_Omega(y,y')],                            (R103.1)

where the source Eq(3.154) distance measures how far the localizations y,y' must reach to encounter the COMPARISON REGION'S COMPLEMENT. The exact OCR formula for d has damaged index symbols; do not use an invented literal version in a native estimate.

The explicitly given mechanism is random-walk cancellation: all walks whose localization domains stay within common Omega cancel; only walks intersecting the changed exterior remain, and the walk-decay factor pays the distance-to-difference penalty. This is NOT merely a generic observation that separate Green kernels decay.

Strict jurisdiction:
- domain sequences satisfying the precise CMP99 conditions, NOT arbitrary different couplings or backgrounds;
- common source operator coefficients/regular background on the overlapping region sufficient for walk-by-walk cancellation;
- the source's already constructed operator types. The later source CMP99(3) Theorem 3.15 / (3.185) gives a related constrained covariance C^(k) and its random-walk decay, but it appears AFTER Theorem 3.14: do NOT claim verbatim (3.154) for C^(k) without verifying how its additional random-walk construction preserves the mark.
- source-uniform prefactors are conditional on the same small-regularity, M,R, scale, operator and volume corridor.

CMP99(3) (3.156)–(3.158), OCR lines 1905–1940, work on an ACTUAL constrained independent Gaussian carrier B=C Bbar and claim uniform coercivity for C* Delta_k C under the cited regularity. This does not identify distinct cutoff carriers as one common operator by itself. Theorem 3.15/(3.185)–(3.187), OCR lines 2095–2117, attests source covariance random-walk expansion/exponential decay, not a two-history difference estimate.

CLASSIFICATION: SOURCE-TEXT-WITNESS OF A NATIVE SPATIAL DOMAIN COMPARISON. It is stronger than a purely synthetic spatial locality lemma, but weaker than required historical scale covariance.

## 2. Exact operator difference channels: domain mark versus bulk/background mark

Suppose, only after defining a common source carrier, an operator K(Omega,U) depends on a localization domain sequence Omega and regular background U. Then the exact algebraic decomposition is

  K(Omega_1,U_1)-K(Omega_0,U_0)
   = [K(Omega_1,U_1)-K(Omega_0,U_1)]
     +[K(Omega_0,U_1)-K(Omega_0,U_0)].                   (R103.2)

The first term is a domain-motion comparison potentially eligible for source (3.154) provided BOTH domain sequences are admissible for the SAME U_1 and have matching overlapping random-walk data. The second is a background/operator-coefficient comparison at a FIXED sequence. CMP99(3) source analyticity/regularity does not supply an arbitrarily small bound for it without quantitative |U_1-U_0| and a common complex chart/radius.

There can also be a third carrier/normalization difference if the two histories have different gauge constraint matrices C_i, conditional Gaussian dimensions, Fourier background identification, cutoff indicators or Wilson/marginal normalization. R99–R102 retain these as separately typed channels, not as a K difference by fiat.

Counterexample to a DOMAIN-ONLY argument for historical differences: same complete domain Omega_0=Omega_1 with a scalar strictly positive local operator K(u)=(1+u)^(-1) at one site, u in [0,1]. K(0) != K(1), despite zero boundary/domain defect. There is no far-away geometric region to pay. Therefore (3.154) cannot bound history-driven changes in local coefficients absent an extra hypothesis.

At a fixed reference U with TWO domain sequences, source (3.154) is especially useful for matching common-interior observables when the domain-difference region recedes in lattice units as a UV cutoff grows. But NO proof that canonical N-vs-N+1 trajectories have the required nested domain coincidence, source-normalized root count and physical-scale separation has been recovered here.

## 3. CMP116 fixed-point equations: exact finite-difference stability consumers

CMP116 printed pp.2–3, (1.2)–(1.5), OCR lines 80–105, expresses the nonlinear substituted fast field H_k(B') via:
  z = H0 B' + a,      Hfast = z - H d(z),
  d(w) = C_nl(w-H d(w)),                               (R103.3)
  a = -G N(H0 B'+a),  N = grad V_nl,                  (R103.4)
where C_nl and V_nl denote the paper's NONLINEAR maps/functions (not Gaussian covariance C, not the pre-Mayer V_k input). Names here are abstract disambiguations because OCR notations overlap. The paper proves source analytic fixed points under its small-coupling regularity conditions and builds weakened H(s),G(s),H0(s) by random walk expansions in (1.6)–(1.11); its displayed text records contraction for the d equation under the selected small-field domain.

CERTIFIED ABSTRACT FIXED-POINT COMPARISON LEMMA:
Let F_i:X->X (i=0,1) be contractions with a COMMON q<1 on a common complete invariant subset of the same normed space; let d_i=F_i(d_i). Then
  ||d_1-d_0|| <= ||F_1(d_0)-F_0(d_0)||/(1-q).          (R103.5)
Proof: telescope F_1(d_1)-F_0(d_0), bound first term by q||d_1-d_0|| and rearrange. This compares actual endpoint fixed points, without any interpolating history.

For the d equation set F_i(d)=C_nl,i(w-H_i d). Suppose C_nl,1 is L_C-Lipschitz on the common argument domain and define delta_C(w0)=||C_nl,1(w0)-C_nl,0(w0)|| at w0=w-H0 d0. Then
  ||d_1-d_0||
    <= [L_C||H_1-H_0|| ||d_0|| +delta_C(w0)]/(1-q_D). (R103.6)
The same bound applies pointwise to d_i(w) with w transported onto an actual common source chart. Source-uniform q_D and marked operator bounds are NOT yet verified in this cross-cutoff weighted norm.

For a equation set T_i(a)=-G_i N_i(H0_i B'+a) and assume common contraction q_A<1, sup||N_1||<=K_N, ||G_0||<=K_G, N_1 L_N-Lipschitz and at z0=H0_0 B'+a0 set delta_N(z0)=||N_1(z0)-N_0(z0)||. Then
  ||a_1-a_0||
    <= [||G_1-G_0|| K_N
        +K_G( L_N||H0_1-H0_0|| ||B'|| +delta_N(z0))]/(1-q_A).  (R103.7)
Proof: apply (R103.5) to T_i and telescope G_1N_1(z1)-G_0N_0(z0) at a0. Here delta_N itself generally depends on the H and d fixed-point movements (and possibly source background), and must NOT be assumed zero.

For Hfast_i=z_i-H_i d_i(z_i), if d_1 is L_d Lipschitz in its argument, sup||d_1||<=K_d, ||H_0||<=K_H (the H, not H0, in the paper's notation), then
  ||Hfast_1-Hfast_0||
    <= (1+K_H L_d)||z_1-z_0||
       +||H_1-H_0|| K_d
       +K_H sup_z||d_1(z)-d_0(z)||,                   (R103.8)
where ||z_1-z_0||<=||H0_1-H0_0||||B'||+||a_1-a_0||.
All these are useful CONDITIONAL consumers, not source-proof of the missing differences.

The actual CMP116 weakening localizations apply s derivatives to composed F(Hfast(s)); propagation of an EXPONENTIALLY MARKED difference through those operations requires a common Banach algebra/norm stable under the nonlinear fixed points, common complex s-polydiscs with Cauchy radii and uniform contraction margins, and a POSITIVE resummation of marked random-walk terms. A standard unmarked existence/analyticity proof is insufficient to guarantee uniform Lipschitz bounds with the exact spatial distance factor or the UV excess exponent.

## 4. Precise source applicability/failed transfer table

A. Pure domain-sequence motion at identical background/operator: SOURCE-TEXT-SUPPORTED via CMP99(3) Theorem3.14, conditional on precise admissible sequence and localization types. It gains SPATIAL boundary distance, not RG-history age.

B. Covariance-root C^(k), constrained Gaussian/gauge/chart motion: individual source decay in CMP99(3) Theorem3.15/(3.185), but domain-marked difference for this later operator and two-cutoff normalization require extra proof. OPEN NATIVE.

C. Background/gauge coefficient change at identical domains: needs a source-common analytic chart and a quantitative Lipschitz bound, or a directly marked propagator response to the background difference. OPEN NATIVE. The scalar counterexample proves domain mark alone does not cover it.

D. CMP116 nonlinear D/a/Hfast maps: abstract finite-endpoint stability (R103.5)-(R103.8) is CERTIFIED conditionally; uniform contraction/weighted operator response in the true CMP116 family remains OPEN.

E. Localization operator L_sigma in R102: need to differentiate/telescope weakening kernels, compositions and their s derivatives under the above quantitative marked bounds, including compatible domains and source absolute summability. OPEN.

F. History input difference Delta E_k and physical beta: neither Theorem3.14 nor fixed-point contraction creates history-age attenuation or a relative positive-alpha a_N gain. R98/R100 relative-history and R72 tail summability remain OPEN.

G. Marginal/Wilson extraction; Gaussian determinant and sharp chi; R/B and large fields; original CMP109 Eq(0.29),(5.37),(5.42) images; complete cutoff/volume Cauchy, OS reconstruction and physical mass gap: all OPEN and independent.

## 5. Two negative controls

1. SAME DOMAIN BUT DIFFERENT BACKGROUND: K(u)=1/(1+u) on a one-site positive matrix. K(0)=1, K(1)=1/2 with no domain defect. This falsifies any inference "domain Theorem3.14 => all two-history operator differences exponentially small."

2. CONTRACTION WITHOUT UNIFORM MARGIN: let F_(N,0)(x)=(1-1/N)x and F_(N,1)(x)=(1-1/N)x+1/N (N>=2). Both maps contract; their input difference is only 1/N, but their fixed points are x0=0,x1=1. Thus even exact per-N contraction plus vanishing input motion does NOT imply vanishing output motion without a common q<1 or a quantified alternative. Not a model of actual Bałaban dynamics.

## 6. Determination and next cursor

SOURCE-TEXT-WITNESS RECOVERED:
- CMP99(3) Thm3.14/Eq(3.154) two-DOMAIN spatial marked Green operator difference, with random-walk cancellation;
- CMP99(3) Thm3.15/Eq(3.185) constrained covariance expansion and single-background decay;
- CMP116 (1.2)–(1.11) nonlinear fast-field fixed points, weakened propagators and source complex analytic construction.

CERTIFIED ABSTRACT UNDER EXPLICIT HYPOTHESES:
- exact domain motion vs bulk/background coefficient difference (R103.2);
- nonlinear fixed-point endpoint stability (R103.5)-(R103.8), with uniform contraction denominator explicit;
- examples obstructing history suppression from domain-only marks and nonuniform contraction.

CONDITIONAL NATIVE:
- actual current operator/gauge/background carrier common to cutoff trajectories;
- marked constrained covariance, background and cutoff transport;
- weighted q<1, nonlinear source map Lipschitz estimates and marked random-walk Cauchy sum;
- rooted history relative Delta E_k, full polarization mixed second moment and beta; Eq029 UV excess.

NO native history-response, exact cutoff beta covariance, positive-alpha residual or mass-gap theorem has been newly certified.

YM-R104 (UNCONSUMED): audit whether CMP99(3) source *background analytic derivative estimates* supply a true local parameter-Lipschitz bound, and whether the original source random-walk expansions can be marked by a BACKGROUND DIFFERENCE rather than solely a DOMAIN DIFFERENCE, for the CMP116 H,G,H0 fixed-point consumers. Separately demand a native actual-cutoff common gauge/carrier map; do not generate further untyped transfer lemmas. Original CMP109 equation image hold persists. Highest reference [92], next [93].
