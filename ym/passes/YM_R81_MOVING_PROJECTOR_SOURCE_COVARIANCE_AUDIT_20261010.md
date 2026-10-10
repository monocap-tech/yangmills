# YM-R81 — prior CMP99 covariance custody / moving gauge-projector defect audit

Date: 2026-10-10
Prior repository head: YM-R80, commit 1a367832051a1f0c69f70c4ad1aee5789addca60
Status: COMPLETE AS AUDIT + ABSTRACT THEOREM; NATIVE POLARIZATION GATES OPEN
Next live cursor: YM-R82 (unconsumed)
Claim discipline: UNPROVED RESEARCH PROGRAM; no continuum Yang–Mills or positive mass gap.

## 1. Recovery: R80's abstract locality source already has a primary Bałaban predecessor

R80 derived an abstract finite-propagation inverse theorem and showed that local constraint equations do not guarantee a local kernel projector. Before reopening this as a new source proof, R81 recovered existing project bibliography and passes:

- Existing reference [77]: Bałaban, *Regularity and decay of lattice Green's functions*, CMP 89 (1983), 571–597, DOI 10.1007/BF01214744. The PRIMARY publisher abstract attests positivity, exponential Green-function decay and lattice-spacing uniformity for a class of covariant lattice Laplace operators with external gauge fields. Scope is THAT operator class; no CMP109 cross-depth theorem follows.
- Existing reference [79]: Bałaban, *Propagators for lattice gauge theories in a background field*, CMP 99 (1985), 389–434, DOI 10.1007/BF01240355. The PRIMARY publisher abstract attests regularity and decay for RG propagators in an external background.
- Existing YM-R32 and reference [79] record an AUXILIARY-SOURCE-VISUALLY-AUDITED equation/theorem ledger: G(U)=(Delta_a|Omega_0)^(-1) (3.26)–(3.27), decay Thm 3.3/(3.42)–(3.47), positivity Thm 3.11, field-background stability Thm 3.12 under (3.35),(3.36), and exponentially decaying background covariance C^(k)(A) Thm 3.15/(3.185),(3.187), under small M alpha_0, schematically ||C^(k)(Lambda;y,y')||<=B_0 exp(-delta_0 ||y-y'||).

This is stronger than rediscovering generic inverse decay in R80. However R81 did NOT retrieve and personally inspect the printed original CMP99 theorem pages; the equation-level statements here are attributed exactly to the prior archived source audit and not silently presented as newly verified verbatim transcriptions. Public publisher pages expose abstracts but not the full equations. Original CMP109 Eqs (5.37),(5.42),(0.29) also remain inaccessible and uninspected.

The actual missing source dictionary has already been identified in YM-R40/R41: CMP102's homogeneous tangent slice V_j=ker(L_eta^j Q_j) intersect ker(RD*) is a conditional derived coordinate, while literal identification of CMP102 Delta_1 with CMP99 Delta_a is UNPROVED. YM-R41 specifically forbids inferring a=1 from the subscript 1. The same type restriction applies when matching CMP99 C^(k)(A) to the one-step CMP109 Gaussian covariance.

Determination: **source evidence exists for native background-propagator locality in a neighboring, previously audited Bałaban construction; its transfer into the full CMP109 polarization remains an OPEN SOURCE/TYPE GATE**. Merely having two decaying propagators does not establish summable cross-cutoff difference.

No new bibliography entry: [77] and [79] are reused; highest [86].

## 2. Weighted moving-projector transfer theorem (ABSTRACT-DERIVED)

Let Lambda be a finite metric-site set and ||.||_kappa the weighted Schur matrix algebra norm
  ||M||_kappa = max(sup_x sum_y e^(kappa d(x,y))||M_xy||, sup_y sum_x e^(kappa d(x,y))||M_xy||).
It is submultiplicative by the metric triangle inequality.

On a COMMON ambient Hilbert space let P_i=P_i*=P_i^2, C_i=C_i*>0, i=0,1. Define
  A_i=P_i C_i P_i+(I-P_i), X_i=P_i A_i^-1 P_i.
Assume the following quantities are bounded uniformly:
  ||P_i||_kappa <= K_P,
  ||C_i||_kappa <= K_C,
  ||A_i^-1||_kappa <= R,
and set
  delta_P=||P_1-P_0||_kappa,
  delta_C=||C_1-C_0||_kappa.

Then
  ||X_1-X_0||_kappa
    <= K_P^4 R^2 delta_C
      + [2 K_P R + K_P^2 R^2(2 K_P K_C+1)] delta_P.

Proof. With D_P=P1-P0,
  A1-A0 = P1(C1-C0)P1 + D_P C0 P1 + P0 C0 D_P - D_P.
Therefore
  ||A1-A0||_kappa <= K_P^2 delta_C+(2K_P K_C+1)delta_P.
The inverse resolvent identity yields
  ||A1^-1-A0^-1||_kappa <= R^2||A1-A0||_kappa.
