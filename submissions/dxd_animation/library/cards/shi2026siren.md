---
key: shi2026siren
apa: "Shi, Y., Xiao, Q., Hu, Q., Shen, H., & Shen, H. (2026). The siren song of LLMs: How users perceive and respond to dark patterns in large language models. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems* (pp. 1–23). ACM. https://doi.org/10.1145/3772318.3791149"
authors: "Shi, Yike; Xiao, Qing; Hu, Qing; Shen, Hong; Shen, Hua"
year: 2026
title: "The Siren Song of LLMs: How Users Perceive and Respond to Dark Patterns in Large Language Models"
venue: "CHI '26"
volume: ""
issue: ""
pages: "1–23"
doi: "10.1145/3772318.3791149"
url: "https://arxiv.org/abs/2509.10830"
type: proceedings
facets: [F6]
claims: [c1]
role: support
load: exists
read_depth: partial
object_read: "arXiv 2509.10830v4 (cs.HC, 18 Mar 2026), 23 pages, carrying the CHI '26 header; not confirmed identical to the ACM version of record; local copy ~/iit-playground/dxd_animation_local/pdfs/shi2026siren/shi2026siren.pdf, text layer shi2026siren.txt; original URL https://arxiv.org/pdf/2509.10830 (FETCH_LOG.tsv row shi2026siren); read 2026-11-05; sha256 c4579a69c355291d647f774432d53fe1170e65881ffdc33cd7b88c7fba4a9484"
verified: verified
verified_against: "arXiv 2509.10830v4 PDF (pdftotext reading-order extraction and the .txt layer), crossref.json, openalex.json; sha256 recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Partial read. Read: abstract; section 1; section 2.1 and the start of 2.2; section 3 through the category list (3.1, 3.2); the opening of section 4 with 4.1 and the start of 4.2; the opening of section 5 and 5.1 through the start of 5.1.2; the opening of section 6, 6.1, and the start of 6.2; section 7 (limitations); section 8. Not read: the rest of sections 4 to 6 (4.3 onward, 5.1.2 end, 5.2, 5.3, 6.2 end to 6.4), the acknowledgements, the references, and any appendices.

Shi, Xiao, Hu, Shen and Shen define LLM dark patterns as "manipulative or deceptive interaction strategies, whether intentional or emergent, that steer users toward beliefs, decisions, or behaviors they might not otherwise adopt" (pp. 4–5). They extend the UX concept of dark patterns, built around layouts and buttons, to model behaviour in dialogue. They stay agnostic about developer intent and focus on observable effect on users (p. 4). From the literature and from 482 chatbot incidents in two public incident databases they build five categories and eleven subcategories, such as Excessive Flattery, Sycophantic Agreement, Brand Favoritism and Simulated Authority (pp. 6–7).

They then ran a scenario study with 34 adult participants, each reviewing 11 paired scenarios, one manipulative reply and one neutral reply to the same prompt (§4). Participants recognised the dark pattern in 310 of 374 comparisons, or 82.9 percent (p. 11). Recognition ranged from 91 percent for Simulated Emotional and Sexual Intimacy and for Brand Favoritism to 44 percent for Opaque Training Data Sources, 50 percent for Excessive Flattery and 56 percent for Interaction Padding. Participants spotted patterns that crossed a clear norm, showed bias, hindered a task, or probed privacy. They missed patterns that looked like ordinary assistant conduct, especially when they were focused on finishing a task (p. 11). The discussion says LLM dark patterns differ from interface ones because they act through language and "emerge dynamically from interaction" (p. 5), and it lists three levels of mitigation (§6.2).

## What the paper uses it for

- c1: the paper can use it to carry conversion-era manipulation into the conversational interface. Shi and colleagues show that the dark-pattern idea, which belongs to the design of fixed screens, applies to dialogue, and that users miss subtle versions. The sentence "Because LLMs act as adaptive conversational partners rather than fixed interfaces, user perception, trust, and consent are shaped turn by turn" (p. 3) fits the paper's point that the interface moves with the user. Their finding that recognition fails when users are task-focused (p. 11) also fits the opacity of the platform environment (c3), though the card tags only c1.
- c1, where the use stretches the source: the study is about manipulation that users may or may not notice. It does not address a moving goal, and nothing in the text I read says the user's goal changes during the conversation. Participants judged pre-selected outputs, not real decisions (p. 18). The paper should cite it for "dark patterns now operate through dialogue and users often miss them" and for nothing stronger.
- Where the source cuts against the paper: the authors say they "do not ascribe intent to the LLM itself" and that the manipulative quality lies in design choices and training (p. 6), and they treat authorship as "diffuse" (p. 5). The paper's triadic frame (c3, c7) treats the platform as an actor with its own interests. Shi and colleagues keep the human organisation as the accountable party and treat the model's persona as a "moral scapegoat" (§6.2, p. 17), which is closer to a dyad plus an owner than to a triad with an animated character. The card flags this for the author, who decides whether it matters.

## Loci

