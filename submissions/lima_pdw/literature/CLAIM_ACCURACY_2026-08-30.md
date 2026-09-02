# Claim-accuracy audit — every reference in PAPER.md, 2026-08-30

Scope: this is a different check from the 2026-08-29 sweep. That sweep verified **existence and
bibliographic accuracy** (real DOI, correct authors/venue/year/pages) for ~75 references, and
page-number accuracy for direct quotes. This audit checks **whether the paper's characterization of
each load-bearing source matches what that source actually argues** — a real risk after a full Opus
rewrite that touched nearly every sentence, since a citation can be bibliographically real and still
be paraphrased into a claim the source doesn't actually support.

**Load-bearing** = the paper attributes a specific claim, finding, quote, statistic, or theoretical
position to the source (not just cited for general lineage alongside several others with no
distinguishing claim). Every load-bearing citation gets checked against the actual source (via its
literature card if full-text/extended-preview depth, or fresh verification if the card is abstract-only
or doesn't exist). Background citations get a lighter existence sanity-check only, since most were
already verified 2026-08-29.

Verdicts: **ACCURATE** (claim matches source), **DRIFTED** (claim is a real distortion — overstated,
understated, or wrong — fixed with an exact replacement), **UNVERIFIABLE AT CURRENT DEPTH** (card
depth doesn't support confirming or denying; the claim may or may not hold, flagged for the author),
**FLAG** (something else worth a human look).

Batches, by section of `manuscript/PAPER.md`:
- Batch 1: Abstract + Introduction + Coordination-Form Gap (lines 1–46)
- Batch 2: Extant Constructs hearings 1–4 — CMC, HMC, AI-MC, AI Literacy (lines 67–111)
- Batch 3: Extant Constructs hearings 5–7 + What These Boundaries Share (lines 113–169)
- Batch 4: Algorithmacy construct section (lines 171–280)
- Batch 5: Empirical Strategy + Appendix A + Appendix B (lines 282–614)
- Batch 6: Appendix C + remaining minor/boundary-case citations

(Results filled in below as each batch reports.)

## Batch 2: Extant Constructs, hearings 1-4 (CMC, HMC, AI-MC, AI Literacy)

Scope checked: `PAPER.md` lines 48–112 (Extant Constructs intro, Table 1, and the Computer-Mediated
Communication Competence, Human–Machine Communication, AI-Mediated Communication, and AI Literacy
hearings). Cards read: `spitzberg2006.md`, `guzmanlewis2020.md`, `hancock2020.md`,
`longmagerko2020.md` (plus its steelman), `gibbs2021.md`, `felin2015.md`, `fortunati2020.md`,
`ng2021.md`, `gittell_relational_coordination.md`, `sutherland2020.md`, `zhou2025.md`,
`zhou2025apjhr.md`. Every direct quotation with a page cite was additionally cross-checked against
the underlying PDF page images (`spitzberg2006_vor.pdf`, `hancock2020_vor.pdf`), not just the card's
prior verification notes, since the task flagged rewrite risk.

### Computer-Mediated Communication Competence — Spitzberg (2006)

All quotes independently re-checked against `spitzberg2006_vor.pdf` page images (not just the card's
recorded verification), because the section is quote-dense and the task asked for byte-level checking.

- "any human symbolic text-based interaction conducted or facilitated through digitally-based
  technologies" (p. 630) — **ACCURATE**. Verbatim match, confirmed directly against the PDF: "CMC is
  tentatively defined as *any human symbolic text-based interaction conducted or facilitated through
  digitally-based technologies*." This quote was not in the card's two prior "Verified" passes; now
  independently confirmed here.
- "the ratio of approach to avoidance attitudes, beliefs, and values in a given CMC context" (p. 640)
  — **ACCURATE**. Verbatim match, both in the card's 2026-08-26 pass and independently re-confirmed
  here against the PDF (p. 640: "CMC motivation is defined here as *the ratio of approach to avoidance
  attitudes, beliefs, and values in a given CMC context*").
- "the cognitive comprehension of content and procedural processes involved in conducting appropriate
  and effective interaction" (p. 641) — **ACCURATE**. This quote was not in either of the card's
  "Verified" passes; independently confirmed here against the PDF (p. 641: "CMC knowledge is defined
  here as *the cognitive comprehension of content and procedural processes involved in conducting
  appropriate and effective interaction in the computer-mediated context*"). The paper's quote truncates
  the source's trailing "in the computer-mediated context," a legitimate end-truncation, not a wording
  change.
- "four core skill clusters — attentiveness, composure, coordination, and expressiveness" (p. 638) and
  "five discrete facets of context" (p. 644) — **ACCURATE**. Confirmed in the card's 2026-08-29 pass.
- "Five relational outcome criteria ... appropriateness, effectiveness (encompassing task achievement
  and efficiency), coorientation, satisfaction, and relationship development" (p. 648) — **ACCURATE**.
  Confirmed in the card's 2026-08-29 pass ("nearly verbatim" to the article's working-typology
  sentence); paraphrase word "encompassing" for the source's "including" is immaterial since this
  passage is not in quotation marks.
- "perceived legitimacy or fit of a message to the context" (appropriateness, unpaged in the paper) —
  **ACCURATE**. Verbatim match, independently re-confirmed against the PDF p. 648.
- "competent interactants can facilitate the competence of cointeractants" and "an incompetent
  interactant can diminish a normally competent cointeractant's performance" (p. 650) — **ACCURATE**.
  Independently confirmed verbatim against the PDF p. 650 (the card's prior note only confirmed the
  general location/topic, not the exact wording — this is the first byte-level check of these two
  quotes).
- **"positive affect associated with fulfillment of positively valenced expectancies" (satisfaction,
  unpaged in the paper) — DRIFTED.** The source (PDF p. 648, independently confirmed): "Satisfaction
  is **the** positive affect associated with **the** fulfillment of positively valenced expectancies
  (Spitzberg & Hecht, 1984)." The paper's quote drops "the" twice. Dropping the leading "the" is a
  defensible start-truncation (the quote begins mid-sentence), but dropping the internal "the" before
  "fulfillment" is not a boundary trim — it silently alters wording inside the quoted span. The card's
  own 2026-08-29 verification note already shows this discrepancy in its side-by-side ("found p. 648
  ('Satisfaction is the positive affect associated with **the** fulfillment...')") without flagging it
  as an error; it should have.
  **Fix:** change the quoted fragment to "positive affect associated with the fulfillment of positively
  valenced expectancies," or, if a page cite is added per the card's earlier recommendation, "the
  positive affect associated with the fulfillment of positively valenced expectancies" (p. 648).

### Human–Machine Communication — Guzman & Lewis (2020), Fortunati & Edwards (2020), Gibbs et al. (2021)

- "communicative subjects, instead of mere interactive objects" (p. 71) — **ACCURATE**. Matches the
  card's confirmed spot-check verbatim.
- "questions of communication as they relate to technologies designed to fulfill the communicator role"
  (p. 74) — **ACCURATE**. Matches the card's corrected page (this was p. 73 in an earlier draft and was
  fixed to p. 74 on 2026-08-29; the current text carries the corrected page).
- "within a communication context in which at least one of the interaction partners is a machine"
  (p. 74) — **ACCURATE**. Matches the card's confirmed spot-check verbatim.
- "the default model Guzman and Lewis describe has people exchanging information through a technology
  that mediates human interaction (p. 73)" — **ACCURATE**, and correctly still a paraphrase (no
  quotation marks). The card records that an earlier draft falsely quoted this as CMC's own claim
  ("technology as a mediator of human interaction," misattributed and mis-paged at p. 72); that error
  is fixed in the current text and the fix has held.
- Gibbs et al. (2021), structurational critique (line 83) — **ACCURATE**. The paper's characterization
  ("mischaracterizes human–machine interaction by treating it as an isolated dyad rather than an
  organizational structuration," agency "distributed across the human user, the technical artifact, and
  the governing institutional order," target is "the field's methodological individualism") matches the
  card's summary closely on every point, including the specific claim that Gibbs et al. work the
  argument through organizational cases including algorithmic management.
- Gibbs et al. (2021) + Felin et al. (2015) (line 87) — **ACCURATE but weakly grounded**. "Gibbs et al.
  (2021) caution against reducing structural dynamics to isolated individual attributes" matches the
  card. "algorithmacy answers that caution as an individual micro-foundation rooted in social
  antecedents (Felin et al., 2015)" is consistent with the Felin card's summary of the microfoundations
  movement, but the Felin card itself is `metadata_only` depth with `evidence_basis: citing_literature`
  — reconstructed from secondary reception, not a direct read, and the card's own caution says to
  "verify... before citing them in support of §8's sentence." This sentence is a different section
  (§9/Extant-Constructs) than the one the card's caution names, so it has not been checked against the
  primary text at all. **Flag for the author**: the specific phrase "rooted in social antecedents" is
  plausible for the microfoundations literature generally but is not independently confirmed as Felin
  et al.'s own vocabulary.
- Fortunati and Edwards (2020) (lines 81, 89) — **ACCURATE**, both instances. "Draw the constitutive
  boundary, defining human–machine communication as the study of meaning-making between humans and
  machines wherein the technical artifact occupies the position of a communicative subject" and "define
  their field around machine-directed meaning-making" both match the card's summary of the editorial's
  founding definition. No page numbers or quotation marks are used, appropriately, since the card
  records this as characterization rather than direct quotation.

### AI-Mediated Communication — Hancock, Naaman & Levy (2020)

- "mediated communication between people in which a computational agent operates on behalf of a
  communicator by modifying, augmenting, or generating messages to accomplish communication or
  interpersonal goals" (p. 90) — **ACCURATE**. Matches the card's confirmed verbatim check of the
  formal definition, introduced in the article "We integrate these AI and CMC conceptualizations to
  define AI-MC as."
- The five-parameter descriptions (magnitude, media type, optimization goal, autonomy, role
  orientation) are now rendered as paraphrase, not direct quotation (no quotation marks in the current
  text). This is a change from an earlier draft state the card describes (which had these as five
  verbatim Table 1 quotes, verified against p. 91). The current paraphrases are accurate glosses of the
  Table 1 definitions the card recorded — no drift, and dropping the quotation marks resolves what would
  otherwise have been a page mismatch (the table is on p. 91, not p. 90).
- **"the message receiver is assumed to understand and accept that agency" (p. 90) — DRIFTED (wrong
  page).** Independently checked against `hancock2020_vor.pdf`: the sentence "Similarly, the message
  receiver is assumed to understand and accept that agency" appears on **p. 89**, in the paragraph
  preceding the formal AI-MC definition, not on p. 90 where the definition itself sits. Wording is
  otherwise exact. **Fix:** change the page cite from (p. 90) to (p. 89).
- "on behalf of a communicator" (p. 90) — **ACCURATE**. This is a sub-span of the already-confirmed
  p. 90 formal definition.
- The reframing in lines 97–99 (AI-MC's optimization-goal parameter as the axis distinguishing a
  principal's delegate from an institutional adjudicator; "their computational agent optimizes for the
  interpersonal or communicative objectives of a designated sender, while the intermediary modeled here
  optimizes for institutional coordination metrics external to both interactants") — **ACCURATE**, and
  notably follows the card's own recommended reframing almost verbatim ("I adopt the optimization goal
  parameter from Hancock et al. (2020) as the analytical axis separating the two frameworks" echoes the
  card's suggested edit). This is a case where the manuscript incorporated prior review feedback
  correctly.

### AI Literacy — Long & Magerko (2020), Ng et al. (2021)

**Regression found: page numbers have been reintroduced on three Long & Magerko quotes, reversing the
2026-08-29 fix.** The `longmagerko2020.md` card is `abstract_only` depth; a companion steelman (built
from a camera-ready copy via Internet Archive, not the ACM version of record) explicitly warns that
page anchors from that copy "still need the ACM version" and that "competency numbers are the safer
citation form." On 2026-08-29 all four page numbers previously in `PAPER.md` for this source (pp. 2, 6,
2, 7) were removed for exactly this reason. The current text has re-added three of them:

- "recognize that humans play an important role in programming, choosing models, and fine-tuning AI
  systems" **(p. 6)** — quote wording **ACCURATE** (verbatim match to the steelman's transcription of
  Competency 10), but the page number is a **regression**: this citation form was explicitly removed on
  2026-08-29 as unverifiable against the ACM version of record, and the steelman recommends citing by
  competency number instead — which the sentence already does ("Competency 10 (Human Role in AI)"), so
  the page parenthetical is both unverifiable and redundant.
- "limit people's ability to effectively use, collaborate with, and act as critical consumers of AI"
  **(p. 2)** — quote wording **ACCURATE** (verbatim match to the steelman), page number is the same
  kind of **regression**.
- "consider designing AI learning experiences that foster social interaction and collaboration"
  **(p. 7)** — quote wording **ACCURATE** (verbatim match to the steelman, modulo the source's
  sentence-initial capital "Consider"), page number is the same kind of **regression**; the sentence
  already cites "Design Consideration 11 (Social Interaction)," which is the recommended stable
  citation form.
- The opening definitional quote ("a set of competencies that enables individuals to critically
  evaluate AI technologies; communicate and collaborate effectively with AI; and use AI as a tool
  online, at home, and in the workplace") correctly carries **no** page number — this one instance is
  consistent with the 2026-08-29 fix and should be the model for the other three.

**Fix for all three:** drop the "(p. N)" parentheticals from the Competency 10 quote, the "limit
people's ability..." quote, and the Design Consideration 11 quote. The competency/design-consideration
numbers already present in each sentence are the verified, stable citation form; the page numbers are
neither verified against the ACM version nor necessary, since the numbered identifiers already do the
citation work.

- "Only two of the seventeen competencies reference human actors" (Competency 10 and Competency 5) —
  **ACCURATE**. The steelman explicitly identifies exactly these two ("Competency 10 is titled *Human
  Role in AI*... Competency 5 names 'human skills' as the alternative to using AI. Neither gives another
  person a position in an interaction the learner is conducting.").
- "nine competencies govern technical mechanics while one addresses normative ethics" — **ACCURATE**.
  The steelman's breakdown (17 competencies split 4/2/9/1/1 across the five organizing questions) puts
  exactly 9 under "How does AI work?" and exactly 1 (Ethics) under "How should AI be used?"
- Ng et al. (2021), four-dimension synthesis (line 109) — **ACCURATE**. "knowing and understanding AI,
  using and applying AI, evaluating and creating AI, and AI ethics" matches the card's "know and
  understand AI, use and apply AI, evaluate and create AI, and ethical issues" (minor relabeling of the
  fourth dimension, immaterial since not quoted). The claim that "subsequent measurement scales
  inherited the fourfold taxonomy" and wrote the counterpart out of "the standard psychometric
  tradition" matches the card's account of Ng et al. as the "transmission mechanism" through which
  downstream instruments (Carolus et al.'s MAILS, Markus et al.'s AICOS) inherit the same four-cell,
  no-counterpart scheme.
- "Long and Magerko's literacy genealogy... tracing literacy from alphabetic text through digital,
  computational, and data literacies" — **ACCURATE** but slightly incomplete as paraphrase: the
  steelman records the source tracing literacy through "digital, computational, scientific and data
  literacies" — the paper's list omits "scientific." Not flagged as DRIFTED since this is paraphrase,
  not a quotation, and the omission does not change the claim's substance.

### Table 1 and section-intro citation (line 50)

- Gittell (2002), relational coordination (line 50) — **ACCURATE**. "Conceptualizes shared
  communication and relational ties among interdependent organizational members" and "presupposes
  unmediated interactants who directly observe, contact, and negotiate with one another" both match the
  card's account of relational coordination as measured on identifiable counterpart *roles* that a
  respondent can name, reach, and rate. No quote, no page number, so the card's separate caution about
  ambiguity between two different 2002 Gittell papers (Management Science vs. Journal of Service
  Research) is a reference-list hygiene question, not a claim-accuracy problem for this sentence.
- Sutherland et al. (2020) and Zhou et al. (2025), socialization claim (line 87: "workers acquire
  platform fluency through informal peer networks, community sensemaking, and shared lore") — **cited
  jointly with no distinguishing claim, so Background** rather than load-bearing by this audit's
  criterion. One caution worth flagging: there are two different Zhou et al. 2025 papers in the library
  (`zhou2025.md`, the Human Resource Management "dual effects" paper on attribution, whose card
  explicitly warns "never cite this as a bare 'Zhou et al. 2025'"; and `zhou2025apjhr.md`, the Asia
  Pacific Journal of Human Resources algorithmic-competency scale paper, whose antecedents include
  "peer social support and cognitive job crafting"). The claim about "informal peer networks" matches
  the APJHR paper's own findings, not the HRM attribution paper's. If the reference list resolves
  "Zhou et al., 2025" to a single specific entry, confirm it is the APJHR paper (`zhou2025apjhr.md`);
  if it is meant to point to the other one, the peer-networks claim is unsupported by that source's
  card.

### Summary

Of roughly 20 checkable load-bearing items in this section, 17 are accurate, matching their cards or
the primary PDFs word-for-word or in substance. Two direct-quote errors: the Spitzberg "satisfaction"
quote drops an internal "the," and the Hancock et al. "message receiver is assumed" quote is cited to
the wrong page (p. 90 instead of p. 89). One clear regression: three Long & Magerko quotes have had
page numbers reintroduced that were deliberately removed on 2026-08-29 as unverifiable against the ACM
version of record — this is the exact regression the task was watching for, and it is real. One
citation-hygiene flag (Zhou et al. 2025 ambiguity) and one weak-evidence flag (Felin et al. 2015's card
is a secondary reconstruction, not a direct read) round out the findings.

---

## Batch 4: Algorithmacy construct section

Scope checked: `manuscript/PAPER.md` lines 171–280 (Scope and Boundary Conditions through the
Propositions). Every citation occurring in that span is listed below in order of first appearance.
Two citations named in the audit brief — Henseler et al. (2015) and the second "bounded behavioral
construct" use of Suddaby (2010) — are **not actually present in lines 171–280**; they are addressed
at the end under "Out-of-range items checked anyway."

### Suddaby (2010) — line 173 — **ACCURATE**

Claim: "Construct clarity in organizational theory turns on four things: a precise definition,
explicit scope conditions, stated semantic relations to neighboring constructs, and demonstrated
theoretical coherence (Suddaby, 2010)."

`literature/models/suddaby2010.md` (read from the source PDF) confirms Suddaby's own four elements
verbatim: "The essence of construct clarity comprises four basic elements" — (1) Definitions, (2)
Scope conditions, (3) Semantic relations ("No construct is an island"), (4) Coherence. The paper's
four nouns map one-to-one onto Suddaby's four elements, in his order. Exact match.

### Hayek (1945); Simon (1997); Weber (1978) — line 181 — **BACKGROUND**

Cited for the classical market and bureaucracy archetypes (posted price + unrestricted refusal
right; codified rule + hierarchical office) with no further specific claim attached beyond the
naming. No card exists for any of the three; not checked further, consistent with background
treatment in the 2026-08-29 existence sweep.

### Sutherland et al. (2020) — line 183 — **ACCURATE**

Claim: freelance platform participants "retain the discretionary capacity to negotiate terms or
migrate collaborations off-platform (Sutherland et al., 2020), mitigating opacity through direct
bilateral communication."

`literature/cards/sutherland2020.md` confirms this directly: the P39 incident and the broader
finding that freelancers "systematically migrated established client relationships off-platform,"
verified against the source PDF (p. 469, corrected from an earlier 468 in the 2026-08-29 sweep).
Matches.

### Zhou et al. (2025) — line 189 — **ACCURATE**

Claim: predicted correlations run *Understanding* with *interpreting* and *Leveraging* with
*specifying intent*, with *Embracing* predicted null because it is "an affective orientation toward
platform efficiency" rather than an operational capacity.

`literature/cards/zhou2025apjhr.md` confirms the three named dimensions and their content:
*Understanding AM* is "a sophisticated grasp of how algorithmic management works," *Leveraging AM*
is "the capacity to use algorithmic management strategically," and *Embracing AM* is "a willingness
to trust the efficiency and accuracy of the system" — an attitudinal item ("I think the platform AM
is highly efficient"), the dimension the card independently flags as weakest-linked to the others
(intercorrelations .22–.25) and as containing no coordinative capacity. The paper's null prediction
for *Embracing* is exactly what the card's own analysis would predict. Matches.

### Rahman (2021) — lines 191, 209, 242, 264 — **ACCURATE** (all four uses)

- Line 191: "Reactivity categorizes degrees of behavioral adaptation versus defensive withdrawal
  under labor discipline" — matches the card's two-form typology, *experimental reactivity*
  (testing tactics to raise the score) versus *constrained reactivity* (limiting engagement to
  protect it).
- Line 209: "determining whether the platform infrastructure or the human client drove a score
  change, Rahman's (2021) fifth dimension of opacity" — matches the card's five components exactly:
  criteria, execution, magnitude, impact, and "who influences it (client or platform, unspecified)"
  — the fifth and last-listed component.
- Line 242: "whether that variance survives controls for platform dependence and prior evaluation
  shocks (Rahman, 2021)" — matches the card: reactivity type "turns on platform dependence and
  evaluation setbacks," which the card names as rival explanations to competency.
- Line 264: "Rahman (2021) documents how individual reactivity can reinforce subordination" —
  matches the card's own framing that reactivity "entrenches rather than relaxes the platform's
  hold" and that "paranoia persists years on."

### Spitzberg (2006) — line 193 — **ACCURATE**

Claim: supplies "the evaluative criteria of appropriateness and effectiveness that algorithmacy
adapts to environments lacking co-present evaluators."

`literature/cards/spitzberg2006.md`, verified against the version-of-record PDF, confirms
appropriateness and effectiveness as two of the five named outcome criteria (p. 648), with page
anchors independently checked in the 2026-08-29 sweep. Matches; no overstatement of the model's
"CMC channel as decision-maker" status, which the card is careful to distinguish from algorithmacy's
own mediator.

### Sutherland et al. (2020) — line 195 — **ACCURATE**

Claim: Gig Literacies "bifurcated pattern" — negative/weak correlation predicted for
*relationship-building* ("a strategy for off-platform disintermediation"), positive for the
remaining four (reputation management, self-presentation, productivity maintenance, transaction
risk mitigation).

The card lists the same five subdimensions verbatim ("reputation and ratings management,
self-presentation, productivity management, risk management, and relationship building") and
independently characterizes relationship-building as "a strategy for escaping mediation" — almost
the identical phrase the paper uses. Precise match, including the specific reasoning for why that
one subdimension is the outlier.

### Long and Magerko (2020) — line 211 — **UNVERIFIABLE AT CURRENT DEPTH**

Claim: "Long and Magerko (2020) trace the lineage across textual, digital, computational, and data
literacies, and their operationalizations remain confined to person–system dyads."

`literature/cards/longmagerko2020.md` is read at `abstract_only` depth and its "What it argues"
section describes only the paper's AI-literacy competency framework, not a stated lineage through
textual/digital/computational/data literacies. This specific historiographic claim about the
paper's literature review is plausible (Long & Magerko's CHI '20 related-work section does trace
prior literacy traditions) but is not confirmed by anything in the card, which never quotes or
paraphrases that section. The second half of the sentence ("operationalizations... confined to
person–system dyads") is supported: the card states "every competency is a relation between a
person and a technology... nothing in it requires a second human party." Flag only the lineage
clause for a first-hand check of the CHI paper's related-work section before Lima.

### Teece et al. (1997) — line 232 — **ACCURATE**

Claim: "A capability resides in organizational routines and administrative assets a firm owns and
deploys (Teece et al., 1997)."

`literature/cards/teece1997.md`, full text verified 2026-08-26 against the source PDF, confirms
this is "a faithful position attribution": capabilities are "embedded in organizational processes,"
"cannot be bought," and are "assembled in integrated clusters spanning individuals and groups" —
i.e., they live in the firm's own routines, which only the firm owns and deploys. Matches.

### Sandberg (2000) — lines 233, 235 — **ACCURATE**

Claim: examining "engine optimizers at the Volvo Car Corporation," Sandberg "demonstrated that
competence reflects an actor's qualitative conception of work" and "identified three interpretive
framings: optimizing separate technical components, balancing interacting qualities, or managing
the entire process from the customer's holistic perspective."

`literature/cards/sandberg2000.md`, page-verified against the scanned PDF 2026-08-26, confirms the
setting (Volvo Car Corporation, engine optimization department) and the three conceptions verbatim
from the source: "Conception 1 treats optimizing as optimizing separate qualities; conception 2 as
optimizing interacting qualities; conception 3 as optimizing from the customer's perspective." The
paper's paraphrase — "separate technical components" / "balancing interacting qualities" /
"managing the entire process from the customer's holistic perspective" — tracks the source closely
enough not to distort it. Two things worth noting rather than flagging as errors: (1) the paper
correctly omits the sample-size number (twenty, not fifty — the card records an earlier version
that had this wrong and has since corrected it, and PAPER.md carries no number here at all, so no
exposure), and (2) "the customer is an interpretive orientation toward the task rather than an
unseen counterpart reached through an opaque, binding intermediary" is the paper's own analytic
gloss built on top of Sandberg's finding, not a claim attributed to Sandberg himself, and it reads
that way (attached via the paper's own sentence, not inside Sandberg's reported finding). Matches
cleanly.

### Spitzberg and Cupach (1984) — line 235 — **ACCURATE, and correctly scoped**

Claim: "Spitzberg and Cupach (1984) argue, from the other direction, that interpersonal
communication competence is not an isolated individual attribute but a relational quality jointly
enacted and evaluated by interacting parties."

`literature/cards/spitzbergcupach1984.md` carries a **2026-08-26 correction** distinguishing two
separate claims the manuscript could attribute to this 1984 book: (1) competence as a jointly
enacted, interpersonally judged quality — sourced independently via a contemporaneous validation
study (ERIC ED279030) quoting the book directly at p. 151 ("relational in the sense that it is
sensitive to the implicit perceptions of the relationship held by the interactants") — the card
states "the manuscript's first use is safe as a position attribution to Spitzberg & Cupach (1984)";
and (2) the stronger "molar/molecular" no-free-inference-across-levels claim, which the card says
belongs to Spitzberg's *later* work (2015 chapters, 1989 handbook), not the 1984 book verbatim.

The line-235 sentence uses only claim (1) — "jointly enacted and evaluated by interacting parties"
— and never invokes molar/molecular language anywhere in lines 171–280. This is exactly the correct
scoping the card's correction calls for: the section draws only on the verified claim and avoids
the claim that needed re-attribution to Spitzberg (2015). No drift.

### Laupichler et al. (2023) — line 241 — **DRIFTED (mild)**

Claim: "Laupichler et al. (2023) developed the SNAIL scale to evaluate formal AI-literacy
coursework, measuring declarative knowledge acquired through explicit curricula."

`literature/cards/laupichler2023.md`, abstract verified 2026-08-26, confirms SNAIL's declared
purpose ("designed to enable the evaluation of AI literacy courses' teaching effectiveness") — that
half of the sentence is accurate. But the instrument's actual structure, confirmed by the same
card, is a **three-factor solution**: Technical Understanding, Critical Appraisal, and Practical
Application. Only the first factor is straightforwardly "declarative knowledge"; the card itself
says these three factors are "the tidiest summary of what this whole literature measures," and
explicitly characterizes Critical Appraisal as evaluative judgment "about a system" and Practical
Application as use of the system as "a tool" — neither is declarative recall. Calling the whole
instrument a measure of "declarative knowledge" understates two of its three validated factors.

**Suggested correction:** replace "measuring declarative knowledge acquired through explicit
curricula" with something that names the actual structure, e.g. — *"measuring technical
understanding, critical appraisal, and practical application acquired through explicit curricula"*
— or, if the contrast with algorithmacy's implicit-acquisition property is the only point needed,
soften to *"measuring AI-literacy competencies formal coursework is designed to instill."* Either
preserves the paragraph's actual argument (classroom instruction installs what a course can teach;
algorithmacy requires participation under stakes) without mischaracterizing SNAIL as a pure
knowledge test.

### Kellogg et al. (2020) — line 246 — **ACCURATE**

Claim: labor process theorists "conceptualize algorithmic workplaces as contested terrain centered
on direction, evaluation, and discipline (Kellogg et al., 2020)."

`literature/cards/kellogg2020.md`, full text, confirms the "6 Rs" typology sorted into exactly
three managerial functions: directing work through *restricting* and *recommending*, evaluating it
through *recording* and *rating*, disciplining it through *replacing* and *rewarding*. The paper's
three-way gloss — direction, evaluation, discipline — is Kellogg et al.'s own three-way sort,
correctly named. Matches precisely.

### Stark & Vanden Broeck (2024) — line 248 — **UNVERIFIABLE AT CURRENT DEPTH**

Claim: "Organizational theorists have detailed how platform designs exploit coordination gaps
(Stark & Vanden Broeck, 2024)."

No card exists for this source (checked `literature/cards/` and `literature/models/`; not found).
The source is used extensively and specifically elsewhere in PAPER.md (e.g., line 44, defining
coordinative co-optation itself: platforms "deploy algorithms to match unchosen parties, evaluate
their ongoing interactions, and unilaterally terminate accounts"), so the paper's authors clearly
have direct familiarity with the source. The specific phrase "exploit coordination gaps" at line
248 is a generic, low-specificity gloss consistent with that established usage, but nothing in this
audit can confirm or deny the precise wording against the source text. Low risk given the source's
otherwise-verified centrality to the paper, but flagged since no card backs this particular clause.

### Cameron (2024) — lines 248, 256 — **ACCURATE**

Claim (line 256, the load-bearing use in the Paradox section): "Cameron (2024) demonstrates how
on-demand workers navigate continuous, confined choices in ways that manufacture consent and
stabilize algorithmic labor regimes, and her model leaves unspecified the individual capacity
separating successful navigation from failure."

`literature/cards/cameron2024.md`, full text, confirms the mechanism precisely: "Algorithmic
management segments the work into a stream of small decisions, which allows more frequent and
narrower choice... Both [engagement and deviance tactics] elicit consent... The construct is the
constant and confined choice." The paper's "continuous, confined choices" is a faithful paraphrase
of the card's "constant and confined choice," and "manufacture consent" quotes Cameron's own title
almost verbatim ("How Algorithmic Management Manufactures Consent"). The clause "her model leaves
unspecified the individual capacity separating successful navigation from failure" is a fair
negative claim — nothing in the card's "What it argues" or "Relation to the argument" sections
describes Cameron as theorizing an individual competency variable; her paper documents *tactics*
(engagement vs. deviance) without a construct for the capacity that predicts which tactic set a
given worker uses successfully. This is the paper's own gap-identification move, correctly
grounded. Matches.

### Curchod et al. (2020) — lines 248, 252 — **line 252 ACCURATE; line 248 FLAG**

Line 252 claim: "Curchod et al. (2020) document the consequence, showing marketplace sellers
evaluated across a visibility gap by buyers they cannot observe or engage." `literature/cards/
curchod2020.md`, full text with wording independently checked against the accepted manuscript
2026-08-26, confirms this exactly: "buyers remained largely invisible to sellers, while sellers
felt entirely visible to buyers" — the visibility gap is the card's own central finding. Matches.

Line 248 claim (joint with Cameron): platform designs "generate consent through algorithmic
enrollment (Cameron, 2024; Curchod et al., 2020)." This is worth a second look. Cameron's paper is
explicitly and centrally about manufacturing consent (see above). Curchod et al.'s contribution, per
the card, is "a theory of power and agency" built on three structural features — a one-way
evaluation right, a visibility gap, and blocked exit — and the card never uses the word "consent" or
frames the sellers' situation as consent-manufacture; sellers are described as experiencing the
apparatus as "a sword of Damocles," which reads as domination documented, not consent elicited.
Pairing Curchod with Cameron under one "generate consent" citation may overstate what Curchod et
al. actually claim — their mechanism (visibility asymmetry, blocked exit) could plausibly *support*
a consent story, but the source itself does not make that argument the way Cameron's does. Not a
clear DRIFTED (the underlying facts Curchod reports are compatible with a consent account, and nothing
in the sentence quotes or paraphrases Curchod specifically), but flagged for the author to consider
narrowing the parenthetical to Cameron alone, or adding a clause distinguishing the two mechanisms.

### Katsh and Rifkin (2001) and Wing et al. (2021) — line 252 — **ACCURATE**

Claim: "Extending Katsh and Rifkin's (2001) 'fourth party,' Wing et al. (2021) argue that an
authoritative dispute system must guarantee participants procedural transparency, institutional
accountability, meaningful contestability, and informed consent."

`literature/cards/katsh2001.md` confirms Katsh and Rifkin coined "the fourth party" (after the two
disputants and the human third-party neutral) and that later work — explicitly naming "Wing,
Martinez, Katsh & Rule (2021)" — is the citable modern extension. `literature/cards/wing2021.md`
confirms the extension claim directly ("Twenty years on, the fourth party is no longer a metaphor")
and lists the design requirements: "transparency about the system's role, accountability for its
determinations, contestability, protection against embedded bias, and informed consent to the
process" — five total. PAPER.md names four of these five (procedural transparency, institutional
accountability, meaningful contestability, informed consent), omitting only "protection against
embedded bias." This is a faithful subset, not a distortion — all four named obligations are
verbatim-adjacent to items on the card's list, and dropping one of five does not misrepresent the
other four. Matches.

### Zhou et al. (2025) — line 252 — **DRIFTED**

Claim: "Algorithmic coordination regimes withhold each of these guarantees in turn: proprietary
decision rules stay unobservable (Rahman, 2021), automated determinations carry no accountable
office, contestation routes to the platform's own apparatus (Zhou et al., 2025), and default
enrollment substitutes for consent."

This is the same Zhou, Lei, Liu, Huang & Hou (2025) *APJHR* algorithmic-competency scale paper
cited earlier in the paper (lines 115–117) and confirmed via `literature/cards/zhou2025apjhr.md`.
Nothing in the card supports the specific empirical claim that "contestation routes to the
platform's own apparatus." The card's four dimensions are Understanding, Embracing, Leveraging, and
Remediating; the nearest candidate, *Remediating*, is defined in the card as "the capacity to
repair or supplement the system's deficiencies" (example item: "I can supplement AM's shortcomings
— imprecise navigation — through the help of WeChat groups or other tools") — a worker's individual
coping/workaround behavior, not a finding about institutional contestation or dispute-routing
architecture. Zhou et al. is a scale-validation paper about worker competency, not a study of
dispute-resolution or contestation channels; it makes no documented claim about where contestation
"routes." This looks like a citation pulled to fill a parallel-structure slot (one citation per
withheld guarantee) rather than one that actually supports the specific claim attached to it.

**Suggested correction:** either drop the citation and let the clause stand as an analytic claim
the paper is entitled to make on its own (opacity + bindingness jointly imply contestation has
nowhere else to go), or replace it with a source that actually documents contestation routing to
platform apparatus — Curchod et al. (2020), already cited two sentences later for the visibility
gap, is a stronger candidate: sellers in that study have no appeal channel outside the platform's
own rating system. E.g.: *"contestation routes to the platform's own apparatus (Curchod et al.,
2020)."*

### Felin et al. (2015) — line 256 — **ACCURATE, correctly scoped**

Claim: "The dynamic fulfills the aggregation requirement expected of micro-foundational
organizational theory (Felin et al., 2015)."

`literature/cards/felin2015.md` confirms a microfoundational account, per Felin, Foss and Ployhart,
"has to specify three things: individuals and their attributes, the processes and interactions
among them, and the mechanism by which the individual level aggregates to the collective outcome."
The paper cites only the aggregation piece — one of the three named requirements — and does not
claim Felin et al. endorse algorithmacy's specific aggregation mechanism or overstate the citation
into a broader claim about the whole microfoundations program. This is a narrow, checkable
attribution and it holds: "the aggregation requirement" is literally one of Felin et al.'s three
named specification requirements. Matches; appropriately modest given the card's own caution that
this is "a long review article... [that] does not settle the debates within it."

### Sutherland et al. (2020) — line 264 — **ACCURATE**

Claim: "Sutherland et al. (2020) show informal literacies shifting coordination burdens onto
labor."

Consistent with the card's framing throughout: gig literacies are the freelancer's own
"skills and work strategies... for using and working around the platform," assembled inductively
from what workers reported doing to manage risk, reputation, and productivity themselves — i.e.,
burdens the platform does not absorb and the worker must. Fair compression of the card's repeated
point that these are informally developed, worker-side compensations for structural gaps. No
citable page or figure attached to this clause, so nothing more specific to check; reasonable as
background-adjacent characterization.

### Hargittai (2002) — line 268 — **UNVERIFIABLE AT CURRENT DEPTH — no card exists**

Claim: "The proposition transposes the logic of second-level digital divides (Hargittai, 2002) from
general digital literacy to triadic algorithmic coordination."

No card exists for Hargittai (2002) specifically. `literature/cards/` contains only
`hargittai2020.md` (Hargittai, Gruber, Djukaric, Fuchs & Brombach, "Black box measures?," 2020,
a different paper on algorithm-skill measurement methodology) and `klawitterhargittai2018.md`
(Klawitter & Hargittai, 2018, on creative-goods marketplace sellers). Neither is the 2002 *First
Monday* paper cited here. The bibliography entry (line 405) is bibliographically correct — "Second-
level digital divide: Differences in people's online skills," *First Monday* 7(4) — and the general
characterization used ("second-level digital divide," i.e., a skills-based divide among people who
already have access, as distinct from the first-level access divide) matches the well-established
public description of that paper. But this audit found no local card and no direct-read verification
to confirm the specific framing against the source text itself, so it is flagged rather than marked
ACCURATE. Recommend building a card for this source before Lima, given the construct now rests two
full propositions on it (Proposition 2 depends on this transposition).

---

### Out-of-range items checked anyway

**Henseler et al. (2015) / HTMT — not present in lines 171–280.** The audit brief asked for this
citation to be checked as part of the Algorithmacy construct section, but it does not appear
anywhere in lines 171–280. It occurs at PAPER.md line 638 (Study 2 measurement plan, well outside
the assigned section): "I evaluate discriminant validity with the heterotrait-monotrait ratio of
correlations (HTMT; Henseler et al., 2015). An HTMT value exceeding the conservative .85 threshold
between any proposed operation and a neighboring subscale falsifies the claim of construct
distinctiveness on that dimension." No card exists for this source in `literature/cards/` or
`literature/models/`. Checked anyway: the method name (heterotrait-monotrait ratio of correlations)
and the .85 figure as the *more conservative* of Henseler et al.'s two proposed cutoffs (.85 stricter,
.90 more liberal, depending on how conceptually distinct the constructs are expected to be) match
the well-established public description of this widely cited methods paper. This characterization
is plausible but not verified against a local card or direct source read — flag as
UNVERIFIABLE AT CURRENT DEPTH, and note for the author that it belongs in a different batch (5 or 6)
given its actual location in the manuscript.

**Second Suddaby (2010) "bounded behavioral construct" use — not present in lines 171–280.** The
audit brief describes Suddaby as "cited twice... for construct-clarity criteria... and for the
'bounded behavioral construct' framing." Only one Suddaby citation falls inside lines 171–280 (line
173, checked above as ACCURATE). The "bounded behavioral construct" phrase and its Suddaby citation
occur at PAPER.md line 31, in the Introduction — outside the assigned section. Checked anyway:
"Algorithmacy is a bounded behavioral construct: it defines the sensibility the triad demands of a
participant and stops there, leaving institutional justice to the governance literatures equipped to
judge it (Suddaby, 2010)." This is a reasonable application of Suddaby's "scope conditions" element
(when a construct does and does not apply) rather than a distinct claim requiring separate
verification — it is the paper's own move, licensed by Suddaby's framework rather than attributed to
him as a specific finding. No drift, but flag the location for whichever batch actually covers line
31 (Batch 1).

---

### Summary table

| Citation | Line(s) in range | Verdict |
|---|---|---|
| Suddaby (2010) | 173 | ACCURATE |
| Hayek (1945); Simon (1997); Weber (1978) | 181 | BACKGROUND |
| Sutherland et al. (2020) | 183 | ACCURATE |
| Zhou et al. (2025) | 189 | ACCURATE |
| Rahman (2021) | 191, 209, 242, 264 | ACCURATE |
| Spitzberg (2006) | 193 | ACCURATE |
| Sutherland et al. (2020) | 195 | ACCURATE |
| Long and Magerko (2020) | 211 | UNVERIFIABLE AT CURRENT DEPTH |
| Teece et al. (1997) | 232 | ACCURATE |
| Sandberg (2000) | 233, 235 | ACCURATE |
| Spitzberg and Cupach (1984) | 235 | ACCURATE (correctly scoped) |
| Laupichler et al. (2023) | 241 | DRIFTED (mild) |
| Kellogg et al. (2020) | 246 | ACCURATE |
| Stark & Vanden Broeck (2024) | 248 | UNVERIFIABLE AT CURRENT DEPTH |
| Cameron (2024) | 248, 256 | ACCURATE |
| Curchod et al. (2020) | 248, 252 | FLAG (248) / ACCURATE (252) |
| Katsh and Rifkin (2001) | 252 | ACCURATE |
| Wing et al. (2021) | 252 | ACCURATE |
| Zhou et al. (2025) | 252 | DRIFTED |
| Felin et al. (2015) | 256 | ACCURATE |
| Sutherland et al. (2020) | 264 | ACCURATE |
| Hargittai (2002) | 268 | UNVERIFIABLE AT CURRENT DEPTH — no card |
| Henseler et al. (2015) [out of range] | 638 | UNVERIFIABLE AT CURRENT DEPTH — no card |
| Suddaby (2010), "bounded behavioral construct" [out of range] | 31 | ACCURATE |

**Two items need author attention before Lima:**
1. **Laupichler et al. (2023), line 241** — "declarative knowledge" understates SNAIL's three-factor
   structure (Technical Understanding, Critical Appraisal, Practical Application). Reword per the
   suggested correction above.
2. **Zhou et al. (2025), line 252** — "contestation routes to the platform's own apparatus" is not
   supported by the algorithmic-competency scale paper. Drop the citation or replace with Curchod et
   al. (2020), which does document exactly this.

Three items need a card built before they can be marked ACCURATE: Long and Magerko (2020)'s lineage
clause (line 211), Stark & Vanden Broeck (2024) (line 248), and Hargittai (2002) (line 268, no card
exists at all despite carrying two full propositions).

---

## Batch 1: Abstract + Introduction + Coordination-Form Gap

Scope checked: `manuscript/PAPER.md` lines 1–46 (Abstract, Introduction, The Coordination-Form Gap).
No citations appear in the Abstract itself (lines 7–11) — all its claims are stated without
parenthetical citation. Every citation in the Introduction and Coordination-Form Gap is listed below
in order of first appearance. Cards read: `bucher2017.md`, `devito2018.md`, `litt2012.md`,
`wilkinson1965.md`, `aneesh2009.md`, `danaher2016.md`, `zhou2025.md`, `zhou2025apjhr.md`,
`longmagerko2020.md`, `guzmanlewis2020.md`, `hancock2020.md`, `katsh2001.md`, `rosenblatstark2016.md`,
`curchod2020.md`. Three sources cited here have no card in `literature/cards/` at all — Manky (2025),
Selznick (1949), and Stark & Vanden Broeck (2024)/Stark & Pais (2020) — so each was checked against
either a WebSearch of the publisher record (Manky, Selznick) or a full-text card that exists in the
adjacent `dissertation/research/library/` tree (`starkpais2020.md`, `stark2024.md`, `stark2024b.md`,
`selznick1949.md`), which this audit read directly since it was the more authoritative source
available.

### Zhou et al. (2025) — lines 17, 27 — **ACCURATE, but FLAG: bare-citation ambiguity**

Line 17 claim: "Recent research identifies the capacities workers deploy directly against an
automated system (Zhou et al., 2025), and leaves the human counterpart outside the analytical
frame." Line 27 claim: "Zhou et al. (2025) reduce the human evaluator to an external score."

Both claims match `zhou2025apjhr.md` (Zhou, Lei, Liu, Huang & Hou, *Asia Pacific Journal of Human
Resources*, the algorithmic-competency scale paper): the four-dimension construct (Understanding,
Embracing, Leveraging, Remediating) is a worker's capacity aimed at the platform apparatus, and the
card is explicit that "the counterpart enters their study only as an *outcome variable* —
customer-oriented service behaviour" and that Item 8 treats the customer/counterpart as "a rating
source feeding the algorithm, an output to be minimised, not a party being coordinated with" — which
is exactly "reduce the human evaluator to an external score." Both instances are ACCURATE against
their source.

**FLAG, repeated from Batches 2 and 4's findings on this same source-ambiguity problem:** there are
two different Zhou, Lei et al. 2025 papers in the library, and both cards explicitly warn against
ever citing "Zhou et al., 2025" bare. `zhou2025apjhr.md`'s own caution: *"Never cite this bare as
'Zhou et al. 2025': an overlapping team published a different 2025 paper (Zhou, Lei, Cooke, Huang &
Zhang, Human Resource Management 64(6))... and the two are routinely confused."* `zhou2025.md`'s
(the HRM paper's) caution says the same in reverse. PAPER.md's in-text citations at lines 17 and 27
are bare "Zhou et al., 2025" with no disambiguating detail, exactly the form both cards warn against.
The claims themselves are correctly matched to the APJHR paper's content, so this is not a content
drift, but a reviewer who knows the literature (or who checks the reference list) may not be able to
tell which Zhou et al. 2025 is meant without inspecting the full reference entry. **Fix:** either add
a disambiguating word at first use ("Zhou et al.'s (2025) scale of algorithmic competency...") or
confirm the reference-list entry is unambiguous and leave the in-text form as is — but do not treat
this as already resolved, since the same bare form recurs at both instances in this section.

### Bucher (2017) — line 19 — **ACCURATE**

Claim: "Bucher (2017) shows that ordinary users build working theories of an opaque feed algorithm —
an *algorithmic imaginary* — and act on what they believe it wants."

`bucher2017.md` confirms this from the published abstract (retrieved via OpenAlex): Bucher studies
"personal stories about the Facebook algorithm gathered through tweets and interviews with 25
ordinary users," from which she develops "the algorithmic imaginary — ways of thinking about what
algorithms are, what they should be and how they function," arguing the imaginary "plays a
generative role in moulding the algorithm itself" — i.e., users act on their beliefs about it.
Matches.

### DeVito et al. (2018) — line 19 — **ACCURATE**

Claim: "DeVito et al. (2018) find those folk theories assembled from many sources and put to work in
the service of self-presentation."

`devito2018.md` confirms both halves directly: "people draw on diverse sources when forming
theories... talk, press coverage, platform statements, inference from others' outcomes," and "folk
theorisation is put in service of self-presentation." Matches precisely — this is close to the
card's own summary language.

### Litt (2012) — line 19 — **ACCURATE**

Claim: "Litt (2012) names the *imagined audience*, the mental picture of unseen others against which
a person calibrates a message she cannot watch land."

`litt2012.md` (abstract_only, publisher_summary) confirms: Litt "names and theorizes the imagined
audience: the mental conceptualization a person builds of who they are communicating with when the
actual audience for an act of online disclosure cannot be directly observed," treating that imagined
composition "as the thing self-presentation is calibrated against." Matches; the card's own caution
(don't attribute a specific empirical design to this 2012 article from memory — that belongs to Litt
& Hargittai 2016) is not triggered, since the paper attributes no empirical design to Litt here.

### Manky (2025) — lines 19, 29 — **ACCURATE (verified independently; no local card exists)**

Line 19 claim: "Manky (2025) watches ride-hailing drivers in Lima read opaque platform metrics to
judge whether a passenger is safe to accept." Line 29 claim: "reading a black-box metric is how a
driver decides whether a stranger is safe to pick up (Manky, 2025)."

No card for this source exists in `literature/cards/`. The lab's own research memos
(`GAPS.md` N4, `CONTEXT_AND_REGION_2026-08-26.md` §2.1) record the finding from a search-record
read, not a formal card, so per instructions this was independently verified by WebSearch against
the publisher record. Confirmed: Manky, O., "Reimagining Work Security in Latin America's Platform
Economy: Workers' Strategies Amid Urban Violence," *New Technology, Work and Employment* 41(1) (2025)
— "draws on 40 in-depth interviews and more than 35 informal conversations with [Lima ride-hailing]
drivers... showing how drivers value platforms not for formal job security, but for mitigating
physical risks, enabling cashless transactions, and providing data-driven oversight of passengers and
routes." The paper's characterization ("read opaque platform metrics to judge whether a passenger is
safe to accept," "reading a black-box metric... decides whether a stranger is safe to pick up")
matches the "data-driven oversight of passengers" / physical-risk-mitigation finding, and the N=40
figure (used later in the paper, at line 169, outside this section) is confirmed correct. The word
"opaque"/"black-box" is the paper's own framing gloss, not language drawn from Manky's abstract
itself, but it is a fair characterization — Manky's own framing is that drivers use platform data
they did not design and cannot fully audit to make safety judgments. No drift found; recommend
building a proper card for this source given it is used twice here and again at line 169, since the
current basis for the claim is a research memo rather than a verified card.

### Wilkinson (1965) — line 21 — **ACCURATE claim; FLAG: unresolved venue ambiguity**

Claim: "the last of these named by Wilkinson (1965), who argued that speaking and listening deserved
the standing schooling already granted reading and counting."

`wilkinson1965.md` (metadata_only) confirms the substance: Wilkinson "names 'oracy' as a general
ability in the oral skills of speaking and listening, arguing it deserves the same standing in
schooling as literacy and numeracy." The claim is ACCURATE.

The card carries an explicit, unresolved caution the task asked to check again: **two different 1965
Wilkinson items share the identical title "The Concept of Oracy"** — one in *Educational Review*
17(4):11–15, one in a different venue (retrospectively titled *English in Education* 2(A2):3–5, dated
three months earlier) — both genuine, Crossref-verified DOIs. The card recommends the *Educational
Review* version because "secondary literature overwhelmingly cites" it, and flags that "a library
check of the actual offprint is worth doing before the citation goes to print." PAPER.md's reference
list (line 493) cites *Educational Review* 17(4), 11–15 — the card's recommended choice — so the
citation is not wrong, but the body text does not hedge, and the underlying venue question the card
raised has not been independently resolved (no offprint check was performed by this audit or, as far
as the record shows, by anyone). This is not a content drift but an open verification item worth a
final check before the citation is locked in for print.

### Aneesh (2009) and Danaher (2016) — line 23 — **ACCURATE**

Claim: "Aneesh (2009) uses *algocracy* for a mode of organization — rule by code, set beside
bureaucracy and the market as a third way of coordinating dispersed labor — whereas algorithmacy
names the individual capacity a person exercises inside such an arrangement (see also Danaher,
2016). One is a property of the system; the other, of the person acting within it."

`aneesh2009.md` confirms this precisely: Aneesh studies transnationally coordinated labor and argues
"a third organizing principle governs this arrangement, distinct from the two [bureaucracy and
market]... bureaucracy runs on legal-rational authority, the market runs on price, and this third
form... algocracy... runs on the programming scheme and the algorithm itself," coordinating
"dispersed labor." The sentence "One is a property of the system; the other, of the person acting
within it" is close to verbatim from the card's own suggested disambiguating language ("One is a
property of the system; the other is a property of the person acting inside the system"). Danaher
(2016) is cited only as a parenthetical "see also" alongside Aneesh, with no separate specific claim
attached, consistent with `danaher2016.md`'s own account of Danaher's "algocracy" as a macro/
institutional-level diagnosis — background use, correctly consistent with the card. Matches.

### Stark and Vanden Broeck (2024) — line 25 — **split verdict: first clause ACCURATE, second clause DRIFTED**

The paragraph makes two separate, checkable claims about this source:

1. "Stark and Vanden Broeck (2024) define the departure by observing that while actors in
   hierarchies command, in markets contract, and in networks collaborate, on platforms they are
   co-opted." — **ACCURATE.** `literature/REFERENCES.md`'s prior verification pass quotes their
   abstract directly: *"Whereas actors in hierarchies command, in markets they contract, and in
   networks collaborate, on platforms they are co-opted."* The full-text card
   `dissertation/research/library/stark2024.md` (read directly for this audit) confirms the same
   line appears verbatim on p. 1 and is repeated on p. 5 of the article. Exact match.

2. "*Coordinative co-optation* is the name Stark and Vanden Broeck (2024) give that arrangement..."
   — **DRIFTED.** This is a specific, checkable attribution: that the compound term "coordinative
   co-optation" — the paper's own central construct name and title term — comes from Stark and
   Vanden Broeck. It does not. The full-text cards for both of their relevant papers
   (`dissertation/research/library/stark2024.md`, the *Organization Theory* English version, and
   `stark2024b.md`, the *Revista MAD* Spanish version reproducing the same argument) were searched
   directly against their underlying full-text files
   (`dissertation/research/library/pdfs/stark2024.txt`) for the string "coordinative" and it does
   not appear anywhere in either. The same check against `starkpais2020.md`'s underlying text
   (`pdfs/starkpais2020.txt`) — the earlier Stark & Pais (2020) paper that actually originates the
   four-verb formulation Stark and Vanden Broeck repeat — also returns no match. What Stark and
   Vanden Broeck call the arrangement, per their own Table 1 and running text, is simply
   **"co-optation"** (a verb/noun, "platforms co-opt," "the co-optation of actors, assets, and
   activities") inside their broader account of "algorithmic management" as a management style —
   never the compound "coordinative co-optation." That compound term appears to be this
   dissertation's own coinage, built on Stark and Pais's/Stark and Vanden Broeck's raw "co-optation"
   concept but not their name for it.

   **Suggested fix:** attribute the compound term to the paper's own construction rather than to the
   source, e.g. — *"I name that arrangement* coordinative co-optation*, building on Stark and Vanden
   Broeck's (2024) 'on platforms they are co-opted'; a reader's intuition for co-optation will
   misfire without a gloss."* This preserves everything else in the sentence and the paragraph that
   follows while correcting the specific authorship claim.

### Selznick (1949) — lines 25, 40, 44 — **ACCURATE**

Claim (line 25): "In Selznick's (1949) classical sense, an organization absorbs an external
challenger by conferring a seat on him: opposition becomes participation, and the seat carries a
formal standing." Repeated in compressed form at line 40 ("An external challenger accepts a
conferred administrative seat, transforming outside opposition into structured institutional
participation") and line 44 ("Selznick's absorbed challenger at least received a seat").

No card exists in `literature/cards/`, but a full-text card exists at
`dissertation/research/library/selznick1949.md` (read directly for this audit, built from the full
Internet Archive OCR of *TVA and the Grass Roots*). It confirms Selznick's verbatim definition —
"cooptation is the process of absorbing new elements into the leadership or policy-determining
structure of an organization as a means of averting threats to its stability or existence" — and
that his **formal cooptation** variant works through "openly avowed relationships — appointments,
contracts, advisory bodies," where "what is shared is the responsibility for power, not power
itself." PAPER.md's gloss ("conferring a seat," "opposition becomes participation," "the seat
carries a formal standing" — i.e., standing without real power) tracks this precisely. One thing to
note rather than flag: Selznick actually splits cooptation into **formal and informal** variants, and
the card stresses this distinction matters for the platform case ("the platform case sits closer to
informal cooptation... than to seating anyone on a board"). PAPER.md's "classical sense" collapses
this to a single reading — the formal one — without naming the split. That is a defensible
compression for a one-clause gloss, not a misstatement of what is there, so this is not marked
DRIFTED, but the author should know the simplification exists if a reviewer versed in the
co-optation literature raises the formal/informal distinction.

### Long and Magerko (2020) — line 27 — **ACCURATE**

Claim: "Long and Magerko (2020) treat the algorithm as an object of formal knowledge, leaving no
communicative counterpart in view."

`longmagerko2020.md` confirms directly: "the one that makes the algorithm an object of knowledge...
Nothing in it requires a second human party whose wants must be reconstructed... the counterpart has
no place to go." Matches (the paper's "object of formal knowledge" is a light paraphrase of the
card's "object of knowledge," immaterial).

### Guzman and Lewis (2020) — line 27 — **ACCURATE**

Claim: "Guzman and Lewis (2020) seat the machine itself in the interlocutor position, leaving the
far-side human untheorized."

`guzmanlewis2020.md` confirms: "the construct that makes the algorithm a partner — an interlocutor
in its own right, studied as a human-machine dyad... the machine is moved onto one axis of a
two-party relation, and the third position never appears." Matches, including the "interlocutor"
language drawn directly from the card.

### Hancock et al. (2020) — line 27 — **ACCURATE**

Claim: "Hancock et al. (2020) model the artifact as a delegate acting on a sender's behalf."

`hancock2020.md` confirms AI-mediated communication's agent "operates on behalf of a communicator,"
optimizing "for a party's goal — it is a delegated instrument, aligned with the sender or the
receiver." Notably, the card's own "Relation to the argument" section flags an *earlier* version of
this citation as vulnerable ("the first three inherit a dyad" — a description the card calls "the
most vulnerable sentence in the section") and recommends exactly the "delegate... on a sender's
behalf" framing PAPER.md now uses. The current text appears to have already incorporated that fix.
Matches.

### Katsh and Rifkin (2001) — line 27 — **ACCURATE**

Claim: "Online dispute resolution scholarship recognized the configuration through Katsh and
Rifkin's (2001) 'fourth party,' and theorized it from the perspective of system design rather than
participant capacity."

`katsh2001.md` (extended_preview, direct_read of chs. 1–4) confirms both halves precisely: Katsh and
Rifkin name "the fourth party" — after the two disputants and the human third-party neutral — and the
card states in its own words, "ODR theorises the system's design, not the disputant's competence...
Nobody in ODR asks what capacity a disputant needs to fare well against an undisclosed fourth party."
Near-verbatim match to the card's own framing.

### Suddaby (2010) — line 31 — **BACKGROUND**

"Leaving institutional justice to the governance literatures equipped to judge it (Suddaby, 2010)" —
a general pointer to institutional-theory scholarship on legitimacy/justice, with no specific finding
attributed. Consistent with Batch 4's finding on the nearby "bounded behavioral construct" use of
this same source at this same line (checked there as an application of Suddaby's scope-conditions
element, not a distinct empirical claim). Background, not re-verified further here.

### Simon (1997); Weber (1978); Hayek (1945); Granovetter (1985); Powell (1990) — lines 37–39 — **BACKGROUND**

The four classical-form citations (hierarchy: Simon and Weber; market: Hayek; network: Granovetter
and Powell) each anchor a single well-known, uncontested concept (zone of acceptance / bureaucratic
authority; the price mechanism as aggregated information; embedded, reciprocal social ties) with no
further specific claim attached. No cards exist for any of the five in `literature/cards/`; consistent
with Batch 4's treatment of the identical citation set at line 181 (also marked BACKGROUND, not
independently checked further there either). Not re-verified beyond the existence sweep already
completed 2026-08-29.

### Stark & Pais (2020) and Stark & Vanden Broeck (2024) — line 44 — **ACCURATE**

Claim: "This fifth coordination form operates through automated enrollment: digital platforms deploy
algorithms to match unchosen parties, evaluate their ongoing interactions, and unilaterally terminate
accounts (Stark & Pais, 2020; Stark & Vanden Broeck, 2024)."

This exact concern (whether the sources actually support calling co-optation a "coordination form"
positioned against the classical triad) was raised and closed once already, per `DEPARTURES.md` row
1, against an earlier draft of this sentence: "the manuscript says *form*, not *mechanism*, and
positions neither source against Powell." The current sentence still says "form," not "mechanism,"
and still does not claim Stark and Pais or Stark and Vanden Broeck themselves make the
Powell-comparison — that framing is the paper's own. The specific mechanics are supported: the
full-text `starkpais2020.md` card confirms "enrolling them in algorithmic management 'without
managerial authority having been delegated to them'" (enrollment/matching) and ratings
"algorithmically translated into rankings" (evaluating ongoing interactions); a direct search of the
underlying Stark & Pais full text (`pdfs/starkpais2020.txt`) turns up footnote 21, "For an analysis
of deactivations at Uber, see Rosenblat (2018)" — a passing reference that loosely supports
"unilaterally terminate accounts" but attributes the deactivation finding itself to Rosenblat, not to
Stark and Pais directly. This is a minor looseness, not a misattribution requiring a fix: the
sentence cites Stark and Pais/Stark and Vanden Broeck for the general mechanism (enrollment, matching,
evaluation), not for a specific finding about termination rates. No drift found; the prior closure
holds against the current wording.

### Rosenblat & Stark (2016) and Curchod et al. (2020) — line 46 — **ACCURATE**

Claim: "Macro-structural scholarship examines how platform firms leverage informational asymmetries
(Rosenblat & Stark, 2016) and non-portable reputational ratings (Curchod et al., 2020) to enforce
administrative control."

`rosenblatstark2016.md` confirms: "the platform's power over drivers runs on information
asymmetries. Uber holds the data, sets the rules, changes them unilaterally and communicates
selectively." `curchod2020.md` confirms the "non-portable" characterization specifically: "blocked
exit, because reputation cannot be rebuilt elsewhere," inside a triadic power-asymmetry account the
card explicitly frames as a challenge to hierarchical-power/administrative-control theory. Both
match.

### Summary table

| Citation | Line(s) | Verdict |
|---|---|---|
| Zhou et al. (2025) | 17, 27 | ACCURATE, but FLAG bare-citation ambiguity (two 2025 Zhou et al. papers) |
| Bucher (2017) | 19 | ACCURATE |
| DeVito et al. (2018) | 19 | ACCURATE |
| Litt (2012) | 19 | ACCURATE |
| Manky (2025) | 19, 29 | ACCURATE (verified via WebSearch; no local card) |
| Wilkinson (1965) | 21 | ACCURATE claim; FLAG unresolved venue ambiguity |
| Aneesh (2009) | 23 | ACCURATE |
| Danaher (2016) | 23 | ACCURATE / BACKGROUND |
| Stark and Vanden Broeck (2024) — "command/contract/collaborate/co-opted" | 25 | ACCURATE |
| Stark and Vanden Broeck (2024) — "coordinative co-optation is the name [they] give" | 25 | **DRIFTED** |
| Selznick (1949) | 25, 40, 44 | ACCURATE |
| Long and Magerko (2020) | 27 | ACCURATE |
| Guzman and Lewis (2020) | 27 | ACCURATE |
| Hancock et al. (2020) | 27 | ACCURATE |
| Katsh and Rifkin (2001) | 27 | ACCURATE |
| Suddaby (2010) | 31 | BACKGROUND |
| Simon (1997); Weber (1978); Hayek (1945); Granovetter (1985); Powell (1990) | 37–39 | BACKGROUND |
| Stark & Pais (2020); Stark & Vanden Broeck (2024) | 44 | ACCURATE |
| Rosenblat & Stark (2016) | 46 | ACCURATE |
| Curchod et al. (2020) | 46 | ACCURATE |

**One item needs a fix before Lima:**
1. **Stark and Vanden Broeck (2024), line 25** — "*Coordinative co-optation* is the name Stark and
   Vanden Broeck (2024) give that arrangement" misattributes the paper's own compound construct term
   (also the article's title term) to a source whose full text — checked directly — never uses the
   word "coordinative." Reword to credit the paper itself with the coinage, built on their verified
   "co-optation" language (see suggested fix above).

**Two items are open verification loose ends, not drifts:**
2. **Zhou et al. (2025), lines 17 and 27** — bare in-text form risks confusion between two different
   2025 Zhou et al. papers; both cards explicitly warn against this. Add a disambiguating word or
   confirm the reference list resolves it unambiguously.
3. **Wilkinson (1965), line 21** — the card's own caution about two identically-titled 1965 venues
   remains unresolved by an offprint check; the current citation matches the card's recommended
   choice, so this is not wrong, just not yet independently confirmed.

**One source used twice in this section has no local card and should get one:** Manky (2025) — the
claim checked out against an independent WebSearch of the publisher abstract, including the N=40
figure, but the paper cites this source three times total (twice in this section, once at line 169)
without a literature card backing it.

## Batch 6: Appendix B (continued) + Appendix C + minor/boundary-case citations

Scope: PAPER.md lines 526–656 (Appendix B's Action Research Design / Instrument Architecture /
Empirical Protocol subsections and all of Appendix C), plus the boundary-case and minor-background
citations scattered elsewhere in the paper that the task specified by name. Per the task's
instructions, only the citations named below were checked — general Appendix B/C citations not named
(Merton 1987, Eisenhardt & Graebner 2007, Bamberger & Pratt 2010, Bothello et al. 2019, Riordan 1995
as cited in Coghlan & Brannick 2014, Anteby 2013, Ferguson et al. 2004, Mercer 2007, Pratt et al.
2020, Tracy 2010, Yurek et al. 2008) are left for whichever batch has that remit.

### Pratt (2009) — line 532 — **ACCURATE (card is abstract-only; moderate confidence)**

Claim: "Following Pratt (2009), qualitative rigor depends on alignment between method and the
underlying theoretical puzzle rather than adherence to generic templates."

The card (`pratt2009.md`, abstract-only, evidence basis `citing_literature`) reconstructs Pratt's
argument as: qualitative research has no boilerplate, and reviewers/authors both suffer for treating
one method template as the standard of rigor; his advice is to justify sampling by the theoretical
question and make the analytic process visible rather than imitate a generic checklist. The article's
own title — "For the lack of a boilerplate" — directly supports "rather than adherence to generic
templates." The manuscript's paraphrase matches this closely. Flag only the card's own caution: it is
an editorial that prescribes, not an empirical study, and Pratt's position develops further in Pratt,
Kaplan & Whittington (2020) — citing the 2009 piece alone is defensible but slightly dates the point.
No change needed.

### Timmermans & Tavory (2012) — the three abductive moves, lines 581–585 — **ACCURATE, and internally consistent**

Claim: Appendix B elaborates the three moves in more detail than anywhere else in the paper —
Revisiting ("returning repeatedly to inscribed transcripts across multiple passes to examine how
emergent categories reframe earlier observations"), Defamiliarization ("treating automated
transcription as a technique of analytical estrangement, subjecting self-evident participant
explanations to theoretical scrutiny"), Alternative Casing ("evaluating raw transcripts against
competing frameworks... to establish whether the data demand the triadic construct").

Checked against `timmermans2012.md` (full_text depth): Revisiting is "returning to the same
observation repeatedly as it is inscribed (field notes, transcripts, coding, memos)... whose relevance
changes with each return" — matches. Defamiliarization is "inscription itself... as a technique of
estrangement... so that what was taken for granted becomes a possible focal point" — the manuscript's
"automated transcription" is the paper's own domain-specific instance of "inscription," a legitimate
operationalization rather than a distortion. Alternative Casing is "deliberately working a data
excerpt against multiple theoretical frameworks in turn... to render the phenomenon a case of more
than one thing before settling" — matches, including the manuscript's specific rival framings
(individual skill acquisition, relational gig literacies, dyadic sensemaking), which are the same
three rivals named at line 622 (Study 1) and line 327 (main text). All three descriptions are accurate
to the source.

Internal consistency: the only other place the manuscript invokes Timmermans & Tavory is line 286
("Data collection and analysis follow an abductive protocol (Timmermans & Tavory, 2012)"), which is a
bare gesture with no detail to contradict. Appendix B is therefore the paper's only detailed
description of the three moves, and there is nothing elsewhere for it to conflict with — the
consistency check passes trivially rather than substantively, and it should be noted that Appendix B
carries the entire explanatory weight for a citation used four times across the paper.

### Blumer (1954), Bowen (2006), Gioia et al. (2013) — line 587 — **ACCURATE**

Claim: "The three operations function as sensitizing concepts (Blumer, 1954; Bowen, 2006). Initial
coding adheres to first-order, participant-centric terminology (Gioia et al., 2013) before
second-order categories are applied. A disconfirming negative case is specified in advance..."

Blumer (1954, card abstract-only): sensitizing concepts orient attention without prescribing what will
be found — matches the manuscript's use. Bowen (2006, card full-text): Bowen's own JSIF study
specified three sensitizing concepts *in advance* (participation, social capital, empowerment) and
reports discarding two of them when they did not survive contact with the data — this is the exact
precedent for "specified in advance" and for treating a negative case as a legitimate, plannable
outcome rather than an ad hoc hedge. Gioia et al. (2013, card full-text): "first-order codes in
informant terms... second-order themes in researcher/theoretical terms" is quoted almost verbatim by
the manuscript's "first-order, participant-centric terminology... before second-order categories are
applied." One nuance worth flagging: the "negative case... specified in advance" sentence itself
carries no citation at that exact point — it follows from, but is not directly footnoted to, Bowen's
demonstrated practice. That is not a misattribution (nothing false is attached to a source), just an
uncited methodological move that Bowen's card would actually strengthen if cited explicitly. No
change required, but citing Bowen a second time at that sentence would tighten the paragraph.

### Flanagan (1954) — critical incident technique, four-part structure, line 579 — **DRIFTED**

Claim: "Each module applies the critical incident technique (Flanagan, 1954), prompting participants
to detail a complete behavioral episode: the baseline objective, the system determination, the
tactical adaptation, and the resolution."

No card exists for Flanagan (1954) anywhere in the lab's literature/cards or dissertation/research/
library directories. Verified instead against the source directly: Flanagan's 1954 *Psychological
Bulletin* article specifies the critical incident technique as a **five-step research procedure** —
(1) determine the general aim of the activity, (2) develop plans and specifications for what counts as
an effective/ineffective incident, (3) collect the data (interview or written report), (4) analyze the
data, (5) interpret and report the findings — not a four-part structure for narrating a single
incident. The technique's classic definition of an *individual incident* itself is built from a
situation/context, a specific observable behavior, and a clear-enough outcome — again not "baseline
objective, system determination, tactical adaptation, resolution."

The four labels the manuscript uses are a domain-specific elaboration built for this paper's own
gate/algorithm context (an objective, an automated determination, the participant's response, an
outcome) — a reasonable operationalization of what an "incident" needs to contain, but it is presented
as though these four terms *are* Flanagan's technique ("applies the critical incident technique
[Flanagan, 1954]... the baseline objective, the system determination, the tactical adaptation, and the
resolution"), when they do not appear in Flanagan's own five-step procedure or in his definition of an
incident. This reads as an invented elaboration attributed to the source rather than flagged as the
paper's own adaptation.

**Suggested correction** (attributes the four-part breakdown to the paper's own design rather than to
Flanagan directly):

> Each module applies the critical incident technique (Flanagan, 1954), prompting participants to
> detail a complete behavioral episode — operationalized here as the baseline objective, the system
> determination, the tactical adaptation, and the resolution.

This keeps Flanagan as the citation for the *technique* (eliciting a specific, complete behavioral
episode rather than a generalization) without implying the four labels are his own terminology.

### Henseler et al. (2015) — HTMT, .85 threshold, line 638 — **ACCURATE, and the only instance in the paper**

Claim: "I evaluate discriminant validity with the heterotrait-monotrait ratio of correlations (HTMT;
Henseler et al., 2015). An HTMT value exceeding the conservative .85 threshold between any proposed
operation and a neighboring subscale falsifies the claim of construct distinctiveness on that
dimension."

No card exists for this source. A full-text search of PAPER.md shows Henseler appears exactly once in
the body (line 638, this Appendix C instance) plus once in the reference list (line 411) — there is no
separate main-text instance to check for consistency against, so the task's premise of a duplicate
main-text citation does not hold for this manuscript as currently written. On the substance: Henseler,
Ringle & Sarstedt (2015) is accurately characterized. HTMT is their proposed criterion for
discriminant validity in variance-based SEM, and .85 (conservative, for conceptually distinct
constructs) / .90 (liberal, for conceptually similar constructs) are their own recommended cutoffs —
using the more conservative .85 threshold, as the manuscript does, is a defensible and accurately
attributed choice. No change needed.

### Zhou et al. (2025) — Study 2 "generation protocol," lines 628–632 — **ACCURATE**

Claim: "I convert the Study 1 incident corpus into a candidate item pool, one item per recurrent
first-order code, following Zhou et al.'s (2025) generation protocol; submit the pool to expert
content validation; and fit an exploratory factor analysis on the first pooled cohorts before
estimating any confirmatory model," and later, "matching the methodological baseline Zhou et al.
(2025) set" for a pooled sample of 200–250.

Checked against `zhou2025apjhr.md` (extended_preview, direct_read of the item set): the actual
sequence in Zhou, Lei, Liu, Huang & Hou (2025) is 99 semi-structured interviews (Sample 1) → 14
candidate items → expert content validation → EFA at N=275 (Sample 2) → CFA at N=213 (Sample 3) →
further validation at N=230 (Sample 4) → N=225 (Sample 5). The manuscript's stated order — incident
corpus → item pool → expert content validation → EFA → (later) CFA — matches this sequence exactly.
The 200–250 sample-size target is consistent with Zhou et al.'s later-stage samples (213, 230, 225),
though their EFA sample (275) exceeds that range; read narrowly as "the CFA-and-beyond baseline" the
claim holds, and the manuscript does not claim 200–250 covers every Zhou et al. sample.

One reference-hygiene point worth confirming, since the cards explicitly warn about this: there are
two different "Zhou et al. 2025" papers in this literature (the APJHR scale-development paper and a
same-year *Human Resource Management* paper by an overlapping author team on attribution effects).
PAPER.md's reference list (line 503) contains **only** the APJHR scale paper — the HRM paper is not in
the reference list at all — so every in-text "Zhou et al. (2025)" in this manuscript resolves
unambiguously to the scale-development paper. No conflation risk in the current draft.

### The anonymous JMIR preprint — lines 331, 343 — **ACCURATE in substance; McGrath name correctly absent; citation form correct**

Claim: "Recent models of AI-mediated medical education incorporate the patient alongside diagnostic
algorithms ('AI-Mediated Relational Competence in Medical Education,' 2026, an unrefereed preprint),
and ultimate clinical and legal authority resides with the human physician rather than an autonomous
intermediary."

No card exists for this source in `literature/cards/`. Fetched directly: Crossref's metadata for DOI
10.2196/preprints.105459 gives the abstract as arguing that "AI tools alter the structure of the
patient-clinician relationship itself," and names six sub-competencies including "accountable human
decision-making." Both halves of the manuscript's claim are supported — the preprint does frame the
issue as patient-clinician-AI (not clinician-AI alone), and it does name human accountability as a
distinct sub-competency, consistent with "ultimate clinical and legal authority resides with the human
physician." Substance: **ACCURATE**.

Citation form: the in-text citation uses the title in quotation marks with the year, `("AI-Mediated
Relational Competence in Medical Education," 2026, an unrefereed preprint)` — correct APA7 form for a
title-as-author entry (no named author), and the reference-list entry (line 343) leads with the title
in the author position, un-italicized, followed by the year, matching the convention for a
periodical-type/preprint entry. **Correct.**

McGrath check, explicit per the task: grepped PAPER.md for "mcgrath" (case-insensitive) — **zero
matches anywhere in the file**. The name does not appear near this citation or anywhere else in the
manuscript. This is the correct, currently-required state: `VERIFICATION_2026-08-29_full_sweep.md`
already flagged that Crossref's metadata now names an author (Robert Joseph McGrath, confirmed again
here via a fresh Crossref fetch) where the manuscript's own reference entry states "authors not
retrievable from the preprint server at the time of writing," and explicitly logged this as **not
applied — needs the author's own decision**. That decision is still open and this batch does not
change it; PAPER.md correctly still withholds the name pending that human confirmation. No action
taken, none recommended beyond what the standing flag already says.

### Rahman (2021) — "who-influences" dimension, Study 1, line 624 — **ACCURATE**

Claim: "Rahman's (2021) 'who-influences' dimension will be formalized as an autonomous fourth
operation if participant accounts systematically reveal actors who decode observable feedback
successfully yet cannot discern whether the platform intermediary or peer evaluators determined the
outcome."

Checked against `rahman2021.md` (full_text, direct_read, with page-verified quotes): Rahman's
"invisible cage" construct decomposes into five components — criteria, execution, magnitude, impact,
and **who influences** the evaluation (client or platform, left unspecified) — confirmed at OnlineFirst
p. 32 / VoR p. 976. "Who-influences" is Rahman's own dimension name and his own description (inability
to tell which party moved the score) matches the manuscript's adaptation (inability to tell whether
the platform intermediary or peer evaluators determined the outcome) — the manuscript substitutes
"peer evaluators" for Rahman's "client," which is the correct domain transposition for this study's
own peer-review gate rather than a misreading of Rahman's construct. ACCURATE.

### Boundary-case and minor citations — line 330–333, 550

**Yang & Liechty (2026)** — line 332 — **UNVERIFIABLE AT CURRENT DEPTH (partial mismatch with the confirmed abstract)**

Claim, under the "Public Child Welfare" boundary case: "Models of AI competence in social work address
client trust and algorithmic risk scoring (Yang & Liechty, 2026), and frame the algorithmic system as
an advisory decision-support tool rather than a binding administrative authority."

No card exists. Fetched the chapter's published abstract directly (Springer, *Artificial Intelligence
in Social Work*, ch. 23): it describes a chapter that "situates social work in a digital and
algorithmic era," defines AI literacy/competency, aligns them with the NASW Code of Ethics and CSWE
EPAS competencies (including a proposed tenth competency on "engaging AI and algorithmic systems"),
and proposes a three-tier professional development model. The confirmed abstract is about AI
literacy/competency *generally* across the social work profession — it does not mention child welfare,
client trust, or algorithmic risk scoring specifically. The manuscript cites this general chapter for
a narrowly-scoped "Public Child Welfare" example (risk scoring, client trust, advisory-vs-binding
framing) that the abstract does not confirm. This may be a subsection within the chapter body not
reflected in the abstract — book chapters often carry worked examples beyond what an abstract states —
but as it stands, only the general topic (AI competence in social work) is verifiable; the
child-welfare/risk-scoring specificity is not. **Flag for the author**: either confirm the risk-scoring
content against the chapter's full text, or generalize the sentence to match what the abstract
actually supports (AI literacy/competency in social work broadly, not a child-welfare-specific claim).

**Dredge & Anderson (2021)** — line 333 — **ACCURATE**

Claim: "Interpersonal frameworks in digital dating examine relationship-formation competencies while
omitting algorithmic curation (Dredge & Anderson, 2021)."

No card exists. Confirmed directly (Wiley abstract, *Personal Relationships* 28(3)): 22 interviews
with emerging adults in Australia and Belgium, thematic analysis, 11 superordinate social competencies
across 85 competent/67 incompetent behaviors, organized across four relationship-formation stages
(profile, matching, discovery, evaluation). Nothing in the confirmed abstract addresses algorithmic
curation or matching algorithms — the study is squarely about interpersonal/social competence during
dating-app use. The manuscript's characterization matches. ACCURATE.

**Hu & Zhan (2024)** — line 333 — **ACCURATE**

Claim: "computational accounts analyze algorithmic awareness while omitting relational counterpart
dynamics (Hu & Zhan, 2024)."

No card exists. Confirmed directly: a quantitative survey study (national sample, N=871, U.S. online
daters) testing whether algorithm awareness predicts mate-searching difficulty and future
expectancies/optimism — a "computational"/quantitative-survey account of algorithmic awareness, with
no apparent measure of the human counterpart (the other party being matched with). Matches the
manuscript's characterization. ACCURATE.

*Minor aside, outside this task's scope*: the search used to confirm this paper's content surfaced the
second author's name as "Zhang" (Emily Shuo Zhang, Michigan State University) rather than "Zhan" as
PAPER.md's reference list (line 415) has it. This is an existence/spelling question, already outside
the claim-accuracy remit and presumably covered by the 2026-08-29 bibliographic sweep — flagging only
because it surfaced incidentally; not independently verified against Crossref here.

**Nutbeam (2000)** — line 157 — **ACCURATE**

Claim (via Iyamu et al. 2026): "Evaluating empirical research against Nutbeam's (2000) tripartite
literacy hierarchy, Iyamu et al. (2026) observe that communicative literacy remains largely absent...
Within Nutbeam's model, communicative literacy... represents the literature's closest empirical
approximation of a second human actor."

No card exists for Nutbeam directly, but `iyamu2026.md` (extended_preview) independently confirms
Nutbeam's model as split into three levels — functional, critical, and communicative (interacting with
AI systems and explaining AI-mediated information to others) — and a general web check confirms
Nutbeam's own 2000 terminology is functional / interactive / critical health literacy, with
"interactive" and "communicative" used interchangeably in the literature that operationalizes his
model. The manuscript's "tripartite literacy hierarchy" and "communicative literacy" label are both
accurate to the source, and the Iyamu-mediated description (communicative = interacting with a system
and explaining its output to another person) is a legitimate, literature-standard extension of
Nutbeam's own third level. ACCURATE.

**Chigbu (2026)** — line 550 — **ACCURATE**

Claim: "empirical scholarship on algorithmic coordination in the region [Anglophone Caribbean]
remaining sparse (Chigbu, 2026)."

No card exists. Confirmed directly (Frontiers in Sociology, systematic review + critical discourse
analysis, 103 sources): the review's own stated finding is that "scholarship on algorithmic management
is conceptually rich but methodologically and geographically uneven... with... limited... 
representation from the Global South" and that attention has "centered disproportionately on Western
contexts." Chigbu's review is global/interdisciplinary rather than Caribbean-specific, so it does not
directly document a Caribbean gap by name — but its own geographic-unevenness finding (thin Global
South representation) is a reasonable, non-overstated basis for the manuscript's inference that
region-specific (Caribbean) empirical scholarship is sparse. ACCURATE as a supported inference; the
manuscript does not claim Chigbu studied the Caribbean specifically.

**ILO (2025)** — line 550 — **ACCURATE**

Claim: "Platform labor across the Anglophone Caribbean, by contrast, remains concentrated in
traditional logistics, ride-hailing, and hospitality (ILO, 2025)."

No card exists. Confirmed directly (ILO, *Decent work in the platform economy in the Caribbean*,
covering Antigua and Barbuda, The Bahamas, Belize, Dominica, Grenada, Jamaica, Saint Kitts and Nevis,
Saint Lucia, Saint Vincent and the Grenadines, Suriname, and Trinidad and Tobago): the report's own
finding is that the platform economy is "concentrated primarily in urban centers and the tourism
sector, and dominated by location-based services like transport and delivery." Transport → ride-hailing,
delivery → logistics, tourism → hospitality: a close, accurate match to the manuscript's three-term
list. Trinidad and Tobago, the paper's own field site, is explicitly among the countries covered.
ACCURATE.

### Summary

| Citation | Verdict |
|---|---|
| Pratt (2009) | ACCURATE |
| Timmermans & Tavory (2012), three moves | ACCURATE, internally consistent (only detailed instance in the paper) |
| Blumer (1954) / Bowen (2006) / Gioia et al. (2013) | ACCURATE |
| Flanagan (1954), four-part structure | **DRIFTED** — correction given above |
| Henseler et al. (2015) | ACCURATE (single instance in paper, no duplicate to reconcile) |
| Zhou et al. (2025), Study 2 generation protocol | ACCURATE |
| Anonymous JMIR preprint | ACCURATE in substance; citation form correct; McGrath name correctly absent (open item, not resolved here) |
| Rahman (2021), "who-influences" | ACCURATE |
| Yang & Liechty (2026) | UNVERIFIABLE AT CURRENT DEPTH — child-welfare/risk-scoring specificity not confirmed by the chapter abstract |
| Dredge & Anderson (2021) | ACCURATE |
| Hu & Zhan (2024) | ACCURATE (minor aside: possible author-surname spelling question, outside this task's scope) |
| Nutbeam (2000) | ACCURATE |
| Chigbu (2026) | ACCURATE |
| ILO (2025) | ACCURATE |

One actionable fix (Flanagan) and one item needing the author's own follow-up (Yang & Liechty's
child-welfare specificity). Every other checked citation in this batch holds up against its source.

## Batch 5: Empirical Strategy + Appendix A + Appendix B (lines 282–614)

**Note on scope.** The task brief for this batch specified lines 282–524 ("through Appendix A"), but the
detailed items it asked me to check by name — Riordan, Flanagan, the three named abductive moves, Yurek,
Merton's "strategic research site," Bamberger & Pratt, Bothello et al. — all sit in **Appendix B**
(lines 526–614), not Appendix A. That is also this file's own stated scope for Batch 5 (line 27 above:
"Empirical Strategy + Appendix A + Appendix B, lines 282–614"). I followed the file's own definition and
read through line 614, i.e., through the end of Appendix B. Appendix C (616–650) is out of scope here
(Batch 6).

