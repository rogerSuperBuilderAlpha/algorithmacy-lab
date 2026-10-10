# DXD Substack v2: citation and wording changes

Built 4 Oct 2026 (ET). Base text: `../source.txt`, the essay as published. Output: `source_v2.txt`, which feeds `dxd-substack.html` and `dxd-substack.md`. The comparison-table PNG is unchanged because the table text did not change.

> **Important: Roger's t3u message was not available to me.** It was not in my context or on the box, and the algorithmacy-lab repo has no DRAFT.md. So his exact line edits are NOT merged verbatim. Instead, I made the same fixes he targeted (sections 2, 2.3-equivalent friction paragraph, 4, 5.1, 5.3, 5.7, 5.8, 7.3, plus the reference entries) directly on the published text. Where his revision relied on Wood et al. (2019), Larivière et al. (2017), Johnson & Barlow / Wilson-Nash (for surveillance anxiety), or Reinders et al. (2015), the replacements below are the ones to use. If his wording differs, his sentences can be swapped in, keeping the citations listed here.

Rules followed: no invented metadata. Every new source was checked by DOI resolution (doi.org CSL) or an official page, and its abstract or text was read against the sentence it supports. Claim-first sentences with terminal APA citations. No em-dashes in modified paragraphs (the only em-dash added anywhere is inside the official title of Hazée et al., 2025).

## A. Text edits (old → new)

### E1. §2 ¶3 (friction discourse) (wording softened)

**Old:** Automated checkouts, mobile payments, and sensor-driven access eliminate tangible payment interactions, encouraging impulse expenditures by detaching consumption from conscious financial evaluation (Johnson & Barlow, 2021).

**New:** Automated checkouts, mobile payments, and sensor-driven access eliminate tangible payment interactions, raising expenditures by reducing the felt "pain of payment" (Johnson & Barlow, 2021).

**Why:** Johnson & Barlow (2021) argue that reduced "pain of payment" (plus product attachment) can increase sales; they do not make an impulse-buying claim.

**Verified at:** https://doi.org/10.3390/jtaer16060130

### E2. §2 ¶4 (constructive friction; Roger's 2.3-equivalent) (citations replaced + wording softened)

**Old:** A parallel body of research demonstrates that removing friction compromises consumer autonomy (Padigar et al., 2025). Frictionless payment designs cause involuntary spending and permit automated commercial software to steer users toward unfavorable financial commitments (Padigar et al., 2025). Automated retail environments that eliminate human workers generate consumer apprehension, transforming routine transactions into encounters with opaque surveillance architectures (Gustafsson, 2026). Introducing intentional operational pauses preserves relational trust and consumer agency during service delivery (Pusceddu et al., 2025).

**New:** A parallel body of research argues that not all friction is a defect: some customer effort creates value, and eliminating this constructive friction can hinder value creation (Padigar et al., 2025). Unstaffed just walk out stores generate consumer apprehension about privacy, payment, and system reliability, transforming routine transactions into encounters with camera-based surveillance (Hazée et al., 2025; Schultz & Paetz, 2025). Offering interaction with an employee as a fall-back option offsets the negative consequences of forcing customers onto self-service technology (Reinders et al., 2008).

**Why:** Padigar et al. (2025) support 'eliminating constructive friction may hinder value creation', not 'compromises autonomy / involuntary spending / steering' (those claims removed). Gustafsson (2026) and Pusceddu et al. (2025) could not be found in Crossref/OpenAlex or the journals (JRCS 103712 is Hyun et al. 2024; JBR 186:114981 is Mourali et al. 2025). Replaced with peer-reviewed cashierless-store studies (Hazée et al.: reasons against adoption include privacy, payment unease, technology reliability; Schultz & Paetz: data-privacy concerns lower satisfaction and willingness to use) and Reinders et al. (2008: an employee fall-back offsets negative effects of forced self-service). The 'pauses preserve trust' claim is reframed as the human fall-back finding.

**Verified at:** https://doi.org/10.1002/mar.22111 · https://doi.org/10.1002/mar.22161 · https://doi.org/10.1016/j.jretconser.2025.104280 · https://doi.org/10.1177/1094670508324297

### E3. §2 ¶5 (structural problems) (citations replaced + wording softened)

**Old:** Coercive service design systematically eliminates human-staffed checkout counters to enforce digital compliance (Lee & Kim, 2026). Computational environments enforce algorithmic rules that users cannot dispute or modify (Shabnam et al., 2026). Retail automations erase service employees entirely or demote them to diagnostic monitors charged with maintaining sensor machinery (Gustafsson, 2026; Mulcahy et al., 2026; Pusceddu et al., 2025).

**New:** Providers increasingly replace full service with technology-based self-service, sometimes leaving no other option, and forced use breeds negative attitudes toward both the technology and the provider (Reinders et al., 2008). Phygital service systems impose digitally enforced rules, and rigid rules intensify exclusion (Shabnam et al., 2026). Service research frames technology as able to augment or substitute for frontline employees (Larivière et al., 2017), and in practice self-checkout recasts cashiers as monitors who troubleshoot machine problems and police customers (Moradi et al., 2025).

