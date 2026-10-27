# YM-R117 — CMP99 gauge-averaging intertwiner and the coarse-representative seam

**Date:** 2026-10-27. **Resume:** [YM-R116](../checkpoints/YM_HEAD_R116_20261027.json), main 36a786de0c6f4f6d0a26f9ea55050f9802d48c18. **Status:** COMPLETED as a SOURCE-LOCATED exact gauge/averaging intertwining identity, a rigorous one-layer gauge-section change, a coarse-representative countertest, and a two-source compatibility type gate. **OPEN:** full CMP99 multiscale region/source original-page images, CMP109 averaged operator matching, CMP99 later Delta_k/A_k normalization, native covariance and two-UV laws. **Next:** YM-R118 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 0. Source and custody

Published Bałaban [CMP99](https://doi.org/10.1007/BF01240355), *Propagators for lattice gauge theories in a background field*, CMP99(3), 389–434 (1985). Directly read pinned original-paper **third-party OCR**, Git blob ce5af9ff9165b3e1a995f4c141c0bc0ca9fc6743 in chboishabba/dashi_agda, at lines 192–263, **1427–1463**, 1895–1938 and 1990–2040. CMP99 original printed page images **not obtained**. The decisive identity is clearly preserved in the text even though several formulas are damaged. [R117 receipt](../source_receipts/YM_R117_GAUGE_INTERTWINING_CMP99_CMP109_SOURCE_RECEIPT_20261027.md).

Published Bałaban [CMP109](https://doi.org/10.1007/BF01215223), 109(2), 249–301 (1987). Original printed p.253–255 (0.4),(0.12)–(0.16) and original p.265–268 (2.1)–(2.13) were previously image-inspected in the third-party 54-page [printed scan](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). Re-read original-paper OCR f1aec083a3a6470c67a2c1205ca740c2583fe37a, lines 175–273, 287–319. CMP109 explicitly says the previous averaging definition [12] was modified to restore Euclidean symmetry; (0.4) and (0.12) are two source-permitted newer alternatives. **Do not silently identify** the CMP99 older Q_j from its cited [5] with the derivative of CMP109 new M from (0.4).

R116 proved that CMP99 hard gauge R projects onto Delta E with E=ker Q' and that its normalized hard FP coordinate is Ghat=Delta^{-1} R D*. The old source **hard-gauge rank is closed on its own E**, not identified with CMP109 based gauge functions. R117 asks whether the DIFFERENCE of gauge sections is a real physical obstruction or only a coarse-gauge representative defect, and which exact source averaging operation carries it.

## 1. Literature source fact: the averaging/gauge-gradient square COMMUTES

CMP99 (3.13)–(3.15) writes each field average Q_j as a composition of one-step averages from its historical source, and (3.18)–(3.19) defines a related average Q'_j of infinitesimal gauge *site* functions. On printed p.418, OCR lines **1427–1463**, differentiating the *nonlinear covariance of the source average* gives
\[
 \boxed{Q_1(U)D_U=D_1Q'_1(U)\quad\text{(CMP99 3.114)},}\tag{R117.1a}
\]
and by composition
\[
 \boxed{Q_j(U)D_U=D_j Q'_j(U)\quad\text{(CMP99 3.115)}.}\tag{R117.1b}
\]
The exact directional/lattice powers and covariant transport notation should be checked in original printed CMP99 images; the structure is readable and the surrounding source prose explicitly states that the averages Q_j A are invariant under infinitesimal gauges lambda with Q'lambda=0. The project records it at SOURCE-PAPER-OCR level, not printed-image verified.

If lambda belongs to **the source's full multiscale space E=ker Q'**, then for every prescribed shell layer j where Q'_j lambda=0,
\[
 Q_j D_U\lambda=D_jQ'_j\lambda=0.\tag{R117.2}
\]
This is a direct and exact source **fixed-average gauge orbit condition**. Merely having lambda(y)=0 at selected coarse vertices is NOT a substitute for Q'_j lambda=0.

The exact square also explains R116's interface term: if a gauge-parameter change creates a nonzero averaged site parameter a=Q'_j lambda, its impact on coarse averaged bond fields is the coarse gauge gradient D_j a, not an arbitrary source amplitude.

## 2. Derived one-layer gauge-section isomorphism with background-dependent Q'

**Theorem R117.3 — one-layer quotient transport (derived).**
Let H_site be finite-dimensional real Lie-site functions on a region with **disjoint one-layer blocks**. Let E_y:H_site→H_coarse evaluate at their designated coarse centers, and let iota:H_coarse→H_site be a chosen coarse lift with E_y iota=I (piecewise-constant in a fixed identity-background gauge is a valid test). Let Q':H_site→H_coarse be the source-shaped site average from CMP99 (3.19) at one layer and on its chosen regional domain. Assume the square operator
\[
 A_{Q'}:=Q'\iota:H_{\rm coarse}\to H_{\rm coarse}
\]
is invertible. Define
\[
 J_{y\to Q'}=I-\iota A_{Q'}^{-1}Q',\qquad
 B_{Q'\to y}=I-\iota E_y.\tag{R117.3}
\]
Then J maps ker E_y to ker Q', B maps ker Q' to ker E_y, and their restrictions are inverses. Proof: Q'J=Q'-Q'iota A^{-1}Q'=0; E_y B=0. B J lambda=lambda for E_y lambda=0, since E_y J lambda=-A^{-1}Q'lambda. J B mu=mu for Q'mu=0, since Q'B mu=-A E_y mu. This is an **exact section isomorphism**, not equality of gauge actions on bonds.

At the SU(2) identity reference and **uniform one-layer site average**, Q'iota=I and the formula reduces exactly to R116's piecewise mean-subtraction J lambda=lambda-iota bar(lambda). The earlier sharp inverse operator norm sqrt(n)=L²=169 for L=13 in the declared unweighted isolated-block model is retained. This value is not an actual CMP99 full nested Q' operator norm.

For nontrivial backgrounds, source (3.19) involves parallel-transported gauge parameters. If on each block the chosen lift satisfies a source-verified **small average-transport perturbation** ||Q'iota-I||≤eta<1 (same coarse norm), then A is invertible and
\[
 \boxed{\|A^{-1}\|\le(1-\eta)^{-1}.}\tag{R117.4}
\]
Proof: Neumann series. In the specific one-layer formula as an average of orthogonal SU(2) adjoint parallel transports, a sufficient condition is sup_{y,x}||Ad_{U(\Gamma_{y,x})}-I||≤eta. **No actual CMP99 uniform chart/collar estimate eta is established here**, and the general multiscale source Q' may not even have the same square target H_coarse. Thus (R117.4) is an ENTRY TEST, not a source covariance constant.

## 3. Exact interface correction is a COARSE GAUGE COB0UNDARY, not a physical random defect

For lambda∈ker E_y, set a=A_{Q'}^{-1}Q'lambda. From R117.3,
\[
 J\lambda=\lambda-\iota a,\qquad
 \boxed{D_U(J\lambda)-D_U\lambda=-D_U(\iota a).}\tag{R117.5}
\]
At the identity vacuum with piecewise-constant lift iota, D=d and the right side VANISHES on any bond whose endpoints lie inside the same block and equals \(-[a_{B'}-a_B]\) on a fine bond crossing blocks B,B'. This is the exact interface cochain of R116, now correctly classified as **the gradient of a lifted COARSE SITE GAUGE PARAMETER**, not an independent non-gauge field.

For the CMP99 older average, applying the SOURCE intertwiner R117.1 (when domains/layers actually match) gives
\[
 Q_1 d(J\lambda)=D_1Q'_1(J\lambda)=0,\quad
 Q_1 d\lambda=D_1Q'_1\lambda,\quad
 Q_1d(\iota a)=D_1(Q'_1\iota)a.\tag{R117.6}
\]
For the uniform identity one-layer lift \(Q'_1\iota=I\), the coarse mismatch is **exactly** \(D_1a\). Therefore:
- If coarse data \(V\) are fixed as a particular representative, \(D_1a\ne0\) is a real **prescribed-representative compatibility obstruction**.
- If the comparison is made in the properly defined quotient of coarse connections by the same allowed coarse gauge group and **coarse observables are gauge invariant**, the extra exact gradient may act trivially on the observable. At the linearized identity, any closed Wilson-loop sum of da vanishes. For non-Abelian full group variables, this must be promoted through a genuine source nonlinear equivariance action, not merely a linear sum.

**Explicit source-shaped refutation test**: on two adjacent disjoint identity blocks choose a based parameter lambda which vanishes at coarse centers but has nonzero mean a on just one block; with suitable interior support, this is compatible with a finite region Dirichlet boundary in the test. CMP109 source (0.13)–(0.16) is invariant under fine gauge u(y)=1 and therefore fixes its **new** averaged M(V) under that based transformation; CMP99 (3.114) instead gives a nonzero coarse gradient \(D_1a\) for its **older** average Q_1. They are **not automatically identical source tangent averaging maps on those gauge directions**. This is a strict local algebraic witness to the missing CMP99/CMP109 averaging crosswalk, NOT a counterexample to gauge-invariant Yang–Mills physics or proof of mismatch for every regional shell.

### Multiscale/geometry type hold

The ACTUAL CMP99 Q' of (3.18) has shell outputs on annuli \(\Lambda_j\) for j=0,...,k; \(\ker Q'\) means all the relevant shell restrictions vanish. The one-layer E_y and H_coarse of R117.3 are therefore not automatically of the same rank or codomain as the nested full source Q'. A single blockwise J does **not** certify all Q'_j(Jlambda)=0, nor preservation of Dirichlet/collar constraints and selected Ω under the full RG sequence. Any global transfer must supply a **rank-compatible multiscale lift** iota_nested and an actual invertible/controlled Q'_nested iota_nested, or an equivalent staged triangular factorization, while matching the identity-background source averaging choice. CMP109 (0.4) must be related to CMP99's historical averaging derivative explicitly; saying “both gauge covariant” is insufficient.

## 4. Independent source precision gate remains genuinely unclosed

CMP99 original-paper OCR, lines 1895–1938 (printed pp.427–428): the Gaussian quadratic is A_k in (3.156), later covariance representations are related by (3.157)–(3.158), and the ensuing lower-bound sentence names **C*Delta_k C**. The formulas have damaged symbols; printed equation images still UNVERIFIED despite searches for the publisher DOI scan, Springer/Project Euclid and third-party mirrors. Do not assert any exact equality among C*Delta_k C, C*A_k C, the physical hard-gauge H0 or the CMP109 reduced Q; neither R116's Delta_a=A identity on its earlier joint slice nor R117's gauge cochain permits that unverified transfer.

The net R117 obligation graph is:
- **G1 (gauge):** CMP99 source E=ker Q'_nested, actual regional Dirichlet/collar, blockwise versus multi-layer based lift and cochain.
- **G2 (averaging):** CMP99 *historical* Q_j and CMP109 newly chosen (0.4) or (0.12) averaged operator and their derivative on the SAME input bond/chart.
- **G3 (precision):** later source Delta_k/A_k covariance/determinant normalization, original (3.157)–(3.158), source hard-to-soft H0 lower-bound applicability.
- **G4 (history):** prescribed physical Ω,V, inherited E, background determinants and true normalized two-ultraviolet-cutoff probability laws.
All four have open hypotheses; no source-uniform cutoff mass/TV bound, continuum OS reconstruction, or physical spectral gap follows.

## 5. Bounded determination / next cursor

| Gate | R117 disposition |
|---|---|
| CMP99 Q_j D = D_j Q'_j | ORIGINAL-PAPER SOURCE TEXT (3.114)–(3.115) LOCATED, original image open |
| E=ker Q'_nested fixed-average gauge | EXACT source algebra under layer restrictions |
| One-layer based/mean-zero/transported-average section | R117.3 DERIVED when Q'iota invertible |
| Small near-vacuum adjoint perturbation inverse | R117.4 CONDITIONAL with explicit eta |
| R116 inter-block discrepancy | RETYPED as coarse lifted gradient / prescribed representative seam |
| CMP99 old Q vs CMP109 new M tangent | SOURCE-DEFINITION INCOMPATIBILITY GATE; explicit one-layer nontransfer witness |
| Full nested Q' lift and source Ω/Dirichlet | OPEN |
| Later CMP99 Delta_k/A_k images, CMP109 coercivity | OPEN |
| Two actual UV histories and Yang–Mills gap | OPEN, UNPROVED |

**YM-R118 unconsumed:** prioritize (i) actual multiscale annular Q'_j ranks and a stage-by-stage site gauge lift that respects the source's Dirichlet/Ω collars, with a single fixed choice of CMP109 averaging; (ii) the derivative of old CMP99 Q_j versus new CMP109 M on the same bond variables, checking whether their differences are exactly coarse gauge derivatives or involve physical components; (iii) recover CMP99 later covariance formula images or a fully legible original-paper equivalent before importing the γ0 bound. No further abstract gauge positivity pass and no invented two-cutoff estimate. No physical mass-gap proof.
