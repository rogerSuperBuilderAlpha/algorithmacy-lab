---
citekey: felt2012android
title: "Android permissions: user attention, comprehension, and behavior"
authors: Felt, Adrienne Porter; Ha, Elizabeth; Egelman, Serge; Haney, Ariel; Chin, Erika; Wagner, David
year: 2012
type: article
doi: 10.1145/2335356.2335360
venue: Proceedings of the Eighth Symposium on Usable Privacy and Security (SOUPS '12), article 3, pp. 1-14
source_basis: partial-text
pages_read: "pp. 1-2 (abstract, introduction, contributions) and p. 5 (attention during installation, Table 1, warning-fatigue passage)"
source_url: https://cups.cs.cmu.edu/soups/2012/proceedings/a3_Felt.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/felt2012/page.pdf
sha256: 58cd8da0afd4572e90300b2ae0079cc1e8a3a8f7016c73e8edf29c03637abad4
manuscript_lines: []
ledger_rows: [H24, E15, H19]
premises: [A8, A4]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
A survey of 308 Android users and a lab study of 25 tested whether install-time permission screens, a consent prompt
before a program gains capabilities, are attended to and understood. 17% paid attention at installation in both
studies; 42% of lab participants did not know permissions existed; 3% of survey respondents answered all three
comprehension questions. Some former readers had stopped looking, which the authors attribute to warning fatigue. Crossref
confirms title, venue and year.

## Key facts it relies on
- "both the Internet survey and laboratory study found that 17% of participants paid attention to permissions during
  installation, and only 3% of Internet survey respondents could correctly answer all three permission comprehension
  questions" (abstract, p. 1).
- "42% of laboratory participants were unaware of the existence of permissions" (p. 2).
- One participant: "I used to look...I just stopped doing that." The authors: "These participants might have
  experienced warning fatigue, since users see permission warnings for about 90% of applications" (p. 5).

## Critical notes from the literature
- 2012 smartphone permissions, not agent approvals; read in part.
- The authors also find "a notable minority of users demonstrated both awareness of permission warnings and
  reasonable rates of comprehension" (abstract, p. 1).

## Where the argument uses it
- M8 and H24 (disclosure in place of understanding): supports. A pre-action consent screen, the ancestor of agent
  permission prompts, was attended to by about one user in six and understood fully by 3%. It corroborates, outside any
  AI vendor, the approval-fatigue reading of anthropic2026how and anthropic2026measuring.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
