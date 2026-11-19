---
citekey: california2025transparency
title: "Senate Bill No. 53, Artificial intelligence models: large developers (Transparency in Frontier Artificial Intelligence Act), Stats. 2025, ch. 138"
authors: "{California Legislature}"
year: 2025
type: statute
doi: null
venue: California Statutes 2025, chapter 138 (approved by the Governor and filed 29 September 2025)
source_basis: full-text
pages_read: "whole chaptered text: legislative counsel's digest; SEC. 1 findings (a)-(n); Bus. & Prof. Code 22757.10-22757.16; Gov. Code 11546.8; Lab. Code 1107-1107.2"
source_url: https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N4/sb53/SB53_chaptered.txt
sha256: bc8263538d90eda1aea5fb25f550154103e6db6d06edad0bfb4600dacccfd39a
manuscript_lines: []
ledger_rows: [O02, E16]
premises: [A4, A8]
facet: N4
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
California's frontier-model statute. Copy: the chaptered version (BILL_VERSION_TBL_8965.lob, version 90 CHP) taken from the Legislature's official bulk download, `pubinfo_2025.zip`, by HTTP range request; the bill page on leginfo.legislature.ca.gov served a Cloudflare challenge, which I did not attempt to pass.

The Act's incident regime runs to the state. A frontier developer reports any "critical safety incident" to the Office of Emergency Services within 15 days, or within 24 hours to an appropriate authority where there is "an imminent risk of death or serious physical injury" (22757.13(c)). "Critical safety incident" is narrow: weight exfiltration causing death or injury, harm from a materialised catastrophic risk, loss of control causing death or injury, or deceptive subversion of the developer's own controls (22757.11(d)). Members of the public may file reports through the OES mechanism (22757.13(a)), which OES "may review" (22757.13(d)). The reports are exempt from the Public Records Act (22757.13(f)); OES publishes only "anonymized and aggregated" annual reports from 2027 (22757.13(g)). Enforcement is "a civil action brought only by the Attorney General", with penalties up to $1,000,000 per violation (22757.15). Nothing requires notice to persons harmed, and the Act gives them no action. Large developers must publish a frontier AI framework describing how they incorporate "national standards, international standards, and industry-consensus best practices" (22757.12(a)(1)), and comply with it on pain of penalty (22757.15(a)). Finding (l) records the legislature's view that voluntary frameworks did not suffice.

## Key facts it relies on
- 22757.11(d): "'Critical safety incident' means any of the following: (1) Unauthorized access to, modification of, or exfiltration of, the model weights of a frontier model that results in death or bodily injury. (2) Harm resulting from the materialization of a catastrophic risk. (3) Loss of control of a frontier model causing death or bodily injury. (4) A frontier model that uses deceptive techniques against the frontier developer to subvert the controls or monitoring of its frontier developer outside of the context of an evaluation designed to elicit this behavior and in a manner that demonstrates materially increased catastrophic risk."
- 22757.13(a): OES "shall establish a mechanism to be used by a frontier developer or a member of the public to report a critical safety incident".
- 22757.13(c)(1): "a frontier developer shall report any critical safety incident pertaining to one or more of its frontier models to the Office of Emergency Services within 15 days of discovering the critical safety incident." (c)(2): imminent risk of death or serious physical injury, disclosure "within 24 hours to an authority".
- 22757.13(d): OES "shall review critical safety incident reports submitted by frontier developers and may review reports submitted by members of the public."
- 22757.13(f): reports "are exempt from the California Public Records Act".
- 22757.13(g)(1): "Beginning January 1, 2027, and annually thereafter, the Office of Emergency Services shall produce a report with anonymized and aggregated information about critical safety incidents".
- 22757.12(a)(1): the framework describes how the developer approaches "Incorporating national standards, international standards, and industry-consensus best practices into its frontier AI framework."
- 22757.15(a)-(b): failure to report or "to comply with its own frontier AI framework" incurs "a civil penalty ... that does not exceed one million dollars ($1,000,000) per violation"; "A civil penalty described in this section shall be recovered in a civil action brought only by the Attorney General."
- SEC. 1(l): "While the major artificial intelligence developers have already voluntarily established the creation, use, and publication of frontier AI frameworks as an industry best practice, not all developers are providing reporting that is consistent and sufficient to ensure necessary transparency and protection of the public. Mandatory, standardized, and objective reporting by frontier developers is required".
- Lab. Code 1107.1: whistleblower protection for covered employees reporting to the Attorney General, a federal authority or persons with authority to correct the issue.

## Critical notes from the literature
- None read this round. The statute is the developer-side counterpart of AI Act Art 55(1)(c).

## Where the argument uses it
- A4, M9 (P20): holds. In the most specific frontier-AI incident statute, notice runs to government, the public's role is to file reports OES "may review", reports are shielded from public records requests, and only the Attorney General can sue. The affected person gets neither notice nor standing.
- A4, M2 (P6): complicates. California turns a developer's own framework, built from industry standards, into an enforceable promise (22757.15(a)). The binding party is the state, not the people acted on; the standard binds because the statute says so.
- Finding (l) is a legislature's own judgment that industry self-reporting fell short, usable against O02's premise that voluntary measures suffice.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
