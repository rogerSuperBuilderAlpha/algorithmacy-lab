# Stage 1 review: "Beyond the Dyadic Straitjacket" against the *Organization Science* call

Reviewed 27 October 2026 against the CFP PDF (`CFP_AI-Enabled Frontiers in Organizational Science`,
7 pages) and the live Google Doc `1fhM_C7pz6e3sR7aXY3_89oys06B-UyK9Vyf93bt1zFA` as it stood at
11:41 UTC that day (8,852 words; Part I 1,890). The export in this folder,
[`gdoc_1fhM_v6_story_plus_addendum.md`](gdoc_1fhM_v6_story_plus_addendum.md), is 130 words shorter and
has different A.2–A.5 and appendix headings, so the Doc, not the export, is the text reviewed.

**What I read in full:** the Doc, the CFP, the prototype's `README.md` and `APPENDIX.md`, the FINDINGS
files of every lab study the Doc cites, Quine (1954), both Hereth Correia & Pöschel papers (2004 from
the copy in `~/Downloads`, 2006 all 23 pages), Koshkin's primitive-positive paper (arXiv 2606.19492v1,
19 pages), the dyad and triad pages of Wolff's Simmel (archive.org scan), the abstracts of every source
the attribution audit names. **What I did not read:** the published *IGPL* version of Koshkin's
paper (theorem numbers are verified against the arXiv version only) and Koshkin's 2024 *IGPL* paper
beyond its abstract. Consensus was out of monthly quota and Scholar Gateway returned ACCESS_DENIED,
so Crossref, OpenAlex, Semantic Scholar and the publishers' pages stood in for them.

**Every number in Part C comes from a fresh run**, not from a FINDINGS file: the prototype's
`reproduce.py` (17/17) and `pytest` (19 passed), `irreducibility.analyze` on all four examples and on
the logged adversary run, `studies.enricher_regime`, `studies.mediator_in_core`, `studies.census`,
`encode_check` on the three AI files, and the eighteen lab CI checks the Doc leans on (17 pass; one
fails, see C7). Outputs sit in
`/private/tmp/claude-501/-Users-ludwitt/99b8f63e-f3ca-4c8c-ab30-c300eeb75236/scratchpad/evidence/`
(`proto_*.txt`, `lab_ci_named.txt`, `crossref/*.json`).

**How to use this file.** Each finding states the Doc's text, the fact, the source, and a replacement
sentence where one is needed. Replacement text is marked `[DRAFTED by Claude]`; the wording around it
stays yours. Nothing here has been applied to the Doc.

---

## 0. The verdict, and the items that block submission

The package fits the call better than its v3 draft feared, and its spine is sound: large language
models fail as structural judges, so the loop confines them to evidence-bound reading under a
deterministic gate and lets exact computation decide, and the logged runs show the model's own
predictions failing. That is an "AI-enabled research loop under human direction" with a built-in
boundary test, which is two of the CFP's categories at once. The prose is strong. The addendum is
not yet true to the prototype it describes.

Eleven items block submission because a reviewer who forks the repository will find them within an
hour:

1. **The prototype is not forkable.** `irreducibility-pipeline` (tag `v0.1-stage1`) existed only on your
   disk with no git remote. It now sits inside the lab at `irreducibility-pipeline/` (see C6); the Doc's
   references to it as a separate artifact need the new path and the lab tag.
2. **"56 dyadic, 132 cycle-supported, 68 mediated triads" and "96 of 256"** (§4, A.3, Appendix C) have no
   source in either repository. The only 256-form census is the prototype's `census`: 24 triadic, 232
   dyadic. (C3.)
3. **Table 3's outside-option rows O₂–O₅ are not the prototype's O1–O5**, and their verdicts contradict the
   study they resemble: both parties mobile gives BYPASSED {D,R}, not "Φ = 0, complete dissolution". (C2.)
4. **Example 03 (code-review gate)** in Table 5 reports parties, rules and results the prototype does not
   produce. Actual: `gated` is triadic at Φ = 1.000 with core {A, M} and the gate BYPASSED. (C2.)
5. **Example 04 (dealer vs clearinghouse)** is not dyadic-vs-triadic; both are triadic at Φ = 2.000 and the
   distinction is contingent vs intrinsic. (C2.)
6. **Example 02's parties and encoding counts** are wrong (engine `E`, not "Intake Portal (M)"; five design
   encodings, not "2 rival + 4 underspecified"). (C2.)
7. **Φ(MIP) = 1.198 and 1.000** in Table 3 and Table 4 are wrong: the direct-tie bypass computes to 0.830;
   the pooled-driver system computes to 0.000 (dyadic) with {P, R} as its major complex. (C2.)
8. **Six file paths do not exist** (`encode/runs/`, the three `*_drafter.json` / `*_adversary.json` names,
   `irreducibility/controls.py`, `studies/strategic_model/`), and two more are modules, not directories.
   (C1.)
9. **Two reference-list entries are fabricated records**: Cameron (2024) carries an invented title, issue and
   pages; "Koshkin (2025) … *IJAR* 186, 109523" is a different paper's article number. Three works cited in
   the text are missing from the list (Stark & Pais 2020; Rosenblat & Stark 2016; Tononi 2004). (D.)
10. **Four Appendix D figures have no source** (R² = 0.992; "3 bits → 5.755 bits"; "4/8 formal vs shadow";
    "hybrid team designs factor cleanly"), and twelve study labels in that table are not the names of any
    study or check. (C4.)
11. **"[Anonymized for Double-Blind Stage 1 Review]"** sits above a link to a public repository under your
    name. The CFP asks for no blinding. You decided to name the author; the line needs replacing. (A.)

Everything else is listed in F by priority.

---

## A. CFP compliance

