# Lukoff, K., Lyngs, U., Zade, H., Liao, J. V., Choi, J., Fan, K., Munson, S. A., & Hiniker, A. (2021). How the design of YouTube influences user sense of agency. In *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems* (pp. 1–17). ACM.

**Identifier:** doi:10.1145/3411764.3445467; arXiv:2101.11778 · **Read depth:** full_text (arXiv v1, 28 Jan 2021, 17 pp., marked "Updated for pre-print"; the PDF has no printed page numbers, so I cite PDF pages and section numbers; the reference list and the appendix pointers read, the OSF appendices not available) · **Source-tier:** proceedings (preprint copy) · **Evidence basis:** direct_read · **Design and sample:** Study 1, online survey of 120 US YouTube-app users recruited on Mechanical Turk (80 Android, 40 iPhone; median 101 minutes a day on YouTube), coded by thematic analysis; Study 2, 13 co-design sessions in Seattle (7 women, 6 men, median age 29), sketching plus ranking of low-, medium- and high-control mockups · **Parties modeled:** person–system (the app), with the platform's own interests named as one stakeholder among several · **Facets:** H · **Read:** 2026-10-13

## What it argues
The authors ask which internal mechanisms of one app, as opposed to screen-time tools that police many apps, change a user's sense of agency. In Study 1 each of the 120 respondents named three things that made them feel most in control and three least. Of 720 responses, 467 named a design mechanism (246 "less in control", 221 "more"). Inter-rater agreement on a 50-response sample was kappa = 0.73 (§3.3, p. 5). The abstract's result: "autoplay and recommendations primarily undermine sense of agency, while search and playlists support it" (p. 1).

By count (Table 3, p. 6): recommendations 128 mentions (27% of the coded mechanism responses), 77% of them "less in control"; ads 55, 98% less; autoplay 32, 87% less; playlists 39, none less; search 36, 33% less; notifications 15, split 53% less. Three themes: control tracks whether the user "agreed" to what the app did (the "spectrum of consent"); planning ahead helps; and algorithm accuracy cuts both ways, since relevant recommendations could undermine control "by being too engaging" (§3.4.4, p. 7).

Study 2 reports one result that matters for design. Participants "preferred higher-control mechanisms when they had a specific intention in mind and lower-control ones when they had a non-specific intention" (§5.3, p. 13), and they wanted active choices over reacting to a feed: "More choice alone did not lead to more control" (§4.5.2, p. 11). Most respondents "seemed either unaware of YouTube's existing customization settings for recommendations or found them inadequate" (§3.4.4, p. 8).

## Relation to the argument
**P9 and the engagement layer (D7).** The study measures felt control, not performance, so it cannot show that a control improves what people do. It does show that adding choice is not the same as adding control: more recommendations meant more passive choosing. That supports the paper's doubt that tools handed to the person (a settings page, a customisation menu) carry the work, and the finding that existing controls went unnoticed fits P9.

**P8.** The mechanisms users valued (search, a finite playlist with a stopping point, subscriptions) are structures that hold a person's stated intention and act on it. A user's own plan constrains the app. The user does not read the app to infer what it will do. This is close to P8's contrast but it is the facet's reading, not a result the authors test.

**P10.** The authors open on the attention economy: app mechanisms "exploit psychological vulnerabilities and harm the interests of the user" (p. 1), and the app owner "may wish to control how much time users spend in the app" (pp. 1–2). They also warn against optimising agency alone, because Google, creators, advertisers and society have stakes too (§5.5, p. 14). This is a worked case of an interface owner whose interest differs from the user's, which is the point of P10.

Facet check: facet H summarises the abstract accurately. Its "(i)-style restructuring, not an added control" reading is only partly borne out. The "high-control" mockups did remove recommendations (restructuring). But the authors' own proposals are mostly controls the user operates: customisation, explicit preferences, a toggle between Explore and Focus modes (§5.3). Users also wanted less control for "ritualized" use. The paper is therefore evidence for context-dependence, not for restructuring over tuning.

## In conversation with
- `cox2016design`: Cox et al. (2016) coined "microboundary", which Lukoff et al. extend into "microplans" (§5.2, p. 13).
- `seaver2018captivating`: cited as a source for recommender systems as traps (reference [101]).
- `gray2018dark`: cited for dark patterns (reference [43]); the authors propose "attention capture dark patterns" (§2.1, p. 2; §5.4, p. 13).
- Leads, not in the bib: Berberian et al. (2012), automation and sense of agency in flight navigation; Brignull's dark-pattern types; Shneiderman & Plaisant's "internal locus of control".

## Caution
Self-report only, on one app, one platform and a small co-design sample of 13 young adults. The survey sample over-represents men, Asian respondents and 25–44 year-olds; the authors say they did not ask about paid YouTube Premium (§3.1). They name present bias, the gap between self-reported agency and "the facts of agency", and the narrow focus on users as limits (§5.5, p. 14). Study 2 compares mockups, not a deployed system. I read the arXiv v1 preprint; the ACM version may differ in wording.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v1 PDF (2101.11778, 17 pp., 'Updated for pre-print'), extracted with pdftotext, with Table 3 re-read in layout mode. I checked 8 verbatim quotations and their pages, the sample facts (120 respondents, 80 Android and 40 iPhone, median 101 minutes a day; 13 co-design participants, 7 women, 6 men, median age 29, Seattle), 720 responses with 467 mechanism responses (246 and 221), kappa 0.73, every Table 3 count and percentage cited, the Premium admission, and the Cox, Seaver, Gray, Berberian, Brignull citations.

**Findings:** One locator fixed: 'attention capture dark patterns' is coined on p. 2, not p. 1 (it is developed again in section 5.4, p. 13). One mild embellishment noted, not changed: the card says the survey over-represents '25-44 year-olds'; the authors say they oversampled 'men, Asians, and young people', and Table 1 shows 41% aged 25-34 and 40% aged 35-44. All other numbers and quotations match. The facet phrase '(i)-style restructuring, not an added control' is the facet's wording, not the paper's.
