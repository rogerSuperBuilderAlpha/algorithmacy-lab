---
key: bommasani2021on
apa: "Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., Brynjolfsson, E., Buch, S., Card, D., Castellon, R., Chatterji, N., Chen, A., Creel, K., Davis, J. Q., Demszky, D., … Liang, P. (2021). *On the opportunities and risks of foundation models* (arXiv:2108.07258) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2108.07258"
authors: "Bommasani, Rishi; Hudson, Drew A.; Adeli, Ehsan; … Liang, Percy (114 authors in csl.json)"
year: 2021
title: "On the Opportunities and Risks of Foundation Models"
venue: "arXiv (cs.LG); Center for Research on Foundation Models (CRFM), Stanford"
volume: ""
issue: ""
pages: "214 pp. (v3)"
doi: "10.48550/arXiv.2108.07258"
url: "https://arxiv.org/abs/2108.07258"
type: preprint
facets: [F8]
claims: [c2, c1]
role: contrast
load: load-bearing
read_depth: partial
object_read: "arXiv v3 PDF (arXiv:2108.07258v3 [cs.LG] 12 Jul 2022; 214 pp.; csl.json gives CC BY 4.0) and its text layer bommasani2021on.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/bommasani2021on/; read 2026-11-08: title page and abstract (p. 1), contents (p. 2), §1 Introduction in full (pp. 3–20: §1.1 emergence and homogenization, §1.1.1 naming, §1.2 ecosystem, §1.3 future, §1.4 overview of the report with its summaries of §§2–5); §§2–5 and the reference list not read; sha256 05e867e3c710a3b0c0e13eb372d013c3511f2ee114bace5ca5c402d6341e92dd (PDF; recomputed with shasum -a 256, matches sha256.txt)"
verified: verified
verified_against: "csl.json (114 authors, first 19 in APA order); held v3 PDF sha256; pdftotext per page over pp. 1–20, 12 of 12 quotations traced to their stated pages"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Bommasani et al. (2021), On the opportunities and risks of foundation models

## What it argues

Rishi Bommasani, Percy Liang and over a hundred co-authors at Stanford's Center for Research on Foundation
Models name a paradigm. A "foundation model" is any model trained on broad data, usually by
self-supervision at scale, that can be adapted to many downstream tasks (BERT, GPT-3, CLIP). They chose the
word to mark the models' "critically central yet incomplete character" (abstract): a foundation model "is
itself incomplete but serves as the common basis from which many task-specific models are built" (p. 7).

Their introduction rests on two words. Emergence means behavior is "implicitly induced rather than
explicitly constructed": with each step from machine learning to deep learning to foundation models, more of
how a task is done emerges from training (in-context learning in GPT-3 is their example). Homogenization means
that many applications now share one model, which gives leverage but creates a single point of failure. The
two together make the models hard to understand and risky to deploy widely.

§1.2 widens the view to an ecosystem: data creation, curation, training, adaptation, deployment. The authors
state that "the foundation model is only one component … of an AI system" (p. 8) and that, for deployment,
adaptation means building a system of modules, rules, classifiers and other signals. Yet their motto is
"Think ecosystem, act model" (p. 9): because many researchers only control training, they ask for ways to
reason about a model's downstream impact from the model itself. §1.3 turns to who shapes the future:
industry builds the models, academia has lost access, and the authors call for public compute and
interdisciplinary norms. §1.4 maps the report's 26 sections across capabilities, applications, technology
and society.

## What the paper uses it for

