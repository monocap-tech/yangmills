# YM-R76 — Schur-complement reintegration / one-step vacuum-polarization audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior certified repository head: YM-R75, 3c35ace083e72d5ba00e08687cafbdb2ea9a6639
Status: COMPLETE AS AUDIT; neither native gate discharged
Next unconsumed cursor: YM-R77
Claim status: UNPROVED RESEARCH PROGRAM. No continuum Yang–Mills existence or mass-gap claim.

## 1. Task and source custody

Audit whether the newly reported Prove2Me acceptance of a Schur-complement positivity lemma can discharge the R75 native obligations: (A) cross-cutoff stationarity of a one-step vacuum-polarization tensor and its marginal beta extraction; (B) primary Bałaban CMP109 Eq. (0.29), a positive-alpha, localized, irrelevant residual bound.

Sources repeated: [7] CMP109, [59] CMP119, existing CMP99/CMP102 source custody and [85] Eriksson secondary locator. Added [86] as a provisional external theorem-provenance record, NOT as independently verified certified Lean evidence. See ym/references/YM_REFERENCES_086_20261010.md. Primary CMP109 equation-level proof text was not newly recovered in this pass. The 1987 peer-reviewed paper metadata/abstract confirms the local one-step small-field architecture and beta-function construction, not the specific Eqs. (5.37), (5.42), (0.29), their exact signs, domains, and constants.

R69-R75 remain historical authority: a_(N,j)=L^(j-N), a_(N+1,j+1)=a_(N,j) exactly; R64 records prescribed bulk coupling recursion and marginal subtraction in CMP119 Eq. (2.24)-(2.25); R75 locates the polarization extraction through [85] ONLY; the exact stationarity theorem and primary Eq. (0.29) remained open.

## 2. Schur provenance / statement / mathematical proof

Reported Prove2Me milestone: a real finite-dimensional symmetric block matrix of shape

    H = [[1, x^T],
         [x, X]] >= 0

implies X - x x^T >= 0, and thus X_jj >= x_j^2 for every coordinate j.

Conventions: >=0 means positive SEMIDEFINITE in the quadratic-form order, for real matrices X on a finite coordinate set; x is a real column vector. The pivot is the unit positive scalar 1. The conclusion permits zero eigenvalues. No quantitative spectral gap, inverse bound, exponential off-diagonal locality, UV uniformity, or positivity of an unbounded infinite-dimensional operator is asserted.

Independent algebraic verification: for any v, test positivity of H on (-x^T v,v), obtaining v^T(X-xx^T)v >= 0. Testing on coordinate vectors gives the diagonal consequence. This elementary argument does NOT independently verify that the particular Lean theorem, proof term, full context, package, or statement has been accepted by Prove2Me.

Prove2Me status: user reports ACCEPTED/Proved on 2026-10-10; public theorem URL/UUID, exact Lean declaration, assumptions/namespace, Mathlib revision and accepted proof artifact were NOT recovered, and therefore the precise P2M identifier is UNKNOWN. Do not cite a guessed UUID or silently label an uninspected formal proof machine-certified. [86] records the verification deficit. The mathematical scalar-pivot implication is CERTIFIED as an elementary derivation here; the platform-specific certification/provenance remains OPEN.

Scope transfer: a general finite block H=[[A,B],[B*,C]], C>0, has reduced quadratic form S=A-BC^(-1)B*. Its positivity follows by completing the square (or suitable congruence), provided H>=0, C is genuinely invertible, and the spaces are exactly specified. This extension is standard mathematical algebra, not automatically the identical Prove2Me theorem: the accepted reported statement is only the 1-by-1 unit pivot. For C merely semidefinite, C^(-1) is undefined; Moore-Penrose treatment needs a range-compatibility condition. Infinite-dimensional/unbounded extensions need separate form-domain and inverse arguments.

## 3. Source-native applicability dictionary

Candidate 1: exact finite Gaussian fluctuation block on the constrained gauge/block slice.
Retained variable r: linearized block/background coordinate. Eliminated variable e: the fluctuation satisfying the homogeneous gauge and block-average constraints. R40 types the prospective slice as V_j = ker(L_eta^j Q_j) intersect ker(R D*), conditional on source translation. On a common positive gauge-fixed real Hessian, A=H_rr, B=H_re, C=H_ee; finite Gaussian elimination gives S=A-BC^(-1)B* and normalization (det C)^(-1/2). SOURCE-IDENTIFICATION CONDITIONAL: the primary Hessian-to-CMP99 Green/precision identity, exact operator domain, volume-uniform invertibility and the normalizations remain to be locked. R38-R41 explicitly prohibit treating CMP102 Delta_1 and CMP99 Delta_a as identical by notation alone. Gauge zero modes cannot be put into an inverse C on the ambient bond space.