**Why:** Lee & Kim (2026), Mulcahy et al. (2026), Gustafsson (2026), Pusceddu et al. (2025) not found anywhere (removed). Reinders et al. (2008) abstract: full service 'increasingly replaced with technology-based self-service (TBSS), sometimes with no other option'; forced use leads to negative attitudes toward the TBSS and the provider. Shabnam et al. (2026) abstract identifies 'digitally enforced rules' and says 'rigid rules intensify exclusion' (it does not say users 'cannot dispute or modify' rules). Larivière et al. (2017) used only as a framework (technology augmenting/substituting employees). Moradi et al. (2025): 22 cashier interviews; self-checkout work became 'more focused on problems, monitoring, and policing'. 'Erase service employees entirely' and 'maintaining sensor machinery' softened accordingly.

**Verified at:** https://doi.org/10.1177/1094670508324297 · https://doi.org/10.1108/JSM-09-2025-0679 · https://doi.org/10.1016/j.jbusres.2017.03.008 · https://doi.org/10.1145/3711051

### E4. §2 ¶7 (information legibility) (wording softened)

**Old:** Phygital researchers propose solutions rooted strictly in information legibility: posting instructional signage, publishing privacy notifications, and updating screen layouts (Shabnam et al., 2026). These informational disclosures fail because

**New:** Phygital research often locates the remedy in legibility, holding that transparent algorithms enhance autonomy and trust while opacity reduces control (Shabnam et al., 2026). Informational disclosures fail because

**Why:** Shabnam et al.'s abstract says 'Transparent algorithms enhance autonomy and trust, while opacity reduces control' but does not list signage, privacy notifications, or screen layouts, and it also discusses adaptive governance, so 'strictly' was dropped.

**Verified at:** https://doi.org/10.1108/JSM-09-2025-0679

### E5. §4 last ¶ (XAI) (citation corrected + wording softened)

**Old:** Modern explainable artificial intelligence literature routinely reduces system transparency to informational text boxes and advisory dashboards (Ehsan et al., 2024).

**New:** Explainable artificial intelligence research has predominantly tackled algorithmic opacity, and seamful XAI researchers argue that hiding system seams disempowers users from mitigating the fallout of AI mistakes (Ehsan et al., 2024).

**Why:** The cited Ehsan et al. TOCHI 31(2) 'Operationalizing explainable AI in physical interaction spaces' does not exist. The real paper is 'Seamful XAI' (PACM HCI 8(CSCW1), Article 119). Its abstract says XAI 'has predominantly tackled algorithmic opaqueness' and that 'hiding the seams risks disempowering users to mitigate fallouts from AI mistakes'. It says nothing about 'text boxes and advisory dashboards'.

**Verified at:** https://doi.org/10.1145/3637396

### E6. §5.1 ride-hail (passenger fee) (fact corrected + citation added)

**Old:** while the passenger incurs fees for failing to reach the pickup coordinate within three minutes (Cameron, 2024; Rosenblat & Stark, 2016).

**New:** while an UberX passenger incurs per-minute wait fees for failing to board within two minutes of the driver's arrival (Cameron, 2024; Rosenblat & Stark, 2016; Uber, n.d.).

**Why:** Neither Cameron (2024) nor Rosenblat & Stark (2016) supports a three-minute passenger threshold. Uber's help page: UberX riders 'are charged a per-minute wait time fee if they don't enter the vehicle within 2 minutes of the driver's arrival' (5 min for Black; varies by location).

**Verified at:** https://help.uber.com/en/riders/article/wait-time-fees-and-refunds?nodeId=469f1786-1543-4c83-abbf-ddccb7826fc2

### E7. §5.1 ride-hail (rule drift) (wording softened)

**Old:** Dispatch algorithms, surge factors, and incentive structures drift continuously across unannounced software builds (Lee et al., 2015).

**New:** Dispatch algorithms, surge factors, and incentive structures shift quickly and unpredictably from the driver's vantage point (Lee et al., 2015).

**Why:** Lee et al. (2015) document drivers' difficulty anticipating fast-changing surge pricing and opaque assignment; the paper does not study 'unannounced software builds'.

**Verified at:** https://doi.org/10.1145/2702123.2702548

### E8. §5.2 airport gate (abbreviations) (APA format)

**Old:** automate identity verification (CBP, 2018; TSA, 2026).

**New:** automate identity verification (U.S. Customs and Border Protection [CBP], 2018; Transportation Security Administration [TSA], 2026).

**Why:** Group-author abbreviations are now defined at first citation so the in-text names match the reference entries.

**Verified at:** https://www.dhs.gov/publication/dhscbppia-056-traveler-verification-service · https://www.dhs.gov/publication/dhstsapia-046-travel-document-checker-automation-using-facial-recognition

### E9. §5.2 airport gate (opt-out) (citation replaced + wording softened)

**Old:** Federal statutory rules permit United States citizens to opt out of commercial biometric scans, but field audits reveal that mandated notification signage remains obscure, missing, or obscured from passenger sightlines (Gambler, 2022). Travelers attempting to exercise opt-out rights routinely encounter threats of denied boarding, severe delays, or punitive secondary interrogations by border guards (DHS, 2025).

**New:** Federal policy permits United States citizens to opt out of biometric face scans, but government auditors found that privacy notices were often incomplete, outdated, or unavailable and that opt-out information was limited (Gambler, 2022). Travelers attempting to exercise opt-out rights at airport checkpoints report being scanned before they could decline, being discouraged or refused by officers, and fearing secondary screening (Buolamwini et al., 2025).

