# Kroll, J. A. (2021). Outlining traceability: A principle for operationalizing accountability in computing systems. In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 758–771). https://doi.org/10.1145/3442188.3445937

**Identifier:** doi:10.1145/3442188.3445937 · arXiv:2101.09385 · **Read depth:** full_text (arXiv v1, 23 Jan 2021, 15 pp.; the pagination cited below is the arXiv PDF's, not the ACM 758–771. Body, pp. 1–9, read in full; the 250-entry reference list read for the citations named below, not entry by entry) · **Source-tier:** peer-reviewed proceedings paper, read as the preprint · **Evidence basis:** direct_read · **Design and sample:** none (a conceptual and policy review: AI principles documents from the US, EU, OECD and China, mapped to technical requirements and tools) · **Parties modeled:** other: system developers and operators, affected stakeholders, and oversight entities (courts, auditors, regulators) · **Facets:** G · **Read:** 2026-10-13

## What it argues
Kroll takes "traceability", a word that recurs in AI-governance documents, and asks what it requires of software. His definition: traceability "requires establishing not only how a system worked but how it was created and for what purpose" (abstract, p. 1). §2 (pp. 2–3) reads US executive orders, the Department of Defense and Intelligence Community principles, the EU high-level expert group, the OECD and Chinese governance principles for what they ask. §3 (pp. 4–6) distils five requirements: design transparency (including testing), reproducibility, operational recordkeeping, human understanding and auditability. §4 (pp. 6–8) lists the tools that exist: version control, provenance, value-sensitive design, structured logs, standardized disclosures such as model cards. §5 (pp. 8–9) sets out gaps: adoption, human factors, test and evaluation standards, and oversight.

Three claims run through it. Traceability is not disclosure: "disclosure alone does not provide traceability, and while traceability requires disclosure, they must not be equated" (§3.1, p. 4). It is not explainability either: "We refrain, however, from saying that traceability requires explainability" (§1, p. 2). And it is "a functional property of the tool in use" (p. 2), not of an artifact, so it depends on who reads the record and what they can do with it. The paper says "traceability is a human factors problem" (p. 2) and later notes that "there is comparatively little work on the human factors of how such explanation methods serve understanding" (§5.0.2, p. 9). Documentation, it adds, has "little in the way of research establishing its effectiveness at communicating within organizations or actually mitigating harms" (§4.5, p. 8).

On who holds the records, §3.3 (p. 5) names options: records that an outside party can check by cryptographic means, or "a trusted third party such as an oversight entity or an independent data trust", and it notes "trusted oversight entities which can receive disclosures under seal", with courts among the examples. §3.5 (p. 6) says audit is "a question both of design and governance": the system needs "interfaces that enable audit and also policies that allow effective uses of those interfaces". Automation, the paper says, leaves humans "both more critical to the outcomes driven by the system and less able to control those outcomes" (§4.3, p. 8), citing Bainbridge. The closing gap is institutional: "no technical control can be more capable than the implementing organization's willingness to take action based on it" (§5, p. 9).

## Relation to the argument
Kroll offers the policy vocabulary behind the post's "observe everything" and its records of meaningful model actions (post P15). It gives that demand a name and a list of requirements, and it asks the question the post leaves open: who can read the records and act on them.

It bears on ruling D3. The author holds that disclosure is a literacy intervention and not an algorithmacy one. Kroll's separation of traceability from disclosure supports the first half in another register: disclosing design choices does not, by itself, give anyone the capacity to hold a system to account, and he puts that capacity in audit and governance. It does not support D3's second half, that disclosure leaves "our ability to navigate" an algorithm untouched; Kroll makes no claim about navigation by users.

It bears on ruling D8 (who holds the convention) through §3.3 and §3.5: courts, auditors and trusted third parties are the holders he names.

Facet check: Facet G read only the abstract and introduction. The body supports its gloss that this is "the best formal statement" of what P15 asks. It adds that Kroll's records are mostly about design and development, with operations covered in §3.3, and that he treats the human-understanding requirement as unsolved.

## In conversation with
Cites `bainbridge1983ironies` (ref. 12, §3.4, §4.3, for operators who are less able to control outcomes), `elish2019moral` (ref. 85, with Elish & Hwang 2015, §3.4, for designs that obscure accountability for accidents) and `mitchell2019model` (ref. 171, model cards, §§3.1, 4.5). Cites his own Kroll et al. (2017), *Accountable algorithms* (ref. 143), not in the bib. He does not cite `santonidesio2018meaningful`; `green2022flaws` and `sterz2024quest` postdate him.
Leads: Kroll (2018), "The fallacy of inscrutability"; Miller (2019) on explanation (ref. 169); Raji et al. (2020), closing the AI accountability gap (ref. 209); Selbst et al. (2019), fairness and abstraction.

## Caution
A 2021 survey of principles documents; it predates large language model agents and says nothing about them. It sets requirements and a research agenda and reports no evidence on whether traceability works. Use arXiv v1 locators or check the ACM text before quoting by page.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The arXiv v1 PDF (arXiv:2101.09385v1, 15 pp., same title and author), extracted with pdftotext. I matched all 14 verbatim quotations word for word and checked each page and section locator, the five requirements in section 3, the tools in section 4, the policy documents in section 2, the 250-entry reference list, and refs 12, 85, 171 and 143.

**Findings:** No issues found. Locators (abstract p. 1; section 1 p. 2; section 3.1 p. 4; section 3.3 p. 5; section 3.5 p. 6; sections 4.3 and 4.5 pp. 7-8; section 5.0.2 and the closing quotation p. 9) match the arXiv pagination. The short quoted phrases that come from the author's essays and facet G are not Kroll's and were not checked against him.