### Empirical Strategy section (282–321)

**Coghlan & Brannick (2014)** — "Following Coghlan and Brannick (2014), I separate the core action
research project from the formal research project conducted upon it" (284); "insider action research...
each cycle's evaluation informing the next construction (Coghlan & Brannick, 2014)" (536); "Following
Coghlan and Brannick (2014), the core action research cycle... remains distinct from the thesis research
cycle" (560).
**Verdict: ACCURATE.** The card (`coghlanbrannick2014.md`, full-text read of Ch. 1) confirms this
precisely: the book distinguishes the **core cycle** (the project/organizational change itself) from the
**thesis cycle** (the dissertation's reflective inquiry into that project) as two AR cycles run in
parallel, "integrally interlinked" but "not identical." This is the paper's central methodological
scaffolding and it is attributed correctly — not a loose gesture at the book but the specific
core/thesis-cycle apparatus the source builds. The four-phase spiral (constructing → planning action →
taking action → evaluating action) invoked at 536 also matches the card's Ch. 1 summary exactly.

**Brannick & Coghlan (2007)** — "The study presented in Paper 3 is insider research on that program's
mature configuration (Brannick & Coghlan, 2007)" (284).
**Verdict: ACCURATE (background use here).** The card (abstract-depth) confirms the article defends
insider/native research across positivism, hermeneutics, and action research and names four dynamics
(access, preunderstanding, role duality, organizational politics). The 284 usage is a general "insider
research" attribution, consistent with the source; the more load-bearing use of this source is at 568
alongside Riordan and Anteby (see below), which also checks out.

**Eisenhardt & Graebner (2007) and Merton (1987)** — "I treat this setting as a strategic research site
(Eisenhardt & Graebner, 2007; Merton, 1987)" (286); expanded at 548: "The early Caribbean cohorts
functioned as a strategic research site in Merton's (1987) sense, providing a setting where the focal
phenomenon manifested with unusual analytical tractability. As Eisenhardt and Graebner (2007) argue,
single-case selections are justified when a setting offers revelatory access to an unexamined process."
**Verdict: ACCURATE for both.**
- *Merton*: the reference-list title itself reads "...strategic research materials," which could look
  like a drift from the in-text "strategic research site." It is not. I verified by web search (Merton,
  1987, *Annual Review of Sociology* 13) that Merton's third fragment, on strategic research materials,
  explicitly coins and defines "a strategic research site" as one that "exhibits the phenomena to be
  explained or interpreted to such an advantage and in such accessible form that it enables the fruitful
  investigation of previously stubborn problems." The manuscript's gloss — "a setting where the focal
  phenomenon manifested with unusual analytical tractability" — is a faithful paraphrase of that
  definition. No card exists for Merton (1987) in `literature/cards/`; this verdict rests on the web
  search, not a card, and should get a card built from primary text if the claim is load-bearing (it is).
- *Eisenhardt & Graebner*: the card (full-text read) confirms single-case selection is justified when a
  case is "unusually revelatory, extreme... or an opportunity for unusual research access" (quoting
  Yin), and the card's own "Relation to the argument" section explicitly endorses pairing this citation
  with "Merton's strategic-research-site language" for exactly this site-justification move, and cautions
  against using Eisenhardt & Graebner for anything broader (it is an "objective"/positivist,
  replication-logic strategy distinct from the paper's actual abductive, single-evolving-field-site
  design). The manuscript's usage here is narrow and matches the card's own recommendation — no drift.

**Timmermans & Tavory (2012)** — "Data collection and analysis follow an abductive protocol (Timmermans
& Tavory, 2012) built to reconcile observed participant behavior with theoretical categories" (286); the
qualitative rigor citation recurs at 532 and 622.
**Verdict: ACCURATE (background in this sub-range).** The general "abductive protocol" characterization
matches the card. The precise, name-level check of the three moves belongs to Appendix B (581–585); see
below — that is where the specific, checkable claim actually appears.

