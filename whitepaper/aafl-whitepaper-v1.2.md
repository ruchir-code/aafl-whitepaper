---
title: "AAFL — An Agent-Augmented Framework for Learning"
subtitle: "Judgment, Gates, and Workplace Performance in the Agent Era"
author: Ruchir Bakshi
version: v1.2
date: 2026-05-14
status: Foundation document — source of truth for derivative artifacts
audience: Instructional design practitioners, federal L&D leaders, learning-science researchers, AI-in-education program leads
length_target: 30–40 pages typeset
typesetting: kami-compatible markdown
ip_status: Independent IP, © Ruchir Bakshi 2026, all rights reserved
suggested_citation: "Bakshi, R. (2026). AAFL: An Agent-Augmented Framework for Learning (v1.2). instructionalai.org."
---

# AAFL — An Agent-Augmented Framework for Learning

*Judgment, Gates, and Workplace Performance in the Agent Era*

**Ruchir Bakshi** · v1.2 · 2026-05-14

---

## Foreword: status and provenance

AAFL is an independent framework. It is offered to the field as a working artifact — opinionated, citable, and revisable. The framework's intellectual debts are deep and broad; they are named in §9 as a substantive lineage rather than as plank-by-plank derivations, because AAFL is intended to read as a single synthesis, not a composite of borrowed parts. Critique should engage the framework on its own terms.

This is v1.2 (2026-05-14).

---

## Executive Summary

Instructional design has spent fifty years answering the question *"how do we build courses that learners pass?"* The performance-oriented corners of the field have spent decades quietly reframing the question to *"how do we accelerate workplace performance?"* — under the broader tradition of Human Performance Technology and through specific operational articulations like Action Mapping, 5 Moments of Need, and the Success Case Method.

The agent era forces a third reframing. As AI agents become competent first-draft authors — capable of producing learner personas, learning objectives, storyboards, item banks, and accessibility-checked content at the level of a mid-career instructional designer — the human ID practitioner's center of gravity shifts from *production* to *judgment*. The skill that compounds is no longer *generating instructional artifacts*; it is *deciding which of three agent-generated drafts is pedagogically defensible, why, and what the agent missed about the learner.*

**This whitepaper introduces AAFL — the Agent-Augmented Framework for Learning** — a framework for the era of agent-authored first drafts and human-held accountability. AAFL preserves ADDIE's five-phase spine (because federal contracting officers, ACE evaluators, and Quality Matters reviewers still read in that vocabulary), adds three cross-cutting layers (orchestration, evaluation-as-spec, governance) that did not exist in classic ADDIE, introduces an inner *Translator's Loop* every artifact runs through, and is anchored in **workplace performance** — not course completion or learning attainment — as the organizing outcome.

AAFL formalizes five intellectual positions that no published competitor currently integrates:

1. **An HITL decision-gate taxonomy** — eight named gates with explicit pedagogical-vs-production classification
2. **A pedagogical vs production task taxonomy** — agents do what is bounded and reviewable; humans hold what is value-loaded and trust-bearing
3. **The Proportional Restraint Scale (PRS)** — a four-level scale (PRS-1 Sandbox · PRS-2 Co-designer · PRS-3 Production Partner · PRS-4 Performance System) with prescribed ceilings for each consequence space; most federal and accredited programs sit at PRS-2 or PRS-3 (see §6)
4. **A performance-anchored eval framework** — six dimensions with workplace performance attainment as the primary spine; eval rubric authored at the Performance Outcome Gate before any agent runs
5. **A governance/escalation layer** — the institutional infrastructure (audit trail, classification handling, accreditation alignment, escalation paths) that operationalizes the PRS ceilings; the federal-applicability claim no civilian framework currently makes

The framework is opinionated about its own limits. It publishes what it *won't* do — concrete caps on agent autonomy tied to data classification, training-program type, and decision class — before publishing what it does. That posture is the source of its credibility, not its limitation.

This whitepaper is structured to be read in two ways. **As a sequential argument**, it moves from the conceptual realignment (§1), through the architecture (§2–§3), the gate taxonomy (§4), the agent-task split (§5), the Proportional Restraint Scale (§6), the eval framework (§7), the cross-cutting layers (§8), engagement with prior frameworks (§9), federal applicability (§10), and risks (§11). **As a reference manual**, each section is self-contained — practitioners can use the gate taxonomy or the eval framework à la carte without adopting the whole framework.

---

## Table of Contents

*Throughout this paper, the symbol "§" (the section sign, also called the silcrow) is used as a shorthand for "section." A reference to "§4" means "see Section 4." This is the standard convention in legal and scholarly writing for cross-referencing numbered sections within a document.*

- **§1.**  The Conceptual Shift
  - **§1.5**  Method — How This Framework Was Developed
- **§2.**  Architecture — The Hybrid Stack
- **§3.**  The Translator's Loop
- **§4.**  The HITL Decision-Gate Taxonomy
- **§5.**  The Agent-Task Taxonomy
- **§6.**  The Proportional Restraint Scale (PRS)
- **§7.**  The Eval Framework
- **§8.**  The Three Cross-Cutting Layers
- **§9.**  Engagement With Prior Frameworks and Intellectual Lineage
- **§10.**  Federal Applicability
- **§11.**  Risks and Pitfalls
- **§12.**  Limitations and Future Work
- **§13.**  Frequently Asked Questions
- **§14.**  Bibliography

Appendices: A. Acronym Glossary · B. Comparison of Published AI-Era ID Frameworks

---

## §1. The Conceptual Shift

Florida State University's 1975 *Interservice Procedures for Instructional Systems Development* — the genealogy of what became ADDIE — assumed a clear sequence of human authorship. The instructional designer analyzed learner needs, designed learning objectives, developed content, implemented delivery, and evaluated results. Each phase had a human author. Tools were accelerants — they did not change the locus of authorship.

The agent era reverses who writes the first draft without reversing who is accountable for it. Agents now produce drafts that human practitioners used to author by hand; institutional, legal, and pedagogical accountability for the work still rests with the practitioner. We call this *authorship inversion without accountability inversion* — the *who-writes* role flips; the *who-owns-it* role does not.

A competent AI agent, given clear instructions, well-formed inputs, and access to source material, can now produce:

- A learner persona drafted from interview transcripts in minutes
- A set of objectives at multiple cognitive levels
- A backward-mapped task list grounded in workplace performance metrics
- A storyboard with branching scenarios
- An item bank with distractors and rubrics
- Accessibility-checked content meeting WCAG 2.1 AA
- A facilitator guide and instructor enablement package
- Learning analytics dashboards with hypothesized causes for learner outcomes

This is not aspirational; it is operational. Across commercial authoring platforms in 2024–2026, design-loop AI tooling has moved from optional add-on to default surface — course-outline generation, narrated-video production at scale, animated scenario-based training, and accessibility-checked content drafting are now common features of mainstream instructional design platforms. On the federal side, in the author's federal ID practice, AI-Enhanced ADDIE workflows applied across ACE-accredited graduate certificate and post-baccalaureate programs have produced first-draft cycle reductions in the 40–60% range. These are practitioner-level observations across multiple production deliveries, not controlled-study results; see §12 (Limitations and Future Work). The capability claim is not in dispute.

What *is* in dispute — and what AAFL claims to resolve — is the question of where the human stays, why, and what authority the human's judgment carries that the agent's output does not. Two positions in the discourse currently dominate:

- **The substitution position.** Agents will replace ID practitioners. Most extreme cases: per-learner curriculum generated end-to-end without human review.
- **The augmentation position.** Agents accelerate ID work without displacing it. Humans review agent output and make the value-laden decisions.

AAFL takes the augmentation position. But "augmentation" is broad — *how* the human relates to the agent's output is what separates augmentation that works from augmentation that drifts into rubber-stamp review. AAFL calls this practitioner posture the **translator stance**: agents produce confident first drafts; humans translate between agent capability and instructional soundness, judging at specific decision points, gating release, and holding the accountability the agent cannot. The translator stance is not a third position on the spectrum; it is the discipline that operationalizes the augmentation position. Substitution requires no stance — there is no human to take one. Augmentation without the translator stance collapses into review-theater.

The translator stance holds that the *authorship inversion* is real — agents write first, humans validate — but that the *accountability inversion* must not be. The learner does not care who wrote the artifact. The learner cares whether the artifact improves their performance. The institution does not care who drafted the assessment. The institution cares whether the assessment validly measures the construct claimed and whether it stands up in audit. Agents do not (yet) bear professional, legal, or institutional accountability for these claims; humans do. AAFL formalizes the gates where human accountability is irreducible regardless of agent capability.

But the conceptual realignment goes deeper than authorship. The *purpose* of doing ID is changing, too — or, more accurately, the agent era exposes a change that was already underway in the most performance-oriented corners of L&D, and provides the eval tooling to finally complete it.

ADDIE was built around *learning attainment*: phases optimize for producing a course that learners pass. That framing was not a failure of imagination on the part of its architects. The performance-oriented tradition recognized the gap from the beginning — Thomas Gilbert, Robert Mager, Geary Rummler and Alan Brache, and the broader Human Performance Technology field that grew up around their work argued that workplace performance, not course completion, was the legitimate outcome of L&D investment. The constraint was *tooling*. Pre/post tests, knowledge checks, retention assessments, multiple-choice quizzes — these were what could practically be measured at scale through the 1980s, 1990s, and 2000s. The eval tools of those decades let practitioners ask *did the learner absorb the content*, but not *did the absorption change what they do at work tomorrow*.

The agent era removes that constraint. AI agents, paired with augmented-reality overlays, instrumentation in the work environment, and per-learner telemetry, now make *while-you-work* evaluation practical at scale: did this technician fix the machine faster? Did this analyst flag the right indicator under load? Did the credentialed officer execute the correct procedure during the incident? The measurement keeps up with the outcome question for the first time. What learning scientists could only argue for in the abstract becomes operationally available.

That is why the choice of organizing outcome is no longer abstract; it is the spec the agent fulfills. An agent will optimize whatever you tell it to optimize. If the eval rubric measures course completion and quiz scores, the agent will produce courses that maximize completion and quiz scores — and the result may be entirely uncorrelated with workplace performance. If the eval rubric measures time-to-competency and transfer-to-job, the agent's output orients toward those outcomes instead.

AAFL therefore takes the opinionated stance: **workplace performance is the framework's organizing outcome, not learning attainment.** Every gate, every eval dimension, every PRS level ties back to performance. ADDIE's five-phase spine survives — practitioners still Analyze, Design, Develop, Implement, and Evaluate — but the organizing question those phases answer changes from *did the learner pass* to *did workplace performance change*. AAFL is continuity-with-evolution: it inherits ADDIE's process, refits it for agent-era eval tools, and anchors it where the HPT tradition always argued the outcome belonged. The substantive engagement with named voices is consolidated in §9.

The realignment, in summary, is from:

- *Designer as maker* → *designer as judge, gate-keeper, and accountability holder for the system that makes*
- *Course completion as the win* → *workplace performance as the win*
- *AI as accelerant for human authorship* → *AI as first-draft author within human-defined judgment gates*
- *Eval tooling as the limit on what could be measured* → *eval tooling as the spec the agent fulfills*

What follows is the architecture that operates inside this realignment.

---

## §1.5. Method — How This Framework Was Developed

