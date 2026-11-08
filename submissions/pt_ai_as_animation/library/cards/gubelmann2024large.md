---
key: gubelmann2024large
apa: "Gubelmann, R. (2024). Large language models, agency, and why speech acts are beyond them (for now) – A Kantian-cum-pragmatist case. *Philosophy & Technology*, *37*(1), Article 32. https://doi.org/10.1007/s13347-024-00696-1"
authors: "Gubelmann, Reto"
year: 2024
title: "Large Language Models, Agency, and Why Speech Acts are Beyond Them (For Now) – A Kantian-Cum-Pragmatist Case"
venue: "Philosophy & Technology"
volume: "37"
issue: "1"
pages: "Article 32 (24 pp.)"
doi: "10.1007/s13347-024-00696-1"
url: ""
type: article
facets: [F12]
claims: [c4, c5]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Publisher PDF (Springer, version of record, open access under CC BY 4.0 per its p. 21; 24 pp.) and its text layer gubelmann2024large.txt, at ~/iit-playground/pt_ai_animation_local/pdfs/gubelmann2024large/; fetched from link.springer.com (FETCH_LOG.tsv); body pp. 1–21 read in full, reference list pp. 21–24 scanned, 2026-11-08; sha256 7fcc9ddc43976ad3d3116c6322d3843b1c38773d9611fbec4e5b7214d28632cd (PDF; recomputed with shasum -a 256, matches sha256.txt)"
verified: verified
verified_against: "crossref.json; held VoR PDF sha256; pdftotext per page, 12 of 12 quotations traced to their stated pages"
prior_cards: []
status: candidate
added: 2026-11-08
run: pta-lib-2026-11
---

# Gubelmann (2024), LLMs, agency, and why speech acts are beyond them (for now)

## What it argues

Reto Gubelmann asks whether transformer-based LLMs could be language users in the way humans are, and he
answers no. His argument runs in four steps (p. 12). To be a speaker, a being must be able to perform speech
acts. To perform a speech act, it must have intentions. LLMs have no intentions. So LLMs are not speakers. He
tests for intention by asking whether we can tell a system's malfunction from a deliberate wrong act. With
ChatGPT, and with an imagined AI assistant that cleans up a racist's restaurant order, he finds no such
distinction: the system only functions or malfunctions.

He then gives the lack of intention a Kantian ground (§4). Mechanisms, like a watch, are heteronomous. An
outside agent assembles them for a purpose, and every goal they serve is set from outside. Organisms are
autonomous. Even a single cell keeps its matter organized and strives to persist, so its goals are its own.
Gubelmann splits autonomy into three kinds: material (self-organizing one's own matter), cognitive (finding
one's own means) and moral (judging one's ends). LLMs lack material and moral autonomy: "they do not care
about their continued existence".

His §5 adds a twist. LLMs are not GOFAI programs. In training they set their own weights and develop inner
functions (an attention head that resolves anaphora) that no engineer chose. That is cognitive autonomy. So
LLMs are "organismic mechanisms", which Kant's dichotomy says should not exist. Gubelmann concludes that
models are moving, slowly, toward "non-biological, but thereby not artificial" agents (p. 20). The closer
they come to being speakers, the less artificial they will be. He adds that cognitive autonomy without
material autonomy gives the dualist new support. His object throughout is the trained model, not the system
deployed around it.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): Gubelmann is the venue's
  sharpest counter. He would object on two counts. First, his life-criterion is material autonomy, a being
  that organizes its own matter and cares about its own persistence, and nothing in a harness, a VM or an
  efficiency layer supplies that. Second, he would read the surrounding system as more of what makes LLMs
  mechanisms. In his deer example, a refusal counts as an intention only if it comes from the model's own
  goal-setting, "not to just another layer of externally forced mechanism" (p. 11). On his terms the paper's
  harnesses are exactly that layer: heteronomy added from outside. The paper must therefore show that the
  organizational account it adopts does not require self-production by the system itself, or concede that
  the life it claims is the craft's, not the artifact's. Gubelmann gives the paper one opening. He grants
  that what is autonomous in an LLM came from training, not from programming, and that weakens the line
  between built and grown. Using that opening for the whole system, not the model, would stretch him.
- **c5** (intelligence frame versus life frame is a stance choice): Gubelmann treats organism versus
  mechanism as a fact about the kind of being, not as a stance. He would object that the paper may not
  choose the life frame as a way of looking. Either the system has autonomous goal-setting or it does not.
  The paper can still use him as a foil: he shows that the venue already argues about LLMs in organism and
  mechanism terms, which makes the life frame a live option, not an idiosyncrasy.

## Loci

