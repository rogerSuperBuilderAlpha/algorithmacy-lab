# Claim codebook — best_time_pilot

Each response in `responses.csv` (role = analysis) is coded for the presence (1) or absence (0) of every
claim below, in `claims_coding.csv`. A claim is present when the response asserts or endorses it, not merely
mentions it in passing. The codebook fixes the inclusion rule so a second coder reproduces the matrix.

The column order in `claims_coding.csv` is load-bearing for the analysis and must not change.

## Verdict

- `verdict_present_best` — concludes that the present / today / the early 21st century is the best time for
  the average person's overall quality of life. Inclusion: an explicit overall judgment naming the present,
  not just "today is best for health."
- `verdict_hedged_nobest` — opens by denying a single best era ("there isn't a single best time," "no
  objective answer"). Inclusion: the explicit refusal of one answer.

## Eras endorsed as a candidate "best" for some criterion

One flag per era the response names as the best, or a leading candidate, for at least one value or criterion.

- `era_classical_athens` — Classical Athens (philosophy/democracy).
- `era_pax_romana` — the Pax Romana / Roman Empire peace (27 BCE–180 CE).
- `era_islamic_golden_age` — the Islamic Golden Age (science/scholarship).
- `era_renaissance` — the (Italian/European) Renaissance (art/thought).
- `era_age_of_discovery` — the Age of Discovery / exploration.
- `era_late_1990s` — the late 1990s to early 2000s (post–Cold War optimism).
- `era_post_wwii` — the post–World War II boom, roughly the 1950s–1970s ("golden age of capitalism").
- `era_present_day` — today / the present named as best for at least one criterion (health, technology).

## Framing moves

- `frame_subjective_disclaimer` — states the answer depends on what you value.
- `frame_lists_criteria` — organizes the body around value-criteria (health, peace, culture…) as the
  primary axis. Coded 0 when the body is organized around named eras instead.
- `frame_best_for_whom` — raises that the "best" era depends on who you were (peasant, woman, enslaved
  person, minority), or that golden ages were golden only for some groups.

## Template family (surface layout, documentation only)

`template_family` records the layout family by hand for reference. It is NOT used to test H2 — the
structural clustering in `analyze_variance.py` derives families from text features, and `template_family`
only documents the expected grouping.

- 1 — "For X:" criterion headers, caveat in prose (r1).
- 2 — "If you value X:" conditional framing with a terminal metric→era summary list (r3, r4).
- 3 — named-era "contenders" with dated ranges and a "best for whom?" close (r2).

## PII

The responses arrived by email with real names, one email address, and one phone number. Names are replaced
by `student_1..4`; the email signature blocks are not part of the ChatGPT answer and were dropped. No
personal identifiers remain in `responses.csv`.
