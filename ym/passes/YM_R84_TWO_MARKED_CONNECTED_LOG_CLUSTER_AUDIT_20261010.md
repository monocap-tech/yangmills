# YM-R84 — two-marked connected-log polymer norm / analytic collar audit

Date: 2026-10-10
Previous head: YM-R83 checkpoint d628f0c436ab16606a9d4d2312993d01224d4889
Status: COMPLETE AS ABSTRACT THEOREM AND SOURCE-SCOPE AUDIT; native R75 gates OPEN
Next cursor: YM-R85 (unconsumed)
Claim status: UNPROVED RESEARCH PROGRAM; no four-dimensional continuum Yang-Mills or mass gap.

## 1. Source scope: H(Z) is pre-exponentiation, not the log itself

The prior primary-source audits have now been reread. YM-R50 records CMP116 [21] Sect.2 as:
- D/Y0/P/Z0 localization and conditioned product Gaussian integral (2.1)-(2.6);
- second weakening localization H(Z,Z0), H(Z), (2.8)-(2.9);
- connected-component factorization H(Z)=product H(Z_i) in (2.10);
- hard-core polymer gas (2.11) followed by exponentiated connected cluster expansion (2.12)-(2.13);
- analyticity and single-term estimate (2.14)-(2.26), with D/P/Z0/Z0' resummation to Lemma 3/(2.38).

Thus a two-background derivative of a PRE-EXPONENT H(Z) is not automatically a two-background derivative of log of the full one-step integral. A distinct connected-log activity representation must be obtained via actual exponentiation, with compatible source variables. The source proves a one-trajectory cluster architecture; a cross-cutoff log-DIFFERENCE has not been source-identified.

YM-R47 already reports direct prior primary-page inspection of CMP116 printed pp.15–17: activities are analytic on U^c_(k+1)(X,alpha0,alpha1); source estimates including (2.16),(2.21),(2.22),(2.26) are field-uniform under the native parameter hierarchy. The separate CanonicalUjcEmbedding into a source-allowed fixed complex collar remains a source/coordinate gate. No radius is invented in R84.

New web check: original publisher article DOI 10.1007/BF01239022 confirms the Part-I fluctuation integral is represented by an exponentiated cluster expansion but displays subscription preview, not equation pages. Project Euclid .full/.pdf gave iframe-only HTML. No fresh original source equation (5.37),(5.42),(0.29) of CMP109 was retrieved. Source [85] remains a secondary locator. Repeat bibliography [7],[21],[59],[85],[86]; highest [86], no new source number.

## 2. TwoMarkedCauchyTreeTransfer — ABSTRACT-DERIVED

Work on a finite nearest-neighbor subset of Z^4, with graph l1 distance. Let z be a root, X a finite connected polymer containing z, and ell(X) a connected edge-tree length. Let h_(N,z,X)(b) be a holomorphic CONNECTED-LOG difference activity on a common complex coordinate polydisc of radius r>0, depending only on background coordinates in the R-neighborhood of X. Assume the logarithmic effective action difference has an ABSOLUTELY and locally uniformly convergent representation
   Delta Gamma_N(b) = Delta K_N(b) + sum_z sum_(X connected, z in X) h_(N,z,X)(b),
with the chosen anchoring counting each term exactly once. This representation is an ASSUMPTION, not the source CMP116 H(Z) statement.

Suppose for some nu>0 the complete entropy-inclusive ROOTED analytic norm is bounded:
   E_N := sup_z sum_(X connected,z in X) exp(nu ell(X)) sup_polydisc |h_(N,z,X)| < infinity,
uniform in N, fixed-volume geometry and the source-allowed chart.

Cauchy's estimate for the mixed coordinate derivative gives
   |partial_bx partial_by h_X(0)| <= (2/r^2) sup_polydisc |h_X|,
where the factor two covers x=y. Derivatives vanish when x or y is outside the R-neighborhood of X.

Whenever both derivatives can be nonzero, connectivity of X gives
   d(x,z)+d(y,z) <= 2 ell(X)+2R,
and hence ell(X) >= (d(x,z)+d(y,z))/2-R.
Consequently
   |sum_X partial_bx partial_by h_(N,z,X)(0)|
      <= (2 exp(nu R)/r^2) E_N
           exp[-(nu/2)(d(x,z)+d(y,z))].

Let S0(kappa)=sum_(u in Z4)exp(-kappa|u|_1), S2(kappa)=sum_u |u|_1^2 exp(-kappa|u|_1), both finite for kappa>0. With kappa=nu/2 and
   k_N=sup_x sum_y d(x,y)^2 |partial_bx partial_by Delta K_N(0)|,
R83's spatial summation now yields
   ||Delta Gamma_N||_(second moment)
      <= k_N + [8 exp(nu R)/r^2] S0(kappa) S2(kappa) E_N.

