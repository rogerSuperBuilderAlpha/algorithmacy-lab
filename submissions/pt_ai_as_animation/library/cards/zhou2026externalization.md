---
key: zhou2026externalization
apa: "Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., … Zhang, W. (2026). *Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering* (Version 1) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2604.08224"
authors: "Zhou, Chenyu; Chai, Huacan; Chen, Wenteng; Guo, Zihan; Shan, Rong; Song, Yuanyi; Xu, Tianyi; Yang, Yingxuan; Yu, Aofan; Zhang, Weiming; Zheng, Congming; Zhu, Jiachen; Zheng, Zeyu; Zhang, Zhuosheng; Lou, Xingyu; Zhang, Changwang; Fu, Zhihui; Wang, Jun; Liu, Weiwen; Lin, Jianghao; Zhang, Weinan"
year: 2026
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
venue: "arXiv (cs.SE)"
volume: ""
issue: ""
pages: "54 pp."
doi: "10.48550/arXiv.2604.08224"
url: "https://arxiv.org/abs/2604.08224"
type: preprint
facets: [F8]
claims: [c1, c2]
role: anchor
load: load-bearing
read_depth: partial
object_read: "arXiv v1 PDF (stamp 'arXiv:2604.08224v1 [cs.SE] 9 Apr 2026'; 54 pp., body pp. 1–44, references pp. 45–54) and its text layer zhou2026externalization.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/zhou2026externalization/; record csl.json (doi.org CSL, version 1, CC BY 4.0); read 2026-11-08; sha256 5f06a75d0819795b077bf41fb61a79db9174aa3e024d5a70b7fde4ccff2088a5 (PDF; matches sha256.txt, recomputed with shasum -a 256). Parts read: abstract and contents (pp. 1–3), §1 Introduction (pp. 4–7), §2 Background (pp. 7–11), §6 Harness Engineering whole (pp. 29–35), §7.2 close and §7.3 (pp. 38–39), §8 opening and §8.1 (p. 39), §8.3 close, §8.4–§8.6 and §9 Conclusion (pp. 41–44). Not read: §3 Memory, §4 Skills, §5 Protocols (pp. 11–29), §7.1–§7.2 body (pp. 35–38), §8.2 and most of §8.3 (pp. 40–41), references."
verified: verified
verified_against: "csl.json (21 authors, title, DOI, version 1, licence); PDF sha256 recomputed; text layer, 15 quotations traced, page locators checked against printed page numbers"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Zhou et al. (2026), Externalization in LLM agents

## What it argues

Chenyu Zhou and twenty co-authors (Shanghai Jiao Tong University, with Sun Yat-Sen University, the
Shanghai Innovation Institute, Carnegie Mellon and OPPO) review LLM-agent engineering under one
thesis: agents are now built "less by changing model weights than by reorganizing the runtime around
them". They borrow Donald Norman's idea of the cognitive artifact. An artifact does not amplify an
unchanged inner ability; it changes the task. On their reading, memory turns recall into
recognition, skills turn improvised generation into composition, and protocols turn ad hoc
coordination into structured contracts. The harness is not a fourth module. It is the runtime that
hosts the other three and adds control flow, sandboxing, approval gates, observability, permissions
and context-budget management.

§2 tells the field's history as an outward movement, from capability in weights, to capability in
context (prompting, RAG, ReAct), to capability through infrastructure. The authors end §2 with the
claim that "agent engineering" is becoming "harness engineering": the model stays "the core
reasoning engine" but is no longer "the sole location of intelligence". §6 defines the harness
(explicitly as a synthesis, not a closed definition), lists six design dimensions, and in §6.4
reads the harness through Norman, Kirsh and Hutchins as a "cognitive environment". There the
operative intelligence is distributed across parameters, stores, skills, protocols, tools, monitors
and runtime constraints. §7.3 recasts the question as a partitioning problem: which burdens belong
in the weights and which outside them, by update rate, reuse, auditability and latency. §8 warns
about overhead and security, asks for governance as part of the harness, and argues that
model-centric benchmarks under-measure what the harness contributes. The conclusion: "better agents
are not merely better reasoners. They are better organized cognitive systems."

The authors keep their extended-cognition language pragmatic. In §1 they take from Clark and
Chalmers only "its core engineering insight" and decline "its stronger ontological claims". The
review is a software-engineering synthesis (arXiv cs.SE). It reports no new experiments in the parts
I read.

