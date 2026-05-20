# AAFL — An Agent-Augmented Framework for Learning

**Whitepaper · v1.3 · 2026-05-20**

*Judgment, Gates, and Workplace Performance in the Agent Era*

**Ruchir Bakshi** · [instructionalai.org](https://instructionalai.org)

[![DOI](https://zenodo.org/badge/DOI/PENDING.svg)](https://doi.org/PENDING)

---

## What this is

AAFL (Agent-Augmented Framework for Learning) is an instructional systems design framework for the agent era — where AI agents author first drafts and humans serve as Human-in-the-Loop (HITL) judgment-holders, anchored in workplace performance as the organizing outcome.

The framework keeps ADDIE's five-phase spine and adds:

- **Eight HITL decision gates** (four pedagogical, four production) where human judgment is irreducible
- **Three cross-cutting layers** — Governance, Evaluation-as-Spec, Orchestration
- **The Translator's Loop** — Draft → Discern → Validate → Release, run per artifact
- **Proportional Restraint Scale (PRS-1 → PRS-4)** — a maturity model with classification-aware caps
- **Six-dimension eval framework** — eval-as-spec discipline at every gate

## Read it

- **PDF (canonical):** [`whitepaper/aafl-whitepaper-v1.3.pdf`](whitepaper/aafl-whitepaper-v1.3.pdf) — A4, print-clean
- **HTML:** [`whitepaper/aafl-whitepaper-v1.3.html`](whitepaper/aafl-whitepaper-v1.3.html) — kami-styled web view
- **DOCX:** [`whitepaper/aafl-whitepaper-v1.3.docx`](whitepaper/aafl-whitepaper-v1.3.docx) — Word format for tracked-changes review
- **Source:** [`whitepaper/aafl-whitepaper-v1.3.md`](whitepaper/aafl-whitepaper-v1.3.md) — Markdown source of truth

Prior versions (v1.2, v1.2.1) remain in the `whitepaper/` folder for traceability.

## Cite it

> Bakshi, R. (2026). *AAFL: An Agent-Augmented Framework for Learning* (v1.3). instructionalai.org. https://doi.org/PENDING

Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff). Once the Zenodo DOI is minted, both this README and the CITATION.cff will be updated with the concept DOI (always-latest) and the v1.3 version DOI.

## Build

The HTML + PDF are rebuilt from the Markdown source via a pandoc → custom kami template → WeasyPrint pipeline.

```bash
cd whitepaper
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build-v1.3.py
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build-docx-v1.3.py
```

Dependencies: pandoc, WeasyPrint, cairosvg, pango/cairo via Homebrew (`brew install pango cairo`).

## Versioning

See [`CHANGELOG.md`](CHANGELOG.md). v1.3 is the current revision (forensic citation pass + license transition to CC BY-NC 4.0); v1.2.1 was the prior peer-review-strengthening revision; v1.2 was the first public citable anchor; earlier internal versions (v1.0, v1.1) preceded the IP-anchoring decision and are not part of the published lineage.

## License

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).** Copyright © 2026 Ruchir Bakshi. See [`LICENSE`](LICENSE) for the full legal code, or the [CC license deed](https://creativecommons.org/licenses/by-nc/4.0/) for the human-readable summary.

**Permitted under CC BY-NC 4.0:**

- Sharing — copying and redistributing the material in any medium or format
- Adapting — remixing, transforming, and building upon the material

…provided that you give appropriate **attribution** to the author (see CITATION.cff), provide a link to the license, indicate if changes were made, and do not use the material for **commercial purposes**.

**Commercial use** — incorporation into paid training programs, paid courses, paid consulting deliverables, commercial books, vendor marketing materials, billable client work product, or any use that is part of revenue-generating activity by a party other than the author — requires prior written permission from the author.

For commercial-licensing or special-use requests: **hello@rbakshi.com**.

*(v1.2.1 and earlier were released under a proprietary license; v1.3 transitions to CC BY-NC 4.0 to maximize the citability of the Zenodo deposit. The license change applies to v1.3 forward. Earlier versions remain governed by the proprietary license under which they were originally released.)*

## Related

- **Site (in progress):** `aafl.instructionalai.org` — the framework's home in the instructionalai.org family of sites
- **Author:** [rbakshi.com](https://rbakshi.com)
