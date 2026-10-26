# Flags: *Organization Science*, AI-Enabled Frontiers

[DRAFTED by Claude, 26 Oct 2026. Cautions kept out of the prose.]

1. **Due 1 Nov 2026,** with three parts: a proposal, a technical appendix and an anonymized repository. The editors' FAQ says "just send us an email" for slight lateness. Do not rely on that.
2. **Anonymity versus the public repo.** algorithmacy-lab is public under the author's GitHub name. The submission needs an anonymized copy (for example an anonymous mirror) with no author names and no commit history. This is the largest practical obstacle.
3. **Fit is low to moderate.** The call is about AI as a research method, not AI as a topic. The proposal only fits if the AI-assisted pipeline and the case-to-model module are the contribution. A paper about algorithmacy does not fit.
4. **Do not claim live LLM-agent probes.** The lab's AI and multi-agent arc uses "in-silico Boolean / tabular / small neural proxies (not live LLM calls...)" (`org_frontier/AI_MULTIAGENT_ARC.md`). The AI in this proposal is the research pipeline (`question_pipeline.js` uses `agent()` calls) and the proposed case-to-model module.
5. **Numbers:** 24 of 256 triadic is in `ci/reproduce.json` (checks 303 and 503). The proxy rank-AUCs (0.563 and 0.629) are in `org_frontier/proxy_bridge/FINDINGS.md` and have **no CI check**. Add one before the appendix cites them. The best-threshold accuracy for the whole-minus-sum proxy is 0.778, so "near chance" refers to rank-AUC only.
6. **Dissertation spine:** Φ is presented as a principled instrument. Nothing here calls it decorative or unnecessary. The limits stated are encoding sensitivity and the validation gap.
7. **The INFORMS PDF was not read.** Format details come from the editors' Substack posts.
