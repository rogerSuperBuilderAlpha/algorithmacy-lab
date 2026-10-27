# Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2024). Reading between the lines: Modeling user behavior and costs in AI-assisted programming. In *Proceedings of the CHI Conference on Human Factors in Computing Systems* (pp. 1–16). ACM. https://doi.org/10.1145/3613904.3641936

**Identifier:** doi:10.1145/3613904.3641936; arXiv:2210.14306 · **Read depth:** full_text of the preprint (arXiv v5, 22 April 2024, 41 pages including appendices; the ACM version of record is open access under CC BY 4.0 but the ACM site and the MIT DSpace copy returned a bot wall or HTTP 429, so I did not open it. I read the body, Tables 1–3, the figure captions, limitations, future work, conclusion and references; in the appendices I looked only at the survey charts (A.3) and timeline figures. Locators are section numbers, not the CHI pages) · **Source-tier:** proceedings (read as preprint) · **Evidence basis:** direct_read · **Design and sample:** 21 programmers recruited from developer mailing lists "within our large organization" (the authors' affiliation is Microsoft Research) each solved one of eight tasks designed to fit a 20-minute block (mean 12.23 min, max 20.80; §5.1–5.2) with GitHub Copilot (August 2022 version), then labelled their own screen recording segment by segment with a 12-state taxonomy (CUPS); 1,024 suggestions shown, 3,137 labels; no no-Copilot baseline · **Parties modeled:** person–system (a programmer and a code-suggestion model) · **Facets:** none (new in round 4) · **Read:** 2026-10-14

## What it argues

Mozannar and colleagues argue that acceptance rates hide where programmers spend time with a code assistant. Their CodeRec User Programming States (CUPS) taxonomy names twelve activities, five of them specific to the assistant: verifying suggestions, deferring thought, waiting, prompt crafting and editing the last suggestion (§4, Table 1).

Findings (§6). "Thinking/Verifying Suggestion" is the largest state at 22.4% of session time (sN = 12.97), top for 6 of 21 participants (§6.1). The Copilot-specific states together take 51.5% of session time on average (§6.1); the conclusion summarises that programmers "may spend a large fraction of total session time (34.3%) on just double-checking and editing Copilot suggestions" (§7.3). Programmers often accept first and check later ("deferring thought", 61 labelled states): an accepted suggestion was edited with probability 0.53 if verification was deferred against 0.18 if verified first (§6.3). Accounting for post-acceptance checking raises mean verification time from 3.25 s to 15.21 s ("nearly a five-times increase", §6.4). Suggestions are presented as grey inline text, line by line, and programmers accept them partly to see them with syntax highlighting (§1, §4.2). Acceptance overall was 34.0% (§5.2). Survey: 17 of 21 said they finished faster, 6 of 21 were concerned about code quality (§6.6).

## Relation to the argument

**Premise P8 and the draft's §2 problem statement.** The study measures an inspection cost: when an AI produces output, a large share of the human's time goes to reading and checking it. That supports the draft's point that generative tools hand the person a reading task. It does not test any alternative presentation, and the authors' own design proposals are about timing and grouping suggestions by the user's state (§6.2), not about removing the need to verify.

**Ruling D7.** The "accept now, verify later" pattern is people learning what a suggestion does by running into it, closer to D7's "understand through deciding" than to reading first. The study counts it as a cost (verification debt) rather than a mode of understanding.

**Use in DRAFT_v2:**
- Line 35 ("Text-generation tools impose an output-inspection cost (Mozannar, Bansal, Fourney, & Horvitz, 2024; Simkute et al., 2024)"): supported for code-suggestion tools (verification 22.4% of session time, §6.1; 34.3% on checking and editing, §7.3). Narrower than the sentence: the study is one code assistant, 21 programmers, short lab tasks. The following sentence about "fluent, probabilistically generated text" and "an uninterrupted token stream" is not Mozannar's description; Copilot showed short inline suggestions, often one line at a time (§4.2, Figure 7).
- Line 633 (reference entry): matches Crossref (CHI 2024, pp. 1–16). Not checked against the ACM PDF.
- Line 772 (notes): lists it as unread; it is now read in preprint form.

## In conversation with

- `grundemclaughlin2026overseeing` — later work with Mozannar on overseeing agents; not cited here, but the same research line.
- `bansal2019updates` — earlier Bansal work on human–AI teams; not cited in this paper's references.
- Not in the bib, as leads: Barke, James & Polikarpova (2023) on acceleration and exploration modes; Vaithilingam et al. (2022); Ziegler et al. (2022) on perceived productivity; Peng et al. (2023) on the 55.8% speed-up; Sarkar et al. (2022).

## Caution

Twenty-one employees of one company, eight short tasks, 19 of 21 in Python, self-labelled states (353 segments marked "IDK" and dropped; §5.2), and no condition without Copilot (§5.1). Time is the only cost measured; the authors set aside security and overreliance (§7.1). Read as arXiv v5, not the CHI version of record; section numbers and figures may differ slightly. The preprint is internally inconsistent on one count: §1 says participants "interacted with 1096 suggestions", §5.2 says Copilot showed 1024.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the arXiv v5 text the writer saved (dxd_foundation_local/pdfs/R4/mozannar2024_arxiv.txt and _plain.txt, dated 22 Apr 2024) and checked the section headings against every locator (§4.2, §5.1, §5.2, §6.1–6.4, §6.6, §7.1, §7.3). I checked each number (22.4%, sN = 12.97, top state for 6 of 21; 51.5% across the five Copilot-specific states; 34.3% in the conclusion; 61 deferred states; 0.53 against 0.18; 3.25 s to 15.21 s, "nearly a five-times increase"; 34.0% acceptance of 1024 suggestions; 3137 labels; 353 IDK uses; 17/21 and 6/21; 19 of 21 in Python; August 2022 Copilot; no no-Copilot baseline), the grey-text and syntax-highlighting passage (§4.2), the design proposals (§6.2, grouping suggestions) and the security/overreliance limitation (§7.1). I checked the record against Crossref (CHI 2024, pp. 1–16, four authors) and re-read DRAFT_v2.md lines 35, 633 and 772.

**Findings:**
1. Numbers, quotations and section locators are correct.
2. Fixed: "21 Microsoft programmers ... (about 20 minutes)". The paper says participants came from "our large organization" (Microsoft is inferred from the affiliations), and the tasks were designed to fit a 20-minute block while the mean completion time was 12.23 minutes (§5.1–5.2).
3. Added to Caution: the preprint gives 1096 suggestions in §1 and 1024 in §5.2.
4. Use verdict for line 35 confirmed: an inspection cost is measured for one code assistant; the next sentence's "fluent, probabilistically generated text" and "uninterrupted token stream" do not describe Copilot's short inline suggestions (§4.2) and rest only on Lee et al. (2025) as the draft cites it.

