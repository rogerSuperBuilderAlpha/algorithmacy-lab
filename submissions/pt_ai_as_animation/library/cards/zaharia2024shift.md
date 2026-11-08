---
key: zaharia2024shift
apa: "Zaharia, M., Khattab, O., Chen, L., Davis, J. Q., Miller, H., Potts, C., Zou, J., Carbin, M., Frankle, J., Rao, N., & Ghodsi, A. (2024, February 18). *The shift from models to compound AI systems*. The Berkeley Artificial Intelligence Research Blog. Retrieved November 8, 2026, from https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/"
authors: "Zaharia, Matei; Khattab, Omar; Chen, Lingjiao; Davis, Jared Quincy; Miller, Heather; Potts, Chris; Zou, James; Carbin, Michael; Frankle, Jonathan; Rao, Naveen; Ghodsi, Ali"
year: 2024
title: "The Shift from Models to Compound AI Systems"
venue: "The Berkeley Artificial Intelligence Research Blog"
volume: ""
issue: ""
pages: ""
doi: ""
url: "https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/"
type: web
facets: [F8]
claims: [c1, c2]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "Web page (HTML as served, saved by S4 with access date 2026-11-08) zaharia2024shift.html and its text extraction zaharia2024shift.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/zaharia2024shift/; source URL and access date from provenance.txt; read in full 2026-11-08; sha256 44e2dbc1587ea35bb5c2b64371fb50d5a72860eef8a68de98149c07824736244 (HTML; computed with shasum -a 256, no sha256.txt in the folder); text extraction sha256 009484c94c2e0d52d152e6f5ea98b98a1bb38334803ebe048be8f9fa7ef5be98"
verified: verified
verified_against: "saved HTML and text extraction (sha256 of both recomputed); provenance.txt; 10 quotations traced, section/paragraph locators checked against the HTML <p> order; byline and BibTeX block"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Zaharia et al. (2024), The shift from models to compound AI systems

## What it argues

Matei Zaharia and ten co-authors argue, in a post on the Berkeley AI Research blog dated 18 February
2024, that "state-of-the-art AI results are increasingly obtained by compound systems with multiple
components, not just monolithic models." They define a compound AI system as one that "tackles AI
tasks using multiple interacting components, including multiple calls to models, retrievers, or
external tools", and set it against an AI model, "simply a statistical model". Their evidence is a
run of named systems: AlphaCode 2 sampling up to a million programs and filtering them,
AlphaGeometry pairing an LLM with a symbolic engine, Medprompt, Gemini's CoT@32 on MMLU, ChatGPT
Plus with plugins, and retrieval-augmented systems. They also cite a Databricks figure that 60% of
LLM applications use some form of RAG and 30% use multi-step chains.

They give four reasons for the shift. Some tasks improve faster and more cheaply through system
design than through scaling; systems can be dynamic (fresh data, access controls); systems make
control and trust easier than a bare model, which is "hard to control"; and systems let developers
trade quality against cost. They then name the open problems: a vast design space, optimisation
across non-differentiable components, and operations (monitoring, DataOps, security). They survey
emerging tools: composition frameworks (LangChain, LlamaIndex, agent frameworks, output-control
tools), DSPy for end-to-end optimisation, FrugalGPT and AI gateways for cost, and LLMOps tracing.
They close with a forecast: compound systems "will remain the best way to maximize the quality and
reliability of AI applications going forward". The post is an engineering position piece with no
new experiments; its numbers come from the linked work.

## What the paper uses it for

- **c1** (a working AI is the LLM plus harnesses, VMs, efficiencies): the anchor the sketch already
  names, and the fit is direct. The authors make the composition claim in the field's own voice and
  list the surrounding work (retrievers, tools, filters, routers, gateways, tracing). Their
  "Optimizing Cost" section is the nearest match to Roger's "efficiencies". They do not mention
  virtual machines or harnesses by name; "harness" comes from Zhou et al. (2026).
- **c2** (model-centrism misplaces where the intelligence sits): support, with a stretch. They
  diagnose the model-centrism the paper targets: 2023 brought "an intense focus on models as the
  primary ingredient in AI application development". But their claim is about where *results* and
  *quality* come from, not where intelligence sits. They keep the word "model" for the statistical
  core and never say the system is the intelligence. The paper's c2 needs the further step.
