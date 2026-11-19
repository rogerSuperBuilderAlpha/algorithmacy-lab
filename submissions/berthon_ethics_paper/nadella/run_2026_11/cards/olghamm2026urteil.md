---
citekey: olghamm2026urteil
title: Oberlandesgericht Hamm, 4. Zivilsenat, Urteil vom 12.05.2026, 4 UKl 3/25 (ECLI:DE:OLGHAM:2026:0512.4UKL3.25.00)
authors: Oberlandesgericht Hamm
year: 2026
doi: null
source_basis: partial-text
pages_read: header and Tenor; paras 1-31 (Tatbestand); paras 32-87 (admissibility; attribution of chatbot output); para 104 (commercial relevance); para 118 (leave to appeal). Paras 88-103 and 105-117 not read
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B5/olghamm2026/judgment.html
sha256: c0a50a174f615a1619f4fe1aed2ca48625ac1f5c93ea13b07007eef6f97be6f5
verified: pending
structure_sections: 4.2; 4.4-loss; 4.4-contest; 6-smartreader; counter
type: case
venue: Justizportal Nordrhein-Westfalen (NRWE), official decision database; first-instance action under § 6 UKlaG
source_url: https://nrwe.justiz.nrw.de/olgs/hamm/j2026/4_UKl_3_25_Urteil_20260512.html
record_check: court database page header (court, date 12.05.2026, Aktenzeichen 4 UKl 3/25, ECLI, "Rechtskraft: rechtskräftig"); lead found via secondary report (tww.law, June 2026); court press release URL returned HTTP 410
facet: B5
supersedes: none
written: 2026-11-18
---

## Summary

Read: header and Tenor, paras 1-87, 104 and 118 (attribution and relevance); paras 88-103 and 105-117 not read. A registered consumer association sued a cosmetic-treatment firm whose website
chatbot told a user on 3 April 2025 that the firm's two physician directors were specialists in plastic and aesthetic
surgery, which they were not. The firm argued that the chatbot answered autonomously, by statistical calculation, so
its outputs were not the firm's own commercial acts, and that consumers know AI answers need fact-checking. The Higher
Regional Court held the chatbot's answers to be the firm's own commercial acts under § 2(1) no. 2 UWG, because the
firm operated it, set its frame of action and could reprogram it (as it did, with a prompt instruction and a keyword
filter); the "black box" problem did not change this. It rejected the fact-checking defence as resting on no rule of
experience. The firm was enjoined (fine up to EUR 250,000 per breach) and ordered to pay the association EUR 260. The
page header marks the judgment final ("rechtskräftig"), although para 118 grants leave to appeal.

## Key facts it relies on

- Tenor and para 2: the claimant is an association entered in the list under § 4 UKlaG, suing for an injunction and warning costs; the defendant is ordered to pay "an den Kläger 260,00 Euro". [quote; paraphrase]
- Paras 5-6: on 3 April 2025 the chatbot answered "Ja, A und B sind Fachärzte für plastische und ästhetische Chirurgie." [quote]
- Para 12: after the warning letter the firm deactivated the chatbot and added "einer Prompt-Anweisung zur neutralen Antwort bei Fragen mit dem Begriff „Facharzt“ sowie eines nachgelagerten Keyword-Filters". [quote]
- Para 30 (the firm's case): the chatbot works "autonom und werde nicht im Einzelnen gesteuert oder kontrolliert, so dass dessen Äußerungen nicht auf eine menschliche Willensentschließung zurückzuführen seien." [quote]
- Para 70: "In Anbetracht dessen stellt der Chatbot (lediglich) ein technisches Mittel dar, dessen sich die Beklagte zur Kommunikation mit potentiellen Kunden/Patienten bediente und über das sie hinreichende Steuerungsgewalt besaß." (The chatbot is merely a technical means the firm used to communicate with customers, over which it had sufficient control.) [quote; translation mine]
- Para 71: the "Black-Box-Problem" does not change the result; the chatbot does not differ in law from the contract-document generator in BGH I ZR 113/20 (2021). [paraphrase]
- Para 73: the use of AI, including chatbots, constitutes commercial acts "seines Betreibers, weil dieser hinreichenden Einfluss auf das System hat und es in Gang setzt" (of its operator, because the operator has sufficient influence on the system and sets it going), consistent with art. 2(d) of the Unfair Commercial Practices Directive. [quote; translation mine]
- Para 77: the AI chatbot is not a third party; the firm is liable for its own infringement, not for a duty of care over a third party's. [paraphrase]
- Para 104: the firm's claim that consumers know chatbots err and need a fact-check rests on no rule of experience; "Vielmehr trifft es zu, dass ein Großteil der angesprochenen Verbraucher in besonderer Weise auf die Richtigkeit der computergenerierten Antwort vertraut, da Maschinen im Allgemeinen als weniger fehleranfällig als der Mensch wahrgenommen werden." [paraphrase; quote]
- Para 118: leave to appeal (Revision) granted for fundamental importance. [paraphrase]

## Critical notes

- Limits: unfair-competition law, injunctive relief only; no damages for any individual, no finding on contract or tort, and the decision concerns a chatbot's statements, not an agent's transactions. A first-instance judgment of a regional appellate court; the court itself granted leave to appeal, and the "rechtskräftig" marker suggests no appeal was lodged (not checked further). The secondary report that led here dates its final status to 30 Sept 2026 (not verified).
- Relation to `moffatt2024air`: same result in a different legal order (Germany, collective consumer action rather than an individual small claim). Para 104 matches Moffatt para 28's rejection of a duty to double-check, and para 70's ground (operator control shown by its own fix) is a new, design-based reason.
- Strongest use against the paper: existing law already attributes an agent's statements to the deployer and refuses to put the reading burden on the consumer, so the "presumption of reading" pairing (STRUCTURE 3.4, 4.4 "who carries the loss") is weaker for misstatements than the paper says.
- What it leaves standing: the person misled got nothing; standing ran to a listed association, and the remedy was an order for the future. The firm's fix (prompt plus keyword filter) was the firm's alone.
- Person acted on gets: record — no; brake — no; envelope — no; standing — partial (through a qualified consumer association, para 2, § 4 UKlaG); loss cover — no (the EUR 260 goes to the association, Tenor).
- Corrected by V-B-1: source_basis changed from full-text to partial-text, and the Summary's first sentence aligned with pages_read; the card had said both "Read in full" and "skimmed" while pages_read lists paras 88-103 and 105-117 as not read.