Telescoping
  X1-X0 = D_P A1^-1 P1 + P0(A1^-1-A0^-1)P1 + P0 A0^-1 D_P
gives the claimed estimate.

The source application additionally needs to identify the aligned charts and possibly conjugate one by a source-defined gauge-slice transport map. Equal lattice spacings alone do NOT imply the P_i share a common chart. For each i, finite-propagation P_i,C_i plus a uniform spectral corridor and uniform lattice growth are one sufficient way to obtain the assumed R at kappa below the inverse-decay exponent; the native CMP99 direct covariance theorem may be a weaker/more appropriate replacement.

If delta_P(N)+delta_C(N) is summable AND source-defined local insertion differences are summable, R79's local Gaussian polarization second-moment estimate can be applied to that component. Full Pi still requires other terms and an exact source extraction.

This removes R80's unnecessary SAME-P hypothesis but does NOT claim summability of delta_P or delta_C in Yang–Mills.

## 3. Obstruction: ordinary projector norm closeness is not enough

Consider sites 0,...,n with distance d(0,n)=n, and vectors
  u_n=sqrt(1-n^-2)e_0+n^-1 e_n.
Let P0=|e_0><e_0| and Pn=|u_n><u_n|. Then
  ||Pn-P0||_op = 1/n -> 0,
while the off-diagonal entry (Pn)_(0,n)=sqrt(1-n^-2)/n is long range.

Keep the ambient precision C(b)=I+sum_x b_x E_x, strictly local. On the rank-one constrained slices, the Gaussian determinant contributions are
  F0(b)=(1/2)log(1+b_0),
  Fn(b)=(1/2)log(1+(1-n^-2)b_0+n^-2 b_n).
At b=0,
  partial_(b_0)partial_(b_n)(Fn-F0)
    = -(1/2)(1-n^-2)n^-2.
Multiplying by the distance-squared n^2 gives a limit -1/2, NOT zero.

Therefore a vanishing ordinary operator-norm gauge-projector defect is insufficient for the spatial second-moment metric required by the R77 Fourier extraction, even with identical positive ambient precision and strictly local background insertions. This is an abstract counterexample, NOT evidence that the physical Bałaban projectors behave this way. A direct decaying *constrained covariance difference* estimate can bypass the weighted P comparison entirely.

## 4. Exact source graph and retained native gates

Source facts / provenance:
[77] covariant Green positivity/locality (publisher abstract).
[79] background-dependent RG propagator decay (publisher abstract), with previously visually audited CMP99 C^(k)(A) equation and theorem locators (YM-R32).

OPEN source/type edges:
(A) CMP99 C^(k)(A) or G(U) <-> CMP102 Delta_1/homogeneous gauge-block fluctuation carrier.
(B) Those native objects <-> exact Gaussian covariance/precision entering CMP109 one-step fluctuation integral.
(C) Two cutoffs, aligned physical scale, possibly differing gauge coordinates: identify C_i,P_i or prove directly a uniform weighted constrained-covariance difference.
(D) Differentiate/localize full one-step Pi including interactions, gauge measure, Jacobians and boundary; prove a summably small mixed second moment and bounded source Loc_F2. Source [85]'s Eq (5.42) locator is NOT a substitute.
(E) Independently directly inspect primary CMP109 Eq (0.29), identify V^(j) and positive alpha polymer norm and its one-layer cross-cutoff role.

CANNOT PROMOTE: a prior source-audited *one-trajectory* exponential decay theorem to exact *two-cutoff* covariance or summable difference without (B)-(D). Also no projection locality conclusion from gauge-fixing equations alone. The original CMP109 equation pages remain uninspected.

## 5. Determination and next frontier

ABSTRACT-DERIVED: varying-projector weighted inverse difference theorem; norm-small but moment-large projector counterexample.
PREVIOUSLY SOURCE-LOCATED: CMP99/1983 native Green/covariance decay theorem package in existing [77],[79], YM-R32; no fresh page-verbatim audit.
CONDITIONAL NATIVE: weighted delta_P/delta_C plus identified Gaussian insertions => R79 Gaussian polarization moment, not full Pi.
OPEN NATIVE: CMP99/CMP102/CMP109 common carrier/operator identity; source aligned Gaussian and non-Gaussian Pi difference; primary Eq (0.29) positive-alpha polymer bound; P2M theorem exact accepted UUID [86].

YM-R82 (unconsumed): pursue the ACTUAL CMP109 one-step fluctuation covariance back-reference and CMP102 Delta_1 provenance on a single native carrier; determine whether CMP99 Thm 3.15's C^(k)(A) is the required object or whether a transported covariance is used. Then seek quantitative cross-depth or boundary-sensitive Green *difference* estimates with the source normalization. Independently recover primary (5.37),(5.42),(0.29) and Eq (0.29) hypotheses; no guessing from [85].

No mass gap, continuum Yang–Mills existence, or unconditional native theorem closure is claimed.
