# YM-R150 continuation — historical CMP99 covariance bound and exact constrained-Hessian transfer gate

**Date:** 2026-10-31. **Source class:** ORIGINAL PRINTED LITERATURE FACT + CONDITIONAL DEDUCTIONS. **Repository predecessor:** merged R150 mixed-second-jet receipt, main 65c977e58b0fdcb64ec8161bb70dd88ca55b700b. **Native YM-R150 IN PROGRESS/UNCONSUMED. Canonical R149 machine checkpoint unchanged.** No CMP109 uniform alpha, UV-pair measure, continuum Yang–Mills existence or mass gap.

## 0. Actual original source custody

User-supplied original typeset **T. Bałaban, CMP 99(3) (1985), 389–434**, 46-page PDF, SHA256 **9904f303f01e2d267a0d138d4fc08d60742086d6557fc78bef6f2d25faeaad20**. Printed pp. **427–428** (3.155)–(3.158), and **432** (3.183)–(3.187) were read from page images (zero-based indices 38,39,43). No source PDF redistribution to public GitHub. CMP109 printed pp.266–268 (2.9)–(2.12) were previously verified, including the distinct new covariance (C_new* A^(k) C_new)^-1.

**PRINTED CMP99 SOURCE p428:** On the permitted Dirichlet/zero-support plus Q1 B=0 Gaussian slice, special-bond graph B=C_o \bar B satisfies P_o C_o=I on the independent (non-special) bond coordinates. Source (3.156) defines the historical quadratic A_k=Delta_k in the author's notation; (3.157)–(3.158) show
    K_o=C_o* Delta_k C_o,
    Sigma_o=K_o^(-1)=P_o C^(k)(Lambda) P_o*,
    C^(k)(Lambda)=C_o K_o^(-1) C_o* .                  (R150.C1)
The source explicitly asserts a positive bound gamma0 independent of k,U under its regularity/smallness and regional hypotheses. The gamma0 is not printed numerically.

**PRINTED CMP99 SOURCE p432:** Theorem 3.15, under sufficiently small M epsilon0 and its established source hypotheses, identifies the same historical covariance via (3.185) and proves
    |C^(k)(Lambda;y,y')| <= B0 exp(-delta0 |y-y'|),  (R150.C2)
with B0,delta0>0 depending only on d,L, not k,U or the allowed region. Source (3.185) is specifically
    C^(k)(Lambda)=(I+D mu) Q Gtilde2 Q* (I+mu*D*),
and (3.186) uses **a distinct Qtilde** in the conditioning of G2. These are SOURCE-IMAGE facts and do not identify the historical covariance with CMP109's 1987 exponential-gauge reduced precision.

Theorem 3.15 is a qualitative statement with unspecified constants. No numerical B0 or delta0, same-chart identification, CMP109 fluctuation Gaussian, source cutoff or interaction-weighted mass has been obtained.

## 1. Concrete historical Gaussian consequence: bypass the full K_o matrix

Equation (R150.C1) shows the source independent-coordinate covariance is a literal coordinate restriction of the full source propagator. Consequently its matrix entries obey (R150.C2). For SU(2), choose a fixed source orthonormal real color basis, so one monitored bond has a *centered* Gaussian color vector X in R^3. If Theorem 3.15's printed |.| bound denotes a 3x3 block operator norm then Cov(X)<=B0 I3. If it denotes only componentwise absolute values, the conservative matrix estimate is
    0<=Cov(X)<=3 B0 I3.                             (R150.C3)
Use B*=3 B0 in either case, to avoid a false norm-convention claim. By coupling X=Sigma_X^(1/2) Z with Z standard R^3 Gaussian, ||X||<=sqrt(B*)||Z|| pointwise on the coupled space; hence for any T>0,
    Pr(||X|| >= T)
       <= Q3(T / sqrt(3 B0)),                        (R150.C4)
where Q3(r)=erfc(r/sqrt2)+sqrt(2/pi) r exp(-r^2/2) is the exact Maxwell radius survival function. If 3B0=0, take the deterministic limiting convention. No global-color isotropy or bond independence is required; in particular this bound holds for any source-eligible background U under Theorem 3.15, assuming the source centered Gaussian definition (3.155). This is an actual **HISTORICAL bare Gaussian one-coordinate exit gate**, not a CMP109 or weighted interacting-law estimate.

For a finite set of m historical monitored bonds with the same formal threshold, the union bound gives m Q3(T/sqrt(3 B0)); this can grow with volume and is not uniform in the UV or a substitute for the historical paper's actual cutoff choices. Do not insert CMP109's theta_k/g_k into the CMP99 source formula without a matched rescaling.

