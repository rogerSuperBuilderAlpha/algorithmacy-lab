---
key: weinmann2016digital
apa: "Weinmann, M., Schneider, C., & vom Brocke, J. (2016). Digital nudging. *Business & Information Systems Engineering*, 58(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1"
authors: "Weinmann, Markus; Schneider, Christoph; vom Brocke, Jan"
year: 2016
title: "Digital Nudging"
venue: "Business & Information Systems Engineering"
volume: "58"
issue: "6"
pages: "433–436"
doi: "10.1007/s12599-016-0453-1"
url: ""
type: article
facets: [F6]
claims: [c1]
role: anchor
load: load-bearing
read_depth: full_text
object_read: "Springer open-access PDF, published online 3 Oct 2016 (journal version, 4 pp.); local copy ~/iit-playground/dxd_animation_local/pdfs/weinmann2016digital/weinmann2016digital.pdf, text layer weinmann2016digital.txt; original URL https://link.springer.com/content/pdf/10.1007/s12599-016-0453-1.pdf (FETCH_LOG.tsv row weinmann2016digital); read 2026-11-05; sha256 c70013fb586234268369cb31cb64b51543b3b7607110b73e2dd9e8eea4bb3ac3"
verified: corrected
verified_against: "Springer OA PDF (pdftotext reading-order extraction and the .txt layer), crossref.json, openalex.json; sha256 recomputed"
prior_cards: []
status: cited
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

I read the whole 4-page text (title page through reference list). It is a short "Catchword" piece, a conceptual overview for information-systems readers. It reports no study and no data.

The three authors define digital nudging as "the use of user-interface design elements to guide people's behavior in digital choice environments" (p. 433). A digital choice environment is any user interface that makes people judge or decide, and they name web forms and ERP screens. Their central premise is that no interface is neutral. Every layout, default and ordering of options steers choices, sometimes by the designer's intent and sometimes by accident (pp. 433–434). They infer that designers must understand what their interfaces do to choices, so that a nudge is deliberate and not random (p. 434).

They borrow the toolkit from offline nudging (Thaler and Sunstein; Johnson and colleagues) and list six nudge principles in Table 1: incentives, understanding mapping, defaults, giving feedback, expecting error, and structuring complex choices (p. 435). Table 2 lists example uses by information-systems field, from business process management to social media (p. 435). They note that research on nudging "has been conducted primarily in offline contexts" (p. 434), call digital nudging an early-stage field, and ask for work on its theoretical mechanisms and on design recommendations (p. 435). They add an ethics warning: nudges meant to help people can be used for short-term company gain, with long-term costs in goodwill and legal exposure (p. 434).

## What the paper uses it for

- c1: this is the source for the paper's term "digital nudging" and for the definition the paper can state (SOURCE.md Pass 2 cites it for "digital nudging tools"; CHECK F6). It supplies the conversion-era picture the paper argues against: the designer fixes the choice environment and steers the user toward an option once the options are set. The paper can cite it for "no interface is neutral" and for "the designer picks the nudge".
- c1, where the use stretches the source: Weinmann and colleagues never ask where the user's goal comes from. Their environment holds a decision the user already has to make ("require people to make judgments or decisions", p. 433). A reader who cites them for the claim that nudging presumes a fixed goal is reading that presumption into a text that does not state it. The paper has to argue it, and should say so.
- c1, c3: the claim that "there is no neutral way to present choices" (p. 433) helps the paper's point that an interface acts on the user whether or not the designer meant it to. Weinmann and colleagues say this about screen layout, not about an LLM that answers back.

## Loci

Quotations are verbatim. The source uses double quotation marks around inner quotations ('nudge', 'tipping'); I use single quotes where a quotation contains them. Locators are the journal pages printed in the text (433–436). Each line was matched against the local PDF, using its pdftotext extraction and the .txt text layer.

- "Digital nudging is the use of user-interface design elements to guide people’s behavior in digital choice environments." — p. 433, §1. Matched against the local PDF text.
- "Digital choice environments are user interfaces – such as web-based forms and ERP screens – that require people to make judgments or decisions." — p. 433, §1. Matched against the local PDF text.
- "In fact, there is no neutral way to present choices." — p. 433, §1. Matched against the local PDF text.
- "Since there is no neutral way to present choices, all decisions related to user-interface design influence users’ behavior (Mandel and Johnson 2002; Sunstein 2015), often regardless of the designers’ intent." — p. 434, §2. Matched against the local PDF text.
- "Research on nudging has been conducted primarily in offline contexts." — p. 434, §3. Matched against the local PDF text.
- "Nudges attempt either to counter or to encourage the use of heuristics by altering the choice environment to change people’s behavior." — p. 434, §3. Matched against the local PDF text.
- "As user interfaces will always steer people in certain directions (depending on how information is presented), information systems designers must understand the behavioral effects of interface design elements so that digital nudging does not happen at random and unintended effects do not occur." — p. 434, §4.2. Matched against the local PDF text (the .txt layer interleaves this sentence with the other column; the pdftotext extraction gives it whole).
- "Preselecting options by setting default options" — p. 435, Table 1, row 'Defaults' (the description cell). Matched against the local PDF text.
- "clarification of the theoretical mechanisms that underlie digital nudging is needed" — p. 435, §4.2. Matched against the local PDF text.

## Caution

- The article is a 4-page conceptual overview and carries no evidence of its own. Its claims about the effect of defaults rest on one cited result (Johnson and Goldstein 2003, organ donation) and one trade-press example (a payment app's tip default, from a 2013 web article). The paper should not cite it for effect sizes. Jachimowicz et al. (2019), carded separately as `jachimowicz2019when`, supplies those.
- `../CHECK.md` row F6 says the lab could not open this article and took its definition from the later CACM piece (Schneider, Weinmann and vom Brocke, 2018). This run opened and read the BISE text, so the definition now comes from the source: quoted above, p. 433. CHECK F6's citation details (58(6), 433–436, DOI) match the printed header and Crossref record. `../OUTLINE.md` §1 lists Weinmann et al. (2016) as "rec" (recommended, needs a library copy); this card is that copy.
- Springer's page for this DOI bot-walled the September run (see triage). This run's FETCH_LOG row shows a 200 response with the open-access PDF (the URL there carries a cookie-error query string; the card gives the clean URL). No wall in the way of this read.
- Crossref records the third author's family name as "Brocke" and puts "vom" in the given name ("Jan vom"). The printed article reads "Jan vom Brocke". The card follows the printed form.
- The abstract on OpenAlex is a keyword list, as the triage notes. The definition quoted above comes from the text, not the record.
- Year: published online 3 Oct 2016; Crossref's print date is Dec 2016, vol. 58 issue 6. The card takes the volume year, 2016, which matches the OUTLINE citation.

## Verification

2026-11-05 · S6 verifier, batch b04 (opus; not the writer) · verdict: corrected · checked: loci 9/9 found at the stated journal pages (PDF p. 1 = p. 433); metadata vs crossref/openalex (authors, 2016 vol. 58(6), 433–436, DOI) match; full_text honest (4 pp. read whole by verifier too); sha256 matches; four sections in order · changed: What it argues: first sentence named the authors as the readers, now 'I read'; Table 2 range starts at business process management, not e-commerce; Loci note on the §4.2 sentence (it sits whole in one column; only the .txt interleaves it); Caution: Crossref holds 'vom' in the given name, not absent
