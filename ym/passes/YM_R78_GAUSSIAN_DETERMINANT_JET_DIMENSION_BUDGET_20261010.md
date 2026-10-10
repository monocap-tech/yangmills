# YM-R78 — full Gaussian second-jet completion / determinant dimension-budget audit

Date: 2026-10-10
Prior head: YM-R77 (00c1df5903848bb172320c781e23745e34fd8715)
Repository: monocap-tech/yangmills
Status: COMPLETE AS BOUNDED ABSTRACT AUDIT; PRIMARY YM GATES STILL OPEN
Next unconsumed cursor: YM-R79
Claim status: UNPROVED RESEARCH PROGRAM; no continuum four-dimensional Yang–Mills or positive mass-gap assertion.

## 0. Actual cursor and source-evidence check

At start, repository main head was 00c1df5903848bb172320c781e23745e34fd8715, with live_cursor=YM-R78 and live_cursor_consumed=false. R77 identified the second-spatial-moment criterion for a Fourier polarization jet and proved unweighted operator norm insufficient. R76 separately showed a positive Schur reduced Hessian cannot control the fluctuation log determinant.

Primary source verification attempted again. Bałaban, CMP 109 (1987), DOI 10.1007/BF01215223, is directly attested by Rutgers bibliographic metadata and publisher descriptions. The Project Euclid article full and pdf paths at /cmp/1104116842.full and /cmp/1104116842.pdf returned iframe-only HTML, not readable article equations. Direct downloadable original PDF was not recovered. No local original CMP109 PDF was found in the current conversation container/file search; another public group's claim to have local primary PDFs is NOT transferable primary text. Therefore (5.37), (5.42), (0.29) remain UNINSPECTED in this pass. No source-specific formula is promoted from secondary [85]. Existing [7], [59], [85], [86] are reused; highest reference remains [86]; no [87] created.

This pass advances the abstract mathematical interface despite this source-access obstruction. It must not be misrepresented as recovering the native one-step vacuum-polarization tensor Pi or its source decomposition.

## 1. Exact finite Gaussian determinant contribution — ABSTRACT-DERIVED

On finite-dimensional real inner product spaces for retained r and eliminated e, let
  H(t) = [[A(t), B(t)], [B(t)*, C(t)]],
with C(t) symmetric positive definite in an open parameter neighborhood. The Gaussian measure is the one corresponding to the indicated quadratic form and Lebesgue measure in the eliminated coordinates, with no parameter-dependent Jacobian included.

Complete the square:
  1/2 <(r,e),H(r,e)> =
  1/2 <r, S(t) r>
    + 1/2 <e + C^-1 B* r, C(e + C^-1 B* r)>,
  S(t)=A(t)-B(t)C(t)^-1 B(t)*.

Integrating e over R^m gives
  integral exp(-1/2 <(r,e),H(r,e)>) de
    = (2pi)^(m/2) (det C(t))^(-1/2) exp(-1/2 <r,S(t)r>).
Therefore the Gaussian contribution to the effective action is
  Gamma_G(r,t) = (1/2)<r,S(t)r> + (1/2)log det C(t) -(m/2)log(2pi).

If C and the chart depend on external background fields, the determinant term contributes to their quadratic coefficient even when S is unchanged. This is exactly the obstruction from R76, now isolated as a quantitative separate target. When the integration density has a parameter-dependent Jacobian, an ADDITIONAL log-Jacobian term must be kept; the displayed expression does NOT include it.

Gauge zero modes exclude applying this identity on the unconstrained gauge orbit; an actual finite gauge-fixed carrier with strict invertibility is required. Complex contours likewise need separate analytic coercivity.

## 2. Mixed derivative and normalized log-determinant sensitivity theorem — ABSTRACT-DERIVED

Let C_i(theta), i=0,1, be C^2 maps in two real parameters theta_mu,theta_nu near 0, with common eliminated dimension m, common Euclidean coordinate identification, and C_i(0)>=c I for c>0.

At theta=0 put
  X_i=C_i^-1,
  P_i=partial_mu C_i,
  Q_i=partial_nu C_i,
  R_i=partial_mu partial_nu C_i.
Suppose ||P_i||,||Q_i|| <= K1 and ||R_i|| <= K2, for i=0,1.
Define differences
  delta0=||C_1-C_0||,
  delta_mu=||P_1-P_0||,
  delta_nu=||Q_1-Q_0||,
  delta_munu=||R_1-R_0||.
