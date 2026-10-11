# YM-R85 — Kotecky-Preiss marked polymer difference / connected-log UV budget audit
Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior checkpoint: YM-R84 b5bc022bf75e67d4ebe7311dfe6ebae84ff497f6
Status: ABSTRACT TRANSFER CLOSED; NATIVE YANG-MILLS GATES OPEN
Next unconsumed cursor: YM-R86
Claim discipline: UNPROVED RESEARCH PROGRAM. No continuum Yang-Mills, OS axioms or positive mass gap.

## 1. Source/evidence recovery

YM-R50 previously source-audited CMP116 [21] Sect.2: connected H(Z) supplies the hard-core polymer gas (2.11); the connected logarithmic expansion follows separately (2.12)-(2.13). YM-R47 located complex field-uniform CMP116 estimates on the source U^c domain. YM-R84 showed two marked derivatives follow from a ROOTED ANALYTIC CONNECTED-LOG DIFFERENCE norm E_N, but did not derive E_N from a difference of the pre-exponent H(Z).

New external general reference [87]: R. Kotecky and D. Preiss, *Cluster expansion for abstract polymer models*, CMP 103 (1986), 491-498, DOI 10.1007/BF01211762. The publisher record identifies the original; a peer-reviewed 2026 CMP theorem (Thm 4.2) explicitly states weighted KP convergence and rooted cluster estimates. It does NOT verify native cross-cutoff CMP116 hypotheses.

Original Bałaban CMP109 [7] Eqs (5.37),(5.42),(0.29) still inaccessible from public Project Euclid / Springer page views in this pass: original PDF equation windows NOT independently read. Previous [85] is secondary only. No primary Eq(0.29) alpha is promoted.

## 2. Finite hard-core polymer coefficientwise difference theorem — ABSTRACT-DERIVED

Let P be a finite family of nonempty connected polymers on a bounded-degree site graph, incompatible when their supports overlap or are at distance <=1. Assign holomorphic weights w_i(gamma,b), i=0,1, on the SAME background polydisc radius r>0, with a source-justified common polymer index/carrier. Define
  p_gamma=max(sup_b|w_0(gamma,b)|, sup_b|w_1(gamma,b)|),
  d_gamma=sup_b|w_1(gamma,b)-w_0(gamma,b)|.
Take the interpolation w_s=(1-s)w_0+s w_1; |w_s|<=p throughout.

For an ordered n-polymer tuple with connected incompatibility graph define its Ursell coefficient phi_T(gamma_1,...,gamma_n). Use the conventional 1/n! cluster series
  F_i(b)=log Z(w_i;b)=sum_(n>=1) 1/n! sum_(gamma_1,...,gamma_n) phi_T product_j w_i(gamma_j,b).
All identities below require uniform absolute convergence; this is insured if a suitable common strict weighted KP majorant is proved. Merely knowing both endpoints separately converge is not enough.

For each tuple, telescope the product:
  |product_j w_1(gamma_j)-product_j w_0(gamma_j)|
  <=sum_(i=1)^n d_(gamma_i) product_(j neq i) p_(gamma_j).
By exchange symmetry the factor n cancels n!, producing a polymer-marked series with coefficient 1/(n-1)!.

For nu>0 define the explicit CHECKABLE rooted susceptibility
  T_(nu,p)(gamma)
    =sum_(n>=1) 1/(n-1)! sum_(gamma_2,...,gamma_n)
       |phi_T(gamma,gamma_2,...,gamma_n)|
       product_(j>=2)[p_(gamma_j) exp(nu |gamma_j|)].
Assume it is finite and T_(nu,p)(gamma)<=exp(a_gamma) with a_gamma>=0 uniformly in the background. A sufficiently strong weighted KP hypothesis can supply such a bound, but R85 DOES NOT infer it merely from the unweighted CMP116 H(Z) estimate.

If a cluster contains a marked gamma and its union X is connected, tree length ell(X) is at most sum_j |gamma_j| in this overlap/adjacency geometry. Thus weighting by exp(nu ell(X)) is dominated by the product exp(nu |gamma_j|). Fix a designated anchor a(gamma) belonging to the marked gamma and collect each marked product-difference term by this anchor and the union X. The resultant connected-log difference activities h_(z,X)(b) satisfy
  sup_z sum_(X contains z) exp(nu ell(X)) sup_b |h_(z,X)(b)|
  <=sup_z sum_(gamma:a(gamma)=z) d_gamma exp(nu |gamma|) T_(nu,p)(gamma)
  <=delta,
  delta:=sup_z sum_(gamma:a(gamma)=z) d_gamma exp(nu |gamma|+a_gamma).
