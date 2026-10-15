# YM-R102 — CMP116 Lemma-1 frozen-localization linearity / two-history operator-motion separation

Date: 2026-10-14
Repository: monocap-tech/yangmills
Prior verified head: YM-R101 13c686dd138c963b2a1e11721b849f0b6a73434a
Status: COMPLETE AS SOURCE-TEXT STRUCTURAL LINEARITY AUDIT AND CONDITIONAL RELATIVE-TRANSFER THEOREM; NATIVE TWO-CUTOFF BOUND OPEN
Next cursor: YM-R103 (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM. No four-dimensional continuum YM construction, Osterwalder–Schrader continuum or positive mass gap.

## 0. Target and evidence boundary

R101 recovered the single-trajectory CMP109 inherited E_k -> CMP116 Lemma1 V'_k(Y) -> Lemma2 full V_k(Y) -> Mayer (2.1) -> H(Z) -> connected-log chain from an accessible third-party paper transcription. R102 asks a STRICTLY narrower question: when does the Lemma1 inherited-activity localization commute with subtraction of two histories, and what separate defect appears if the source operator/chart changes?

Preflight confirmed repository main = YM-R101. The relevant primary bibliographic source is reused [21] T. Bałaban, CMP 116 (1988), 1–22, DOI 10.1007/BF01239022; the actual third-party OCR primary-paper text inspected was:
  https://github.com/chboishabba/dashi_agda/blob/master/Docs/support/reference/balaban-source-extracts/cmp116-effective-actions-part-ii.txt
  Git blob: 2de28469578fcdc14270f57516b190234f9c8812
The same external source packet README expressly says these text/OCR files are NOT replacements for original PDFs. Exact signs, numeric constants and normalization remain original-image-unverified. Reference [7] CMP109 original Eq(0.29)/(5.37)/(5.42) image hold persists. No new bibliographic source is consumed; highest cumulative [92], next [93].

## 1. Source-visible mechanism: weakening differentiates a FROZEN analytic input linearly

CMP116 Section 1 text supplies a detailed apparatus:
- printed pp2–3 (OCR lines 56–105): source function E(X,U,J,A), localized before substitution of nonlinear H_k(B'), with H_k determined by propagators and the separate variational/background equations (1.2)–(1.5);
- printed pp3–4 (OCR lines 127–157): define weakened propagators H(s),G(s),H0(s), which equal original operators at s=1, then apply the fundamental theorem of calculus (1.9) to the analytic source expression after the substitution;
- printed pp4–5 (OCR lines 159–211): derivatives outside the connected component containing the original source cube vanish, yielding a connected-domain localization indexed by Y0 and (1.10);
- printed pp5–8 (OCR lines 209–379): Cauchy bounds on derivatives with respect to s, the source tree/domain entropy sums (1.26), and resulting individual localized activity (1.29);
- printed pp9–10 (OCR lines 430–445): Lemma1 Eq(1.33), the historical E_k difference is represented by sum_Y V'_k(Y), with source domain (1.34)/(1.35) and a single-trajectory absolute bound (1.36).

Crucial detail: the weakening and nonlinear field map Phi_(sigma,s)(U,B), once FIXED, is an ARGUMENT SUBSTITUTION independent of the test activity F being inserted. Composition F -> F(Phi) is linear as a map of F. The weakening derivatives d_(sΔ), their finite integrals, sums over a fixed index family, and any fixed linear Taylor/Ward extraction are also linear in F. The variational/minimizer map may itself be nonlinear in propagators or background fields without destroying this EXTERNAL linearity in F.

This is SOURCE-SHAPED AND MATHEMATICALLY DERIVED, not a claim that CMP116 prints a freestanding bounded linear operator between two full-history Banach spaces. The paper does not assert a new uniform two-history Lipschitz estimate; nor have all auxiliary analytic extensions and weakened paths been proven identical between different cutoff trajectories.

## 2. Precise abstract finite/absolutely convergent localization theorem

Let B_in be a vector space of source analytic activity families F=(F_X), each defined on a common source complex domain. Fix a source apparatus sigma consisting of:
  - same background U,J and current g_k, gauge chart and B fast-variable carrier;
  - same weakener index sets I_(Y,X), localized propagators, weakened nonlinear substitution maps Phi_(sigma,i,t);
  - same integration contours and analytic extensions, and the same indexing/anchoring conventions.
For each Y define
  (L_sigma F)_Y
   := sum_X sum_(i in I_(Y,X)) int_(T_i)
        a_(Y,X,i)(t) [d_(t_1)...d_(t_m) F_X(Phi_(sigma,i,t))] dt,  (R102.1)
where a_(Y,X,i)(t) is fixed (independent of F), each integral exists and sums converge absolutely in the intended norm. Terms with m=0 are permitted.

The operator L_sigma is LINEAR:
  L_sigma(F1-F0)=L_sigma(F1)-L_sigma(F0).                           (R102.2)
Proof: composition with a FIXED Phi, ordinary differentiation, integration and convergent summation are linear in F. No assumption that Phi is linear in U,B, or s is required.

Source interpretation: (1.9)–(1.10) and Lemma1 (1.33) exhibit this grammar for EACH source analytic term of the inherited E_k DIFFERENCE. To identify the complete paper V'_k(Y) with L_sigma(E_k), one must preserve the chosen decomposition/analytic extension, the finite-to-infinite summation prescription and normalization. This is a CONDITIONAL SOURCE IDENTIFICATION even though structural linearity of its building operations is established.

## 3. Two-history EXACT decomposition: input variation versus operator motion

For two endpoint histories let E_0,E_1 have been transported to a COMMON source activity space and let sigma_0,sigma_1 denote their full current localization apparatus (same output index family or an explicitly constructed common refinement). Then algebra gives
  L_(sigma1)E_1-L_(sigma0)E_0
      = L_(sigma1)(E_1-E_0)+(L_(sigma1)-L_(sigma0))E_0.           (R102.3)

First term = relative inherited-source input localized by a frozen apparatus.
Second term = MOVING LOCALIZATION OPERATOR defect, including changes to weakener propagators, background maps, analytic extensions, site/cube/root indexing and source coordinate transport.

If histories are on different integration spaces and NO source-defined common comparison transport exists, neither R102.3 nor its norm is yet native/well-typed. A formal label (N,j)->(N+1,j+1) with equal physical a is insufficient.

Example showing the second term is essential even with ZERO input defect: take scalar F0=F1=f(z)=z, Phi0=0, Phi1=1 and L_sigma f=f(Phi_sigma). Then E1-E0=0, but L_sigma1 E1-L_sigma0 E0=1. No statement about Bałaban's actual source history motion follows from this toy example.

An additional difference can arise BEFORE L if extracting source representations from two E_k uses different nonlinear source decomposition choices or different current Wilson/marginal counterterm conventions. These must be represented as part of sigma or as a separately declared source input; they are not silently cancelled.

## 4. Conditional weighted Lipschitz transfer with exact missing hypothesis

For common normed activity spaces B_in and B_out, if
  ||L_sigma||_(B_in->B_out) <= M
uniformly for all relevant cutoff depths, source gauge/volume/chart and admissible current couplings, then for a FROZEN common apparatus
  ||Delta V'_k||_out <= M ||Delta E_k||_in.                       (R102.4)

For two moving apparatuses satisfying a comparison norm bound
  ||L_sigma1-L_sigma0|| <= eta_(N,k)
on B_in,
  ||Delta V'_k||_out
   <= M ||Delta E_k||_in + eta_(N,k)||E_(k,0)||_in.              (R102.5)

Proof: apply (R102.3) and triangle inequalities.

For actual CMP116 one may choose entropy-inclusive rooted analytic/polymer norms retaining exponential domain/tree weights and a common source complex collar. Then obtaining M uniform is NOT just continuity of an individual L_Y: one needs absolute termwise positive majorants with fixed contour radii, field restrictions and D_k/cube entropy, as in CMP116 (1.24)–(1.29), WITH THE INPUT DIFFERENCE in the same admissible norm. If the proof provides an input-weighted estimate
  |Delta F_X(Phi_(sigma,s))| <= epsilon_N A_X
uniformly on every weakened complex path, all fixed linear operations in R102.1 can carry epsilon_N through a source-uniform positive majorant, provided the resummation constants and Banach norm are established.

Missing NATIVE quantitative inputs are explicit:
  (I) ||Delta E_k||_in <= epsilon_(N,k) with summable UV budget,
  (II) ||L_sigma1-L_sigma0|| <= eta_(N,k) with source-normalized summable motion budget,
  (III) gauge, coupling, domain and source-index transports making (I),(II) meaningful.
No numeric epsilon, eta, power alpha, or uniform operator norm is claimed here. The SOURCE single-trajectory bound on V'_k in Lemma1 (1.36) is an ABSOLUTE value on a generated family, not a bound on the operator norm of L over all admissible input differences.

## 5. The genuinely NONLINEAR stage begins after the pre-Mayer potential

Even at a fixed apparatus, Lemma2 adds the current Gaussian/perturbative source family and defines V_k(Y). If current terms P^(k) are held fixed, the inherited-part comparison is linear at the V'_k stage, and Delta V_k equals Delta V'_k under a truly common Lemma2 decomposition. If P or the source quadratic normal form changes, a new DeltaP contribution is mandatory.

The next Mayer map V_k(Y) -> w_Y=e^(V_k(Y))-1 is NONLINEAR, although the exact difference identity R101.3 bounds it by Delta V times an exponential majorant on a common Y carrier. Subsequent Gaussian conditioning, weakening, polymer exponentiation and connected-log activity maps are also nonlinear in the potential family. R83–R93 provide conditional differences/marked KP transfers for these stages and do not close them from the linearity of Lemma1.

CMP116 (2.3) separately decomposes sharp chi_k; a common fixed L does not imply chi_1=chi_0. R99/R100 demonstrate cutoff changes can create a nonzero polarization jet with Delta E=0. The constrained covariance/normalization and background Green maps may also move, as in R78–R82.

CMP109 Eq(0.29)'s final irrelevant V^(j)(X) is an OUTPUT of Taylor/Ward/marginal subtraction. CMP116 V'_k and V_k(Y) are BEFORE Mayer and before the full effective-action extraction; do not identify them or infer Eq(0.29) alpha from their linearity.

## 6. Negative controls and epistemic status

(A) UNMARKED OUTPUT DOES NOT GIVE RELATIVE INPUT LIPSCHITZ. A scalar source family can be restricted to f_N=1/N, with L_N(f)=N f. Then |L_N f_N|=1 at every N, but the operator norm ||L_N||=N diverges. A theorem bounding generated |L_N f_N| by a fixed absolute constant says nothing about uniform M on differences. The example is abstract, not a model of the CMP116 actual operator.

(B) HISTORY ALIGNED SPACING DOES NOT GIVE IDENTICAL SIGMA. Equal a_(N,j) and a_(N+1,j+1) does not imply equality of the source propagators, cutoff masks, constraint coordinates, or inherited normalization.

(C) SOURCE LINEARITY DOES NOT GIVE HISTORY AGE GAIN. For fixed identity localization L(F)=F, a historical difference of size O(1) stays O(1); spatial locality of the map supplies no theta^(j-s). The dynamical estimate of R98/R99 or a directly summable endpoint defect is still required.

(D) INTERPOLATION IN AN INPUT VECTOR SPACE IS NOT AN INTERPOLATION OF CANONICAL RG HISTORY. R102.2 uses purely algebraic linearity even when F1-F0 does not itself satisfy the paper's original positivity/admissibility conditions. Quantitative estimates for that signed difference still require both inputs to admit common analytic extensions and a linear source Banach domain containing their difference. One cannot invoke the paper's SINGLE-TRAJECTORY theorem for an unphysical signed input without verifying this extension.

## 7. Determination and next cursor

SOURCE-TEXT-WITNESS: CMP116 weakened propagator definitions (1.6)–(1.9), connected localization (1.10), Cauchy/rooted sum (1.24)–(1.29), Lemma1 inherited E_k (1.33)–(1.36). The underlying weakened substitution Phi is fixed during differentiation of a given source analytic E-term; full source identification and exact formulas remain OCR/image sensitive.

CERTIFIED ABSTRACT: frozen-apparatus localization linearity (R102.1–R102.2); two-history operator-motion decomposition (R102.3); conditional Lipschitz transfer (R102.4–R102.5); counterexamples to forgetting sigma motion or assuming absolute bounds imply uniform operator norm.

CONDITIONAL NATIVE: identify same source analytic input representation for two histories at fixed current coupling/background/gauge chart and bounded localized operator in a rooted norm; control its movement via propagator/minimizer/domain differences.

OPEN: relative historical ||Delta E_k||; summable motion eta_(N,k); rooted two-background CMP116 potential response; marginal/Wilson subtraction, covariance/cutoff/large-field channels; original Eq(0.29)/(5.37)/(5.42) image confirmation and positive-alpha output dictionary; continuum existence/OS/gap.

YM-R103 (UNCONSUMED): isolate the SHARPEST SOURCE OWNED QUANTITATIVE INPUT for motion of weakening kernels H,G,H0 under a two-cutoff comparison, distinguishing spatial domain discrepancy (CMP99(3) Theorem3.14/(3.154)) from inherited coupling history. Determine whether a source-derived marked operator DIFFERENCE propagates through the nonlinear H_k fixed-point/minimizer map in (1.2)–(1.5) with uniform Lipschitz constants, without claiming that ordinary spatial kernel locality produces history-age suppression. If not accessible, record a hard native source-deficit rather than assuming eta_N. Keep direct original image receipt open.

Highest numbered reference [92], next [93]; no continuum YM or mass-gap proof.
