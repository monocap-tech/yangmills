# YM-R20 — irrelevant-remainder / inductive-norm audit

Date: 2026-09-15
Status: COMPLETE
Claim status: UNPROVED RESEARCH PROGRAM
Prior head: `YM_HEAD_R18_20260915.json` / YM-R19 completion in live thread
Next cursor: `YM-R21` (unconsumed)

## 1. Target

Audit the two defects introduced by replacing the hard Bałaban block constraint by the reflection-adapted soft kernel:

1. the quadratic soft-hard defect

\[
E_a=\Delta_a-\Delta_\infty
=-a^{-1}\Delta_\infty^2(I+a^{-1}\Delta_\infty)^{-1},
\]

2. the nonlinear analytic remainder

\[
R_{\ge 3}(A,B).
\]

Determine whether these are genuinely irrelevant in the 4d ultraviolet RG sense, or whether they contaminate the marginal Yang–Mills coupling.

## 2. Quadratic defect: dimension-six

At small momentum the hard coarse kinetic operator behaves as

\[
\Delta_\infty(p)\sim p^2.
\]

Therefore

\[
E_a(p)\sim -a^{-1}p^4+O(p^6).
\]

In four dimensions a gauge field has canonical mass dimension one. A quadratic local operator of the form

\[
\int d^4x\, A\,\partial^4 A
\]

has canonical dimension six. Its coefficient has dimension minus two. Under one RG step with length rescaling factor \(L\), its dimensionless coefficient therefore gains the tree-level factor

\[
L^{4-6}=L^{-2}.
\]

Thus the soft-hard quadratic mismatch is a leading irrelevant operator, not a mass term or a new marginal kinetic term.

This is consistent with Symanzik's pure-gauge continuum-improvement analysis, where the leading lattice-action corrections are dimension-six operators and hence produce \(O(a_{\rm lat}^2)\) effects. [68]

Near the asymptotically free fixed point anomalous corrections can perturb the exponent, so the safe target is

\[
L^{-2+O(g_k^2)},
\]

which remains a strict contraction for sufficiently small \(g_k\).

## 3. Important qualification: positivity

Dimension-six improved gauge actions need not themselves be reflection positive; Lüscher–Weisz [11] show that generic dimension-six additions can lead to nonstandard transfer-matrix properties.

This does not invalidate the present kernel route, because reflection positivity is being carried by the exact half-space-factorized blocking kernel, not inferred from a standalone truncated improved action. The derivative expansion of \(E_a\) is used only for UV typing and localization. It must not replace the exact coarse measure when RP custody is required.

## 4. Nonlinear remainder is not wholly irrelevant

The normalized weak-field kernel has the schematic expansion

\[
S_{\rm block}(A,B)
=
\frac a2\|B-QA\|^2
+gR_3(A,B)+g^2R_4(A,B)+\cdots.
\]

It is incorrect to classify all of \(R_{\ge3}\) as irrelevant merely because it is cubic or higher in fields. The marginal Yang–Mills density

\[
\frac14\int \operatorname{tr}F_{\mu\nu}F_{\mu\nu}
\]

itself contains quadratic, cubic, and quartic gauge-field vertices.

Therefore the nonlinear blocking remainder can project onto the same marginal local operator and shift the effective coupling.

## 5. Required local extraction

The correct decomposition is

\[
R_{\ge3}
=
\delta c(g,a)\,\mathcal O_{F^2}
+R_{\rm irr}
+\text{vacuum/total-derivative pieces},
\]

where

\[
\mathcal O_{F^2}=\int d^4x\,\operatorname{tr}F^2.
\]

For a real reflection-symmetric / CP-even kernel, a CP-odd \(\operatorname{tr}F\widetilde F\) term is excluded. Gauge covariance forbids a gauge-boson mass term. After vacuum normalization and coupling extraction, the first generic local gauge-invariant residual operators have canonical dimension six.

The coupling shift can be written perturbatively as an analytic finite scheme redefinition

\[
g' = g+c_1(a)g^3+c_2(a)g^5+\cdots.
\]

The first two Yang–Mills beta-function coefficients are scheme-independent under such analytic redefinitions with the same leading normalization; this was already custodied under [51]. Hence the soft kernel is allowed to change the UV coupling coordinate without changing asymptotic freedom at its universal leading orders.

## 6. Residual power counting

After the marginal extraction,

\[
R_{\rm irr}=\sum_i c_i\mathcal O_i,
\qquad \dim \mathcal O_i\ge6.
\]

Tree-level rescaling gives

\[
c_i'\sim L^{4-d_i}c_i,
\]

hence at least

\[
\|R_{\rm irr}'\|\lesssim L^{-2}\|R_{\rm irr}\|
\]

before weak anomalous/logarithmic corrections.

The pure-gauge Symanzik literature independently confirms that the leading symmetry-allowed lattice artifacts are dimension-six. [68]

## 7. What is actually proved versus inferred

### Derived

- \(E_a(p)=O(p^4)\) once \(\Delta_\infty(p)=O(p^2)\).
- Its canonical RG eigenvalue is \(-2\) in 4d.
- Cubic/quartic field order does not imply irrelevance because \(F^2\) contains cubic/quartic vertices.
- The nonlinear remainder must first be projected onto the marginal Yang–Mills operator.
- After gauge/symmetry-constrained marginal extraction, generic residual local gauge operators begin at dimension six.

### Literature-supported

- Bałaban constructs localized effective actions and a recursive coupling renormalization in the 4d small-field regime [7].
- Part II proves the cluster terms satisfy the inductive assumptions [21].
- Pure-gauge Symanzik improvement identifies dimension-six operators as leading irrelevant corrections [68].
- The first two beta-function coefficients are universal under ordinary analytic scheme changes [51].

### Not proved here

The crucial constructive estimate

\[
\|R_{\rm irr,k+1}\|_{\rm Balaban}
\le
C L^{-\eta}\|R_{\rm irr,k}\|_{\rm Balaban}
\]

for the *specific soft-kernel-generated remainder*, with cutoff-uniform constants and all large-field/localization machinery included, has not been found in the literature and is not derived by canonical power counting alone.

Likewise, it remains to prove that the extracted coefficient \(\delta c(g,a)\) fits the precise Bałaban coupling-recursion hypotheses without producing extra marginal structures.

## 8. Main determination

R20 therefore closes neither as failure nor as full inductive closure.

The modification decomposes naturally as

\[
\boxed{
\text{soft kernel}
=
\text{Bałaban quadratic family}
+\text{finite coupling-scheme shift}
+\text{dimension-6+ remainder}.
}
\]

The first two pieces are structurally admissible. The remaining theorem deficit is a quantitative **local-extraction / polymer-norm closure theorem** for the dimension-six-plus remainder.

The live frontier is therefore not 'is the kernel irrelevant?' but:

> Can the soft-kernel local functional be projected onto Bałaban's marginal coupling coordinate with a remainder satisfying the same analytic/localized polymer estimates as his native fluctuation activities?

## 9. Next frontier

`YM-R21 — local extraction / coupling-coordinate audit`

Tasks:

1. identify Bałaban's exact marginal extraction used to define the recursive coupling constant;
2. express the soft-kernel local functional in the same coordinate system;
3. compute/characterize its projection onto the plaquette / \(F^2\) coupling;
4. show the residual Taylor jet starts at the irrelevant order required by the inductive assumptions;
5. test the relevant Cauchy/analytic and polymer-support constants rather than relying only on engineering dimension.

No continuum Yang–Mills construction or mass-gap theorem is claimed.