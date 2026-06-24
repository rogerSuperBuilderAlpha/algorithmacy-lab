# q176 — The pass-through flip and the rule the verdict is most sensitive to

A coded account of a worker-system-counterpart coordination names a Boolean determination
rule for each party. The system rule carries one decision that matters for the structural
verdict: whether the system COMMITS (S = D & R, acting only when the worker decision and
the counterpart request both hold) or RELAYS (S = D, passing the worker decision through).
Switching commit to relay is the pass-through flip. This study asks whether the flip moves
the verdict from triadic to dyadic, and whether the commit-vs-convey bit is the single
rule the Phi verdict is most sensitive to under coder disagreement.

## Method

The study reuses the field bridge `org_frontier/field/rule_to_phi.py`. `rule_to_phi`
encodes the per-party rules into a TPM and reads the exact IIT-4.0 Phi verdict;
`phi_ci` propagates coder disagreement into a bootstrap-t Phi interval. Phi is not
reimplemented.

For H1, a basis family of 25 worker-counterpart accounts is read under a committing
system; the 15 that read triadic are re-read under pure relay. For H2, five synthetic
accounts each give every party a set of plausible coder readings, with the system always
carrying the commit / relay / store ambiguity. A coder panel splits across one party's
readings while the others hold consensus, and the induced Phi-CI width is attributed to
that party. The reported statistic is the median system share of CI width.

## Results

H1 is refuted. Of 15 accounts triadic under commit, pure relay flipped 4 to dyadic and
left 11 triadic, a flip rate of 0.267. The null holds: relaying does not guarantee a
literacy pipe. The accounts that survive share a worker-counterpart cycle that bypasses
the system, so the structure stays irreducible without routing through the system.

H2 is supported. The system's commit-vs-convey ambiguity drove the entire induced CI
width in all five accounts; the worker and counterpart ambiguities induced zero width.
Under a committing system, no worker or counterpart reading changed the verdict. The
median system share is 1.000.

The commit-vs-convey bit is the rule the classifier tracks: it carries the verdict's whole
sensitivity to coder disagreement. Coding it as a relay is necessary to certify a literacy
pipe but not sufficient, because a worker-counterpart cycle can keep the verdict triadic
on its own.

## Scope

Synthetic coded rule sets with known structure, not measured worker states. The empirical
arms report results on synthetic data. Whether a coded account matches an observed
coordination is a separate question this study does not address.

## Run

    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
      python -m org_frontier.questions.q176_passthrough_flipper.probe_passthrough_flipper
