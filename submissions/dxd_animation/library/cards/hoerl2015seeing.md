---
key: hoerl2015seeing
apa: "Hoerl, C. (2015). Seeing motion and apparent motion. *European Journal of Philosophy*, *23*(3), 676–702. https://doi.org/10.1111/j.1468-0378.2012.00565.x"
authors: "Hoerl, Christoph"
year: 2015
registered_year: 2012
title: "Seeing Motion and Apparent Motion"
venue: "European Journal of Philosophy"
volume: "23"
issue: "3"
pages: "676–702"
doi: "10.1111/j.1468-0378.2012.00565.x"
url: "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1468-0378.2012.00565.x"
type: article
facets: [F2]
claims: [c6]
role: contrast
load: load-bearing
read_depth: abstract
object_read: "Registry records only, no PDF: OpenAlex W2121842656 (carries the abstract), at ~/iit-playground/dxd_animation_local/pdfs/hoerl2015seeing/openalex.json (sha256 35328e3d316b310d287c5ea1e96bfb55482d2d5d22eb2c8b07aa7a78e3c831ee), and the Crossref record (no abstract), crossref.json (sha256 11b79f464a23ccbdf35489940c54676606e2af468a93ac325f11ca5977ba64d1); the scripted fetch of https://doi.org/10.1111/j.1468-0378.2012.00565.x returned HTTP 403 (FETCH_LOG.tsv, status closed); read 2026-11-05"
verified: verified
verified_against: "Crossref crossref.json (sha256 11b79f46 recomputed) and OpenAlex openalex.json (sha256 35328e3d recomputed; abstract rebuilt from inverted index): author, vol 23(3) 676-702, print 2015-09, online 2012-08-29, DOI, pdfdirect URL, counts 9/25; FETCH_LOG 403; SOURCE Pass 2 wording"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

# Hoerl (2015), Seeing motion and apparent motion

## What it argues

This card rests on the OpenAlex abstract only; I read no text of the article.

Hoerl starts from the experiment: participants see "a succession of two brief stationary stimuli at two
different locations, but they report an impression of movement". Philosophers have debated whether apparent
motion favours one account of temporal experience. Hoerl argues that this debate "is premised on a mistaken
view of the phenomenology of apparent motion", so the space of positions "has not yet been fully explored".
His positive claim is that apparent motion "is compatible with an account of the nature of temporal
experience that involves a version of direct realism". Along the way he argues "against two other claims
often made about apparent motion, viz. that apparent motion is the psychological phenomenon that underlies
motion experience in the cinema, and that apparent motion is subjectively indistinguishable from real
motion".

## What the paper uses it for

- **c6** (animation is co-optive; the viewer locks in): this is the contrast. Pass 2 says the viewer "locks
  in" and "the perceptual gaps disappear". CHECK F12 proposes calling that apparent motion, after Wertheimer.
  Hoerl denies both halves of that move: that apparent motion underlies cinema, and that it is
  indistinguishable from real motion. If he is right, "apparent motion" is the wrong label for film's
  lock-in, and "the gaps disappear" overstates what a viewer experiences. The source cuts against the
  paper's current wording and against CHECK's fix (DECISIONS, finding b). The paper must state which
  phenomenon it means before §4.2 is drafted.

## Loci

None

## Caution

- Read depth: DECISIONS approved this as "full_text, open (Wiley bronze)", but the fetch returned HTTP 403 and
  no PDF or text layer is held. OpenAlex still lists the bronze pdfdirect URL; a browser may open it. The
  card stays abstract-depth until then, and the paper's use must say it rests on the abstract.
- Year: Crossref dates it online 2012-08-29 and in print 2015-09, volume 23, issue 3. The card takes the
  volume year with `registered_year: 2012` (README rule 4); OpenAlex gives `publication_year` 2012.
- The abstract does not say what Hoerl thinks does underlie motion experience in the cinema. That is the
  question the paper needs answered, and only the full text can answer it.
- Counts: Crossref 9 citing works; OpenAlex 25.

## Verification

2026-11-05 · S6 verifier, batch b08 (opus; not the writer) · verdict: verified · checked: loci 0/0; abstract quotations verbatim; metadata vs crossref/openalex; registered_year 2012 correct; depth abstract honest · changed: nothing

## Hand-check

- 2026-11-05, Fable (S7). Verdict: **index**.
- Checked: 0/0 loci (None; the five abstract phrases in 'What it argues' are verbatim from the OpenAlex abstract, rebuilt from the inverted index, and cited as the abstract); author, title, EJP 23(3) 676–702, DOI, online 2012-08-29, print 2015-09, registered_year 2012, pdfdirect URL, counts 9/25 and both sha256 values against crossref.json and openalex.json; FETCH_LOG 403; SOURCE Pass 2 line 32 does say the viewer 'locks in' and 'the perceptual gaps disappear', and CHECK F12 does propose apparent motion after Wertheimer, so the c6 contrast is stated correctly.
- Changed: nothing.
- For the author: besides the Wiley bronze URL the OpenAlex record lists an accepted-version PDF at Warwick WRAP (http://wrap.warwick.ac.uk/50746/1/WRAP_Hoerl_ejop565.pdf) and a PhilPapers archive copy (philarchive.org/rec/HOESMA); either may open in a browser and would let the card answer what Hoerl thinks does underlie cinema motion (DECISIONS finding b), which the abstract leaves open.