Thus SUM_N(k_N+E_N)<infinity is a sufficient abstract criterion for a summable two-marked response after linked-cluster exponentiation. The norm E_N already contains ALL rooted polymer entropy, so no additional animal-counting constant needs to be guessed. Uniformity of r,R,nu and the physical source normalization is essential.

This establishes a rigorous CONSUMER for the missing primary quantitative estimate; it does NOT show CMP116 H(Z) satisfies E_N, and it does NOT identify the background derivative with source beta/F² extraction.

## 3. Analytic exponentiation can discharge the separate zero-free check, but only when established uniformly

If for every interpolation parameter s and every background b in the common source complex domain one has an EXACT identity
   Z_s(b) = exp(F_s(b))
with F_s a locally uniformly convergent holomorphic connected-cluster sum, then Z_s is nonzero everywhere on that domain and its log branch is F_s. This is immediate from the exponential and removes a *separate* zero-free hypothesis in that case.

CMP116's single-step exponentiation is not by itself an interpolation-uniform cross-cutoff identity. To use it for R83, prove the complete interpolated family is within the same analytic cluster-convergence class and source normalizations, including all deterministic counterterms. Endpoint exponentiation does not imply this.

A one-polymer sanity check: if Z=1+h(b) with h=a+delta b_x b_y, then at b=0 the mixed derivative of h is delta, whereas the mixed derivative of log Z is delta/(1+a). This differs even for harmless small a and can blow up if a approaches -1. Therefore pre-exponent H derivative must NOT be equated with a log-partition polarization derivative.

## 4. Ultraviolet summability is still an independent numeric power gate

The previously traced (but NOT original-primary-verified) candidate CMP109 Eq (0.29) is schematically per-root ||V^(j)(X)|| <= C a^(4+alpha) exp(-kappa tree), alpha>0. Under an actual first-common-scale one-layer dictionary and a uniformly rooted summable norm on a fixed physical four-volume with O(a^-4) roots, this would leave O(a^alpha). But an activity estimate on V^(j) does NOT automatically become E_N for the linked-cluster LOG difference; source marginal subtraction and cross-cutoff normalization need proof.

Uniform analyticity and exponential locality do not imply E_N summability: take a single-site connected analytic activity h_(N,z,{z})(b)=N^-1 b_z^2, with r fixed. It has trivial tree length and perfect spatial locality, but sum_N E_N diverges. Conversely source couplings g_N need not yield a geometric a^alpha simply because they are weak.

The missing source input is therefore a CROSS-CUTOFF exponentially weighted rooted analytic bound for connected logarithmic response activities carrying positive cutoff-distance excess after 4D root count. This is stronger and more sharply typed than CMP116's existing one-step H(Z) field-uniform bound.

## 5. Evidence classification and YM-R85

ABSTRACT-DERIVED:
- two-mark Cauchy/tree bound from a rooted analytic CONNECTED LOG activity norm;
- uniform second-moment transfer with explicit constant 8 exp(nu R) S0 S2/r²;
- analytic uniform exponentiation implies interpolation zero-freeness;
- pre-exponent vs log derivative counterexample;
- locality and fixed collar alone do not imply UV summability.

PREVIOUSLY SOURCE-LOCATED: CMP116 analytic source domain field-uniformity (R47), native H(Z) construction and later exponentiation (R50), original single-step localization/resummation estimates [21]. No fresh CMP116 equation-page verification.

OPEN PRIMARY/NATIVE:
1. Show a CMP116-source-compatible comparison of TWO cutoff trajectories actually induces an analytic connected-log activity difference with the stated anchored support and rooted norm.
2. Establish uniform complex radius and cluster convergence on the entire needed interpolated family (or bypass interpolation by a direct source endpoint comparison).
3. Prove E_N has a summable UV scale factor and k_N is summable with correct physical momentum/density normalization.
4. Original CMP109 Eqs (5.37),(5.42),(0.29), the V^(j) definition, positive alpha and first-common-scale marginal subtraction and one-layer dictionary.
5. Correct full Pi/Ward/F² source projection and P2M Schur UUID [86] provenance.

NEXT CURSOR YM-R85 (UNCONSUMED): verify the precise CMP116 connected-cluster log activity and analyticity/derivative norms after exponentiation; test whether a cross-cutoff extra-layer insertion can be represented with a source-owned root and obtain a physically normalized positive-alpha E_N from original CMP109, without confusing pre-exponent H(Z) with connected-log contributions. If no primary source text, preserve the source-access boundary and test conditional alternatives rather than inventing an alpha theorem.

No continuum Yang-Mills, Osterwalder-Schrader reconstruction or mass-gap claim.
