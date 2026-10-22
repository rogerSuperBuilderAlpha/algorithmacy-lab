# parklee2024: The Effect of Text Movement on Eye Movements in Generative AI Chatbots (생성형 인공지능 챗봇의 텍스트 움직임이 안구운동에 미치는 영향 연구)
Full citation: Park, H., & Lee, Y. (2024). Archives of Design Research, 37(4), 181–197. | DOI: 10.15187/adr.2024.08.37.4.181 | Read: full text (Korean original, aodr.org full-text HTML, via browser 2026-10-20). Based on first author's 2024 master's thesis (Acknowledgments).

Question: How do the "text movement" properties of chatbot output (generation unit/speed, position, direction, scroll focus) affect eye movements? (§1.1, §4.1)

Claim: Text generated at the bottom of the screen (downward with auto-scroll, or upward) produced more fixations, longer total fixation duration and larger saccade amplitudes than text that appears whole at the top; authors recommend generating from the top (§6).

Method: Case analysis of 5 chatbots as of Sept 2023 (ChatGPT-3.5, Bing AI, Bard, Wrtn, YouChat) → 4 movement types (§3.2, Table 5):
- Type 1: top, generates downward (ChatGPT first turn, YouChat, Wrtn)
- Type 2: bottom, generates downward with auto-scroll (ChatGPT continued turn)
- Type 3: bottom, generates upward (Bing AI)
- Type 4: whole text appears at top, no direction (Bard) — used as the comparison resembling static text (§4.2)
Generation unit split between groups: Group A letter-by-letter (slower), Group B sub-sentence chunks (faster); 18 per group, N = 36, ages 20–39 (§5). Explanatory texts of 1,300–1,500 Korean characters on climate change effects on animals, topic differs per type (§4.3). Tobii 3 eye tracker; 50 s generation window (§5.1). RM-ANOVA, Bonferroni, independent t-tests.

Key results:
- Group A omnibus: fixation starts F = 6.474, p = .001; whole fixations F = 5.805, p = .002; total fixation duration F = 11.637, p < .001; saccade amplitude F = 8.563, p < .001; first fixation duration F = 2.624, p = .052 (Table 11). Post hoc mostly a2 > c4 (Table 12).
- Group B: fixation starts b3 > c4; whole fixations b2, b3 > c4; total duration b3 > b1, c4; saccade amplitude b2 > c4 (Table 12).
- First fixation duration on Type 2 higher for letter-by-letter than sub-sentence: 1,538.89 vs 1,255.44 ms, t = 2.206, p = .017 (Table 13).
- Fixation starts concentrated in lower AOIs (area6, area7) for Types 2 and 3, where new text appears (§5.1, Table 9).

Controls: Type 4 (whole text) as quasi-static baseline. No comprehension, regression, or decision measure.
Stated limitations: expository text only; manual scrolling excluded; single age band (§6).
My concerns (mine): topic confounded with type; no comprehension test, so "higher cognitive activity" is inferred from gaze counts only; regressions not reported.

Cited by me for: proposal's sentence "Park and Lee (2024) observed that readers showed more fixations and longer saccades when chatbot text appeared incrementally at the bottom of the screen, rather than all at once." → Consistent with Tables 11–12; the "all at once" baseline was text appearing whole at the top (Type 4). Accurate as written.