### Conclusion (323–337) — no load-bearing citations in this range needing card checks; Spitzberg & Cupach
(1984) and Sandberg (2000) appear but are outside this batch's requested checklist and read as background
molar/molecular-competence citations consistent with their titles.

### Appendix A: Comparative Framework (505–524)

**Powell (1990), Williamson (1991), Bradach & Eccles (1989), Ouchi (1980)** — "Extending the comparative
traditions established by [these four]..." (507).
**Verdict: BACKGROUND.** Named together for genre lineage (classic hierarchy/market/network/clan
comparative frameworks), no individually distinguishing claim attached to each. No cards exist for any of
the four; none needed at this citation depth.

**Okhuysen & Bechky (2009)** — "The integrative deliverables map to the three conditions synthesized by
Okhuysen and Bechky (2009): predictability, common understanding, and accountability" (507), reused
across every row of Table A1's "What it must deliver."
**Verdict: ACCURATE.** The card (full-text read, direct quotes from pp. 483–490) confirms the three
integrating conditions by name and definition: accountability ("who is responsible for specific elements
of the task"), predictability ("anticipate subsequent task related activity"), common understanding (a
shared conception of the whole). Appendix A's use is exactly the card's flagged *safe* use — laying the
three conditions across the coordination-form columns is explicitly the dissertation's own extension, not
attributed to Okhuysen & Bechky, and the paper does not (in this range) commit the specific misattribution
the card warns about elsewhere (defining accountability as a "forum relation," which is Bovens's term, not
theirs) — that risk lives in §5/§6, outside this batch.

