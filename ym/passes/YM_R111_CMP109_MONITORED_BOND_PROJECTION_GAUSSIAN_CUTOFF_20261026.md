# YM-R111 — CMP109 monitored-bond projection eliminates the nonlinear cutoff displacement

**Date:** 2026-10-26. **Native predecessor:** [YM-R110](../checkpoints/YM_HEAD_R110_20261026.json), merged main d2dec9be5b82f67c1c674a395132d954751b2cbc. **Scope:** COMPLETE AS PRINTED-SOURCE EXACT PROJECTION IDENTITY AND DIRECT GAUSSIAN CUTOFF TAIL; ACTUAL CHART, INTERACTION, AND PAIRED UV LAW OPEN. **Next:** YM-R112 unconsumed. **Claim:** UNPROVED_RESEARCH_PROGRAM.

## 1. Primary-image checks and a declared legal test parameter

Source: T. Bałaban, CMP109 (1987), scanned original printed pages [PDF mirror](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). Direct printed-page visual recheck: p.253 (0.4), p.254 (0.12), p.265 (2.1),(2.3), p.266 (2.9), p.267 equation for tilde D and constraint-linearizing transform, p.268 (2.12) Gaussian covariance/chi and (2.13) effective E. Zero-based PDF indices 4,5,16–19. [Exact screenshot/location receipt](../source_receipts/YM_R111_CMP109_BOND_PROJECTION_SOURCE_RECEIPT_20261026.md).

For a source-eligible **test of local algebra**, declare L=13 (odd >11 as required by printed p.251), compact G=SU(2), and the explicit CMP109 averaging choice **(0.4)** rather than silently switching to equally source-permitted (0.12). The proof below uses the support property of h and hence applies to either averaging when its source-local analytic hypotheses hold. L=13 and choice (0.4) do NOT construct a full legal input history U, chart, prescribed V, inherited E, or required pair Omega; they merely settle these free *type parameters*. Nothing here certifies a source-admissible two-history block.

## 2. Direct source support identity

Let \(\mathcal B\) be the fine bonds in the step, \(\mathcal B_0=\{b_0(c):c\in T^{(k+1)}\}\) the special bonds singled out by the source linearization, and \(P:E=\mathfrak g^\mathcal B\to E_{\rm mon}=\mathfrak g^{\mathcal B\setminus\mathcal B_0}\) the coordinate restriction to the bonds monitored by Eq.(2.9).

Printed p.267 defines a linear h with values in E, satisfying
\[
 (hz)(b)=0\quad\text{for all }b\notin\mathcal B_0,\qquad
 (hz)(b_0(c))=h(c)z(c).
\]
In particular, \(\boxed{Ph=0}\). The nonlinear constraint-linearizing substitution is printed as
\[
 B_{\rm old}=X-h\widetilde D(X),
\]
where the source obtains an analytic \(\widetilde D\) implicitly from the displayed block constraint equation, with quadratic leading order \(\widetilde D^{(2)}(X)=\widetilde C^{(2)}(X)\) and a higher-order remainder.

Therefore the **entire nonlinear correction lies in ker P**:
\[
 \boxed{P B_{\rm old}=P X,\quad
  P\bigl(B_{\rm old}-X\bigr)=-Ph\widetilde D(X)=0.}\tag{R111.1}
\]

**This is an exact source-specific identity; no smallness bound on \(\widetilde D\) is needed for the monitored projection, beyond the coordinate map being defined.** It does NOT assert \(\widetilde D=0\) or a globally valid analytic chart. The inverse Jacobian and the eliminated variables depend on \(\widetilde D\) and remain in (2.12).

Source Eq.(2.9) is precisely
\[
 \chi_k(B_{\rm old})=
 \prod_{b\notin\mathcal B_0}\mathbf1_{\{\|B_{\rm old}(b)\|<\theta_k\}},
\]
with \(\theta_k=\varepsilon_1\) or \(\theta_k=g_k\varepsilon_1/\gamma_k\) as mentioned immediately beneath (2.9).

