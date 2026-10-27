# YM-EXT-01 — external YM4 claims versus native R104/R105 frontier

Date: 2026-10-26  
Repository: monocap-tech/yangmills  
Workstream: **YM-EXT-01 / comparison stage completed, no mathematical native gate closed**  
Native head at start/end: **YM-R104**. **YM-R105 unconsumed**.  
Status: **EXTERNAL_CANDIDATE_THEOREM_FOUND; HYPOTHESIS_TRANSFER_UNVERIFIED; EXTERNAL_PROOF_INCOMPLETE**.  
Evidence: [source receipt with pinned blobs, precise lines, and text-inspection limitations](YM_EXT_01_SOURCE_RECEIPT_20261026.md).  
Not a Yang–Mills existence, mass-gap, formalization or priority claim.

## 1. Main finding

The external Sussman–Alpöge long-form YM4 account is **closer to the exact native missing theorem than earlier source-only work suggested**. In its Part III, Chapter 9, it proposes a specific **paired-variational-problem** construction with one extra ultraviolet lattice and a relative background gauge transform, then derives an explicit comparison of constrained covariances **and their square roots**, and a second-moment bound for the one-loop beta coefficient.

However, this is a predominantly AI-generated, publicly tentative account; its own Chapter 13 lists numerous explicit unproved hypotheses. The strongest comparison statements are therefore **candidate conditional arguments**. They have not been independently verified or transplanted into this repository.

**Evidence categories here:**
- **SOURCE LOCATED**: the relevant external proposition/theorem and its prerequisites were actually inspected in the pinned TeX.
- **CANDIDATE CONDITIONAL ROUTE**: a concrete argument that might satisfy a native gate, only if all assumptions and identities are checked independently.
- **SAME OR ADJACENT GAP**: manuscript expressly marks an issue unproved, closely related to our requirement; this is not a claim the two mathematical statements are equivalent.
- **NO TRANSFER ESTABLISHED**: the currently inspected evidence cannot be used to change a native gate from OPEN.
- **OUT OF MODEL**: an observation from a different mathematical theory (e.g. classical O(N) or QED3), informative but not a direct YM4 theorem.

## 2. Hypothesis-by-hypothesis crosswalk

