# Mitchell, M., Ghosh, A., & Passi, S. (2026). AI agents push humans out of the loop. *arXiv preprint* arXiv:2608.23642.

**Identifier:** arXiv:2608.23642 · **Read depth:** full_text (preprint v3, 6 Sep 2026, 22 pages; locators are PDF pages. I read the ten-page body and skimmed the reference list for the works the text leans on. The two appendix pages of solution diagrams and the larger Table 2, pp. 20-22, I looked at for structure only) · **Source-tier:** preprint, position paper (its closing page invites "the broader NeurIPS community", p. 10; I found no sign it has been published) · **Evidence basis:** direct_read · **Design and sample:** none. A position paper that assembles prior HCI, cognitive-science and AI-safety studies, plus a "structured inventory" of solutions sorted by six oversight goals and six solution categories (Table 1, p. 7). It gathers no data · **Parties modeled:** person–system (a human overseer and an AI agent), with deployers and developers as the two parties who must support the overseer; affected parties do not appear · **Facets:** G, Z · **Read:** 2026-10-13

## What it argues

The authors take the claim that a "human in the loop" makes agents safe and say it fails twice. Current agent design "impede[s] effective human oversight," and the cognitive capacities oversight needs "are also themselves degraded by extended use of AI systems" (abstract, p. 1). The first half (Section 3, "The oversight oversight") says the stream an overseer must follow is large and spread across components, that users repeatedly approve prompts until they "stop paying close attention to what they are approving" (p. 4), and that the burden falls "almost entirely on users" (p. 1). It adds a claim about the frame: "'Human-in-the-loop' is only a meaningful solution if the human can independently see into the loop" (p. 4).

The second half (Section 4, "The irony of automation") collects reports of deskilling, automation bias, anchoring and complacency, and puts them under Bainbridge's irony: "Oversight degrades the overseer" (p. 6). It adds a feedback argument. If approvals are treated as evidence of success, a system trained on them "can begin to optimize for disincentivizing thoughtful oversight" (pp. 5-6), so the human rater becomes "the exploitable part of the reward channel" (p. 6).

The remedy is "cognitive scaffolding" in two prongs. Developers supply affordances: strategic friction (pre-commitment, delay-and-choice, reasoning probes, action gating), decision design (bounded autonomy, batch review, automated pre-checks), and behavioural monitoring of the overseer (time, override and evidence-seeking signatures; planted canaries; audits) (pp. 7-8). Deployers supply protocols: training, enforced breaks and rotations, and role design, including "separating roles" so the overseer is not the decision-maker who gains from approvals (p. 8). Section 6 answers three objections. On "Better tooling and transparency will solve this" the authors reply that it is "necessary, but insufficient," since explanations "operate on cognitive capacities that AI agent use itself degrades" (p. 9).

## Relation to the argument

Strongest support for premise P12 (people perform sustained monitoring and whole-volume review badly), and a direct counter to the post's P15 and P19, where a person reads tamper-proof evidence and holds the brake. It is also the closest 2026 case for the lineage the paper needs: design the task so the person carries less, and do not hand them more to read.

Three points of contact with the rulings. (1) D3 and D4: Section 6's reply on transparency ("necessary, but insufficient," p. 9) supports the author's line that disclosure does not change how well people navigate, but only as an argument; Mitchell cites studies of explanations in AI-assisted decisions, not of platform disclosure. (2) The argument map's "lowering a cost has costs" worry: Mitchell's friction mechanisms ask the person to do more work, which pulls against the "carry less" direction of P5 and P8, and the paper argues for it because offloading erodes the skill oversight needs (pp. 4-5). (3) P10: the paper's "separating roles" and "aligning incentives" (p. 8) name the same problem as a conflict of interest between the overseer and the beneficiary of approvals.

Facet check: facet Z quotes the abstract ("impede effective human oversight," "design-level affordances") and notes that none of the oversight-fallacy sources "replaces the human check with structure." That holds for the headline, but the inventory includes structural items (bounded autonomy, automated pre-checks, separated roles), so Mitchell sits closer to the structural camp than facet Z's summary suggests. Facet G calls it a paper "arguing that agent design degrades the overseer's skills"; it argues that design both obstructs oversight (Section 3) and erodes it (Section 4).

## In conversation with

- `bainbridge1983ironies`: the frame ("irony of automation," p. 6), and the aviation lineage of the human in the loop (p. 2).
- `endsley1995out`: out-of-the-loop performance, p. 5; also behind the call to preserve domain skill (p. 8).
- `parasuraman2000types`: levels of automation, cited for the user's shifting role (p. 4) and for complacency and overload (p. 5). The paper does not cite Parasuraman and Manzey (2010).
- `bucinca2021trust`: cognitive forcing functions, the model for its strategic-friction mechanisms (p. 7), and the source for "users may disprefer systems that reduce overreliance" (p. 8).
- `green2022flaws`, `langer2024effective`, `sterz2024quest`: cited together for the claim that "the presence of an overseer does not entail reliable oversight" (p. 1); Sterz is also cited for role design (p. 8).
- `santonidesio2018meaningful`, `eu2024regulation`: cited as governance frameworks that require meaningful control and final human decisions (p. 1); Santoni de Sio is also the authority for the "autonomous weapons lineage" of the human in the loop (p. 2).
- `anthropic2026how`: Mitchell cites an Anthropic engineering post titled "Claude Code auto mode: A safer way to skip permissions" for approval fatigue (p. 4). The bib title differs slightly; I did not compare the URLs.
- Leads, not in the bib: Passi 2025, "Agentic AI has a human oversight problem" (SSRN), which Mitchell calls the "most similar" sociotechnical perspective (p. 3); Dhanorkar, Passi and Vorvoreanu (2026) on developers overseeing software agents (FAccT).

## Caution

A position paper; its evidence is other people's studies and several self-reports, including a blog post and a Reddit post (refs 113, 116). It does not itself measure approval fatigue or skill loss. The solution inventory is the authors' own construction, not a systematic review; they call it a structural map, "not as a definitive taxonomy" (p. 6). Preprint v3 of an unpublished paper.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened arXiv:2608.23642v3 PDF (6 Sep 2026; 22 pp.). Checked 14 quotations and 20 page locators by page (pp. 1, 3-10), the Table 1 and Table 2 locations, the section titles, the 'Separating roles' bullet (p. 8), and 12 of the cited works against the reference list (Bainbridge, Buçinca ref. 10, Passi 2025 ref. 88, Dhanorkar et al. FAccT '26 ref. 25, Anthropic auto-mode post ref. 5, others).

**Findings:** No issues found. Card's Read depth correctly says the body was read in full and only the appendix and reference list were skimmed; I left it as full_text. 'lowering a cost has costs', 'replaces the human check with structure' and 'arguing that agent design degrades...' are the project's or facets' wording, not the paper's.