Candidate 2: covariance decomposition into retained and eliminated shells.
If an actual finite positive Gaussian covariance K is partitioned, the covariance-conditioned Schur matrix is K_rr-K_re K_ee^(-1) K_er; equivalently precision-block elimination describes the marginal covariance after inversion. The two constructions must not be interchanged. Need a source-defined conditioning/marginalization convention and strict invertibility on the actual carrier. CONDITIONAL. Positivity of a covariance does not identify the vacuum-polarization vertex or its local F^2 coefficient.

Candidate 3: background-dependent effective-action Hessian.
An abstract Hessian H_eff with actual source-native retained/eliminated chart could support quadratic Schur reduction near a positive critical configuration. But the one-step effective action also has interaction/cumulant, fluctuation-determinant, chart Jacobian and localization contributions. A background-dependent log det C term is NOT controlled by positivity of S. CONDITIONAL for the quadratic algebra; OPEN for the full effective-action identification.

Candidate 4: local Taylor/Ward/F^2 marginal projection.
One may apply the source-defined functional Loc_F2 only to the complete source polarization Pi, after proving gauge/translation/Ward identities and C^2 momentum-jet existence with correct scale normalization. Neither the finite PSD lemma nor a generic Hessian Schur reduction provides this identity. NOT APPLICABLE AS A STANDALONE TRANSFER; source extraction and stationarity remain OPEN.

Candidate 5: Eq. (0.29) marginal-subtracted polymer activity V^(j).
The displayed a^(4+alpha) exp(-kappa d_j(X)) estimate is an activity/polymer norm bound, not a matrix PSD statement. A Schur complement of a Hessian is insufficient even to control higher interaction vertices. OBSTRUCTED as an implication from positivity alone; source Eq. (0.29) OPEN.

Gauge: Hessians on unrestricted gauge orbits have null directions from infinitesimal gauge transformations; an unrestricted inverse is invalid. The source-native Dirichlet/gauge-fixed V_j must be identified at every scale and on every regular background. Complex analytic contours require coercive real-part estimates; a real PSD theorem does not supply complex coercivity. UV/volume/cutoff/gauge independence cannot be inferred from finite-dimensional positivity.

## 4. Gate A: exact statement, quantitative conditional lemma and obstruction

The alignment a_(N+1,j+1)=a_(N,j) is an algebraic fact, not an identification of backgrounds, gauge slices, normalized Gaussian measures, covariances, boundary cutoffs, or vacuum-polarization tensors.

For two finite gauge-fixed positive quadratic matrices H_i=[[A_i,B_i],[B_i*,C_i]], assume C_i >= c I (c>0), norm B_i <= K, and all operators have compatible identified coordinates. S_i=A_i-B_i C_i^(-1)B_i*. The resolvent identity gives

    ||S_1-S_0|| <= ||A_1-A_0||
                  + (2K/c)||B_1-B_0||
                  + (K^2/c^2)||C_1-C_0||.

Proof: telescope B_1 C_1^(-1) B_1* - B_0 C_0^(-1) B_0* in three factors; use C_1^(-1)-C_0^(-1)=C_1^(-1)(C_0-C_1)C_0^(-1). This is a legitimate CONDITIONAL finite-dimensional stability lemma with explicit constants. The positivity theorem itself supplies NEITHER c NOR K NOR the three differences. For momentum second-derivative beta extraction the same estimate must hold in an appropriate C^2 jet algebra, including derivative bounds on C^(-1), not merely in uniform operator norm.

If the full source polarization difference obeys ||Pi_(N+1,j+1)-ScaleIdentify Pi_(N,j)||_jet <= eps_(N,j) AND Loc_F2 is a uniformly bounded functional commuting with scale identification, then

    |beta_(N+1,j+1)-beta_(N,j)| <= C_Loc eps_(N,j).

If this bound is summable with the appropriate R72 tail sensitivity, the weaker marginal mismatch route follows. Exact equality needs exact transport of ALL contributing terms and normalized measures, including log determinant/cumulants, not only Schur matrices. The source has not supplied those data.

OBSTRUCTION 1: positivity without cross-cutoff covariance. H_0=I and H_1=2I are both strictly positive at the same nominal physical lattice spacing, while their reduced forms differ by O(1).

OBSTRUCTION 2: even equality of reduced S does not control polarization from Gaussian normalization. Take scalar background t, A(t)=I, B(t)=0, C(t)=exp(lambda t^2) I. Every block is positive and S(t)=I independently of lambda, yet the Gaussian effective-action term (1/2)log det C(t)=(dim e/2)lambda t^2 has arbitrary quadratic background coefficient. No Schur PSD conclusion determines this term.

Therefore Schur positivity does NOT discharge PrimaryOneStepVacuumPolarizationStationarity; the interface, if used, is a conditional estimate only.

