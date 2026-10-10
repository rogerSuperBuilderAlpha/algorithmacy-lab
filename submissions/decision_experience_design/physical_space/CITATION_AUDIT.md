# Citation audit: Decision Experience Design in Physical Space

Audited text: `source_v3.txt`, with the same wording in `dxd-substack.md` and `dxd-substack.html`. The sentence-level record is `changes.md` (built 4 October 2026). The pre-fix paste is `source_original.txt`. This note does not add findings beyond those two files and the checks recorded in the change log.

The final essay has 67 reference entries. The change log's citation cross-check reports 67 in-text citations and 67 references, with no orphan on either side. Every DOI added in the repair resolves through doi.org. Several sentences were rewritten so the claim stays inside what the cited source reports.

## Summary

The pasted essay mixed three different failures.

1. Some references do not exist. The titles, journals, years, and article numbers were plausible, and in two cases the article number is a real number that belongs to a different paper.
2. Some references exist, but the title, journal, coauthors, pages, or DOI were wrong.
3. Some references exist and were described accurately enough to find, but the sentence attached to them is not what the source says. The sharpest case is the Conseil d'État ruling on Amazon France Logistique, which the original sentence reversed.

A second round of errors appeared while those problems were being fixed. That correction pass was drafted with AI help. It assigned Seamful XAI a DOI that belongs to a different paper, gave the electronic-shelf-label study an invented title and page range, cited New York's petting-zoo section, § 396-ff, for the cashless-store rule, and moved several claims onto real papers that do not support them. The change log refused those attachments. The replacements are the ones in `source_v3.txt`.

Roger Hunt approved four last edits on 4 October 2026: the casino sentence, the systematic-review citation, the friction-figure label, and the January 2026 Amazon Go and Amazon Fresh closure. Those are F1 through F4 in the change log.

What remains unchecked is listed at the end. It is a short list of sentences whose sources were not read at the grain of the claim, one working paper, and one unconfirmed session-law chapter number.

## How the problems were found

The repair rule in the change log was: no invented metadata. Each new source was checked by DOI resolution (doi.org content negotiation, which returns a CSL record) or by an official page, and the abstract or the page text was read against the sentence it was asked to support. Lookups also used Crossref, OpenAlex, publisher pages, and official statute and agency pages. A reference that could not be found in Crossref, OpenAlex, or the named journal was treated as absent.

Article numbers were checked as identifiers. Two of them resolved, and both resolved to someone else's paper:

| Cited as | The number actually belongs to |
| --- | --- |
| Gustafsson (2026), *Journal of Retailing and Consumer Services* 88, article 103712 | Hyun, Park, and Hong (2024), *Journal of Retailing and Consumer Services* 78. The article number is real. The author, year, volume, and title are not. |
| Pusceddu, Cabiddu, and Hurmelinna-Laukkanen (2025), *Journal of Business Research* 186, article 114981 | Mourali et al. (2025), "Post hoc explanations..." The article number is real. The author list and title are not. |

DOIs were checked the same way. A DOI that resolves is not yet a confirmation. It has to resolve to the title in the reference list. Three cases in this essay show why:

| DOI as used | What it resolves to |
| --- | --- |
| 10.1145/3637396 | Ehsan, Liao, Passi, Riedl, and Daumé III (2024), "Seamful XAI," *Proceedings of the ACM on Human-Computer Interaction* 8(CSCW1), Article 119. This is the paper the corrected essay cites. |
| 10.1145/3686950 | Not Seamful XAI. The correction pass attached this DOI to Seamful XAI. It is Errey et al., on narrative visualization. |
| 10.1080/01944363.2013.787329 | The original Pierce and Shoup DOI. The working DOI is 10.1080/01944363.2013.787307. |
| 10.4000/tc.4999 | Akrich. The DOI lands on the 2010 reprint in *Techniques & Culture* 54-55, pages 205-219. The essay cites the 1987 original and now says so. |

The v2 change log records that all 57 reference URLs and DOIs then on the list were requested. Every DOI resolved through doi.org content negotiation. Some publisher landing pages (Wiley, ACM, MDPI, SSRN, GAO) return 403 to scripts. The California legislative site timed out from the machine that ran the check. The Uber help URL returns 404 to curl and loads in a browser fetch. The SSRN page for Stamatopoulos, Sanders, and Bray (2025) blocks scripts, so that paper's claim was checked through the UC San Diego press release that reports the same study. v3 added the Amazon Staff page of 27 January 2026 and rechecked the four approved edits against their sources.

Each new source below was kept only for a sentence its abstract or text supports. The "Use" column is the sentence in the final essay.

