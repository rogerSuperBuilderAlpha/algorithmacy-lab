# xiaoyang2025: Streaming, Fast and Slow: Cognitive Load-Aware Streaming for Efficient LLM Serving
Full citation: Xiao, C., & Yang, B. Z. (2025). ACM DOI 10.1145/3746059.3747721 (UIST '25 per DOI prefix — venue to confirm in audit); arXiv:2504.17999v2. | Read: full text body §1–§6 (arXiv v2).

Question: Can streaming speed be modulated by the estimated cognitive load of content to save compute while keeping speed above users' reading speed? (§1)
Claim: Slowing complex segments and speeding simple ones saves compute at a given "Streaming-Reading Alignment Rate" (SRAR) (Abstract; §5.2).
Method: Pilot N = 100 Prolific (79 valid) with PEST procedure to find comfortable streaming speed for an easy vs complex passage (§3.2); main study N = 200 Prolific, 10 GPT-4o passages, 150–200 words, 6 per participant, two-choice comprehension check (§5.1). Simulation of compute savings.
Key results:
- Comfortable speed lower for complex passage, t(78) = 11.81, p < .001 (§3.2).
- 99th percentile comfortable speed 21.20 WPS (simple) vs 11.97 WPS (complex); vs ~45 WPS GPT-4o API speed → 63.14% compute saving at 99% SRAR (§3.2).
- LLM-estimated load correlated with median comfortable speed r = 0.955; Gunning-Fog r = 0.828 (§5.2).
- At SRAR .95: 10.33% (Gunning-Fog) and 16.79% (LLM) savings (Table 1).
Assumption stated: "streaming content faster than a user's reading speed does not enhance the experience" (§3.1, citing [1]).
Limitations: simulation; linear allocation assumption (§4.3, §6).
My concerns (mine): no eye tracking, no measure of regressions or decisions; comprehension check is a filter, not an outcome.
Cited by me for: background that stream pacing is set by compute, not reading — "this shift transforms text from a static payload into a dynamic, time-based medium" (§1). Supports Roger's framing that the display updates autonomously.