## 5. Gate B: positivity/coercivity do not imply positive-alpha locality

The candidate residual inequality, from [85] and NOT primary-verbatim-verified [7], has the schematic form

    ||V^(j)(X)||_j <= C a_(N,j)^(4+alpha) exp(-kappa d_j(X)), alpha>0.

Finite PSD elimination does not bound analytic Taylor remainders: the functions f_M(t)=t^2+M t^6 have the same positive Hessian at t=0 for every M>=0 but arbitrarily large sixth-order coefficients. The Hessian alone cannot force the activity estimate.

Nor does uniform strong coercivity alone force exponential locality. For each n>=2 let J_n=1_n 1_n^T, C_n=I_n, A_n=I_n and B_n=J_n/(2n). Then

    S_n = A_n-B_n C_n^(-1) B_n* = I_n-J_n/(4n) >= 3I_n/4,

and H_n=[[A_n,B_n],[B_n*,C_n]] is uniformly positive. But (S_n)_(1,n)=-1/(4n) for two sites distance n-1 on a line. There are no n-independent C,kappa>0 with 1/(4n)<=C exp(-kappa(n-1)). Thus even UNIFORM positive-definite full blocks can have reduced forms lacking uniform exponential off-diagonal decay.

A genuine Eq. (0.29) bridge requires native bounds on off-diagonal decay of C^(-1), B, and their background/momentum derivatives, locality of gauge-slice projectors and Gaussian measure/Jacobian, controlled higher Taylor/Ward jets with marginal subtraction, a rooted polymer norm and entropy budget, and extraction of a positive UV-scale excess alpha with all constants uniform in j,N,volume and the prescribed weak-coupling window. Source text must specify V^(j), X, ||.||_j, d_j, alpha, normalization and domain. Schur positivity supplies none of these quantitative inequalities.

R69-R70 conditional root count is unchanged: if the native source bound and rooted polymer summability hold, 4D root number O(a^-4) leaves O(a^alpha), summable as N grows. Schur does not produce alpha.

## 6. Status classification

- CERTIFIED (mathematical derivation, not native gate): scalar-pivot 1+n PSD implication by quadratic-form test; finite invertible-positive-block Schur identity and perturbation bound under named hypotheses; physical-scale index equality from R70.
- CONDITIONAL: applying block elimination to the actually gauge-fixed, finite native Gaussian Hessian; quantitative reduced-Hessian cross-depth mismatch; bounded Loc_F2 map from a proved polarization jet mismatch to beta mismatch.
- OBSTRUCTED: PSD alone => exact cross-cutoff polarization/beta covariance; equality of reduced S => equality of determinant-derived polarization; PSD/uniform coercivity alone => exponential locality or alpha>0 irrelevant residual; lifting a 1+n real finite theorem automatically to complex, gauge-degenerate or infinite-dimensional operators.
- OPEN: exact P2M theorem UUID, Lean declaration/proof receipt; CMP99/CMP102/CMP109 common Hessian operator definition and gauge-domain custody for this use; primary CMP109 Eqs. (5.37),(5.42),(0.29); full one-step Pi and beta normalization; exact/summable cross-depth polarization covariance; Eq. (0.29) positive-alpha assumptions, constants, and one-layer V dictionary.

There is NO newly certified Yang–Mills-specific Schur application, no new source-theorem closure of either native gate, and no valid mass-gap inference. Schur is a potentially useful local algebraic lemma, not a currently load-bearing solution mechanism.

## 7. Bounded next frontier: YM-R77 (unconsumed)

Return to the original one-step vacuum-polarization audit without forcing Schur:

1. Acquire an equation-readable *primary* CMP109 (5.37), (5.42), (0.29) window; record exact signs, tensor components, Fourier momentum normalizations, domain, alpha, polymer definition and cutoff/volume uniformity.
2. Reconstruct the full Pi_(N,j), not just a quadratic Hessian: background propagator, determinant, vertices, gauge slice and source localization; list every scale-dependent input and a native scale-identification map.
3. Test exact rescaling covariance at a_(N+1,j+1)=a_(N,j); otherwise establish a summable C^2 polarization-jet mismatch and a uniformly bounded Loc_F2.
4. Pair the extracted beta/F^2 projection with the actual V^(j) remainder, test whether it is the first-common-scale extra-layer defect, and prove or obstruct its positive-alpha bound in the original norm.
5. If Schur is revisited, do so only after a source-identified C_j, uniform inverse/locality constants and the correct Gaussian determinant/cumulant accounting are available.
6. Resolve P2M theorem UUID/proof version as provenance, but treat this as independent from the native mathematical burden.

No other prior cursor is consumed; highest reference ID is now provisional [86], future new source [87]. Historical R69-R75 records remain unchanged.