## 2. Explicit uniform historical operator bound from source exponential decay

For four-dimensional unit-lattice *oriented* bonds, use a site anchor plus one of 4 positive directions and 3 real colors. The physical edge-midpoint separation exceeds anchor separation minus at most one in Euclidean norm. For lattice-site difference n in Z^4,
    exp(-delta0 |b-b'|) <= exp(delta0) exp(-delta0 |n|_2)
                        <= exp(delta0) exp(-delta0 |n|_1/2).
Thus (componentwise convention, conservative 12 coordinates per anchored site) Schur's row/column bound gives
    ||Sigma_o||_{2->2} <= M_hist,
    M_hist = 12 B0 exp(delta0)
             [(1+exp(-delta0/2))/(1-exp(-delta0/2))]^4.  (R150.C5)
Because source finite Dirichlet regions are subsets of this infinite lattice sum, the bound is independent of domain size. It depends only on B0,delta0,d=4,L=13, provided Theorem 3.15's |.| is in the specified source unit-lattice coordinate norm. We are NOT asserting the source printed this Schur constant. It is a derived conservative bound; replacing source metric by another metric requires an explicit equivalence constant.

If positive K_o is the inverse of Sigma_o, then
    K_o >= (1/M_hist) I.                              (R150.C6)
This is a symbolic source-uniform (under the source hypotheses) positivity consumer **for the historical independent-coordinate operator**, not a numerical alpha or an inequality for CMP109.

## 3. Source-shaped 1985→1987 constrained-Hessian criterion

This is the exact **remaining transfer gate** for a common admissible regional carrier, not a claim that this carrier has been constructed.

Let F map new independent coordinates to old independent coordinates on a legitimate shared source Ω and gauge chart, with invertible F and sigma_min(F)>=s>0 in the chosen Hilbert metrics. Let K_n denote CMP109's full reduced constrained-Hessian precision and suppose actual source action/constraint/gauge transport establishes
    K_n=F* K_o F + E,   E*=E,   ||E||<=eta.           (R150.C7)
The defect E must include the **complete** second variation, i.e. action Hessian minus multiplier times constraint second derivative, source gauge/Dirichlet contributions and chart transport. The prior R150 commutator second-jet model is NOT by itself a nonzero E at physical U=1 because source current J=0 there.

The exact Rayleigh bound then gives
    K_n >= (s^2/M_hist - eta) I.                      (R150.C8)
If eta < s²/M_hist, the new precision is positive and its inverse satisfies
    ||K_n^(-1)|| <= 1/(s²/M_hist-eta).                (R150.C9)
This can feed R149's two directional variance solves and R148's Maxwell Gate B without constructing every historical K_o entry. It requires TWO distinctly source-specific certificates: (i) uniform **minimum singular value** s of the actual 1985→1987 chart, and (ii) upper **complete constrained-Hessian defect** eta including residual E_var/E_jet and gauge/collars. **Neither is currently available.** Chart determinant one, the positivity of G^(2) by itself, the identity-background disappearance of J, and the old-source theorem alone do NOT certify the transfer. If the full old/new field spaces, metrics or backgrounds do not match, E cannot even be defined as a difference.

**Crucial interpretation:** CMP99 Theorem 3.15 already solves the old-side *bare covariance bound* obligation. The present bottleneck is **transporting that control to CMP109's genuinely different constrained Hessian** (and then weighting/normalization), NOT missing original CMP99 equation images or an inability to name the old precision. Do not present R150.C8 as a native positivity result.

## 4. Conditional source/domain pass accounting

- SOURCE VERIFIED: original CMP99 (3.157),(3.158),(3.185)–(3.187), including its spectral positivity statement and covariance decay under its paper hypotheses.
- DERIVED ON HISTORICAL SOURCE CARRIER: (R150.C1),(R150.C4),(R150.C5)–(R150.C6), with stated component-norm, graph-distance and source-metric assumptions.
- CONDITIONAL 1985→1987 INTERFACE: (R150.C7)–(R150.C9). No genuine F, eta, s, K_n, complete Ω/Λ comparison or source scale/gauge dictionary is obtained.
- OPEN: CMP109 native positive coercivity, nonlinear source cutoff masses and Jacobian, actual two UV normalized law, mass-gap spectral construction.

**Custody:** append-only R150 source receipt and standard-library lattice-sum verification; R150 remains IN PROGRESS/UNCONSUMED, R149 canonical checkpoint unchanged. **Next bounded source task:** establish a source-legal same-region chart F and compute/bound E (full constrained Hessian, NOT only the jet) in the historical p428 and revised p267 native Hilbert metrics. If source domains cannot be identified, stop rather than supply a synthetic operator.
