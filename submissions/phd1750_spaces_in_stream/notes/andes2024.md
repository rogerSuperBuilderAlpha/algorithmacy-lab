# liu2024andes: Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services
Full citation: Liu, J., Chung, J.-W., Wu, Z., Lai, F., Lee, M., & Chowdhury, M. (2024). arXiv:2404.16283 (v1 Apr 2024; v2 13 Dec 2024). PREPRINT. | Read: v2 §1–§2.3 and v1 §2 (pp. 1–3) in full; system design and evaluation not read.

Claim: LLM servers deliver tokens faster than users can consume them; a QoE-aware scheduler and client-side "token pacer" improve QoE up to 4.7× or save up to 61% GPU (v2 Abstract).
Key facts with locators:
- Average reading speed estimated at 4.8 tokens/s and speaking at 3.3 tokens/s, converting words to tokens at ~1.3 tokens/word (v1 §2.1; v2 Fig. 2, Fig. 4 caption). This is an AVERAGE, which the authors use as a target delivery speed — not a "biological ceiling".
- Reading speed by age (v1 Table 1): 18–24 236 WPM; 25–44 200; 45–54 192; 55–64 185; 65+ 175. Age shares are population shares, cited to a secondary web source.
- "32% dropout rate if the response takes longer than three seconds" — v1 §2.1, citing [6], a web-statistics source, about web applications generally, not LLMs.
- v2: vLLM average TDS 11.2 tokens/s on a real trace (§2.2).
NOT in either version: "238 WPM overall", "200 WPM nonfiction / 260 WPM fiction" (the packet attributes these to Liu et al.).
Cited by me for: server delivery outruns average reading speed; delivery pacing is a design choice.
