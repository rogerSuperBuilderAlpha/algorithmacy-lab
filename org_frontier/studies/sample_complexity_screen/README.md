# Sample complexity of the cheap screen (agenda #23)

How long a trajectory does mean-pairwise-MI (#122) need to hit AUC≥0.90?

## Run

```
python org_frontier/studies/sample_complexity_screen/analyze_complexity.py
```

## Result in one line

**FAST_WITHIN_FAMILY** — family n=3 T*_MI=125; noise does not raise T*;
cross-topo MI never hits 0.90 at any T (#134).