## What the paper uses it for

- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the anchor, and the fit is
  close. The authors state c1 in engineers' words: a practical agent is "a model operating inside a
  harness", and their harness inventory (sandboxes, cloud execution environments, cost ceilings,
  context budgets) covers Roger's "harnesses, virtual machines, efficiencies" almost item by item.
  §6.2.2 names "a dedicated cloud sandbox" per task, which is the nearest thing in the parts I read
  to Roger's "virtual machines".
- **c2** (model-centrism misplaces where the intelligence sits): strong support with one limit.
  The authors say agency "is therefore not located in the model alone", that intelligence is "no
  longer localized in the model alone", and that the field attributes "to model intelligence what is
  partly an achievement of externalization design". All three are c2 in substance. The limit: they
  disclaim the ontological reading. Their claim is about where reliability and capability come from
  in design, not about what an AI *is*. The paper's c2 (and c12, a claim about what AI is) goes one
  step past them, and should say so.
- **"Harnesses are CS too"** (the rebuttal the sketch's edit aims to defuse; no claim tag): this
  source stocks the objection. The authors file harness engineering under software engineering and
  call it "the broader discipline concerned with constructing the cognitive and operational
  environment". A reader could cite them to say the surrounding work is still computer science. The
  paper's reply has to be that the edit targets model-centrism, not computer science as such; Zhou
  et al. agree with the first and are an instance of the second.

## Loci

Locators: the PDF prints page numbers that match the PDF page count (printed p. n = PDF p. n), so
one number is given. Every quotation was matched against `zhou2026externalization.txt`, the text
layer of the held PDF (sha256 above), with whitespace normalised. Where the authors' text has
double quotation marks inside a quotation, I give them as single quotes.

- "Large language model (LLM) agents are increasingly built less by changing model weights than by reorganizing the runtime around them." — p. 1, Abstract; matched against zhou2026externalization.txt
- "This is not merely a claim about engineering convenience. It is a claim about where reliable agency comes from: not from ever-larger models alone, but from the systematic restructuring of task demands so that internal capabilities and external infrastructure jointly cover the full range of competencies required" — p. 5, §1; matched against zhou2026externalization.txt
- "Many of the largest gains in reliability do not come from changing the base model at all. They come from changing the environment around the model" — p. 5, §1; matched against zhou2026externalization.txt
- "once crucial parts of remembering, guiding action, and coordinating interaction are delegated to external structures, intelligence is no longer localized in the model alone [Clark and Chalmers, 1998]." — p. 6, §1; matched against zhou2026externalization.txt
- "We draw on this tradition for its core engineering insight—that the boundary between 'agent' and 'environment' is a design choice with real performance consequences—rather than committing to its stronger ontological claims." (inner quotes given as single) — p. 6, §1; matched against zhou2026externalization.txt
- "Under this framing, 'agent engineering' increasingly takes the form of 'harness engineering.' The model remains the core reasoning engine, but it is no longer the sole location of intelligence." (inner quotes given as single) — pp. 10–11, §2.3 (the sentence breaks across the page); matched against zhou2026externalization.txt
- "The central claim is that a harness is not merely an implementation convenience layered on top of a capable model." — p. 29, §6 opening; matched against zhou2026externalization.txt
- "Because the concept is still consolidating, the characterization we offer here is best understood as a synthesis of recurring patterns in current systems rather than a closed definition." — p. 30, §6.1; matched against zhou2026externalization.txt
- "A practical agent, on this account, is better understood as a model operating inside a harness than as a model with peripheral capabilities attached." — p. 30, §6.1; matched against zhou2026externalization.txt
- "Agency is therefore not located in the model alone; it emerges from the coupling of the model with the environment that organizes its cognition into action." — p. 30, §6.1; matched against zhou2026externalization.txt
- "The model’s apparent intelligence is thereby altered not only because it has more resources, but because the cognitive workload has been redistributed across artifacts, representations, and procedures outside the model." — p. 34, §6.4; matched against zhou2026externalization.txt
- "The operative intelligence is distributed across model parameters, external memory stores, executable skills, protocol definitions, tool surfaces, monitoring systems, and the runtime constraints that govern their interaction." — p. 35, §6.4; matched against zhou2026externalization.txt
- "The relevant design problem is not whether intelligence should reside in the model or in the infrastructure." — p. 38, §7.3; matched against zhou2026externalization.txt
- "Until such methods mature, the field will continue to attribute to model intelligence what is partly an achievement of externalization design." — pp. 43–44, §8.6 (the sentence breaks across the page); matched against zhou2026externalization.txt
- "On that view, better agents are not merely better reasoners. They are better organized cognitive systems." — p. 44, §9; matched against zhou2026externalization.txt

## Caution

- **Version.** This is arXiv v1, a preprint with no peer-reviewed version of record in the local
  records. The arXiv stamp reads 9 Apr 2026; the title page prints "Date: April 10, 2026"; csl.json
  carries only the year 2026 and "version": "1". Cite as v1 and check for later versions before S8.
- **Authors.** csl.json lists 21 authors in the order given above, matching the PDF byline. APA 7
  lists the first 19, an ellipsis, then the last (Weinan Zhang). Two authors share the
  abbreviation "Zhang, W." (Weiming, 10th; Weinan, 21st); the PDF marks Weinan Zhang as a
  corresponding author. Equal-contribution and corresponding-author marks are on the PDF byline,
  not in the record.
- **Depth.** Partial, not full text. I did not read §3–§5 (memory, skills, protocols) or §7.1. The
  paper's uses rest on §1, §2, §6 and §9, which I read whole. A verifier should not cite the card
  for anything in the module chapters.
- **Their stance on ontology.** The authors explicitly decline the stronger extended-cognition claim
  (p. 6). A citation that makes them say the AI *is* the system around the model overstates them.
- **The "virtual machines" match** is mine: the parts I read speak of sandboxes, cloud sandboxes,
  filesystem snapshots and isolation, not of virtual machines by that name.
- **Homonym in the registry.** `spaces/zhou2026check` (10.1145/3772318.3790655, "When should users
  check…") is a different work by a different Zhou; no collision with this key.
- **Figures** (1, 2, 3, 7, 8) are images; the text layer holds only their captions. Nothing on the
  card rests on figure content beyond the captions.

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 2
- verdict: verified. Frontmatter matches csl.json: 21 authors in byline order, title, DOI, arXiv URL, version 1. The APA line's 19 names, ellipsis and last author are right. The PDF has 54 pages and its sha256 matches sha256.txt. All 15 quotations are verbatim in the text layer, and every page locator matches the printed page number. The two quotations marked as breaking across a page (pp. 10–11, pp. 43–44) do run across the printed page break. The section numbers (§2.3, §6.1, §6.2.2, §6.4, §7.3, §8.6, §9) match the contents list. `partial` is honest: the card lists the parts read and the parts skipped. DECISIONS predicted full_text.
- checked: csl.json; the PDF byline (21 names; affiliations Shanghai Jiao Tong, Sun Yat-Sen, Shanghai Innovation Institute, Carnegie Mellon, OPPO; Weinan Zhang one of four corresponding authors); "Date: April 10, 2026" on the title page; paraphrased phrases in the first two sections ("a dedicated cloud sandbox", "the broader discipline concerned with constructing…", "cost ceilings", "context budget"); no "virtual machine" in the text, as the card says. The c2 stretch (the authors decline the ontological reading, p. 6) is named on the card.
- for Fable: the card sets `status: cited`, but neither SOURCE.md nor SKETCH.md names Zhou et al. Under the README definition the status would be `candidate`. Many cards in this run use `cited` for works DECISIONS approved, so I left the field alone; the author decides.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index**.
- Checked: 15/15 loci found in zhou2026externalization.txt (three differ only by a printed page number falling inside the sentence or by the card's single-for-double inner quotation marks, both declared in the Loci preamble); PDF sha256 recomputed, matches; pdfinfo 54 pp.; arXiv stamp 'arXiv:2604.08224v1 [cs.SE] 9 Apr 2026' and 'Date: April 10, 2026' on p. 1; csl.json: 21 authors, version 1, copyright 'Creative Commons Attribution 4.0 International', DOI, arXiv URL; read_depth partial matches the parts listed; the c2 stretch (the authors decline the ontological reading) is named.
- Changed: nothing
- For the author: status `cited` though neither SOURCE.md nor SKETCH.md names Zhou et al. (the S6 verifier raised this too); decide `cited` vs `candidate`
