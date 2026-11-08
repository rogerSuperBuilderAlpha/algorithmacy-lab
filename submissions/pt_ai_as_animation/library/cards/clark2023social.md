---
key: clark2023social
apa: "Clark, H. H., & Fischer, K. (2023). Social robots as depictions of social agents. *Behavioral and Brain Sciences*, *46*, Article e21. https://doi.org/10.1017/S0140525X22000668"
authors: "Clark, Herbert H.; Fischer, Kerstin"
year: 2023
registered_year: 2022
title: "Social robots as depictions of social agents"
venue: "Behavioral and Brain Sciences"
volume: "46"
issue: ""
pages: "Article e21"
doi: "10.1017/s0140525x22000668"
url: ""
type: article
facets: [F10]
claims: [c9, c10]
role: anchor
load: load-bearing
read_depth: abstract
object_read: "No text held. Records only: crossref.json (Crossref, with the JATS abstract) and openalex.json (W4221071943), at ~/iit-playground/pt_ai_animation_local/pdfs/clark2023social/; nothing in ~/iit-playground/pt_ai_animation_local/inbox/; read 2026-11-08. No PDF; sha256 of the records 1a95465f7b3efca03c423b8600744adf1bdc1ff2f9e2b0f7ace8d2ff9c728558 (crossref.json) and aabd829ef97ede668a747f2f4ccfc1beb9a832ccfe262a09b244c4dbfd4af0af (openalex.json), computed with shasum -a 256 [Corrected by Fable, S7: the card had 'No sha256 (no PDF)']. The open copy (SDU portal d790c03c-4181-429c-bc5b-36fd59f8eae9) returned 403 to S4 (FETCH_LOG.tsv); the work is on BROWSER_LIST.md."
verified: verified
verified_against: "crossref.json (authors, title, BBS 46 e21, DOI, dates, JATS abstract) and openalex.json (W4221071943, 2022, green OA, affiliations); abstract quotations checked; FETCH_LOG and BROWSER_LIST rows"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Clark & Fischer (2023), Social robots as depictions of social agents

## What it argues

This card rests on the abstract in the Crossref record only; I have not read the article.

Herbert H. Clark (Stanford) and Kerstin Fischer (University of Southern Denmark) ask how people can
know that social robots are mechanical artifacts and still interact with them "as if they were
actual agents". Their proposal is that people construe social robots not as social agents per se
but as *depictions* of social agents, interpreted "much as they interpret ventriloquist dummies, hand
puppets, virtual assistants, and other interactive depictions of people and animals". Depictions,
in their account, consist of three physical scenes with part-by-part mappings: a base scene (the
raw artifact), the depiction proper (the artifact construed as a depiction), and the scene depicted
(what people are to imagine). The abstract says evidence shows people form the same three scenes
with robots and "engage in the pretense" that they interact with the character depicted. People
also recognise three classes of agents: the characters depicted, the intended recipients, and "the
authorities responsible for the robots (the designers, makers, and owners)". The authors claim the
account covers phenomena that alternative models miss. The article appeared in *BBS* with open peer
commentary and an authors' reply (see Caution).

## What the paper uses it for

- **c9** (triadicity, narrowed: the studio *determines* what the viewer gets): prior triad, per
  Checkpoint B ruling 2. The abstract places the makers inside the interaction as a third class of
  agent, "the authorities responsible for the robots (the designers, makers, and owners)". That is
  close to c9 and threatens its novelty. What the third party does, as far as the abstract says: it
  is "responsible for" the robot. The abstract does not say that the authorities make binding
  determinations about what the recipient gets, hold an interest of their own, or keep the
  character and recipient apart, which are the lab criterion's three tests. The paper's distinction
  from Clark & Fischer rests on those tests, and this card cannot yet say whether the full article
  meets them. That check needs the text.
- **c10** (the analogy breaks at liveness; puppetry is the closer case): support from the abstract.
  The authors' model class is interactive depiction (ventriloquist dummies, hand puppets, virtual
  assistants), the live, answering-back kind of depiction the paper's §5 reaches for, as opposed to
  pre-rendered animation. Their base scene / depiction / depicted scene structure may also give §5
  the vocabulary to say what is animated and what is merely operated. Whether they discuss LLMs
  or animation proper is not visible in the abstract.