| CFP asks | Where the Doc answers | Gap or fix |
|---|---|---|
| Proposal 1,500–2,000 words plus references, 3–5 pages | Part I §1–5, **1,890 words** (`wc -w` on the export's lines 11–142) | None. |
| "what you have done" | §3–§4; A.2 | None. |
| "what you hope to do" | §4 Stage 2 workstreams; A.3; App. C | None. |
| "the key risks you face in fully executing your vision" | §5 gives four *boundary conditions* of the method. Execution risks appear only in the addendum: IRB timing (A.3 item 3), open-weight model performance (A.3 item 1), coder agreement target (prototype APPENDIX H: Krippendorff's α ≥ 0.80, absent from the Doc) | Add one sentence to §5 naming the execution risks: `[DRAFTED by Claude]` "Three risks govern Stage 2: the field protocol waits on IRB approval; the encoding step must hold up on open-weight models, not only on the commercial one we logged; and AI–human coder agreement (target Krippendorff's α ≥ 0.80 per rule) is not yet measured." |
| "how organizational and social science would change if you are successful" | §5 closing paragraph; A.5 | None. |
| Technical appendix "details needed to evaluate and understand the work" | Part II + Appendices A–D | Fix the factual items in C; add table captions (the text cites Tables 1–6, the tables carry none). |
| Research artifact: "a Git repository or equivalent artifact that includes a prototype or proof of concept" | Links `algorithmacy-lab`; names `irreducibility-pipeline v0.1-stage1` | The prototype had no remote. Now in the lab tree (C6). Replace "fork our repository" references with the single lab URL and the lab tag. |
| Contribution types | Title block: "Submission Tracks: Reusable Research Infrastructure; AI-Enabled Research Loops Under Human Direction; New Forms of Measurement; Critical, Diagnostic, and Boundary-Setting Work" | The CFP lists "contribution types", not tracks, and does not ask you to pick. Four is defensible; "New Forms of Measurement" is the weakest fit (the CFP's wording is "measure constructs in text, audio, or video … at scale", and nothing here measures at scale yet). Suggest naming two: research loops under human direction, and boundary-setting. |
| Criterion: novelty | §2 | Strong. See E for the one overclaim ("overturns a sixty-year assumption"). |
| Criterion: feasibility | §4, A.3 | Strong once the addendum matches the code. |
| Criterion: stage of development | A.2 (17 checks, 19 tests, 542 lab checks) | Strong; numbers verified (C5). |
| Criterion: ethicality | A.4 item 5 only; Part I is silent | One clause in §5 (IRB, rule architectures not individuals, symmetric lever matrix). |
| Criterion: reproducibility | `reproduce.py`, `ci/reproduce.json` | Strong. One lab check does not reproduce today (C7). |
| Criterion: scalability | §5 "three to ten roles"; A.4 "n = 10 … bound to 3–5" | Honest. Keep. |
| Criterion: potential use and adoption | §3 "any researcher can fork" | True only after C6. |
| Criterion: expand the frontier | §2, A.5 | Strong. |
| FAQ: proprietary AI models — "infrastructure that other researchers have a reasonable chance of accessing" | A.3 item 1 commits to open-weight endpoints; the logged runs used Claude Sonnet 5.5 | Say in Part I §3 that the prompts are model-agnostic and the Stage 2 release runs on an open-weight model as well. |
| FAQ: data that cannot be shared | Examples are stipulated prose (prototype README: "a stipulated description, not field data"); field data waits on IRB | State it in Part I once: the worked cases are stipulated, the field packet is pre-built. |
| FAQ: negative results welcome | The two failed adversary predictions (A.2.2), the MARL null (A.4), the proxy failure (A.2.2) | These are assets under this call. §4 could name them as such in one clause. |
| Double-blind | Title block "[Anonymized for Double-Blind Stage 1 Review]" | Not required by the CFP; contradicts the public named repo. Replace with the author line. |
| Dates | §4: "before the February 2027 Duke workshop"; folder README: "Duke on 19–20 February 2027" | The CFP says **27–28 February 2027, tentative**, and names no venue. Fix both. |
| Portal | — | `mc.manuscriptcentral.com/orgsci`, deadline 1 November 2026. |

---

## B. The narrative

**What the editors asked.** "What kinds of knowledge can we create when the tools of inquiry
themselves change?" — and, in the same breath, no "Potemkin villages of slop", no conventional papers
with AI content, prototypes over polish. Part I answers the question in §3, and §3 is the best section
in the package: the LLM fails as a judge of structure, so the harness uses it only as an evidence-bound
reader and lets PyPhi decide, and the logged adversary run shows the model finding two readings and
mispredicting both. Keep that paragraph exactly as it is. It is the contribution.

**Three moves weaken the case, and each is fixable without new research.**

*The four-regime claim rests on numbers that do not exist.* §2 says that running PyPhi "across all 256
possible three-party mediated coordination structures proves that joint influence and systemic
wholeness are orthogonal dimensions, revealing four distinct coordination regimes." The 2 × 2 is real,
but it comes from the Peirce probes (89 one-input wirings; 30 two-input forms), and the "256" census says
something else (24 triadic, 232 dyadic). The reviewer who runs `studies.census` will see the mismatch
first. C3 gives the sourced sentence.

*"Self-exemplifying" is asserted, not computed.* §3 says the research architecture "quite literally
demonstrates the exact triadic coordination we are examining." Nothing in either repository encodes
scholar, agents and PyPhi as a structure and computes it. Two fixes. The cheap one is to drop
"literally" and say the harness is built on the same commit-and-read form the paper studies. The
better one — an hour's work with the prototype — is to write the three-party encoding (the scholar
reads the harness's verdict; the agents read the scholar's question and the evidence; the harness
commits only on a gated encoding and a question) and report its Φ(MIP) and core in one sentence. Under
this call, the harness run on itself is exactly the kind of result the editors say they cannot
predict. `[DRAFTED by Claude]` placeholder if you compute it: "Encoded as a structure in its own
pipeline — the scholar, the drafting agents, and the gate-and-compute harness — the loop reads
[verdict] with core [core]; the computation is `examples/05_harness/` in the prototype."

*Agents are promised as present.* §3 says a forking researcher can "have their AI agents run the
experimental workflow" and that "competing AI agents translate field evidence." The prototype's README
says: "Nothing yet reads interview transcripts or documents at scale." The lab's AI arc says its agents
are "in-silico Boolean / tabular / small neural proxies (not live LLM calls)". What exists is two
prompts, a gate, and three logged runs made by pasting prose into one model. State that size. The
call rewards an honest prototype over an imagined platform, and the v3 FLAGS file already warned
against claiming live agent probes. `[DRAFTED by Claude]` for §3: "Any researcher can fork the lab,
paste a case into the drafter and adversary prompts with any model, pass the result through the
evidence gate, and compute. Three runs are logged so far, all on one model; reading transcripts at
scale and measuring agreement with human coders is Stage 2."

**Two judgment calls, flagged, not decided.**

*Algorithmacy.* §1, §2 and §5 carry the literacy → algorithmacy frame. The v3 FLAGS file judged that
"a paper about algorithmacy does not fit" this call. I would not cut it — it is the dissertation
spine and it gives the paper its organizational stake — but it costs about 180 of Part I's 1,890
words, and the CFP never asks for a construct. One sentence in §1 and the closing clause of §5 would
hold the frame; §2's "requiring only literacy" / "Navigating it requires algorithmacy" glosses on the
four regimes could go.

*"Potemkin village."* The phrase is the editors' own (for AI loops that only look like research).
Using it twice for your own objects — the bypassed platform in §3, "Potemkin oversight" in A.5 — reads
as an echo. One use, or none.

**Overclaims to soften** (each is one word): "proves" appears six times (§2 ×2, §3, §4, A.1, A.2.3)
for results that are computations on stipulated models; the prototype's own README says "a verdict on
a model is evidence about the model." "Overturns a sixty-year assumption" (§2) — see E3. "Every
nontrivial variation backward" (§3) — the evidence is two predictions on one case (E8). "Collapses a
decade-long debate" (§4) — into a testable rule, yes; "collapses" overstates. "Pre-registered" (A.2.1
Step 2, A.4 opening, A.4 item 2) — no registry record exists; the lab's own phrase, in every FINDINGS
file, is "hypotheses fixed before computing", and the prototype's is "a prediction fixed before
anything is computed." Use those.

**House-style flags** (your `CLAUDE.md` rules, applied to Part I only; the addendum is reference
material and reads fine as a list):
- A.4's opening, "Because our laboratory commits pre-registered hypotheses before running experiments
  and keeps refuted predictions in CI, we can state the exact boundary conditions," is self-narrating
  rigor (rule 4). The sentence after it does the work; cut the opener.
- §2, §4 and §5 each run four or five bullets of identical shape (bold label, colon, one sentence).
  The CFP format tolerates it; the house rule (mechanism 8) would group §4's three findings into prose.
- Paragraph openings in §1 land on agents (Simmel, organization theory, scholars) — good. §2's second
  paragraph opens "Neuroscientists confronted the exact puzzle" — good. §5's bullets open on abstract
  nouns ("Interpretive ambiguity:") — acceptable in a list.

---

## C. Repo-reference audit

Status: ✓ verified · ✗ wrong · ~ imprecise · ∅ no source found. Doc locations use the export's line
numbers in `gdoc_live.md` (my capture of the Doc at review time) where it helps.

### C1. Paths, files, functions, tags

