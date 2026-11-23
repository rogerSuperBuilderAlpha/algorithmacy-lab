# Experiment backlog after update_order_quorum

1. **Random asynchronous update, exactly.** Needs a non-conditionally-independent TPM; the per-node
   marginal is `lazy_update`'s `all`, λ = 0.75 (OR3 whole Φ 0.195650).
2. **Two at a time.** Partial synchrony: S with one party, then the other two.
3. **Order with mediator noise**, scored on the conditionally independent projection, with the residual
   reported (the `continuous_time_invariance` method).

None of these had been started when PR #927 was opened.
