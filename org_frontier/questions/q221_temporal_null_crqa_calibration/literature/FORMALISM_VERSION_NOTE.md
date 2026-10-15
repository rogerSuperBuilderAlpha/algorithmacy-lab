# IIT formalism-version and prior-art caveat

The pinned Q221 exact-Φ calculations use PyPhi `feature/iit-4.0` at `b78d0e34`, IIT version 4.0 and GENERALIZED_INTRINSIC_DIFFERENCE, as recorded in `GATES.md` and `identifiability/results/rep_verify.txt`.

**Version risk:** [PyPhi's formalism-version documentation](https://pyphi.readthedocs.io/en/latest/theory/formalism-versions.html) distinguishes IIT 3.0, IIT 4.0 (2023), and IIT 4.0 (2026), with potentially different Φ values for the same substrate/state. Do not treat the pinned historical implementation as interchangeable with current PyPhi defaults. Any independent reproduction must state the precise version, commit, config, state selection and target definition.

**2026 reproducibility note:** [PyPhi's 2.0 changelog](https://github.com/wmayner/pyphi/blob/main/CHANGELOG.md) records an October 1, 2026 release with the default IIT-4.0 (2026) intrinsic-information requirement. [The official comparison](https://pyphi.readthedocs.io/en/latest/theory/formalism-versions.html) gives a deterministic XOR example where the 2023 and 2026 system-integrated-information numbers differ. Thus the pinned deterministic Q221 result (Phi=2 under the historical implementation) **must not be transported automatically** to the 2026 default. No independent 2026-formalism rerun of Q221's bottleneck targets is reported. This limits any claim of formalism robustness, but it does not invalidate the historical pinned computation.

**Intervention risk:** The Q221 bottleneck is the *lab's* leave-one-node-out decrease in major-complex Φ. It is not itself a universal IIT construct. Clamp-to-0 and clamp-to-1 sensitivity and value-relabeling equivalence are material.

**Prior-art limits:** IIT's interventional formalism is described by [Albantakis et al. 2023](https://doi.org/10.1371/journal.pcbi.1011465) and [Computing integrated information](https://pmc.ncbi.nlm.nih.gov/articles/PMC6007153/). Comparison of approximate integrated-information measures across network models predates Q221 ([review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7514120/)). Surrogate-data calibration and recurrence-based inference are also established, as documented in `LITERATURE_REGISTER_DRAFT.md`.

The present work may supply a useful **specific exploratory construction**, but source-level novelty of that exact conjunction is not certified. Do not claim a general IIT theorem, new estimator, or theory-independent structural ground truth.