| Source | Read against | What the source supplies |
| --- | --- | --- |
| Hazée et al. (2025), doi 10.1002/mar.22161 | Section 2, unstaffed stores | Reasons against adopting just-walk-out stores include privacy, payment unease, technology reliability, and customer-care inconvenience. |
| Schultz and Paetz (2025), doi 10.1016/j.jretconser.2025.104280 | Section 2, the same sentence | Data-privacy concerns lower satisfaction with cashierless systems and willingness to use them. |
| Reinders, Dabholkar, and Frambach (2008), doi 10.1177/1094670508324297 | Section 2 | Full service is increasingly replaced with technology-based self-service, sometimes with no other option. Forced use produces negative attitudes toward the technology and the provider. An employee fallback offsets those effects. |
| Shabnam et al. (2026), doi 10.1108/JSM-09-2025-0679 | Section 2 | The abstract identifies digitally enforced rules and says rigid rules intensify exclusion. It also says transparent algorithms enhance autonomy and trust, while opacity reduces control. It does not list signage, privacy notices, or screen layouts, and it does not say users cannot dispute rules. |
| Larivière et al. (2017), doi 10.1016/j.jbusres.2017.03.008 | Section 2, one clause | Technology can augment or substitute for frontline employees. Cited only as that framework. |
| Moradi, Levy, and Cheyre (2025), doi 10.1145/3711051 | Section 2 | Twenty-two cashier interviews. Self-checkout work became more focused on problems, monitoring, and policing. |
| Ehsan et al. (2024), doi 10.1145/3637396 | Section 4 | Explainable AI has predominantly tackled algorithmic opacity. Hiding seams risks disempowering users who need to mitigate the fallout of AI mistakes. The author PDF confirms Article 119. |
| Uber help, wait-time fees | Section 5.1 | UberX riders are charged a per-minute wait fee if they do not enter the vehicle within 2 minutes of the driver's arrival. Black is 5 minutes. The threshold varies by product and location. |
| Lee, Kusbit, Metsky, and Dabbish (2015), doi 10.1145/2702123.2702548 | Section 5.1 | Drivers have trouble anticipating fast-changing surge pricing and opaque assignment. The paper does not study unannounced software builds. |
| Gambler (2022), GAO-22-106154 | Section 5.2 | Testimony of 27 July 2022. CBP privacy notices were not always current or complete, or were unavailable, and opt-out information was limited. Opt-out is described as policy. |
| Buolamwini, Raman, and Dean (2025), Algorithmic Justice League, "Comply to fly?" | Sections 5.2 and 7.1 | Survey of 420 travelers at 91 airports, at TSA checkpoints. 82 scanned before they could opt out, 56 discouraged or coerced, 36 refused, 49 feared consequences, and a few believed they were sent to secondary screening. |
| Cheon and Erickson (2025), doi 10.1145/3757409 | Section 5.3 | Imposed productivity rates. |
| U.S. Senate HELP Committee (2024), majority staff report | Section 5.3 | Rates vary by facility and position. |
| Cal. Lab. Code §§ 2100-2112; N.Y. Lab. Law §§ 780-788 | Section 5.3 | Both statutes regulate quotas. Both require written quota descriptions and restrict quotas that penalize rest breaks, including bathroom breaks. |
| Conseil d'État, No. 492830 (23 December 2025) | Section 5.3 | Holding summarized in the section below. Official page and the Juricaf copy. |
| Mass. Gen. Laws ch. 255D, § 10A; N.Y.C. Admin. Code § 20-840; N.Y. Gen. Bus. Law § 396-ii | Section 5.7 | Cash-acceptance mandates. Statute text and, for New York, the bill page (S4153A) and the Attorney General's effective-date notice. |
| Stamatopoulos, Bassamboo, and Moreno (2021), doi 10.1287/mnsc.2019.3551 | Section 5.8 | Electronic shelf labels cut the labor and material costs of price adjustment. More and smaller price changes occurred, mostly decreases. |
| Stamatopoulos, Sanders, and Bray (2025), doi 10.2139/ssrn.5271491 | Section 5.8 | No meaningful rise in short-lived price spikes after shelf-label installation. Working paper. Content checked via the UC San Diego release (114 stores, 180 million observations). |
| N.Y. Gen. Bus. Law § 349-a | Section 5.8 | Disclosure when a price shown to a New York consumer was set by an algorithm using that consumer's personal data. In effect 10 November 2025. Online or offline. |
| Rosenberger (2017), *Callous Objects*, University of Minnesota Press | Section 5.9 | The press page for the book on design against the homeless. |
| Gregory (2021), doi 10.1177/0950017020969593 | Section 6 | Interviews with 25 couriers in Edinburgh. Physical risk and bodily harm under algorithmically managed delivery work. |
| Zheng et al. (2019), doi 10.1177/0361198119841028 | Section 6 | 824 delivery riders. Time pressure is linked to crash involvement through fatigue and risky riding. |
| Benoit, Altrichter, Grewal, and Ahlbom (2024), doi 10.1016/j.jretai.2023.12.003 | Section 7.3 | In autonomous stores, limited access to staff and the inability to verify the basket before payment deter patronage. |
| Palmer (2024), CNBC, 3 April 2024 | Section 7.3 | Amazon removed Just Walk Out from its U.S. Fresh stores. A spokesperson said customers wanted to view their receipt as they shopped. |
| Kumar (2024), About Amazon, 17 April 2024 | Section 7.3 | In larger grocery stores, customers so far preferred Amazon Dash Cart, with a running tally and spending tracked in real time. |
| Amazon Staff (2026), About Amazon, 27 January 2026 | Section 7.3 | Amazon announced it would close Amazon Go and Amazon Fresh physical stores and convert some locations to Whole Foods Market. Page metadata datePublished 2026-01-27T14:55Z. Same-day CNBC and Reuters reports corroborate the announcement. |
| Schüll (2012), *Limn* | Section 5.5 | Casinos switch game configuration (theme, denomination, payout rate) in real time from tracked touch-point data, to match emerging player preference groups. No biometric data in the essay. |
| Mele, Russo Spena, Marzullo, and Di Bernardo (2023), doi 10.1007/s43039-023-00070-7 | Section 2, first paragraph | The systematic review. Empirical studies use "phygital" without an operational consensus. |
| Johnson and Barlow (2021), doi 10.3390/jtaer16060130 | Section 2 | Reduced "pain of payment," together with product attachment, can increase sales. The paper is a literature-based theoretical article. The finding used here is reduced pain of payment. The systematic-review citation and the unstaffed-store surveillance sentence were moved to other sources. |
| Padigar, Li, and Manjunath (2025), doi 10.1002/mar.22111 | Section 2 and the friction figure | Some customer effort creates value, and eliminating that constructive friction can hinder value creation. The figure's stronger wording is marked "after" this paper. |

## Fully fabricated references

These entries were removed. Nothing in Crossref, OpenAlex, or the named journal matches them. Where a real article number was reused, the real paper was identified and was not substituted under the fake authors' names.

