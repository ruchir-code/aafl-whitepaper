# Changelog

All notable changes to the AAFL whitepaper are documented here. v1.3.1 is the current revision; v1.3 was the first public release and DOI mint; v1.2.1 was the prior peer-review-strengthening revision; v1.2 was the first review-readiness anchor; earlier versions (v1.0, v1.1) preceded the IP-anchoring decision and are recorded for historical completeness only.

## v1.3.1 — 2026-05-21

Repository-cleanup patch. **No content changes.**

- Removed v1.2 build artifacts (`whitepaper/aafl-whitepaper-v1.2.{md,html,docx,pdf}`) that had been carried inside the v1.3 GitHub release and therefore inside the Zenodo deposit. The v1.3 deposit had inadvertently archived two whitepaper versions side-by-side under different licenses (v1.2 was proprietary, v1.3 was CC BY-NC 4.0), creating license-status ambiguity and reader confusion. v1.3.1 deposit contains v1.3-forward artifacts only.
- Removed superseded build scripts (`whitepaper/build.py`, `whitepaper/build-docx.py`) that targeted v1.2.
- Updated CITATION.cff, README, and manuscript suggested citation to v1.3.1 metadata.
- Concept DOI (`10.5281/zenodo.20319475`) unchanged — still resolves to the latest version. v1.3 frozen DOI (`10.5281/zenodo.20319476`) remains permanently citable.

## v1.3 — 2026-05-20

Forensic citation pass, expanded learning-sciences and AIED grounding, broadened critic-camp engagement, and license transition from proprietary to **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**. Same framework substance — architecture, eight HITL gates, PRS, six-dimension eval, governance layer — held constant from v1.2.1.

**License transition.**

- v1.3 and forward are released under CC BY-NC 4.0 to maximize the citability of the Zenodo-deposited artifact. The full legal code is reproduced in `LICENSE`; the deed is at https://creativecommons.org/licenses/by-nc/4.0/.
- v1.2.1 and earlier remain governed by the proprietary "all rights reserved" license under which they were originally released; that prior license text is preserved in this repository's git history.
- Commercial use (paid training programs, paid consulting deliverables, commercial books, vendor marketing, billable client work product, etc.) continues to require written permission from the author. CC BY-NC 4.0 only permits non-commercial reuse.

**Forensic citation corrections.** The v1.2.1 bibliography was audited entry-by-entry against canonical sources via DOI/URL resolution and direct fetch. Five reject-tier errors were corrected:

- **Brynjolfsson, Li, & Raymond (2023)** — the v1.2.1 entry combined a wrong title (Dell'Acqua's "Navigating the Jagged Technological Frontier"), wrong venue (Organization Science), and wrong DOI into a single misattributed citation. Corrected to the actual paper: *Generative AI at Work*, NBER Working Paper 31161, subsequently published in *Quarterly Journal of Economics* 140(2), 889–942 (2025).
- **Davenport & Daugherty (2018)** on *Human + Machine* — replaced with the actual author, **Wilson, H. J., & Daugherty, P. R.** (Davenport is a different prominent AI/work author often confused in citation).
- **Saghafian et al. (2024)** on the HDSR centaur paper — co-authors corrected from the fabricated "Bauer-Wolf & Donohue" to the actual co-author, **Idan, L.**
- **Chai et al. (2025)** — journal corrected from *Performance Improvement Quarterly* to the actual venue, *Human Resource Development Review* (SAGE).
- **Clark (2025)** *Learning Experience Design* — replaced a citation that pointed at a book review with the actual book citation: Kogan Page, 2025.

Plus fourteen major-tier corrections including: McKenney & Reeves (2013) ghost citation added with author-order fix; O'Donnell (2008) ghost citation added; Hardman 2025a/b in-text labels disambiguated and the unauditable "author copy on file" Hardman 2025a entry consolidated into the single citable Hardman (2025) Substack reference; EduPlanner and AUSS placeholder author-team labels replaced with actual lead authors (Zhang, X., et al., 2025; Arya Mary, K. J., et al., 2026); Liu et al. corrected to 2024 (TACL Vol 12); Anthropic Engineering "Demystifying evals" corrected to 2026 publication; Anthropic Research "Building effective AI agents" corrected to 2024 publication.

