# YM-R79 — local-insertion determinant polarization / first native trace bridge audit

Date: 2026-10-10
Repository: monocap-tech/yangmills
Prior recorded head: YM-R78 checkpoint 52f2c5b3de51d3d5e03aa623e7ea4997a6e829fb
Status: COMPLETE AS BOUNDED ABSTRACT AUDIT; NATIVE GATES OPEN
Next unconsumed frontier: YM-R80
Claim discipline: UNPROVED RESEARCH PROGRAM. No continuum Yang–Mills, OS reconstruction, or positive mass-gap result.

## 1. Cursor recovery and primary-source boundary

YM-R78 proved a finite-dimensional, per-mode mixed logdet-jet mismatch inequality and showed that unnormalized determinant traces accumulate a factor m=dim(eliminated modes). R77 gave an abstract second-spatial-moment sufficient condition for the beta/F^2 marginal extraction, but no native Pi tensor.

The R79 source search rechecked the original record for T. Bałaban, "Renormalization group approach to lattice gauge field theories: I", Communications in Mathematical Physics 109 (1987), 249-301, DOI 10.1007/BF01215223. The Springer publisher article page confirms small-field localized effective actions and recursive beta-functions, but presents only an abstract/preview and subscription access. Alternate Project Euclid / article-format links did NOT yield equation-readable originals. Searches on DOI, PDF filename and other hosts found bibliographic locators and SECONDARY summaries, not authentic equation windows. No current user-supplied original CMP109 page image or PDF was available. Hence Eqs (5.37), (5.42), (0.29) and their nearby normalization, sign, and quantitative hypotheses REMAIN UNINSPECTED. In particular [85] is still only a conditional secondary locator; no source text is silently promoted. Existing reference IDs [7],[59],[85],[86] repeated; bibliography highest [86]; next new source [87].

R79 accordingly investigates one rigorously typed ABSTRACT local-Gaussian route, not a reconstructed primary Yang–Mills proof.

## 2. One-step determinant differentiated at two *local* insertions

Let Λ be a finite graph of lattice roots with metric d and finite real Hilbert space H=direct sum_(x in Λ) H_x. Let C(b) be C^2 near b=0, symmetric strictly positive definite, in a FIXED Euclidean integration chart with parameter-independent measure. Define X=C(0)^(-1). For each root x write
  V_x = (partial_(b_x) C)(0),
  W_xy = (partial_(b_x)partial_(b_y) C)(0).
By Jacobi's formula,
  Pi^G_xy := (partial_(b_x)partial_(b_y) [ (1/2)log det C(b)] )|_(b=0)
           = (1/2)Tr(X W_xy - X V_x X V_y).
The second term is a two-insertion propagator loop; the first is the double-insertion/contact term. These are precise derivatives for this abstract finite model only.

This identity is more useful for local polarization than the R78 global `(1/(2m))logdet` estimate because a local vertex has uniformly bounded rank, independent of the full number of eliminated modes.

Additional *hypotheses*, not results: for each x there is an orthogonal projection P_x onto sites within radius R of x, rank(P_x)<=r, and V_x=P_x V_x P_x with ||V_x||<=v. Let W_xy be zero if d(x,y)>R_w; for d(x,y)<=R_w assume W_xy is supported on projection P_xy of rank<=r_w and ||W_xy||<=w. Assume
  ||X||<=G0,
  ||P_x X P_y||<=G exp(-kappa D_xy),
  D_xy=(d(x,y)-2R)_+,
with constants G0,G,kappa>0,R,R_w,r,r_w,v,w all independent of |Λ|.

Then
  |Pi^G_xy| <= (1/2) [
       r_w G0 w 1_(d(x,y)<=R_w)
       + r G^2 v^2 exp(-2 kappa D_xy)
  ].

PROOF: |Tr(X W_xy)|<=||X|| ||W_xy||_1 <= G0 r_w w on the contact support. For the loop use cyclicity and V_x=P_x V_x P_x, V_y=P_y V_y P_y, obtaining a trace on ran(P_y) of a product with factors P_y X P_x and P_x X P_y. Bound each by G exp(-kappa D_xy), each local vertex by v, and the trace by rank(P_y)<=r. No global factor m appears.

