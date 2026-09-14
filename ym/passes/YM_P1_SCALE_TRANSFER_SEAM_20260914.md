# YM-P1 — continuum mass-gap custody is a scale-transfer problem

Date: 2026-09-14
Status: OPEN / UNPROVED RESEARCH PROGRAM
Predecessor state: conversational opening only; no prior durable Yang–Mills checkpoint was found before initialization of this repository.

## 1. Target

Determine whether the opening Yang–Mills investigation should be typed as

`prove a lattice mass gap -> remove the lattice -> obtain a continuum mass gap`

or whether the continuum limit forces a different carrier and a different proof architecture.

## 2. Source-attested facts from the opening literature pass

The following facts were source-checked in the originating conversation; exact theorem numbers, hypotheses, and bibliographic metadata must be rechecked against primary sources before proof-level use.

### LITERATURE FACT L1 — official target remains open

The Clay Yang–Mills problem requires a nontrivial four-dimensional quantum Yang–Mills theory together with a positive mass gap. The problem remains unsolved.

### LITERATURE FACT L2 — rigorous lattice gaps exist in restricted strong-coupling jurisdictions

Recent strong-coupling lattice Yang–Mills work of Shen–Zhu–Zhu proves, under explicit small-coupling-parameter / strong-coupling hypotheses, infinite-volume functional inequalities and exponential decay of correlations, giving a lattice mass-gap statement in that jurisdiction.

### LITERATURE FACT L3 — continuum-construction machinery exists in lower-dimensional / related gauge settings

Modern stochastic-quantization work by Chandra–Chevyrev–Hairer–Shen and Chevyrev–Shen constructs or controls gauge-covariant renormalized dynamics/state spaces in lower-dimensional Yang–Mills(-Higgs) settings. These results are not a construction of four-dimensional pure Yang–Mills.

### LITERATURE FACT L4 — a non-Abelian lattice-to-continuum scaling limit can be rigorous when the model is altered

Chatterjee has obtained a rigorous scaling limit for a special `SU(2)` lattice Yang–Mills–Higgs regime yielding a massive Gaussian field. This does not supply the desired non-Gaussian four-dimensional pure Yang–Mills continuum theory.

### LITERATURE FACT L5 — Balaban's program attacks the multiscale UV side

Balaban's lattice gauge renormalization-group program develops multiscale control, background-field/propagator machinery, and renormalization transformations relevant to the ultraviolet continuum-limit problem. It is not by itself a completed proof of the Clay statement.

## 3. DERIVATION P1-D1 — a uniform positive lower bound on dimensionless lattice mass is not the desired continuum behavior

Let `a` be lattice spacing and let `m_lat(a)` denote a dimensionless lattice mass scale. A physical mass extracted from the lattice has the form

`m_phys(a) = m_lat(a) / a`.

Along a continuum-producing critical trajectory, the correlation length in lattice units must diverge. Equivalently, the dimensionless lattice mass must tend to zero:

`m_lat(a) -> 0`.

A nonzero continuum physical mass is compatible with this if

`m_lat(a) ~ a * Delta`

for a finite `Delta > 0`.

Therefore a theorem of the schematic form

`m_lat >= c > 0 uniformly as a -> 0`

would not be the continuum scaling law required for a finite nonzero physical mass. It would correspond to a physical mass that grows like `1/a` rather than a finite mass gap.

## 4. NEGATIVE RESULT P1-N1 — reject the naive lattice-gap handoff

The opening decomposition

`strong-coupling lattice gap -> continuum limit -> Clay mass gap`

is too coarse and, as stated, incorrectly typed.

Strong-coupling exponential clustering and a continuum physical mass gap occupy different scaling jurisdictions. A successful proof must transport a scale-sensitive quantity through an asymptotically free / critical continuum trajectory.

## 5. WORKING RECONSTRUCTION P1-W1 — the missing corridor

The current structural synthesis is

`UV asymptotic freedom`
`-> controlled RG trajectory`
`-> dynamically generated dimensional scale`
`-> IR exponential clustering in physical units`
`-> OS/Wightman reconstruction and spectral gap`.

This is a research reconstruction, not a theorem asserting that existing programs jointly establish every arrow.

The observed literature jurisdictions currently look roughly like:

- Balaban-type multiscale RG: attacks the UV / RG end;
- strong-coupling functional inequalities: establish restricted IR clustering/gap information;
- stochastic quantization: clarifies continuum construction, renormalization, and gauge-covariant state-space issues in related/lower-dimensional regimes;
- OS/Wightman reconstruction: supplies the framework in which Euclidean correlation control must become a spectral statement.

The important unresolved question is whether these jurisdictions possess a common quantitative carrier.

## 6. Candidate carriers

The next audit should compare at least:

1. `a^{-1} m_lat(a)`;
2. `(a * xi_lat(a))^{-1}` where `xi_lat` is the lattice correlation length;
3. physical-unit exponential-clustering rates;
4. transfer-Hamiltonian spectral data;
5. an RG-invariant dimensional scale analogous to `Lambda_YM`.

A candidate is useful only if it can be defined and controlled on enough of the continuum-producing trajectory to connect ultraviolet construction to infrared spectral information.

## 7. Limitations

This pass does not establish:

- existence of a four-dimensional continuum measure;
- non-Gaussianity/nontriviality of the limiting theory;
- gauge-covariant convergence of all required observables;
- a uniform RG transport inequality for any listed candidate carrier;
- exponential clustering in physical units along the full weak-coupling continuum trajectory;
- OS positivity/reconstruction hypotheses at the needed level;
- equality or even rigorous comparability of a generated RG scale with the spectral mass gap.

## 8. Bounded determination

The first opening seam is now typed as follows:

> The Yang–Mills mass-gap problem cannot be reduced to proving a dimensionless lattice gap and then taking `a -> 0`. The missing obligation is custody of a dynamically generated physical scale through the continuum-producing RG trajectory, with enough control to survive as exponential clustering and then as a spectral gap.

This is stronger than the generic statement that “the continuum limit is hard” because it identifies the quantity that must change units while preserving nonzero physical content.

## 9. Next frontier — YM-NF2

Audit the **RG transport of physical clustering scale**.

Target question:

> What quantitative object can be propagated through renormalization so that its dimensionless lattice representative vanishes while its physical value remains bounded away from zero?

Tasks:

1. type the continuum-limit scaling law for each candidate carrier;
2. determine what strong-coupling functional-inequality results actually control;
3. determine what Balaban-style RG estimates transport between scales;
4. determine the exact Euclidean-to-spectral hypotheses needed for OS reconstruction;
5. mark every interface as proved, conditional, jurisdiction-restricted, or missing;
6. do not identify `Lambda_YM`, a clustering exponent, and the Hamiltonian spectral gap without an explicit theorem linking them.

Live successor cursor: `YM-NF2`.