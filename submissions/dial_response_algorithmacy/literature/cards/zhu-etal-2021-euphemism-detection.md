---
citekey: zhu-etal-2021-euphemism-detection
authors: Zhu, W., Gong, H., Bansal, R., Weinberg, Z., Christin, N., Fanti, G., & Bhat, S.
year: 2021
title: "Self-supervised euphemism detection and identification for content moderation"
venue: "42nd IEEE Symposium on Security and Privacy (S&P), 229–246"
doi: 10.1109/SP40001.2021.00075
url: unknown
verified: verified
found_in_runs: ["Algospeak/gig-worker coordination"]
supports_sections: ["4.8"]
needs_full_copy: false
---

## Summary
Names the arms-race dynamic explicitly: banning a euphemism only prompts the group to coin another, so the detector trails the code. Builds self-supervised methods that recover euphemistic usage and its hidden referent from context — the vendor's side of the loop.

## Relevance to draft.md
NEW SUPPORT for §4.8's "one version behind" sentence, WITH AN IMPORTANT DIRECTIONAL CAVEAT: this paper argues the MODERATOR is one step behind the community, the OPPOSITE causal direction from draft.md's current phrasing ("the protocol the community ships is always one version behind the rule it ships over"). If cited, either adopt this paper's direction or mark the inversion deliberately — a reviewer who knows the paper will notice.

## Key facts / candidate quotes
- Framing (paraphrased): in the arms race between moderators and evaders, banning a euphemism only prompts a new one, so the detector trails the code.

## Verification notes
Confidence: high on the citation, high on the direction-mismatch flag.