This is an ABSTRACT-DERIVED locality theorem. It does not prove that the actual Bałaban constraints leave P_x local or that its constrained propagator satisfies the stated decay. It also does not control the full interacting polarization.

## 3. Physically aligned local-difference theorem

For two kernels C_i(b), i=0,1, assume IDENTIFIED local carriers and matching local projections P_x, P_xy. Put X_i=C_i(0)^(-1), V_(i,x)=partial_x C_i, W_(i,xy)=partial_x partial_y C_i.

Assume all prior size, rank and locality bounds hold uniformly, and define nonnegative aligned differences:
  ||X_1-X_0|| <= delta_X0,
  ||P_x(X_1-X_0)P_y|| <= delta_X exp(-kappa D_xy),
  ||V_(1,x)-V_(0,x)|| <= delta_V,
  ||W_(1,xy)-W_(0,xy)|| <= delta_W 1_(d(x,y)<=R_w).
The last inequality presupposes the common supported contact W domain, and all differences are on the same physical root chart.

Then the determinant-polarization kernel difference obeys:
 |Pi^G_(1,xy)-Pi^G_(0,xy)|
  <= (1/2) [r_w (w delta_X0 + G0 delta_W) 1_(d(x,y)<=R_w)
       + r (2 G v^2 delta_X + 2 G^2 v delta_V)
           exp(-2 kappa D_xy)].

PROOF: telescope the contact trace as Tr((X1-X0)W1 + X0(W1-W0)). Telescope the loop Tr(X1 V1x X1 V1y - X0 V0x X0 V0y) into four terms varying one of two propagators or one of two vertices, retaining local supports. Every loop term contains TWO projected propagator paths between P_x and P_y, one of which may be the aligned difference; use the rank-r trace bound. All inequalities are finite dimensional and need no implicit mode-count factor.

If delta_X0,delta_X,delta_V,delta_W <= eps_N with sum_N eps_N < infinity, and the constants are independent of N, volume and x,y, then on a physically aligned infinite lattice Z^4 (or finite-volume embeddings satisfying the needed translation/boundary-extension conventions), the mixed second-spatial-moment defect is summable:
  sup_x sum_y |(y-x)_mu (y-x)_nu|
        |Pi^G_(1,xy)-Pi^G_(0,xy)|
      <= C_(kappa,R,R_w,r,r_w,G0,G,v,w) eps_N.
Reason: 4D lattice sums of polynomially weighted finite-range contact functions and exp(-2kappa(d-2R)_+) are finite.

If, IN ADDITION, these determinant kernels equal the properly normalized relevant part of the source vacuum-polarization and the precise source projection is a mixed Fourier second derivative, R77 transfers this to a summable Gaussian marginal defect. Neither extra source identity is proved here.

The theorem isolates the actual source-boundary task: do we have matched LOCAL insertions and exponential decay for both the constrained propagator and its cross-cutoff difference, with correct normalization? Neither follows from finite Schur positivity or from a_(N+1,j+1)=a_(N,j) alone.

## 4. Negative control: coercivity plus local vertices is NOT enough

Let Λ_n={1,...,n} with line distance and H=R^n. Let J_n be the all-ones matrix and define
  C_n = I_n+J_n/n,    X_n=C_n^(-1)=I_n-J_n/(2n).
The eigenvalues of C_n are 1 (multiplicity n-1) and 2 (multiplicity 1), so  I<=C_n<=2I uniformly.
Set C_n(b)=C_n + sum_x b_x E_x, where E_x=e_x e_x^T is the rank-1 local insertion, and consider b near 0. Then V_x=E_x is supported at exactly x, W_xy=0 and
  Pi^G_xy=-(1/2)Tr(X_n E_x X_n E_y)=-(1/2)|(X_n)_(xy)|^2.
For x=1,y=n, X_n(1,n)=-1/(2n), giving |Pi^G_(1,n)|=1/(8n^2).