All operator norms refer to identified finite-dimensional Hilbert spaces.

Jacobi's formula and differentiation of X give
  partial_mu partial_nu log det C_i
   = Tr(X_i R_i - X_i P_i X_i Q_i).

Claim. For f_i(theta)=(1/(2m))log det C_i(theta),
  |partial_mu partial_nu(f_1-f_0)(0)| <=
     (1/2)[ delta_munu/c
         + K1(delta_mu+delta_nu)/c^2
         + (K2/c^2 + 2 K1^2/c^3)delta0 ].

Proof. ||X_i||<=1/c. Resolvent identity gives ||X_1-X_0||<=delta0/c^2. Expand
  X_1 R_1-X_0 R_0=(X_1-X_0)R_1+X_0(R_1-R_0).
For the four-factor term telescope
  X_1 P_1 X_1 Q_1 - X_0 P_0 X_0 Q_0
   = (X_1-X_0)P_1 X_1 Q_1
   + X_0(P_1-P_0)X_1 Q_1
   + X_0 P_0(X_1-X_0)Q_1
   + X_0 P_0 X_0(Q_1-Q_0).
Use |Tr T|/m<=||T|| and the bounds to conclude. The factor 1/2 is inherited from the Gaussian effective action.

For the actual unnormalized (1/2)logdet, the RHS is multiplied by m. For a trace-per-volume convention, the physical count and density normalization must be inserted exactly as the source specifies.

Consequently, if source-native C0,C1 and their first and mixed second SOURCE/BACKGROUND parameter derivatives are aligned and controlled with sufficient summable dimension/volume budget, the Gaussian determinant jet mismatch is controlled. This lemma does not assert that the external parameters are the Fourier momenta in CMP109 Eq (5.42): that identification is OPEN PRIMARY/NATIVE.

## 3. New obstruction: small per-mode C2 error need not control the full determinant

For m>=1 define
  C_m(s,t)=exp(st/m) I_m,  C'_m(s,t)=I_m.