Locators: the PDF prints "Page n of 24" with the article number 32; PDF page and printed page agree. Every
quotation was matched against `gubelmann2024large.txt`, the text layer of the held PDF (sha256 above).
Line-end hyphens in the text layer are rejoined.

- "Apart from niche uses, to use language means to act. But LLMs are unable to act because they lack intentions. This, in turn, is because they are the wrong kind of being: agents with intentions need to be autonomous organisms while LLMs are heteronomous mechanisms." — p. 1 of 24, Abstract; matched against gubelmann2024large.txt
- "these LLMs have taken a first step away from mechanistic artificiality to autonomous self-constitution" — p. 1 of 24, Abstract; matched against gubelmann2024large.txt
- "they are artifacts, that is, engineered mechanisms without any autonomy or intrinsic goals. Organisms, in contrast, even very simple ones, function to maintain themselves autonomously as long as they are what they are." — p. 2 of 24, §1; matched against gubelmann2024large.txt
- "It is customary to call the basic set-up of a neural NLP (NNLP) system an architecture, and a fully trained, usable instance of a given architecture a model." — p. 2 of 24, footnote 2; matched against gubelmann2024large.txt
- "The latter also draws the important connection to liability questions: if AI systems cannot be considered autonomous actors, then it is their creators that are ultimately liable for any harm caused by these systems." (Gubelmann reporting Popa 2021) — p. 3 of 24, §1; matched against gubelmann2024large.txt
- "For this distinction to really make sense, the goal to protect the deer would have to be somehow ascribable to ChatGPT’s autonomous goal-setting, not to just another layer of externally forced mechanism to prevent people from doing harm with the system" — p. 11 of 24, §3; matched against gubelmann2024large.txt
- "We note that LLMs have no such material autonomy; they do not care about their continued existence." — p. 15 of 24, §4.1; matched against gubelmann2024large.txt
- "A mechanism has been assembled by a given external agent for a certain purpose during a certain period of time. An organism, in contrast, is conceived and then grows and flourishes autonomously, given favorable environmental conditions." — p. 17 of 24, §4.2; matched against gubelmann2024large.txt
- "Unlike these traditional GOFAI programs, contemporary transformer-based models evolve impressively autonomously." — p. 18 of 24, §5; matched against gubelmann2024large.txt
- "Any goal that such an LLM might pursue has been determined externally." — p. 19 of 24, §5; matched against gubelmann2024large.txt
- "In sum, what is distinctive about these transformer-based LLMs is that they are mechanisms with recognizably organismic traits." — p. 19 of 24, §5; matched against gubelmann2024large.txt
- "The closer we get to models that qualify as speakers, the less artificial they are going to be." — p. 20 of 24, §6; matched against gubelmann2024large.txt

## Caution

- **Object of the argument.** Gubelmann argues about trained models (BERT, GPT-3, the transformer), and his
  own footnote 2 defines "model" that way. He never discusses harnesses, tool use or deployment systems, so
  the card's c4 objection applies his criteria to a case he did not consider.
- **Scope of the dualism claim.** His dualism point is tentative ("I tentatively suggest", p. 3) and
  conditional on moral autonomy following cognitive autonomy. The paper should not cite him as a dualist.
- **Dates.** Crossref gives online 2024-02-23 and print 2024-03; the volume year is 2024, so no
  `registered_year`.
- **Reference list errors in the source.** His reference list prints Burge (2010) twice, and his GPT-4
  quotation (p. 7, footnote 6) contains citation placeholders ("Jakobson (2003)", "Kahneman (2003)") that look
  like reference-manager slips. Neither affects the loci above.
- **Status.** SKETCH does not name this work; the card is a candidate the author decides on.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 1
- verdict: verified
- checked: frontmatter against crossref.json (author, title, Philosophy & Technology 37(1), article number 32, DOI, journal-article, online 2024-02-23, print 2024-03, CC BY 4.0); sha256 recomputed, matches sha256.txt. I traced all 12 quotations with pdftotext page by page: each is verbatim and on the page given, and the section labels match the headings (§3 p. 11, §4.1 p. 15, §4.2 p. 17, §5 pp. 18–19, §6 p. 20). In the text I confirmed the four-line argument P1–K (p. 12), the deer and racist-order examples, the Kantian watch, "I tentatively suggest" (p. 3), "organismic mechanisms" and "non-biological, but thereby not artificial" (p. 20), the CC BY notice (p. 21), the doubled Burge (2010) entry, and the Jakobson/Kahneman placeholders in footnote 6 (p. 7). The c4 and c5 uses say plainly that they apply his criteria to a case he did not consider.
- changed: nothing

## Hand-check