A framework paper that proposes a new operating model for a field's practice owes the reader an account of how the proposal was arrived at. AAFL was developed as **design-based theorizing** (Reeves & McKenney, 2013) grounded in two substantive inputs: a literature scan of the human performance technology and agent-era AI-in-instructional-design (AI-in-ID) traditions, and the author's federal instructional design practice across multiple production deliveries.

### Inputs to the synthesis

**Literature scan (2025–2026).** A bounded review of three intersecting bodies of work: (i) the human performance technology (HPT) tradition (Gilbert, 1978; Rummler & Brache, 1990; Moore, 2017; Mosher & Gottfredson, 2011; Brinkerhoff, 2003; Kirkpatrick & Kirkpatrick, 2016) for the *workplace performance as organizing outcome* commitment; (ii) the contemporary AI-in-ID literature (Chai et al., 2025; Hardman, 2025; EduPlanner, 2025; AUSS, 2025) and the practitioner-competency literature surrounding it (Dakan & Feller, 2023–2025, anchored in the *AI Fluency for Educators* and *AI Fluency: Framework & Foundations* courses published by Anthropic Academy) for the agent-era state of the art; and (iii) methodological adjacencies — eval-driven agent engineering practice (Anthropic Engineering, 2025), human-algorithm centaur models (Saghafian et al., 2024), and empirical work on uneven AI capability across tasks (Brynjolfsson et al., 2023; Dell'Acqua et al., 2023). The positioning records, white-space analysis, named-voice engagement map, and full annotated reading list are versioned alongside this whitepaper in a public project repository (see §1.5 Reproducibility below).

**Practitioner experience.** The author has applied AI-Enhanced ADDIE workflows across ACE-accredited graduate certificate and post-baccalaureate programs in federal security education. Adjacent practice that informed the framework's design choices, particularly around the human-in-the-loop discipline and the eval-as-spec stance, includes extensive AI-assisted software-engineering work; advocacy-research and policy-paper authorship for an unnamed civil-society organization, where AI-drafted materials had to clear external-audience credibility bars; and a sustained curriculum-design body of work for an unnamed performing-arts credentialing program operating internationally, where the agent-era split between source-truth fidelity and pedagogical strategy first surfaced as a recurring design problem. The federal practice produced the operational observations on first-draft cycle compression reported in §1 and the practitioner-level PRS-1 / PRS-2 productivity bands reported in §6. These are practitioner-level observations across multiple production deliveries — they are not the outputs of a controlled study, and the framework treats them as such (see §12, Limitations and Future Work).

### Synthesis method

The framework's distinctive choices — the eight HITL gates, the pedagogical-vs-production split, the Proportional Restraint Scale with classification caps, the eval-as-spec discipline, and the three cross-cutting layers — emerged from this synthesis under four design criteria: (a) preserve the workplace-performance commitment of the HPT tradition, (b) absorb the eval-driven and centaur-model methodological adjacencies, (c) extend the named published AI-in-ID frameworks rather than competing with them, and (d) address the federal-applicability white space that no civilian framework currently occupies. The integration is the contribution; no individual element is novel in isolation.

### What this method is *not*

AAFL has not been developed via external expert-panel consensus methods such as the Delphi technique (the iterative-expert-feedback methodology common in education-research framework development); it has not been validated by independent field tests at PRS-3+; it does not draw on federally-funded user research; and it does not yet rest on published case studies that any reader can audit. These are deliberate scope boundaries for this whitepaper — the framework is offered to the field as a *spec inviting field validation*, not as a validated framework. The §12 Limitations and Future Work section names this explicitly. Field tests, external review panels, and comparative practitioner studies are the natural next steps; the framework's structure tolerates row-level updates without changing its architecture (see §11, Risk 4, and §5 "When the line moves").

### Reproducibility

The literature scan, white-space analysis, named-voice engagement map, and source-citation bibliography are versioned in the project repository alongside this whitepaper. A reader who wishes to audit the synthesis can trace any claim in AAFL back to its source in those documents.

---

## §2. Architecture — The Hybrid Stack

AAFL preserves ADDIE's five phase names as the **vertical spine** and introduces three **cross-cutting horizontal layers** that did not exist in classic ADDIE.

The decision to keep ADDIE's vocabulary is deliberate. Federal contracting officers, ACE evaluators, Quality Matters reviewers, military training command staff, and corporate L&D leadership all read in ADDIE's vocabulary. A framework that begins by replacing the vocabulary forfeits the audience most likely to adopt it. AAFL assumes the audience knows ADDIE; the framework's contribution is what runs *across* the phases, not what replaces them.

### The hybrid stack

```
   ╔═══════════════════════════════════════════════════════════════════════╗
   ║  GOVERNANCE LAYER  ·  policy boundary                                 ║
   ║  escalation · classification · audit · accreditation · IP discipline  ║
   ╠═══════════════════════════════════════════════════════════════════════╣
   ║  EVALUATION-AS-SPEC LAYER  ·  quality boundary                        ║
   ║  performance evals defined BEFORE agents draft; rubric blocks Design + Develop ║
   ╠═══════════════════════════════════════════════════════════════════════╣
   ║  ORCHESTRATION LAYER  ·  routes within both boundaries                ║
   ║  agent routing · HITL gates · model selection · audit log             ║
   ╚═══════════════════════════════════════════════════════════════════════╝
          ▲  ▼        ▲  ▼        ▲  ▼         ▲  ▼          ▲  ▼
          │  │        │  │        │  │         │  │          │  │
   ┌──────┴──┴────┬───┴──┴────┬───┴──┴─────┬───┴──┴──────┬────┴──┴─────┐
   │   ANALYZE    │   DESIGN  │   DEVELOP  │  IMPLEMENT  │   EVALUATE  │   ◄── ADDIE spine
   └──────────────┴───────────┴────────────┴─────────────┴─────────────┘
                                    ▲
                                    │  (every artifact in every phase
                                    │   passes through this inner cycle)
                                    ▼
                  ┌────────────────────────────────────┐
                  │        THE TRANSLATOR'S LOOP       │
                  │                                    │
                  │      Draft  ────►  Discern         │
                  │        ▲              │            │
                  │        │              ▼            │
                  │      Release  ◄──  Validate        │
                  └────────────────────────────────────┘
                                    │
                                    ▼
   ┌───────────────────────────────────────────────────────────────────────┐
   │  ANCHOR — Workplace performance  ·  Kirkpatrick L3/L4                 │
   │  Every phase, every gate, every eval ties back to whether the         │
   │  intervention moved time-to-competency, error rate, throughput, or    │
   │  transfer-to-job. Not "did the learner pass."                         │
   └───────────────────────────────────────────────────────────────────────┘
```

*Figure 1 — alt-text caption.* AAFL framework architecture. Three horizontal cross-cutting layers stacked top to bottom — Governance, Evaluation-as-Spec, and Orchestration (each layer's specific responsibilities are expanded in the *What's in each cross-cutting layer* subsection below). Beneath the three layers, ADDIE's five phases — Analyze, Design, Develop, Implement, Evaluate — run left to right as the framework's vertical spine. Each phase connects to the three layers above via bidirectional arrows: the layers shape the phase's work, and the phase reports back into the layers' audit, eval, and governance state. Each phase column carries an embedded *DDVR* indicator — four small chiclets reading D-D-V-R — signaling that the four-step Translator's Loop (Draft → Discern → Validate → Release) runs *within* each phase against every agent-produced artifact. A legend below the phase row expands DDVR into its four numbered steps with their human-or-agent role assignments. At the bottom sits the framework's anchor: workplace performance, Kirkpatrick L3/L4 — every phase, every gate, every eval ties back to whether the intervention moved time-to-competency, error rate, throughput, or transfer-to-job, not whether the learner passed.

### Why hybrid (not pure overlay, not pure replacement)

Three architectural choices were considered:

- **(a) Pure overlay** — keep ADDIE phases unchanged, bolt on HITL gates as checklists. This is too conservative. Orchestration, evaluation, and governance need to run *continuously* across every phase; they cannot be a Phase 6.
- **(b) Pure replacement** — discard ADDIE phases, introduce new phase names like *Brief → Generate → Discern → Validate → Release → Learn*. Too radical. Forfeits ADDIE Guide lineage, federal vocabulary, and accreditation language. Reduces credibility with the audience most likely to adopt.
- **(c) Hybrid** — preserve the phase names, add cross-cutting layers and an inner motion. Practitioners keep the map they already use; AAFL adds the new instruments running across it.

AAFL adopts (c). ADDIE Guide remains the *reference* (the dictionary); AAFL is the *operating manual* (the process for using the dictionary in the agent era).

### What's in each cross-cutting layer

*The layers are presented here in the same top-to-bottom order they appear in Figure 1: Governance (the outermost policy boundary), then Evaluation-as-Spec (the quality boundary inside it), then Orchestration (the runtime within both).*

**The Governance Layer** is the institutional infrastructure. It captures audit trail (chain of custody for every agent-generated artifact, model version recorded, prompt-and-response archived for the contract retention window), classification handling (FedRAMP, NIST 800-171, CUI marking, ITAR/EAR where applicable), accreditation alignment (ACE evaluator expectations, Quality Matters Standards 2/3/8, WCAG 2.1 AA + Section 508), escalation paths (what happens when the human reviewer disagrees with the agent's output, when does human override, when does the disagreement escalate), and **PRS caps by data classification** — the federal-applicability claim no civilian framework currently makes.

**The Evaluation-as-Spec Layer** borrows the eval-driven discipline from agent engineering practice ("define evals before agents fulfill them"; Anthropic Engineering, 2025) and operationalizes it for ID. The eval rubric for a given course is authored at the Performance Outcome Gate (Gate 2) *before* any Design-phase or Develop-phase agent runs. The rubric *blocks both Design and Develop*. No rubric, no Design — and certainly no Develop. The reasoning is straightforward: a malformed design is worse than no design, because malformed designs commit reviewers, schedule, and downstream production to the wrong target. This is the framework's single biggest defense against the agent-era failure mode of artifacts that are well-formed but not instructionally sound.

**The Orchestration Layer** routes work between agents and humans. It decides which agent runs which task, which model is appropriate for which class of work (frontier vs cost-optimized vs federal-tenant), when artifacts route to which gate, and what gets logged. At PRS-1, orchestration is manual — the human is the orchestrator. At higher PRS levels, orchestration becomes increasingly automated within the boundaries Governance and Evaluation-as-Spec define.

The three layers work together in nested order: Governance sets the policy boundary; Evaluation-as-Spec sets the quality boundary inside it; Orchestration routes work within both.

---

## §3. The Translator's Loop

Inside every phase, every artifact runs through a four-step inner cycle. The diagram-side mnemonic is **DDVR** — the four chiclets embedded in each ADDIE column of Figure 1:

> **Draft → Discern → Validate → Release**

This is *the unit of work* in AAFL. Practitioners measure progress not in deliverables but in loop completions. A phase ends when all its artifacts have passed the loop.

**Draft.** The agent generates the artifact against a brief that includes the eval rubric authored at the Performance Outcome Gate. The brief is precise — it specifies the artifact type, the source material, the constraint set (cognitive level, modality, accessibility tier, classification), and the eval criteria.

**Discern.** The human applies the appropriate HITL gate criterion (see §4). The Anthropic AI Fluency framework (Dakan & Feller) gives the practitioner-side competency that operates here: *Discernment* is the act of judging which agent output meets the criterion.

**Validate.** For production-class artifacts, a second pass against eval criteria — automated where possible (accessibility scans, citation checks, classification marking); human where not (pedagogical fit, learner-context judgment).

**Release.** The artifact is signed by the accountable human, archived to the audit trail (Governance Layer), and made available to downstream phases.

The Translator's Loop is also the practitioner-facing slogan for AAFL. Where the framework name (AAFL) is institutional and acronym-coded, the Translator's Loop is human and process-coded. Both terms operate in the literature; both refer to the same framework.

---

## §4. The HITL Decision-Gate Taxonomy

Eight gates. A memorable count, mapped to ADDIE phases, with each gate classified as either **pedagogical** (humans-only, value-statement decisions) or **production** (agent-prepared, human-signed, sampleable at higher PRS levels). The split is the framework's load-bearing distinction.

### Gate 1 — Learner Reality (Analyze, pedagogical)

*Stake.* Whether the design serves a real population or a synthetic one.

*Agent input.* Drafted learner persona; prior-knowledge map; performance-gap hypothesis; demographic and contextual analysis.

*Human criterion.* *Does this match what I have actually heard from this audience? What is the agent confidently wrong about?*

*Failure mode.* Designing for the LLM's median-case learner instead of the actual workplace population — ships a course that solves no one's problem.

### Gate 2 — Performance Outcome (Analyze → Design boundary, pedagogical)

*Stake.* The terminal definition of mastery — what workplace performance looks like when the intervention has worked. This is where AAFL departs from legacy *learning objectives*. Traditional learning objectives describe what a learner should know or be able to do at the end of the course; AAFL's performance outcomes describe what the learner should *do differently at work*. The two are not interchangeable. A learner can master every learning objective and still not change a single workplace behavior — which is precisely the gap the pre-agent eval tooling left open (see §1). This gate is where the new eval tooling has the most to offer: *while-you-work* signals make these performance outcomes practically measurable for the first time.

*Agent input.* Candidate objectives at multiple cognitive levels; backward-mapped action lists; performance-context scenarios; assessment criteria.

*Human criterion.* *Are these the performance outcomes that matter, or the outcomes that are easiest to measure? Time-to-competency, error rate, throughput, transfer-to-job — defined and measurable?*

*Failure mode.* Defaulting to learning-attainment proxies (course completion, knowledge-check scores) instead of performance metrics. These proxies persisted because the eval tools of the pre-agent era could not reliably measure anything else. The agent era removes that excuse — and an agent will optimize whatever you tell it to optimize, including the wrong thing.

*Critical role.* This gate **blocks** the Evaluation-as-Spec Layer for both the Design and Develop phases. The eval rubric is authored here, *before* any Design-phase or Develop-phase agent runs. No rubric, no Design — and no Develop. The framework's working principle is that a malformed design is worse than no design at all: a design committed to the wrong performance outcome will marshal downstream production effort, reviewer attention, and schedule around an incorrect target, and the cost of unwinding that is far higher than the cost of pausing Design until Gate 2 is signed.

### Gate 3 — Pedagogical Strategy (Design, pedagogical)

*Stake.* Whether the instructional approach (scaffolding sequence, modality mix, practice-to-feedback ratio) fits the learner and the content.

*Agent input.* 2–3 candidate strategies with rationales; cognitive-load analysis; modality recommendations; UDL-fit notes.

*Human criterion.* *Which of these survives contact with this specific learner population in this specific workplace context? Which one accelerates performance the soonest with the least cognitive cost?*

*Failure mode.* Adopting a strategy because it is well-formed in the agent's draft rather than because it fits the learner.

### Gate 4 — Source Truth (Develop, production)

*Stake.* Factual and SME accuracy of generated content.

*Agent input.* Drafted content with citations; SME-validated transcripts mapped to drafted points; hallucination-flag pass.

*Human criterion.* *SME-validated, traceable to source, free of hallucinated authority.*

*Federal note.* Non-negotiable in federal contexts. CUI/classification-marked sources only; classified material does not pass through general-purpose agents (caps at PRS-2).

### Gate 5 — Equity & Accessibility (Develop, production)

*Stake.* WCAG/UDL conformance, representational fairness, cognitive load fit.

*Agent input.* Accessibility-checked draft; alt-text; transcripts; captions; reading-level analysis; automated WCAG scan results; representational-bias audit.

*Human criterion.* *Does this work for the learner whose context I have least imagined?*

### Gate 6 — Assessment Validity (Develop, production)

*Stake.* Whether the assessment measures the stated outcome.

*Agent input.* Item bank; rubric; distractor analysis; item-response statistics where available.

*Human criterion.* *Construct validity, not surface plausibility. Does a learner who passes this actually have the competency that accelerates workplace performance?*

*Failure mode.* Agent-generated items that look professional but measure surface fluency (recall) rather than the targeted competency (transfer). An assessment that does not predict workplace performance is theatre, regardless of psychometric polish.

### Gate 7 — Release (Implement, production)

*Stake.* Whether the artifact is fit to put in front of learners.

*Agent input.* QA bundle; packaging (SCORM/xAPI/cmi5); deployment checklist; 508 conformance report; classification marking confirmation.

*Human criterion.* *Named accountable owner. Reviewer signature. Artifact-of-record archived to the Governance Layer audit trail.*

### Gate 8 — Performance-Effect (Evaluate, pedagogical)

*Stake.* Whether the intervention actually accelerated workplace performance — not just whether the course was completed. "Accelerated workplace performance" is increasingly operationalized through *while-you-work* signal capture: AR overlays at the moment of task execution that log whether the technician completed the procedure correctly the first time; instrumented work environments that record cycle-time and error rates; per-learner telemetry that surfaces the gap between training-environment competence and on-the-job execution. These signals — unavailable to ADDIE's original architects — are what make Gate 8 operationally answerable today rather than aspirational (see §1, *agent era removes the tooling constraint*).

*Agent input.* Outcome data; analytics; drop-off patterns; pre/post performance metrics; transfer-to-job indicators; error-rate change; time-to-competency analysis; hypothesis on causes.

*Human criterion.* *Causal interpretation, decision to iterate, learner-harm assessment. Did performance get faster, more accurate, more capable — and if so, can we credibly claim the intervention caused it?*

*Vocabulary note.* This is Kirkpatrick L3 (Behavior) and L4 (Results) territory in the L&D dialect every reviewer of this work will use. The framework's organizing outcome lives or dies here.

### The gates at a glance

```
   ╔══════════════════╗  ╔══════════════════╗  ╔══════════════════╗  ╔══════════════════╗  ╔══════════════════╗
   ║     ANALYZE      ║  ║      DESIGN      ║  ║     DEVELOP      ║  ║    IMPLEMENT     ║  ║     EVALUATE     ║
   ╚══════════════════╝  ╚══════════════════╝  ╚══════════════════╝  ╚══════════════════╝  ╚══════════════════╝
   ┃ Gate 1           ┃  ┃ Gate 3           ┃  │ Gate 4           │  │ Gate 7           │  ┃ Gate 8           ┃
   ┃ Learner Reality  ┃  ┃ Pedagogical      ┃  │ Source Truth     │  │ Release          │  ┃ Performance-     ┃
   ┃ (pedagogical)    ┃  ┃ Strategy         ┃  │ (production)     │  │ (production)     │  ┃ Effect           ┃
   ┃                  ┃  ┃ (pedagogical)    ┃  │                  │  │                  │  ┃ (pedagogical)    ┃
   ┃ Gate 2           ┃  ┃                  ┃  │ Gate 5           │  │                  │  ┃                  ┃
   ┃ Performance      ┃  ┃                  ┃  │ Equity & A11y    │  │                  │  ┃                  ┃
   ┃ Outcome          ┃  ┃                  ┃  │ (production)     │  │                  │  ┃                  ┃
   ┃ (pedagogical)    ┃  ┃                  ┃  │                  │  │                  │  ┃                  ┃
   ┃ ⚠  BLOCKS        ┃  ┃                  ┃  │ Gate 6           │  │                  │  ┃                  ┃
   ┃    DEVELOP       ┃  ┃                  ┃  │ Assessment       │  │                  │  ┃                  ┃
   ┃ (no rubric,      ┃  ┃                  ┃  │ Validity         │  │                  │  ┃                  ┃
   ┃  no Develop)     ┃  ┃                  ┃  │ (production)     │  │                  │  ┃                  ┃
   ┗━━━━━━━━━━━━━━━━━━┛  ┗━━━━━━━━━━━━━━━━━━┛  └──────────────────┘  └──────────────────┘  ┗━━━━━━━━━━━━━━━━━━┛

   Legend:  ┃━┃  Pedagogical gates  — humans-only at every PRS level (anti-replacement claim)
            │─│  Production gates   — agent-prepared, human-signed; sampleable at higher PRS levels
            ⚠    Gate 2 blocks Design AND Develop until the eval rubric is signed (Evaluation-as-Spec discipline)
```

*Figure 2 — alt-text caption.* The eight AAFL HITL decision gates mapped to ADDIE phases. Gate 1 (Learner Reality, pedagogical) and Gate 2 (Performance Outcome, pedagogical, blocks Design + Develop) sit in the Analyze phase. Gate 3 (Pedagogical Strategy, pedagogical) sits in the Design phase. Gates 4 (Source Truth), 5 (Equity & Accessibility), and 6 (Assessment Validity) — all production gates — cluster in the Develop phase. Gate 7 (Release, production) sits in the Implement phase. Gate 8 (Performance-Effect, pedagogical) sits in the Evaluate phase. The four pedagogical gates (1, 2, 3, 8) bookend the framework and remain humans-only at every PRS level. The four production gates (4, 5, 6, 7) cluster in Develop and Implement and are agent-prepared and human-signed, becoming sampleable at higher PRS levels. Gate 2 is marked as the framework's structural blocker: until the eval rubric is signed at Gate 2, neither the Design nor the Develop phase can run.

### Reading the gate map

The first three gates and the last (Reality, Performance Outcome, Pedagogical Strategy, Performance-Effect) are *pedagogical*. They are humans-only at all PRS levels. They are where the framework's anti-replacement claim lives: these are the irreducibly human decisions, regardless of agent capability.

The middle four (Source Truth, Equity, Assessment Validity, Release) are *production*. They are agent-prepared and human-signed. At PRS-1 and PRS-2, every production-gate output is reviewed. At PRS-3, only flagged outputs trigger review (the agent's own confidence scoring + automated checks gate the human queue). At PRS-4, production gates become statistical sampling — humans audit a representative slice rather than every artifact.

The pedagogical gates do *not* relax at higher PRS levels. That asymmetry is what prevents the framework from sliding into pure agentic autonomy.

---

## §5. The Agent-Task Taxonomy

The framework's deterministic answer to "what does the agent do, what does the human do" — and the answer it gives to "will AI replace ID practitioners."

### The split principle

> Anything where the cost of being wrong is bounded and reviewable goes to the agent.
> Anything where being wrong harms a learner, breaks trust, or commits the institution stays with the human.

### The taxonomy

The taxonomy uses a third-column tag: **DL** (design loop — compresses ID cycle time), **PL** (performance loop — compresses learner time-to-competency or improves transfer), or **DL+PL** (both).

*Reading the PRS prefixes.* Untagged rows apply at all PRS levels. Rows prefixed **(PRS-3+)** mark capability that is unlocked only at PRS-3 and above; rows prefixed **(PRS-4)** mark capability unlocked only at PRS-4. The prefix is a PRS gate, not a row category — these are not separate "advanced" rows but specific capabilities that PRS-1/PRS-2 implementations should not attempt because the governance discipline required to operate them has not been established. See §6 (Proportional Restraint Scale).

| Agent-led tasks | Human-only tasks | Loop |
|---|---|---|
| Drafting learner-persona templates from raw inputs | Deciding *who the real learner is* and what they don't yet know they need | DL |
| Pulling SME interview transcripts into structured analysis notes | Choosing which SME contradictions are signal vs noise | DL |
| Generating candidate learning objectives at multiple cognitive levels | Selecting which objectives define mastery for *this* program | DL |
| Mapping objectives to existing competency frameworks (ACE, NICE, OPM, JKO) | Defending the mapping in an accreditation review | DL |
| Drafting backward-mapped action lists from performance gap analysis | Validating that the actions actually move workplace performance | DL+PL |
| Generating workflow-moment scenarios from job task analysis | Confirming the moments map to real workflow behaviors | DL+PL |
| Drafting storyboards, scripts, scenario branches | Pedagogical sequencing; narrative coherence; learner-emotional arc | DL |
| First-pass content generation against a validated outline | Final voice, tone, cultural fit, value-loaded framing | DL |
| Generating distractors for multiple-choice items | Construct validity; item-bias review; cut-score setting | DL |
| Producing alt-text, transcripts, captions, reading-level adjustments | Confirming UDL fit for the *least-imagined* learner | DL+PL |
| Running WCAG automated scans, contrast checks, link audits | Adjudicating ambiguous accessibility tradeoffs | DL |
| Generating Quality Matters self-review evidence packages | Final QM reviewer judgment and rubric application | DL |
| Pulling and visualizing learning analytics, drop-off, time-on-task, performance metrics | Causal interpretation of *why* learners disengaged or performance moved | PL |
| Drafting iteration recommendations from outcome data | Deciding which iteration is worth the cost | DL+PL |
| Producing federal-format deliverable packaging (SCORM, xAPI, 508, classification marking) | CUI/classification review and marking sign-off | DL |
| Translating between practitioner-facing and reviewer-facing language | Stakeholder trust calls and political reads | DL |
| Generating evaluation instruments (Kirkpatrick L1–L3 surveys, observation rubrics) | PRS-4 business-impact attribution; performance-causation claims | PL |
| Synthesizing competitor / prior-art scans for instructional approaches | Strategic positioning of the offering | DL |
| Drafting facilitator guides and instructor enablement | Live read of room; recovery from learner derailment | DL+PL |
| Maintaining a living style guide and component library | Deciding when the style itself needs to change | DL |
| **(PRS-3+)** Generating per-learner content variations from a validated template | Setting the variation boundaries; auditing for fairness across subgroups | PL |
| **(PRS-3+)** Real-time hint and scaffold generation during workflow learning | Defining what counts as success and what counts as derailment | PL |
| **(PRS-3+)** Match · Gap · Recommend patterns for performance support | Validating the gap analysis and recommendation logic | PL |
| **(PRS-4)** Continuous content adaptation based on learner performance signals | Setting the risk envelope; auditing the adaptation logic | PL |

### Reading the taxonomy

Most agent-led tasks accelerate the *design loop* (DL) — they compress ID cycle time. This is what most published AI-in-ID work focuses on, and the productivity gains are real (the author's federal practitioner observations of first-draft cycle reductions sit here; see §1 and §12). But by itself, design-loop acceleration ships courses faster without proving they move performance.

*Performance-loop acceleration* (PL) is where the framework's organizing outcome actually plays out. PL tasks cluster at PRS-3+: per-learner variation, real-time scaffolding, performance-support recommendation, continuous adaptation. They belong in the agent column because they are tasks the human ID practitioner *cannot do at scale* — no one can hand-author per-learner content variations for 500 learners — so agent capability on these tasks is genuinely new ground, not substitution.

A concrete, operational instance of PL acceleration in adjacent practice: AR-overlay performance-support tooling deployed in industrial-machine maintenance contexts — voice in, expert answer out, automatic logging, layered knowledge across documentation and per-asset history, AR overlay at the moment of work. It is not formal training; it is performance support delivered into the workflow, exactly the territory PRS-3+ AAFL implementations occupy. The Apply, Solve, and Change moments of need are served at the point of work, not in a classroom.

The human-only column is the framework's anti-replacement claim. Every entry in it is a decision that requires *learner-in-context judgment*, *value commitment*, *causal reasoning*, *political read*, or *institutional accountability*. None of these is bounded-and-reviewable. None of these compresses with model improvement.

### When the line moves

The split is not a permanent claim about AI capability. It is a permanent claim about *what kinds of decisions belong to humans regardless of capability*. As models improve, more rows can move from human-only to agent-led — but only at the production gates (rows 4–7 territory), never at the pedagogical gates (rows 1–3, 8 territory). The pedagogical/production split is the load-bearing distinction; specific row assignments are versioned.

---

## §6. The Proportional Restraint Scale (PRS)

Four PRS levels of HITL implementation. What advances an organization between them is **governance discipline** — not AI capability.

### PRS-1 — Assistant

Agent generates suggestions; human authors every artifact. Human reviews 100% of agent output before incorporation. Modest design-loop savings, consistent with the lower end of generative-AI productivity bands measured inside the jagged frontier in adjacent knowledge-work domains (Brynjolfsson et al., 2023; Dell'Acqua et al., 2023). Default starting posture; always appropriate.

### PRS-2 — Co-designer

Agent drafts artifacts inside a defined scope (a lesson, an item bank, a storyboard); human edits to final. Human reviews 100% of agent output but no longer authors first-draft prose. Substantial first-draft compression — first-draft cycle reductions in the 40–60% range based on the author's federal practitioner observations across multiple production deliveries (see §1, §1.5 Method, §12 Limitations); this range is consistent with the higher end of generative-AI productivity bands inside the frontier (Dell'Acqua et al., 2023, BCG-Harvard field experiment in knowledge work). Most accredited and federal training programs land here.

### PRS-3 — Agent-driven with gates

Agents run production tasks (Source Truth, Equity, Assessment Validity, Release prep) end-to-end inside one phase; humans engage at the eight HITL gates. Output is gate-flagged: clean drafts auto-route through production gates, flagged drafts trigger human review. Per-learner personalization becomes possible — Match · Gap · Recommend territory. First-draft → final compression with gate quality, reallocated to gate quality rather than to volume. **This range is projected, not measured** — AAFL has not yet been operated end-to-end at PRS-3 across a federal program; see §12 (Limitations and Future Work). Performance-loop acceleration becomes real.

### PRS-4 — Bounded autonomy

Multi-agent workflows generate per-learner curriculum end-to-end inside an institution-defined risk envelope. Humans spot-audit, set policy, own escalation. Pedagogical gates stay human; production gates become statistical sampling. The framing changes — at PRS-4, you are not "designing a course" anymore, you are running a performance-acceleration system. Continuous performance-loop acceleration in bounded domains. **No measured productivity bands are available at PRS-4** — the published AI-in-ID literature reports no field deployment at this PRS level at this writing; AAFL's PRS-4 prescription is a forward-looking spec, not a measured operating point (see §12 Limitations).

### The realistic ceiling

> **Higher restraint is not better. Appropriate restraint is better.**

Most federal and accredited programs should sit at **PRS-2 or PRS-3**. PRS-4 is the right answer for a narrow set of contexts and the wrong answer for most.

**Where PRS-4 is inappropriate:**

- **Credentialing and certification programs.** A credential whose content was authored by autonomous agents without human gate-review on each artifact cannot defend itself in audit.
- **Classified content authoring.** No agent autonomy on classified material. Classified content authoring caps at PRS-2 even with approved infrastructure.
- **High-consequence performance training.** Anything where a learner's performance failure has safety, security, or financial consequences requires human-signed production gates.
- **Programs without operational governance discipline.** PRS-4 governance is not a checklist; it is a running system. Organizations that cannot reliably operate PRS-3 governance cannot operate PRS-4 governance at all.

**Where PRS-4 is appropriate:**

- **High-volume skill refreshers** (annual compliance refresh for a 10,000-person workforce)
- **Onboarding pathways** (role-based onboarding where the content space is bounded)
- **Performance support continuum** (real-time recommendations within a defined competency space — the Match · Gap · Recommend pattern, or AR-overlay performance-support tooling deployed at the point of work in industrial-machine maintenance contexts)
- **Adaptive remediation** (agent-driven re-teaching loops *after* the learner has failed a human-validated assessment)

### Performance and what the framework actually delivers

The PRS is not just "how much can the agent do" — it is **how much workplace performance acceleration the system delivers**:

| Level | Design-loop impact | Performance-loop impact |
|---|---|---|
| PRS-1 | ID-design speed gains only | None |
| PRS-2 | Training-development cycle compression (40–60% first-draft, practitioner observation; see §1, §12) | Limited — same content for all learners, produced faster |
| PRS-3 | First-draft → final compression with gate quality | Real — per-learner personalization; performance-support generation |
| PRS-4 | "Designing a course" reframes as "running a performance-acceleration system" | Continuous — real-time learner-to-content fit in bounded domains |

PRS-1 / PRS-2 are *productivity* stories (faster ID work). PRS-3 / PRS-4 are *capability* stories (work that wasn't possible before). The performance-acceleration claim only becomes credible at PRS-3+.

### How to choose the right level

Three questions, asked in order:

1. **What is the consequence space?** The consequence space sets the PRS ceiling:

   | Consequence space                                | PRS ceiling          |
   |--------------------------------------------------|----------------------|
   | Credentialing / classified / safety-critical     | Cap at **PRS-2**     |
   | CUI / accredited but not classified              | Consider **PRS-3**   |
   | Public-trust unclassified high-volume            | Consider **PRS-4**   |

2. **What governance is operationally running?** PRS-1 governance means a working audit trail (a record of which agent ran which task with which model against which source, with the human gate decision logged); reliable handling of agent-output classification; and a documented escalation path when the human reviewer disagrees with the agent. If the organization cannot reliably operate that PRS-1 baseline, do not aspire to PRS-3. PRS readiness follows operational capacity, not desire.
3. **What is the performance claim?** If the goal is "ship courses faster," PRS-2 suffices. If the goal is "compress time-to-competency for a 10,000-person workforce," PRS-3+ becomes the answer. Match the level to the claim.

If any answer is unclear, default to one level lower than the question would suggest. *Higher restraint is not better; appropriate restraint is better.*

---

## §7. The Eval Framework

How to evaluate an AI-designed instructional intervention. Borrows the eval-driven discipline from agent engineering practice (*"define evals before agents fulfill them"*) and anchors it in workplace performance as the organizing outcome.

### The discipline

> The eval rubric for a given course is authored at the **Performance Outcome Gate** (HITL Gate 2), *before* any Develop-phase agent runs. Agents are then evaluated against those criteria.

This is the single biggest defense against the agent-era failure mode of *artifacts that are well-formed but not instructionally sound*. An agent that doesn't know what success looks like will produce confident, professional, fluent output that misses the actual outcome — and a reviewer who is checking surface fluency will let it through. The Evaluation-as-Spec Layer makes this discipline **blocking**: neither the Design nor the Develop phase can run until the eval rubric is signed at Gate 2.

### Six dimensions, ordered by priority

#### 1. Performance attainment (primary spine)

**The non-negotiable.** Did workplace performance actually accelerate?

*Measures:* time-to-competency; error rate change; throughput; transfer-to-job; retention over time (30/60/90-day).

*Why primary.* Workplace performance is the framework's organizing outcome. An intervention that does not move performance is a learning experience, not a performance-acceleration intervention. The framework is opinionated: this dimension is the spine, not one of six equal dimensions. This is Kirkpatrick L3 (Behavior) and L4 (Results) territory.

*Failure mode this catches.* Beautiful, well-formed courses that learners complete and pass and that change nothing about workplace performance. The phrasing can read as a contradiction — *how can a well-formed course change nothing?* — but the contradiction is the point. A well-formed course is a *necessary* condition for performance gain, not a *sufficient* one. Transfer-to-job depends on opportunity to practice, reinforcement structures, manager behavior, performance-support availability at the moment of work, and the gap between training-environment fidelity and on-the-job conditions. The course can satisfy every learning-attainment criterion and still fail Kirkpatrick L3/L4 because it never made contact with those downstream conditions. This is exactly why AAFL anchors in workplace performance rather than course completion: the framework refuses to let well-formedness substitute for outcome.

#### 2. Outcome attainment

Did learners demonstrate the stated objectives at the stated mastery threshold? Pre/post, transfer task, performance observation. Kirkpatrick L2.

A learner can pass and not transfer (false positive on the assessment). A learner can fail the assessment and still improve workplace performance (false negative on the assessment). Both dimensions matter; #1 is primary because it is the outcome the institution is buying.

#### 3. Construct validity

Does the assessment actually measure the construct claimed? Item analysis, expert review, fairness audit.

The agent-generated assessment is the place where surface plausibility is most easily mistaken for instructional soundness. Items can be well-formed, distractors plausible, and the whole assessment can measure a subtly different construct than the one stated. Construct validity review at HITL Gate 6 is what catches this.

#### 4. Pedagogical fidelity

Did the implementation match the design intent? Detects drift between Gate 3 (Pedagogical Strategy) decisions and the artifact actually produced; between Gate 2 (Performance Outcome) criteria and assessment items at Gate 6; between learner persona at Gate 1 and content reading level / cultural fit / contextual examples.

Agents drift between phases. The strategy committed at Gate 3 doesn't always survive contact with the source materials and constraint set the agent encounters in Develop; without explicit fidelity checks, the agent re-anchors to the local context and produces artifacts internally consistent with that local context but inconsistent with the Gate 3 commitment. The general phenomenon — capability variance and anchoring drift across adjacent agent tasks — is consistent with the empirical findings on the "jagged frontier" of AI productivity (Brynjolfsson et al., 2023; Dell'Acqua et al., 2023). Fidelity checks at Gate 6 close the loop.

#### 5. Learner experience

The learner-side construct. Did the intervention work for the learner across the population, not just the median case?

*Measures:* cognitive load fit (Sweller-tradition working-memory considerations applied to the artifact's information density and sequence); engagement (drop-off rates, replay rates, voluntary continuation past required completion); equity-of-experience across subgroups (does the median learner succeed while the tails are abandoned? are there subgroup-by-outcome interactions worth surfacing?).

*Why distinct from #2 (Outcome attainment).* A learner can meet the objective and have had a bad experience — high cognitive load, low engagement, equity gaps in supporting subgroups. Learner Experience and Production Integrity (the next dimension) are kept separate because they answer fundamentally different questions: *did the learner have the experience the design intended* (this dimension) vs *was the artifact infrastructurally fit to ship* (the next dimension). Conflating them obscures the trade-offs.

#### 6. Production integrity

The infrastructure-side construct. Was the artifact infrastructurally fit to ship?

*Measures:* source-traceability (every claim citable to a validated source; no hallucinated authority); accessibility conformance (WCAG 2.1 AA, Section 508, alt-text completeness, transcript accuracy, contrast compliance); classification compliance (CUI marking, FedRAMP, NIST 800-171 where applicable; ITAR/EAR where applicable).

*Why distinct from #5 (Learner experience).* Production integrity dimensions are *runnable as checks against spec* — accessibility scanners, citation auditors, classification-marking validators — without a learner in the loop. Learner-experience dimensions require learner data. In federal contexts, production integrity is gating, not advisory: a CUI training program that ships without classification compliance — for example, source material that should have been marked CUI but was reproduced unmarked into a learner-facing module, or an artifact stored in a tenant cleared only for FOUO — is not primarily an instructional design problem. It is a federal compliance incident. The ID team owns the consequences (rework, retraction, possible reporting obligation), the program owns the audit-finding exposure, and the institution owns the accreditation risk. AAFL treats production integrity as gating to keep this category of failure out of the path to release in the first place.

### Eval framework × Proportional Restraint Scale

The rubric is authored at Gate 2 before Design at every PRS level — its existence is constant. What changes across PRS levels is *what runs against it* and *how much is reviewed*:

- **PRS-1 and PRS-2** — human or human-led drafts are evaluated against the rubric; 100% human review of every artifact.
- **PRS-3** — agents run production tasks against the rubric; humans review agent-flagged outputs plus a statistical sample of the rest.
- **PRS-4** — continuous, real-time evaluation of agent outputs against the rubric; humans audit aggregate eval performance rather than individual artifacts.

Refer back to §6 for the substantive PRS level definitions; this section only restates the eval-discipline implications at each level.

### What the eval framework requires

The framework refuses to let Develop run until the practitioner can answer:

1. What workplace performance metric will move (and how will we measure it)?
2. What is the mastery threshold for the stated objectives?
3. What construct does each assessment item measure, and how will we know?
4. What pedagogical strategy has been committed, and what is fidelity drift?
5. What does equity-of-experience look like for this learner population?

If the practitioner cannot answer these before Design, the rubric is not yet authored.

---

## §8. The Three Cross-Cutting Layers

Architectural depth on the three layers that did not exist in classic ADDIE.

### Orchestration

Routes work between agents and humans. Decides:

- **Which agent runs which task.** A specialized item-writer agent handles distractor generation; a different agent handles facilitator-guide drafting; orchestration knows which is appropriate.
- **Which model is appropriate.** Frontier models for high-judgment drafting; cost-optimized models for high-volume formatting; government-tenant generative AI tools (only environments cleared for the relevant data classification) for CUI work. Orchestration is the layer that enforces classification-based model selection.
- **When artifacts route to which gate.** A drafted assessment item routes to Gate 6 (Assessment Validity) for human review at PRS-1 / PRS-2; at PRS-3+, agent-confidence-flagged items route to Gate 6 while clean items route directly to Validate.
- **What gets logged.** Every agent invocation, every model version, every human gate decision. The orchestration log is the input to the Governance Layer audit trail.

### Evaluation-as-Spec

*Evaluation-as-Spec* is a practice borrowed from agent engineering (Anthropic Engineering, 2025) where the criteria an agent's output will be judged against are defined as a structured artifact — the *eval rubric* — *before* the agent runs. The rubric is the spec the agent fulfills. The discipline inverts the conventional Design-then-evaluate flow: instead of building first and checking against criteria afterward, AAFL requires the criteria to exist, in writing, before any building begins. This is the framework's structural answer to the agent-era failure mode of *artifacts that are well-formed but not instructionally sound*.

**The blocking discipline.** Neither the Design nor the Develop phase can run until:

1. The Performance Outcome Gate (Gate 2) has been signed
2. The eval rubric is authored, including all six dimensions (Performance attainment, Outcome attainment, Construct validity, Pedagogical fidelity, Learner experience, Production integrity)
3. The rubric defines measurable criteria — not aspirations

Without a blocking eval rubric, agents will produce surface-fluent content that drifts from the intended outcome. The Layer makes the rubric a precondition, not a postcondition.

### Governance

Institutional accountability. Captures:

- **Audit trail.** Chain of custody for every agent-generated artifact: model version, prompt-and-response, human reviewer signature, gate-flag history, classification marking. Retained for the contract retention window.
- **Classification handling.** FedRAMP, NIST 800-171, CUI marking, Section 508 conformance, ITAR/EAR where applicable.
- **Accreditation alignment.** ACE evaluator expectations; Quality Matters Standards 2 (Learning Objectives), 3 (Assessment), 8 (Accessibility); WCAG 2.1 AA + Section 508 conformance evidence.
- **Escalation paths.** Defined human-side decision protocol for when the human reviewer disagrees with the agent's output, when human override is logged, when the disagreement escalates to a senior reviewer or governance board.
- **PRS caps by classification.** No PRS-4 on classified content. PRS-3 only on approved federal-tenant infrastructure. PRS-4 only on public-trust unclassified high-volume work. Caps are *enforced* by the Layer, not aspirational.

The federal claim AAFL can defensibly make: among the published AI-era ID frameworks reviewed in this work (see Appendix B for the comparative scan — ADDIE, FRAME™, Anthropic 4Ds, Chai et al., EduPlanner, AUSS, Action Mapping), AAFL appears to be the only framework that prescribes PRS caps tied to data classification. That is exactly the question federal contracting officers ask first.

---

## §9. Engagement With Prior Frameworks and Intellectual Lineage

AAFL enters the literature as a coherent extension and integration of existing work, not as a clean-break replacement. The engagement here is substantive and structural rather than plank-by-plank: AAFL inherits a tradition of thought rather than borrowing isolated techniques. The reader should be able to recognize the lineage without being able to reduce any one feature of the architecture to any single source.

### The performance tradition

The Human Performance Technology (HPT) tradition is the bedrock AAFL inherits — a body of work that has insisted on workplace performance as the legitimate outcome of L&D investment for more than half a century. The decisive intellectual contributions in that tradition include Thomas Gilbert's *Human Competence* (1978), which reframed the unit of analysis from the learner's behavior to the performer's output and gave the field its enduring distinction between behavior and accomplishment; Geary Rummler and Alan Brache's *Improving Performance* (1990), which treated workplace performance as a systems-level property; and the long-running professional infrastructure of the International Society for Performance Improvement, which sustained the discipline through periods when the rest of L&D was preoccupied with course completion as the win condition.

Workplace-oriented operational articulations of the same commitment include Cathy Moore's Action Mapping (2008), which insists on backward design from business performance goals; Bob Mosher and Conrad Gottfredson's 5 Moments of Need (2011), which draws the line between formal learning (the New and More moments) and performance support (Apply, Solve, Change) and locates the bulk of workplace skill acquisition outside formal training; Allison Rossett and Lisa Schafer's performance-support taxonomy (Planners, Advisors, Coaches, Sidekicks, 2007) which named the categories of in-workflow help that AR-overlay tooling now operates; and Robert Brinkerhoff's Success Case Method (2003), which provided the methodology for tracing whether an intervention actually moved performance for the workers who used it. The Kirkpatrick L1–L4 vocabulary (1959, updated 2016) is the dialect every reviewer of AAFL will use; AAFL adopts the vocabulary natively.

These works do not appear in AAFL as plank-by-plank derivations. They appear as bedrock — the assumption that workplace performance is the legitimate organizing outcome, that course completion is a weak proxy, that performance support belongs in the workflow rather than in the classroom, and that the eval question is *did performance move*, not *did the learner pass*. AAFL does not paraphrase any one of these voices; it operates inside the consensus they built.

### ADDIE as the architectural heritage

**ADDIE** (Branson et al., 1975, FSU). AAFL is ADDIE practiced at agent speed with HITL gates and three new layers. *Continuity, not replacement.* ADDIE Guide remains the reference; AAFL is the operating manual. The decision to preserve ADDIE's vocabulary is the framework's single largest concession to its audience: federal contracting officers, ACE evaluators, Quality Matters reviewers, and military training command staff all read in ADDIE's vocabulary, and a framework that begins by replacing the vocabulary forfeits the audience most likely to adopt it.

### Iterative design heritage

**SAM** (Allen Interactions, 2012). AAFL inherits SAM's iterative discipline. The Translator's Loop is functionally similar to SAM's rapid-prototyping cycle, applied at per-artifact granularity rather than per-course granularity.

### Pedagogical-design heritage

AAFL's pedagogical gates — Learner Reality, Performance Outcome, Pedagogical Strategy, and Performance-Effect — do not invent the underlying instructional-design theory. They operate against a body of work that any ID reviewer will expect to see named.

**Gagné's *Conditions of Learning*** (1985; original 1965) provides the cognitive-architecture grounding for the conditions under which different categories of learning outcome can be reliably produced. AAFL's Gate 3 (Pedagogical Strategy) is the framework's structural commitment to asking *which conditions does this strategy create for this learner population*; the question is Gagné's even when the answer is agent-drafted. **Dick, Carey & Carey's *Systematic Design of Instruction*** (2014, 8th ed.; original 1978) is the canonical systematic-design textbook against which any ADDIE-extension framework will be read; AAFL inherits its commitment to backward-mapped objectives and criterion-referenced assessment, both operationalized at Gate 2 (Performance Outcome) and Gate 6 (Assessment Validity).

**Merrill's First Principles of Instruction** (2002, *Educational Technology Research and Development*) consolidates the cross-theoretic instructional principles — task-centeredness, activation of prior knowledge, demonstration, application, integration — that AAFL's pedagogical gates assume without restating. A practitioner who passes Gate 3 with a strategy that violates Merrill's principles has produced a pedagogically thin design; the framework does not relitigate Merrill, it operates on top of him.

**Reigeluth's *Instructional-Design Theories and Models*** (1999, 2009, 2017) catalogs the theoretical pluralism within which AAFL is one operating choice. AAFL takes an explicitly *performance-acceleration-oriented* stance within that pluralism; it does not claim that workplace performance is the only legitimate organizing outcome of L&D, only that it is the legitimate organizing outcome for the workplace contexts AAFL addresses (see §12 Limitations on K-12 scope).

**Universal Design for Learning** (Meyer, Rose, & Gordon, 2014; CAST, 2018) is the theoretical anchor underneath AAFL's Gate 5 (Equity & Accessibility). The framework's operational instance — automated WCAG 2.1 AA conformance scans, alt-text, transcripts, captions, reading-level analysis — is the production-gate layer; the substantive commitment is UDL's *multiple means of engagement, representation, and action/expression* applied to the agent-era authoring stack. Gate 5's human criterion ("Does this work for the learner whose context I have least imagined?") is UDL's commitment translated into a single reviewer-facing question.

These four anchors are named here, not at individual gates, in keeping with the lineage discipline established in §9's opening paragraph: AAFL is a synthesis, not a composite of borrowed parts.

### Agent-era frameworks

**FRAME™** (Hardman, 2025). FRAME maps capability risk; AAFL maps decision authority. FRAME tells you *which AI to trust for which task*; AAFL tells you *which task humans must keep regardless of which AI you trust.* The frameworks are complementary, not competing — citing FRAME strengthens AAFL's positioning. Hardman's "danger zone" language is the closest published precursor to AAFL's pedagogical-vs-production task split.

**Anthropic AI Fluency Framework / 4Ds** (Dakan & Feller, 2023–2025). The 4Ds (Delegation, Description, Discernment, Diligence) are practitioner *competencies*; AAFL is the *process* those competencies operate within. Discernment lives at every HITL gate; Delegation defines the agent-vs-human task split; Description briefs the agent at every gate; Diligence is the audit trail the Governance Layer records. *Disclosure:* the author completed Anthropic Academy's *AI Fluency for Educators* and *AI Fluency: Framework & Foundations* courses as a learner; AAFL is informed by but independent of those curricula, and the author has no instructional or advisory role at Anthropic.

**Chai et al.** (2025). Peer-reviewed phase-by-phase synthesis of generative AI in instructional system design. The academic anchor for the position that AI integration is phase-specific, not monolithic. AAFL extends Chai et al. by adding the gate taxonomy, the PRS with caps, the Evaluation-as-Spec Layer, and workplace performance as the eval spine.

**Multi-agent academic systems — EduPlanner, AUSS** (2025). Cited as prior art on multi-agent ID systems. AAFL distinguishes itself by foregrounding *human gates*, not multi-agent collaboration. EduPlanner's Evaluator/Optimizer/Analyst is an agent harness; AAFL's eight gates are human criteria.

### Methodological foundations

**Anthropic Engineering — eval-driven development** (2025). Source of the technical discipline borrowed for the Evaluation-as-Spec Layer. Cited as methodological foundation, not as ID framework.

**Centaur models** (Saghafian et al., 2024, *Harvard Data Science Review*). Hybrid human-algorithm symbiosis pattern. The Translator's Loop is functionally a centaur cycle applied to instructional artifact production.

**Human + Machine** (Davenport & Daugherty, 2018, updated 2024). The augment-not-replace operating principle, articulated for organizational practice generally. AAFL localizes this thesis to ID specifically.

**Brynjolfsson et al., *Navigating the Jagged Technological Frontier*** (2023). Empirical grounding for the claim that AI capability is uneven across tasks within the same role — the precondition for any framework that asks *which tasks belong to whom*. **Dell'Acqua et al.** (2023, BCG-Harvard field experiment, HBS Working Paper 24-013) is the companion field-experimental study cited in §6 as the productivity-band anchor for PRS-1 and PRS-2.

### Engagement with the critic camp

A framework that proposes to operationalize agent capability in instructional design owes the reader a substantive engagement with the critical AI-in-education tradition, not just the productivity-oriented and HPT-oriented traditions. Several concerns from that tradition shape AAFL's design choices even when they are not named at individual features.

**Selwyn's *Should Robots Replace Teachers?*** (2019, Polity) raises the deskilling concern — that delegating authorship to AI agents hollows out the practitioner profession over time, leaving humans only the credentialing-and-rubber-stamping residue of work the agent now drafts. AAFL's structural response is the four pedagogical gates: Learner Reality, Performance Outcome, Pedagogical Strategy, and Performance-Effect are *humans-only at every PRS level*, including PRS-4. The framework's anti-replacement claim is not a sentimentality about human craft; it is a structural commitment that the value-loaded decisions of instructional design do not relax with model capability. The deskilling concern is taken seriously precisely by refusing to let production-gate automation creep across the pedagogical line.

**Williamson's *Big Data in Education*** (2017, SAGE) raises the surveillance and data-political concerns inherent in learner analytics, adaptive systems, and per-learner content variation — exactly the territory PRS-3 and PRS-4 operate in. AAFL's Governance Layer (§8) and classification-aware caps (§10) are partly a structural response: audit trail, classification handling, escalation paths, and named-accountable-human signatures are the institutional infrastructure that prevents AAFL implementations from becoming the surveillance-and-optimization regimes Williamson describes. PRS-4 is *bounded* autonomy — bounded by classification, by domain, by named risk envelope — not unbounded.

**Holmes, Bialik, & Fadel's *Artificial Intelligence in Education*** (2019, Center for Curriculum Redesign) is the most-cited recent overview of AI's promises and implications for teaching and learning; AAFL inherits its commitment to taking both the affordances and the risks seriously, and its emphasis on educator agency in the face of vendor-driven adoption pressure. The framework's *cite-don't-pitch* engagement principle (§9 close) is partially indebted to Holmes et al.'s posture of substantive engagement rather than evangelism or rejection.

The framework does not claim to resolve the critic camp's concerns — those concerns are about the political economy of AI-in-education and the institutional cultures that adopt these tools, not about framework architecture. AAFL's claim is narrower: the structural choices the framework makes — pedagogical gates as humans-only, caps by classification, blocking eval discipline, audit-trail governance — are the framework architecture's contribution to a problem space the critic camp has correctly named.

### What AAFL adds that the field does not yet integrate

Across all of the cited work, no published framework integrates: an HITL decision-gate taxonomy with explicit pedagogical-vs-production classification; a Proportional Restraint Scale (PRS) with prescribed caps by data classification; a performance-anchored eval framework that *blocks* the Develop phase; and a governance layer that enforces the caps rather than describing them. AAFL's contribution is the integration, not any individual element.

---

## §10. Federal Applicability

For classified, CUI, and federally-accredited contexts, three things change in AAFL.

### The Source Truth, Release, and Production Integrity gates become legally non-negotiable

Audit trail must satisfy FedRAMP, NIST 800-171, and contract-specific marking requirements. The Governance Layer captures chain of custody for every agent-generated artifact, model version recorded, prompt-and-response archived for the contract retention window. Section 508 conformance evidence is retained alongside the artifact-of-record.

### PRS caps by classification

- **Classified content authoring caps at PRS-2.** No agent autonomy on classified material. Classified content authoring is human-led with agent assistance only.
- **CUI training development can reach PRS-3 with approved infrastructure.** Government-tenant generative AI tools only — environments cleared for the relevant data classification. PRS-3 is *not* available on commercial-tenant frontier models for CUI work.
- **Public-trust and unclassified high-volume work can reach PRS-4.** Annual compliance refreshers, role-based onboarding pathways, performance-support adaptive remediation in bounded domains.

AAFL prescribes the cap by classification, not by capability. This is the framework's distinctive federal claim.

### Accreditation alignment

The eight gates map cleanly to accreditation expectations:

- **ACE evaluator expectations.** Gate 2 (Performance Outcome) and Gate 6 (Assessment Validity) directly address ACE's competency-based evaluation criteria.
- **Quality Matters Standards.** Gate 2 addresses QM Standard 2 (Learning Objectives); Gate 6 addresses QM Standard 3 (Assessment); Gate 5 addresses QM Standard 8 (Accessibility).
- **WCAG 2.1 AA + Section 508.** Gate 5 (Equity & Accessibility) is the conformance gate; Section 508 evidence is part of the Release Gate (Gate 7) artifact-of-record.
- **UDL fit.** Checked at Gate 3 (Pedagogical Strategy); validated at Gate 5.

The framework's documentation artifact-of-record is *designed* to drop into an ACE submission packet or a Quality Matters self-review evidence package.

### The federal-applicability claim

Among the published AI-era ID frameworks reviewed in this work — ADDIE, FRAME™, Anthropic 4Ds, Chai et al., EduPlanner, AUSS, and the HPT performance-orientation lineage (see Appendix B for the comparative scan) — AAFL appears to be the only framework that prescribes PRS caps tied to data classification. This is the question federal contracting officers ask first when evaluating AI integration proposals. FRAME™, the 4Ds, and Chai et al. are all classification-agnostic. AAFL's classification-aware caps are not a restriction; they are the source of its federal credibility.

---

## §11. Risks and Pitfalls

Five real risks, named so they can be defended.

### Risk 1 — PRS drift

Organizations read the model as a ladder and push past their appropriate level.

*Mitigation.* Explicit "realistic ceiling" language in §6; case studies of PRS-2 and PRS-3 wins, not just PRS-4; the "default to one level lower than the question would suggest" rule.

### Risk 2 — Eval theatre

Teams adopt the eval framework as documentation rather than as a constraint on the agent loop.

*Mitigation.* The Evaluation-as-Spec Layer is *blocking* — agents cannot run Design or Develop until the eval rubric is signed at Gate 2. The discipline is structural, not aspirational.

### Risk 3 — Gate fatigue

Eight gates feel like eight bottlenecks; teams collapse them to ship faster, defeating the purpose.

*Mitigation.* The PRS permits gate-flagging at PRS-3 — only flagged outputs trigger review. The four pedagogical gates are non-negotiable; the four production gates are sampleable at higher PRS levels. The framework is *designed to scale review intensity with the PRS level in operation*.

### Risk 4 — The autonomy-responsibility problem

Recommending PRS-4 in any context is a public claim about when humans can step back. If the recommendation is wrong, the consequences fall on learners.

*Mitigation.* PRS-4 is bounded by classification cap (§10) and by domain risk; AAFL never claims PRS-4 fits credentialing, classified, or high-consequence performance contexts. The framework is *opinionated about its own limits*. Publishing what AAFL won't do is the source of the framework's credibility, not its limitation.

### Risk 5 — Translator-not-evangelist voice risk

A framework launch reads as evangelism by default. The temptation is to lead with productivity numbers and capability claims.

*Mitigation.* Lead with the gates and the caps, not with the productivity numbers. Publish what AAFL *won't* do, in writing, before publishing what it does.

### IP and authorship

AAFL is independent IP authored by Ruchir Bakshi. The framework is offered to the field for citation, critique, and operational use. Suggested citation: *Bakshi, R. (2026). AAFL: An Agent-Augmented Framework for Learning (v1.2). instructionalai.org.* © Ruchir Bakshi 2026, all rights reserved. Engagement with the framework on cited claims is welcome and expected; the engagement principle is *cite, don't pitch*.

---

## §12. Limitations and Future Work

A framework that publishes its own caps owes the reader an account of its own limits. AAFL is a publishing-ready spec, not a validated artifact, and the gap between the two should be visible to anyone deciding whether to adopt it.

### Limitations

- **Not yet operated end-to-end at PRS-3+.** The framework's PRS-1 and PRS-2 prescriptions are grounded in the author's federal practitioner observations across ACE-accredited programs (see §1.5 Method). The PRS-3 productivity band reported in §6 is *projected, not measured*; no published field test of AAFL at PRS-3 or PRS-4 exists at this writing.

- **Single-author synthesis without external review panel.** AAFL was developed by one practitioner-researcher (see §1.5). The framework has not been subjected to Delphi consensus with an independent expert panel, independent peer review of the integrated framework (individual sources are peer-reviewed; the integration is not), or formal user research with a representative practitioner sample. This whitepaper is offered to the field with the explicit invitation that external review and field testing become the next stage of development.

- **Federal proof-of-application reported as practitioner observation, not citable artifact.** The author's federal ID practice produced the operational observations on first-draft cycle compression reported in §1 and the PRS-1 / PRS-2 productivity bands reported in §6. The underlying internal deliverables are not citable in public-facing AAFL artifacts. A reader who wishes to audit those observations independently does not have a published artifact to consult.

- **PRS productivity bands are practitioner-level observations, not controlled-study results.** The numerical ranges reported in §6 are anchored to published generative-AI productivity studies (Brynjolfsson et al., 2023; Dell'Acqua et al., 2023) where the empirical literature supports the anchor, and labeled as practitioner observation where the author's federal experience is the source. No row in §6 should be read as the output of a controlled experiment on AAFL itself.

- **Scope explicitly excludes K-12 and adult-non-workplace learning.** AAFL is designed for workplace performance contexts (federal training, corporate L&D, higher-ed-to-workplace pipelines). The gate taxonomy and the construct-validity dimension are transferable to K-12, but the PRS-caps-by-classification framing does not map cleanly to FERPA / COPPA regulatory regimes. K-12-specific application is outside the framework's claim space.

- **The pedagogical-vs-production split is a *theoretical commitment*.** The §5 task assignments — which rows sit in the agent column and which in the human-only column — are versioned. The commitment is to the discipline of asking *which decisions belong to humans regardless of capability*, not to a permanent row assignment. Field experience may require updates; see §11 Risk 4 and §5 "When the line moves."

### Future work

- **Field tests at PRS-3 on bounded scopes.** Two natural targets: one credentialing program (where PRS-2 is the appropriate cap and gate-discipline can be measured) and one CUI training program on approved federal-tenant infrastructure (where PRS-3 becomes available and gate-flagging behavior can be characterized).

- **External expert review panel.** A bounded Delphi or modified-Delphi exercise with five to ten federal ID and AI-in-education practitioners would test the framework's specifics against multiple independent expert perspectives, and surface row-level disagreements with the pedagogical-vs-production split that the single-author synthesis cannot.

- **Comparative practitioner study against FRAME-using practitioners.** AAFL maps decision authority; FRAME™ maps capability risk. A comparative study of practitioners using both, one, or neither would test the operational complementarity claim made in §9.

- **Open-source the eval rubric template and gate-checklist as living artifacts.** The companion tactical assets — the HITL Decision-Gate Practitioner Checklist and the AAFL Eval Rubric Template — are presently bundled with the framework spec. Releasing them as separately versioned artifacts under the same © Ruchir Bakshi 2026 attribution would let the field test, fork, and feed back into them without waiting for a v1.3 framework release.

- **K-12-specific application paper.** The gate taxonomy and construct-validity dimension are transferable; the PRS-caps-by-classification framing is not. A separate paper extending AAFL to K-12 — re-anchored in FERPA/COPPA rather than FedRAMP/NIST 800-171 — would address the audience explicitly excluded here without compromising the workplace-performance commitment of the present framework.

The framework's structure is designed to tolerate row-level updates, comparative validation, and federation with adjacent published frameworks without architectural rewrites. The published spec is the starting point; field experience is the next contributor.

---

## §13. Frequently Asked Questions

**Q: How is AAFL different from Hardman's FRAME™?**

FRAME maps capability risk (which AI to trust for which task). AAFL maps decision authority (which task humans must keep regardless of which AI). The frameworks are complementary. FRAME is upstream of AAFL — once you've used FRAME to determine which agent-task allocation is technically defensible, AAFL determines which human gates apply regardless.

**Q: Does AAFL replace ADDIE?**

No. AAFL preserves ADDIE's five-phase spine and adds three cross-cutting layers, an inner Translator's Loop, and the eight HITL gates. ADDIE Guide remains the reference (the dictionary); AAFL is the operating manual (how to use the dictionary in the agent era). The framework is continuity-with-evolution, not replacement.

**Q: What is the framework's organizing outcome, and why is it not learning attainment?**

Workplace performance — measured as time-to-competency, error rate, throughput, transfer-to-job, and retention. This is Kirkpatrick L3/L4 territory rather than L1, and it places AAFL inside the performance-oriented tradition of L&D rather than the course-completion tradition. The agent era makes the choice of organizing outcome consequential because agents optimize whatever they are told to optimize: a rubric measuring completion produces courses optimized for completion; a rubric measuring transfer produces courses oriented toward transfer.

**Q: Is AAFL appropriate for K-12 education?**

The framework is designed for workplace performance contexts (federal training, corporate L&D, higher-ed-to-workplace pipelines). K-12 has different stakeholder structures, different consequence spaces, and different regulatory regimes (FERPA, COPPA). The gate taxonomy and the eval framework's construct-validity dimension are transferable, but the PRS-caps-by-classification framing does not map cleanly. K-12-specific application would require its own work.

**Q: Does AAFL require any specific tooling or platform?**

No. The framework is platform-agnostic. The Orchestration Layer can be operated manually, with workflow tools, or with multi-agent harnesses. The Evaluation-as-Spec Layer requires a documented rubric — the format is up to the implementer. The Governance Layer requires audit trail capability that organizations operating under federal accreditation already have.

**Q: What's the path for an organization currently at PRS-1 (Assistant)?**

Audit your governance discipline first (can you reliably operate the audit trail at PRS-1? Are gate decisions logged?). Then identify a pilot scope at PRS-2 (one course, one item bank, one storyboard pipeline). Build out the Evaluation-as-Spec discipline before lifting to a higher PRS level (rubric authored at Gate 2 on the pilot scope before any agent runs). Move to PRS-3 only after PRS-2 has been operational across multiple deliverables and the gate-flagging discipline is reliable.

**Q: What are the failure modes of trying to operate AAFL at the wrong PRS level?**

Operating below your appropriate level wastes agent capacity (you're paying for human review that a higher PRS level would automate). Operating above your appropriate level fails the audit trail (you can't produce the documentation an accreditation review demands). Both failure modes are real; the second is more dangerous because it's harder to detect until something goes wrong.

**Q: How is AAFL related to the Anthropic AI Fluency framework (4Ds)?**

The 4Ds (Delegation, Description, Discernment, Diligence) are practitioner *competencies*. AAFL is the *process* those competencies operate within. Discernment lives at every HITL gate; Delegation defines the agent-vs-human task split; Description is how you brief an agent at any gate; Diligence is the audit trail the Governance Layer records. The frameworks are layered, not competing. Practitioners trained in AI Fluency operate AAFL natively.

---

## §14. Bibliography

Allen, M. W. (2012). *Leaving ADDIE for SAM: An agile model for developing the best learning experiences*. ASTD Press.

Anthropic Engineering. (2025). *Demystifying evals for AI agents*. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

Anthropic Research. (2025). *Building effective AI agents*. https://www.anthropic.com/research/building-effective-agents

AUSS research team. (2025). *Agentic Unified Student System: A four-module agent architecture across student, educator, and institutional levels*. arXiv. https://arxiv.org/html/2604.16566v1

Branson, R. K., Rayner, G. T., Cox, J. L., Furman, J. P., King, F. J., & Hannum, W. H. (1975). *Interservice procedures for instructional systems development* (Vols. 1–5). Florida State University. (ADDIE origin.)

Brinkerhoff, R. O. (2003). *The success case method: Find out quickly what's working and what's not*. Berrett-Koehler.

Brynjolfsson, E., Li, D., & Raymond, L. (2023). Navigating the jagged technological frontier. *Organization Science*. https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838

CAST. (2018). *Universal Design for Learning Guidelines version 2.2*. https://udlguidelines.cast.org/

Chai, D. S., Kim, H. S., et al. (2025). Generative artificial intelligence in instructional system design. *Performance Improvement Quarterly*. https://journals.sagepub.com/doi/10.1177/15344843251320256

Clark, D. (2025). *Learning experience design*. Reviewed in Worklearning. https://www.worklearning.com/2025/05/27/book-learning-experience-design-by-donald-clark/

Dakan, R. & Feller, J. (2023–2025). *AI Fluency Framework for Educators*. Anthropic Academy. https://aifluencyframework.org/

Davenport, T. H. & Daugherty, P. R. (2018, updated 2024). *Human + Machine: Reimagining work in the age of AI*. Harvard Business Review Press.

Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*. Harvard Business School Working Paper 24-013. https://www.hbs.edu/faculty/Pages/item.aspx?num=64700

Dick, W., Carey, L., & Carey, J. O. (2014). *The systematic design of instruction* (8th ed.). Pearson. (Original 1978.)

EduPlanner research team. (2025). EduPlanner: A multi-agent system for instructional design optimization. arXiv. https://arxiv.org/html/2504.05370v1

Gagné, R. M. (1985). *The conditions of learning* (4th ed.). Holt, Rinehart and Winston. (Original 1965.)

Gilbert, T. F. (1978). *Human competence: Engineering worthy performance*. McGraw-Hill. (Tribute edition, ISPI/Pfeiffer 2007.)

Hardman, P. (2025a). *Defining and navigating the jagged frontier in instructional design*. Substack. https://drphilippahardman.substack.com/p/defining-and-navigating-the-jagged

Hardman, P. (2025b). *AI in instructional design: 2025 reflections*. Substack. https://drphilippahardman.substack.com/p/ai-in-instructional-design-reflections

Holmes, W., Bialik, M., & Fadel, C. (2019). *Artificial intelligence in education: Promises and implications for teaching and learning*. Center for Curriculum Redesign.

Kirkpatrick, D. L. & Kirkpatrick, J. D. (2016). *Kirkpatrick's four levels of training evaluation*. ATD Press. (Original 1959.)

Mager, R. F. (1962). *Preparing instructional objectives*. Fearon. (Third edition, 1997, Center for Effective Performance.)

McKenney, S. & Reeves, T. C. (2018). *Conducting educational design research* (2nd ed.). Routledge.

Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development*, 50(3), 43–59. https://doi.org/10.1007/BF02505024

Meyer, A., Rose, D. H., & Gordon, D. (2014). *Universal Design for Learning: Theory and practice*. CAST Professional Publishing.

Moore, C. (2017, updated). *Map It: The hands-on guide to strategic training design*. Montesa Press. https://blog.cathy-moore.com/action-mapping/

Mosher, B. & Gottfredson, C. (2011). *Innovative performance support: Strategies and practices for learning in the workflow*. McGraw-Hill.

Quality Matters. (2023). *QM higher education rubric* (7th ed.). MarylandOnline. https://www.qualitymatters.org/

Reigeluth, C. M. (Ed.). (1999). *Instructional-design theories and models, Volume II: A new paradigm of instructional theory*. Lawrence Erlbaum Associates. (Volume III, with A. A. Carr-Chellman, 2009; Volume IV, with B. J. Beatty & R. D. Myers, 2017, Routledge.)

Rossett, A. & Schafer, L. (2007). *Job aids and performance support: Moving from knowledge in the classroom to knowledge everywhere*. Pfeiffer.

Rummler, G. A. & Brache, A. P. (1990). *Improving performance: How to manage the white space on the organization chart*. Jossey-Bass. (Third edition, 2013.)

Saghafian, S., Bauer-Wolf, S., & Donohue, K. (2024). Effective generative AI: The human-algorithm centaur. *Harvard Data Science Review*. https://hdsr.mitpress.mit.edu/pub/3rvlzjtw

Selwyn, N. (2019). *Should robots replace teachers? AI and the future of education*. Polity Press.

Web Content Accessibility Guidelines (WCAG) 2.1. (2018, updated). *W3C Recommendation*. World Wide Web Consortium. https://www.w3.org/TR/WCAG21/

Williamson, B. (2017). *Big data in education: The digital future of learning, policy and practice*. SAGE Publications.

---

## About the Author

**Ruchir Bakshi** is a federal instructional design consultant. He has applied his AI-Enhanced ADDIE methodology across ACE-accredited graduate certificate and post-baccalaureate programs at the Center for Development of Security Excellence, and authored the AI Prompt Library for Instructional Systems Designers. He runs the [instructionalai.org](https://instructionalai.org) ecosystem of practitioner-first resources.

AAFL is independent IP. © Ruchir Bakshi 2026, all rights reserved. Suggested citation: *Bakshi, R. (2026). AAFL: An Agent-Augmented Framework for Learning (v1.2). instructionalai.org.*

---

## Appendix A. Acronym Glossary

A consolidated reference for the acronyms used in this paper. Every acronym below is also spelled out at first body-text appearance where space permits.

| Acronym | Expansion |
|---|---|
| **AAFL** | Agent-Augmented Framework for Learning |
| **ACE** | American Council on Education |
| **ADDIE** | Analyze · Design · Develop · Implement · Evaluate (the canonical five-phase instructional design model) |
| **AR** | Augmented Reality |
| **AUSS** | Agentic Unified Student System |
| **CAST** | Center for Applied Special Technology (publisher of the UDL Guidelines) |
| **cmi5** | Computer-Managed Instruction profile of xAPI |
| **CUI** | Controlled Unclassified Information |
| **DDVR** | Draft · Discern · Validate · Release — the four steps of the Translator's Loop, run by the human practitioner against every agent-produced artifact within each ADDIE phase |
| **DL** | Design Loop (taxonomy tag: tasks that compress ID cycle time) |
| **DoD** | Department of Defense |
| **EAR** | Export Administration Regulations |
| **EdArXiv** | Open-access preprint repository for education research |
| **FedRAMP** | Federal Risk and Authorization Management Program |
| **FERPA** | Family Educational Rights and Privacy Act |
| **FRAME™** | Framework for Responsible AI in Mapping the (Jagged) Frontier (Hardman) |
| **HITL** | Human-in-the-Loop |
| **HPT** | Human Performance Technology |
| **ID** | Instructional Design / Instructional Designer |
| **ISD** | Instructional Systems Design |
| **ISPI** | International Society for Performance Improvement |
| **ITAR** | International Traffic in Arms Regulations |
| **JKO** | Joint Knowledge Online (DoD learning platform) |
| **L1–L4** | Kirkpatrick's four levels of training evaluation (Reaction · Learning · Behavior · Results) |
| **L&D** | Learning and Development |
| **LMS** | Learning Management System |
| **NICE** | National Initiative for Cybersecurity Education (NIST framework) |
| **NIST** | National Institute of Standards and Technology |
| **OPM** | Office of Personnel Management |
| **PL** | Performance Loop (taxonomy tag: tasks that compress time-to-competency or improve transfer-to-job) |
| **PRS** | Proportional Restraint Scale — AAFL's four-level autonomy scale (PRS-1 Sandbox · PRS-2 Co-designer · PRS-3 Production Partner · PRS-4 Performance System) |
| **QM** | Quality Matters |
| **SAM** | Successive Approximation Model (Allen Interactions) |
| **SCORM** | Sharable Content Object Reference Model |
| **SME** | Subject Matter Expert |
| **UDL** | Universal Design for Learning |
| **WCAG** | Web Content Accessibility Guidelines (W3C) |
| **xAPI** | Experience API (formerly Tin Can API) |

*Note.* "Section 508" is a section of the U.S. Rehabilitation Act, not an acronym; it is preserved as-written throughout the paper. The taxonomy column-tag prefixes **(PRS-3+)** and **(PRS-4)** in §5 are PRS-gate prefixes, not acronyms; see §5 (Reading the PRS prefixes).

---

## Appendix B. Comparison of Published AI-Era ID Frameworks

This appendix substantiates the federal-differentiation claim made in §8 and §10 by tabulating the architectural features of the published AI-era instructional design frameworks reviewed in this work, plus the most-cited established models AAFL inherits from. The scan is not exhaustive; it is the working set against which AAFL positions itself, and it should be expanded as additional frameworks are published or surfaced.

The columns are deliberately narrow architectural questions, not value judgments. *HITL gates?* asks whether the framework specifies named decision points where human judgment is irreducible. *Progression model?* asks whether it prescribes levels with stopping points. *Classification caps?* asks whether progression is tied to data-classification context (the federal-applicability question). *Eval discipline* names the framework's stated approach to assessing the work agents produce. *Primary contribution* names what the framework adds to the field.

| Framework | Author / Year | Organizing outcome | HITL gates? | Progression model? | Classification caps? | Eval discipline | Primary contribution |
|---|---|---|---|---|---|---|---|
| **AAFL** | Bakshi (2026) | Workplace performance (Kirkpatrick L3/L4) | **Yes — 8 named gates with pedagogical/production split** | **Yes — PRS-1 → PRS-4 with prescribed caps** | **Yes — by data classification (the framework's distinctive federal claim)** | Eval-as-spec; blocking rubric authored at Gate 2 before Design or Develop runs | Integration of all four: gates + PRS + caps + eval-as-spec |
| **ADDIE** | Branson et al. (1975) | Learning attainment (implicit) | No — phases, not decision gates | No | No | End-of-phase evaluation (Phase E) | The five-phase ID spine that the field still reads in |
| **FRAME™** | Hardman (2025a) | Capability-risk management | No — risk zones, not decision gates | No | No | Task-specific quality-zone checks | Maps capability risk across the jagged frontier |
| **Anthropic 4Ds** | Dakan & Feller (2023–2025) | Practitioner AI fluency | No — competencies, not gates | No | No | Diligence-as-audit (one of the four competencies) | Educator-facing AI fluency competencies |
| **Chai et al.** | Chai et al. (2025) | Phase-by-phase AI integration | No | No | No | Not framework-prescribed | Peer-reviewed academic anchor for AI-in-ID |
| **EduPlanner** | EduPlanner research team (2025) | Iterative ID optimization | No — three-agent harness, not human gates | No | No | Evaluator agent inside the three-agent loop | Multi-agent academic system for ID drafting |
| **AUSS** | AUSS research team (2025) | Personalization at student / educator / institutional levels | No — four-module agents, not human gates | No | No | Per-module evaluation inside the agent architecture | Four-module agent architecture across levels |
| **Action Mapping** | Moore (2017) | Business performance (backward design) | Implicit — backward-design checkpoints | No | No | Performance observation against business goal | Backward-from-business-goal design discipline |
| **5 Moments of Need** | Mosher & Gottfredson (2011) | Workflow learning + performance support | No — moments, not decision gates | No | No | Workflow observation across the five moments | Workflow learning continuum from formal to performance support |
| **Success Case Method** | Brinkerhoff (2003) | Did the intervention move performance? | No — case-finding method, not gates | No | No | Targeted case interviews + impact attribution | Method for tracing whether the intervention actually moved performance |

### Reading the scan

**The integration is the contribution.** No single row above is unique to AAFL except the classification-caps column. The eight gates, the four-level PRS, the eval-as-spec discipline, the workplace-performance organizing outcome — each individually has precedent or near-precedent in the cited works. What AAFL claims is the *integration*: a framework that simultaneously specifies (a) HITL decision gates with pedagogical/production classification, (b) a four-level scale with prescribed caps, (c) caps that are *tied to data classification* rather than to capability or context-in-general, (d) an eval discipline that *blocks* the Develop phase until the rubric is signed, and (e) a governance layer that enforces all of the above. The scan shows no other reviewed framework occupies all five positions.

**The federal-caps column is where AAFL is structurally distinct.** FRAME™, the 4Ds, and Chai et al. are all classification-agnostic frameworks. They could be operated in any context — commercial, federal, K-12, civilian or military — without changing their prescriptions. AAFL is the only reviewed framework whose architecture changes prescriptions based on the data-classification context of the work: classified content authoring caps at PRS-2; CUI training development can reach PRS-3 with approved infrastructure; public-trust unclassified high-volume work can reach PRS-4. This is the question federal contracting officers ask first, and AAFL's caps-by-classification framing is the framework's answer.

**Scope limits.** This scan covers published AI-era ID frameworks at the time of drafting (mid-2026). It does not exhaust the corporate-LMS-vendor space (Articulate, Synthesia, Vyond, etc., are tools — not frameworks — and live in the §1 capability claim, not here). It does not cover the broader AI-in-education academic literature beyond the AI-in-ID corner (Selwyn, Williamson, Holmes-Bialik-Fadel are engaged in §9 as critic-camp voices, not as competing frameworks). Additional frameworks should be added as they are surfaced; the comparative-scan structure is versioned with the framework.

---

*Whitepaper v1.2 · 2026-05-14 · © Ruchir Bakshi 2026 · all rights reserved · suggested citation: Bakshi, R. (2026). AAFL: An Agent-Augmented Framework for Learning (v1.2). instructionalai.org.*