Every C_m is positive definite for all real s,t. At the origin
  C_m=C'_m=I,
  first s/t derivatives vanish,
  ||partial_s partial_t(C_m-C'_m)(0)||=1/m ->0.
Yet
  (1/2)partial_s partial_t logdet C_m(0) = 1/2
for ALL m, while the normalized per-mode derivative equals 1/(2m)->0.

Thus even complete smallness of the finite-dimensional block C2 DIFFERENCE in operator norm does not imply smallness of an UNNORMALIZED Gaussian determinant coefficient when the number of eliminated modes grows. The exact dimension budget cannot be omitted.

This is not a Yang–Mills counterexample; it refutes a generic shortcut that would bypass volume/root counting. In the source application the actual density or local-trace normalization must be identified before deciding which quantity is marginal.

## 4. What the full Gaussian interface now would require

On a source-identical retained/eliminated gauge-fixed finite carrier, combined with R77:
  - Schur block mismatch in a weighted, C2-compatible algebra, including inverse/locality control, yields a bound on the reduced-Hessian part;
  - the present determinant theorem bounds the Gaussian normalization jet only with matched C2 background derivatives and the dimension/trace normalization;
  - the complete Gaussian effective action is the SUM of both. Neither part by itself determines the full polarization, even at one finite cutoff.

To turn this into a beta shift estimate would further require a PROVED native dictionary:
  * Which actual source variables are used in the second derivative, and how they match p_mu,p_nu at zero momentum;
  * How the background-field/gauge Ward identities and Fourier kernel define the local F^2 projection Loc_F2;
  * Whether determinant and Schur terms exhaust the quadratic *one-step* contribution, or exactly which interaction/cumulant/measure pieces must be appended;
  * How each of these terms transforms under the physical alignment a_(N+1,j+1)=a_(N,j);
  * The correct source volume factors, momentum powers of lattice spacing, and bounds uniform in gauge-fixed slice, volume and weak coupling.

In particular the correct scalar marginal coefficient requires full Pi_j, NOT the Gaussian block alone.

## 5. R77 moment localization versus the determinant trace

R77's moment criterion was: for a translation-invariant difference kernel D_N(z),
  |partial_mu partial_nu Dhat_N(0)| <= sum_z |z_mu z_nu| ||D_N(z)||.
This controls the Fourier mixed derivative if that kernel is the ACTUAL complete normalized source tensor. The present determinant lemma is a way to bound one pre-projection component of that kernel, provided it can be expressed as a local connected kernel with quantitative spatial decay and correctly normalized trace.

It is NOT legitimate to substitute the determinant trace mismatch for the entire D_N(z), nor to infer a localized kernel from a bound on the total trace. The additional locality and finite-volume-boundary-to-bulk dictionary remains OPEN.

The minimal sufficient scalar input is actually summability of the SOURCE-DEFINED projected moment itself; absolute weighted second-moment bounds are convenient sufficient conditions, not logically necessary. Cancellation between legitimate tensor components could weaken them, but must be proven rather than assumed.

## 6. Paired Eq (0.29) remainder obligation still separate

The secondary [85] Eq (0.29) candidate is a norm on the complementary nonlinear/localized polymer activity after marginal subtraction, schematically a^(4+alpha)exp(-kappa d_j(X)), alpha>0. Neither the Schur Hessian nor determinant jet yields control of higher local vertices, contour/localization polymer expansions, or the rooted summability budgets. The R69 root-count calculation O(a^-4)*a^(4+alpha)=O(a^alpha) is CONDITIONAL on the genuine primary bound, exact object dictionary, and uniformity.

Thus:
  Gate A1 = reduced Gaussian Hessian alignment/locality (CONDITIONAL);
  Gate A2 = determinant source-jet/trace-dimension normalization (new CONDITIONAL);
  Gate A3 = non-Gaussian interaction, gauge/Jacobian, boundary/localization contributions (OPEN);
  Gate A4 = exact primary full Pi/Loc_F2 projection and summable marginal tail (OPEN);
  Gate B  = direct primary Eq (0.29) positive-alpha V^(j) activity bound and first-common-scale dictionary (OPEN).

These are a work decomposition, not proof that all pieces exist in the source with precisely this form.

## 7. Evidence status

ABSTRACT-DERIVED: finite Gaussian integration identity; mixed logdet trace formula; quantitative determinant-jet difference bound with explicit constants and factor m; counterexample to discarding mode-count factor.

CONDITIONAL-NATIVE: common gauge-fixed Hessian carrier and measure; uniform inverse and C2 derivative bounds; correct Fourier/background projection; Gaussian and non-Gaussian source decomposition; complete scale-aligned polarization mismatch.

OPEN PRIMARY: equation-level CMP109 (5.37),(5.42),(0.29), exact source norm/domain/alpha constants and derivation, full gauge/measure/normalization data.

OBSTRUCTED: unweighted small Gaussian block C2 perturbation => small unnormalized determinant jet, without volume/mode budget; Schur positivity alone => full polarization beta covariance; Gaussian jets alone => positive-alpha polymer remainder.

No Prove2Me theorem URL or Lean proof term from R76 [86] was retrieved. The elementary algebra and determinant calculation here have human-checkable proofs but are not claimed to have been formalized in Lean.

## 8. Next frontier YM-R79 (UNCONSUMED)

1. Primary CMP109 equation access: inspect original printed windows containing (5.37), (5.42), (0.29), plus nearest definitions, hypotheses and scale-dependent constants; record original page numbers and exact tensor/marginal and V^(j) types.
2. Source-native full one-step Pi ledger: classify (a) quadratic/Schur, (b) determinant, (c) vertices/cumulants, (d) gauge Jacobian/measure and (e) localization/boundary terms, without presuming that the primary decomposition follows this abstract enumeration.
3. Determine whether the beta extraction is a mixed momentum-derivative of the COMPLETE Pi or another source local projection and its exact physical versus dimensionless normalization.
4. Test a source-native *trace-per-root* Gaussian normalization with explicit eliminated-mode count, volume and lattice spacing to decide whether R78's determinant mismatch lemma has a uniform consumer.
5. Seek source-native weighted second-moment/covariance mismatch; exact shift covariance remains stronger than needed.
6. Independently source-verify positive-alpha Eq (0.29) and first-common-scale V^(j) dictionary. Keep P2M Schur provenance [86] separate.

Highest bibliographic item remains [86]; the next new source would be [87]. Historical heads through R77 preserved.