**Why:** GAO-22-106154 (Gambler testimony, 27 Jul 2022) found CBP privacy notices 'were not always current or complete' or available and opt-out information limited. Opt-out is a CBP policy, not a statute. DHS (2025, FR Doc 2025-19655) is the final rule extending biometric entry/exit collection to noncitizens; it says nothing about threats to opt-out travelers, so it was removed. Replaced with AJL 'Comply to Fly?' survey of 420 travelers at 91 airports (TSA checkpoints): 82 scanned before they could opt out, 56 coerced/discouraged, 36 refused, 49 feared consequences, a few believed they got secondary screening. 'Denied boarding' and 'border guards' are not supported and were removed.

**Verified at:** https://www.gao.gov/products/gao-22-106154 · https://ajl.org/flyreport · https://afp.oxford-aiethics.ox.ac.uk/sitefiles/complytoflyreport-ajl.pdf · https://www.federalregister.gov/documents/2025/10/27/2025-19655/collection-of-biometric-data-from-aliens-upon-entry-to-and-departure-from-the-united-states

### E10. §5.3 warehouse (quota drift + HELP abbreviation) (wording softened + in-text name fixed)

**Old:** Picking quotas fluctuate dynamically based on seasonal logistics velocity and opaque software revisions (Cheon & Erickson, 2025; U.S. Senate HELP Committee, 2024).

**New:** Picking quotas vary by facility and position and are imposed on workers rather than negotiated (Cheon & Erickson, 2025; U.S. Senate Committee on Health, Education, Labor, and Pensions, 2024).

**Why:** The HELP report says 'rates vary based on facility and position'. Cheon & Erickson describe 'imposed productivity rates'. Neither documents 'seasonal velocity' or 'opaque software revisions'. The in-text author now matches the reference entry.

**Verified at:** https://www.help.senate.gov/imo/media/doc/amazon_investigation.pdf · https://doi.org/10.1145/3757409

### E11. §5.3 warehouse (statutes) (citation added + minor wording)

**Old:** require employers to provide written quota descriptions and prohibit performance algorithms from penalizing workers for taking bathroom breaks.

**New:** require employers to provide written quota descriptions and prohibit quotas that penalize workers for taking bathroom breaks (Cal. Lab. Code §§ 2100–2112, 2021; N.Y. Lab. Law §§ 780–788, 2022).

**Why:** Both statutes regulate quotas, not 'performance algorithms' as such. Added terminal citations.

**Verified at:** https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?article=&chapter=&division=2.&lawCode=LAB&part=8.6.&title= · https://www.nysenate.gov/legislation/laws/LAB/A21-A

### E12. §5.3 warehouse (Conseil d'État) (factual correction)

**Old:** Regulatory authorities in France reduced corporate fines while ruling that continuous real-time scanner metrics violate European privacy laws by transforming ordinary physical movements into permanent disciplinary evidence (Conseil d'État, 2025).

**New:** In France, the Conseil d'État cut the data-protection fine against Amazon France Logistique from €32 million to €15 million: it held that the scanner productivity indicators themselves had a lawful basis, but upheld the finding that retaining every worker's scanner data for 31 days breached the GDPR's data-minimisation principle (Conseil d'État, 2025).

**Why:** The original sentence reversed the ruling. The court annulled the CNIL's finding that the 'stow machine gun', 'idle time' and 'temps de latence' indicators lacked a legal basis (Art. 6 GDPR). It confirmed only the minimisation breach for the 31-day retention (Art. 5), plus uncontested information and security breaches, and cut the fine to €15 million.

**Verified at:** https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-12-23/492830 · https://juricaf.org/arret/FRANCE-CONSEILDETAT-20251223-492830

### E13. §5.7 cashless counters (citations added)

**Old:** Municipalities and state legislatures in Massachusetts and New York intervened by mandating cash acceptance at physical storefronts, blocking corporations from turning digital payment credentials into prerequisites for physical retail participation.

**New:** Municipalities and state legislatures in Massachusetts and New York intervened by mandating cash acceptance at physical storefronts, blocking corporations from turning digital payment credentials into prerequisites for physical retail participation (Mass. Gen. Laws ch. 255D, § 10A, 1978; N.Y. Gen. Bus. Law § 396-ii, 2025; N.Y.C. Admin. Code § 20-840, 2020).

**Why:** The sentence had no citation. Massachusetts ch. 255D § 10A (retailers may not discriminate against cash buyers); NYC Admin Code § 20-840 (Local Law 34 of 2020); N.Y. Gen. Bus. Law § 396-ii 'Cashless policies prohibited' (S4153A, signed 2025, effective 21 March 2026). § 396-ff is not the cash law.

**Verified at:** https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleIV/Chapter255D/Section10A · https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-114885 · https://www.nysenate.gov/legislation/bills/2025/S4153/amendment/A · https://ag.ny.gov/press-release/2026/attorney-general-james-notifies-new-yorkers-about-new-state-law-requiring-stores

### E14. §5.8 ESLs (concern + NY law) (wording corrected + citation format)

**Old:** (FTC, 2024, 2025; New York State, 2025; Warren & Casey, 2024). New York enacted statutory requirements compelling retailers to post disclosures whenever in-store prices rely on personal data algorithms (New York State, 2025).

**New:** (Federal Trade Commission [FTC], 2024, 2025; Warren & Casey, 2024). New York now requires any seller to disclose, alongside the price, when that price was set by an algorithm using the consumer's personal data (N.Y. Gen. Bus. Law § 349-a, 2025).

