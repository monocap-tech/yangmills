# YM-EXT-01 — external YM4 account / O(N) crosswalk source receipt

Date: 2026-10-26. Workstream: **YM-EXT-01**, external comparison only. Native checkpoint: **YM-R104**; native cursor **YM-R105 remains unconsumed**.

## Evidence class and version boundary

**External, predominantly AI-generated, unrefereed manuscript; proof statements are NOT adopted as valid.** The Sussman–Alpöge repository explicitly warns its content is work in progress, inadequately vetted and tentative.

- Repository: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment
- Observed branch head: **af96f9c5ec6d05a5c8f251256d87970d73b7f25a**. The account consists of huge TeX source files \`theorem_0_complete_account_raw_I.tex\`, \`_II.tex\`, \`_III.tex\`, with master input file \`theorem_0_complete_account_raw_master.tex\`. A GitHub file-content request for high lines returned empty, but a GitHub **blob** read returned the actual entire TeX content; line numbers below were established by splitting fetched contents on newlines.
- Part I blob: **31898fb205c2990b59b7574915e82b22e08450b4**, 166,712 split lines; 10,554,715 characters.
- Part II blob: **f1e0aa132d23ed7f6d44f504a78ad57bd4ce38b8**, 145,625 split lines; 9,092,938 characters.
- Part III blob: **6012ff578fb1c67c29651f1f4192ab59a4c862a3**, 111,584 split lines; 6,963,154 characters.
- Only selected, relevant sections of these very long files were **actually reviewed**, not the entire manuscript. Line locations below refer to the **observed blobs**, not necessarily to another release or to page numbers of the abridged manuscript.

**Independent secondary locator, not proof validation:**
- https://github.com/scottnarmstrong/balaban-lean/blob/main/notes/phase1/YMACCOUNT.md
- Observed blob SHA **50f1bc6522679a950a39af7b184cb0b8f856010a**. Written 16 October 2026, based on the external YM4 account at the **older** source commit \`e392ef4\`. Its references of the form I:n/II:n/III:n are locators in that account; read the exact blob above before transferring a locator unchanged.
- Armstrong's work formalizes a related **classical O(N)** RG program, not this repository's 4D quantum Yang–Mills claim. Its labels **ROUTE / SAME GAP / NOTHING** must not be copied into our native theorem-status ledger.

## Exact Part I inspection

- **I:45215–45234:** a lemma asserting cube gauge/background regularity under the renormalization step is followed by the explicit status **“Proof outstanding.”** This is an upstream native-admissibility interface, not a trivial consequence of free-current coordinates.
- **I:45236–45314:** free-current notation, including the source \`J\` and a quadratic form \(\mathsf Q=C_{\flat}^{\top}\Delta^{(k)}C_{\flat}\) on the unit-bond carrier; the construction replaces physical graph current by a free complex variable. This is a *specific analytic design*, **not** a theorem identifying two cutoff-dependent carriers or admitting all complex currents.
- **I:135200–135217:** the threshold agreement in case (4b) explicitly says the marked step \((*)\) **is not proved**; the known condition is only a monotone inequality. The one-point current probe (I:135723–135823) tests inclusion of current-radius domains and exhibits why larger-radius admissibility cannot be silently treated as inclusion into the smaller-radius class.
- **I:61295–61350:** a proposed relative format for labelled inherited/boundary terms asserts an RG preservation implication, but the proposition is marked **“Proof outstanding”** (I:61325). It explicitly depends on unproved persistence of weights across *two runs on one scaffold* and an orbit datum on the stored analytic domain (I:61348–61350). This bears on our **historical relative \(E\)** gate but does not discharge it.
- **I:58187–58217:** “Torus-independence of the localized terms” theorem assumes a long list, including the average-Laplacian walk expansion, one-family operator bounds and large-field representation. Its statement I:58274–58340 gives intrinsic nonwrapping local terms, a limiting \(\Pi_\infty^{(j)}\) tensor, and a *site-free* \(\beta_j\), **conditional on those hypotheses**. This is site/torus independence at a fixed level, **not** automatically cross-cutoff stationarity.
- **I:53428–53548:** a seam-transfer theorem works under listed nesting, grid, thickness, radii-growth and source hypotheses. The prose flags a printed one-step transfer passage of Bałaban as used without proof, while the book gives an internal implication under named assumptions. This is an interface lead rather than a verified global completion.

## Exact Part II inspection

- **II:89911–89973:** definition of partition-lattice and \(W_4\) covariance of individual localized terms, explicitly **“Stated; proof incomplete at the step marked (*)”.**
- **II:89995–90034:** the termwise covariance of \(E^{(j)}(X,\cdot)\), the residual family and frozen sourced family is not established merely from covariance of summed functionals. The claimed comparison of nonwrapping torus terms to infinite-volume terms up to uniformly summable \(O(e^{-c\mathcal{N}/M})\) is **also explicitly not proved**.
- This is directly relevant to the credibility of moving a marginal/one-loop coefficient between settings: “Euclidean invariant sum” and “covariant individual local term” are different claims.

## Exact Part III inspection: the strongest possible native bridge

**Paired variational setup, III:34660–34734**
- Same physical-scale determining data are paired by \(\Omega'_{j+1}=\Omega_j\), \(V'=V\) on \(\Lambda'_{j+1}=\Lambda_j\), with one additional finer lattice \(\eta'=\eta/L\). The data satisfy small curvature \(|(\partial V)(p')-1|<\varepsilon\) and source admissibility of domain sequences. This is a **specific comparison of paired minimizing problems**, not a statement that all actual histories in our YM-R105 construction automatically satisfy the pairing hypotheses.
- The scaled relative norm \(\|A\|_{\theta}\) is defined in III:34698–34710; the geometric floor \(\delta_0 R M_1\ge 16\log L\) in III:34729–34734.

**Theorem “Index stationarity of minimal configurations,” III:35626–35641**
- For those paired inputs, the manuscript **claims and gives a proof** of a gauge transform \(\mathsf u\) for the one-step average \(W=M(U')\) with
  \[
    W^{\mathsf u}=e^{i\eta A}U_{\mathfrak B}(V),\qquad
    \|A\|_{\theta}\le C_A\varepsilon \eta^\theta,
  \]
  and the printed gauge/averaging constraints. This is the first **concrete proposed relative-background transporter** found in the external account. Do not claim independent validation; several underlying minimizer properties and printed Bałaban steps appear as unresolved assumptions elsewhere.

**Theorem “Stationarity of the fluctuation covariance,” III:36675–36807**
- On the entire unit-lattice torus, or sufficiently deep inside the small-field region, the manuscript claims (and writes a proof from upstream source/nested-minimizer/jet hypotheses)
  \[
  \|\delta C^{(k)}\|_\delta,\quad
  \|\delta(C^{(k)})^{1/2}\|_\delta,\quad
  \|\delta\Delta^{(k)}\|_\delta,\quad
  \|\delta\Gamma_k\|_\delta
  \le C_C L^{-\theta k/8}
  \]
  along with analogous estimates for \(V^{(k)}\), \((QG_1Q^*)^{-1}\) and first/second background derivatives.
- III:36766–36782 gives explicit inverse-resolvent and \(T^{-1/2}\) integral formulas for the **sandwiched covariance precision** \(T_k=C(V^{(k)})^*\Delta^{(k)}C(V^{(k)})\), using local kernel calculus. These are a much closer candidate to our open constrained-carrier/root transfer gate than CMP99(3) domain locality.
- The proof uses paired problems, a uniform small-field/complex tube, background stationarity, “one-step data as functionals of jets” (III:36447–36543), and local-kernel calculus (III:36545–36673). The statement **does not by itself certify** that all actual large-field histories, collars, gauge representatives, Gaussian normalizations and moving localization operators satisfy these hypotheses.

**Theorem “Convergence of the one-loop coefficients and offsets,” III:36809–36935**
- Conditional on the covariance stationarity setting, the account claims and argues
  \[
  |\beta^0_{l+1}-\beta^0_l|\le C_D\,L^{-\theta l/8}.
  \]
  Its proof works with \(\Pi_l=\partial^2 \log Z^{(l)}\), including determinant/Jacobian derivatives, and sums the exponentially decaying second-moment difference (III:36831–36910).
- Identification of the limit with \(c_0\) **also assumes** the specific offset difference equation and uniform boundedness of offset differences, III:36818–36827.
- This is a one-loop coefficient \(\beta_l^0\), **not** automatic stationarity of the complete nonlinear beta history or a Bałaban Eq. (0.29) positive-\(\alpha\) residual certificate.

**Proposition “Weak stationarity of the fine-lattice propagators,” III:37365–37482**
- **“Proof outstanding.”** It demands a paired comparison of the *unsandwiched fine-lattice* \(G',G,G_1\) and a slice propagator, with \(Q_1^\dagger\) transport, scale-factor bounds and a rate \(L^{-\theta'\min j}\).
- The manuscript expressly explains why the proved-in-the-account **sandwiched** fluctuation covariance theorem fails to imply the requested fine-propagator junction estimate: the gauge-fixing form is not nested under averaging and the fine random-walk junctions are not derivatives of the minimizer (III:37420–37427).
- Two proposed routes: establish the missing fine-propagator estimate via a scalar covariant-Laplacian chain lift; **or bypass** it by localizing a resolvent of the already sandwiched fluctuation operator and then the log determinant (III:37429–37478). **Neither route was verified as completed in these passages.** A naive fat-cube telescope loses because 4D cube counting is \(n^4\) versus exponential decay only in a linear radius (III:37480–37482).

**Exact paired-shell/analyticity transfer, III:37533–37560, 37611–37633**
- Reading the zeroth-order two-cutoff response on the *exactly paired shells* of the uniqueness theorem is stated to be **not proved**. It requires covariance under re-basing, shrink of analytic radii **once per object**, uniform absorption of constants, and consistent point identification. The alternative supremum estimate is also not proved.
- The manuscript explicitly says that some remaining radius and repetition controls cannot be shown from its existing order-of-choice argument (III:37594–37604).

**Inherited history and large-field dependence, III:32417ff, 34033–34071, 111167–111313**
- Proposition “history-wise modulus majorant” is **Proof outstanding** (III:32417).
- “Geometric forgetting of old regions” is a *conditional theorem*, assuming that majorant among other hypotheses; it gives an age factor \(q^{a+1}\) **only under those assumptions**, not as an unconditional two-history source response.
- Chapter 13 explicitly inventories further unresolved statements: unique/local constrained minimizer (III:111209–111214), a **kernel-difference bound** (111219–111222), weak propagator stationarity (111262–111263), shifted two-cutoff response on new shells (111264–111266), and **differences of two nested Gaussian integrals interrupted by large-field regions** (111269–111275). This is a decisive reason **not** to treat the draft as a complete verified comparison theorem.

## External status — allowed inferences

1. **Identified** a precise claimed *conditional* relative-background and constrained-covariance/root comparison mechanism not previously constructed in the native ledger.
2. **Identified** a claimed conditional one-loop beta stationarity estimate with an explicit rate and derivative/second-moment calculation.
3. **Identified** explicit, author-acknowledged proof holes at exactly the later two-run history/shell/fine-junction/collar transfers where our native project must be rigorous.
4. **Did not verify** all upstream source arguments, the vast TeX account end-to-end, the exact Clay axioms, group generality, the remaining marginal/RG residual bounds, or mathematical correctness of the proposed theorems.
5. **Did not** inspect or reuse any restricted/proprietary OpenAI physics proof materials; the announcement is a separate claim.
6. **Did not transfer** any of the external theorem-status claims into YM-R104 native gate closure.

## Next native comparison question

Can our **actual** YM-R105 pair of ultraviolet cutoffs be represented as the external manuscript's *paired determining-set variational problems* III:34660–34734, including small curvature, nested domains, same data on shared layers, gauge transport, a common complex analytic tube, and identification of all Gaussian/constraint normalizations? A negative answer is an obstruction; a positive answer would allow a **new, independent** verification attempt for the R105 covariance/root response.

Even a positive answer would leave the external account's explicitly open fine-junction, exact-shell, historical Gaussian integration and positive-\(\alpha\) issues.

This receipt is **provenance only**. See the [YM-EXT-01 assessment](YM_EXT_01_EXTERNAL_YM4_NATIVE_CROSSWALK_20261026.md) for gate-by-gate verdicts.