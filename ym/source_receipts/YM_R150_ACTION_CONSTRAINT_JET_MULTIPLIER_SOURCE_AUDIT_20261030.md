# YM-R150 continuation — action jet versus constraint jet; Lagrange multiplier custody

**Date:** 2026-10-30. **Prior merged head:** 1aa63c0a010b706715a8f4525ae909149b5edbe2 (R150 historical H1 variational identity). **Status:** exact source-reading correction, conditional finite-dimensional constrained-gradient theorem, and zero-current vacuum specialization. **YM-R150 REMAINS IN PROGRESS / NOT CONSUMED**; canonical R149 machine checkpoint remains unchanged. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 1. Source equations and their actual operations

Original CMP99 user-uploaded typeset 46-page paper, printed p.391–392 (3.7),(3.11)–(3.12), p.421 (3.127)–(3.129), pp.427–428 (3.155)–(3.158). CMP109 original source printed p.266 (2.5)–(2.9), p.267 (2.10)–(2.11) and p.268 (2.12), images inspected in the third-party scan https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf (PDF indices 17–19). See prior R150 source crosswalk and H1 variational-residue receipts. The CMP99 PDF is NOT redistributed.

**LITERATURE FACT / crucial correction:** CMP109 p.266 (2.6)–(2.8) explicitly says the *action/gauge-parameter* quadratic term D^(2) is C^(2) and, together with a neighboring quadratic term, gives the reduced expression 1/2<H1 B', Delta1 H1 B'>+1/2<A1,Delta1 A1>; it cites CMP99 definitions (3.127),(3.128). The resulting (2.8) already contains the action second-order correction. Do **not** add an independent copy of this D^(2)/C^(2) action jet to CMP109 Delta1.

**A DIFFERENT SOURCE TERM:** CMP109 p.267 then relinearizes the nonlinear *coarse constraint* Qtilde(B'), using a special-bond supported h and a quadratic term Ctilde^(2)(B) in its straightening. Its order-zero exponent (2.11) contains +<H1 h Ctilde^(2)(B),J>. In the quadratic energy, this term appears with coefficient -2. This constraint jet is not the previously absorbed action jet, despite similar superscripts. Historical CMP99 p.428 (3.156) separately has -2<H1 Dtilde^(2)(B),J>; it must be compared with the correctly typed new *constraint jet*, not blindly identified with the action jet from (2.7).

## 2. Exact CMP109 constrained-gradient / multiplier factorization

**DERIVATION, source-shaped finite legal chart:** Let E denote the actual finite coarse fluctuation vector space, F the action bond vector space and Y the linearized coarse constraint target (all with source Hilbert metrics). Write D=L Qtilde:E→Y for the normalized linearized constraint on this chosen chart. Assume D is surjective with special-bond-supported right inverse h:Y→E, Dh=I. Let H1:E→F and J∈F. Set j=H1*J∈E.

CMP109 p.267 explicitly says <H1 B',J>=0 for any legal B' satisfying the linearized homogeneous coarse constraint. Translated to the source domain, this is the **condition j|ker D=0** (provided no extra gauge/support restrictions were inadvertently excluded). In finite dimensions, ker D orthogonal complement equals ran D*, and surjectivity makes the multiplier lambda in

    j=D* lambda                                               (R150.J1)

unique. Hence the *source's* quadratic constraint-straightening term is exactly

    <H1 h Ctilde^(2)(B),J>
      = <j,h Ctilde^(2)(B)>
      = <lambda,Ctilde^(2)(B)>.                              (R150.J2)

This identity does not assume J=0, does not estimate lambda, and does not identify CMP99 and CMP109 chart spaces. It only requires the actual source p267 annihilation statement to hold on the complete ker D under examination.

**New pivot-invariance statement:** If h' is another right inverse of the SAME D (Dh'=I) while H1,J and Ctilde^(2) are fixed, then D(h-h')=0 and

    <H1(h-h') Ctilde^(2)(B), J> = 0.                         (R150.J3)

Thus the quadratic *J-pairing* is invariant under a mere change in the distinguished-bond lifting/right inverse, once constrained stationarity is imposed. The full Gaussian coordinate map, physical chi, gauge/chart Jacobian and normalization are NOT rendered pivot invariant by this equation; R145–R148 still stand.

**NEGATIVE RESULT / avoid stationarity confusion:** Constrained stationarity means only j annihilates ker D. It does not imply j=0, J=0, or lambda=0; the normal-direction multiplier can be nonzero. The p267 Ctilde^(2) correction is therefore expected even at a constrained minimizer, and cannot be deleted by invoking the first-order cancellation. A bound needs lambda and the second jet, not merely the linear constraints.

## 3. Exact vacuum specialization

**SOURCE + DERIVATION:** CMP99 (3.7),(3.11) defines the Wilson-action linear current J from the first variation at U. At the identity connection U=1 every elementary plaquette is the identity, the imaginary curvature term is zero and therefore J(1)=0 in the source convention. Accordingly at the identity source vacuum:

    <H1 Dtilde^(2)(B),J(1)>=0,
    <H1 h Ctilde^(2)(B),J(1)>=0.                           (R150.J4)

The CMP99 (3.127) correction inside G1^(-1) is also proportional to J, so it vanishes. These are unconditional zero-current statements on any *otherwise legal* identity chart; they do not require the historical/revised nonlinear jets to coincide.

**This DOES NOT prove** K_new>=K_old at U=1: the averaging constraints, reduced embeddings C_old,C_new, gauge/Dirichlet restrictions and source action quadratic terms may still differ. At nonidentity constrained minimizing backgrounds J need not vanish; zero-current reasoning cannot cover the required background-uniform theorem.

## 4. Revised nonlinear-jet transfer gate

The previous R150 formula E_jet=-2<H1(h Ctilde^(2)-Dtilde^(2)),J> was explicitly **conditional on a common source-typed ambient field space**. R150.J2 now shows that, on CMP109's *own* source chart, its part is -2<lambda_new,Ctilde_new^(2)>. Comparing to CMP99 requires recovering the historical constraint jet in its own correct target and its own multiplier, then a legitimate map between the two target spaces/second jets. It is **not** sufficient to compare h_old and h_new: for one fixed D their difference is invisible to the source quadratic J-pairing, while the physical cutoff pullback is not.

**R150 source outcome:** one spurious action-jet double-counting route is ruled out by printed CMP109 (2.7)–(2.8); the new constrained quadratic jet is a Lagrange-multiplier/second-constraint-jet term and has an exact h-choice invariance; both source jet pairings vanish at the zero-current identity vacuum.

**Still OPEN:** full source admissibility of ker D stationarity on a chosen Ω/collar, explicit old/new nonlinear second constraint derivatives and multipliers on matched targets, E_var action Hessian/metric equality, old/new chart transport and weighted Gaussian normalizers, actual native K and alpha, two R149 directional solves, paired UV laws, continuum OS mass gap.

**Next bounded R150 step:** recover source old/revised second derivative of the coarse constraint and compare multiplier pairings on one common *legal source region*, including any nonlinear second-order term of the transport itself. Do not use another synthetic positive matrix or declare the CMP109 covariance controlled merely because its J term vanishes at U=1.
