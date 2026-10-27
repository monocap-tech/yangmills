# YM-R124 original-image source receipt — H_k fluctuation chart and winding Wilson custody

**Date:** 2026-10-27. [Pass](../passes/YM_R124_FLUCTUATION_CURVATURE_CHART_AND_GLOBAL_HOLONOMY_PASSPORT_20261027.md). Evidence hierarchy: original published CMP109 printed pages rechecked using actual PDF image screenshots; exact elementary SU2 algebra derived; CMP102 missing quantitative H_k norm remains OPEN.

## Primary source inspected

T. Bałaban, *Renormalization Group Approach to Lattice Gauge Field Theories I*, CMP **109** (1987), 249–301, DOI https://doi.org/10.1007/BF01215223, [54-page original published printed scan hosted by SciSpace](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf).

- PDF index **2** / printed p.251: torus construction and half-shifted periodic fine and coarse lattice, (0.1).
- PDF indexes **3–4** / printed pp.252–253: original (0.3) centered L-block and the ACTUAL nonlinear full source M(U) (0.4), shortest-path relative logarithmic loops.
- PDF index **16** / printed p.265: original (2.1)–(2.3), regularizing χk and saddle. Later paragraph explicitly says after axial→Landau gauge transformation the fluctuating fine configuration is **exp(iηH_k(B')) U_{k+1}**, with H_k regular **of the same order as B'**, referred to **Sect. G [15]**. The gauge transformation is also analytic in H under its own smallness condition. This wording does NOT give a numeric sup norm on all links or the source halo.
- PDF index **17** / printed p.266: (2.4)–(2.9) independent B' variables and χk cutoff omitting b0(c); optional source gk ε1/γk threshold.
- PDF index **18** / printed p.267: source b0 O(ε1) and the analytically constrained nonlinear change \(\widetilde D(B)\), source h with LQh=I; later (2.11) covariance precision points to CMP99 (3.156).
- PDF index **50** / printed p.299: reference [15] is Bałaban *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP **102**, 277–309 (1985), DOI https://doi.org/10.1007/BF01229381. This article is the exact prequel source for quantitative H_k properties, not an assumed theorem inferred from "same order". Search found a University of Michigan archive link via a third-party seminar bibliography, but the PDF was not accessible as a readable original-page artifact this pass. No Prop. 9/(190) from CMP102 was inspected directly.

Related exact repository custody: [R106](../passes/YM_R106_FINITE_WILSON_OBSERVABLE_COSPAN_COUPLING_CUTSET_20261026.md) explicitly restricts its Wilson cospan to local physical squares and ignores winding geometry; [R122](../passes/YM_R122_NONLINEAR_COARSE_LINK_CURVATURE_AND_TWO_STAGE_GATE_20261027.md) provides local source M relative fine path bound under complete contractible plaquette ribbon; [R123](../passes/YM_R123_SOURCE_REGULARITY_TO_NONLINEAR_M_ENTRY_AND_FLUCTUATION_SEAM_20261027.md) source-certifies background curvature but not B'→original field.

## Independent exact deductions

1. **Curvature transfer without intermediate gauge norms**: local plaquette norms are conjugation-invariant. If in the Landau representative \(U_{\rm fl}=e^{i\eta H_k(B')}U_{\rm bg}\) with \(\|H_k\|_\infty\le C_H\theta_k\), then \(\eta_{\rm phys}\le\eta_{\rm bg}+4\eta C_H\theta_k\). **C_H, source units, regional bond halo and special b0 remain UNVERIFIED**, so the R122 chart \(666(\eta_{\rm bg}+4\eta C_H\theta_k)<1\) is a conditional gate.
2. **Flat torus family**: one constant Cartan SU2 element \(D(\theta/N)\) on every positive e1 link and identity elsewhere has trivial plaquettes and winding Wilson trace cos θ; for θ=π/3 trace 1/2, not equal to trivial 1. Different flat Wilson classes need not be disconnected sectors.
3. **Actual nonlinear flat M retention**: if source relative loops are plaquette-contractible on an eligible periodic graph, they are I on flat U, so M(U,c)=straight U(c). On aligned winding cycle and L|N, \(W_\gamma(M(U))=W_{\gamma_{\rm fine}}(U)\). **Full V does not discard flat holonomy**, even though curvature-only summary does.
4. **Near-flat winding fidelity**: per coarse link R122 bound \(\delta=C\eta/(1-666\eta)\) on all winding halos gives \(\|W_\gamma(M(U))-W_{\gamma_{\rm fine}}(U)\|\le\min(2,n\delta)\), and same normalized trace bound. With physical period ell fixed, fine spacing h and \(\eta\le\varepsilon_0h^2\), n=ell/(Lh) gives \(O(h)\) one-step bound CONDITIONAL on actual source h/regularity match and complete global halo. This is NOT a coupling or probability-law convergence.
5. **Harmonic residue**: periodic curl-free 1-forms need not be periodic gradients; fixed V may remove these directions on the source constrained carrier. Actual CMP99 precision and harmonic kernel criterion not checked.

[Reproducible finite SU2 numerical witness](../computations/YM_R124_FLAT_WINDING_AND_CURVATURE_TRANSFER_20261027.py) tests N=13³, theta=π/3 and winding retention at L13 plus the product telescoping inequality. Floating numerical tolerance is explicitly distinguished from the EXACT analytic proof. No source-matched χk sample or physical mass gap inferred.

**Open source passports:** CMP102 Sect G actual H_k bound on all original bonds and Dirichlet/collar, CMP109 special b0 chart+gauges and source field units, CMP99 late precision (3.157)–(3.158), matched Ω/V across independent UV histories, normalized conditional laws and global winding observable distributions, OS mass gap. Historical bibliography highest [92] unchanged.