**Hayek (1945)** — "the price mechanism bears the primary coordinative burden because it functions as an
aggregated public statistic no participant needs to reconstruct privately" (509); reused in Table A1 and
at 522.
**Verdict: ACCURATE.** No card exists; verified by web search against the source. Hayek's actual argument
in "The Use of Knowledge in Society" (1945) is that "we must look at the price system as a mechanism for
communicating information... the most significant fact about this system is the economy of knowledge with
which it operates, or how little the individual participants need to know in order to take the right
action." The manuscript's "aggregated public statistic no participant needs to reconstruct privately" is a
faithful compression of that argument.

**Simon (1997) and Weber (1978)** — "Authority; participant operates within an institutional zone of
acceptance (Simon, 1997; Weber, 1978)" (513); reprised at 522: "Simon (1997) and Weber (1978) together
locate the individual in hierarchy through an administrative zone of acceptance."
**Verdict: ACCURATE, with one precision note.** No cards exist for either; verified by web search.
"Zone of acceptance" is specifically Simon's term (*Administrative Behavior*), his renaming of Barnard's
"zone of indifference" — the range within which a subordinate obeys orders without independently
examining their merits. Weber (1978, *Economy and Society*) supplies the account of legitimate
(rational-legal/bureaucratic) authority itself, not the "zone of acceptance" terminology. The manuscript
does not claim Weber coined the phrase — it cites both together for the composite hierarchy
characterization (authority + the psychological mechanism that sustains it), which is a defensible joint
citation, not a misattribution of the term to Weber specifically. Worth a light edit only if a reviewer
presses on it: something like "an administrative zone of acceptance (Simon, 1997), backed by legitimate
bureaucratic authority (Weber, 1978)" would remove any ambiguity, but the current text does not actually
assert Weber originated the term.

