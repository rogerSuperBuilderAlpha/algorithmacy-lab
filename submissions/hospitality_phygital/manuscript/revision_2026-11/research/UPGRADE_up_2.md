# Full-text upgrade — up_2 (rr-2026-11, 2026-11-08)

All 13 PDFs are the right works and all are versions of record. Every card is now
`read_depth: full-text`, with journal-page locators and a verdict section. I changed no `status`.
`library/build_index.py --check` passes every card check; it fails only because CARDS_INDEX.md is
now stale, and I did not regenerate it, since the brief limits me to the cards and this report.

## Per card

| card | version read | verdicts changed |
|---|---|---|
| vaccaro2020contesting | ACM VoR, PACM HCI 4(CSCW2) Art. 167, 22 pp. | v4 lines 41, 60, 86 → PARTLY; WS_B gloss → PARTLY |
| yurrita2025needs | ACM VoR, PACM HCI 9(7) Art. CSCW234, 29 pp. | line 67 → PARTLY; "precondition" fact corrected; new support for the 4th principle (p. CSCW234:16) |
| hirsbrunner2025contestation | Frontiers VoR, 10:1638257, 15 pp. | line 67 → PARTLY; "found" corrected to "argued"; two author names fixed |
| sterz2024effectiveness | ACM VoR, FAccT '24 pp. 2495–2507, 13 pp. | line 66 → SUPPORTED (core); "institutional-not-trainable" limited |
| lin2025oscillation | Sage VoR, SM+S 11(1) pp. 1–13 | line 60 → PARTLY; author given name fixed (Hui) |
| ytrearnemoe2021folk | Sage VoR, MCS 43(5) pp. 807–824 | line 58 → PARTLY; debt paid; `abstract-only-debt` removed, `swap-candidate` added |
| rahman2021cage | JSTOR copy of VoR, ASQ 66(4) pp. 945–988 | lines 31, 34 → SUPPORTED; summary corrected |
| pedersen2022 | OUP VoR, JPART 33(1) pp. 80–93 (2023) | line 31 → SUPPORTED; year field set to 2023; well-being claim not in source |
| padigar2024friction | Wiley VoR, P&M 42(1) pp. 21–43 (2025) | line 72 → PARTLY; negotiation gloss contradicted; year field set to 2025 |
| mohlmann2021algorithmic | MISQ VoR, 45(4) pp. 1999–2022 | line 36 → PARTLY; v4 still cites a source the card calls cut |
| jianu2025 | Elsevier VoR, IJHM 129 Art. 104168, 14 pp. | line 33 → NOT SUPPORTED (`claim-contradicted` added); lines 31, 59 → PARTLY |
| schmidt2025field | Wiley VoR, Strategic Change 34(4) pp. 559–575 | line 55 → SUPPORTED (gloss noted); design is self-selection; two author names fixed |
| pigac2026transparency | Sage VoR, CHQ 67(3) pp. 283–297 | line 65 → PARTLY; "transparency only" fact overturned; two author names fixed |

## For the authors

Ranked by how much the argument leans on each item.

1. **Vaccaro et al. 2020 carries the competence/standing hinge and the accountability null, and it supports neither fully.** Lines 60 ("Knowing how to file an appeal is not the same as having a right to an answer"), 86 ("individual skill cannot create institutional rights, authority, or responsibility") and 41 ("A perfectly transparent algorithm can still replace hospitality …"). The study varied neither skill nor transparency: every condition carried the same explanation (p. 167:7), and opacity was a top complaint (n = 113, p. 167:13). The authors read their own null as a design failure: "most of the lack of effect should be attributed to poor appeal design" (p. 167:15). They also note that appeals currently favour "users who understand the systems better" (p. 167:17). Their "perceived illegitimacy" passage (p. 167:16) is the nearest support for the structural reading. The no-lift result itself stands (Table 2, p. 167:11).
2. **Lin 2025, line 60, "it is the hinge of the paper":** "Users who understand a platform's curation well still cannot bend it." Users did bend non-political curation: "Every time I pressed dislike, the relevant content was reduced" (p. 9). What holds is that resistance "remains predominantly confined to the dominant use of technological affordances" (p. 11). A tighter wording is suggested on the card.
3. **Jianu et al. 2025 is a forecasting Delphi, not a description of practice.** It aims "to gauge consensus about the future implications of AM" (p. 4); 9 of 22 recruits are academics (Table I, p. 4). Line 33, "the managers who run such desks describe a running negotiation …", is NOT SUPPORTED, because pricing appears only in the literature review (p. 3). Lines 31 and 59 ("translating those decisions for the people they affect"; "hotel managers describe carrying the system's decisions") are PARTLY: the translation runs to frontline staff, "to explain and justify otherwise opaque algorithmic decisions to frontline staff" (p. 10), not to guests. The plan's fallback "keep Jianu 2025 as the hotel evidence" over Spektor 2023 would swap observation for forecast.
4. **Yurrita et al. 2025, line 67:** "A hotel that responds … by offering guests more education has misdiagnosed itself." PARTLY. The paper supports "correcting AI's mistakes is not the decision subject's responsibility" (p. CSCW234:18), but it also prescribes literacy-tailored explanations and third-party help (pp. 17, 21). The system was never deployed (p. 6). The same paper can help the fourth principle, where Fable found Yurrita 2023 weak: "AI was seen as unable to change the output. Humans … could" (p. 16).
5. **Pigac et al. 2026, line 65:** "explain a decision where it lands." PARTLY. Guests wanted "minimal disclosure during check-in; richer, retrospective transparency in loyalty apps" (p. 286), as in "Tell me later when I'm curious" (p. 291). The card's premise that Pigac lacks adjustability and bypass is wrong. "Systems that allowed concierges to override or explain AI decisions were described more positively" (p. 291), so the "what the framework adds" argument must meet an override it treats as a trust device.
6. **Padigar et al. 2025, line 72:** keeping "moments where recognition, negotiation, and exception stay possible." PARTLY. The paper never discusses negotiation. It classes contacting customer service "when there is a problem" as low-value friction to reduce (p. 32).
7. **Hirsbrunner et al. 2025, line 67 ("constitutional conditions …"):** PARTLY. The paper says contestants "must be competent to contest" (p. 3), and its designer/community contrast is argued, not found (p. 11). The plan already cuts it.
8. **Ytre-Arne and Moe 2021, line 58:** "Through repeated encounters they build working theories of how a system behaves." PARTLY. The theories are perceptions of consequences, collected from the 59% who claimed understanding (p. 812). If DeVito and Jhaver leave as planned, the sentence loses its operational sources.
9. **Möhlmann et al. 2021, line 36 ("produce the guest's sense of control"):** PARTLY. The supporting passage is "little flexibility for the driver to adapt to special client requests" (p. 2009). It is a better anchor than Fuller and Smith.
10. **Minor glosses.** Line 31's "more and more of their day" is not measured in Pedersen and Pors (p. 89 supports the workarounds). Line 55's "because little is at stake" is the authors' gloss; Schmidt et al. say "clear functional boundaries" (p. 571), and guests chose their agent. Line 66's "source of accountability" goes beyond Sterz et al., who analyse risk mitigation, though "pseudo-options" (p. 2498) carries the core.

**Bibliographic.** v4's reference for Yurrita 2025 lacks the issue and article number (9(7), Article CSCW234). The citekeys `pedersen2022` and `padigar2024friction` still carry the online-first years.