| As printed in `source_original.txt` | What the lookup found | What the final text uses instead |
| --- | --- | --- |
| Lee, H., and Kim, Y. (2026). "Coercive service design: The withdrawal of human-staffed retail alternatives." *Service Industries Journal*, 46(2), 112-131. | No such article. | Reinders, Dabholkar, and Frambach (2008) on forced technology-based self-service. |
| Gustafsson, E. (2026). "Anxiety and surveillance in unstaffed automated retail environments." *Journal of Retailing and Consumer Services*, 88, 103712. | No such article. Article 103712 is Hyun, Park, and Hong (2024) in volume 78 of the same journal. | Hazée et al. (2025) and Schultz and Paetz (2025) for shopper apprehension. Moradi, Levy, and Cheyre (2025) for the cashier's changed job. |
| Mulcahy, R., Russell-Bennett, R., and Zainuddin, N. (2026). "The dyadic service encounter under automated mediation." *Journal of Retailing*, 102(1), 45-61. | The authors are real. This paper is not. | Moradi, Levy, and Cheyre (2025). |
| Pusceddu, G., Cabiddu, F., and Hurmelinna-Laukkanen, P. (2025). "Reintroducing human slowness in automated service encounters." *Journal of Business Research*, 186, 114981. | No such article. Article 114981 in that volume is Mourali et al. (2025), "Post hoc explanations..." | Reinders et al. (2008) for the human fallback. Moradi et al. (2025) for monitoring and policing at self-checkout. |
| Rosenberger, R. (2023). *On hostile design: The political philosophy of urban deterrence.* University of Minnesota Press. | No such book. Rosenberger's 2020 *Urban Studies* article is titled "On hostile design: Theoretical and empirical prospects." His University of Minnesota Press book on this subject is *Callous Objects* (2017). | Rosenberger (2017), *Callous Objects*. |
| Ehsan, U., Wintersberger, P., Liao, Q. V., Mara, M., Streit, M., and Riener, A. (2024). "Operationalizing explainable AI in physical interaction spaces." *ACM Transactions on Computer-Human Interaction*, 31(2), 1-34. | That paper does not exist. | Ehsan, Liao, Passi, Riedl, and Daumé III (2024), "Seamful XAI: Operationalizing seamful design in explainable AI," *Proceedings of the ACM on Human-Computer Interaction*, 8(CSCW1), Article 119, 1-29, doi 10.1145/3637396. |

The Ehsan line is the pattern in miniature. Real researchers, a real journal, a topical title, and no article. The replacement is a real Ehsan paper whose abstract matches a narrower sentence: explainable-AI research has predominantly tackled algorithmic opacity, and seamful-XAI researchers argue that hiding system seams disempowers users who need to mitigate the fallout of AI mistakes. The original sentence said the literature "routinely reduces system transparency to informational text boxes and advisory dashboards." Seamful XAI does not say that, so the sentence was rewritten.

The correction pass then gave Seamful XAI the DOI 10.1145/3686950. That DOI is Errey et al. on narrative visualization. The DOI in the final reference list is 10.1145/3637396.

## Real works with wrong metadata

These works exist. The original reference list gave them the wrong title, venue, coauthors, issue, pages, or DOI. The final list uses the record below. Verifying URLs are the ones in `changes.md`.