| Native target (R104/R105) | External object and exact inspected location | Required transfer not yet established | Verdict |
| --- | --- | --- | --- |
| **Actual two-cutoff backgrounds on one relative chart** | Paired variational setting III:34660–34734; stationarity of minimizers III:35626–35641 proposes \(W^{\mathsf u}=e^{i\eta A}U_{\mathfrak B}\), \(\|A\|_\theta\le C_A\varepsilon\eta^\theta\). | Our actual UV histories must have nested \(\Omega'_{j+1}=\Omega_j\), equal shared-layer data \(V'=V\), small real curvature, admissible gauge fixing, and the source's scales/norms. Its minimizer existence and locality dependencies are not externally certified. | **CANDIDATE CONDITIONAL ROUTE**; native chart gate OPEN. |
| **Constrained Gaussian covariance and root** | External theorem III:36675–36807 proposes \(\|\delta C^{(k)}\|_\delta,\|\delta(C^{(k)})^{1/2}\|_\delta,\|\delta\Delta^{(k)}\|_\delta,\|\delta\Gamma_k\|_\delta\le C L^{-\theta k/8}\); precision \(T_k=C(V)^*\Delta^{(k)}C(V)\); inverse and square-root resolvent identities III:36766–36782. | Need verify entire upstream paired-minimizer and jet chain, the source’s uniform coercivity and weighted kernel calculus, true matching of Gaussian dimensions/normalization/constraints on all relevant regions, and the native definition of the two cutoff carriers. | **SOURCE LOCATED / CANDIDATE CONDITIONAL ROUTE**; native carrier/root gate OPEN. |
| **Fixed-background propagator motion** | External account references CMP99(3) bounds and includes fine-propagator comparison proposal III:37365–37482. | That proposed fine \(G',G,G_1\) stationarity is explicitly marked **Proof outstanding**; gauge-fixing form not nested and random-walk junctions are not minimizer derivatives. Our R104 fixed-domain resolvent response does not automatically fill that need. | **SAME OR ADJACENT GAP**; native fine-propagator gate OPEN. |
| **One-step vacuum-polarization / marginal coefficient** | External theorem III:36809–36935 compares \(\Pi_l=\partial^2\log Z^{(l)}\), including determinant and Jacobian, and claims \(|\beta^0_{l+1}-\beta^0_l|\le C L^{-\theta l/8}\). | Verify external covariance theorem and derivative kernels; identify \(\beta_l^0\) with our precisely typed *one-loop* subcomponent (not the entire native \(\beta_l\)), check physical scale and normalization; convergence to \(c_0\) needs external offset assumptions. | **CANDIDATE CONDITIONAL ROUTE** for one-loop gate only; full native beta gate OPEN. |
| **Inherited history-dependent \(E\) and large-field two-run response** | I:61295–61350 relative label format proposition explicitly proof outstanding; III:32417ff modulus majorant proof outstanding; III:34033ff forgetting theorem assumes that majorant; Chapter 13 III:111269–111275 lists nested Gaussian-integral difference proof outstanding. | Need relative history estimates for *actual* RG law and moving large-field regions, plus uniform summation/normalizations. A conditional \(q^{a+1}\) forgetting factor does not come for free. | **SAME OR ADJACENT GAP**, not solved. |
| **Localization/weakening transfer through CMP116** | External proposed bypass of fine propagator response: localize sandwiched \(T_\square\) resolvent and \(\log\det T\) (III:37455–37478). Separate seam transfer theorem I:53445ff is conditional on source/geometry/radius inputs. | Prove the bypass actually localizes the needed step outputs with uniform marked rooted norm, analytic radius, positive term summability and native weakening/Mayer channels. No such completed external proof was verified. | **POSSIBLE BYPASS DESIGN**, native CMP116 gate OPEN. |
| **Cross-cutoff exact paired-shell comparison / uniqueness** | III:37533–37560 and 37611–37633 expressly mark pairing of the zeroth-order two-cutoff response on required shells unproved. | Require re-basing covariance, radius shrink once per object rather than each RG step, constants uniform under repeated comparison and exact point/shell identifications. | **SAME OR ADJACENT GAP**; no fully transported comparison. |
| **Torus/site locality and beta extraction** | I:58187ff theorem yields intrinsic nonwrapping terms and site-free \(\beta_j\), *assuming* multiple operator and large-field statements. II:89995–90034 explicitly leaves termwise covariance and torus exponential comparison incomplete. | Site-free within one level is distinct from cutoff-depth stationarity; termwise Euclidean covariance cannot be inferred from covariance of the summed functional. | **CONDITIONAL LEAD / SAME GAP**. |
| **Bałaban Eq. (0.29) positive-\(\alpha\) residual** | External text distinguishes \(\beta_j\) and residual \(V_X^{(j)}\), e.g. II:89918–89922, and contains RG remainder machinery; no direct **verified** certificate for our precise native Eq.(0.29) bound was established in this audit. | Primary-page Eq. (0.29)/(5.37)/(5.42) still on image hold; must locate external complete residual estimate with source-normalized constants and verify its exact domain/scale. | **NO TRANSFER ESTABLISHED**; native gate OPEN. |
| **Continuum/OS existence / positive physical gap** | External README declares long apparent YM4 existence argument unverified; Part III Chapter 13 lists numerous proof holes, including large-field rarity, source/kernel comparisons and several global/IR steps. | Requires coherent whole-construction proof, not conditional local stationarity. The public external account does not certify a Clay existence-plus-gap solution. | **UNVERIFIED, NOT ADOPTED**. |

## 3. Distinguish a potential breakthrough from actual theorem closure

The new finding is **not merely that another program mentions Bałaban or covariance**. It supplies a concrete, inspectable candidate lemma for a previously unfilled *native* comparison requirement:

For successive determining sets \(\mathfrak B,\mathfrak B'\) satisfying the external paired hypotheses, the account claims a common-gauge relative background
\[
M(U')^{\mathsf u}=e^{i\eta A}U_{\mathfrak B},\qquad
\|A\|_\theta\le C_A\varepsilon\eta^\theta,
\]
and then a normalized small difference between \(\Delta^{(k)}\), \(C^{(k)}\), \((C^{(k)})^{1/2}\), and \(\Gamma_k\) under the one-lattice shift, with rate \(L^{-\theta k/8}\).

This is strictly stronger in *intended scope* than our R104 same-domain resolvent:
\[
\|G(U_1)-G(U_0)\|\le\|G(U_0)\|\,\frac{q}{1-q},\qquad
q=\|V(A)G(U_0)\|<1,
\]
because the external candidate also tries to **construct the needed relative \(A\)** and compare constrained covariances/roots. However, its correctness and physical transfer remain unverified. No source uniformity should be inferred from the superficial similarity of notation.

**Why the external theorem does not automatically discharge YM-R105:**
1. The theorem first posits exactly paired variational problems with same shared-layer data; the actual histories and large-field/collar transitions must be put in that form.
2. The proof builds on named minimizer/jet/one-step data results and published source assertions. The account's own Chapter 13 says some necessary earlier minimizer and gauge/large-field statements remain unproved.
3. The covariance theorem treats the **sandwiched** Gaussian precision. The account explicitly says the **unsandwiched fine propagators** required for random-walk junctions do not follow (III:37420–37427).
4. Absolute/pointwise covariance differences must still be transported through all localization, weakening, non-Gaussian RG, and mixed-history sectors.
5. The one-loop \(\beta_l^0\) should not be silently identified with full beta-history or the Eq.(0.29) residual.
6. No mathematical peer review or formal machine check of these pages was performed.

## 4. Independent red-team controls on this crosswalk

- **Potentially false equivalence:** "Two perfectly paired external minimizers" \(\not\Rightarrow\) "two actual arbitrary Wilson RG histories", especially when thresholds, large-field regions or normalization vary.
- **Potentially false proof inheritance:** A theorem with a proof block is not automatically established when its upstream lemmas are conjectural or use Bałaban claims quoted without proof.
- **Potentially false resummation:** Exponential covariance kernels and their differences alone do not yield uniform marked localization/derivative sums without verifying each nonlinear/complex-domain operation.
- **Potentially false marginal equivalence:** One-loop \(\beta_l^0\), full extracted \(\beta_l\), and regular Eq.(0.29) term must remain separately typed.
- **Potentially false gap claim:** The public external manuscript is an existence attempt and an acknowledged work in progress. No proof of a strictly positive Yang–Mills mass gap follows from these passages.

## 5. Decision and work order

**YM-EXT-01 comparison milestone:** CLOSED AS A **DOCUMENTED CROSSWALK ONLY**. The exit criterion was to produce at least one source-cited, hypothesis-by-hypothesis verdict on an R104/R105 gate, positive or negative. This audit has done that. **No mathematical proof gate is closed.**

The highest-yield native next step is to resume **YM-R105**, but now under a sharper candidate interface:

1. Reconstruct the exact two-cutoff \(\mathfrak B,\mathfrak B'\), \(\Omega,\Omega'\) pair from native source definitions and ask whether they satisfy the external paired-variational conditions III:34660–34734. Treat failure to pair as a **refute-first** stopping condition.
2. Independently check the external claimed minimizer stationarity III:35626–35641 against original CMP102b/CMP99b and *actual* gauge constraints, including its dependencies noted in Chapter 13.
3. Check the external kernel-calculus lemma III:36545ff and covariance/root theorem III:36675–36807 on the exact resulting common space. No result is admitted until the hypotheses are instantiated and the normalization accounted for.
4. If a valid finite-step comparison survives, inspect the **unsandwiched** junction gap III:37365–37482 and decide whether its direct lemma or sandwiched-logdet bypass is necessary for our exact marginal extraction.
5. In parallel, verify the exact source-level correspondence between the external one-loop \(\beta_l^0\) and our R75 \`PrimaryOneStepVacuumPolarizationStationarity\`, keeping \`PrimaryEq029PositiveAlphaBound\` separate.
6. Keep the older open inherited-history and large-field gates in view; do not let a positive **local** Gaussian comparison be presented as existence, OS reconstruction, or mass gap.

The [YM-R104 canonical head](../checkpoints/YM_HEAD_R104_20261026.json) is unchanged; **YM-R105 remains unconsumed**. No new numbered Bałaban reference [93] was created; external git blobs are listed in the [source receipt](YM_EXT_01_SOURCE_RECEIPT_20261026.md) rather than being silently folded into the primary bibliography.

**Result summary:** a precise new *candidate comparison route*, explicit acknowledged *blocking dependencies*, and a much narrower native question. No theorem-status promotion.