**Eighteen minor-tier corrections** including: version harmonization across frontmatter and About the Author; Mosher & Gottfredson author-order correction to Gottfredson & Mosher per book cover; Gagné (1985) full title to *The Conditions of Learning and Theory of Instruction*; Rummler & Brache 3rd edition date corrected from 2013 to 2012; Allen (2012) co-author Richard Sites added; NIST AI RMF lead author Tabassi added; Mollick year normalized to 2024; AR-overlay claim further hedged; "we call this" first-person slip corrected.

**Expanded theoretical grounding.** New §9 subsection *Scaffolding as the underlying construct* anchors AAFL's HITL gates in Vygotsky (1978) ZPD and the Wood, Bruner, & Ross (1976) scaffolding tradition that any learning-sciences reviewer will read AAFL against. New §9 paragraph adds VanLehn (2011) as the AIED tradition's most-cited empirical anchor (with Bloom 1984 2-sigma as historical reference). §7 dimension 5 (Learner experience) supplemented with Mayer (2014) *Cambridge Handbook of Multimedia Learning* alongside Sweller.

**Broadened critic-camp engagement.** Existing engagements with Selwyn, Williamson, and Holmes-Bialik-Fadel deepened (Selwyn: political-economy acknowledgment; Williamson: causal-vs-representational distinction; Holmes: self-positioning inside their tripartite taxonomy). Five new engagements added: Bender et al. (2021) "Stochastic Parrots" cited in §7 dim 1; Hicks, Humphries, & Slater (2024) "ChatGPT is bullshit" cited at §4 Gate 4 and §9 (sharpens the framework's "hallucinated authority" vocabulary); Luckin (2018) *Machine Learning and Human Intelligence* cited as the European AIED tradition anchor; Bayne et al. (2020) *The Manifesto for Teaching Online* added to §12 as the non-instrumentalist limitation acknowledgment; Watters (2021) *Teaching Machines* cited as the historical-context anchor for the framework's restraint posture.

**§11 Risks expanded from five to six** with the addition of Risk 6 — *Citation-and-source integrity in the implementation pipeline*. This is a self-reflexive risk: AAFL implementations are exposed to the agent-era citation-fabrication failure mode the framework is designed against. Mitigation language gives the practitioner a Gate 4 responsibility frame for citation verification.

**§12 Limitations expanded** with the non-instrumentalist scope acknowledgment, citing Bayne et al. (2020).

**Appendix B comparison table** gains a new contrast column — *Performance-anchored?* — that reveals AAFL is the only reviewed framework occupying both the workplace-performance-anchored AND agent-era-operating-discipline positions. Author attributions updated to match v1.3 bibliography corrections.

**Appendix A acronym glossary** gains AAFL pronunciation note ("*ay-eff-ell* or *apple* with a soft P"), AUSS expansion corrected to "Agentic Unified Student Support System" per Arya Mary et al. (2026), and EdArXiv glossary entry activated by citation in §12 Future Work.

**Edition fix.** Tag for the second version of the framework's runtime substrate articulation: §2 and §8 now cite *both* Anthropic Engineering 2026 (eval-driven discipline) and Anthropic Research 2024 (orchestrator-workers patterns) where each is load-bearing for a different layer.

**ATD Research (2025) State of the Industry Report** cited in §1 as the empirical anchor for the market-state capability claim ("design-loop AI tooling has moved from optional add-on to default surface"), replacing the previously uncited assertion.

**§1 federal practitioner-observation claim hedged with measurement frame.** The 40–60% first-draft compression range is now presented with an explicit measurement definition (ID-team hours from brief acceptance to first-draft sign-off, relative to comparable pre-2024 baselines on adjacent programs in the same portfolio) and a confidentiality justification for the withheld denominator.

**Bibliography expanded from 47 to 60 entries** (14 added, 1 removed: the unauditable Hardman 2025a "author copy on file" entry).

No architectural changes. Eight gates, four-level PRS, three cross-cutting layers, six-dimension eval framework, and the workplace-performance organizing outcome are unchanged in substance from v1.2.1. The v1.3 revision is a citation-discipline and theoretical-grounding pass, not a framework rewrite.

Full reviewer report, citation forensics ledger, counter-position audit, and change log for v1.3 are filed in `Claude_Code/AAFL_Review/2026-05-20/` (in the author's working repository, not this whitepaper repo). The revised manuscript in `whitepaper/aafl-whitepaper-v1.3.md` is the authoritative output of that review pass.

## v1.2.1 — 2026-05-17

Editorial and peer-review revision. Same v1.2 framework substance — architecture, eight HITL gates, PRS, six-dimension eval, governance layer — with seven targeted strengthenings from an authority-lens peer review:

- **§1 — Working definition of *agent* added.** Spans the single-prompted-model to orchestrated-multi-step range; clarifies which PRS levels assume which end of the range.
- **§4 Gate 2 — Defense of the blocks-Design discipline.** Engages the iterative-design counterargument explicitly; reframes the discipline as *eval-first*, not *eval-frozen*; permits rubric refinement as deliberate amendment to a committed spec.
- **§1 + §4 Gate 8 — While-you-work / AR claim hedged.** Recast from "operationally available at scale" to "beginning to relax the constraint in instrumented domains"; explicit acknowledgment that AR-overlay tooling is uneven across federal/credentialing contexts; Gate 8 reframed to require *some* honest performance-outcome signal, fidelity-calibrated to context.
- **§1.5 Method — Design-based-theorizing label softened.** Recast as "practitioner-researcher synthesis informed by design-based research and theorizing traditions"; deliberately does not claim the full apparatus (multi-cycle intervention testing with refinement traces).
- **§9 — Kirkpatrick L3/L4 critique engaged.** Adds Kraiger/Ford/Salas (1993) and Holton (1996) critique that the four-level model conflates taxonomy with causal theory; AAFL retains L3/L4 vocabulary for field readability while anchoring the actual causal work in transfer-of-training literature.
- **§9 + §14 — Transfer-of-training literature added.** Baldwin & Ford (1988) and Burke & Hutchins (2007) as the deeper causal anchor for Gate 8 while-you-work signal capture; bibliography expanded to 39 entries.
- **§6 — PRS positioned against adjacent autonomy and risk scales.** New subsection "How the PRS relates to adjacent autonomy and risk scales" engaging SAE J3016 (driving automation), NIST AI RMF 1.0 (AI risk governance), and Mollick's centaur/cyborg distinction; clarifies PRS is the ID-specific operating layer that consumes from general-purpose risk governance and instantiates the centaur-cyborg gradient at gate-level granularity.

Bibliography additions: Baldwin & Ford (1988), Burke & Hutchins (2007), Holton (1996), Kraiger/Ford/Salas (1993), Mollick (2024), NIST AI RMF 1.0 (2023), SAE J3016 (2021).

Plus five medium-priority issues from the same peer-review pass:

- **§4 — Defended Gate 5/6 production classification.** Added sub-distinction: production-prep work is sampleable at PRS-3+; the *human criterion* the gate names (accommodation reasonableness at Gate 5; cut-score / construct-validity at Gate 6) stays per-artifact human sign-off at every PRS level.
- **§7 dim 4 — Tightened "agents drift between phases" citation.** Recast as practitioner observation; added Liu et al. (2023) "lost in the middle" as a closer empirical adjacency than the jagged-frontier work, which remains cited.
- **§7 — Eval-dimensions provenance acknowledgment.** Added a single paragraph at the head of the six-dimension block naming the different traditions (HPT/Kirkpatrick, Dick-Carey, Messick, Dane & Schneider / O'Donnell, Sweller, federal compliance). Honors the CLAUDE.md no-Heritage-callouts rule by consolidating into one paragraph rather than per-dimension tags.
- **§9 — Methodological-foundations citation broadened beyond Anthropic.** Eval-driven-development paragraph now names Stanford HELM (Liang et al. 2023) and the EleutherAI lm-evaluation-harness alongside Anthropic Engineering, making the non-vendor lineage visible.
- **§6 — Resolved PRS-4 "forward-looking spec" vs "where appropriate" contradiction.** Added a parenthetical at the head of the "Where PRS-4 is appropriate" list clarifying it is design guidance, not a field-deployment claim.

Additional bibliography: Dane & Schneider (1998), EleutherAI lm-evaluation-harness (2024), Liang et al. (Stanford HELM, 2023), Liu et al. (2023, lost-in-the-middle), Messick (1989), Sweller (2011).

Plus the eight lower-priority issues from the same peer-review pass:

- **§1 — Substitution position engaged properly.** Added a paragraph acknowledging legitimate motives behind substitution (consistency at scale, removal of certain reviewer biases, per-learner unit economics) before naming AAFL's narrow ground: federal/accredited/credentialing/workplace-performance contexts where institutional accountability is non-transferable.
- **§10 — Other accreditation rubrics named.** QM remains the worked example; OLC OSCQR, iNACOL, and ACCJC distance-education standards explicitly noted as equivalent mapping targets; gate structure declared rubric-agnostic by design.
- **§1.5 — Reproducibility paragraph made accurate.** Now names the repository at `github.com/ruchir-code/aafl-whitepaper` and notes the proprietary-license terms under which the materials are made available for reader audit.
- **§11 — Risks vs Limitations distinction framed.** Brief opening sentence at §11 distinguishing operational risks (§11) from epistemic limits (§12); back-to-back placement is deliberate.
- **§13 (formerly FAQ) — Removed from paper.** The FAQ was uncommon for an academic whitepaper. Content preserved as a separate companion artifact at `aafl-faq.md` for the planned instructionalai.org/aafl web companion page. §14 Bibliography renumbered to §13.
- **Hardman citation upgraded.** Two Substack entries reduced to one; the second replaced with Hardman (2025a) *FRAME™: A 5-step method for integrating and scaling AI use in L&D, without losing quality* — the substantive self-published report.
- **Bibliography additions for ID-textbook breadth.** Smith & Ragan (2005) *Instructional Design* and Driscoll (2005) *Psychology of Learning for Instruction* added — canonical ID textbooks expected by an academic audience.
- **Em-dash + AI-tell polish.** Em-dash density reduced from 11.95 per 1000 words to 3.10 per 1000 (199 → 51 dashes). Replacements were case-by-case: commas for parentheticals, colons for definitions, periods for sentence breaks, parentheses for heavier asides. Remaining em-dashes are field-standard typography (gate/PRS/risk header conventions, figure labels, table cells). Other AI-tells swept: "unlocked" → "available"; checked for and confirmed absence of leverage / delve / robust / seamless / underscore / moreover / hollow conjunctives.

Plus a small editorial cleanup: removed the explanatory note about the "§" symbol from the Table of Contents (the symbol is recognizable in cross-references; the explainer read as defensive).

No architectural changes. Bibliography now ~47 entries. Page count and word count modestly increased.

## v1.2 — 2026-05-14

Public citable anchor. First version archived to Zenodo with a DOI.

- Added §1.5 Method and §12 Limitations and Future Work
- Softened the 50%+ first-draft compression claim to a sourced practitioner-observation range
- Replaced unsourced PRS productivity bands with sourced ranges (Brynjolfsson et al. 2023; Dell'Acqua et al. 2023) and explicit limits where data does not exist
- Expanded bibliography from 20 to 35 entries including UDL theory (Meyer/Rose/Gordon), Merrill First Principles, Reigeluth, and critical AI-in-education voices (Selwyn, Williamson, Holmes-Bialik-Fadel)
- Added new Appendix B comparison table substantiating the federal-caps differentiation
- Un-merged eval dimension #5 into separate Learner Experience and Production Integrity dimensions (now six dimensions)
- Redrew the hybrid stack architecture diagram in §2 to track the commissioned Diagram 1 visual brief
- Added §5 phase-grid view sourced from the primer
- Added Appendix A acronym glossary
- Trimmed Foreword to remove v1.0/v1.1 versioning history
- Updated Anthropic disclosure to reflect both *AI Fluency for Educators* and *AI Fluency: Framework & Foundations* courses completed as a learner

Architecture, eight HITL gates, PRS, eval framework (six dimensions), and governance layer unchanged in substance from v1.1.

## v1.1 — 2026-05-06 (internal)

Repositioned the framework's organizing outcome to *workplace performance* (descriptive) and consolidated intellectual lineage into §9. Architecture, eight gates, maturity model, and eval framework unchanged from v1.0.

## v1.0 — 2026-05-04 (internal)

Initial publishing-ready draft.
