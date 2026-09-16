# Discriminant scale-blur (#42)

Do omit cycle-type discriminants stay sharp as n grows, or does scale blur
them (within-class Φ mixing)?

## Run

```
python org_frontier/studies/discriminant_scale_blur/analyze_blur.py
```

## Result in one line

**SCALE_MORPHS.** Purity holds at n=5 and n=6; law morphs singleton→band;
not blur.