**Granovetter (1985) and Powell (1990)** — "Ongoing relational ties; actor invests in an elective,
revocable partnership (Granovetter, 1985; Powell, 1990)" (513, 522).
**Verdict: ACCURATE (background-level, standard characterization).** No cards exist. This is the
textbook-standard gloss of Granovetter's embeddedness argument and Powell's "network forms" article; the
characterization is consistent with well-established scholarly consensus on both sources, though neither
has been read at full-text depth in this project's card store.

**Selznick (1949)** — "Institutional absorption; an external opponent is brought inside to assume a
formal seat, converting opposition into participation (Selznick, 1949)" (513, 522).
**Verdict: ACCURATE (background-level).** No card exists. This is the standard characterization of
Selznick's *TVA and the Grass Roots* (1949), the foundational co-optation study in organizational theory;
the gloss matches the concept's well-established meaning in the field.

**Stark & Pais (2020) and Stark & Vanden Broeck (2024)** — "Enrollment; an opaque algorithm matches
unchosen parties, evaluates actions, and exercises unilateral account termination (Stark & Pais, 2020;
Stark & Vanden Broeck, 2024)" (513); reprised at 524: "digital platforms do not coordinate through
command, price discovery, or relational reciprocity; they enroll participants through matching algorithms
that pair unchosen parties, monitor performance metrics, and enforce unilateral sanctions."
**Verdict: UNVERIFIABLE AT CURRENT DEPTH.** No cards exist for either source in `literature/cards/`. A web
search confirmed Stark & Vanden Broeck (2024), *Organization Theory*, "Principles of Algorithmic
Management," exists and concerns reconfigured boundaries and relations among managers, workers, and other
actors under algorithmic coordination, which is directionally consistent, but I could not confirm the
specific "matches unchosen parties... unilateral account termination" language against the source text
itself. These citations define the paper's own core construct (coordinative co-optation) and are almost
certainly checked in Batch 1, where the construct is first introduced (lines 1–46) — flagging here so the
two batches can be reconciled rather than duplicating the check.

