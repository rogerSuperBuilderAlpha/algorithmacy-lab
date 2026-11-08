---
key: boge2022two
apa: "Boge, F. J. (2022). Two dimensions of opacity and the deep learning predicament. *Minds and Machines*, *32*(1), 43–75. https://doi.org/10.1007/s11023-021-09569-4"
authors: "Boge, Florian J."
year: 2022
registered_year: 2021
title: "Two Dimensions of Opacity and the Deep Learning Predicament"
venue: "Minds and Machines"
volume: "32"
issue: "1"
pages: "43–75"
doi: "10.1007/s11023-021-09569-4"
url: ""
type: article
facets: [F7]
claims: [c7]
role: support
load: load-bearing
read_depth: full_text
object_read: "Publisher version of record (Springer open-access PDF, CC BY 4.0, 33 pp.) and its text layer boge2022two.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/boge2022two/; fetched from https://link.springer.com/content/pdf/10.1007/s11023-021-09569-4.pdf (FETCH_LOG.tsv); read in full 2026-11-08 (PDF pp. 1–29 text, pp. 30–33 reference list scanned); sha256 8d4350abb4dbd05652c1170b284c0330017e45322134965765f958136af7eb88 (PDF, recomputed with shasum -a 256; matches sha256.txt)"
verified: verified
verified_against: "crossref.json; PDF sha256; full text layer per page (pdftotext -f N -l N), 16 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Boge (2022), Two dimensions of opacity and the deep learning predicament

## What it argues

Florian Boge asks whether deep neural networks (DNNs) can give scientists understanding of the
mechanisms behind the data, and not just predictions. He defends three theses. First, a trained DL
model, taken as an input–output mapping (his sense "(c)"), is "c-instrumental": its weights, biases and
activations carry no assigned meaning, so the model's whole interpretation comes from how the scientist
conceptualised input and output before training. He grants that features can be read off nodes, but he
holds that models are epistemic devices of cognising agents, which DNNs are not, so an "internal model"
exists only once scientists construct it. Second, DL opacity has two independent dimensions. H-opacity
concerns how the machine learns; it is continuous with the opacity of computer simulations and, citing
Sullivan, need not block understanding. W-opacity concerns what the machine learned: the complex,
non-obvious features of the data that drive its success. Boge offers a criterion (C1) for independence
and shows it met by two studies, an information-plane study of hidden layers (h) and a particle-physics
"data planing" study (w). He finds no counterpart to w-opacity in simulations or other scientific models.
Third, c-instrumentality and w-opacity together create a "DL predicament": an unsupervised model in an
exploratory context may predict an unexpected discovery whose understanding needs a radical conceptual
shift, and scientists, bound to their existing concepts, may then fail to translate the features the
network found into scientific concepts. He limits the claim: these four conditions make the gap likely,
not certain, and the gap can arise elsewhere too. His cases are scientific uses of DNNs (particle physics,
protein folding, climate), not deployed AI products.

## What the paper uses it for

- **c7** (necessary opacity: no frame holds the motion, no component the intelligence): Boge gives the
  paper its strongest philosophical support on the AI side, in two places. His w-opacity is a kind of
  opacity that he says has no counterpart in earlier scientific models, which backs the claim that DL
  opacity is not just the old complexity problem. And his argument that the "internal model is literally
  nowhere" until someone constructs it, because the model's meaning "stems entirely from the
  conceptualization of input and output", parallels the sketch's reading that no frame contains the motion
  and the viewer supplies it. The use stretches him in four ways. (1) His opacity is not in-principle in
  Roger's sense: benchmark studies did recover what the network learned, and his predicament arises only
  when four conditions hold jointly, and even then he says it is not bound to happen. (2) He treats
  h-opacity, the "how", as continuous with simulation opacity and as possibly harmless to understanding, so
  he does not support an in-principle black box about the algorithm itself. (3) His subject is DNNs as
  scientific instruments for discovering mechanisms in the world, not LLM-based systems with harnesses, and
  he says nothing about the system around the model. (4) His "nowhere" claim rests on the premise that DNNs
  are not cognising agents; a paper that frames the AI as an animated or living character should not lean
  on that premise without saying so.

## Loci

Locators: printed journal page (PDF page + 42), with the PDF page and section. Line-end hyphens in the
text layer are joined. Every quotation was matched against `boge2022two.txt`, the text layer of the held
PDF (sha256 above). Curly single quotes inside a quotation are Boge's own.