| Doc says | Status | Fact | Source |
|---|---|---|---|
| `irreducibility-pipeline`, tag `v0.1-stage1` (A.2, App. B.2, App. D) | ✗→✓ | Existed only at `~/iit-playground/irreducibility-pipeline`, one commit, **no remote**. Now copied into the lab as `irreducibility-pipeline/`; tag to be cut on the lab commit when you push (C6). | `git remote -v` (empty); this branch |
| "reproduces all 17 reference results and passes 19 automated test gates in two minutes via a single command" (A.2) | ~ | Two commands: `python reproduce.py` (17 checks, about 2½ minutes on this laptop; the per-check times sum to 138 s) and `pytest -q` (19 tests, 5 s). | `proto_reproduce.txt`, `proto_pytest.txt` |
| `encode/runs/` (A.2.2 item 1, Table 5) | ✗ | No such directory. Logged runs live beside the examples. | `ls encode` → `PROMPT_adversary.md PROMPT_drafter.md SCHEMA.json` |
| `01_gig_dispatch_drafter.json`, `01_gig_dispatch_adversary.json`, `02_insurance_claim_drafter.json` (Table 5) | ✗ | `examples/01_gig_dispatch/ai_draft.json`, `examples/01_gig_dispatch/ai_draft_plus_adversary.json` (plus `ai_adversary_raw.json`), `examples/02_insurance_claim/ai_draft.json`. | `ls examples/01_gig_dispatch` |
| `irreducibility/controls.py` with "four mandatory controls" (Step 4, Table 2, App. B.1) | ✗ | No `controls.py`. `irreducibility/validate.py` runs **two controls** (factoring Φ = 0.000; irreducible Φ = 0.830) and **five reference forms** (strict mediation 2.000; chat dyad, dyadic gig model, broken-liveness feedback, each 0.000; gig false dyad 2.000). Table 2's four rows are the two controls plus two of the five forms. | `validate.py` docstring; prototype APPENDIX §C |
| `studies/adversarial_coding/`, `studies/proxies/`, `studies/strategic_model/` (A.2.2, App. C, App. D) | ✗ | Modules, not directories: `studies/adversarial_coding.py`; proxies = `studies/proxy_run.py` + `proxy_bridge.py` + `phiid_measure.py`. **`strategic_model` does not exist**; the README says "the strategic model … is the next stage of the work and is not here yet." Appendix D row 1 lists it as part of `v0.1-stage1`. | `ls studies`; README l. 24–26 |
| `irreducibility/core.py`, `encode_check.py`, `validate.py`, `spread.py`, `regime.py`, `contingency.py`, `rules.py`, `analyze.py`; `tpm_from_rules`, `cm_from_rules`, `classify_mediator`, `reduce_mediator`; `pyphi.new_big_phi.sia` / `maximal_complex` | ✓ / ~ | All files exist. `tpm_from_rules` and `cm_from_rules` are in `core.py`. `classify_mediator` and `reduce_mediator` are **not function names**: the mediator's position comes from `regime()` in `regime.py` (with `REGIMES` and `lesion_survives()`), the bypass reduction from `contingency_test()` and `add_bypass()` in `contingency.py`, and the verdict from `classify_rules()` in `core.py`. | `grep -n "^def"` |
| `contingency.py` "sweeps outside-option exit scenarios" (Step 6) | ✗ | `contingency.py` runs the bypass test (intrinsic / contingent / partial / reducible). Outside options are the O1–O5 design encodings in `examples/01` and the battery in `studies/enricher_regime.py`. | prototype APPENDIX §D |
| `protocol/` (Step 1, A.3, App. C) | ✓ | `PROTOCOL.md`, `coding_scheme.md`, `interview_guide.md`, `ethics.md`, `predictions_fixed_in_advance.md`. | `ls protocol` |
| `examples/03_code_review_gate/` (A.3) | ✓ path | Results wrong, see C2. | |
| `org_frontier/field/`, `recurrence/`, `survey/`, `classifier/`, `thinkers/peirce/probe_peirce_joint_determination.py`, `third_party/pyphi_iit4_mv`, `smoke_m2.py`, `foundations/phiid_vs_phi/FINDINGS.md` | ✓ | All exist. | `ls` |
| PyPhi pin `b78d0e342`; upstream `134a8f31`; `iit4_2026` returns φₛ = 0 at ε = 0; Python 3.10–3.12 | ✓ | | `requirements.txt`; `third_party/pyphi_iit4_mv/README.md` l. 7–9 |
| Blind runs "Claude Sonnet 5.5, October 2026" | ✓ | "26 Oct 2026, prompts as committed, case prose only, no tools". | prototype README l. 126 |

### C2. The worked examples and Tables 2, 3, 5

Fresh `python -m irreducibility.analyze examples/<n>/encodings.json` output, in full, is in
`proto_analyze_*.txt`.

