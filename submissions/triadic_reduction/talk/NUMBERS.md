# Numbers on the slides and in the script

Every numeral in `deck.md` and `script.md` appears in this table. A row of kind `lab result` names a check
in `ci/reproduce.json` and a substring of that check's expect strings; `check_talk.py` fails if the
substring is not there. The other kinds are dates, loci, arithmetic and names, which cite no lab result.

The rows for 11 and 30 name `thinkers-peirce-jd-full`, registered by the lab addendum (#772).

| number | kind | check | expect |
|---|---|---|---|
| 2.0 | lab result | thinkers-peirce-h1-irreducibility | control conjunctive triad: Φ=2.000000 core=('A', 'M', 'B') adicity=3 PASS |
| 89 | lab result | thinkers-peirce-h1-irreducibility | wirings=89 |
| 2 | lab result | thinkers-peirce-h1-irreducibility | max cause-side adicity over all=2 |
| 0 | lab result | thinkers-simmel-h3-majority | majority_triad         dyadic   Φ_MIP=0.000000  core=() coreΦ=0.000 |
| 11 | lab result | thinkers-peirce-jd-full | joint determination with Φ_MIP=0=11 |
| 30 | lab result | thinkers-peirce-jd-full | forms=30  joint determination in a whole=5 |
| 3 | arithmetic | — | 3 + 3 − 2 = 4 (valency) |
| 4 | arithmetic | — | 3 + 3 − 2 = 4 (valency) |
| 4.0 | name | — | IIT 4.0 |
| 3.144 | locus | — | CP 3.144 (peirce1870description) |
| 1.363 | locus | — | CP 1.363 (peirce1890guess) |
| 1.345 | locus | — | CP 1.345 (peirce1931papers) |
| 8.331 | locus | — | CP 8.331 (peirce1904letter) |
| 1870 | year | — | peirce1870description |
| 1886 | year | — | kempe1886memoir |
| 1892 | year | — | peirce1892critic |
| 1897 | year | — | peirce1897logic |
| 1902 | year | — | simmel1902number1, simmel1902number2 |
| 1908 | year | — | simmel1908soziologie |
| 1915 | year | — | lowenheim1915moglichkeiten |
| 1936 | year | — | kalmar1936zurueckfuehrung |
| 1954 | year | — | quine1954reduction |
| 1981 | year | — | herzberger1981theorem |
| 2006 | year | — | herethcorreia2006teridentity |
| 2022 | year | — | koshkin2022reduction |
| 2025 | year | — | koshkin2025completeness |
| 2026 | year | — | the conference |
| 13 | lab result | thinkers-peirce-jd-full | n=5 isomorphism classes=13  with joint determination=0 |
| 5 | lab result | thinkers-peirce-jd-full | forms=30  joint determination in a whole=5 |
| 1.25 | locus | — | CP 1.25 (peirce1931papers) |
| 1.325 | locus | — | CP 1.325 (peirce1931papers) |
| 1.337 | locus | — | CP 1.337 (peirce1931papers) |
| 1.346 | locus | — | CP 1.346 (peirce1931papers) |
| 2.274 | locus | — | CP 2.274 (peirce1931papers) |
| 1991 | year | — | burch1991reduction |
| 1 | label | — | argument numbering on slides 6–8 |

Added for v3 (2026-09-25). The v3 table on slide 14 prints `Φ = 0.0` for the 89 one-input wirings; the CI
record (`thinkers-peirce-h1-irreducibility`) has Φ > 0 in 8 of them, so `0.0` is left undeclared and
`check_talk.py` fails on it until the author decides (AUTHOR_TASKS.md, v3 item 2).

| 2024 | year | — | koshkin2024reduction |
| 2010 | year | — | williams2010decomposition |
| 1.0 | arithmetic | — | XOR synergy of 1 bit (williams2010decomposition card, the carder's arithmetic, not W&B's printed numbers) |