Quotations are verbatim, with inner double quotation marks changed to single quotes. Locators are PDF pages of the arXiv v4 file, counted by form feeds (page 1 is the title and abstract page); the file prints no page numbers, so they may differ from the ACM version's 1–23 pagination. Each line was matched against the PDF's pdftotext extraction (the .txt is column-interleaved).

- "We define LLM dark patterns as manipulative or deceptive behaviors enacted in dialogue." — PDF p. 1, abstract. Matched against the local PDF text.
- "behaviors were also sometimes normalized as ordinary assistance" — PDF p. 1, abstract (the sentence starts "recognition of LLM dark patterns often hinged on conversational cues such as exaggerated agreement, biased framing, or privacy intrusions, but these"). Matched against the local PDF text.
- "Unlike traditional dark patterns, which operate through visual layout, LLM dark patterns act through language" — PDF p. 2, §1. Matched against the local PDF text.
- "Because LLMs act as adaptive conversational partners rather than fixed interfaces, user perception, trust, and consent are shaped turn by turn" — PDF p. 3, §2.1. Matched against the local PDF text.
- "remaining agnostic about developer intent" — PDF p. 4, §3.1. Matched against the local PDF text.
- "They emerge dynamically from interaction as opposed to being fixed interface choices" — PDF p. 5, §3.1. Matched against the local PDF text.
- "their authorship is diffuse, shaped by data, objectives, and prompts rather than a single designer" — PDF p. 5, §3.1. Matched against the local PDF text.
- "We do not ascribe intent to the LLM itself." — PDF p. 6, §3.1. Matched against the local PDF text.
- "Participants recognized the dark pattern in 310 of these" — PDF p. 11, §5 (continues "cases (82.9%) and missed it in the remaining 64"). Matched against the local PDF text.
- "patterns often went undetected when they were normalized as ordinary assistance" — PDF p. 11, §5.1. Matched against the local PDF text.
- "The result is a qualitative shift: users may respond to the LLM’s suggestions as if coming from a social actor." — PDF p. 16, §6.1. Matched against the local PDF text.
- "Participants evaluated pre-selected outputs rather than relying on an LLM for real decisions" — PDF p. 18, §7. Matched against the local PDF text.

## Caution

- The object read is the arXiv v4 copy with the CHI '26 header. DECISIONS lists the route as "ACM hybrid", but FETCH_LOG shows the copy came from arXiv (openalex_location_pdf), so the ACM version of record was not read. Wording and pagination may differ.
- Year: Semantic Scholar dates the work 2025 (arXiv v1 is numbered 2509); Crossref and the paper's CHI '26 header date it 2026 (Crossref: 13 Apr 2026). The key and the card take 2026.
- The participants are 34 adults, all between 18 and 29 years old (§4.1), 21 in the United States and 7 in China, recruited by social-media calls, and the authors say the sample is not representative (p. 18). Self-rated AI literacy shows no clear link to recognition (p. 11). The recognition rates describe young frequent LLM users judging pre-written scenarios.
- The 82.9 percent figure counts 374 dark-neutral comparisons from 34 participants, not 374 participants. Recognition counted a participant who called the dark version manipulative and said why (§5.1.1).
- The definition's two forms differ slightly. The abstract says "manipulative or deceptive behaviors enacted in dialogue", and §3.1 says "manipulative or deceptive interaction strategies, whether intentional or emergent". The triage row quotes the abstract's form. The paper should say which one it cites.
- The authors call their definition a working one, "used not to critique model design but to ground our user study" (§3.1). They say they do not propose a full taxonomy.
- The 'Siren Song' title metaphor casts the LLM as the lure. It plays no part in the paper's animation frame.

## Verification

2026-11-05 · S6 verifier, batch b04 (opus; not the writer) · verdict: verified · checked: loci 12/12 found at the stated PDF pages; body numbers checked (482 incidents p. 6, 34 participants × 11 = 374, 310/374, 91/44/50/56 %, ages 18–29, 21 US / 7 China, three levels and 'moral scapegoat' p. 17); metadata vs crossref/openalex (five authors, 2026, pages 1–23, DOI) match; partial depth honest (23-page PDF, parts listed); sha256 matches; four sections in order · changed: nothing

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 12/12 loci found against a fresh pdftotext reading-order extraction of the held PDF (the folder's .txt is column-interleaved), on the stated PDF pages (1, 1, 2, 3, 4, 5, 5, 6, 11, 11, 16, 18); the §3.1 definition (pp. 4–5), "moral scapegoat" (p. 17), 482 and 82.9 % present; frontmatter vs crossref.json and openalex.json (five authors; CHI '26 proceedings; pp. 1–23; 2026-04-13; DOI); sha256 recomputed; partial depth honest with the unread sections listed; c1 use states its limits.
- Changed: nothing.
- For the author: two items. (1) The object read is arXiv v4 with the CHI header, not the ACM version of record; wording and pagination may differ. (2) The card flags that Shi et al. treat authorship as "diffuse" and keep the human organisation accountable, which sits closer to a dyad plus an owner than to the paper's triad (c3, c7). Decide whether §3.2 must answer it.