| Work | As printed | Corrected record |
| --- | --- | --- |
| Johnson and Barlow (2021) | "The phygital advantage: Frictionless commerce and consumer spending." *Journal of Consumer Marketing*, 38(6), 612-622. | "Defining the phygital marketing advantage." *Journal of Theoretical and Applied Electronic Commerce Research*, 16(6), 2365-2385. doi 10.3390/jtaer16060130. |
| Padigar, Li, and Manjunath (2025) | Padigar, M., Li, S., and Manjunath, A. "Constructive friction in algorithmic commerce." *Harvard Business Review on Technology*, 41(1), 88-97. | Padigar, M., Li, Y., and Manjunath, C. N. "'Good' and 'bad' frictions in customer experience: Conceptual foundations and implications." *Psychology & Marketing*, 42(1), 21-43. doi 10.1002/mar.22111. *Harvard Business Review on Technology* is not a venue. |
| Mele and Russo-Spena (2025) | "The agency of smart artifacts in phygital service ecosystems." *Journal of Service Research*, 28(2), 215-232. | "Agencement of onlife and phygital: Smart tech–enabled value co-creation practices." *Journal of Service Management*, 36(2), 217-240. doi 10.1108/JOSM-03-2023-0113. The abstract still supports the section 2 sentences on onlife agency and phygital materiality. |
| Stamatopoulos et al. (2021) | Stamatopoulos, Tan, and Zervas. "Dynamic pricing with electronic shelf labels: Operational evidence from retail grocery." *Management Science*, 67(8), 4912-4934. | Stamatopoulos, Bassamboo, and Moreno. "The effects of menu costs on retail performance: Evidence from adoption of the electronic shelf label technology." *Management Science*, 67(1), 242-256. doi 10.1287/mnsc.2019.3551. There is no Tan and Zervas article at 67(8). |
| Pierce and Shoup (2013) | DOI 10.1080/01944363.2013.787329. Title, journal, volume, and pages were already right. | DOI 10.1080/01944363.2013.787307. |
| Kitchin and Dodge (2009) | Pages 58-78. | Pages 96-114, from the author's publication list. |
| Petty (2016) | "...urban architecture and the question of 'hostile design'." | "...urban securitisation and the question of 'hostile architecture'." Journal, volume, issue, and pages were already right. doi 10.5204/ijcjsd.v5i1.286. |
| Akrich (1987) | Cited as *Techniques & Culture*, 9, 49-64, with doi 10.4000/tc.4999. | The 1987 original is *Techniques et Culture*, 9, 49-64. The DOI points at the 2010 reprint, *Techniques & Culture*, 54-55, 205-219. The entry now cites the 1987 original, notes the reprint, and keeps the DOI. |
| Gambler (2022) | A GAO report number with no document type and no date. | GAO testimony, 27 July 2022, GAO-22-106154. https://www.gao.gov/products/gao-22-106154. |
| Weiser (1994) | "Building invisible interfaces (Invited talk slides)." No date. | Keynote presentation slides, 2 November 1994, UIST '94. Crossref lists the keynote abstract as "Creating the invisible interface," doi 10.1145/192426.192428. The essay cites the slides under the title "Building invisible interfaces" and does not attach that DOI. |
| Shabnam et al. (2026) | *Journal of Services Marketing*, pages 1-17. | Advance online publication. No volume or issue yet. doi 10.1108/JSM-09-2025-0679. |
| Cheon and Erickson (2025) | "CSCW228:1-30." | Article CSCW228, 1-30. doi 10.1145/3757409. |
| Moradi, Levy, and Cheyre (2025) | Not in the original list. | *Proceedings of the ACM on Human-Computer Interaction*, 9(2), Article CSCW153, 1-21. doi 10.1145/3711051. The article number is taken from the ACM reference block on arXiv 2410.02888. Crossref has no article number for it. |
| Floridi (2015) | Book citation, no DOI. | DOI 10.1007/978-3-319-04093-6 added. The book is open access. |
| Gutelius and Theodore (2019) | UC Berkeley Center for Labor Research and Education only. | Co-publisher Working Partnerships USA, and the Labor Center URL, added. |
| CBP (2018) and TSA (2026) | "Customs and Border Protection" and an undated TSA entry. | Group author "U.S. Customs and Border Protection," 14 November 2018, DHS/CBP/PIA-056. TSA entry dated 16 January 2026, PIA-046(e) update, with the DHS URL. Abbreviations are defined at first citation. |
| FTC (2024, 2025) | Undated press release and an undated staff report. | 23 July 2024 press release. January 2025 staff perspective, full title, URLs. Abbreviation defined at first citation. |
| U.S. Senate HELP Committee (2024) | "Staff Report. Chairman Bernard Sanders." In-text shorthand "U.S. Senate HELP Committee." | "Majority staff report," URL added. The in-text name is now "U.S. Senate Committee on Health, Education, Labor, and Pensions," matching the reference entry. |
| Warren and Casey (2024) | Undated letter "regarding electronic shelving labels and dynamic pricing." | 5 August 2024. The descriptive title now matches the letter, which is about price gouging. The letter does mention weather-based surges and facial-recognition shelves, so section 5.8's use of it stands. "Jr." is restored on Casey. |
| Schüll (2012) | *Limn*, 2, no URL. | Limn URL added. |
| Conseil d'État (2025) | Decision number, no URL, date only in a trailing note. | Date 23 December 2025 and the official ArianeWeb URL. The description of the holding was also wrong. See below. |
| California (2021), New York State (2022), New York State (2025) | Informal author-date names. | Cal. Lab. Code §§ 2100-2112 (2021; effective 1 January 2022). N.Y. Lab. Law §§ 780-788 (2022; effective 19 June 2023). N.Y. Gen. Bus. Law § 349-a (2025; effective 10 November 2025). The code heading of § 349-a is "Pricing." "Algorithmic Pricing Disclosure Act" is the popular name used by the New York Attorney General. |

The Stamatopoulos row has a second, later error. The correction pass retitled the 2021 paper "Dynamic pricing with electronic shelf labels: An empirical investigation" and gave it pages 297-315. That title and those pages are invented. The *Management Science* article is the Bassamboo and Moreno paper in volume 67, issue 1, pages 242-256.

## Real sources that did not support the claims attached to them

A resolvable paper can still be the wrong paper for the sentence. Two layers of this problem are in the file. The original paste attached real or partly real sources to claims they do not make. The correction pass then moved some of those claims onto a different set of real sources that also do not make them. The final text drops both attachments.

### In the original paste

