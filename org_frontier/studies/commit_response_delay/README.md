# Commit→response delay (agenda #10)

Fixed transport delay between mediator commit and party response.
Buffer pipeline primary; lagged-read construction check. Exact IIT-4.0.

## Run

```
python org_frontier/studies/commit_response_delay/analyze_delay.py
```

## Result in one line

**DELAY_CORE_SHIFT** — buffer stays triadic with shifting core; lagged
read disagrees at d=2; ≠ #9 sticky-{S} factorization.