Combining with R111.1:
\[
 \boxed{\chi_k(B_{\rm old})=\chi_k(X)\ \text{on the legal chart}.}\tag{R111.2}
\]
The general R110 notation chi_pre(Phi(B)) was formally correct. Its proposed **nonlinear cutoff displacement** delta, however, is exactly ZERO in the seminorm determined by P. R110.4 was an overgeneral entry condition, not an actual obstruction for the (2.9) monitor.

## 3. The actual Gaussian-coordinate cutoff event

Printed pp.267–268 then rescale by \(g_k\), eliminate the special variables using the linearized constraint, and set the resulting full unscaled fluctuation to \(\mathcal C_{k,U} B\), where \(\mathcal C_{k,U}\) is the source embedding operator (called C in (2.12)), while B is the final vector of independent Gaussian coordinates. Consequently
\[
 \boxed{
 \widehat\chi_{k,U}(B)=
 \prod_{b\notin\mathcal B_0}
 \mathbf1_{\{\|g_k(\mathcal C_{k,U} B)(b)\|<\theta_k\}}
 }\tag{R111.3}
\]
on the source's valid coordinate domain. It is a **linear image of the Gaussian B**, not a nonlinear Gaussian box. \(\mathcal C_{k,U}\) is generally not identity; covariance and source background remain nontrivial.

The final covariance is \(\Sigma_{k,U}=(\mathcal C_{k,U}^* A^{(k)}(U)\mathcal C_{k,U})^{-1}\) on independent B variables, if the operator is positive definite on the source physical real domain. The source Gaussian distribution is \(\gamma_{k,U}=N(0,\Sigma_{k,U})\). Let
\[
 S_{k,U}=P\mathcal C_{k,U}\Sigma_{k,U}\mathcal C_{k,U}^*P^*,
\]
the covariance of the **actual monitored field** \(P\mathcal C_{k,U}B\).

No assumption of diagonal/independent bond coordinates is required.

## 4. Exact finite-dimensional cutoff bound without nonlinear error

Choose an orthonormal real basis in \(\mathfrak g\), m=dim \(\mathfrak g\), n=number of monitored fine bonds, and set \(v=\max_{b,a}\operatorname{Var}_\gamma[(\mathcal C B)_{b,a}]>0\). For the formal Gaussian linear event of R111.3,
\[
 q_{k,U}:=
 {\bf P}_\gamma\!\left[\max_{b\notin\mathcal B_0}
 \|g_k(\mathcal C B)(b)\|\ge\theta_k\right]
\]
satisfies the **direct, exact-condition** Gaussian bound
\[
 \boxed{
 q_{k,U}\le
 \min\left\{1,\;2mn
 \exp\!\left[-\frac{\theta_k^2}{2m\,g_k^2\,v}\right]\right\}.
 }\tag{R111.4}
\]
Proof: norm at least theta implies one of m orthonormal components is at least theta/sqrt(m). Each centered scalar Gaussian has variance at most v, so the standard two-sided tail and union bound over mn components prove (R111.4). It requires the covariance's ordinary positive finite-dimensional Gaussian realization but **does not require independence of the correlated monitored bonds**.

Compare R110.4: its delta and its additive gamma(D^c) were only needed to bound a *hypothetical nonlinear displacement of the cutoff*. For the **literal source (2.9) monitored coordinates**, delta=0 and no chart-exit term is needed **inside this formal Gaussian event's probability estimate**. Chart admissibility is still a logically separate requirement for interpreting R111.3 as the physical source integral. A source-defined χ domain outside the (2.9) event, additional conditions in χ_k, or restrictions needed for analytic Jacobian may reduce the actual integration domain. This pass does not assert all such events have the same probability q.