**Möhlmann et al. (2021)** — "Dynamic matching coupled to algorithmic control (Möhlmann et al., 2021)"
(514, table); "algorithmic matching and surveillance (Möhlmann et al., 2021)" (524).
**Verdict: ACCURATE.** Card confirms (full-text): the article's central distinction is matching
(market-side coordination) versus control (organizational-side monitoring/discipline), on Uber. "Dynamic
matching coupled to algorithmic control" is a precise compression of the paper's own title and thesis
("When Matching Meets Control").

**Kellogg, Valentine & Christin (2020)** — "administrative direction and evaluative discipline (Kellogg
et al., 2020)" (514, 524).
**Verdict: ACCURATE.** Card confirms (full-text): the "6 Rs" typology sorts algorithmic control into
directing (restricting/recommending), evaluating (recording/rating), and disciplining
(replacing/rewarding). "Administrative direction and evaluative discipline" tracks two of these three
functions closely (the third, "disciplining," is folded into "evaluative discipline" here, which is a
slight compression but not a distortion — the paper is not claiming to reproduce all six Rs, only citing
the source's general control-typology finding).

**Rosenblat & Stark (2016)** — "Asymmetric information dashboards (Rosenblat & Stark, 2016)" (516);
"information asymmetries (Rosenblat & Stark, 2016)" (524).
**Verdict: ACCURATE.** Card confirms (full-text): the article's central argument is that Uber's power
over drivers runs on documented information asymmetries (surge maps drivers cannot verify, blind
acceptance of ride requests, unilateral rate changes). "Asymmetric information dashboards" is a fair,
concrete instantiation of the article's own examples (the driver-facing app interface itself functions as
the asymmetric dashboard).

**Curchod, Patriotta, Cohen & Neysen (2020)** — "non-portable algorithmic reputational ratings (Curchod
et al., 2020)" (516); "non-portable reputational capital (Curchod et al., 2020)" (524).
**Verdict: ACCURATE.** Card confirms (full-text, wording-checked against the accepted manuscript): the
study documents "blocked exit, because reputation cannot be rebuilt elsewhere" among eBay sellers —
exactly the non-portability claim the manuscript attributes to it.

### Appendix B: Action Research Design (526–614)

**Pratt (2009)** — "Following Pratt (2009), qualitative rigor depends on alignment between method and the
underlying theoretical puzzle rather than adherence to generic templates" (532). No card exists for
Pratt (2009) specifically (distinct from Pratt et al., 2020, which does have a card); this is a
well-known, title-consistent characterization of Pratt's ASQ "boilerplate" editorial but is
**UNVERIFIABLE AT CURRENT DEPTH** — flagging for a card if this citation is treated as load-bearing.

**Coghlan & Brannick (2014)**, reprised at 536 and 560 — see above; both uses (the four-phase spiral, the
core/thesis-cycle split) remain **ACCURATE** against the card.

**Merton (1987) and Eisenhardt & Graebner (2007)**, reprised at 548 — see above; **ACCURATE**, verified by
web search for Merton and by card for Eisenhardt & Graebner.

**Bamberger & Pratt (2010) and Bothello, Nason & Schnyder (2019)** — "Studying non-traditional research
contexts prevents the misapplication of mature institutional assumptions and allows emergent behavioral
phenomena to surface in unobstructed form (Bamberger & Pratt, 2010; Bothello et al., 2019)" (550).
**Verdict: ACCURATE, both.** No cards exist for either; verified by web search.
- Bamberger & Pratt (2010), *AMJ* "From the Editors," argues for reclaiming unconventional/extreme
  research contexts because they can reveal insights inaccessible or poorly understood elsewhere, and
  that scholars must "ensure that [their] context and sample serve [their] theory, rather than vice
  versa." This supports the manuscript's claim about non-traditional contexts surfacing phenomena in
  less-confounded form.
- Bothello et al. (2019), *Organization Studies*, critiques the stretched use of "institutional void" to
  characterize non-Western contexts and calls for an "epistemological rupture" against imposing
  Western/"mature" institutional assumptions on other settings, in favor of contextually grounded,
  indigenous theorization. This is a good fit for the manuscript's specific phrase "prevents the
  misapplication of mature institutional assumptions." One caveat: Bothello et al.'s argument is more
  pointedly about ethnocentrism and construct clarity in institutional-voids research than a general
  methods point about "unobstructed" phenomena; the manuscript's paraphrase compresses a fairly political,
  targeted critique into a generic methods claim. Directionally faithful, not misrepresented, but a
  reader who goes to the source will find a sharper argument than the citation implies.

**Chigbu (2026)** — "empirical scholarship on algorithmic coordination in the region remaining sparse
(Chigbu, 2026)" (550).
**Verdict: UNVERIFIABLE AT CURRENT DEPTH.** No card exists. Chigbu (2026) is titled "Algorithmic
management in the global gig economy: An interdisciplinary systematic literature review and critical
discourse analysis" (*Frontiers in Sociology*) — a global systematic review, not a Caribbean-specific
study. It is plausible that a systematic review documents geographic gaps in the literature it surveys
(SLRs commonly do), which would support the manuscript's specific claim about regional sparsity, but this
was not confirmed against the source text. Flagging for a card/direct check before treating this as
settled — this is the one citation in the batch where the paper's specific claim (a *regional* gap) is
narrower than what the title alone guarantees (a *global* review).

