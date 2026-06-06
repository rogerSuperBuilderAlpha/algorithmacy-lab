# Q73 — Stage 4 methods (fixed before re-derivation)

One probe (`probe_law_pillars.py`) re-derives pillars P1-P4 from keystone forms with exact IIT-4.0 Φ
(`classifier.classify_rules`, `probes.lib.major_complex`); P5 is carried from Q71 (noise robustness) and
Q72 (proxy frontier), each CI-backed. Keystone forms: read_recipient, broadcast, one_shot (n=3),
all_required, substitutable (n=4), closed ring (n=4). Run on `~/iit-playground/venv-4.0/bin/python`.

## Decision rule

The law's pillars hold iff: P1 read_recipient triadic and broadcast dyadic; P2 read_recipient triadic and
one_shot dyadic; P3 all_required triadic and substitutable dyadic; P4 the ring's major complex is the full
set at Φ > 2.0. P5 holds by the registered Q71 and Q72 checks. Q73 is confirmed iff P1-P4 all hold.
