# YM-R80 — constrained inverse locality audit

Date: 2026-10-10
Prior checkpoint: YM-R79, 0df6c4050a1d26389d001c42fd1d9710a0fa0620
Status: mathematical audit complete; native source gates OPEN
Next cursor: YM-R81
Claim status: unproved research program.

## 1. Native source custody

The original Bałaban CMP109 article (1987, DOI 10.1007/BF01215223) is bibliographically identified. Springer currently supplies preview/abstract but not the equation text; Project Euclid .full/.pdf views did not expose original pages. The precise original equations (5.37), (5.42), (0.29) and their gauge, scale, polymer, normalization and domain definitions have not been inspected in this pass. Secondary source [85] remains a locator, not original theorem custody. Existing bibliographic references [7], [59], [85], [86] are reused. No new numbered source.

## 2. Local precision has local inverse under a uniform spectral corridor

Let H be a finite metric-site Hilbert space, with site projections E_x. Suppose self-adjoint C satisfies 0<m I<=C<=M I and finite propagation ell: E_x C E_y=0 for d(x,y)>ell. Write q=1-m/M and T=I-C/M. Then ||T||<=q and C^-1=(1/M) sum_{k>=0} T^k. Since T^k propagates at most k ell,
  ||E_x C^-1 E_y|| <= m^-1 q^ceil(d(x,y)/ell).
For 0<q<1 this is bounded by m^-1 exp(-gamma d(x,y)), gamma=-log(q)/ell. If q=0, C=M I is diagonal. The constants are independent of the number of lattice sites if m,M,ell are uniform.

This is an abstract finite-dimensional theorem, not yet an identified Bałaban propagator estimate.

## 3. The gauge-constraint projector is an independent locality gate

Let P be a FIXED orthogonal projector onto a constrained fluctuation space, with propagation ell_P. Define A=P C P+(I-P), so the constrained covariance embedded in the original carrier is X_P=P A^-1 P. On ran P, A is C restricted to that space; on ker P, A=I. Thus
  m'=min(m,1), M'=max(M,1)
bound its spectrum, and A has propagation at most ell_A=ell_C+2ell_P+1.

Putting q_A=1-m'/M', for q_A in (0,1):
  ||E_x X_P E_y||
  <= (m')^-1 q_A^ceil((d(x,y)-2ell_P)_+/ell_A).
This is a sufficient exponential localization criterion with an enlarged finite range. A source construction could instead prove locality of X_P directly without finite-range P; the latter is not a necessary hypothesis.

## 4. Aligned inverse difference estimate

For physically identified finite carriers and the SAME fixed projector P, take C_0,C_1 satisfying common m,M,ell_C, and let epsilon=||C_1-C_0||. Define A_i=PC_iP+(I-P), T_i=I-A_i/M'. By telescoping:
  ||T_1^k-T_0^k|| <= k q_A^(k-1) epsilon/M'.
The difference has propagation <=k ell_A. If D=(d(x,y)-2ell_P)_+ and K=max(1,ceil(D/ell_A)), then
  ||E_x(X_(P,1)-X_(P,0))E_y||
  <= (epsilon/M'^2) sum_{k>=K} k q_A^(k-1)
  = (epsilon/M'^2) q_A^(K-1)[K/(1-q_A)+q_A/(1-q_A)^2].
If q_A=0, the difference is zero. The estimate is O(epsilon (1+d)exp(-gamma_A D)), gamma_A=-log(q_A)/ell_A, and admits a slightly weaker pure exponential bound.

On standard Z^4 root geometry, summable epsilon_N gives a summable second-spatial-moment bound for the constrained covariance defect. Combined with R79, summably aligned LOCAL background vertices could then control the Gaussian determinant portion of the polarization defect. Neither exact physical-scale alignment alone nor Schur positivity proves epsilon_N small. A source-matched common gauge projector remains unverified.

## 5. Counterexample: local constraint equations need not yield a local projector

Consider n sites on a cycle, ambient precision C=I_n and nearest-neighbor constraints (Qv)_j=v_j-v_(j+1)=0. The kernel consists of constant vectors; its orthogonal projector is P=J_n/n, with all entries 1/n. For sites at distance comparable to n/2, these entries cannot satisfy a volume-uniform exponential bound.

For a local background diagonal precision C(b)=diag(1+b_j), the restriction to the constant unit vector has scalar precision c(b)=1+n^-1 sum_j b_j. Hence for distinct x,y,
  partial_bx partial_by [ (1/2)log c(b) ] at b=0 = -1/(2n^2).
This Gaussian polarization derivative also fails volume-uniform exponential decay at opposite sites.

Thus local ambient precision, uniform coercivity and local constraint EQUATIONS are not sufficient to prove locality of the constrained Gaussian covariance. This is an abstract counterexample, not a Yang-Mills-specific result.

## 6. Evidence and next frontier

ABSTRACT-DERIVED: the Neumann inverse estimate; the finite-range-projector constrained inverse estimate; the cross-cutoff inverse difference estimate; the local-equations/global-projector counterexample.

CONDITIONAL NATIVE: identify a common physical gauge slice and its propagator/constraint geometry; obtain uniform spectral and finite-propagation bounds or direct constrained Green-function decay; prove summably small aligned precision and vertex differences and all background normalization identities.

OPEN PRIMARY: original CMP109 equations (5.37),(5.42),(0.29) and associated CMP99/CMP102 Green/gauge definitions; full polarization including non-Gaussian and measure terms; positive-alpha irrelevant-polymer bound and one-layer correspondence; separate P2M Schur theorem provenance [86].

Next cursor YM-R81: read original equation windows or existing original source cache, determine whether native gauge constraints admit a local/quasilocal projector or a directly localized constrained Green operator, and test full polarization plus Eq (0.29) independently.

No continuum Yang-Mills theory or positive mass gap is claimed. Highest reference [86], next new source [87].
