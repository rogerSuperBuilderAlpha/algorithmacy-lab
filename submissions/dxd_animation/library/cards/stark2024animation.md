---
key: stark2024animation
apa: "Stark, L. (2024). Animation and artificial intelligence. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency* (pp. 1663–1671). ACM. https://doi.org/10.1145/3630106.3658995"
authors: "Stark, Luke"
year: 2024
title: "Animation and Artificial Intelligence"
venue: "FAccT '24"
volume: ""
issue: ""
pages: "1663–1671"
doi: "10.1145/3630106.3658995"
url: ""
type: proceedings
facets: [F1, F3, G]
claims: [c4, c6, c7]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "FAccT '24 open proceedings PDF (9 pp.; its first page states a Creative Commons Attribution-NonCommercial 4.0 licence) and its text layer stark2024animation.txt, at ~/iit-playground/dxd_animation_local/pdfs/stark2024animation/; original https://facctconference.org/static/papers24/facct24-110.pdf (provenance.txt); read in full 2026-11-05; sha256 a2c6e94ef3e31ad92cd6d06119c24ddb51fd9f61035aad5aba1fd5e2e4b87101 (PDF, recomputed with shasum -a 256; matches provenance.txt)"
verified: verified
verified_against: "stark2024animation.txt (column-split, all 9 pages), the PDF first page (title, author, DOI, ACM reference line, licence), provenance.txt; pp. 1663–1671 only via the reference list of maeda2025anthropomorphism.txt p. 1671 (no Crossref record in the folder); sha256 recomputed"
prior_cards: []
status: cited
added: 2026-11-05
run: dxda-lib-2026-11
---

# L. Stark (2024), Animation and artificial intelligence

## What it argues

Luke Stark argues that ChatGPT and similar LLM chatbots are best understood as animated characters, and
that the same holds for "any artificial intelligence system designed to interact with human beings". He
takes his definition of animation from the anthropologist Teri Silvio: the projection of qualities perceived
as human "outside of the self, and into the sensory environment". Silvio sets animation against performance.
A performer embodies one role and invites an introjective bond. An animated character shows a "numerical
disjunct" between the character and the people who make it move. Stark then borrows Philip Agre's "grammar
of action" to name the mechanism: an LLM lays a computational grammar over natural language, and RLHF tunes
it towards human preferences. The result, in his words, is "a persuasive, sophisticated textual animation"
and not a quasi-sentient being.

His §3 draws out three facets of the frame. First, labour (§3.1): many hands animate a chatbot. OpenAI's
staff, RLHF raters, low-paid Kenyan moderators and every author of the training text all count, and the
user counts too, as "the final uncompensated animator". The character's charm pushes this labour offstage.
Second, inference (§3.2): animation is a "conjectural" medium that leans on stereotypes, and generative AI
is "inferential AI" that risks reifying them. Third, introjection (§3.3): interactive characters add
"synthetic introjection", but only the human changes, so influence runs one way, from the creators through
the character to the audience. On this reading the chatbot works as an attention trap akin to a
recommender. Stark's §4 turns to governance: consumer-protection law on unfair or deceptive animation, bot
disclosure, and a speculative "AI iconoclasm" that would ask whether design meant to encourage projection
is ever ethical. His conclusion calls for research on where AI systems sit "on the continuum between
performance and animation". The paper is conceptual. It runs no study, and its design consequences stop at
regulation.

## What the paper uses it for

- **c4** (an LLM interface is an animation): the anchor, and the use fits. Stark states c4 outright for
  chatbots and extends it to all interactive AI. SOURCE.md Pass 2 says Stark "demonstrates" the claim.
  Stark himself speaks of arguing and of a goal "to demonstrate the utility of such a frame", so CHECK F2's
  "argues" matches his framing of the claim itself. SOURCE's paraphrase of Silvio ("onto non-human
  objects") echoes Stark's own abstract ("onto objects in the environment") more closely than Silvio's
  definition as Stark quotes it ("into the sensory environment").