This is a valid absolute-coefficient majorant: no cancellation, unknown cluster signs or division by possibly zero w_gamma are used. Its connected support is the union of the constituent polymers; a common halo R for background-variable dependence must be verified separately if needed for source application.

In short:
  CommonWeightedKP + AnchoredPreExponentActivityDifference(delta)
  => AnchoredConnectedLogDifference(E <= delta).
The cluster expansion also supplies a holomorphic log Z_s on the whole common polydisc and all s, so Z_s=exp(F_s) is zero-free there. This resolves the abstract interpolation zero-free gate UNDER common KP, not for an unverified native interpolation.

## 3. Two marked background derivatives — coupling to YM-R84

Assume the log activities have background-variable support inside a fixed radius-R neighborhood of their connected spatial union X; uniform common analytic radius r and polymer geometry as above. R84 then gives
  |rooted DeltaGamma_xy from anchor z|
    <= [2 exp(nu R)/r^2] delta exp[-nu/2(d(x,z)+d(y,z))].
With k_N the deterministic source K-counterterm second moment,
  ||DeltaGamma_N||M2
    <= k_N + [8 exp(nu R)/r^2]S0(nu/2)S2(nu/2) delta_N,
where S_j are the usual finite 4D exponential lattice moments.

This is a mathematically derived conditional chain from a PRE-EXPONENT difference norm to a CONNECTED LOG two-mark difference; the link missing in R84 is now an explicit finite-polymer theorem with a clear uniform KP source gate.

For a physical fixed-volume cutoff comparison, a source-native per-UV-root d_gamma budget of a_N^(4+alpha) with root count O(a_N^-4) would give O(a_N^alpha), assuming the rooted weight, a_gamma, source projection and scale factors remain uniform. The factor alpha>0 must come from a native primary source estimate and the actual one-layer/marginal-subtracted dictionary. No epsilon or exponent is invented by KP.

## 4. Boundary counterexamples

(a) Near an activity zero the log is not uniformly Lipschitz. For one polymer Z=1+w, choose w0=-1+epsilon, w1=-1+2epsilon, epsilon>0 small. Then |Delta w|=epsilon->0 but logZ1-logZ0=log2. A common convergence/zero-free margin is essential; endpoint nonzero partition functions do not suffice.

(b) A common KP margin alone does not produce UV suppression. One single-site polymer with w_0=0, w_1=constant small c>0 satisfies a strict KP condition at every N but has a nondecaying logZ difference log(1+c). The required delta_N summability is independent.

(c) A source per-root V^(j) estimate cannot directly be identified with the activities w_1-w_0 until marginal subtraction, normalization and first-common-scale comparison are proved. Moreover CMP116 H(Z) is not equal to the pre-exponent activity of an arbitrary synthetic interpolated gauge theory without a source chart.

## 5. Status and next frontier

ABSTRACT-DERIVED: coefficientwise marked activity telescoping; under a declared rooted KP susceptibility, transfer to a connected-log rooted analytic difference norm; composition with R84 two-mark moment estimate; common uniform analytic cluster convergence supplies zero-freeness; two negative controls.

GENERAL SOURCE-CITED: weighted KP polymer convergence [87], as theorem framework, NOT native Yang-Mills source closure.

PREVIOUSLY SOURCE-LOCATED: native CMP116 pre-exponent connected H(Z) and subsequent cluster log (YM-R50), native complex field-uniform termwise bound (YM-R47).

OPEN NATIVE:
1. Instantiate w_0,w_1 as the actual CMP116 H(Z) connected polymer weights on common physically aligned source coordinates, respecting different UV shell dimensions, gauge, boundary and localization.
2. Verify an INTERPOLATION-UNIFORM strong weighted KP majorant in the original source analytic collar, including derivative and root support geometry, rather than just individual endpoint one-step bounds.
3. Prove the anchored pre-exponent cutoff-difference budget delta_N has a positive UV excess with correct 4D root counting, or prove an alternative summable bound.
4. Read primary CMP109 (5.37),(5.42),(0.29), the actual V^(j), beta/F2 subtraction and first-common-scale extra-layer dictionary; source [85] insufficient.
5. Keep deterministic counterterm k_N and full Pi/Ward/momentum normalization, as well as independent P2M Schur exact Lean provenance [86].

Next unconsumed YM-R86: audit the native CMP116 Lemma-3 activity bound for a common weighted KP margin and explicit *difference* dependence (not just per-step norm); seek an original-source positive-alpha one-layer bound that converts into delta_N, including boundary and marginal/counterterm channels. Test whether the weighted KP margin is implied by the already-audited source smallness or requires a genuinely stronger hypothesis.

No four-dimensional continuum Yang-Mills or mass-gap theorem follows.