**Why:** § 349-a (in effect 10 Nov 2025) covers any 'personalized algorithmic pricing' displayed to a NY consumer, online or offline, not only in-store prices. The statute is a disclosure law, not an expression of 'concern', so it was dropped from the first citation. Statute citation now in legal format.

**Verified at:** https://www.nysenate.gov/legislation/laws/GBS/349-A · https://ag.ny.gov/press-release/2025/attorney-general-james-warns-new-yorkers-about-algorithmic-pricing-new-law-takes

### E15. §5.8 ESLs (empirical deployments) (citation corrected + wording softened + source added)

**Old:** Retailers install electronic shelf labels to reduce the labor costs of manually replacing paper tags and to implement scheduled price adjustments across entire store inventories (Stamatopoulos et al., 2021).

**New:** Retailers install electronic shelf labels to reduce the labor and material costs of changing prices, and adoption produces more frequent, smaller price changes, most of them decreases (Stamatopoulos et al., 2021). Transaction data from a major US grocery chain show no meaningful rise in short-lived price spikes after shelf-label installation (Stamatopoulos et al., 2025).

**Why:** Stamatopoulos, Bassamboo & Moreno (2021, MS 67(1)) abstract: ESLs cut 'labor and material costs of price adjustment'; 'more and smaller price changes occurred with ESLs... mostly price decreases'. Nothing about 'scheduled' adjustments across entire inventories. The cited 'Tan & Zervas, MS 67(8)' article does not exist. Added the 2025 SSRN working paper (Stamatopoulos, Sanders & Bray) as support for 'no surge pricing in practice'. The SSRN page blocks scripts, so its content was verified through the UC San Diego press release (114 stores, 180M observations, no meaningful change).

**Verified at:** https://doi.org/10.1287/mnsc.2019.3551 · https://doi.org/10.2139/ssrn.5271491 · https://today.ucsd.edu/story/new-research-debunks-fears-of-supermarket-surge-pricing-with-electronic-shelf-labels

### E16. §5.9 hostile architecture (citation replaced)

**Old:** (Petty, 2016; Rosenberger, 2023).

**New:** (Petty, 2016; Rosenberger, 2017).

**Why:** No Rosenberger (2023) 'On hostile design: The political philosophy of urban deterrence' book exists. His University of Minnesota Press book on anti-homeless design is Callous Objects (2017).

**Verified at:** https://www.upress.umn.edu/9781517904401/callous-objects/

### E17. §6 Form 4 (citations added)

**Old:** (Cameron, 2024; Wilson-Nash et al., 2026). This reality applies

**New:** (Cameron, 2024; Gregory, 2021; Wilson-Nash et al., 2026; Zheng et al., 2019). This reality applies

