# External research interfaces — comparison plan, not proof adoption

**Prepared:** 2026-10-26. **Status:** Proposed workstream **YM-EXT-01**; no native theorem gate is closed by this document. The independent native cursor remains **YM-R104**, following the [YM-R103 checkpoint](ym/checkpoints/YM_HEAD_R103_20261014.json).

This page identifies external materials worth checking against our [research-status ledger](RESEARCH_STATUS.md) and [target-scope hold](TARGET_SCOPE.md). An analogous technique, press release, manuscript, or Lean development does **not** establish that the exact theorem needed in this repository holds.

## Public leads

| Lead | What is publicly available / claimed | What must not be inferred |
| --- | --- | --- |
| [OpenAI, 26 October 2026](https://openai.com/index/building-scientific-understanding-with-academic-communities/) | OpenAI **announced** AI-generated constructive existence results for four-dimensional pure Yang–Mills and QCD, building on Bałaban, and reported completion of Yang–Mills Lean formalization on 16 October. It says the physics collaboration will prepare its own account and has deferred release of AI-generated physics artifacts. | The underlying physics proof is not publicly auditable from the announcement. It neither certifies our R103 gates nor announces a **positive mass-gap** proof. |
| [Sussman–Alpöge, Yang--Mills-LLM-experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) | Public draft and raw YM4 account, plus QED3/YM3 material and a reflection-positivity/rotation-invariance argument. The authors explicitly characterize the research as tentative and insufficiently vetted, including an extremely long, hard-to-understand apparent YM4 construction. | Raw proof output is not an independently verified theorem. QED3, YM3, and YM4 arguments have distinct assumptions and UV behavior. |
| [Armstrong, balaban-lean](https://github.com/scottnarmstrong/balaban-lean) | Extensive, unfinished Lean formalization of Bałaban's **classical O(N) spin-model** renormalization group; its [YMACCOUNT analysis](https://github.com/scottnarmstrong/balaban-lean/blob/main/notes/phase1/YMACCOUNT.md) compares some of that project's blockers against the Sussman–Alpöge YM account and explicitly marks proposed routes and same gaps. | This is not a Lean formalization of our four-dimensional pure Yang–Mills theorem. Its comparison notes are leads, not automatically transferable gauge-theory estimates. |

There is no established collaboration or shared proof chain between this repository and any group listed here. We have not claimed independent verification of their proposed constructions.

## Public-repository reference snapshots

For a reproducible *entry point* into moving external repositories, the heads observed on 2026-10-26 were: Sussman–Alpöge at [af96f9c](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/commit/af96f9c5ec6d05a5c8f251256d87970d73b7f25a) and Armstrong at [493e9eb](https://github.com/scottnarmstrong/balaban-lean/commit/493e9eb97292ebf6070c1c217a09bcf1adc23857). These are snapshots **for later comparison**, not a claim that all cited manuscripts were read at those commits or that any theorem is validated. Each future lemma must be pinned to the *particular content version actually checked*.

## Comparison questions (ordered by direct relevance to YM-R103)

1. **Cutoff and source carriers.** Does an external construction compare actual cutoff histories on explicit common gauge/constraint/Gaussian/source carriers? Locate the definition and transport theorem, not merely an informal identification.
2. **Background-field variation.** Is there a two-background estimate at fixed domains, in the correct weighted complex chart, with constants uniform in the RG step? Or does the argument avoid the comparison?
3. **Marked constrained covariance.** Does a spatial domain-difference mark survive the construction of the relevant constrained covariance (and any root or square-root), and does the argument distinguish it from history-age decay?
4. **Nonlinear maps and localization.** Are CMP116-type minimizers, weakened propagators, weakening derivatives, and connected sums stable under moving the input apparatus with a common contraction margin?
5. **Marginal/residual split.** Are the polarization coefficient and the Eq. (0.29) complement treated at the needed physical scale and with sufficient positive UV exponent? What are the exact source identities?
6. **Beyond small fields.** Which theorem covers large-field sectors, thermodynamic/continuum limits, nontrivial observables, and Osterwalder–Schrader reconstruction?
7. **Mass gap.** Is a strictly positive spectral gap actually deduced from reconstructed physical correlations? **Existence alone is insufficient.**

For each candidate external lemma, record the exact statement, section/page/commit, hypotheses, required model, source provenance, and a verdict: **DISCHARGES**, **WEAKENS**, **BYPASSES**, **INAPPLICABLE**, or **UNKNOWN**. Mark a result **DISCHARGES** only after verifying the mapping of every hypothesis to the native gate; otherwise retain a conditional or unknown status. A positive comparison must subsequently be audited in a *new* native pass before updating the canonical checkpoint.

## First comparison target

Armstrong's [YMACCOUNT](https://github.com/scottnarmstrong/balaban-lean/blob/main/notes/phase1/YMACCOUNT.md) cites a Sussman–Alpöge YM4 account and classifies several potential arguments as **ROUTE**, **SAME GAP**, or **NOTHING** for O(N) formalization blockers. It is useful as a *locator* for:

- handling inherited boundary terms and retained holes;
- the large-field gas and polymer core incidence;
- last-scale and torus-independence interfaces;
- fixed or moving backgrounds.

**Do not assume** that its O(N) blockers coincide with our native history-response obstruction. A useful first deliverable is a narrow theorem-level crosswalk, especially for two-cutoff backgrounds and carrier movement, with negative findings recorded as carefully as positive ones.

## Source and communication protocol

- Prefer dated, versioned manuscripts, commit links, exact theorem statements, and original source pages over secondary paraphrase.
- Keep third-party OCR, manuscript claims, machine-checked formalization, and independently reconstructed proofs in distinct evidence classes.
- Do not import external claims into the native pass lineage merely because they are associated with Bałaban's program.
- Do not copy entire external manuscripts into the repository; link to their licensed sources and quote sparingly with attribution.
- Preserve the existing history: YM-R104 is the *native* next cursor; YM-EXT-01 is a separate, proposed comparison workstream.
- Public outreach should identify the repository's limitations and specific source-audit contributions, without implying priority, affiliation, discovery of existence, or a solved Millennium problem.

OpenAI's 26 October announcement requests physics-collaboration correspondence via **YANGMILLS4D@gmail.com**. No contact has been sent from this documentation update; preparing a technically navigable public record precedes outreach.

## Exit criteria for YM-EXT-01

The initial *survey milestone* ends when it has produced at least one **source-cited, hypothesis-by-hypothesis** finding about a named R103/R104 gate, whether positive or negative. A broad survey without this precise interface does not count as gate progress. Publish the verdict and its unresolved assumptions in a dated note, leaving the canonical status unchanged until native audit. A documentation milestone or external survey is **not** proof completion.