| Citation | Sentence it was holding up | What the source supports | Final disposition |
| --- | --- | --- | --- |
| Johnson and Barlow (2021) | Automated checkouts and sensor-driven access "encourag[e] impulse expenditures by detaching consumption from conscious financial evaluation." | Reduced pain of payment, plus product attachment, can increase sales. No impulse-buying claim. | Sentence rewritten to "raising expenditures by reducing the felt 'pain of payment'." |
| Padigar et al. (2025) | Removing friction "compromises consumer autonomy." Frictionless payment causes involuntary spending and lets software "steer users toward unfavorable financial commitments." | Eliminating constructive friction can hinder value creation. The autonomy, involuntary-spending, and steering claims are not in the paper. | Those three claims were removed. |
| Shabnam et al. (2026) | Computational environments "enforce algorithmic rules that users cannot dispute or modify." Later, the remedy is "posting instructional signage, publishing privacy notifications, and updating screen layouts," and the field proposes solutions "rooted strictly" in that. | Digitally enforced rules; rigid rules intensify exclusion; transparent algorithms enhance autonomy and trust, while opacity reduces control. The abstract does not say users cannot dispute rules, and it does not list signage, privacy notices, or screen layouts. The paper also discusses adaptive governance, so "strictly" does not fit. | Both sentences narrowed to the abstract. |
| Ehsan et al. (2024), the nonexistent TOCHI paper, and then Seamful XAI | Transparency reduced to "informational text boxes and advisory dashboards." | Seamful XAI: the field has predominantly tackled algorithmic opacity, and hiding seams disempowers users. Nothing about text boxes or dashboards. | Sentence rewritten to the abstract. |
| Cameron (2024); Rosenblat and Stark (2016) | The passenger "incurs fees for failing to reach the pickup coordinate within three minutes." | Neither paper supports a three-minute passenger threshold. | Uber's help page: UberX wait fee after two minutes. Citation added. |
| Lee et al. (2015) | Dispatch algorithms, surge factors, and incentives "drift continuously across unannounced software builds." | Drivers cannot anticipate fast-changing surge pricing and opaque assignment. | "Shift quickly and unpredictably from the driver's vantage point." |
| Gambler (2022), called a statute | "Federal statutory rules permit" citizens to opt out, but "mandated notification signage remains obscure, missing, or obscured." | GAO testimony: privacy notices often incomplete, outdated, or unavailable, and opt-out information limited. Opt-out is a CBP policy. The GAO testimony does not call it a statute. | "Federal policy permits..." and the auditor's finding, in the auditor's terms. |
| DHS (2025), FR Doc. 2025-19655, 90 FR 48604 | Travelers who opt out "routinely encounter threats of denied boarding, severe delays, or punitive secondary interrogations by border guards." Repeated in section 7.1 as interrogations, delays, or exclusion. | The final rule extends biometric entry-exit collection to noncitizens. It does not describe threats to travelers who opt out. | Entry removed. Opt-out experience is now Buolamwini, Raman, and Dean (2025). "Denied boarding," "border guards," and "interrogations" were dropped. The survey supports being scanned before one can decline, being discouraged or refused by officers, and fearing secondary screening. |
| Cheon and Erickson (2025); HELP Committee (2024) | Picking quotas "fluctuate dynamically based on seasonal logistics velocity and opaque software revisions." | Rates vary by facility and position (HELP). Cheon and Erickson describe imposed productivity rates. | Sentence rewritten to those two findings. |
| Conseil d'État (2025) | The court ruled that scanner metrics violate EU privacy law. | The court held the opposite on that point. See the next section. | Section 5.3 rewritten. |
| Schüll (2012) | Slot platforms modify payout pacing, visuals, and volatility from "real-time biometric and behavioral data," read as per-individual tailoring. | Real-time reconfiguration from touch-point data and heat maps, for emerging player preference groups: theme, denomination, payout rate. No biometrics. Adjustments are for groups. | "Real-time player-tracking data." Roger approved this edit. The comparison-table row already said "YES (Real-Time Difficulty)" and did not say biometric or per-individual, so `dxd-comparison-table.png` is unchanged. |
| Stamatopoulos et al. (2021), under the wrong coauthors | Retailers install electronic shelf labels "to implement scheduled price adjustments across entire store inventories." | Labels cut labor and material costs of changing prices. Adoption produces more frequent, smaller price changes, most of them decreases. | Sentence rewritten to that abstract. The 2025 working paper was added for the separate claim that short-lived price spikes did not rise. |
| N.Y. Gen. Bus. Law § 349-a, cited as "New York State, 2025" | The state requires disclosures "whenever in-store prices rely on personal data algorithms," and the statute was grouped with expressions of concern about surveillance pricing. | The statute covers any personalized algorithmic price displayed to a New York consumer, online or offline. It is a disclosure law. | Scope corrected. Dropped from the "concern" citation. Legal form used in the text. |

Johnson and Barlow were also grouped with Mele et al. (2023) under "Systematic reviews indicate." Johnson and Barlow (2021) is a literature-based theoretical paper. The final sentence cites only Mele et al. (2023), and "reviews" became "review." Johnson and Barlow stay on the three sentences the change log says they support: the import of the word "phygital," the pain-of-payment sentence, and the sentence on single-user perceptions of brand consistency and convenience.

The friction figure labeled a row "(Padigar et al., 2025)" on wording that goes beyond the paper: preserves human dignity, prevents automated steering, and exposes authority. The label is now "(after Padigar et al., 2025)."

### Introduced during the correction pass

The change log's opening note records that an intermediate revision, drafted with AI help, was not in the editor's context. Where that revision had leaned on the sources below, the published text was corrected with the replacements in this audit instead. The misplaced sources are:

| Source the correction pass used | Claim it was given | Why it does not hold the claim | Replacement in the final text |
| --- | --- | --- | --- |
| Wood, Graham, Lehdonvirta, and Hjorth (2019), *Work, Employment and Society*, 33(1), 56-75 | Sections 5.1 and 5.3, drivers and warehouses. | The paper studies remote online freelancers in Southeast Asia and Sub-Saharan Africa. It does not study drivers or warehouses. The original body never cites it. It is an orphan in the original reference list. | Removed. Gregory (2021) and Zheng et al. (2019) cover physical risk under algorithmic time pressure for couriers and delivery riders. Wood would support claims about remote workers' overwork, sleep deprivation, and exhaustion. This essay has no such sentence. |
| Larivière et al. (2017) | "Service research fails to analyze the triad." Frontline workers "demoted to hardware custodians." | The paper proposes the Service Encounter 2.0 framework of technology, employees, and customers. It does not say the field has failed to analyze the triad. It does not describe workers as hardware custodians. | Kept for one clause only: service research frames technology as able to augment or substitute for frontline employees. The custodian claim is now Moradi et al. (2025): self-checkout recasts cashiers as monitors who troubleshoot machine problems and police customers. |
| Johnson and Barlow (2021), again | Unstaffed-store surveillance anxiety. | The paper is about reduced pain of payment. | Hazée et al. (2025) and Schultz and Paetz (2025): privacy, payment, reliability, and data-privacy concerns in just-walk-out and cashierless stores. |
| Reinders, Frambach, and Kleijnen (2015), *European Journal of Marketing*, 49(1/2), 190-211, doi 10.1108/EJM-12-2012-0735 | Consumer reactance. | The paper is real. The change log judges that it supports reactance only weakly, so it was not added. | Reinders, Dabholkar, and Frambach (2008), *Journal of Service Research*: forced self-service, negative attitudes, and an employee fallback. |

Wilson-Nash was paired with Johnson and Barlow in that same revision for the surveillance-anxiety point. The final section 2 sentence on camera-based surveillance cites Hazée et al. and Schultz and Paetz. Wilson-Nash remains cited for digital technology captivity, which the change log says the paper does support. The food-exclusion example attached to Wilson-Nash was not checked against the full text. See "What remains open."

## Wrong legal citations

The cashless-store statute is the clearest identifier error, and it happened in the correction pass.

New York General Business Law § 396-ff concerns petting zoos. The cashless-store law is § 396-ii, "Cashless policies prohibited" (S4153A / A7929, signed 2025, effective 21 March 2026). The final essay cites § 396-ii. The session-law chapter number was not confirmed, so it is omitted. The effective date is the one in the New York Attorney General's notice of the new law.

