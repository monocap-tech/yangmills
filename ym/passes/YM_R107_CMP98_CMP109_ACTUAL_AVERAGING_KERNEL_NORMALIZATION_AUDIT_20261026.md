# YM-R107 — CMP98/CMP109 source averaging and kernel-normalization audit

**Date:** 2026-10-26. **Native previous:** YM-R106, checkpoint [R106](../checkpoints/YM_HEAD_R106_20261026.json), merge 1e5ecab8f0201cf3ee6794f79d1d78bdd236f181. **Determination:** COMPLETE AS SOURCE-LOCATION / SPECIFIC NONTRANSFER AUDIT; actual two-cutoff law, source-normalized kernel and summability OPEN. **Next:** YM-R108 unconsumed. **Research status:** UNPROVED_RESEARCH_PROGRAM.

## 1. Recovered native-source definitions: CMP98 prototype differs from CMP109 operative choices

Bałaban [35], *Averaging Operations for Lattice Gauge Theories*, CMP98(1), 17–51 (1985), DOI 10.1007/BF01211042, **original-paper third-party OCR** SHA 1442f25d63ef4189608e73bff05c2a359c16c01d:
- OCR lines 69–91: gauge transformation and contour holonomy (6)–(9).
- Lines 94–147, printed p.19: schematic RG delta kernel (10), Lie-algebra linearization (14), and a nonlinear averaged link (15) built from a block sum of logarithms of parallel-transported relative contour holonomies.
- Lines 339–360, printed p.23: one-step average (42), composition (43), locality in neighboring blocks, and gauge covariance.
- Lines 444–480: small-curvature regularity under source hypotheses, OCR-damaged precise exponents.

This average is **not** a single chosen coarse-bond path product and not R106's gauge-invariant physical-loop half-trace.

Bałaban [7], *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP109(2), 249–301 (1987), DOI 10.1007/BF01215223, **original-paper third-party OCR** SHA f1aec083a3a6470c67a2c1205ca740c2583fe37a:
- Lines 181–217, printed pp.252–253: source explains CMP98's earlier averaging was not Euclidean-lattice symmetric; it **modifies** the contour averaging using permutations of shortest coordinate paths, equation (0.4).
- Lines 219–276: distinct analytic symmetric mean of nearby group elements with axioms (0.5)–(0.9), implicit condition (0.10), group-averaged contour variables (0.11), and *another acceptable* gauge-field average (0.12). CMP109 explicitly permits either (0.4) or (0.12). Neither should silently be identified as the uniquely chosen map without checking the consuming step.
- Lines 375–398, printed pp.256–257: variational constrained background is written with the **source averaging** M^k(U)=V, equation (0.21), and uniqueness of the regular critical orbit is attributed to Bałaban [41] CMP102b. This is direct CMP109 source prose/cross-reference, not independent original-image verification of CMP102b.
- Lines 935–1000: source fluctuations, sharp small-field restriction, Gaussian normalization and interaction in (2.10)–(2.13).

**R107 source-positive determination:** the actual coarse prescribed variable is an M^k-averaged gauge field in a declared regularity/gauge domain. The R106 Wilson-loop cospan is only an external test observable. CMP98's prototype average does not fix which CMP109 Euclidean-symmetric operation is used in a specific full two-run history. Source formulas' exact symbols still require printed-page image checks.

## 2. CMP109 kernel is not automatically a Markov pushforward

CMP98's introductory (10) uses a symbolic delta constraint between coarse V and averaged U. CMP109 (0.13), lines 277–289, instead introduces a **general gauge-invariant kernel transformation**
\[
 (T\rho)(V)=\int t(V,U)\rho(U)\,dU.
\]
The text in (0.14)–(0.17), lines 283–338, imposes regular/small-field restrictions, symmetric gauge-fixing, characteristic factors and the Faddeev–Popov transformation. It specifies an action **reference normalization** N_0 by evaluation of the corresponding integral at the identity coarse background V=1. That reference value is not *by its definition* the total integral of the resulting density over V. CMP109 (2.12)–(2.13) similarly involves normalized Gaussian internal coordinates and special source action normalization; these do not automatically equate independently cutoff-indexed full physical laws.

Hence the shortcut "RG by averaging implies (M)_* mu at every cutoff" is unjustified without exhibiting a globally admissible map/kernel, correct density/gauge/cutoff factors and normalization, especially across independently chosen UV bare actions. This is a **failure of automatic inference**, not a claim of error in CMP109.

## 3. Exact normalized positive-kernel decomposition (self-contained)