- **Stretch to avoid:** the abstract concerns how *recipients* construe robots. Nothing in it
  concerns how the makers build the depiction, so it gives the paper no support on the
  development side (c1, c6).

## Loci

None. No text was read (abstract-only card); quotations from the abstract appear in "What it argues"
for orientation and are not loci.

## Caution

- **Abstract only; on BROWSER_LIST.md** (rows 9 and the closed-works table). The SDU portal copy
  refused this machine (403). The card's c9 distinction cannot be finished until Roger opens the
  article: the paper needs exactly what the "authorities" do in the full text (DECISIONS asks the card
  to record it, per Checkpoint B ruling 2).
- **Commentaries.** DECISIONS asks the card to note which *BBS* commentaries press the "authorities"
  class. No commentary text or list is in the local records, so I cannot. That stays open for the
  writer who gets the browser copy.
- **Registered year.** Crossref: published online 28 March 2022, print 2023, volume 46, article
  e21. OpenAlex publication_year 2022. The key and `year` take the volume year 2023;
  `registered_year: 2022`, as DECISIONS ("Record corrections") directs.
- **Reply is a different DOI.** The authors' response to commentaries is e51,
  10.1017/s0140525x22002825 (per DECISIONS; no record of it in the folder). It is not the target
  article. DECISIONS ("Record corrections") flags the confusion; I did not find that DOI in
  FACETS.md, so the earlier mispairing sits in a triage or search file, which is left alone.
- **Open access status.** OpenAlex marks the work green OA via the SDU repository; the publisher
  copy is not open (`is_oa: false` on the primary location; licence is Cambridge's terms page).
- **Role.** DECISIONS sets `anchor`; after Checkpoint B the work is both precedent and foil for
  c9. Fable may prefer `contrast`.

## Verification
- date: 2026-11-08; agent: S6 verifier (opus), batch W3 group 2
- verdict: verified. Frontmatter matches crossref.json: Clark, Herbert H. and Fischer, Kerstin; title; *Behavioral and Brain Sciences* 46, article e21; DOI. Crossref gives online 28 Mar 2022 and print 2023, and OpenAlex gives 2022, so `year: 2023` with `registered_year: 2022` is right. `read_depth: abstract` and `## Loci` None are honest. No text is held, FETCH_LOG.tsv row 45 records the 403, and BROWSER_LIST lists the work (row 9 and the closed-works table). Every phrase the card quotes from the abstract is verbatim in the Crossref JATS abstract. The Stanford and SDU affiliations come from openalex.json.
- checked: the c9 bullet claims only what the abstract says about the "authorities" (that they are "responsible for" the robots), and it leaves the lab-criterion test open. The reply DOI e51 is marked as coming from DECISIONS, with no local record. The OA note matches openalex.json (green via SDU; primary location not OA) and the Crossref licence URL.
- for Fable: `status: cited`, but SOURCE.md and SKETCH.md do not name Clark & Fischer; README's c9 wording does. The role question (anchor or contrast) is flagged on the card.
- changed: nothing

## Hand-check

- 2026-11-08, Fable (S7). Verdict: **index after fix** (fixed here).
- Checked: 0/0 (abstract card, Loci None); every phrase quoted in 'What it argues' is verbatim in the Crossref JATS abstract; frontmatter vs crossref.json and openalex.json (BBS 46, e21; online 2022-03-28, print 2023; registered_year 2022); record sha256 values computed; ruling B2 met: the card records that the abstract makes the third party 'responsible for' the robots and no more.
- Changed: object_read had 'No sha256 (no PDF)'; added the sha256 of crossref.json and openalex.json, marked.
- For the author: (1) role: anchor per DECISIONS, but after Checkpoint B the work is precedent and foil; 'contrast' may fit better. (2) The lab-criterion test (binding determination, own interest, keeping the parties apart) cannot be finished from the abstract; the article is on BROWSER_LIST.md.
