# Doyle, A., & McCrae, J. P. (2025). An assessment of word separation practices in Old Irish text resources and a universal method for tokenising Old Irish text. In B. Davis, T. Fransen, E. Uí Dhonnchadha, & A. Walsh (Eds.), *Proceedings of the 5th Celtic Language Technology Workshop (CLTW 5)* (pp. 1–11). International Committee on Computational Linguistics. https://aclanthology.org/2025.cltw-1.1/

**Identifier:** ACL Anthology 2025.cltw-1.1 (open access PDF; the Anthology record and its BibTeX give no DOI, name the publisher as the International Committee on Computational Linguistics, the address as "Abu Dhabi [Virtual Workshop]" and the month as January 2025) · **Read depth:** full_text (the 10 pages of text; the appendix tables of tokenised examples skimmed) · **Source-tier:** peer-reviewed workshop proceedings (computational linguistics) · **Evidence basis:** direct_read · **Design and sample:** survey of the word-separation practices of the existing Old Irish digital corpora (Würzburg, Milan and St Gall glosses, POMIC, CorPH, the UD treebanks) and a proposed tokenisation method; no experiment · **Parties modeled:** none (editors, corpora and the manuscript text) · **Facets:** W · **Read:** 2026-10-15

## What it argues

Old Irish, "written between roughly the 7th and 9th centuries" (§2), survives mostly as glosses: 3,501 Irish glosses in Würzburg, 8,443 in Milan, 3,478 in St Gall (§2). The paper's problem is that digital resources split the text into words by different rules, and the reason is the manuscripts: "Separating words is a deceptively difficult task for Old Irish ... for Old Irish 'words which are grouped round a single chief stress and have a close syntactic connexion with each other are written as one in the manuscripts' (Thurneysen, 1946, 24)" (§2). Clitics fuse and lose letters (*isamlid* for *is samlid*, §2, §3.5); nasalisation markers are written "as a part of that following word ... but are also frequently separated from it by spacing, and even enclosed by punctuation" (§3.5); some conjunctions "can nevertheless be found written graphically as two words in manuscripts" (§3.2). Modern editors add punctuation and hyphens that the manuscript lacks (Figures 1–2, §2). The proposed method tokenises by synchronic lexical word without altering characters (§3), and has been applied to the Würzburg glosses website and two UD treebanks (§4).

## Relation to the argument

The abstract credits "seventh-century Irish scribes" with breaking up *scriptio continua* "by adding spaces between words". The same scribes wrote their own language in stress-groups, not in the words a modern editor counts, and modern Irish studies still argue about where the words are. That is Tunbridge's point (card `tunbridge1992study`, pp. 89–92) from the other end: the separation of Latin was a grammarian's analysis of a foreign language, and it did not come from a native habit of writing words apart.

- **Narrows** the abstract's clause: the Irish separated Latin, which they parsed as learners; they did not discover a general truth about writing and apply it to everything they wrote.
- **Supports** the project's P5 and D8 (the scribe carries the analysis, and the convention lives in practice): what counts as a word is still being decided by editors twelve centuries later.
- Bears on "representational effect" alongside `barton1980awareness`: the word as a unit is in part an artefact of how a text is written down.

## In conversation with

- `tunbridge1992study`: the palaeographic account of Old Irish stress-group writing and Latin separation.
- `saenger1997space`: the Insular chapter (ch. 4) this complicates.
- Leads not in the bib: Thurneysen (1946), *A Grammar of Old Irish*, p. 24 on word grouping; Stifter (2006), *Sengoídelc*; Bronner (2016) on dry-point glosses; Griffith (2013) and Bauer (2015) corpora.

## Caution

A natural-language-processing paper about corpora, not a palaeographic study; its statements about manuscript practice rest on Thurneysen and on cited images of Cod. Sang. 904. It says nothing about Latin texts, spacing in them, or reading. Use it for the single point that Old Irish manuscripts grouped by stress, and cite Thurneysen through it with care.

## S2 adversarial verification (2026-10-15)

**Verdict: corrected (bibliographic fields and one locator).**

**What I checked:** Re-opened the Anthology PDF (local copy dxd_foundation_local/pdfs/W/doyle2025.pdf), re-extracted it in reading order, and fetched the Anthology page and its BibTeX on 2026-10-15. Confirmed in §2 ("Currently Available Corpora"): "written between roughly the 7th and 9th centuries"; 3,501 (Wb.), 8,443 (Ml.) and 3,478 (Sg.) glosses; "Separating words is a deceptively difficult task for Old Irish"; the Thurneysen (1946, 24) quotation word for word; "isamlid"; Figures 1–2 from Cod. Sang. 904. In §3.2: "can nevertheless be found written graphically as two words in manuscripts". In §3.5: nasalisation markers "generally written as a part of that following word ... but are also frequently separated from it by spacing, and even enclosed by punctuation". In §4: the method "has been employed by the online text repository of the Würzburg glosses ... as well as by two UD treebanks". The PDF footer reads "Proceedings of the 5th Celtic Language Technology Workshop (CLTW 5), pages 1–11, Abu Dhabi, UAE (Online), January 20, 2025". Read depth full_text stands.

**What I changed:** (1) The publisher: the Anthology's own BibTeX gives "International Committee on Computational Linguistics", not the Association for Computational Linguistics; the editors are added and the address corrected in the card and the facet .bib. (2) There is no §2.1; the figures stand in §2. Nothing in Relation to the argument claims more than the paper says; the card already restricts the use to the Thurneysen point.