Let (X,mu) be a probability space, (Y,m) a sigma-finite measured space, and nonnegative measurable t(y,x) with
\[
 \kappa(x)=\int_Y t(y,x)\,m(dy),\qquad 0<C=\int_X\kappa(x)\,\mu(dx)<\infty.
\]
Define
\[
 \nu(dy)=C^{-1}\!\int_X t(y,x)\mu(dx)\,m(dy).
\]
On kappa-positive inputs define K(dy|x)=t(y,x)m(dy)/kappa(x), and define the **tilted input law** mu^kappa(dx)=kappa(x)mu(dx)/C. Then
\[
 \boxed{\nu(dy)=\int_X K(dy|x)\,\mu^\kappa(dx).}\tag{R107.1}
\]
**Proof:** substitute and cancel kappa under the integral; the kappa-zero set has zero tilted mass. Tonelli supplies the normalization. The *original-input Markov case* follows if kappa(x)=1 almost everywhere. A deterministic pushforward follows when K(dy|x) is the point mass at a lawful M(x) and the input is not reweighted. These hypotheses are not verified for native CMP109 t.

**Negative control:** X=Y={0,1}, mu=(1/2,1/2), t(y,x)=kappa(x) 1_{y=x}, kappa(0)=1,kappa(1)=2. Normalized output = (1/3,2/3), versus the identity map pushforward (1/2,1/2). This is an abstract finite counterexample, not Bałaban's kernel.

If CMP109's reference-field action normalization is N_ref rather than C, the output density divided by N_ref has total mass C/N_ref, not automatically one. **First concrete source-specific law gate**: identify t(V,U), chi/gauge factors, kappa(U), C and N_ref in an actual CMP109 step, and prove their required relation or carry the input tilt. Only then derive the distributions of actual M-derived prescribed V on two cutoff histories.

## 4. Small-field chart control and native pair passport

No globally conjugation-equivariant Lie-algebra logarithm ell:SU(2) -> su(2) with exp(ell(g))=g can exist on all SU(2): at the central -I, equivariance makes ell(-I) invariant under every adjoint action, forcing it into the zero Lie-algebra center and yielding exp(0)=I, contradiction. This elementary point **does not** exclude restricted charts, almost-everywhere measurable averages, or an alternative global construction. It forbids a careless all-field extension of the source logarithmic chart.

At one aligned physical block, the next native comparison must type, separately for each cutoff:
\[
 (\eta,\Omega,M^j,V,t,\chi,\kappa,C,N_{\rm ref},\text{gauge chart},\mu,F).
\]
Source-prescribed V is not a gauge-invariant loop trace. Pair admissibility still requires the *actual* nested domains and identical determining data (or controlled discrepancies). The exact R106 conditional-law estimate only applies once legitimate normalized data marginals, paired-fiber observable estimates and large-field masses have been established. No such source-native numerical or summable defect was found.

## 5. Refute-first decision and stopping point

| Gate | R107 determination |
|---|---|
| CMP98 contour-logarithm averaging; locality/composition | SOURCE-PAPER OCR LOCATED, equations publisher-image OPEN |
| CMP109 Euclidean-symmetric (0.4), group contour mean (0.10)–(0.11), alternative (0.12) | SOURCE-PAPER OCR LOCATED; operative choice/source formula image OPEN |
| CMP109 M^k(U)=V fixed-average variational carrier (0.21) | SOURCE-PAPER OCR LOCATED; CMP102b original formulas OPEN |
| CMP109 kernel (0.13), small field/gauge (0.16)–(0.17), N_ref at V=1 | SOURCE-PAPER OCR LOCATED; global stochasticity not verified |
| Normalized positive-kernel input tilt | EXACT ABSTRACT PROOF R107.1 |
| Full Wilson measure is automatically source t-pushforward with correct marginals | GENERAL INFERENCE REFUTED by two-point counterexample |
| Native actual kappa/C/N_ref, paired source M, Omega,V and observable laws | OPEN |
| Full beta, Eq.(0.29), original CMP109 (5.37),(5.42), OS and physical mass gap | OPEN |

**YM-R108 next, unconsumed:** verify printed CMP98/CMP109/CMP102b equations by original-page images where possible; select the CMP109 averaging (0.4) or (0.12) used in a specific one-step construction and a concrete aligned block. Recover the actual positive kernel t, gauge-fixing/cutoff factors and normalization, compute its fiber mass or a lawful conditional disintegration, and test the induced two-run M-derived V distributions. Require source-specific estimates or record the exact obstruction; do not replace a source kernel with a toy delta map. Historical bibliography remains [92]; no external unverified candidate theorem or mass-gap conclusion promoted.