**Two source thresholds, genuinely distinct:**
\[
 \theta_k=\varepsilon_1
 \Rightarrow q\le 2mn\exp[-\varepsilon_1^2/(2m g_k^2 v)];
\]
\[
 \theta_k=g_k\varepsilon_1/\gamma_k
 \Rightarrow q\le 2mn\exp[-\varepsilon_1^2/(2m\gamma_k^2 v)].
\]
Thus the coupling cancels explicitly from the exponent in the alternative branch. The bound can be trivial for large n or covariance variance v; **no positive source uniform/summable rate has been established.** For the declared SU(2) test, m=3; n still depends on the lattice volume and chosen step and is NOT automatically assigned an invented number.

## 5. Minimal covariance rather than full-coordinate pair passport

The Gaussian cutoff depends only on the **monitored marginal** \(Z=P\mathcal C B\sim N(0,S)\), not on all independent Gaussian coordinates B. A two-background comparison of *this particular event* needs the covariance of Z on a genuinely identified common monitored bond set, not a full isomorphism between the independent Gaussian B spaces.

If two legal histories admit **a proved common monitored-coordinate target of the same dimension d**, with positive-definite \(S_0,S_1\), their Gaussian marginal laws obey
\[
 \|N(0,S_1)-N(0,S_0)\|_{\rm TV}
 \le \tfrac12\sqrt{
 \operatorname{tr}(S_0^{-1}S_1)-d
 -\log\det(S_0^{-1}S_1)}.\tag{R111.5}
\]
This is Pinsker plus the centered Gaussian KL formula, and is a less demanding **conditional source cutset** than R110.5's full independent B-coordinate identification. It is not yet a cross-UV-history comparison because no actual common physical monitored bond passport, matched source gauge/background, nor source determinant/E transfer has been constructed. Furthermore these gauge-fixed monitored Z coordinates are NOT automatically gauge-invariant Wilson observables.

## 6. Refute-first ledger

| Question | YM-R111 determination |
|---|---|
| Actual source support h on b0(c) | PRINTED p.267 VERIFIED |
| Eq.(2.9) χ support on bonds excluding b0(c) | PRINTED p.266 VERIFIED |
| Nonlinear D correction affects χ-monitored components | REFUTED by exact Ph=0 |
| Post-rescaling χ in constrained Gaussian coordinates | EXACT LINEAR monitored projection R111.3 ON SOURCE CHART |
| Gaussian cutoff tail | EXACT CONDITIONAL BOUND R111.4; no δ needed |
| Fixed vs coupling-scaled cutoff | DIFFERENT source tail exponents; no rate certified |
| Actual source covariance S and uniform variance | DEFINED FORMALLY VIA SOURCE OPERATORS; NUMERICAL/UNIFORM CONTROL OPEN |
| Nonlinear chart, Jacobian, eliminated b0, interaction oscillation | STILL REQUIRED FOR FULL INTEGRAL |
| Paired admissible Ω,V, M and inherited E, determinant | SOURCE HISTORIES NOT MATCHED |
| True two-UV normalized law defect / summability | OPEN |
| Original images CMP98, CMP102b, CMP109 (0.29),(5.37),(5.42) | OPEN |
| Continuum YM / OS / physical gap | UNPROVED |

## 7. Stop; native YM-R112 unconsumed

R111 resolves the **wrongly attributed nonlinear cutoff displacement** before it can become an MG-scale numerical detour. The nonlinear constraint remains a genuine analytic/Jacobian problem, but **not** for estimating (2.9)'s Gaussian monitored cutoff probability. The next appropriate source-native task is **R112:** at a declared legal CMP109 averaged block, recover or bound the source \(\mathcal C_{k,U}\), \(A^{(k)}(U)\), and \(\Sigma_{k,U}\) strongly enough to estimate S's component variance and volume factor for each threshold. Audit the analytic chart and determinant/E separately, then test an actual common monitored physical carrier or matched prescribed V,Omega for two UV histories. Do not re-open the χ/D displacement or assign false numerical decay.

Historical bibliography upper bound [92] retained; no existence or mass-gap theorem.
