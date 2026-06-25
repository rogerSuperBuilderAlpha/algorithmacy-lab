---
citekey: mosnar2025revisiting
title: Revisiting Algorithmic Audits of TikTok: Poor Reproducibility and Short-term Validity of Findings
authors: Mosnar, Matej and Skurla, Adam and Pecher, Branislav and Tibensky, Matus and Jakubcik, Jan and Bindas, Adrian and Sakalik, Peter and Srba, Ivan
year: 2025
doi: 10.1145/3726302.3730293
arxiv: null
journal: 
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2504.18140
sha256: f45f3b449f3deda62c5585ed0f523070694297da75752014a87e75fe6d4dbbdb
pdf_path: literature/pdfs/mosnar2025revisiting.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how reproducible and generalisable existing sockpuppeting algorithmic audits of TikTok's recommender system are when re-run after several years and extended to additional countries. The authors reproduce and extend prior audits—primarily Boeker and Urman (2022) and Vombatkere et al. (2024), partly Mousavi et al. (2024)—using agent-based bots that interact with the For You page through TikTok's web interface, testing personalisation factors of location, watch duration, liking, and following across scenarios run in January–February 2025. They report severe reproducibility problems stemming both from the original studies (unreleased/incomplete code and data, under-specified methodology) and from the platform itself (constantly evolving content, changing HTML structure, more ads and livestreams, active anti-bot banning). They find that audit findings have only short-term validity: contrary to the reference studies, the watch (implicit) action is now the strongest personalisation factor while like and follow show a strong early-exploration phase. They further show findings flip with small changes in evaluation metric or bot simulation, and that explicit actions (like, follow) often do not appear in GDPR-requested data when taken through the web interface, biasing results. They release their code and data and advocate for reproducible, longitudinal, multiplatform audits with more authentic user simulation.

## Key facts it relies on
- Reproducing the prior audits cost roughly 9 person-months over a 5-month period; the audit re-run came more than 3.5 years after the reference study by Boeker and Urman [4].
- The audit defined scenarios mapped to personalisation factors: none [S0], location (Germany, France, Romania, Ukraine; [S1]-[S4]), watch duration ([S5]-[S11]), liking ([S12]-[S14]), and following ([S15]-[S16]); each scenario ran 4 runs/sessions with a ~1-day break between runs, with a paired control user (USA) and a personalised user.
- Default scenario: bots used incognito Chrome via the nodriver library, set to English/USA via proxy, scrolled through 250 videos watching each for 100% of duration or up to a 120-second cap, whichever shorter.
- Evaluation used only heuristics (no annotation): video play count (popularity) and hashtag-based similarity (Jaccard similarity and a more lenient "basic match" similarity that counts videos as similar if they share at least one hashtag or substring).
- Noise control ([S0]): average Jaccard similarity between two concurrent bots' feeds was only ~10% (single-user similarity stayed ~20%); average similarity between control users across scenarios was 11% (range 2%–28%), versus 35% in Boeker and Urman [4], indicating recommended-video diversity increased over ~3 years.
- Location had a strong effect: Jaccard similarity among USA control users was 25–38%, while personalised-user similarities were an order of magnitude lower; under the lenient basic-match metric control similarity was ~80–90% and personalised/control ~65%, showing the metric choice can skew findings.
- Watch was found to be the strongest personalisation factor, followed by follow; like gave a signal only with defined interests (random like showed strong exploration)—contrasting the reference studies [4, 28] which found follow most impactful and watch only as strong as like.
- For predefined-interest scenarios, ~36% of videos contained at least one interest hashtag (vs. 6% containing a target creator), consistent with Vombatkere et al.'s 30–50% range [28]; the like action showed early exploration then strong exploitation after ~1000 videos.
- Watching beyond 100% (e.g., 200%) only slightly increased personalisation, but 400% watch duration produced a strong personalisation increase—contrasting reference studies that found watch time above 75% gave no significant increase.
- Platform anti-bot effects: ~1 in 20 videos were livestreams and ~1 in 4 were ads; 5 bots were banned near the end and 15 more accounts banned after the study (mostly implicit-action scenarios); Italy's banning was so fast it prevented running the audit there.

## Critical notes from the literature
- The authors flag hashtag-based metrics as their most significant limitation, noting that the choice of metric and its strictness strongly affect (and can flip) findings, and that the generic hashtag set used to define interests may itself skew results; both were inherited from the replication character of the work.
- A key validity caveat the paper raises: explicit actions (like, follow) often did not appear in GDPR-requested data when performed through the web interface (matching non-bot web behaviour), implying the recommender may ignore them on web and that audits may need the mobile app; the follow action did not work on the web interface even for non-bot accounts.
- TikTok flagged some bots as suspicious and could not complete all 4 repeats (e.g., the Germany location user), so some scenario findings rest on fewer collected videos and may be biased; a problematic proxy setup (proxies not actually located in the indicated country) may have contributed to banning.
- The paper frames audits as needing a paradigm shift away from ad-hoc, single-shot studies toward reproducible, longitudinal, multiplatform audits with more authentic user simulation, noting the original works released incomplete/inaccessible code (Vombatkere et al.'s repository was inaccessible; Boeker and Urman's code was missing fundamental parts such as the database schema).

## Key topics covered
Algorithmic auditing; sockpuppeting audits; TikTok recommender system; For You page personalisation; reproducibility and generalisability; short-term validity of findings; implicit vs. explicit feedback (watch, like, follow, location); exploration vs. exploitation; Jaccard and basic-match hashtag similarity; video popularity/play-count metric; Digital Services Act (DSA) Article 37/40, Recital 83; GDPR data donations; anti-bot banning and platform evolution; metric-dependence of audit findings.
