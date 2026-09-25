# Slides 13 and 14 — proposed corrections (NOT applied)

These are proposals for the author, drafted 2026-09-25 with the v4 slides. Nothing here has been applied: `talk/deck.md` and `talk/script.md` still carry the author's slides 13 and 14 word for word, and they stay that way until the author says yes to each row. Each "why" below was re-checked against `ci/reproduce.json` and `CLAIM.md` on 2026-09-25; where the author's wording is true it is kept, and only the false cells change. Applying every row also clears the two `check_talk.py` failures on the undeclared `0.0` (slide 14, row 1), because that cell disappears; the `0.0` that remains on row 3 then needs the NUMBERS.md row listed at the end.

## Slide 13 — deck.md

| current | proposed |
|---|---|
| `### Causal Collapse Theorem (IIT 4.0)` | `### The Causal Test (IIT 4.0)` |
| `**Φ = 0**` | `**Φ = 0** — the system factors: cutting its weakest seam loses nothing.` |
| `**Extensional Dyadic Decomposition Erases System Synergy**` | `**Φ > 0** — the system is a whole: no cut leaves it as it was.` |
| `Forcing multi-input causal mechanisms into dyadic channels matches the partitioned repertoire with the whole.` | `**Wholeness Is Not Yet a Triad**` |
| `Integrated information vanishes under the Minimum Information Partition (MIP).` | `Φ says whether the system factors, not whether any member is set by two others. A ring of one-input copies is a whole at Φ = 2.0.` |

Why. `CLAIM.md` "Do not claim" forbids the "Causal Collapse Theorem" by name (l.70) and the claim that dyadic channels give Φ = 0 (l.69). The record contradicts the current body: a ring of three one-input copies is a whole, `copy_BCA               Φ_MIP=2.000000  core=('A', 'B', 'C')        adicity=2 (cause 2, effect 2)` (`thinkers-peirce-h1-irreducibility`), and so is the mutual dyad, `dyad_mutual ... Φ_MIP=2.000000  core=('A', 'B')` (`thinkers-simmel-h1-superindividual`). The proposed Φ = 0 and Φ > 0 lines are the author's own scissors sentences from the slide 13 script, moved onto the slide; that script section needs no change and is not touched.

## Slide 14 — deck.md table

| row | current | proposed |
|---|---|---|
| 1 | `\| Dyadic Cascade \| 89 Wirings \| Point-to-point lines \| Φ = 0.0 \| No Complex \|` | `\| Dyadic Cascade \| 89 Wirings \| Point-to-point lines \| Φ > 0 in 8 \| No Member Set by Two Others \|` |
| 2 | `\| Dyadic Ring \| Feedback Loop \| Recurrent pairs \| Φ = 2.0 \| Whole Without Synergy \|` | `\| Dyadic Ring \| One of the 89 \| Recurrent pairs \| Φ = 2.0 \| Whole Without a Triad \|` |
| 3 | `\| Uncoupled Triad \| 11 / 30 Systems \| Synergistic gate \| Φ = 0.0 \| Synergy Without Whole \|` | `\| Uncoupled Triad \| 11 / 30 Systems \| Two-input gate \| Φ = 0.0 \| Triad Without a Whole \|` |
| 4 | `\| Integrated Triad \| 5 / 30 Systems \| Teridentity in loop \| Φ = 2.0 \| Genuine Triadic Complex \|` | `\| Integrated Triad \| 5 / 30 Systems \| Two-input gate in the loop \| Φ > 0 \| Genuine Triadic Complex \|` |

Why, row by row.

- Row 1. The 89 one-input wirings are not all Φ = 0: `wirings=89  max genuine adicity=4  adicity counts={2: 11, 3: 66, 4: 12}  whole-irreducible (Φ>0)=8` (`thinkers-peirce-h1-irreducibility`). Eight are wholes, so "No Complex" is false for them. What is true of all 89 is `max cause-side adicity over all=2`: no element is ever determined by two others. "89 Wirings" and "Point-to-point lines" are the author's and stay.
- Row 2. The ring (`copy_BCA`, three copies in a cycle) is itself one of the 89 one-input wirings, not a separate family, so "Feedback Loop" in the count column misleads; "One of the 89" is the record. "Φ = 2.0" is the author's and is true. "Without Synergy" changes because no run measured synergy: the lab ran no PID on any of these forms. The ring lacks a triad in the sense the talk fixes (no member set by two others), which is what "Whole Without a Triad" says.
- Row 3. The 30 four-element forms use two-input gates drawn from AND, OR, XOR, NAND, NOR, XNOR (`peirce/forms.py` `GATES`, `two_input_sample`). AND is not synergistic in the PID sense (the Williams & Beer card, "NOT FOR SLIDES" note: AND under I_min carries about 0.311 bit of redundancy, the carder's arithmetic), so "Synergistic gate" overstates; "Two-input gate" is what was built. "11 / 30" is the author's and is registered: `joint determination with Φ_MIP=0=11` (`thinkers-peirce-jd-full`). "Φ = 0.0" is true for these eleven.
- Row 4. "5 / 30" is registered: `forms=30  joint determination in a whole=5`. "Φ = 2.0" is false for the five as a group: their whole-system Φ runs from 0.207519 to 2.0 (`org_frontier/thinkers/peirce/results/probe_peirce_joint_determination_full.json`, forms `two_input_00`, `_02`, `_14`, `_16`, `_24`; the values are in the results file only and are not CI strings, so print none of them). "Φ > 0" is what the author's own script already says for this row. "Teridentity in loop": `CLAIM.md` l.63 forbids identifying Thirdness with teridentity, and none of the five gates is the teridentity relation (x, x, x). The author may keep "Teridentity" and take the objection at question time; "Genuine Triadic Complex" is the author's and stays.

## Slide 14 — script.md

| current | proposed |
|---|---|
| `Under Partial Information Decomposition (PID), this configuration exhibits pure causal synergy ($\text{Syn} > 0$).` | delete. No PID was run on the control, and for an AND gate under uniform inputs the synergy is not "pure": the Williams & Beer card's note puts about 0.311 bit in redundancy (carder's arithmetic, not for slides). |
| `Testing 89 discrete single-input copy architectures confirms Peirce's valency rule: pairwise connections produce only pairwise distinctions, generating zero triadic mechanisms.` | `Testing 89 discrete single-input copy architectures, no element is ever determined by two others: pairwise connections produce only pairwise determination. Our pre-registered hypothesis was refuted on the effect side, where one element can drive three; the cause-side reading is post hoc.` |

Why. The pre-registered H1 is registered as refuted, `H1 (no complexus of dyads reaches adicity 3): REFUTED`, because 66 wirings reach adicity 3 and 12 reach adicity 4 on the effect side (`copy_DDDA ... D -> cause A effect ABC`: one element drives three). `CLAIM.md` l.79 forbids saying H1 was confirmed and requires the split to be called post hoc. The cause-side ceiling, `max cause-side adicity over all=2`, is what "no element is ever determined by two others" reports. The rest of the slide 14 script, including the control at Φ = 2.0 with all three in the core and the "5 of the 30" and "11 of the 30" sentences, matches the record and is not touched.

## NUMBERS.md rows these changes need

| number | kind | check | expect |
|---|---|---|---|
| 8 | lab result | thinkers-peirce-h1-irreducibility | whole-irreducible (Φ>0)=8 |
| 0.0 | lab result | thinkers-peirce-jd-full | joint determination with Φ_MIP=0=11 |

The `0.0` row also covers the v4 slides (17, 18, 22), which print Φ = 0.0 for the majority triad and the bypassed dealer; the v4 handoff lists the alternative check names.