- **c2** (model-centrism misplaces where the intelligence sits): Bommasani et al. are the paper's best
  statement of the frame it contests, and a careful one. The report makes the model the unit of study and of
  naming ("an emerging paradigm for building artificial intelligence (AI) systems based on a general class of
  models"), puts emergence inside the model, and closes the ecosystem view with "Think ecosystem, act model".
  The paper can cite them for how the field's own vocabulary centers the model. It must not cite them as
  naive model-centrists. They say the model is incomplete, only one component, and unfinished until adapted.
  What they would object to in the thesis is its location of the intelligence: for them the capabilities
  "emerge" in the model and the surrounding system adapts and constrains it, whereas the paper says the
  working AI is the composition. The disagreement is over where capability comes from, not over whether the
  system matters.
- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the report concedes c1's premise in
  the engineers' words. Deployment "is about creating a system, which requires potentially many different
  modules, custom rules … or classifiers … and combination with other complementary signals" (p. 9), and
  "computer systems determine what is practically achievable" (p. 17). The use fits, with a stretch: the
  report treats these layers as adaptation and harm mitigation around a model whose capabilities are already
  there, not as where the intelligence is composed.

## Loci

Locators: the PDF's printed page numbers (running heads) equal its PDF page numbers for the pages read. Every
quotation was matched against `bommasani2021on.txt`, the text layer of the held v3 PDF (sha256 above).
Line-end hyphens are rejoined. Where the authors' text has double quotation marks inside a quotation, I give
them as single quotes. An ellipsis marks words I left out.

- "We call these models foundation models to underscore their critically central yet incomplete character." — p. 1, Abstract; matched against bommasani2021on.txt
- "This report investigates an emerging paradigm for building artificial intelligence (AI) systems based on a general class of models which we term foundation models." — p. 3, §1; matched against bommasani2021on.txt
- "Emergence means that the behavior of a system is implicitly induced rather than explicitly constructed; it is both the source of scientific excitement and anxiety about unanticipated consequences." — p. 3, §1.1; matched against bommasani2021on.txt
- "Since the power of foundation models comes from their emergent qualities rather than their explicit construction, existing foundation models are hard to understand" — p. 6, §1.1; matched against bommasani2021on.txt
- "a foundation model is itself incomplete but serves as the common basis from which many task-specific models are built via adaptation." — p. 7, §1.1.1; matched against bommasani2021on.txt
- "It is important to note that the foundation model is only one component (though an increasingly important component) of an AI system." — p. 8, §1.2; matched against bommasani2021on.txt
- "is the celebrated centerpiece in AI research, though it is only one of many stages." (of training on curated datasets) — p. 9, §1.2, stage (3); matched against bommasani2021on.txt
- "For deployment, adaptation is about creating a system, which requires potentially many different modules, custom rules (e.g., restrictions on the output space) or classifiers (e.g., for toxicity classification), and combination with other complementary signals" — p. 9, §1.2, stage (4); matched against bommasani2021on.txt
- "Think ecosystem, act model. While the social impact depends on the whole ecosystem, it is still important to be able to reason about the social implications of a foundation model, given that many researchers’ and practitioners’ purview is restricted to the training stage." — p. 9, §1.2; matched against bommasani2021on.txt
- "foundation models are unfinished intermediate objects that can be adapted to many downstream applications, sometimes by an entirely different entity for unforeseen purposes." — p. 9, §1.2; matched against bommasani2021on.txt
- "Foundation models are intermediary assets; they are unfinished and generally should not be used directly, instead requiring adaptation for specific downstream tasks." — p. 17, §1.4.3 (summary of §4.3); matched against bommasani2021on.txt
- "computer systems determine what is practically achievable." — p. 17, §1.4.3 (summary of §4.5); matched against bommasani2021on.txt

## Caution

- **Partial read.** I read the introduction and its overview only (pp. 1–20). The p. 17 loci are the
  introduction's one-paragraph summaries of §4.3 (adaptation) and §4.5 (systems), not those sections. The
  full §4.3 and §4.5 may qualify these lines; S6 or the author should read them before the paper relies on
  the adaptation point.
- **Version.** The held copy is arXiv v3 (12 Jul 2022), per its p. 1 stamp and csl.json; DECISIONS gives the
  same. The year 2021 follows the record (`issued` 2021, the v1 year). v1 wording may differ.
- **Authors and APA.** csl.json lists 114 authors. The APA above gives the first 19, an ellipsis and the last,
  per APA 7. One name differs between sources: csl.json gives "Demszky, Dora", the PDF byline gives "Dorottya
  Demszky"; I used the initial D., which fits both. The report's own Author Contributions (p. 14) say "not
  all the views expressed in this report are held by all the authors", so the paper should attribute claims
  to "Bommasani et al." as a report, not to every author.
- **Type.** The work is a report posted to arXiv by CRFM, not a peer-reviewed paper; csl.json types it
  `article` with publisher arXiv. I typed it `preprint`.
- **Status.** SKETCH does not name the report (it names Sculley et al. and Zaharia et al. for the
  compound-AI premise), so the card is a candidate. DECISIONS notes that the abstract's "incomplete character"
  is one reason `schaeffer2023are` can yield to Sculley; that is a library decision, not a claim of this card.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 1
- verdict: verified
- checked: frontmatter against csl.json (title, 114 authors, the first 19 in APA order, issued 2021, DOI, version 3, CC BY 4.0, publisher arXiv); the p. 1 stamp "arXiv:2108.07258v3 [cs.LG] 12 Jul 2022" and the byline "Dorottya Demszky"; 214 pages per pdfinfo; sha256 recomputed, matches sha256.txt. I traced all 12 quotations with pdftotext page by page: each is verbatim and sits on the page given. The body's details check out in the text: "26 sections" (§1.4), the p. 14 line "not all the views expressed in this report are held by all the authors", and the p. 17 lines under the headings "§4.3: Adaptation" and §4.5 in §1.4.3. I did not read §§4.3 and 4.5 either; the card's Caution about them stands. The c2 and c1 uses name their stretches.
- changed: nothing

## Hand-check