- **c6** (animation is co-optive; the user also animates): Stark supports the second layer directly. The
  user's prompts help populate the instance, and prompt engineering is "a labor of textual projection". His
  co-optation is attentional and emotional (enthralment, the attention trap), not perceptual. He says
  nothing about frames, thresholds or apparent motion, so the "lock in" half of c6 needs other sources.
  His one-way "chain of influence" also sits in tension with the user-as-animator layer: the user supplies
  labour but, in his account, does not change the character's creators.
- **c7** (animation is triadic): Stark supplies the structure the paper wants. The creators act through the
  character on the audience, and their labour stays offstage. But his animators are many: staff, raters,
  moderators, authors and the user. The paper's singular "unseen 'animator'" stretches him. The paper can
  read "animator" as a role filled by many parties, or concede the plurality (see
  `maeda2025anthropomorphism`). He also quotes Silvio's concession that performance and animation are
  "[hard] to separate", which CHECK F4 asks the paper to concede.
- **c5** (opacity, missing frames): no support. Stark's opacity is the "obfuscation of human labor", the
  hidden animators, not missing frames. A use for c5 would stretch him.
- **c8** (apply the animator's methods): Stark cuts against it in part. He sends his reader to existing HCI
  and design-values work, but his own proposals are governance, and his "AI iconoclasm" questions design
  that encourages projection. The paper must say why DXD's use of the animator's craft does not deepen the
  projection Stark worries about.
- **c9** (gap): Stark is the nearest prior on the first half of the argument (G verdict). He says the frame
  "lays ground for a new framework to conceptualize the design and regulation" of interactive AI, but he
  develops only the regulation side. Nothing here concerns decisions or decision design.

## Loci

Locators: the held copy prints no page numbers. "PDF p." counts pages by form feeds in the text layer.
The proceedings page in brackets is inferred from the range 1663–1671 (see Caution). Section numbers are the
printed headings. Every quotation was matched against `stark2024animation.txt`, the text layer of the held
PDF (sha256 above). Where Stark's text has double quotation marks inside a quotation, I give them as single
quotes.

- "In this paper, I argue ChatGPT and similar chatbots powered by Large Language Models (LLMs) can be best understood as animated characters." — PDF p. 1 [p. 1663], Abstract; matched against stark2024animation.txt
- "Characteristics of animation—including reliance on stereotypes, obfuscation of human labor, and manipulation of an audience’s emotions—can help us both analyze and respond appropriately to interactive AI technologies and the hyperbolic claims of their promoters." — PDF p. 1 [p. 1663], Abstract; matched against stark2024animation.txt
- "my goal in this work is to demonstrate the utility of such a frame for AI practitioners, policymakers, and citizens in general" — PDF p. 1 [p. 1663], §1; matched against stark2024animation.txt
- "lays ground for a new framework to conceptualize the design and regulation of interactive AI systems more generally." — PDF p. 1 [p. 1663], §1; matched against stark2024animation.txt
- "as, in Silvio’s words, a '‘structuring trope’ for understanding the relationship between digital technologies, creative industries, and our lived experience of mediation' [88:422]" (Stark's outer double quotes given as single; the inner curly single quotes are his) — PDF p. 2 [p. 1664], §1; matched against stark2024animation.txt
- "Silvio defines animation is a genre of human expression: 'the projection of qualities perceived as human—life, power, agency, will, personality, and so on—outside of the self, and into the sensory environment, through acts of creation, perception, and interaction' [89:52]." (Stark's "defines animation is" as printed; inner quotes given as single) — PDF p. 2 [p. 1664], §2; matched against stark2024animation.txt
- "Animated characters often possess a numerical disjunct between their characterization and the number of human agents involved in the creation or manipulation: one puppeteer might control multiple marionettes, or many humans might work in coordination to animate a Chinese dragon puppet." — PDF p. 2 [p. 1664], §2; matched against stark2024animation.txt
- "The so-called 'ELIZA effect,' or 'the tendency for people to treat programs that respond to them as if they had more intelligence than they really do' has been a staple of animation and virtual agent development since Weizenbaum’s initial experiments" (inner quotes given as single) — PDF p. 3 [p. 1665], §2.1; matched against stark2024animation.txt
- "a persuasive, sophisticated textual animation—but an animation nonetheless and not, hyperbolic claims to the contrary, a quasi-sentient being." — PDF p. 3 [p. 1665], §2.1; matched against stark2024animation.txt
- "Animated characters (be they Chinese dragon puppets, Disney films, or chatbots) are typified by the distributed agency of their creation and enlivenment." — PDF p. 4 [p. 1666], §3.1; matched against stark2024animation.txt
- "The appeal and charisma of the animated character itself often pushes the actual living labor of their animators into the background or offstage [74]." — PDF p. 4 [p. 1666], §3.1; matched against stark2024animation.txt
- "ChatGPT’s host of animators include not only OpenAI’s technical staff, but also any humans participating in RLHF training, including the low-paid Kenyan content moderators contracted by the company" — PDF p. 5 [p. 1667], §3.1; matched against stark2024animation.txt
- "The final uncompensated animator of any particular ChatGPT instance is the individual human user interacting with the system. It is, after all, a user’s prompts that help populate an instance in the first place." — PDF p. 5 [p. 1667], §3.1; matched against stark2024animation.txt
- "'prompt engineering,' or the crafting of text queries to optimize an LLM’s output, is a labor of textual projection" (inner quotes given as single) — PDF p. 5 [p. 1667], §3.1; matched against stark2024animation.txt
- "in the case of interactive animated agents, only the human actor is reflexively changing their perspective based on the actions of the animated entity. As such, the chain of influence is only one-way, from the creators of the animated character through it to the responses and self-conceptualization of the audience." — PDF p. 6 [p. 1668], §3.3; matched against stark2024animation.txt
- "Indeed, interactive AI agents could be understood as a form of attention trap akin to contemporary content recommender systems [84]." — PDF p. 6 [p. 1668], §3.3; matched against stark2024animation.txt
- "Silvio observes that, 'in practice, performance and animation are [hard] to separate' [88:432]." (inner quotes given as single; the bracket is Stark's) — PDF p. 6 [p. 1668], §3.3; matched against stark2024animation.txt
- "whether design measures intended to encourage the projection of human attributes onto an AI system might be deemed unethical in some contexts." — PDF p. 7 [p. 1669], §4; matched against stark2024animation.txt
- "More research is needed to distinguish where and how various different types and examples of AI systems sit on the continuum between performance and animation" — PDF p. 7 [p. 1669], §5; matched against stark2024animation.txt

## Caution

- **Pagination.** The held copy prints no page numbers, only "9 pages" in its ACM reference line. No Crossref
  record sits in the local folder. I took the range 1663–1671 from the reference list of Maeda & L. Stark
  (2025, p. 1671), which I read this run. It fits nine pages, so PDF p. n = p. 1662 + n. S6 should confirm
  the range on the Crossref record for 10.1145/3630106.3658995.
- **CHECK.md "Verified as written"** places the "structuring trope" quotation at Stark p. 1663. The held copy
  prints it on PDF p. 2, which is p. 1664. CHECK's other Stark loci (traits p. 1663; Silvio's definition and
  the numerical disjunct p. 1664; the user as animator p. 1667; "hard to separate" p. 1668) match. CHECK.md
  is left alone.
- **OUTLINE §4.2 and triage F3-F4.md** (row 1 and the note at line 165) tie "the ELIZA effect" to p. 1667. The
  ELIZA-effect definition sits on PDF p. 3 (p. 1665). ELIZA recurs on p. 1666 (§3 opening) and p. 1668
  (§3.3). P. 1667 carries the "final uncompensated animator" sentence only. Both files are left alone.
- **Section map.** Stark's introduction promises Sections II to V, with "Section IV" on the three areas and
  "Section V" on governance. The printed headings run 2 (animation), 3 (three facets), 4 (governance) and 5
  (conclusion). I cite the printed numbers.
- **Licence.** `provenance.txt` calls the copy "CC BY 4.0". The PDF's first page says "Creative Commons
  Attribution-NonCommercial International 4.0 License".
- **Silvio through Stark.** Stark's [88] is Silvio (2010) and his [89] is Silvio (2019). He attributes the
  definition to [89:52] and the "structuring trope", "illusion of life", "creator/character" ratio,
  receiver and "[hard] to separate" lines to [88]. The bracketed "[hard]" is Stark's insertion, so Silvio's
  own word is unseen. Maeda & L. Stark (2025, p. 1662) attribute the same definition to Silvio (2010), with
  no page. The silvio cards must settle the attribution from Silvio's own texts, not from either Stark paper.
- **"Third party" here means Turing's interrogator** (PDF p. 4, §2.2: a thinking machine elicits "life,
  power, agency, will [and] personality" from a third party). It is not the interested third party of the HF
  finding at Checkpoint B and should not be cited for it.
- **Homonyms.** This is Luke Stark (Western University). D. Stark & Vanden Broeck (2024) is David Stark
  (CHECK F8). Stark's own ref. [57] is Maeda & Quan-Haase (2024), not Maeda & L. Stark (2025).
- **What the paper may not claim from it:** any empirical result, any account of frames or apparent motion,
  or any design method.

## Verification

2026-11-05 · S6 verifier, batch b01 (opus; not the writer) · verdict: verified · checked: loci 19/19 found verbatim in the text layer once its two columns are split, each on the PDF page and in the section its locator gives (section headings located in the text layer); metadata: author, title, FAccT '24, DOI 10.1145/3630106.3658995 and "9 pages" match the PDF's own ACM reference line; no crossref.json or openalex.json exists in the folder, so the page range 1663–1671 rests only on Maeda & L. Stark (2025, p. 1671, reference list), which I confirmed in that text layer; it remains unchecked against a registry record; read_depth full_text is honest (whole 9-page PDF and text layer held); "What it argues" terms (numerical disjunct, grammar of action, Kenyan moderators, conjectural, inferential AI, synthetic introjection, consumer protection, disclosure, AI iconoclasm, continuum) all found in the text; Section II–V mismatch and the CC BY-NC licence line confirmed; sha256 a2c6e94e…7101 recomputed, matches provenance.txt; four body sections present and in order · changed: nothing

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 19/19 loci found verbatim in stark2024animation.txt after splitting the two columns, each on the form-feed page the card gives (9 pages); "9 pages" in the ACM reference line and the Attribution-NonCommercial licence line found on p. 1; the §2.2 "third party" (Turing's interrogator) found on p. 4; references [57.] Maeda & Quan-Haase 2024, [88.] Silvio 2010, [89.] Silvio 2019 found in the reference list; sha256 of the PDF recomputed and matches provenance.txt; the page range 1663–1671 is confirmed only in the reference list of maeda2025anthropomorphism.txt ("FAccT '24, 1663–1671"), since the folder holds no Crossref record; full_text depth honest; the c4, c6, c7 uses follow from the text and the card marks the stretches (singular animator, lock-in, c5, c8).
- Changed: nothing.
- For the author: (1) S8's DOI check should confirm pp. 1663–1671 against Crossref; the card's only source is another paper's reference list. (2) Two page mismatches in files I did not touch: CHECK.md puts the "structuring trope" quotation at p. 1663 (it is on p. 1664), and OUTLINE §4.2 and triage F3-F4 tie the ELIZA effect to p. 1667 (its definition is on p. 1665; p. 1667 carries the user-as-animator sentence). (3) c7's singular "unseen animator" stretches Stark, whose animators are many, including the user; the author chooses between reading "animator" as a role and conceding the plurality.
