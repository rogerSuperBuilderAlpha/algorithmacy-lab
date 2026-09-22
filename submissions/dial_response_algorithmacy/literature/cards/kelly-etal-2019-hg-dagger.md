---
citekey: kelly-etal-2019-hg-dagger
authors: Kelly, M., Sidrane, C., Driggs-Campbell, K., & Kochenderfer, M. J.
year: 2019
title: "HG-DAgger: Interactive Imitation Learning with Human Experts"
venue: "2019 IEEE International Conference on Robotics and Automation (ICRA), 8077–8083"
doi: 10.1109/ICRA.2019.8793698
url: unknown
verified: verified
found_in_runs: ["AV trust calibration"]
supports_sections: ["4.7"]
needs_full_copy: false
---

## Summary
A DAgger variant where the human expert chooses when to seize control; the policy is trained on the intervention segments, additionally learning a safety threshold on a model-uncertainty risk metric. Literature descendants: MEGA-DAgger, MILE, interactive-imitation-learning surveys.

## Relevance to draft.md
NEW SUPPORT AS MECHANISM, not industry fact — establishes that intervention-as-training-data is a real, standard ALGORITHM, without claiming any particular company deploys it fleet-wide on consumer data. The honest citation if §4.7 wants to assert the mechanism exists, rather than that Tesla/Waymo specifically does this to ordinary drivers.

## Key facts / candidate quotes
- None directly quoted; mechanism (train on human-intervention segments plus an uncertainty-based safety threshold) summarized above.

## Verification notes
Confidence: high.
