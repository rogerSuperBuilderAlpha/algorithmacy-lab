# Noise × composed carriers (V3 #12)

Does party-vs-mediator flip-noise still share p\*=0.5 on a composed
necklace or shared-mediator span?

**Verdict: SAME_PSTAR_COMPOSED** — hub3, shared_k2, and necklace all
collapse at p\*=0.5 for both seats.

## Run

```
python org_frontier/studies/noise_composed_carriers/analyze_noise_composed.py
```

(default loads committed sweep; `--rebuild` ~8 min)

## Result in one line

V2 #7’s shared coin-flip threshold survives necklace and shared-mediator
composition; seats do not split under these carriers.