- **Against the paper's anti-CS framing** (no tag): the post cuts the other way too. The authors
  treat everything around the model as engineering and optimisation ("clever engineering, not just
  scaling up training"), modelled on end-to-end training in PyTorch. Their single nod to craft is
  that "the art of designing, optimizing, and operating them is still emerging". The paper can cite
  that phrase for craft only as a figure of speech; the authors do not develop it.

## Loci

Locators: the web page has no page numbers, so each quotation carries the section heading under
which it appears ("opening" = the untitled introduction before "Why Use Compound AI Systems?").
Every quotation was matched against `zaharia2024shift.txt`, the text extraction of the saved HTML,
with whitespace normalised; four were also confirmed in the HTML itself.

- "This naturally led to an intense focus on models as the primary ingredient in AI application development, with everyone wondering what capabilities new LLMs will bring." — opening, para. 1; matched against zaharia2024shift.txt and zaharia2024shift.html
- "state-of-the-art AI results are increasingly obtained by compound systems with multiple components, not just monolithic models." — opening, para. 1; matched against zaharia2024shift.txt
- "it means leading AI results can be achieved through clever engineering, not just scaling up training." — opening, para. 2; matched against zaharia2024shift.txt and zaharia2024shift.html
- "We define a Compound AI System as a system that tackles AI tasks using multiple interacting components, including multiple calls to models, retrievers, or external tools. In contrast, an AI Model is simply a statistical model, e.g., a Transformer that predicts the next token in text." — "Why Use Compound AI Systems?"; matched against zaharia2024shift.txt
- "We frequently see this with LLM users, where a good LLM creates a compelling but frustratingly unreliable first demo, and engineering teams then go on to systematically raise quality." — "Why Use Compound AI Systems?", first reason; matched against zaharia2024shift.txt and zaharia2024shift.html
- "Neural network models alone are hard to control: while training will influence them, it is nearly impossible to guarantee that a model will avoid certain behaviors." — "Why Use Compound AI Systems?", third reason; matched against zaharia2024shift.txt
- "the art of designing, optimizing, and operating them is still emerging." — "Developing Compound AI Systems", para. 1; matched against zaharia2024shift.txt
- "On the surface, an AI system is a combination of traditional software and AI models, but there are many interesting design questions." — "Developing Compound AI Systems", para. 1; matched against zaharia2024shift.txt
- "compound AI systems contain non-differentiable components like search engines or code interpreters, and thus require new methods of optimization." — "Key Challenges in Compound AI Systems" › "Optimization"; matched against zaharia2024shift.txt and zaharia2024shift.html
- "We believe that compound AI systems will remain the best way to maximize the quality and reliability of AI applications going forward, and may be one of the most important trends in AI in 2024." — "Conclusion"; matched against zaharia2024shift.txt

## Caution

- **Web source.** A blog post, not peer reviewed, and no DOI. The byline (eleven names) and the date
  "Feb 18, 2024" come from the page; the post's own BibTeX block gives the same eleven names and
  year 2024. Venue name as the page title gives it: "The Berkeley Artificial Intelligence Research
  Blog" (DECISIONS shortens it to "BAIR Blog"). Retrieval date 2026-11-08 from provenance.txt.
- **Stray author meta tag.** The HTML holds two `<meta name="author">` tags: one with the eleven
  names, and one reading "C.K. Wolfe". The second looks like a site-template default; it is not on
  the visible byline or in the BibTeX. A reference manager that reads meta tags may pick it up.
- **Figure not held.** The caption "Increasingly many new AI results are from compound systems."
  belongs to an image the text extraction does not contain. The card claims nothing from the figure.
- **Second-hand numbers.** The 60% / 30% Databricks figures, the AlphaCode 30%→80% illustration
  (explicitly hypothetical: "suppose…"), the 9% Medprompt gain, and the FrugalGPT 4% / 90% figures
  are the authors' summaries of linked work. I did not follow the links. The paper should cite the
  primary sources if it uses any number.
- **Sketch status.** SKETCH marks this work "(unverified)". Title, byline, date and venue are now
  confirmed from the page; the sketch is left alone.
- **Checkpoint B 6(c).** Roger accepted the web card. Until `sculley2015hidden` is promoted, the
  sketch's compound-AI premise rests on this post, `paleyes2023challenges` and `zhou2026externalization`.

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 2
- verdict: verified. The byline (eleven names, in the order of the author meta tag and the BibTeX block), the date "Feb 18, 2024", the page title and the URL all match the saved page and provenance.txt (access 2026-11-08). The sha256 values for the HTML and the text extraction match the ones the card gives. All 10 quotations are verbatim in zaharia2024shift.txt. Every locator matches: the opening paragraphs are numbered by the HTML `<p>` order, and the headings match "Why Use Compound AI Systems?", "Developing Compound AI Systems", "Key Challenges…" › "Optimization" and "Conclusion". The first and third reasons are right.
- checked: the stray `<meta name="author" content="C.K. Wolfe">` (present, as the card says); the figure caption; the second-hand numbers (60% / 30% Databricks, 9% Medprompt, 30%→35%→80% "suppose" illustration, FrugalGPT 4% / 90%) in the text, all of which the card attributes to linked work. The c2 stretch (results and quality, not where intelligence sits) is named.
- changed: nothing