**Riordan (1995), as cited in Coghlan & Brannick (2014); Anteby (2013)** — "I manage the dual role through
structural safeguards rather than methodological disavowal (Riordan, 1995, as cited in Coghlan &
Brannick, 2014; Anteby, 2013)" (568).
**Verdict: ACCURATE — correct, honest secondary citation.** The `coghlanbrannick2014.md` card (full-text
read of Ch. 1) confirms Riordan (1995) is directly quoted there: "require[s] a practitioner of science who
is not only an engaged participant, but also incorporates the perspective of the critical and analytical
observer, not as a validating instance but as integral to the practice." No card or record anywhere in
`literature/` shows Riordan (1995) was read directly, and the manuscript does not present it as if it
were — it is correctly flagged "as cited in Coghlan & Brannick, 2014," consistent with this project's
established citation-depth tracking (Riordan is secondary-only). The trailing "; Anteby, 2013" reads most
naturally as an additional, independently-supporting citation for the same sentence (Anteby's own
distance/involvement argument, confirmed accurate against its card above), not as a claim that Riordan is
also quoted inside Anteby — no card evidence suggests Anteby (2013) discusses Riordan, and the sentence
does not assert that it does. No drift.

**Ferguson, Yonge & Myrick (2004) and Mercer (2007)** — "To remove power asymmetries and instructional
demand characteristics (Ferguson et al., 2004; Mercer, 2007), the intake client anonymizes participants
before any record reaches me" (568).
**Verdict: ACCURATE.** Both cards (full-text-verified) confirm the fit: Ferguson et al. (2004) is the
specific source for faculty-researching-own-students consent/coercion protections (agent-mediated
consent, non-participation kept confidential from the faculty researcher) — the manuscript's anonymized
intake is, if anything, a stronger version of the same protection, per the card's own 2026-08-26
verification note. Mercer (2007) is the specific source for the residual concern that participants may
still manage a researcher's/teacher's expectations even under structural safeguards — consistent with how
the manuscript uses her (naming a known, published dilemma rather than a design flaw).

**Pratt, Kaplan & Whittington (2020) and Tracy (2010)** — "I log every protocol version, coding memo, and
dated analytic decision in an audit trail (Pratt et al., 2020; Tracy, 2010)" (568).
**Verdict: ACCURATE (Pratt et al.); background-consistent but unconfirmed on the specific term (Tracy).**
Pratt et al. (2020)'s card confirms trustworthiness in qualitative work should rest on "visible analytic
process, the audit trail, negative cases" rather than raw-data disclosure — a precise match to the
manuscript's audit-trail practice. Tracy (2010)'s card (abstract-depth) confirms her eight "big-tent"
criteria (including "rich rigor" and "credibility") but does not itself confirm, at this card's depth,
that "audit trail" is one of Tracy's own named practices (it is standard in the Lincoln & Guba tradition
Tracy draws on, but the card cannot confirm the specific term without full-text access). Not a drift, but
flagged as resting on general fit rather than a confirmed textual match.

**Flanagan (1954)** — "Each module applies the critical incident technique (Flanagan, 1954), prompting
participants to detail a complete behavioral episode: the baseline objective, the system determination,
the tactical adaptation, and the resolution" (579).
**Verdict: ACCURATE for the core attribution; UNVERIFIABLE AT CURRENT DEPTH for the specific four-part
structure.** No card exists for Flanagan (1954). The attribution of "the critical incident technique" to
Flanagan (1954) is definitionally safe — Flanagan's *Psychological Bulletin* article is the technique's
originating source and the paper's own reference-list title matches exactly ("The critical incident
technique"). The specific four-part decomposition (baseline objective / system determination / tactical
adaptation / resolution) reads as the manuscript's own operationalization of the technique for this
protocol rather than a claim about Flanagan's original published structure, and should not be read as
asserting Flanagan specified those four exact stages — the sentence's grammar supports that reading (the
technique is Flanagan's; the four-part episode structure is presented as what the study elicits, not
quoted from the source).

**Timmermans & Tavory (2012), named three moves** — "Analysis follows an abductive logic of inquiry
(Timmermans & Tavory, 2012) through three iterative moves: **Revisiting**... **Defamiliarization**...
**Alternative Casing**..." (581–585).
**Verdict: ACCURATE — names and substance both check out precisely against the card (full-text read).**
- *Revisiting* (paper): "Returning repeatedly to inscribed transcripts across multiple passes to examine
  how emergent categories reframe earlier observations." Card: "returning to the same observation
  repeatedly as it is inscribed (field notes, transcripts, coding, memos)... whose relevance changes with
  each return." Matches.
- *Defamiliarization* (paper): "Treating automated transcription as a technique of analytical
  estrangement, subjecting self-evident participant explanations to theoretical scrutiny." Card:
  "inscription itself (the act of writing observation into text) as a technique of estrangement... so
  that what was taken for granted becomes a possible focal point." Matches — the paper narrows T&T's
  general "inscription" to this protocol's specific instrument (automated transcription), which is a
  legitimate operationalization of the same concept, not a redefinition of it.
- *Alternative Casing* (paper): "Evaluating raw transcripts against competing frameworks (individual
  skill acquisition, relational gig literacies, dyadic sensemaking) to establish whether the data demand
  the triadic construct." Card: "deliberately working a data excerpt against multiple theoretical
  frameworks in turn... to render the phenomenon a case of more than one thing before settling." Matches,
  and the card itself flags this exact move ("alternative casing is the move behind treating a
  participant who reports full transparency as evidence against the construct") as already operative in
  the manuscript's design.
All three names are correct, in the source's own order and terminology, and each definition is a faithful
compression rather than a distortion.

**Blumer (1954) and Bowen (2006)** — "The three operations function as sensitizing concepts (Blumer,
1954; Bowen, 2006)" (587).
**Verdict: ACCURATE, and correctly ordered/weighted.** Blumer's card confirms he is the originating source
for the definitive-vs-sensitizing-concept distinction; Bowen's card (full-text) confirms Bowen is the
applied precedent, reporting a real discard — two of three literature-derived sensitizing concepts
dropped from his emergent theory, one retained. The manuscript cites Blumer first (for the concept) and
Bowen second (for the applied practice), which matches both cards' own recommended citation order and
division of labor. Note: the manuscript's Appendix B text does **not** itself invoke Bowen's
discard-two-of-three precedent explicitly in this sentence — it is cited generally for "sensitizing
concepts" — so the task brief's expectation that the discard precedent appears explicitly here is not
borne out by the text; the disconfirming-negative-case sentence immediately following (587) is consistent
with that precedent in spirit but does not name it. Not a drift, just noting the precedent is implicit
rather than stated.

**Gioia, Corley & Hamilton (2013)** — "Initial coding adheres to first-order, participant-centric
terminology (Gioia et al., 2013) before second-order categories are applied" (587).
**Verdict: ACCURATE.** Card confirms (full-text): the Gioia methodology's first step is coding in
informant terms ("staying close" to how informants describe their own experience), followed by
second-order, researcher/theoretical themes. The manuscript's use is exactly the narrow "discipline, not
full apparatus" citation the card itself recommends (first-order coding transfers even though the full
Gioia data-structure-diagram template does not apply to a design that starts from three operations
derived in advance).

**Yurek, Vasey & Havens (2008)** — "participants generate a self-derived confidential token at baseline,
derived from invariant personal elements, and re-enter it across successive waves (Yurek et al., 2008)"
(591).
**Verdict: ACCURATE.** No card exists in `literature/cards/`, and no record of Yurek anywhere in
`literature/` (checked `GAPS.md`, `COVERAGE.md`, `VERIFICATION_2026-08-29_full_sweep.md`, and the pdfs
directory — none reference it), despite the task brief's note that this reference was "previously
re-added... after being found missing." I could not locate documentation of that history in this
project's files; the reference-list entry (line 501, correct DOI-bearing bibliographic form) and the
in-text citation are both present and consistent with each other, at least. I verified the claim by web
search: Yurek, Vasey & Havens (2008), *Evaluation Review* 32(5), 435–452, describes self-generated/
subject-generated identification codes (built from invariant personal elements, e.g., initials, birth
digits) that "permit an anonymous means to track respondents over multiple data collection points" in a
longitudinal nursing study. This matches the manuscript's claim precisely — self-derived token from
invariant personal elements, re-entered across waves, for anonymous longitudinal tracking. **Recommend
building a card for this source given how load-bearing the panel's confidentiality architecture is to the
paper's IRB and researcher-blindness claims.**

### Summary table

| Citation | Verdict |
|---|---|
| Coghlan & Brannick (2014) | ACCURATE |
| Brannick & Coghlan (2007) | ACCURATE (background) |
| Eisenhardt & Graebner (2007) | ACCURATE |
| Merton (1987) | ACCURATE (verified by web search; no card exists — recommend building one) |
| Timmermans & Tavory (2012), general | ACCURATE |
| Timmermans & Tavory (2012), three named moves | ACCURATE — precise match |
| Powell/Williamson/Bradach & Eccles/Ouchi | BACKGROUND, no check needed |
| Okhuysen & Bechky (2009) | ACCURATE |
| Hayek (1945) | ACCURATE (web-verified; no card) |
| Simon (1997) / Weber (1978) | ACCURATE, minor precision note (web-verified; no cards) |
| Granovetter (1985) / Powell (1990) | ACCURATE (background-level; no cards) |
| Selznick (1949) | ACCURATE (background-level; no card) |
| Stark & Pais (2020) / Stark & Vanden Broeck (2024) | UNVERIFIABLE AT CURRENT DEPTH — no cards; check against Batch 1 |
| Möhlmann et al. (2021) | ACCURATE |
| Kellogg, Valentine & Christin (2020) | ACCURATE |
| Rosenblat & Stark (2016) | ACCURATE |
| Curchod et al. (2020) | ACCURATE |
| Pratt (2009) | UNVERIFIABLE AT CURRENT DEPTH — no card |
| Bamberger & Pratt (2010) | ACCURATE (web-verified; no card) |
| Bothello et al. (2019) | ACCURATE, with caveat that the source's argument is sharper/more political than the paraphrase (web-verified; no card) |
| Chigbu (2026) | UNVERIFIABLE AT CURRENT DEPTH — global SLR title, regional-gap claim unconfirmed |
| Riordan (1995), as cited in Coghlan & Brannick (2014); Anteby (2013) | ACCURATE — honest secondary citation |
| Ferguson et al. (2004) / Mercer (2007) | ACCURATE |
| Pratt et al. (2020) / Tracy (2010) | ACCURATE (Pratt et al.); background-consistent, unconfirmed specific term (Tracy) |
| Flanagan (1954) | ACCURATE for core attribution; four-part structure is the paper's own, not Flanagan's |
| Blumer (1954) / Bowen (2006) | ACCURATE, correctly ordered; Bowen's discard-precedent implicit not stated |
| Gioia et al. (2013) | ACCURATE |
| Yurek et al. (2008) | ACCURATE (web-verified; no card — recommend building one) |

**No DRIFTED findings in this batch.** The strongest candidate for drift going in — Merton's "strategic
research site" language against a reference title reading "strategic research materials" — resolved as
accurate once checked against Merton's actual text: he coins "strategic research site" himself inside the
discussion of strategic research materials.

**Cards recommended for the record, given load-bearing use and no existing card:** Merton (1987),
Yurek, Vasey & Havens (2008), Hayek (1945), Bamberger & Pratt (2010), Bothello et al. (2019), Stark &
Vanden Broeck (2024) / Stark & Pais (2020) if not already covered in Batch 1.


---

## Batch 3: Extant Constructs hearings 5-7 + What These Boundaries Share

Scope: PAPER.md lines 113-169 (Algorithmic Competency / Zhou et al., Reactivity under Opaque
Evaluation / Rahman, Gig Literacies / Sutherland et al., and What These Boundaries Share). Method:
read each card's "What it argues" and dated verification notes, then independently re-verified
every page-numbered quotation against the source PDF directly with `pdftotext -f N -l N` (per-page
extraction matched to the page's own printed running header, not formfeed counting) rather than
trusting the cards' page-correction notes at face value — this surfaced two places where a card's
own "correction" was itself wrong. Sources checked directly: `zhou2025apjhr_workingpaper.pdf`,
`dissertation/research/sources/pdfs/zhou2025_algorithmic_competency.pdf` (journal VoR),
`sutherland2020.pdf`, `rahman2021_onlinefirst_typeset.pdf`, `dissertation/research/library/pdfs/cameron2024.txt`.

### Algorithmic Competency (Zhou et al. 2025), lines 115-125

| Claim | Verdict | Notes |
|---|---|---|
| 99 semi-structured interviews → 14 items | ACCURATE | Matches `zhou2025apjhr.md` and `ZHOU_2025_INSTRUMENT.md` exactly (Sample 1). |
| EFA N=275, CFA N=213, construct validation N=230, three-wave panel N=225 | ACCURATE | Matches card's sample sequence exactly (Samples 2-5). |
| Second-order, four-factor model | ACCURATE | Matches card. |
| 12-item instrument, aggregate reliability .85 across four subdimensions | ACCURATE | Matches card (overall α = .85; 12 items survive, three per dimension). |
| Quote, p. 2: "understanding of platform algorithms that assign and evaluate their work and their ability to adapt to and navigate those algorithms" | ACCURATE — independently verified | Card's "Verified 2026-08-29" note only checked Item 8/Item 11 at p. 8, leaving this quote's page unverified by the card. I located it directly in the journal VoR PDF (`zhou2025_algorithmic_competency.pdf`): verbatim match, and the PDF page footer reads "2 of 15." Page 2 is correct. |
| Understanding/Embracing/Leveraging/Remediating dimension definitions | ACCURATE | Matches `ZHOU_2025_INSTRUMENT.md`'s table verbatim in substance. |
| r=.37 (digital competence) and r=.04, ns (Embracing) | ACCURATE | Matches card exactly, including the ns designation. |
| Item 8 quote, p. 8: "I proactively explore AM rules to minimize negative customer feedback" | ACCURATE | Card's "Verified 2026-08-29 (A2/A3 sweep)" confirms this verbatim against the VoR Table 2, page footer "8 of 15." |
| Item 11 quote, p. 8: "I think the platform AM is highly efficient, such as in customers–workers matching" | ACCURATE | Same verification note, confirmed verbatim including the en dash. |
| Item 6 quote, p. 8: "use platform APP functions (i.e., reporting exceptions and appealing) to resolve vulnerabilities in AM" | ACCURATE | Not explicitly checked in the card's own verification notes (which named only Items 8 and 11), but I located it directly in the working-paper Table 1/Table 2 material: item 6 reads "I can use platform APP functions (i.e., reporting exceptions and appealing) to resolve vulnerabilities in AM," verbatim match. It sits in the same Table 2 block as Items 8 and 11, consistent with the shared p. 8 citation. |
| "The qualitative fieldwork underpinning the item illustrates an asymmetrical dispute process: ... a courier compiles objective documentation (audio recordings, timestamped delivery logs) and submits an administrative appeal" | **DRIFTED / embellished — not supported by the source** | The working paper's actual qualitative exemplar for this item (Table 1, Remediating AM row) is a single sentence from interviewee N22: "When receiving unfair ratings from customers, I can use evidence like recordings to appeal to the AM." There is no mention of "audio recordings" specifically (just "recordings," unspecified medium) and no mention of "timestamped delivery logs" at all — that detail does not appear anywhere in the working paper or the journal VoR. The manuscript's parenthetical invents specificity beyond what N22 said. Recommend cutting "(audio recordings, timestamped delivery logs)" or replacing it with the actual quote/citation to N22. |
| "the primary organizational antecedents predicting algorithmic competency are social mechanisms — informal peer support systems moderated by collectivist cultural orientations" | ACCURATE | Verified directly against the working-paper text (§ Antecedents of algorithmic competency): "peer support from peers significantly and positively interacted with collectivism to predict AC (b = .09, p < .05)." The manuscript's phrasing is accurate, though it foregrounds only one of the paper's two antecedents (peer support + collectivism moderation) and omits the second, cognitive job crafting, which the working paper treats as co-equal. Not an error, but a selective emphasis worth knowing about — the source's "socialization proposition" support is real but partial. |
| Customer-oriented service behavior via Peccei and Rosenthal's (1997) scale | ACCURATE | Matches card exactly ("customer-oriented service behaviour, measured with Peccei and Rosenthal's six-item scale"). |

### Reactivity under Opaque Evaluation (Rahman 2021), lines 129-137

All page numbers below were independently re-derived from the OnlineFirst typeset PDF using
`pdftotext -f N -l N` and the constant +944 offset the card documents (OnlineFirst page X → VoR
page X+944), then cross-checked against the exact wording. Every one is correct as currently
written in PAPER.md — this is the one hearing in the batch with a clean bill of health.

| Claim | Verdict | Notes |
|---|---|---|
| Five properties (criteria, execution, magnitude, impact, who-influences), p. 976 | ACCURATE | OnlineFirst p. 32 → VoR 976, confirmed. |
| Quote, p. 976: "even if a freelancer makes headway in uncovering one or a few components of the evaluation algorithm, other facets will remain opaque" | ACCURATE — independently verified verbatim | Located and confirmed word-for-word on OnlineFirst p. 32 (VoR 976), immediately following the five-properties passage. |
| 18 clients, 80 freelancers, p. 956 | ACCURATE | Table 1 with "80 freelancer interviews" / "18 client interviews" located on OnlineFirst p. 12 → VoR 956, confirmed. |
| "Registered freelancers could access a client's full profile only after submitting a job application... withheld direct contact information," p. 954 | ACCURATE | Paraphrase of OnlineFirst p. 10 ("Registered freelancers could see a client's full profile only after applying for their job, and even then, TalentFinder withheld their contact information") → VoR 954, confirmed. |
| "The scope of those client interviews remained bounded, serving primarily to examine client evaluation practices and triangulate freelancer accounts," p. 954 | ACCURATE | Same OnlineFirst p. 10 passage ("I used client interviews to understand their perspectives on providing freelancers feedback... and to triangulate what freelancers said") → VoR 954, confirmed. This is the same page as the "full profile" claim above — both anchor to the same paragraph. |
| "assuring clients that their evaluative feedback would remain anonymous and never appear directly to the freelancer," p. 960 | ACCURATE | Paraphrase of OnlineFirst p. 16 ("This feedback will be kept anonymous and never shared directly with the freelancer") → VoR 960, confirmed. |

This confirms the task brief's expectation exactly: the current text uses 954/954/960, not the old
wrong 956/956/963. No further correction needed anywhere in the Rahman hearing.

### Gig Literacies (Sutherland et al. 2020), lines 141-149

Independently re-verified every page-numbered quotation directly against `sutherland2020.pdf` using
`pdftotext -f N -l N` matched to each page's own printed running header (the method the card's own
"A2/A3 sweep" note recommends, because formfeed counting drifts by one page after the Table 1
break). **This turned up two places where the card's own 2026-08-29 "correction" was itself wrong**,
and — critically — comparing the corrected-per-card values against the current PAPER.md text shows
one place where PAPER.md still (correctly) disagrees with the card, and one place where PAPER.md
now carries the card's bad fix.

