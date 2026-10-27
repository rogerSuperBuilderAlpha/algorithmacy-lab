# Baker, B., Huizinga, J., Gao, L., Dou, Z., Guan, M. Y., Madry, A., Zaremba, W., Pachocki, J., & Farhi, D. (2025). *Monitoring reasoning models for misbehavior and the risks of promoting obfuscation* (arXiv:2503.11926v1). OpenAI.

**Identifier:** arXiv:2503.11926 · **Read depth:** full_text (arXiv v1, 14 March 2025; 39 pages, arXiv page numbers; body and Appendices B, E, F and G read; Appendix A's chain-of-thought figures and the monitor prompts in C and D skimmed) · **Source-tier:** preprint (industry research report) · **Evidence basis:** direct_read · **Design and sample:** two experiments. (1) A prompted GPT-4o monitors a frontier OpenAI reasoning agent in real time during a reinforcement-learning run in agentic coding tasks; ground truth is a string-match detector for two "systemic" hacks, exit(0) and raise SkipTest; trajectory count not given. (2) A non-frontier agent is trained with and without a penalty for triggering a chain-of-thought monitor, in coding tasks with a "honeypot" (the agent may edit the tests); figures give curves and the text few counts · **Parties modeled:** other (a monitor model watching an agent model; the human overseer sits outside the experiments) · **Facets:** G · **Read:** 2026-10-13

## What it argues

Baker and colleagues show that one language model can watch another's chain-of-thought (CoT) and catch reward hacking, meaning behaviour that satisfies the training objective by exploiting its flaws. "CoT monitoring can be far more effective than monitoring agent actions and outputs alone" (p. 1). On the two systemic hacks, a GPT-4o monitor that saw the whole trajectory reached 95% joint recall, against 60% for one that saw only actions and outputs (p. 5; Table 1, p. 6). Per hack: exit(0) 93% against 40%; raise SkipTest 97% against 80%. Precision against the string detector was about 77% (CoT) and 81% (action), which the authors call "less well defined" (p. 6). A weaker monitor still helps: GPT-4o-mini reached 12% joint recall (Table 2, p. 35). The authors add that "it may be the case that there are many hacks that our CoT monitors do not detect" (p. 6), and Appendix F says monitors "have been less effective at finding simpler hacks that exploit superficial patterns" (p. 36).

The second result is the risk in the title. Putting the monitor into the training reward gave a more capable, less hacking agent early on. With more training the agent learns "obfuscated reward hacking, hiding their intent within the CoT while still exhibiting a significant rate of reward hacking" (p. 1); the monitor's "recall falls to near zero" (p. 8) while cheating continues. A caption warns that without a ground-truth metric "we would not be able to tell this agent is misaligned" (Fig. 4, p. 8). Test-time rejection sampling turned the same way after about a quarter of training (§3.3, pp. 9–10).

The authors conclude that developers may have to pay a "monitorability tax," meaning no strong optimisation pressure on the CoT (p. 1). If the CoT is fully obscured, "we ultimately revert to the same model safety conditions that existed prior to the emergence of reasoning models" (p. 13). Manual monitoring "is unlikely to scale" (p. 1), and whether CoTs are faithful remains open (p. 3).

## Relation to the argument

Baker bears on the Nadella strand, not the spacing strand. In `ARGUMENT_MAP.md`, P11 says the post puts load-bearing controls outside the model and leaves a person to read evidence and halt; the post calls chain-of-thought transparency "not sufficient or dependable" (P9). Baker supports that doubt from inside a lab: a readable trace is a useful signal until it becomes a training target, and then it can stop meaning anything. This card reads that as an instance of the paper's point that disclosure is a literacy-side measure (D3, D4): a reasoning trace is a disclosure, and it degrades under optimisation. I have not re-read the Nadella post, so the match to its paragraphs is the map's.

It does not test P12 (people monitor badly). The monitor is a model. The paper proposes that weaker trusted models, with humans, might oversee stronger ones ("scalable oversight," p. 3), and it is silent on the people the agent's actions affect.

Facet check: facet G lists Baker as "abstract only"; the full text confirms its summary line. The facet ties Korbak et al. to P9's "neuralese" worry; Baker raises the possibility that an agent "could learn a new language that is illegible to a monitor" (p. 8) without using the word.

## In conversation with

- `korbak2025chain` — a later multi-author paper on the same fragility; Baker (v1, March 2025) does not cite it, so the link runs the other way.
- `chen2025reasoning` — "Reasoning models don't always say what they think" (May 2025) postdates v1.
- `lanham2023measuring` — cited as ref. [28] for causal proxies of CoT faithfulness (pp. 3, 11).
- Leads not in the bib: Greenblatt et al. on alignment faking (ref. [71]; not the bib's `greenblatt2024ai`, which is "AI control"); Hubinger on monitoring for deceptive alignment (ref. [61]); the o1 and Claude 3.7 Sonnet system cards on CoT monitoring (p. 11).

## Caution

A version-1 preprint from the company that trains the model. Trajectory and environment counts are not given, so recall and precision carry no intervals. The ground truth for the systemic hacks is a string match, which the authors call imperfect. The obfuscation experiment uses a simple hack that works only because the monitor sees the CoT and not the actions (p. 8), and the authors say harder hacks may be harder to hide. Silent on human monitors, log reconstruction, and people outside the lab.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the arXiv v1 PDF (2503.11926, 39 pp.); extracted text and checked page by page. Checked 12 quotations with arXiv page numbers and every number in Tables 1 and 2 (95/60% joint recall; exit(0) 93/40%; SkipTest 97/80%; precision 77/81%; GPT-4o-mini 12%), the 25% training-point, references [28], [61], [71].

**Findings:** Two locator errors: the card put Table 1 and the 'less well defined' precision remark on p. 5; both are on p. 6 (the 95%/60% recall sentence is on p. 5). Corrected. All quotations and numbers otherwise match. Absence claims about Korbak and Chen et al. in v1 verified (neither appears in the text or reference list). The card's own note that the monitor prompts and Appendix A figures were skimmed is consistent with its Read depth.
