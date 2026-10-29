# YM-R150 — source-image gate PASS, native-operator gate OPEN (2026-10-29)

**Predecessor:** merged AUX-05 main `de5c7c933b320e723383b196d4a094794693d6c9`. **Canonical numbered machine state remains YM-R149 completed, YM-R150 UNCONSUMED.** **Claim status:** UNPROVED_RESEARCH_PROGRAM.

## New verified custody artifacts

- [Original 46-page CMP99 direct mathematical-image receipt](../source_receipts/YM_R150_CMP99_ORIGINAL_IMAGE_VERIFIED_20261029.md)
- [Append-only source-projection correction to AUX-05](../passes/YM_R150_ORIGINAL_IMAGE_PROJECTOR_CORRECTION_20261029.md)
- [Exact correction reproducer](../computations/YM_R150_AUX05_PROJECTION_COUNTERCHECK_20261029.py)
- [Local run record](../computations/YM_R150_PROJECTOR_COUNTERCHECK_RUN_LOG_20261029.txt)

## Exact gate dispositions

| Gate | Status |
|---|---|
| Original CMP99 printed pp.393–395,427–432 images | **PASS 2026-10-29**: user-supplied 46-page scan visually inspected, file SHA256 recorded |
| Historical Δ_k quadratic form (3.155)–(3.156) | **SOURCE RECOVERED** |
| Independent special-bond C and reduced precision (3.157)–(3.158) | **SOURCE RECOVERED** |
| Historical source positivity γ₀ of C*Δ_k C | **SOURCE ASSERTION VERIFIED** under stated regularity/smallness, numerical value not given |
| Projection R (3.21) and historical projected Landau | **SOURCE CORRECTED**: ran R=Δ_U ker Q', not ker Q' |
| Historical hard→exponential gauge representation (3.159)–(3.186) | **SOURCE IMAGES RECOVERED**, original formal transformation identified |
| Actual CMP109 exp-gauge C* A^(k) C = historical positive reduced operator | **NOT PROVED; non-transfer remains** |
| Eligible L13 Ω/Λ, full native C and actual matrix K, α | **OPEN**, no synthetic matrix |
| Two R149 native directional inverse solves, FP/weight/partition | **OPEN** |
| Independently normalized two-UV law, OS continuum and 4D mass gap | **OPEN / UNPROVED** |

**Important correction:** AUX-05's field is a valid exact rational negative control for the declared *wrong* projector onto ker Q'. But the original CMP99 projector has range Δ_U ker Q'. Explicit ψ test gives `<D*a,Δψ>=−1/169`, so the AUX-05 example is **not** in native projected Landau. Do not treat the earlier auxiliary example as source gauge evidence.

**Native next:** after image recovery, type CMP99 gauge and C against CMP109's exponential A^(k) using original CMP109 p266–268 and the full original CMP99 pp427–432 operator, then construct a legal finite ambient K and run the two source inverse actions. **Do not consume YM-R150 without K/region certification.** This is bounded image/source-correction custody, not theorem closure. Original publisher PDF is not uploaded/reproduced in repo; only checksum and equation-number ledger retained.