| Claim | Verdict | Notes |
|---|---|---|
| Quote, p. 457: "critical literacies… emerging around online freelancing" | ACCURATE | Verbatim (with correctly-placed ellipsis) against the abstract on p. 457. |
| Quote, p. 457: "adapt their skills and work strategies in order to leverage platforms creatively and productively, and as a component of their 'personal holding environment'" | ACCURATE — independently verified verbatim | Located word-for-word in the abstract, p. 457: "We find that gig workers must adapt their skills and work strategies in order to leverage platforms creatively and productively, and as a component of their 'personal holding environment'." (Note: `sutherland2020.md`'s own "What it argues" section paraphrases this with "use" instead of "leverage," which could mislead a checker relying on the card alone — the manuscript's "leverage" is the actual verbatim word and is correct.) |
| Quote, p. 470: "the know-how required to leverage platform resources in order to minimize the precarity of independent work, while retaining as much autonomy as possible from those platform structures themselves" | ACCURATE | Verbatim on p. 470, confirmed directly. |
| 20 freelancers / 19 clients, dual-sided walkthrough, pp. 461-463 | ACCURATE | Interview counts on p. 461, Table 1 on p. 462, walkthrough method spanning into p. 463 — confirmed directly and consistent with the card. |
| Quote, p. 463: "some verification as to which literacies or skills were in fact valued in gig workers" | **ACCURATE AS CURRENTLY WRITTEN — card's "correction" to p. 462 is wrong.** | Direct `pdftotext -f 7 -l 7` extraction shows this sentence on the PDF page whose printed running header reads "Sutherland et al. 463" — i.e., printed page 463, not 462. The card's 2026-08-29 note ("is p. 462, not the p. 463 the draft had... fixed in PAPER.md 2026-08-29") is itself incorrect; it appears to have been produced by the earlier, drift-prone formfeed-counting method the card's own later "A2/A3 sweep" flags as unreliable, and that later sweep never went back to re-check this specific quote with the reliable per-page method. PAPER.md's current text (p. 463) is correct and should **not** be "fixed" to 462 — doing so would introduce an error. Recommend correcting the card, not the manuscript. |
| Quote, p. 467/468, P10: "to build a rapport and a little longer lasting relationship" | **DRIFTED — current text (p. 467) is wrong; should be p. 468.** | Direct `pdftotext -f 12 -l 12` extraction shows the full sentence — "Usually I try to engage them in a little conversation and try to build a rapport and a little longer lasting relationship" (P10) — on the PDF page whose printed header reads "468 Work, Employment and Society 34(3)." The correct page is **468**, which is the *original* value the card's 2026-08-29 note replaced with 467. That correction was a mistake (same drift-prone method as above), and PAPER.md currently carries the bad fix. **Correct PAPER.md line 145 from "(p. 467, participant P10)" to "(p. 468, participant P10)."** |
| P39 incident, p. 469: "migrated established client relationships off-platform to preserve economic viability" | ACCURATE | Confirmed directly: "P39, who was unable to recover from a bad rating early in his..." on the page printed "469." This matches the card's later, more reliable A2/A3-sweep correction (468→469) — that one was right. |
| Uber/Upwork contrast, p. 470: "automated dispatch systems such as Uber, where algorithms assign labor deterministically" | ACCURATE | Confirmed directly: "the Uber platform plays a more dominant role, assigning workers and clients to each other based on algorithmic calculations" on the page printed "470." |
| Jarrahi and Sutherland's (2019) sensemaking/circumventing/manipulating lineage | ACCURATE (background) | Matches `jarrahisutherland2019.md` card exactly — three worker-to-system activities, no counterpart role, consistent with the manuscript's framing of an "adversarial dyad." |

**Net correction needed for Sutherland et al.:** PAPER.md line 145's P10 quote page should read
**468**, not 467. No other change needed — the "some verification" quote at line 143 is already
correct at p. 463 and must not be touched.

### What These Boundaries Share, lines 153-169

| Citation | Claim | Verdict |
|---|---|---|
| Oeldorf-Hirsch and Neubaum (2025) | 50 empirical investigations, four research databases, pervasive conceptual fragmentation | ACCURATE | Card confirms: 96 screened, 50 reviewed, across Google Scholar, Communication and Mass Media Complete, PsycInfo, and ACM Digital Library (four databases); "no cohesive construct exists." |
| Gagrčin et al. (2024) | 169 peer-reviewed studies, entrenched absence of unified theoretical frameworks | ACCURATE | Card confirms "169 studies" and "lacks a cohesive framework." |
| Iyamu et al. (2026) | Nutbeam's tripartite hierarchy; communicative literacy largely absent from conceptual frameworks and instruments | ACCURATE | Card confirms the three-level Nutbeam model (functional/critical/communicative) and that "communicative literacies were infrequently assessed" and only 1 of 12 studies defined algorithmic literacy as a distinct construct. The manuscript's clinician-patient gloss on "communicative literacy" matches the card's "interacting with a system and explaining what it produced to another person." The "(2000)" attributed to Nutbeam's model is plausible (Nutbeam's health-literacy framework is standardly dated 2000) but is not itself confirmed by the card, which doesn't give Nutbeam's original year. |
| Abidin (2016) | Strategic self-presentation before a specific, identifiable influencer; brackets algorithms as "analogue affective labour" | ACCURATE | Matches card closely, including the specific quote the card itself verified ("visibility labour is concerned with analogue affective labour ordinary users perform to be noticed by prolific elite users") and the "identifiable human counterpart" framing. |
| Cotter (2019) | "The visibility game," influencers and algorithms negotiating influence, human audiences pursued through opaque system | ACCURATE (background) | Matches card's summary of the visibility-game construct and relational/simulation typology. |
| Bucher (2017) | "Algorithmic imaginary," folk understandings shape conduct and feed back into the system | ACCURATE (background) | Matches card almost verbatim. |
| DeVito et al. (2018) | Folk theories assembled from observation, talk, press coverage, platform statements; put to work for self-presentation under obscured audience conditions | ACCURATE (background) | Matches card's "What it argues" closely; no page-specific quote used, so no page check needed. |
| Litt (2012) | Imagined audience as anticipatory mental construction against which disclosure is calibrated | ACCURATE (background) | Matches card; no direct quote used. |
| Katsh and Rifkin (2001) | "Fourth party" exerting autonomous influence, two human disputants through an authoritative intermediary | ACCURATE | Matches card's "fourth party... a positioned entity with its own effects on an outcome that binds both disputants." |
| Wing et al. (2021) | Evaluate opaque, protection-withholding fourth-party variants through a normative legal/ethical framework | ACCURATE | Matches card's "ethical design requirements: transparency, accountability, contestability, protection against bias, informed consent." |
| Curchod et al. (2020) | Automated feedback regimes dismantle bilateral exchange, asymmetrical triad (platform, buyers, sellers), visibility gap lets buyers evaluate invisibly | ACCURATE | Matches card, including the card's own prior wording-verification note ("in place of traditional dyadic exchanges, customer reviews enact triadic relationships among the platform operator, buyers, and sellers" and the visibility-gap passage), confirmed against the WRAP manuscript text. |
| Cameron (2024) | Formalizes the "algorithmic labor triangle"; continuous, bounded choices generate labor consent and system stability | **MOSTLY ACCURATE, one unsupported word.** | "Algorithmic labor triangle" is a genuine term from the paper — I located it directly in the source text (`cameron2024.txt`): Figure 1 is titled "Algorithmic Labor Triangle and On-Demand Work," and Table 1 lists "Algorithmic labor triangle: app–worker–customer–(merchant)" as the on-demand-work analogue to the "customer service triangle." This is NOT in the card (the card's summary focuses entirely on "constant and confined choice" and never mentions the triangle), so a checker relying on the card alone would flag this as unsupported — it is not. However, "system stability" as an outcome specifically attributed to Cameron's triangle is not supported: I searched the full paper text for "stability" and "equilibrium" and found no occurrence bearing on this claim (the paper's own vocabulary is "consent," not stability/equilibrium). "System stability" appears to be borrowed from the *manuscript's own* later, group-level sentence about Curchod/Cameron/Healy & Pekarek together ("how equilibrium emerges") and misattributed here to Cameron individually. Recommend cutting "and system stability" from the Cameron sentence, or rewording so the equilibrium/stability claim only appears in the group-level summary sentence where it is not tied to one source. |
| Healy and Pekarek (2025) | Integrate the triangular framework into labor process theory; worker vulnerability and institutional control | BACKGROUND / loosely characterized | Card confirms the substantive claim (consumer as third party, triangular relationship, worker vulnerability from the triangle) and confirms the 2025 citation year is defensible (Wiley early view 2024, issue 40(2) is 2025). However, the card frames the paper's own theoretical grounding as the *labour-law literature on triangular employment* (agency work, labour hire), not explicitly "labor process theory" — that term is not used in the card's account of this source (it is used elsewhere in the batch for Rahman). This is a minor categorical looseness, not a factual error, since the paragraph is grouping three sources under a shared "organizational and labor-process" heading rather than making a specific claim about Healy and Pekarek's own theoretical lineage. |
| Manky (2025) | Ride-hailing drivers in Lima (N=40) interpret opaque platform metrics to infer passenger trustworthiness and ensure physical safety | ACCURATE, but **no card exists in `literature/cards/`** | No `manky2025.md` file is present in the cards directory, contrary to what the task brief expected. The claim is nonetheless well-supported by two other lab documents: `GAPS.md` ("40 interviews with Lima ride-hailing drivers who use platform data to read... passengers") and `CONTEXT_AND_REGION_2026-08-26.md` ("40 in-depth interviews with Lima ride-hailing drivers. Drivers value platforms not for job security but for mitigating physical risk... data-driven oversight of passengers and routes... Manky's drivers use the intermediary to read the human counterpart"). The citation year (2025, not the earlier "2026") matches `VERIFICATION_2026-08-29_full_sweep.md`'s note that this was corrected in PAPER.md on 2026-08-29 to "Manky, O. (2025), *New Technology, Work and Employment*, 41(1), 33–44." The claim checks out, but flag for the author that this source has no formal literature card, unlike every other citation in this section. |

### Summary table

| Citation | Line(s) | Verdict |
|---|---|---|
| Zhou et al. (2025) — sample sizes, dimensions, reliability, r-values | 115-117 | ACCURATE |
| Zhou et al. (2025) — p. 2 definition quote | 115 | ACCURATE (independently verified) |
| Zhou et al. (2025) — Item 8 / Item 11 quotes, p. 8 | 119 | ACCURATE |
| Zhou et al. (2025) — Item 6 quote, p. 8 | 121 | ACCURATE |
| Zhou et al. (2025) — "audio recordings, timestamped delivery logs" narrative | 121 | **DRIFTED — invented detail, not in source** |
| Zhou et al. (2025) — antecedents (peer support × collectivism) | 125 | ACCURATE |
| Rahman (2021) — all quotes and page numbers (976, 956, 954, 954, 960) | 129-135 | ACCURATE — matches task brief's expected corrected values exactly |
| Sutherland et al. (2020) — abstract quotes, p. 457 | 141 | ACCURATE |
| Sutherland et al. (2020) — platform-literacy quote, p. 470 | 141 | ACCURATE |
| Sutherland et al. (2020) — walkthrough method, pp. 461-463 | 143 | ACCURATE |
| Sutherland et al. (2020) — "some verification" quote, p. 463 | 143 | ACCURATE as written — do not change to 462 |
| Sutherland et al. (2020) — P10 quote | 145 | **DRIFTED — currently p. 467, should be p. 468** |
| Sutherland et al. (2020) — P39 incident, p. 469 | 147 | ACCURATE |
| Sutherland et al. (2020) — Uber contrast, p. 470 | 149 | ACCURATE |
| Jarrahi and Sutherland (2019) | 141 | ACCURATE (background) |
| Oeldorf-Hirsch and Neubaum (2025) | 157 | ACCURATE |
| Gagrčin et al. (2024) | 157 | ACCURATE |
| Iyamu et al. (2026) | 157 | ACCURATE |
| Abidin (2016) | 159 | ACCURATE |
| Cotter (2019) | 159 | ACCURATE (background) |
| Bucher (2017) | 161 | ACCURATE (background) |
| DeVito et al. (2018) | 161 | ACCURATE (background) |
| Litt (2012) | 161 | ACCURATE (background) |
| Katsh and Rifkin (2001) | 163 | ACCURATE |
| Wing et al. (2021) | 163 | ACCURATE |
| Curchod et al. (2020) | 165 | ACCURATE |
| Cameron (2024) | 165 | **MOSTLY ACCURATE — "system stability" unsupported, cut it** |
| Healy and Pekarek (2025) | 165 | ACCURATE (background, minor categorical looseness) |
| Manky (2025) | 169 | ACCURATE — but **no card exists**; supporting material is in GAPS.md / CONTEXT_AND_REGION file only |

### Three items need author attention before Lima

1. **PAPER.md line 145 (Sutherland et al., P10 quote)** — change "(p. 467, participant P10)" to
   "(p. 468, participant P10)." The card's earlier correction note was itself wrong; direct PDF
   verification confirms 468 is correct.
2. **PAPER.md line 121 (Zhou et al., Item 6 narrative)** — "(audio recordings, timestamped delivery
   logs)" is invented detail not present in the working paper or journal VoR. The actual qualitative
   exemplar (interviewee N22) says only "evidence like recordings." Cut the parenthetical or replace
   it with an accurate gloss.
3. **PAPER.md line 165 (Cameron 2024)** — "generate labor consent and system stability" — cut "and
   system stability." No occurrence of "stability" or "equilibrium" appears in Cameron (2024)
   bearing on this claim; it appears to be borrowed from the paragraph's own later group-level
   sentence about Curchod/Cameron/Healy and Pekarek together.

**One item needs a card built:** Manky (2025), line 169 — the claim checks out against `GAPS.md`
and `CONTEXT_AND_REGION_2026-08-26.md`, but no `literature/cards/manky2025.md` exists, unlike every
other source in this section.

**One correction to the literature/cards themselves (not PAPER.md):** `cards/sutherland2020.md`'s
"Verified 2026-08-29" note wrongly "corrects" the "some verification" quote to p. 462; direct
per-page-header extraction shows p. 463 is correct and PAPER.md should not be changed. The card
should be amended so a future pass doesn't re-introduce the error.
