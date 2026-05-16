# AAFL — An Agent-Augmented Framework for Learning

**Whitepaper · v1.2 · 2026-05-14**

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

- **PDF (canonical):** [`whitepaper/aafl-whitepaper-v1.2.pdf`](whitepaper/aafl-whitepaper-v1.2.pdf) — 47 pages, A4, print-clean
- **HTML:** [`whitepaper/aafl-whitepaper-v1.2.html`](whitepaper/aafl-whitepaper-v1.2.html) — kami-styled web view
- **Source:** [`whitepaper/aafl-whitepaper-v1.2.md`](whitepaper/aafl-whitepaper-v1.2.md) — Markdown source of truth

## Cite it

> Bakshi, R. (2026). *AAFL: An Agent-Augmented Framework for Learning* (v1.2). instructionalai.org. https://doi.org/PENDING

Machine-readable citation metadata is in [`CITATION.cff`](CITATION.cff). Once the Zenodo DOI is minted, both this README and the CITATION.cff will be updated with the concept DOI (always-latest) and the v1.2 version DOI.

## Build

The HTML + PDF are rebuilt from the Markdown source via a pandoc → custom kami template → WeasyPrint pipeline.

```bash
cd whitepaper
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 build.py
```

Dependencies: pandoc, WeasyPrint, pango/cairo via Homebrew (`brew install pango cairo`).

## Versioning

See [`CHANGELOG.md`](CHANGELOG.md). v1.2 is the public/citable anchor; earlier internal versions (v1.0, v1.1) preceded the IP-anchoring decision and are not part of the published lineage.

## License

Copyright © 2026 Ruchir Bakshi. All rights reserved. See [`LICENSE`](LICENSE).

For attribution-with-reuse questions (citation in academic work, classroom use, etc.), contact the author. Standard academic citation under fair use is welcomed without prior permission.

## Related

- **Site (in progress):** `aafl.instructionalai.org` — the framework's home in the instructionalai.org family of sites
- **Author:** [rbakshi.com](https://rbakshi.com)