Other legal repairs:

| Original treatment | Problem | Final citation |
| --- | --- | --- |
| Section 5.7 stated the Massachusetts and New York cash mandates with no citation. | The statutes exist. They were not cited. | Mass. Gen. Laws ch. 255D, § 10A (1978): retailers may not discriminate against a cash buyer. N.Y.C. Admin. Code § 20-840, Local Law 34 of 2020. N.Y. Gen. Bus. Law § 396-ii (2025). |
| Section 5.3 said performance algorithms are prohibited from penalizing bathroom breaks, with no statute citation. | Both statutes regulate quotas. The change log records that they do not regulate "performance algorithms" as a named object. | Cal. Lab. Code §§ 2100-2112 (2021) and N.Y. Lab. Law §§ 780-788 (2022), cited for written quota descriptions and for quotas that penalize bathroom breaks. |
| Section 5.8 treated § 349-a as an in-store concern, grouped with the FTC and the Warren and Casey letter. | The section is a disclosure duty. It covers any seller, and any price set by an algorithm using the consumer's personal data, online or offline. In effect 10 November 2025. | N.Y. Gen. Bus. Law § 349-a (2025), in its own sentence. The FTC and the Warren and Casey letter stay on the concern sentence. |
| Section 5.2 called the biometric opt-out a federal statutory rule. | GAO-22-106154 describes a CBP policy and faulty notices. | "Federal policy," cited to Gambler (2022). The traveler-experience claims are cited to Buolamwini et al. (2025). |
| "California, 2021," "New York State, 2022," "FTC, 2025" in section 8. | The in-text names did not match the reference entries. | Cal. Lab. Code §§ 2100-2112 (2021); FTC (2025); N.Y. Lab. Law §§ 780-788 (2022). |
| "CBP, 2018; TSA, 2026" and "FTC, 2024, 2025" at first mention. | Group-author abbreviations were used before they were defined. | U.S. Customs and Border Protection [CBP]; Transportation Security Administration [TSA]; Federal Trade Commission [FTC], at first citation. |

DHS (2025) is a real final rule and a wrong legal citation for the sentences that used it. It is covered above with the unsupported sources. It is not in the final reference list.

## A substantive misreading: Conseil d'État, No. 492830

The original section 5.3 said that regulatory authorities in France reduced a corporate fine while ruling that continuous real-time scanner metrics violate European privacy law, by turning ordinary physical movements into permanent disciplinary evidence.

The decision is Conseil d'État, 23 December 2025, No. 492830, *Société Amazon France Logistique*, 10e et 9e chambres réunies. The change log reads the holding as follows. The court annulled the CNIL's finding that the "stow machine gun," "idle time," and "temps de latence" indicators lacked a legal basis under Article 6 of the GDPR. It held that the scanner productivity indicators themselves had a lawful basis. It upheld the finding that retaining every worker's scanner data for 31 days breached the data-minimisation principle in Article 5, and it left standing information and security breaches that were not contested. It cut the fine from €32 million to €15 million.

The original sentence reversed the central point. The indicators were not held unlawful. The excessive retention was. Section 5.3 now says that, and only that: the court cut the fine from €32 million to €15 million, held that the scanner productivity indicators had a lawful basis, and upheld the finding that the 31-day retention breached data minimisation.

Verified at the Conseil d'État decision page (https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-12-23/492830) and the Juricaf copy (https://juricaf.org/arret/FRANCE-CONSEILDETAT-20251223-492830).

## Uncited claims that were filled

Two passages stated legal or corporate facts with no citation. Both now end on sources that were read for those facts.

**Section 5.7, cash mandates.** The sentence said Massachusetts and New York had required stores to accept cash, so that a digital credential could not be the price of entering a shop. That is now cited to Mass. Gen. Laws ch. 255D, § 10A (1978), N.Y. Gen. Bus. Law § 396-ii (2025, effective 21 March 2026), and N.Y.C. Admin. Code § 20-840 (Local Law 34 of 2020).

**Section 7.3, visible checkout.** The paragraph said shoppers rejected invisible ceiling-camera billing and preferred cart-mounted terminals that show a running tally. It had no citation, and "shoppers rejected" was stronger than the reporting. The final paragraph cites three sources for three narrower facts. Benoit et al. (2024): in autonomous stores, limited staff access and the inability to verify the basket before payment deter patronage. Palmer (2024): Amazon removed Just Walk Out from U.S. Fresh stores after customers said they wanted to view their receipt as they shopped. Kumar (2024): in larger grocery stores the company reported that shoppers so far preferred Dash Cart, which shows a running tally and tracks spending in real time. A further sentence, approved by Roger, adds the 27 January 2026 announcement that Amazon would close its Amazon Go and Amazon Fresh stores and convert some of them to Whole Foods Market (Amazon Staff, 2026).

Three other bare or weakly supported claims picked up citations in the same pass. The two-minute UberX wait fee is cited to Uber's help page (section 5.1). The quota statutes are cited in section 5.3. Section 6's claim that delivery drivers risk collisions to beat the clock is no longer left to Cameron (2024), who studies ride-hail consent. It is cited to Zheng et al. (2019) and Gregory (2021), alongside Cameron and Wilson-Nash.

## Wording softened to match the evidence

Where a source was real but the verb was too strong, the sentence was cut back to the finding. The change log's rule for these paragraphs was claim-first sentences with the citation at the end, and no em-dash in the modified paragraphs. The only em-dash added anywhere in the essay is inside the official title of Hazée et al. (2025). In the HTML and Markdown, the modified friction figure uses a colon where the earlier figures use an em-dash.