No volume-independent C,kappa>0 can bound 1/(8n^2)<=C exp(-kappa(n-1)) for all n. Thus even uniformly bounded/strictly coercive C and rank-one LOCAL vertices do not imply exponential decay of the determinant polarization kernel. The separate propagator locality assumption is mathematically necessary for this route. This is an abstract counterexample, not source gauge theory.

## 5. Full native Pi and what remains outside the Gaussian determinant

The abstract Gaussian representation comprises
  * retained/eliminated quadratic Schur term, treated conditionally in R76-R77;
  * (1/2)logdet C and its local insertion/contact kernel, now quantified;
  * fixed Gaussian normalization -(m/2)log(2pi) if the integration measure/chart is fixed.

The actual one-step Bałaban polarization may also involve perturbative/interacting vertices, connected cumulants, background-dependent measure and gauge-chart Jacobians, Ward/Taylor subtractions, and localization/boundary terms. These are NOT asserted to form exactly this decomposition in CMP109; only the full native source can decide. No cancellation of any part is presumed.

Formal account:
  Pi_native = Pi_Gaussian + Pi_full_nonGaussian
is permitted only AFTER original source identification of both terms, and any mixed beta extraction must act on the entire properly normalized Pi_native. Proving the Gaussian kernel's decay does not imply the other terms are small or their difference summable.

For the Eq (0.29) complement, neither local determinant derivative nor Schur coercivity yields the required nonlinear/polymer estimate with positive alpha. Its exact primary norm, support, exponents, uniformity and first-common-scale identity remain independent open obligations.

## 6. Evidence classification and conclusion

ABSTRACT-DERIVED:
- finite local double-derivative logdet kernel identity with contact and two-vertex loop;
- uniform-in-volume pointwise exponential decay under finite-support vertices, finite-rank contact, and two-sided constrained propagator locality;
- explicit cross-cutoff determinant-kernel difference bound;
- summable 4D second moment under summably small aligned local-defect parameters;
- rank-one vertex/coercive-precision counterexample refuting locality without propagator decay.

CONDITIONAL NATIVE:
- common physically aligned gauge-fixed carrier and local background insertion support;
- uniform exponential decay of constrained propagator and of its aligned difference;
- correct gauge/measure/Fourier/tensor/volume normalization for beta extraction;
- control of full non-Gaussian polarization remainder, then a full Pi moment mismatch.

OPEN PRIMARY:
- exact original CMP109 Eqs (5.37), (5.42), (0.29), surrounding source definitions, alpha and norms;
- source-native local V_x and W_xy and whether constraint projectors are local;
- beta tensor projection, Ward identities and source coupling relation;
- first-common-scale extra-layer residual V^(j) and quantitative polymer summability;
- Prove2Me scalar Schur exact Lean theorem ID from provisional [86].

OBSTRUCTED:
- strict positivity of C + local vertices => exponentially decaying Gaussian polarization;
- Gaussian determinant control alone => cross-cutoff full beta stationarity or positive-alpha residual.

The native R75 gates remain OPEN. No continuum existence, reflection positivity/OS construction, or mass-gap theorem is obtained.

## 7. Next frontier — YM-R80 (unconsumed)

1. Retrieve the original CMP109 equation windows (5.37), (5.42), (0.29) in an inspectable primary PDF/page scan from an authorized archive; record page number, exact normalization and domain. Do not infer equation contents from [85].
2. From the primary full-polarization definition, test whether its Gaussian component can be expressed by the R79 LocalBackgroundInsertion and DoubleInsertionContact dictionary, including gauge slices and actual background field chart.
3. Audit locality of the constrained inverse (not merely elliptic coercivity), and whether aligned differences are bulk-stationary or boundary/extra-UV defects with summable exponential locality.
4. Prove or refute the matching of determinant/Schur/non-Gaussian terms under physical-scale index alignment and the full tensor's second-moment estimate.
5. Independently recover Eq (0.29)'s primary localized polymer bound and one-layer V^(j) role; test positive-alpha and uniform rooted summation.
6. Keep [86] Prove2Me theorem provenance as a separate tracking task.

Highest existing reference remains [86], next genuinely new source [87]. Historical checkpoints R76-R78 remain immutable.