**Why:** Cameron (2024) studies ride-hail consent and does not support the claim that delivery drivers risk collisions to beat the clock. Zheng et al. (2019; 824 delivery riders) found that time pressure raises crash involvement through fatigue and risky riding. Gregory (2021; 25 couriers) documents 'physical risk and bodily harm' under algorithmically managed delivery work. These are the real sources for driver physical strain under algorithmic deadlines (the role Roger's revision gave Wood et al., 2019).

**Verified at:** https://doi.org/10.1177/0361198119841028 · https://doi.org/10.1177/0950017020969593

### E18. §7.1 structural refusal (citation replaced + wording softened)

**Old:** fail to provide legitimate exit options when non-digital alternatives trigger interrogations, delays, or outright exclusion from essential services (DHS, 2025; Gambler, 2022; Wilson-Nash et al., 2026).

**New:** fail to provide legitimate exit options when non-digital alternatives trigger officer pressure, delays, or outright exclusion from essential services (Buolamwini et al., 2025; Gambler, 2022; Wilson-Nash et al., 2026).

**Why:** DHS (2025) final rule does not document opt-out costs. The AJL survey documents officer discouragement/refusal and some secondary screening, not 'interrogations'.

**Verified at:** https://ajl.org/flyreport

### E19. §7.3 conspicuous commitment (citations added + wording softened)

**Old:** Consumers reject invisible tracking architectures, favoring visible verification mechanisms. In grocery environments, retail corporations retreated from automated ceiling camera tracking after shoppers rejected invisible billing systems. Shoppers preferred cart-mounted terminals that display running financial tallies and confirm individual item registrations as goods enter the basket.

**New:** Consumers resist invisible billing, favoring visible verification mechanisms: in autonomous stores, limited access to staff and the inability to verify the basket before payment deter patronage (Benoit et al., 2024). In US grocery environments, Amazon removed camera-based Just Walk Out checkout from its Fresh supermarkets after customers said they wanted to view their receipt as they shopped (Palmer, 2024). In larger grocery stores, the company reported that shoppers so far preferred cart-mounted terminals that display a running tally of purchases and track spending in real time as goods enter the basket (Kumar, 2024).

**Why:** The paragraph had no citations. CNBC (Palmer, 3 Apr 2024) confirms Amazon removed Just Walk Out from US Fresh stores, quoting a spokesperson that customers 'wanted the ability to... view their receipt as they shop'. Amazon's own statement (Kumar, 17 Apr 2024) says that in larger grocery stores 'customers so far prefer Amazon Dash Cart', which tracks 'savings and spending in real time', and that customers want 'a running tally'. 'Shoppers rejected invisible billing systems' is stronger than the evidence, so it was softened. Benoit et al. (2024, J. Retailing) show that the inability to verify the basket and limited staff access are barriers to autonomous-store patronage.

**Verified at:** https://www.cnbc.com/2024/04/03/amazon-ditches-cashierless-checkout-system-at-its-grocery-stores.html · https://www.aboutamazon.com/news/retail/amazon-just-walk-out-dash-cart-grocery-shopping-checkout-stores · https://doi.org/10.1016/j.jretai.2023.12.003

### E20. §8 methodological boundaries (APA format)

**Old:** (California, 2021; FTC, 2025; New York State, 2022).

**New:** (Cal. Lab. Code §§ 2100–2112, 2021; FTC, 2025; N.Y. Lab. Law §§ 780–788, 2022).

**Why:** Statute citations now match the reference entries.

## B. Reference-list changes

### Removed (no such work could be found, or no longer cited)
- **Gustafsson, E. (2026).** JRCS 88, 103712. Not found in Crossref, OpenAlex, or the journal. Article 103712 is Hyun, Park & Hong (2024, vol. 78). Replaced by Hazée et al. (2025), Schultz & Paetz (2025), and Moradi et al. (2025).
- **Lee, H., & Kim, Y. (2026).** Service Industries Journal 46(2). Not found. Replaced by Reinders et al. (2008).
- **Mulcahy, R., Russell-Bennett, R., & Zainuddin, N. (2026).** J. Retailing 102(1). Not found. Replaced by Moradi et al. (2025).
- **Pusceddu, G., Cabiddu, F., & Hurmelinna-Laukkanen, P. (2025).** JBR 186, 114981. Not found; that article number is Mourali et al. (2025). Replaced by Reinders et al. (2008) (human fall-back) and Moradi et al. (2025).
- **Department of Homeland Security (2025).** FR Doc 2025-19655. A real final rule (biometric entry/exit for noncitizens, 90 FR 48604), but it does not support either sentence that cited it. Both citations were replaced (E9, E18), so the entry is gone. https://www.federalregister.gov/documents/2025/10/27/2025-19655/
- **Wood, A. J., Graham, M., Lehdonvirta, V., & Hjorth, I. (2019).** WES 33(1), 56–75. Real, but it studies remote online gig work (Southeast Asia/Sub-Saharan Africa), not drivers or warehouses, and the published essay never cites it. Removed. Gregory (2021) and Zheng et al. (2019) cover driver/courier physical strain under algorithmic time pressure instead. Wood could only honestly support claims about remote platform workers' overwork, sleep deprivation, and exhaustion, and the essay has no such sentence.
- **Rosenberger, R. (2023).** *On hostile design: The political philosophy of urban deterrence.* No such book exists. Replaced by Rosenberger (2017), *Callous objects* (U Minnesota Press). (Rosenberger's 2020 *Urban Studies* article is titled "On hostile design: Theoretical and empirical prospects".)

### Corrected metadata (entry existed, details wrong)
- **Ehsan et al. (2024)**: was "Ehsan, Wintersberger, Liao, Mara, Streit & Riener, Operationalizing explainable AI in physical interaction spaces, TOCHI 31(2)". That paper doesn't exist. Now: Ehsan, Liao, Passi, Riedl & Daumé III, *Seamful XAI*, PACM HCI 8(CSCW1), Article 119, 1–29, https://doi.org/10.1145/3637396 (article number confirmed in the author PDF).
- **Johnson & Barlow (2021)**: was "The phygital advantage: Frictionless commerce and consumer spending, J. Consumer Marketing 38(6)". Now: "Defining the phygital marketing advantage," JTAER 16(6), 2365–2385, https://doi.org/10.3390/jtaer16060130
- **Mele & Russo-Spena (2025)**: was "The agency of smart artifacts in phygital service ecosystems, JSR 28(2)". Now: "Agencement of onlife and phygital: Smart tech–enabled value co-creation practices," J. Service Management 36(2), 217–240, https://doi.org/10.1108/JOSM-03-2023-0113. The abstract (onlife agency, phygital materiality) still supports the §2 sentences.
- **Padigar et al. (2025)**: was "Padigar, Li, S., & Manjunath, A., Constructive friction in algorithmic commerce, HBR on Technology". Now: Padigar, M., Li, Y., & Manjunath, C. N., "'Good' and 'bad' frictions in customer experience," Psychology & Marketing 42(1), 21–43, https://doi.org/10.1002/mar.22111
- **Stamatopoulos et al. (2021)**: was "Stamatopoulos, Tan & Zervas, Dynamic pricing with electronic shelf labels, MS 67(8)". Now: Stamatopoulos, Bassamboo & Moreno, "The effects of menu costs on retail performance...," MS 67(1), 242–256, https://doi.org/10.1287/mnsc.2019.3551
- **Akrich (1987)**: the DOI points to the 2010 reprint (Techniques & Culture 54–55, 205–219). The entry now cites the 1987 original (Techniques et Culture, 9, 49–64) with a reprint note and the DOI.
- **Petty (2016)**: true title "...Homelessness, urban securitisation and the question of 'hostile architecture'" (was "urban architecture... 'hostile design'").
- **Pierce & Shoup (2013)**: DOI corrected from ...787329 to **10.1080/01944363.2013.787307**.
- **Kitchin & Dodge (2009)**: pages corrected from 58–78 to **96–114** (author's publication list: https://www.kitchin.org/?page_id=1457).
- **CBP (2018) / TSA (2026)**: group author now "U.S. Customs and Border Protection", with dates (14 Nov 2018; 16 Jan 2026), the PIA-046(e) "update" wording, and official DHS URLs. Abbreviations are defined at first citation.
- **FTC (2024, 2025)**: dates (23 Jul 2024; Jan 2025), full staff-perspective title, and URLs added. Abbreviation defined at first citation.
- **Gambler (2022)**: identified as GAO testimony (27 Jul 2022), with URL.
- **Conseil d'État (2025)**: date and official URL added. The essay's description of the holding was corrected (E12).
- **Statutes**: "California (2021)" became Cal. Lab. Code §§ 2100–2112 (2021). "New York State (2022)" became N.Y. Lab. Law §§ 780–788 (2022, eff. 19 Jun 2023). "New York State (2025)" became N.Y. Gen. Bus. Law § 349-a (2025, eff. 10 Nov 2025; the code heading is "Pricing", and "Algorithmic Pricing Disclosure Act" is the act's popular name used by the NY AG). In-text citations were changed to match.
- **U.S. Senate HELP Committee (2024)**: in-text name now matches the reference ("U.S. Senate Committee on Health, Education, Labor, and Pensions"). Report type set to "Majority staff report" and URL added.
- **Warren & Casey (2024)**: date (5 Aug 2024) and URL added. The descriptive title now matches the letter (price gouging). The letter does mention weather-based surges and facial-recognition shelves, so §5.8 is supported.
- **Floridi (2015)**: DOI added (open access). **Gutelius & Theodore (2019)**: co-publisher Working Partnerships USA and URL added. **Schüll (2012)**: Limn URL added. **Weiser (1994)**: formatted as UIST '94 keynote slides, 2 Nov 1994 (Crossref lists the keynote abstract as "Creating the invisible interface," doi 10.1145/192426.192428). **Shabnam et al. (2026)**: page range replaced with "Advance online publication" (no volume/issue yet). **Cheon & Erickson (2025)**: "Article CSCW228" format. **Moradi et al. (2025)**: Article CSCW153 (from the ACM reference block on arXiv 2410.02888; Crossref has no article number).

### Added (all verified; abstract or text read against the sentence)

- **Benoit, S., Altrichter, B., Grewal, D., & Ahlbom, C.-P. (2024). Autonomous stores: How levels of in-store automation affect store patronage. Journal of Retailing, 100(2), 217–238.** https://doi.org/10.1016/j.jretai.2023.12.003. Use: §7.3 (E19): consumers prefer staffed stores. Limited staff access and the inability to verify the basket before payment are patronage barriers.
- **Buolamwini, J., Raman, S., & Dean, A. (2025, July 21). Comply to fly? How airport travelers experience TSA's facial recognition experiment. Algorithmic Justice League.** https://ajl.org/flyreport. Use: §5.2 and §7.1 (E9, E18): survey of 420 travelers at 91 airports. 82 scanned before opting out, 56 discouraged/coerced, 36 refused, 49 feared consequences.
- **Gregory, K. (2021). 'My life is more valuable than this': Understanding risk among on-demand food couriers in Edinburgh. Work, Employment and Society, 35(2), 316–331.** https://doi.org/10.1177/0950017020969593. Use: §6 (E17): physical risk and bodily harm under algorithmically managed courier work.
- **Hazée, S., De Keyser, A., Larivière, B., Kim, Y., Talebi, A., & Gordeliy, I. (2025). Just walk out stores—The future of shopping? Examining configurations of reasons for and against consumer adoption. Psychology & Marketing, 42(4), 987–1017.** https://doi.org/10.1002/mar.22161. Use: §2 (E2): reasons against adoption include privacy, payment unease, technology reliability, and customer-care inconvenience.
- **Kumar, D. (2024, April 17). An update on Amazon's plans for Just Walk Out and checkout-free technology. About Amazon.** https://www.aboutamazon.com/news/retail/amazon-just-walk-out-dash-cart-grocery-shopping-checkout-stores. Use: §7.3 (E19): 'customers so far prefer Amazon Dash Cart' in larger grocery stores, with spending tracked in real time and a 'running tally'.
- **Larivière, B., Bowen, D., Andreassen, T. W., Kunz, W., Sirianni, N. J., Voss, C., Wünderlich, N. V., & De Keyser, A. (2017). "Service Encounter 2.0": An investigation into the roles of technology, employees and customers. Journal of Business Research, 79, 238–246.** https://doi.org/10.1016/j.jbusres.2017.03.008. Use: §2 (E3): cited only as a framework (technology augmenting or substituting frontline employees).
- **Moradi, P., Levy, K., & Cheyre, C. (2025). Pseudo-automation: How labor-offsetting technologies reconfigure roles and relationships in frontline retail work. Proceedings of the ACM on Human-Computer Interaction, 9(2), Article CSCW153, 1–21.** https://doi.org/10.1145/3711051. Use: §2 (E3): self-checkout makes cashier work centre on problems, monitoring, and policing. This is the real source for 'frontline workers demoted to monitoring/fixing self-service tech'.
- **Palmer, A. (2024, April 3). Amazon ditches cashierless checkout system at its grocery stores. CNBC.** https://www.cnbc.com/2024/04/03/amazon-ditches-cashierless-checkout-system-at-its-grocery-stores.html. Use: §7.3 (E19): Amazon removed Just Walk Out from US Fresh stores, and customers wanted to 'view their receipt as they shop'.
- **Reinders, M. J., Dabholkar, P. A., & Frambach, R. T. (2008). Consequences of forcing consumers to use technology-based self-service. Journal of Service Research, 11(2), 107–123.** https://doi.org/10.1177/1094670508324297. Use: §2 (E2, E3): forced self-service leads to negative attitudes toward the technology and the provider, and an employee fall-back offsets this. Replaces Reinders et al. (2015) for the reactance point. Reinders, Frambach & Kleijnen (2015), EJM 49(1/2), 190–211, doi 10.1108/EJM-12-2012-0735, is real but supports reactance only weakly, so it was not added.
- **Schultz, C. D., & Paetz, F. (2025). The way out – Customer benefits and self-service satisfaction in cashierless shopping systems. Journal of Retailing and Consumer Services, 85, Article 104280.** https://doi.org/10.1016/j.jretconser.2025.104280. Use: §2 (E2): data-privacy concerns lower satisfaction with, and willingness to use, cashierless systems.
- **Stamatopoulos, I., Sanders, R. E., & Bray, R. (2025). Electronic shelf labels have not led to surge pricing in US grocery retail, despite regulator concerns [Working paper]. SSRN.** https://doi.org/10.2139/ssrn.5271491. Use: §5.8 (E15): no meaningful rise in temporary price spikes after ESL adoption. Verified through the UC San Diego release (https://today.ucsd.edu/story/new-research-debunks-fears-of-supermarket-surge-pricing-with-electronic-shelf-labels) because SSRN blocks automated access. This is a working paper, not peer-reviewed.
- **Uber. (n.d.). Wait time fees and refunds. Uber Help. Retrieved October 4, 2026.** https://help.uber.com/en/riders/article/wait-time-fees-and-refunds?nodeId=469f1786-1543-4c83-abbf-ddccb7826fc2. Use: §5.1 (E6): UberX wait fee after 2 minutes. Varies by product and location.
- **Zheng, Y., Ma, Y., Guo, L., Cheng, J., & Zhang, Y. (2019). Crash involvement and risky riding behaviors among delivery riders in China: The role of working conditions. Transportation Research Record, 2673(4), 1011–1022.** https://doi.org/10.1177/0361198119841028. Use: §6 (E17): 824 riders. Time pressure is linked to crashes through fatigue and risky riding.
- **Mass. Gen. Laws ch. 255D, § 10A (1978).** https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleIV/Chapter255D/Section10A. Use: §5.7 (E13).
- **N.Y. Gen. Bus. Law § 396-ii (2025). Cashless policies prohibited (S4153A/A7929; effective March 21, 2026).** https://www.nysenate.gov/legislation/bills/2025/S4153/amendment/A. Use: §5.7 (E13). Effective date confirmed by the NY AG: https://ag.ny.gov/press-release/2026/attorney-general-james-notifies-new-yorkers-about-new-state-law-requiring-stores. The session-law chapter number was not confirmed, so it is omitted.
- **N.Y.C. Admin. Code § 20-840 (2020). Local Law 34 of 2020.** https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-114885. Use: §5.7 (E13).

## C. Checks run
- `xcheck.py`: every in-text citation has a reference and every reference is cited (66/66). The one reported mismatch is a parser artifact caused by the comma inside the HELP Committee's name; the two strings are identical.
- `verify_v2.py`: every prose line of `source_v2.txt` appears verbatim in the HTML, no box-drawing characters remain, all 8 diagrams render as lists. The SFpark "(+$0.25" token difference is a tokenizer artifact that also appears in v1.
- All 57 reference URLs/DOIs were requested. Every DOI resolves through doi.org content negotiation. Some publisher landing pages (Wiley, ACM, MDPI, SSRN, GAO) return 403 to scripts, and leginfo.ca.gov times out from the box. Uber help returns 404 to curl but loads in the fetch tool.

## D. Still unresolved / flagged for Roger (not changed)
1. **t3u wording**: see the note at the top. His exact revised sentences need to be merged or resent.
2. **§5.5 casino (Schüll, 2012)**: the Limn essay does support real-time reconfiguration. Casinos switch game configurations "(i.e theme, denomination, payout rate)" in real time to match emerging player preference groups, using touch-point data and heat maps. It does not support "biometric" data driving these changes, and it describes adjustments for aggregate groups, not individual players. Suggested minimal softening: replace "real-time biometric and behavioral data" with "real-time player-tracking data". Not changed, because this falls outside the sections Roger revised.
3. **Hollands et al. (2017)**: cited for the cafeteria "collects no data" points (§ intro, §1) and for TIPPME "explicitly excluding systems that tailor options to specific individuals". The paywalled full text was not checked against that exclusion wording.
4. **Suchman (1985)**: report ISL-6 exists. The specific "paper-release doors and manual abort controls" detail is interpretive and was not checked against the report text.
5. **Johnson & Barlow (2021) in §2 ¶1**: grouped with Mele et al. under "Systematic reviews indicate". J&B is a literature-based theoretical paper, not a systematic review. Consider citing only Mele et al. (2023) there.
6. **Figure "Seamless Designs Versus Constructive Friction"**: the label "(Padigar et al., 2025)" is attached to "preserves human dignity, prevents automated steering, and exposes authority", which goes beyond Padigar. Suggest "(after Padigar et al., 2025)" or dropping the citation from the figure.
7. **§5.2 "passenger risk scores" (Adey, 2004; TSA, 2026)**: the TSA PIA describes gallery pre-staging and matching, not risk scores. Not re-verified sentence by sentence.
8. **Wilson-Nash et al. (2026)**: supports "digital technology captivity". The specific "exclusion from purchasing food" example was not checked against the full text.
9. **Amazon context**: on 27 Jan 2026 Amazon announced it is closing Amazon Go and Amazon Fresh stores (update note on the Kumar page). §7.3 remains accurate as history, but Roger may want to acknowledge this.
10. **Lee et al. (2015) / Rosenblat & Stark (2016)**: not re-read in full. §5.1 wording was softened conservatively.
11. **Batat (2024) / Johnson & Barlow (2021)** for "ideal customer journey... removes conscious cognitive deliberation" (§2 ¶3) was not checked at sentence level.

---

# v3 changes (approved by Roger, 4 Oct 2026, ET)

Base: `../v2/source_v2.txt`, now `source_v3.txt`. This resolves v2 flags D2, D5, D6, and D9.

### F1. §5.5 casino

**Old:** Modern slot platforms dynamically modify payout pacing, visual assets, and game volatility based on real-time biometric and behavioral data, while floor managers

**New:** Modern slot platforms dynamically modify payout pacing, visual assets, and game volatility based on real-time player-tracking data, while floor managers

**Why:** Schüll (2012, Limn) describes casinos switching game configurations ('theme, denomination, payout rate') in real time from tracked touch-point data to match emerging player preference groups. It does not mention biometric data.

**Verified at:** https://limn.press/article/the-touch-point-collective-crowd-contouring-on-the-casino-floor/

### F2. §2 ¶1 (systematic review)

**Old:** Systematic reviews indicate that empirical studies deploy the term without operational consensus, oscillating between ubiquitous computing descriptions and consumer experience frameworks (Johnson & Barlow, 2021; Mele et al., 2023).

**New:** A systematic review indicates that empirical studies deploy the term without operational consensus, oscillating between ubiquitous computing descriptions and consumer experience frameworks (Mele et al., 2023).

**Why:** Johnson & Barlow (2021) is a literature-based theoretical paper, not a systematic review, so only Mele et al. (2023) is cited here. 'Systematic reviews indicate' became singular to match the single citation. Johnson & Barlow is still cited in §2 ¶1 sentence 1 and in §2 ¶3 and ¶6, where it supports the claim.

**Verified at:** https://doi.org/10.1007/s43039-023-00070-7 · https://doi.org/10.3390/jtaer16060130

### F3. Figure: Seamless Designs Versus Constructive Friction

**Old:** |  (Padigar et al., 2025)          |

**New:** |  (after Padigar et al., 2025)    |

**Why:** The figure row goes beyond what Padigar et al. claim, so the attribution now reads '(after Padigar et al., 2025)'.

### F4. §7.3 (Amazon closure)

**Old:** track spending in real time as goods enter the basket (Kumar, 2024).

**New:** track spending in real time as goods enter the basket (Kumar, 2024). On January 27, 2026, Amazon announced that it would close its Amazon Go and Amazon Fresh physical stores, converting some locations to Whole Foods Market (Amazon Staff, 2026).

**Why:** Added context sentence. Amazon's statement of 27 Jan 2026 (datePublished 2026-01-27T14:55Z, byline 'Amazon Staff'): 'we've made the difficult decision to close our Amazon Go and Amazon Fresh physical stores, converting various locations into Whole Foods Market stores.' Corroborated by CNBC and Reuters the same day.

**Verified at:** https://www.aboutamazon.com/news/company-news/amazon-fresh-go-stores-closing-expanding-whole-foods · https://www.cnbc.com/2026/01/27/amazon-fresh-go-supermarkets-whole-foods-convert.html · https://www.reuters.com/business/retail-consumer/amazon-expand-same-day-delivery-close-some-stores-whole-foods-expansion-push-2026-01-27/

### Reference added

- **Amazon Staff. (2026, January 27). Amazon to close Fresh, Go stores, expanding Whole Foods. About Amazon.** https://www.aboutamazon.com/news/company-news/amazon-fresh-go-stores-closing-expanding-whole-foods (date from page metadata; byline 'Amazon Staff'; closure statement quoted in F4).

### Other notes

- **Casino table row:** reads 'YES (Real-Time Difficulty)', with no biometric or per-individual wording, so the table text is unchanged and `dxd-comparison-table.png` is identical to v2. §5.5 ¶2 ('ingests telemetry exclusively from the gambler') describes one-sided sensing (Mark 2), not per-individual tailoring, so it was left as is.

- **Friction figure:** in the HTML/MD output, this figure's term/description separator is now a colon instead of an em-dash, because the figure is a modified block. The other figures keep the v1 format.

- **Checks:** citation cross-check gives 67 in-text keys = 67 references, with no orphans either way (Johnson & Barlow is still cited 3 times; 'after Padigar' resolves to Padigar et al., 2025). Render check: all prose lines present, no box characters, all 8 figures render as lists, and a screenshot was reviewed (qa/v3.png). No em-dashes in F1–F4 paragraphs.