| Place | Original wording | Final wording | Why |
| --- | --- | --- | --- |
| §2, friction | Impulse expenditures, consumption detached from conscious financial evaluation. | Expenditures rise because the felt pain of payment falls. | Johnson and Barlow (2021). |
| §2, constructive friction | Removing friction compromises autonomy, causes involuntary spending, and lets software steer users. Pauses "preserve relational trust and consumer agency." | Some customer effort creates value. Unstaffed just-walk-out stores raise apprehension about privacy, payment, and reliability, and the encounter becomes camera-based surveillance. An employee fallback offsets the harm of forced self-service. | Padigar et al. (2025); Hazée et al. (2025); Schultz and Paetz (2025); Reinders et al. (2008). The pause-preserves-trust claim is gone. |
| §2, structural problems | "Coercive service design" eliminates staffed checkout. Users cannot dispute or modify rules. Retail automation erases employees or demotes them to "diagnostic monitors charged with maintaining sensor machinery." | Forced self-service, sometimes with no other option, breeds negative attitudes. Rigid digitally enforced rules intensify exclusion. Technology can augment or substitute for employees, and self-checkout recasts cashiers as monitors who troubleshoot and police. | Reinders et al. (2008); Shabnam et al. (2026); Larivière et al. (2017); Moradi et al. (2025). "Erase service employees entirely" and "maintaining sensor machinery" were dropped. |
| §2, legibility | The remedy is strictly signage, privacy notices, and screen layouts. | The field often locates the remedy in legibility: transparent algorithms enhance autonomy and trust, while opacity reduces control. | Shabnam et al. (2026) abstract. |
| §2, opening | "Systematic reviews indicate," citing Johnson and Barlow with Mele et al. | "A systematic review indicates," citing only Mele et al. (2023). | Johnson and Barlow are not a systematic review. Approved edit. |
| §4 | Text boxes and advisory dashboards. | The field has predominantly tackled algorithmic opacity, and hiding seams disempowers users. | Seamful XAI abstract. |
| §5.1, fee | Three minutes, cited to Cameron and to Rosenblat and Stark. | An UberX passenger incurs per-minute wait fees after two minutes. | Uber help page. |
| §5.1, drift | Unannounced software builds. | Shift quickly and unpredictably from the driver's vantage point. | Lee et al. (2015). |
| §5.2 | Statutory opt-out; signage "obscure, missing, or obscured"; denied boarding; border guards; punitive secondary interrogations. | Policy opt-out; notices incomplete, outdated, or unavailable; scanned before one can decline; discouraged or refused; fear of secondary screening. | Gambler (2022); Buolamwini et al. (2025). |
| §5.3, quotas | Seasonal velocity and opaque software revisions. | Quotas vary by facility and position and are imposed rather than negotiated. | HELP report; Cheon and Erickson (2025). |
| §5.3, France | Scanner metrics violate EU privacy law and become permanent disciplinary evidence; the fine was merely reduced. | Lawful basis for the indicators; 31-day retention breached data minimisation; fine cut from €32 million to €15 million. | Conseil d'État, No. 492830. |
| §5.5 | Real-time biometric and behavioral data. | Real-time player-tracking data. | Schüll (2012). Approved edit. |
| §5.8 | Scheduled price adjustments across entire inventories. A New York statute aimed at in-store algorithmic prices, cited as concern. | More frequent, smaller price changes, most of them decreases. No meaningful rise in short-lived spikes in the 2025 working-paper data. Disclosure beside any personalized algorithmic price. | Stamatopoulos, Bassamboo, and Moreno (2021); Stamatopoulos, Sanders, and Bray (2025); § 349-a. |
| §7.1 | Interrogations, delays, or exclusion, cited in part to DHS (2025). | Officer pressure, delays, or exclusion, cited to Buolamwini et al. (2025), Gambler (2022), and Wilson-Nash et al. (2026). | DHS does not document opt-out costs. The survey documents officer discouragement and refusal, and some secondary screening. |
| §7.3 | Consumers reject invisible tracking. Corporations retreated after shoppers rejected invisible billing. | Consumers resist invisible billing. Limited staff access and the inability to verify the basket deter patronage. Amazon removed Just Walk Out from U.S. Fresh after customers asked to see the receipt while shopping, and reported a preference for Dash Cart's running tally. | Benoit et al. (2024); Palmer (2024); Kumar (2024). |
| Friction figure | "(Padigar et al., 2025)" on a row that outruns the paper. | "(after Padigar et al., 2025)." | Approved edit. |

## Removals

References removed from the list:

| Removed | Why it left |
| --- | --- |
| Gustafsson (2026) | No such article. The article number belongs to Hyun, Park, and Hong (2024). |
| Lee and Kim (2026) | No such article. |
| Mulcahy, Russell-Bennett, and Zainuddin (2026) | No such article. The authors publish in this area. This title does not. |
| Pusceddu, Cabiddu, and Hurmelinna-Laukkanen (2025) | No such article. The article number belongs to Mourali et al. (2025). |
| Rosenberger (2023), *On hostile design* | No such book. Replaced by *Callous Objects* (2017). |
| Ehsan, Wintersberger, Liao, Mara, Streit, and Riener (2024), TOCHI | No such article. Replaced by Seamful XAI, different authors, different venue. |
| Department of Homeland Security (2025), FR Doc. 2025-19655 | Real rule on biometric entry and exit for noncitizens. It supported neither sentence that cited it. |
| Wood, Graham, Lehdonvirta, and Hjorth (2019) | Real paper on remote online gig work. Present in the original reference list, never cited in the original body, and unfit for the driver and warehouse sentences a later pass tried to hang on it. |

Reinders, Frambach, and Kleijnen (2015) was considered and not added. It is real, and the reactance use was too weak.

Claims removed because no retained source makes them:

