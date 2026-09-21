# PR #739 package — arcs on `cursor/triad-template-census-6ac4`

Merge-ready inventory for
[PR #739](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/pull/739)
→ `contrib`. Exact IIT-4.0 Φ throughout (binary stock pin unless noted).
In-silico; validation gap stated in each FINDINGS. No Hegel/Substack.

**Do not merge from this note** — packaging and human gate only.

## Instrument

| piece | status |
|---|---|
| Stock `feature/iit-4.0` | binary exact Φ (default) |
| `third_party/pyphi_iit4_mv` M1 | SBS-native ExplicitTPM ingest **green** |
| `third_party/pyphi_iit4_mv` M2 | exact multivalued Φ **green** (binary regression Φ=2) |
| Overlay subset Φ | caveat: dyadic inflation on XOR (optional M3) |

## Closed arcs (one-line verdicts)

| arc | spine | verdict |
|---|---|---|
| Residual → cascade | [`foundations/RESIDUAL_AND_CASCADE.md`](../foundations/RESIDUAL_AND_CASCADE.md) | Holistic residual widens then holds (~9% n=5); margin cascade B=10% is lab default |
| Topology / interiors | studies under #15–#20 | Hierarchy WIN; spanning multi-hub WIN; small-world PICK_ONE; ring–pool NO_INTERMEDIATE_LAW; random coupling DISCRETE_LANDMARKS / PARTIAL_N5 |
| Omit-atom | [`OMIT_ATOM_ARC.md`](OMIT_ATOM_ARC.md) | Discrete motif-ruled Φ; size morphs rule form (**SCALE_MORPHS**), not continuum |
| Role-target grain | [`ROLE_TARGET_GRAIN.md`](ROLE_TARGET_GRAIN.md) | ROLE_TARGETS / Z_TARGETS / JOINT_TZ purify MIX indegs |
| Construct × ladder | [`CONSTRUCT_LADDER_ARC.md`](CONSTRUCT_LADDER_ARC.md) | COMMIT_READ + monotone Φ=n−1 flip; gate regimes seal (**GATE_SEAL_HOLDS**) |
| Estimation | [`ESTIMATION_ARC.md`](ESTIMATION_ARC.md) | Topology bottleneck; MI fast within family; AL_NO_GAIN; **#24 HIDDEN_COLLAPSE_INTERMITTENT_CLIFF**; lane closed |
| Stoch–temporal | [`STOCH_TEMPORAL_ARC.md`](STOCH_TEMPORAL_ARC.md) | p\*=0.5 smooth decay; construction decides time factoring; lane picture closed |
| Formal theory | [`FORMAL_THEORY_ARC.md`](FORMAL_THEORY_ARC.md) | #47–#50 done (**PARTIAL_PROOFS** / **NORMALIZED_CUT** / **NOT_UNIQUE** / **LATTICE**); lane closable |
| AI / multi-agent | [`AI_MULTIAGENT_ARC.md`](AI_MULTIAGENT_ARC.md) | Membership cuts transfer; displacement sharp; structure≠learnability; lane closable |
| Political economy | [`POLITICAL_ECONOMY_ARC.md`](POLITICAL_ECONOMY_ARC.md) | Encoding decides conflict; CO_EJECT_TO_OWNER; lane closable |
| Beyond-binary | [`BEYOND_BINARY_ARC.md`](BEYOND_BINARY_ARC.md) | #1–#4 on mv pin M2; **BLINDSPOT_SURVIVES_RADIX**; science closable (optional M3) |
| Construct validity | [`CONSTRUCT_VALIDITY_ARC.md`](CONSTRUCT_VALIDITY_ARC.md) | #43–#46; labels fail/cut across; intensity tracks class; law needs strong model; **lane closable** |

## Agenda map (RESEARCH_AGENDA_50_V2 on this PR)

Closed science cells include A #1–#4, B #5–#14 (stoch–temporal), topology #15–#20, estimation #21–#25, PE #29–#36, AI #37–#41, omit/construct scale #42, CV #43–#46, formal #47–#50. Open curiosities (not blockers): optional M3 subset-Φ fidelity; optional deep MARL.

## Residual risks (not science reopen)

1. **CI wall-clock.** PR reproduce selects ~89 non-slow checks (no shared-infra trigger). 60m timed out; workflow budget raised to 180m on this packaging commit — confirm green before merge.
2. **Overlay subset Φ** inflated on binary XOR dyads — do not claim pure-HO at k>2 from overlay subsets without M3.
3. **Mega-PR review load.** ~160 commits / many studies; prefer squash or carefully reviewed merge commit (human choice).
4. **Nightly full manifest** still the backstop for untouched slow checks.

## Test plan (pre-merge)

```
python ci/reproduce.py --changed-file <(git diff --name-only origin/contrib...HEAD)
# or rely on GitHub Actions reproduce-the-numbers after push
python tools/build_map.py --check
python tools/build_index.py --check
python org_frontier/research/build_research_index.py --check
```

Spot-check closed arcs via their spine reproduce blocks (each `*_ARC.md`).

## Human decisions (explicit)

| decision | options | note |
|---|---|---|
| Merge PR #739? | yes / no | Agent must **not** merge |
| Merge style | squash vs merge commit | Squash collapses ~160 commits; merge preserves history |
| Approving review | required (`REVIEW_REQUIRED`) | One approving review per branch protection |
| CI | wait for reproduce green after 180m budget | update-directory already green historically |
| Follow-ups | M3 overlay; empirical/survey | Outside this PR’s science scope; #24 closed on follow-up branch |