**Example 01, gig dispatch.** Rival encodings: A (platform commits) **triadic Φ = 2.000, core {D,P,R},
BOTTLENECK, intrinsic**; B (driver's relay) **dyadic 0.000, {D,P}**; C (pooled drivers, four nodes)
**dyadic 0.000, major complex {P,R}**. Single flipping rule A→B: `P: 'D and R' -> 'D'`. Design
encodings:

| | Rules (D′, P′, R′) | Φ(MIP) max | Core | Position |
|---|---|---|---|---|
| O1 both captive | P · D∧R · P | 2.000 | {D,P,R} | BOTTLENECK |
| O2 complementary direct tie | P∧R · D∧R · P∧D | 6.000 | {D,P,R} | ENRICHER |
| O3 captive driver, mobile rider | P · D∧R · P∨D | 0.415 | {D,P} | CAPTURE |
| O4 mobile driver, captive rider | P∨R · D∧R · P | 0.415 | {P,R} | CAPTURE |
| O5 both mobile (substitute direct tie) | P∨R · D∧R · P∨D | 0.830 | {D,R} | BYPASSED |

Against the Doc:

| Doc (Table 3 / A.2.2) | Status | Fact |
|---|---|---|
| "2 rival (R₁, R₂), 2 design (D₁, D₂), 5 exit (O₁–O₅)" (Table 5) | ✗ | 3 rival (A, B, C) + 5 design (O1–O5) = 8 admissible encodings. Your D₁ is rival C; your D₂ is design O5. |
| R₁ Φ = 2.000 {D,P,R} BOTTLENECK; R₂ Φ = 0.000 CONDUIT | ✓ / ~ | R₂'s position prints as `dyadic` (the regime set is dyadic / BYPASSED / CAPTURE / BOTTLENECK / ENRICHER). "CONDUIT" and "PASSIVE" are your labels, not the code's. Either rename in the text or say the two words gloss the code's `dyadic`. |
| D₁ driver pool "Φ(MIP) = 1.000, {P,R}" | ✗ | System **Φ(MIP) = 0.000 (dyadic)**; {P,R} is the major complex. The 1.000 does not appear anywhere in the output. |
| D₂ direct tie "Φ(MIP) = 1.198, {D,R}, BYPASSED" | ✗ | **Φ(MIP) max = 0.830** (states 100 and 001), core {D,R}, BYPASSED. 1.198 appears nowhere in either repo. |
| O₂ "D′ = P ∨ E(D) … Φ = 2.000, {P,R}, CAPTURE of rider"; O₃ symmetric "{D,P}" | ✗ | These are not the prototype's O2/O3. The nearest computed facts: O4 (mobile driver) → CAPTURE {P,R} at Φ = 0.415; O3 (mobile rider) → CAPTURE {D,P} at 0.415. The exogenous-option battery in `enricher_regime.py` prints the same regimes (W:full/C:none → CAPTURE; W:none/C:full → CAPTURE) and **prints no Φ values**. |
| O₄ "both have outside options … Φ(MIP) = 0.000, ∅, Complete Dissolution (platform loses all lock-in)" | ✗ | Both-mobile is **BYPASSED, core {D,R}** (prototype O5, Φ = 0.830; `enricher_regime` phase diagram W:full/C:full → BYPASSED; its summary line: "bypassed (both options)"). The platform leaves the core; the parties stay bound to each other. "Dissolution to Φ = 0" is the opposite of what the code says. Part I §4 bullet 2 ("workers and clients escape lock-in by building outside options") survives; A.2.2's sentence "giving both sides outside options (O₄) dissolves lock-in to Φ(MIP) = 0" does not. |
| O₅ "Platform Substitute (multi-homing) D′ = P₁ ∨ P₂ … Φ = 1.000, {D,R}, Mediator Replaced (competing platforms factor out)" | ✗ | Not in the prototype. The lab's `rival_platforms` study (V2 #32, verdict RIVAL_ENCODING) finds the opposite of "platforms factor out": substitutable `W′ = S1 ∨ S2` gives "equal-Φ rivalry: each reachable state selects one platform triad with W". Either drop the row or restate it from that study. |
| "a sharp structural law that held across 60 of 60 randomized multi-party configurations: a platform's irreducible core consists of itself plus whichever parties lack an outside option" | ✓ | `enricher_regime.py` §4: "law holds on 60/60 random option configurations". |
| Table 2 controls 0.000 / 0.830 / 2.000 / 2.000 with those rules | ✓ values | File name wrong (C1). |

`[DRAFTED by Claude]` replacement for the Table 3 outside-option rows, using the prototype's own five
designs (keep your column headings):

> O₁ both captive — D′=P, P′=D∧R, R′=P — Φ 2.000 — {D,P,R} — BOTTLENECK (neither party can exit)
> O₂ complementary direct tie (repeat trips need app and contact) — D′=P∧R, P′=D∧R, R′=P∧D — Φ 6.000 — {D,P,R} — ENRICHER
> O₃ captive driver, mobile rider — D′=P, P′=D∧R, R′=P∨D — Φ 0.415 — {D,P} — CAPTURE of driver
> O₄ mobile driver, captive rider — D′=P∨R, P′=D∧R, R′=P — Φ 0.415 — {P,R} — CAPTURE of rider
> O₅ both mobile (substitute direct tie) — D′=P∨R, P′=D∧R, R′=P∨D — Φ 0.830 — {D,R} — BYPASSED (platform leaves the core; parties stay bound)

and for A.2.2's third bullet: "Giving only the rider an outside option (O₃) shrinks the core to the
captive driver and the platform; giving only the driver one (O₄) shrinks it to the platform and the
captive rider; giving both (O₅) removes the platform from the core and leaves the driver and rider bound
to each other — the platform is bypassed, not dissolved."

**Example 02, insurance claim.** Parties: Claimant `C`, **auto-adjudication engine `E`**, human
adjuster `A`; mediator `E`. **Five design encodings**, no rival pair: `pipe` triadic 2.000 {C,E,A}
BOTTLENECK (prediction held); `gated` 0.415 {C,E} CAPTURE (failed); `loop` 1.000 {E,A} CAPTURE (failed);
`loop_nolearn` 2.000 {C,A} BYPASSED (failed); `frozen` dyadic 0.000 (held). Two of five naive
predictions held. The logged AI drafter left rules unwritten for four of five designs; `encode_check`
rejects the file with **9 problems in 5 encodings** (eight missing party rules, one missing mediator
alternative). Doc Table 5 says "Intake Portal (M)" and "2 rival readings + 4 underspecified designs"
— ✗ on both; "9 problems" ✓; "Drafter refused to invent 4 ungrounded rules" ~ (it left four designs'
rules unwritten).

**Example 03, code-review gate.** Parties: Author `A`, CI gate `G`, **Maintainer `M`** (not "Reviewer
R"). Two rival encodings. `gated` ("maintainers wait for CI": A′ = G∧M, G′ = A, M′ = A∧G) → **triadic
Φ = 1.000, core {A,M}, G BYPASSED**, naive prediction failed. `diff_only` ("approve on the diff alone":
M′ = A) → **triadic Φ = 2.000, core {A,G,M}, G ENRICHER**, prediction failed. The Doc's row ("G′ = A ∧ R
yields Triadic BOTTLENECK Φ = 2.0, core {A,G,R}; rubber-stamp excludes R from major complex (#39
HUMAN_COMMIT_READ)") is ✗ throughout: no encoding has that rule, no result is BOTTLENECK, and the
rubber-stamp result belongs to the lab's `hitl_rubber_stamp` study, not to this example.
`[DRAFTED by Claude]`: "Required review gate (`gated`): when maintainers wait for CI the gate is
bypassed — the author and maintainer form the core at Φ = 1.0 and the gate sits outside it; approving
on the diff alone (`diff_only`) brings the gate into a three-party core at Φ = 2.0 as an enricher.
Both naive predictions failed; the field-mock M4 reads the same (BYPASSED)."

**Example 04, dealer vs clearinghouse.** Parties `U` (upstream), `I` (intermediary), `V` (downstream).
`dealer` (U′ = V, I′ = U, V′ = I, a ban on direct sales) → triadic 2.000 {U,I,V} BOTTLENECK,
**contingent** (opening the bypass loses Φ = 2.000; core → {U,V}). `clearinghouse` (I′ = U∧V) →
triadic 2.000 {U,I,V} BOTTLENECK, **intrinsic** (bypass loses 0.000; core → {U,I}). The Doc's row
("Sequential dealer inventory relay factors (Dyadic, Φ = 0.0); simultaneous net clearinghouse binds
{B,M,S} (Triadic, Φ = 2.0)") is ✗: both are triadic; the contrast is whether the intermediary's place
survives a direct tie. That contrast is a better story for the call than dyadic-vs-triadic; use it.

**Logged AI runs.** Drafter on 01: 2 encodings, admissible, identical to A and B, both predictions
held ✓. Adversary on 01: 4 encodings admissible; `driver_pool` predicted triadic {D1,D2,P,R} → computed
**dyadic, {P,R}**, FAILED ✓; `direct_contact_substitute` predicted dyadic → computed **triadic {D,R},
BYPASSED, Φ = 0.830**, FAILED ✓. The Doc's narrative of both failures is right; only the file names and
the 1.198 are wrong. Insurance drafter: REJECTED, 9 problems ✓.

### C3. "256 structures", regimes, and the lever matrix

| Doc says | Status | Fact | Source |
|---|---|---|---|
| "Running PyPhi across all 256 possible three-party mediated coordination structures proves that joint influence and systemic wholeness are orthogonal … four distinct coordination regimes" (§2) | ✗ | The 2 × 2 (wholeness × joint determination) comes from the **Peirce probes**: 89 four-node one-input wirings (Φ > 0 in 8, all pure cycles) and 30 two-input forms (5 jointly determined inside a whole, 11 jointly determined at Φ = 0, 1 neither). The 256-form census is a different object (next row). | `thinkers-peirce-h1-irreducibility`, `thinkers-peirce-jd-full` (both PASS today) |
| "Exhaustive enumeration of all 256 three-party Boolean structures partitions the space into 56 dyadic structures, 132 cycle-supported triads, and 68 mediated triads" (A.3 item 2; App. C item 2) | ∅ | No file in either repo contains 56, 132 or "cycle-supported". The census is **4 worker rules × 16 mediator rules × 4 counterpart rules = 256 strict-mediation forms; 24 triadic (9.4%), 232 dyadic; 24/160 where the mediator reads both parties, 0/96 otherwise**. "68" matches `BOTTLENECK 68 (13.6%)` in the coarse regime count over **500 random forms**, a different universe. | `proto_census.txt`; `proto_mediator_in_core.txt` §3 |
| "correlation and mutual-information proxies miss over a third (96 of 256) of the irreducible triads that exact PyPhi catches (Appendices A–B)" (§4) | ∅ | No such figure. The proxy result is rank-AUC 0.563 (ΦID Φᵣ) and 0.629 (Φ_WMS) over the 256 census forms; "96" is the number of census forms whose mediator does not read both parties (0/96 triadic). | `reproduce.json` `proxies`, `census` |
| Regime frequencies | — | Over 500 random mediated forms (seed 7): coarse dyadic 44.4%, BYPASSED 18.8%, BOTTLENECK 13.6%, ENRICHER 23.2%; refined (capture split out) CAPTURE 28.2%, BOTTLENECK 2.6%, ENRICHER 6.0%. The Doc does not cite these; they are the sourced numbers to use if you want a population statement. | `proto_enricher_regime.txt` §1 |
| Table 4 lever matrix: "Switch Convey → Joint Commit: Φ 0.0 → 2.0" | ✓ | B→A flip. | |
| Table 4: "Pool Replaceable Side … locks in {M,B} (Φ = 1.0)" | ✗ | System Φ = 0.000; {M,B} is the major complex. | C2 |
| Table 4: "Establish Direct Tie to B … core {A,B} (Φ = 1.198, BYPASSED)" | ✗ | Φ = 0.830. | C2 |
| Table 4: "Block Counterpart Exit … across all 60/60 random trials" | ✓ | | |
| Table 4: "Multi-Home Across Mediators (O₅ …): Factors individual mediator out of core" | ✗ | See `rival_platforms` (C2). | |
| Table 4: "Form Worker Coalition / Union: Restores collective input parity" | ~ | Lab `worker-union-scale` (V2 #31) verdict UNION_MIRRORS_COAL: a union scales like a counterpart coalition. Cite it; the Doc's cell cites nothing. | `ci/reproduce.json` |
| "studies/strategic_model/ … We will formalize the actor-indexed strategic lever matrix (Table 4)" (A.3) | ~ | Fine as Stage 2 work **if** the path is dropped (it does not exist) and Appendix D stops listing it under `v0.1-stage1`. | |

`[DRAFTED by Claude]` for §2's sentence: "Running the Peirce probes — 89 one-input wirings and 30
two-input forms, each cut by PyPhi — shows that joint influence and systemic wholeness come apart in
both directions, which yields four coordination regimes that organizational prose routinely conflates
(Technical Addendum, Section A.1 and Appendix A.2)."

`[DRAFTED by Claude]` for §4's third bullet: "…and shows, across the 256 strict-mediation forms of the
census, that two popular time-series proxies separate dyadic from triadic structures at rank-AUC
0.563 and 0.629 — barely above chance — while exact PyPhi finds the 24 irreducible forms outright
(Technical Addendum, Appendix A.3)."

`[DRAFTED by Claude]` for A.3 item 2 / Appendix C item 2: "Exhaustive enumeration of the 256
strict-mediation three-party forms (4 worker rules × 16 mediator rules × 4 counterpart rules) finds 24
irreducible and 232 factorable, with a mediator that reads both parties necessary but not sufficient
(24/160 vs 0/96)."

### C4. Lab studies and Appendix D

Eighteen lab checks re-run today by name; 17 PASS, `wageman-ti-verdict` FAIL (C7).

| Doc says | Status | Fact | Source |
|---|---|---|---|
| Peirce: 89 wirings; 66 adicity 3, 12 adicity 4; cause-side ≤ 2; 11 unbranched; 8 of 89 Φ > 0; copy ring Φ = 2.0 | ✓ | Exactly as printed. | `lab_ci_named.txt`; `thinkers/peirce/FINDINGS.md` |
| 30 two-input forms: 5 in a whole, 11 at Φ = 0, 1 no JD; "3-voter majority triad … Φ = 0 with 4 partition ties" | ✓ | | `thinkers-peirce-jd-full`, `thinkers-peirce-jd` |
| "such as a unanimous three-voter majority triad" (A.1) | ✗ wording | The form is `majority_triad` (2 of 3). "Unanimous majority" contradicts itself; unanimity is the AND triad, which is triadic at Φ = 3 in `probe-voting-robustness`. | `ci/reproduce.json` |
| Thompson: pooled Φ = 0, sequential 2.0, reciprocal 2.0, "collapses at its top step" (A.2.3, A.5) | ✓ + omission | Canonical encodings only. The study's verdict is **PARTIAL_ALIGNMENT, alignment 0.429**: "alternate encodings flip the verdict" (pooled all-required → triadic; sequential acyclic hand-off → dyadic). Say so in one clause. | `thompson_verdict_bridge/FINDINGS.md` |
| "Wageman's (1995) hybrid team designs factor cleanly" (A.2.3); WAGEMAN_PREDICTS_VERDICT (App. D) | ✗ | The study tests whether a Wageman-style interdependence index predicts the verdict: AUC 1.000 on the designed panel, and it does **not** predict Φ magnitude (XOR and AND share W at Φ 0.5 vs 2). Nothing about hybrid designs factoring. | `wageman_ti_verdict/FINDINGS.md` |
| CUTS_ACROSS "(4/8 formal vs. shadow diverge)" (App. D) | ✗ | Six forms, **4 of 6 mismatch** H1, alignment 0.333; the words "shadow" and "8" appear nowhere. | `formal_informal_cut/FINDINGS.md` |
| HITL: "rubber-stamping … leaves the human reviewer outside the major complex while the automated loop stays integrated at Φ = 2.0" (A.2.3) | ✓ | Panel row `stamp_posthoc`: whole dyadic, Φ 2, core {AI,S,C} or {S,C}, H out. | `hitl_rubber_stamp/FINDINGS.md` |
| SHARP_CLASS_GRADED_PATH "(R² = 0.992)" (App. D) | ∅ | No R² anywhere in the study. The result: on the diagonal (L,L,L), L = 0 NULL; L = 1 DYADIC Φ 0.390 {W,S}; L = 2 TRIADIC Φ 3.170 {W,S,C}. | `graded_commit_verdict/FINDINGS.md` |
| EXTRA_RESOLUTION_TO_PHI "(3 bits → 5.755 bits)" (App. D) | ∅ | No such figures. The result: with a ternary mediator, Φ on the (1,S,1) sweep runs 1.170 / 0.500 / 2.000 (full form) while the core stays {W,S,C}. | `mixed_radix_mediator/FINDINGS.md` |
| BLINDSPOT_SURVIVES_RADIX "(parity Φ = 2²⁻ⁿ)" (App. D, A.3) | ~ | That study shows balanced commits `S′ = (W+C) mod k` keep a flat Φ ≈ 0.5 band at k = 2, 3, 4. The 2^(2−n) law is `parity_law_n_gt6` and `parity_law_n_gt8` (LAW_HOLDS_NGT6, LAW_HOLDS_NGT8). Attach each figure to its study. | both FINDINGS |
| MARL "rank-AUC 0.485–0.555 across tabular and neural policies" | ✓ | EMERGENT_NULL (tabular Q-learning: 0.555 / 0.485) and NULL_SURVIVES (MLP and linear-FA policies). The study says "not deep MARL"; your "multi-agent reinforcement learning (MARL)" should say "tabular and small-network MARL proxies". | both FINDINGS |
| Imputation 0.944 (MI), 0.806 ring / 0.750 omit / 0.896 copy-W (exact Φ) | ✓ | | `topology_aware_imputer`, `imputer_exact_phi`, `matched_imputer_exact_phi` |
| Parity law to n = 10 | ✓ | LAW_HOLDS_NGT8 at n ∈ {8, 9, 10}. | `parity_law_n_gt8` |
| 3.169925 = 2 log₂ 3 (B.2) | ✓ | | `pyphi-iit4-mv-m2-smoke` PASS |
| TWO_CONDITION_STATE_DEPENDENT | ✓ | Study `ternary_pivotality` (V2 #1). | |
| Appendix D study labels | ✗ ×12 | `ternary_conjunctive_mediator`→`ternary_pivotality`; `graded_commitment_sweep`→`graded_commit_verdict`; `mixed_radix_asymmetric`→`mixed_radix_mediator`; `multivalued_xor_blindspot`→`parity_radix_blindspot`; `hitl_oversight`→`hitl_rubber_stamp`; `ai_labor_displacement`→`ai_fidelity_displace`; `marl_emergent_triads`→`marl_emergent_learn`; `dual_principals`→`dual_principal_conflict`; `union_vs_coalition`→`worker_union_scale`; `multihoming_bypass`→`rival_platforms`; `Substitute_degradation`→`gig_substitution`; `prior_matched_vs_mismatched`→`matched_imputer_exact_phi`. | `ls org_frontier/studies`; check names in `ci/reproduce.json` |
| "CI checks #001–#082" for the thinker catalog | ~ | 82 checks named `thinkers-<name>-…`, 16 thinkers; the manifest has no numeric IDs. | `ci/reproduce.json` |
| Agenda IDs V2 #1–#4, #24, #29, #31, #32, #35, #37, #39, #40, #41, #43, #44, #46; V3 #1, #5, #10, #15; V4 #4, #5, #9 | ✓ | Each matches the question text in `org_frontier/RESEARCH_AGENDA_50_V2.md`, `org_frontier/RESEARCH_AGENDA_V3.md` and `org_frontier/RESEARCH_AGENDA_V4.md`. | |
| "V3 #6" in the AI-workflows row | ✗ | V3 #6 is "k > 2 local triads sharing a single mediator". No MARL/AI study answers it; `marl_deep_replicate` cites no agenda number. Drop it. | `RESEARCH_AGENDA_V3.md` l. 56 |
| "probes 98, 107" | ✓ | PROBES.md rows 98 (agent-based difficulty, refuted, AUC 0.567) and 107 (partner-modeling agents, refuted, 0.541). | `org_frontier/probes/PROBES.md` |
| `foundations/phiid_vs_phi`: ρ 0.283 / AUC 0.669; ρ 0.124 / AUC 0.560 | ✓ | | its FINDINGS l. 32–33 |
| Proxies rank-AUC 0.563 / 0.629 | ✓ | Prototype check `proxies`; lab `proxy_bridge/FINDINGS.md`. Also in the lab essay the best-threshold accuracy for Φ_WMS is 0.778, so "near chance" is true of rank-AUC only. | |

### C5. Counts

| Doc | Status | Count today |
|---|---|---|
| 542 automated CI checks | ✓ | 542 before this branch's addition (543 with `irreducibility-pipeline-reproduce`). |
| 127 studies in `org_frontier/studies/` | ✓ | 127 directories. |
| 135 probes | ✓ | 135 `probe_*.py` files. |
| 9 `foundations/` studies | ✓ | 9 study directories plus `paper/`. |
| 82 probes across 16 thinkers | ✓ | 82 `thinkers-*` checks; 16 thinker directories. |
| 17 reference results; 19 tests | ✓ | 17/17; 19 passed. |
| 101/101 flips; 22/101 bracketed; 60/60 | ✓ | |
| Part I 1,890 words | ✓ | |

### C6. The prototype is now inside the lab

Per your decision — "people fork algorithmacy lab and that should give them all the access" — the
prototype was copied into this branch at `irreducibility-pipeline/` with its internal layout intact
(`irreducibility/`, `encode/`, `examples/`, `studies/`, `protocol/`, `tests/`, `reproduce.py`,
`reproduce.json`, `README.md`, `APPENDIX.md`, `CITATION.cff`, `LICENSE`, `pyproject.toml`,
`requirements.txt`); `.git`, caches and a stray `pyphi.log` were left out. Its own `reproduce.py`
resolves paths from its file location, so `python irreducibility-pipeline/reproduce.py` runs from
the lab root, and a lab check `irreducibility-pipeline-reproduce` (slow, 900 s) is registered in
`ci/reproduce.json` expecting its "17/17 checks passed." line. The lab README's programs list gains
one line pointing at it.

What this changes in the Doc: every "`irreducibility-pipeline` (tag `v0.1-stage1`)" becomes "the
`irreducibility-pipeline/` directory of `algorithmacy-lab`"; the tag is re-cut on the lab commit that
lands this (suggest `orgsci-stage1`) when you push; the one URL
`https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab` covers both artifacts; and A.2's
"reproduces … via a single command" can become "`python irreducibility-pipeline/reproduce.py` from a
clone of the lab". Nothing is pushed; the branch is `cursor/orgsci-ai-stage1-proposal-ec39` in the
worktree `~/iit-playground/wt-orgsci-ai`, and `REPO_LAYOUT.md` wants a PR into `contrib`.

### C7. Repo health found on the way

- **`wageman-ti-verdict` fails on this branch.** The manifest expects "ρ(W,Φ)=0.883"; the script now
  prints **0.867** (`results/summary.json` would change from 0.8833 to 0.8667). Every other number in
  the check reproduces (AUC 1.000, acc 1.000 at W ≥ 0.472, H3 refuted). Either the manifest or the script
  drifted after the last full run. I restored the regenerated `results/summary.json` rather than commit
  it; the drift needs a maintainer's decision. The Doc cites WAGEMAN_PREDICTS_VERDICT (Appendix D), so
  a reviewer running `ci/reproduce.py` in full would hit this.
- The Peirce probe runs rewrite their `results/*.json` with new timings only; restored.
- `third_party/pyphi_iit4_mv/README.md` and the lab README still describe the upstream PyPhi 2.0 state
  as of 25 October; fine for now.

---

## D. Citation audit

Every entry checked against Crossref (`crossref/*.json`), with the publisher's page, Semantic Scholar
or OpenAlex where Crossref lacked the record, and against full text where it was on disk.

| # | Reference as in the Doc | Status | Finding |
|---|---|---|---|
| 1 | Albantakis et al. (2023) … "phenomenal existence in physical **systems**", *PLoS Comput Biol* 19(10) e1011465 | ✗ title | "…in physical **terms**". DOI 10.1371/journal.pcbi.1011465. |
| 2 | Anthony, Bechky & Fayard (2023) *Org Sci* 34(5) 1672–1694 | ✓ | 10.1287/orsc.2022.1651 |
| 3 | Burch (1991) Texas Tech UP | ✓ | Lubbock, TX. |
| 4 | Burt (1992) Harvard UP | ✓ | |
| 5 | **Cameron (2024). "The making of crystal-clear calls: Algorithmic management and the standardization of service work." *ASQ* 69(1), 1–42** | ✗ fabricated | No such article. The ASQ 2024 article is Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures consent through constant and confined choices. *ASQ*, 69(2), 458–514. DOI 10.1177/00018392241236163. (Copy in `~/Downloads`.) Its abstract — ride-hail drivers "navigate being managed by an algorithm" through "constant and confined choices" — supports your §1 and §4 uses. |
| 6 | Caplow (1956) *ASR* 21(4) 489–493 | ✓ | 10.2307/2088718 |
| 7 | Coleman (1988) *AJS* 94(Suppl.) S95–S120 | ✓ | 10.1086/228943 |
| 8 | Curchod et al. (2020) *ASQ* 65(3) 644–676 | ✓ | 10.1177/0001839219867024 |
| 9 | Daft & Lewin (1990) *Org Sci* 1(1) 1–9 | ✓ | 10.1287/orsc.1.1.1 |
| 10 | Gartenberg, Hasan, Murray & Pierce (2026) *Org Sci* 37(3) 795–812 | ✓ | 10.1287/orsc.2026.ed.v37.n3; matches the CFP's own list. |
| 11 | Girotra, Terwiesch & Ulrich (2010) *Mgmt Sci* 56(4) 591–605 | ✓ | 10.1287/mnsc.1090.1144 |
| 12 | Granovetter (1973) *AJS* 78(6) 1360–1380 | ✓ | 10.1086/225469 |
| 13 | **Hereth Correia & Pöschel (2004)** "The power of Peircean algebraic logic." In *Conceptual Structures at Work: ICCS 2004* (LNCS 3127, pp. 337–350) | ✗ venue | The paper is in Eklund, P. (Ed.), *Concept Lattices: Second International Conference on Formal Concept Analysis, ICFCA 2004*, LNAI **2961**, pp. 337–**351**. DOI 10.1007/978-3-540-24651-0_29. The 2006 paper's own reference [HCP04] says the same. |
| 14 | Hereth Correia & Pöschel (2006) "The teridentity and Peircean algebraic logic." *ICCS 2006*, LNAI 4068, pp. 229–246 | ✓ | 10.1007/11787181_17. **Lemma 1** (any t-connected set of places in a PAL∖{id₃} term over unary and binary relations has |X| ≤ 2) and **Theorem 2** (|A| ≥ 2 ⇒ ⟨Σ⟩PAL∖{id₃} ⊊ ⟨Σ⟩PAL) are as the Doc states. |
| 15 | Kellogg, Valentine & Christin (2020) *AMA* 14(1) 366–410 | ✓ | 10.5465/annals.2018.0174 |
| 16 | Koshkin (2024) "Logical reduction of relations…" *Logic J. IGPL* 32(5) 779–**813** | ~ pages | 779–**809**; online June 2023, print September 2024. DOI 10.1093/jigpal/jzad010. |
| 17 | **Koshkin (2025). "Logical reduction of finite relations and granular computing." *IJAR* 186, 109523** | ✗ fabricated record | *IJAR* 186, 109523 is Obiedkov & Sertkaya, "PAC learning of concept inclusions…". The paper whose content Appendix A.1 describes (Δ₃ from binary equality; reduction to binaries on finite |D| ≥ 3; ¬I₃ pp-irreducible on Boolean domains, Theorems 2–4; bond algebra, Theorem 6) is Koshkin, S. (2024). Functional completeness and primitive positive decomposition of relations on finite domains. *Logic Journal of the IGPL*, advance article, jzae077. DOI 10.1093/jigpal/jzae077; arXiv 2606.19492. **Theorem numbers verified against arXiv v1**: Thm 2 (relative reduction; n ≥ 4 reduces to ternary), Thm 3 (cofinite n-ary relations, 3 ≤ n ≤ |D|, reduce to binary), Thm 4 (¬I₃ non-bijunctive, irreducible on Boolean domains), Thm 6 (I₃ bond-irreducible on any domain with ≥ 2 elements). The published version's numbering is unchecked. |
| 18 | March (1991) *Org Sci* 2(1) 71–87 | ✓ | 10.1287/orsc.2.1.71 |
| 19 | Mayner et al. (2018) *PLoS Comput Biol* 14(7) e1006343 | ✓ | 10.1371/journal.pcbi.1006343 |
| 20 | Mediano et al. (2025) "Toward an **extended** taxonomy…" *PNAS* 122(39) e2423297122 | ✗ title | "Toward a **unified** taxonomy of information dynamics via Integrated Information Decomposition." DOI 10.1073/pnas.2423297122. |
| 21 | Obstfeld (2005) *ASQ* 50(1) 100–130 | ✓ | 10.2189/asqu.2005.50.1.100 |
| 22 | Orlikowski & Scott (2008) *AMA* 2(1) 433–474 | ✓ | 10.5465/19416520802211644 |
| 23 | Ostrom (1990) CUP | ✓ | 10.1017/cbo9780511807763 |
| 24 | Peirce (1933) "The logic of relatives" (1897), CP 3.456–3.552 | ✓ | Standard locator for the 1897 *Monist* paper. |
| 25 | Quine (1954) *JSL* 19(3) 180–182 | ✓ | 10.2307/2268616. Read in full: the Kuratowski construction {{x},{x,y}} and "a universe closed under pairing" are on p. 180 as the Doc says. |
| 26 | Rahman (2021) *ASQ* 66(4) 945–988 | ✓ | 10.1177/00018392211010118 |
| 27 | Rudin (2019) *Nat Mach Intell* 1(5) 206–215 | ✓ record | 10.1038/s42256-019-0048-x. Attribution questioned in E6. |
| 28 | Simmel (1950) "Quantitative aspects of the group (1902)." In Wolff, pp. 87–177 | ✓ pages, ~ date | Part Two of Wolff's edition runs from p. 87 to the end of "Maximum and Minimum Sizes" (p. 174 ff.; Part Three opens at 181). Wolff translates *Soziologie* (1908), ch. 2; the 1902 *AJS* articles are the earlier English version — say 1908 or 1902/1908. The dyad passage you paraphrase is on **p. 123**: "the secession of either would destroy the whole … As soon, however, as there is a sociation of three, a group continues to exist even in case one of the members drops out." |
| 29 | Thompson (1967) McGraw-Hill | ✓ | |
| 30 | Wageman (1995) *ASQ* 40(1) 145–180 | ✓ | 10.2307/2393703 |
| 31 | Williams & Beer (2010) arXiv:1004.2515 | ✓ | Submitted 14 April 2010. |
| 32 | Mediano/Williams-Beer as PID/ΦID sources | ✓ | PID (Williams & Beer); ΦID (Mediano et al.). |

**Cited in the text, absent from the list** — add, verified:

- Stark, D., & Pais, I. (2020). Algorithmic management in the platform economy. *Sociologica*, 14(3),
  47–72. https://doi.org/10.6092/issn.1971-8853/12221
- Rosenblat, A., & Stark, L. (2016). Algorithmic labor and information asymmetries: A case study of
  Uber's drivers. *International Journal of Communication*, 10, 3758–3784. (Running head of the PDF.)
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.
  https://doi.org/10.1186/1471-2202-5-42

**Corrected entries** `[DRAFTED by Claude]`, in your list's format:

- Albantakis, L., … & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the
  properties of phenomenal existence in physical terms. *PLoS Computational Biology*, 19(10), e1011465.
- Cameron, L. D. (2024). The making of the "good bad" job: How algorithmic management manufactures
  consent through constant and confined choices. *Administrative Science Quarterly*, 69(2), 458–514.
- Hereth Correia, J., & Pöschel, R. (2004). The power of Peircean algebraic logic (PAL). In P. Eklund
  (Ed.), *Concept Lattices: Second International Conference on Formal Concept Analysis, ICFCA 2004*
  (LNAI Vol. 2961, pp. 337–351). Springer.
- Koshkin, S. (2024a). Logical reduction of relations: From relational databases to Peirce's reduction
  thesis. *Logic Journal of the IGPL*, 32(5), 779–809.
- Koshkin, S. (2024b). Functional completeness and primitive positive decomposition of relations on
  finite domains. *Logic Journal of the IGPL*, advance article jzae077. https://doi.org/10.1093/jigpal/jzae077
- Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K., &
  Barrett, A. B. (2025). Toward a unified taxonomy of information dynamics via Integrated Information
  Decomposition. *Proceedings of the National Academy of Sciences*, 122(39), e2423297122.

and in the text, "(Koshkin, 2024, 2025)" → "(Koshkin, 2024a, 2024b)"; "Koshkin, 2025, Theorems 2–4"
→ "Koshkin, 2024b, Theorems 2–4"; "Koshkin, 2025, Theorem 6" → "Koshkin, 2024b, Theorem 6".

---

## E. Attribution and the debates as portrayed

Depth of reading, so you can weigh each item. **Read in full:** Quine (1954); Hereth Correia &
Pöschel (2004, 2006); Koshkin (2024b, arXiv v1); Rosenblat & Stark (first page); Wolff's Simmel (the
table of contents and pp. 118–124 around the dyad passage). **Abstract only:** Kellogg et al. (2020);
Stark & Pais (2020); Cameron (2024); Rahman (2021); Rudin (2019); Vallas & Schor (2020); Schor et al.
(2020); Einav, Farronato & Levin (2016); Hall & Krueger (2018); Wood et al. (2019); Victor & Blackburn
(1987); Puranam, Raveendran & Knudsen (2012); Raveendran, Silvestri & Gulati (2020); Parasuraman &
Riley (1997); Green & Chen (2019); Lebovitz, Lifshitz-Assaf & Levina (2022); Koshkin (2024a).
**Database record only, not read:** Skitka, Mosier & Burdick (1999); Sundararajan (2016); every other
entry in Part D that is marked ✓ on its record. Where a proposal below rests on an abstract, read the
paper before the sentence goes into the Doc.

**E1. The "rival camp" has no citation (§1).** "One camp sees totalizing triads that fuse workers,
clients, and software into an indivisible whole (Kellogg et al., 2020; Stark & Pais, 2020); a rival
camp sees high-speed market relays unbundling work into arms-length dyads." The second camp is real
and nameable. Einav, Farronato and Levin (2016, *Annual Review of Economics* 8, 615–635,
10.1146/annurev-economics-080315-015334) "view the primary function of these markets as making it easy
for buyers to find sellers and engage in convenient, trustworthy transactions" — the platform as
matching market. Hall and Krueger (2018, *ILR Review* 71(3), 705–732, 10.1177/0019793917717222) model
Uber drivers as flexible independent suppliers. Sundararajan (2016, *The Sharing Economy*, MIT Press)
calls it crowd-based capitalism. Vallas and Schor's review (2020, *Annual Review of Sociology* 46,
273–294, 10.1146/annurev-soc-121919-054857) names this image "entrepreneurial incubators" and sets it
against "digital cages", which is your first camp. `[DRAFTED by Claude]`: "…a rival camp sees
matching markets that relay buyers to sellers and leave the work itself to arm's-length contractors
(Einav, Farronato, & Levin, 2016; Hall & Krueger, 2018; Sundararajan, 2016) — the 'entrepreneurial
incubator' image in Vallas and Schor's (2020) review."

**E2. Kellogg et al. do not describe a triad (§1).** Their abstract frames algorithmic control as
Edwards's "contested terrain" between employers who implement technologies and workers who resist,
through six mechanisms (restricting, recommending, recording, rating, replacing, rewarding). That is a
labor-process, employer–worker frame; customers enter only as raters. Stark and Pais (2020) do say what
you attribute: "In a triangular geometry, platform owners co-opt the behavior of providers and users,
enrolling them in the practices of algorithmic management without managerial authority having been
delegated to them." Keep Stark & Pais for the triad; cite Kellogg et al. for control, not for fusion.
(Stark and Pais also give you the contrastive line "actors in markets contract, hierarchies command,
and networks collaborate, platforms co-opt" — it may be worth quoting.)

**E3. "Since Thompson (1967), scholars have treated joint influence and systemic wholeness as if they
were the same thing … overturns a sixty-year assumption" (§2).** The field has re-cut interdependence
repeatedly. Victor and Blackburn (1987, *AMR* 12(3), 486–498, 10.2307/258515) argued that Thompson's
conceptualization "fail[s] to satisfy basic requirements for empirical or practical investigations"
and rebuilt it on Kelley–Thibaut outcome structures. Wageman (1995) split task from outcome
interdependence. Puranam, Raveendran and Knudsen (2012, *AMR* 37(3), 419–440, 10.5465/amr.2010.0535)
introduced epistemic interdependence "to sharply distinguish interdependence between tasks and between
agents." Raveendran, Silvestri and Gulati (2020, *AMA* 14(2), 828–868, 10.5465/annals.2018.0015) sort
it into task, goal and knowledge interdependence. None of the four abstracts describes a partition
test of whether the coupled unit is decomposable, which is your point — I did not read the four papers
in full, so check before asserting it — but "treated as the same thing" is not what happened. `[DRAFTED by Claude]`: "Interdependence typologies since Thompson (1967) classify how tasks,
outcomes and knowledge couple (Victor & Blackburn, 1987; Wageman, 1995; Puranam, Raveendran, &
Knudsen, 2012; Raveendran, Silvestri, & Gulati, 2020); none supplies a test of whether the coupled
unit can be cut without loss. Running PyPhi over the Peirce probes shows that joint influence and
systemic wholeness are separate dimensions…" and drop "overturns a sixty-year assumption".

**E4. "After a decade of fieldwork … scholars remain deadlocked" (§1).** No source says deadlock. Two
reviews document the disagreement you need: Vallas and Schor (2020) find four competing metaphors
(incubator, digital cage, accelerant of precarity, chameleon), each with limitations; Schor et al.
(2020, *Theory and Society* 49, 833–861, 10.1007/s11186-020-09408-y) find that both dominant
approaches — precarity and algorithmic control — "predict that workers will have relatively common
experiences," and the data show heterogeneity instead. `[DRAFTED by Claude]`: "…scholars still hold
competing images of what the platform is (Vallas & Schor, 2020; Schor et al., 2020): when an algorithm
mediates…"

**E5. Simmel (§1, A.1).** Accurate. Wolff p. 123 carries both halves of your paraphrase (the dyad dies
with either member's secession; a group of three "continues to exist even in case one of the members
drops out"), and "super-individual" is his term on the same page. Add the page: (Simmel, 1950: 123).
"Play partners against each other" is *tertius gaudens* and *divide et impera*, Wolff pp. 154–169.

**E6. Rudin (2019) as the source of the "post-hoc verification trap" / "Potemkin oversight" (A.2.3,
A.5).** Rudin's argument is that post-hoc explanations of black-box models are unreliable and that
high-stakes decisions should use inherently interpretable models. It says nothing about a human
reviewer rubber-stamping a system's recommendation. That phenomenon is automation bias: Parasuraman
and Riley (1997, *Human Factors* 39(2), 230–253, 10.1518/001872097778543886) and Skitka, Mosier and
Burdick (1999, *IJHCS* 51(5), 991–1006, 10.1006/ijhc.1999.0252) name it; Green and Chen (2019, *PACM
HCI* 3 CSCW, 1–24, 10.1145/3359152) study "algorithm-in-the-loop" decisions; and in this journal
Lebovitz, Lifshitz-Assaf and Levina (2022, *Org Sci* 33(1), 126–148, 10.1287/orsc.2021.1549) watched
radiologists either disengage from or defer to opaque AI tools. `[DRAFTED by Claude]`: "…formalizing
the rubber-stamp pattern that the automation-bias literature documents (Parasuraman & Riley, 1997;
Skitka, Mosier, & Burdick, 1999) and that Lebovitz, Lifshitz-Assaf, and Levina (2022) observed among
radiologists facing opaque AI." Keep Rudin only where the claim is about explanations of black boxes.

**E7. The formal-logic claims (A.1, Appendix A.1).** Verified against full text: Quine's pairing
translation (p. 180); Hereth Correia & Pöschel 2006 Lemma 1 and Theorem 2; Koshkin's Theorems 2, 3, 4
and 6 (arXiv version). The 2004 paper's Theorem 13 states the finite-domain version of the 2006
result with the proof deferred, which is why "introduced with a restricted proof in Burch, 1991" and
the 2004/2006 pairing are right. Two wording points: "Peircean Algebraic Logic (introduced with a
restricted proof in Burch, 1991)" — Burch introduced PAL and proved the thesis under a restriction on
juxtaposition; the 2006 paper removes the restriction and reproves it; say that. And "Koshkin, 2024 for
infinite domains and projoins" — the 2024a abstract speaks of "natural joins", "ternarity" and the
finite/infinite split; I could not confirm the word "projoin" without the full text.

**E8. "A frontier LLM … got every nontrivial variation backward" (§3); "standalone LLMs fail badly"
(§3); "LLMs hallucinate ungrounded rules and misguess multi-party partition math" (A.2.1).** The
evidence is one model, one stipulated case, two adversary predictions (both wrong), plus one drafter
run that matched the human encodings and one that declined to invent rules. That supports "the
model's own predictions about what its readings would compute were wrong both times"; it does not
support "every nontrivial variation" or a general failure claim. `[DRAFTED by Claude]`: "Given only
the case prose, the model found both design variants a human had encoded — and predicted both
verdicts backward: it expected driver pooling to stay a three-party triad (PyPhi: the drivers factor
out) and off-app repeat rides to collapse into a dyad (PyPhi: a bypass core of driver and rider)."

**E9. PID / ΦID (A.3, App. A.3).** Correctly attributed. One nuance: Φᵣ is the ΦID-based revised
integrated information; the Doc's gloss "corrects whole-minus-sum Φ(WMS) for double-counting
redundancy" matches Mediano et al.'s framing.

**E10. Daft & Lewin, March, Girotra et al., Gartenberg et al.** All as the CFP cites them. "Thirty-six
years later" (A.1) is right for 2026.

---

## F. Prioritized fix list

**Must fix before 1 November**
1. Replace the Table 3 outside-option rows and A.2.2's third bullet with the prototype's O1–O5 (C2).
2. Replace Table 5's Example 02, 03, 04 rows and A.2.3's "four worked cases" clause with the computed results (C2).
3. Correct Φ = 1.198 → 0.830 and Φ = 1.000 → "Φ = 0 (dyadic); core {P,R}" in Table 3, Table 4, A.2.2 and Part I §3 (C2, C3).
4. Remove "56 / 132 / 68" and "96 of 256"; use the census (24/256, 24/160, 0/96) and the Peirce probes (C3).
5. Fix the file paths in C1 and the twelve study labels in C4; drop `strategic_model` from `v0.1-stage1`; drop "V3 #6".
6. Replace the four unsourced Appendix D figures (R², 5.755 bits, 4/8, Wageman hybrid) with the studies' own numbers (C4).
7. Fix the reference list: Cameron, Koshkin 2025→2024b, HC&P 2004 venue, Albantakis and Mediano titles, Koshkin 2024 pages; add Stark & Pais, Rosenblat & Stark, Tononi (D).
8. Point every prototype reference at `irreducibility-pipeline/` inside the lab and name the lab tag (C6); then push the branch, open the PR into `contrib`, and cut the tag.
9. Replace the "[Anonymized …]" line with the author line.
10. Fix the workshop date in §4 and in this folder's README (27–28 February 2027, tentative, venue unstated).

**Should fix**
11. §1: cite the rival camp (E1); move Kellogg et al. to the control claim (E2); replace "deadlocked" (E4).
12. §2: replace the "sixty-year assumption" sentence (E3); fix the "256 … proves … four regimes" sentence (C3).
13. §3: state the AI step at its actual size (B); soften "every nontrivial variation" (E8); decide "literally" (B).
14. A.2.3 / A.5: re-attribute the rubber-stamp trap (E6); add the Thompson caveat (C4).
15. A.1: "unanimous three-voter majority" → "three-voter majority"; "Broadcast Cascades" (§2) vs "Cyclic One-Input Relay" (Table 1) — one name.
16. Step 6 / App. B.1: `contingency.py` is the bypass test; outside options are the O-designs and `enricher_regime` (C1).
17. "proves" ×6 → "shows" / "computes"; "collapses a decade-long debate" → "turns … into one testable rule"; "pre-registered" ×3 → "fixed before computing" (B).
18. §5: one sentence of execution risks; one clause on ethics (A).
19. Add captions "Table 1 … Table 6" where the text cites them; fix "Section A.2.2 and Table 5" (Table 5 is in Appendix B).

**Nice**
20. Compute the harness on itself and report it (B).
21. Trim the algorithmacy frame in §2's regime glosses; keep §1 and §5 (B).
22. One "Potemkin", or none (B).
23. "tabular and small-network MARL proxies" (C4); "Submission Tracks" → "Contribution types" (A).
24. Fix `wageman-ti-verdict`'s manifest or script so the full lab CI is green before reviewers run it (C7).

---

## Appendix: how each number was produced

```
# prototype (from its own root; venv-4.0 carries the PyPhi pin)
python reproduce.py                                    # 17/17, 2 m 17 s
python -m pytest -q tests                              # 19 passed
python -m irreducibility.analyze examples/01_gig_dispatch/encodings.json
python -m irreducibility.analyze examples/01_gig_dispatch/ai_draft_plus_adversary.json
python -m irreducibility.analyze examples/02_insurance_claim/encodings.json
python -m irreducibility.analyze examples/03_code_review_gate/encodings.json
python -m irreducibility.analyze examples/04_dealer_vs_clearinghouse/encodings.json
python -m studies.census; python -m studies.mediator_in_core; python -m studies.enricher_regime
python -m irreducibility.encode_check examples/01_gig_dispatch/ai_draft.json              # ADMISSIBLE 2
python -m irreducibility.encode_check examples/01_gig_dispatch/ai_draft_plus_adversary.json  # ADMISSIBLE 4
python -m irreducibility.encode_check examples/02_insurance_claim/ai_draft.json           # REJECTED 9

# lab (from the lab root)
python ci/reproduce.py thinkers-peirce-h1-irreducibility thinkers-peirce-jd thinkers-peirce-jd-full \
  hitl-rubber-stamp graded-commit-verdict mixed-radix-mediator parity-radix-blindspot formal-informal-cut \
  wageman-ti-verdict thompson-verdict-bridge imputer-exact-phi topology-aware-imputer \
  matched-imputer-exact-phi marl-emergent-learn marl-deep-replicate pyphi-iit4-mv-m2-smoke \
  parity-law-n-gt8 ternary-pivotality                 # 17 PASS, wageman-ti-verdict FAIL
python ci/reproduce.py irreducibility-pipeline-reproduce   # the new check

# citations
curl -s -G https://api.crossref.org/works --data-urlencode "query.bibliographic=<ref>" --data-urlencode rows=2
```