- Impulse buying, and consumption detached from conscious financial evaluation.
- Frictionless payment as a cause of involuntary spending and automated steering toward unfavorable commitments.
- Intentional pauses as a preservation of relational trust.
- Users' inability to dispute or modify algorithmic rules, as a finding of Shabnam et al.
- Signage, privacy notifications, and screen layouts as the field's stated remedy.
- Erasure of service employees, and cashiers reduced to people who maintain sensor machinery.
- A three-minute passenger threshold at the curb.
- Unannounced software builds as the mechanism of surge and dispatch change.
- Denied boarding, border-guard interrogation, and punitive secondary screening as documented opt-out consequences.
- Seasonal logistics velocity and opaque software revisions as the account of picking quotas.
- The holding that Amazon France Logistique's scanner indicators violate EU privacy law.
- Biometric data as the input to the casino-floor reconfiguration Schüll describes.
- "Shoppers rejected invisible billing systems," as stronger than the Amazon and CNBC reporting.
- Johnson and Barlow as a systematic review.

## What remains open

v3 closed four items the v2 log had flagged and left alone: the casino biometrics (F1), the systematic-review citation (F2), the friction-figure attribution (F3), and the January 2026 store closures (F4). The comparison-table image did not need a new render.

Still only partly checked, and left as written:

| Item | What is unsettled |
| --- | --- |
| Hollands et al. (2017) | Cited for the cafeteria that collects no individual data, and for the TIPPME typology's exclusion of systems that tailor options to specific individuals. The paywalled full text was not checked against that exclusion wording. |
| Suchman (1985), Xerox report ISL-6 | The report exists. The essay's detail about paper-release doors and manual abort controls was not checked against the report text. The change log calls that detail interpretive. |
| Section 5.2, "passenger risk scores," cited to Adey (2004) and TSA (2026) | The TSA privacy impact assessment describes gallery pre-staging and matching. It was not re-verified sentence by sentence against "risk scores." |
| Wilson-Nash et al. (2026) | Supports digital technology captivity. The specific example of exclusion from purchasing food was not checked against the full text. |
| Batat (2024) and Johnson and Barlow (2021) | The section 2 sentence that the ideal customer journey "removes conscious cognitive deliberation" was not checked at sentence level. |
| Lee et al. (2015) and Rosenblat and Stark (2016) | Not re-read in full. The section 5.1 wording was softened on the basis of what had been checked. |
| Stamatopoulos, Sanders, and Bray (2025) | SSRN working paper, doi 10.2139/ssrn.5271491. Not peer-reviewed. The "no meaningful rise in short-lived price spikes" claim was verified through the UC San Diego release because SSRN blocked the script. |
| N.Y. Gen. Bus. Law § 396-ii | The session-law chapter number was not confirmed and is omitted. The effective date, 21 March 2026, is taken from the Attorney General's notice. |

The change log also records a process limit. The editor who produced v2 did not have Roger's intermediate correction message. v2 applied the targeted fixes to the published essay. His exact revised sentences were unavailable to paste. v3 records his approval of F1 through F4. The archived final text is `source_v3.txt`.

## Lessons for AI-assisted drafting

The failures here are checkable. Each of them survives a glance and fails a lookup.

1. Resolve every DOI, then compare the returned title with the cited title. 10.1145/3686950 loads, and it is Errey et al. on narrative visualization. 10.1080/01944363.2013.787329 is one digit off Pierce and Shoup. 10.4000/tc.4999 is Akrich, and it lands on the 2010 reprint. The citation names the 1987 original.
2. Check article numbers against year and volume. JRCS 103712 and JBR 114981 are real articles. They are Hyun, Park, and Hong (2024) and Mourali et al. (2025). A number that resolves to a different author is a fabricated citation.
3. Read the abstract against the sentence it is asked to support. Padigar et al. are about constructive friction and value, which does not yield "compromises autonomy." Shabnam et al. say rigid rules intensify exclusion, which does not yield "users cannot dispute or modify" the rules. Seamful XAI is about seams, which does not yield "text boxes and advisory dashboards." Schüll describes group-level reconfiguration from touch-point data, which does not yield biometrics. Johnson and Barlow are about pain of payment, which does not yield impulse buying and does not yield unstaffed-store surveillance.
4. Beware a plausible author-journal pair. Mulcahy, Russell-Bennett, and Zainuddin publish service research. "The dyadic service encounter under automated mediation" in *Journal of Retailing* (2026) has no matching record. Ehsan publishes on explainable AI. The TOCHI article named in the original list has no matching record. Rosenberger writes on hostile design. The 2023 Minnesota book under that title has no matching record. The nearby real works are a 2020 article and a 2017 book, and they are different texts.
5. Treat a correction pass as a new draft. The second round assigned a wrong DOI to the paper that had just been found, invented a title and a page range for a *Management Science* article that had just been identified, and cited § 396-ff, the petting-zoo section, for the cashless-store rule. That rule is § 396-ii, "Cashless policies prohibited."
6. A real paper in the right field can still be the wrong evidence. Wood et al. (2019) studies algorithmic control of remote freelancers. Larivière et al. (2017) proposes the triad framework. Reinders et al. (2015) is a real reactance paper, and the change log found the support too weak to use. DHS (2025) is a real biometric rule covering noncitizens. The source has to make the sentence's claim.
7. Court holdings have to be read. The Conseil d'État cut a fine and upheld a retention violation. The original sentence reported the inverse result on the indicators. The lower fine accompanied a holding that the indicators had a lawful basis.
8. Fill a factual sentence or delete it. The cash mandates and the Dash Cart paragraph were sourced and had been uncited. The three-minute curb fee was precise, and it was wrong. A precise number still needs a source.
9. Mark what was not read. The open list above is the part of this essay a later pass still has to open: Hollands on the TIPPME exclusion, Suchman on the copier doors, the "risk scores" clause, Wilson-Nash on food, and the deliberation sentence shared by Batat and Johnson and Barlow. Stamatopoulos, Sanders, and Bray (2025) should stay labeled as a working paper for as long as it is one.

The practical sequence is short. Resolve the DOI to a title. Confirm the article number, volume, and year belong to that title. Read the abstract against the sentence. If the sentence is a holding, a statute, or a product rule, open the decision, the code, or the official page. If a later pass replaces a citation, run the same four checks on the replacement before it enters the list.