- "I here argue that these models are instrumental in a sense that makes them non-explanatory, and that their automated generation is opaque in a unique way." — p. 43 (PDF p. 1), Abstract; matched against boge2022two.txt
- "When unsupervised models are successfully used in exploratory contexts, scientists face a whole new challenge in forming the concepts required for understanding underlying mechanisms." — p. 43 (PDF p. 1), Abstract; matched against boge2022two.txt
- "these ‘tricks’ by themselves can already decrease understanding." — p. 47 (PDF p. 5), §2.2, footnote 5; matched against boge2022two.txt
- "the interpretation of a DL model stems entirely from the conceptualization of input and output." — p. 50 (PDF p. 8), §2.3; matched against boge2022two.txt
- "unless explicitly constructed by the scientists using the DNN, that internal model is literally nowhere, or rather, does not really exist." — p. 50 (PDF p. 8), §2.3; matched against boge2022two.txt
- "Most elements in formal representations of a DL model need not be assigned any meaning at all in order for the model to have predictive value." — p. 52 (PDF p. 10), §2.3; matched against boge2022two.txt
- "a process is epistemically opaque relative to a cognitive agent X at time t just in case X does not know at t all of the epistemically relevant elements of the process." (Boge quoting Humphreys, 2009, p. 618) — p. 59 (PDF p. 17), §3.1; matched against boge2022two.txt
- "The point hence is that, despite some abstract analogies between human and Deep Learning, it is in important respects opaque how the machine learns. Call that h-opacity." — p. 59 (PDF p. 17), §3.1; matched against boge2022two.txt
- "In order to gain understanding of underlying mechanisms from DL, we need not understand the training or the learning algorithm in full detail (Sullivan, 2019)." — p. 60 (PDF p. 18), §3.1; matched against boge2022two.txt
- "The second dimension concerns the question of what was learned by the machine. Call that w-opacity." — p. 61 (PDF p. 19), §3.2; matched against boge2022two.txt
- "When a DNN learns to approximate a desired function, it is hence not only opaque how, precisely, it achieves this goal: It is also opaque what it is about the data that drives this process." — p. 62 (PDF p. 20), §3.2; matched against boge2022two.txt
- "As far as I can tell, there really is no pendant for w-opacity in CSs or other scientific models." — p. 63 (PDF p. 21), §3.2; matched against boge2022two.txt
- "In these studies, researchers were hence in possession of rich information about the targeted objects and used that information to tackles the question of what the network had learned." ("tackles" as printed) — p. 66 (PDF p. 24), §4.1; matched against boge2022two.txt
- "the DNN finds significant features, but the translation of these into scientific concepts is up to scientists’ ability and knowledge." — p. 70 (PDF p. 28), §4.2; matched against boge2022two.txt
- "I have argued that DNNs are c-instrumental models that harvest their success in a w-opaque way." — p. 70 (PDF p. 28), §5; matched against boge2022two.txt
- "Emphatically, I am not claiming that only under conditions 1.–4. will scientists face problems in gathering understanding of underlying mechanisms from DL, nor that this is bound to happen in case 1.–4. occur" — p. 71 (PDF p. 29), §5; matched against boge2022two.txt

## Caution

- **Registered year (DECISIONS record correction applied).** Crossref gives `published-online` 2021-09-03
  and `issued` 2021-09-03; the volume (32(1), print 2022-03) is 2022. The key and `year` take the volume
  year; `registered_year: 2021` records the online date. The PDF's own header reads "Minds and Machines
  (2022) 32:43–75" and "Published online: 3 September 2021".
- **Humphreys through Boge.** The opacity definition in Loci is Humphreys (2009, p. 618) as Boge quotes
  it. Cite it from `humphreys2009philosophical`, checked there, not from this card.
- **Creel in a footnote.** Boge's footnote 18 (p. 59) maps h-opacity onto Creel's (2020) functional,
  structural and run transparency; the `creel2020transparency` card, not this one, carries Creel's terms.
- **Special-issue context.** The article appears under "SI: Machine Learning: Prediction Without
  Explanation" (PDF p. 1). Boge's question is scientific understanding, not trust, accountability or user
  experience.
- **"pendant"** (p. 63) and "tackles" (p. 66) are printed as given; do not silently correct them in a
  quotation.
- **What the paper may not claim from it:** that DL opacity is in principle irremediable; anything about
  LLMs, harnesses or deployed systems (the paper never discusses them); or that Boge treats DNNs as agents.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 2
- verdict: verified
- checked: frontmatter against crossref.json (author Florian J. Boge; title; *Minds and Machines* 32(1), 43-75; DOI; journal-article; issued and published-online 2021-09-03, published-print 2022-03, so `year: 2022` with `registered_year: 2021` is right). PDF sha256 recomputed; it matches sha256.txt and the card. All 16 quotations found verbatim in the PDF's text layer, each on the PDF page the card gives; the printed page = PDF page + 42 offset holds (PDF p. 1 header reads "32:43–75"). Section headings (2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 5) match the text. Humphreys (2009, p. 618) is cited inside Boge's text as the card says; footnote 18 on PDF p. 17 (p. 59) names Creel (2020). Summary points spot-checked against the text: criterion (C1), the 'planing' study, the "cognizing, conscious agents" premise, and the four-condition hedge. The claim use (c7) and its four named stretches fit what the text says.
- changed: nothing
