# AI-slop tells, 2026 merge — checklist for the 2026-07-22 panel

Built 2026-07-22 from: Wikipedia's "Signs of AI writing" (the actively maintained editors' guide,
the strongest single source), Decrypt's five-tells analysis (with persistence claims), the
copyadscontent 32-signs list, and TechCrunch/NPR/Forbes coverage confirming the Wikipedia guide's
standing. Only tells corroborated by ≥2 sources (or by the primary guide with examples) are
included. Merged with the house style (`~/.claude/writing-style.md`) and the /peer-review
harness Part 2 — entries note which are already covered there and which are new.

A meta-finding worth keeping (Decrypt): **structural habits persist across model generations;
vocabulary tells rot.** "Delve" has already faded; the durable signal is symmetry, neatness, and
negative parallelism. Weight structure over word-lists.

## The checklist

1. **Negative-parallelism family** — "not X, but Y," "not just X — it's Y," "not only… but
   also," "X rather than Y." The Washington Post measured "not just X, but Y" in ~6% of ChatGPT
   messages; Wikipedia splits it into three sub-patterns. *House style covers the family as the
   antithesis machine (budget: well under 5/1k, one per paragraph max); ADD the "not just / not
   only" variants to the mechanical scan.*
2. **Copulative avoidance** — "serves as," "stands as," "marks," "represents," "boasts,"
   "features" where "is" would do. (Wikipedia; kin to the harness's nominalization rule.) *NEW —
   scan for these.*
3. **Undue-significance framing** — "pivotal," "underscores," "testament," "enduring legacy,"
   "marks a shift," "reflects broader trends." (Wikipedia + Forbes.) *Mostly covered by the
   house inflation list; add "pivotal/underscores/marks a shift."*
4. **Rule-of-three / staccato triplet** — decorative triplets, "No X. No Y. No Z." (Wikipedia +
   copyadscontent.) *House style allows triplets that carry distinct analytic weight; flag only
   decorative ones — but in a piece this polished, audit every triplet.*
5. **Metronomic rhythm** — narrow sentence-length variance, every paragraph the same shape,
   "revises compulsively but never improvises." (Decrypt + copyadscontent + Duey: removing
   em-dashes doesn't help because the rhythm underneath is the tell.) *Covered in principle;
   NEW: check quantitatively — sentence-length distribution, paragraph-shape repetition.*
6. **Trailing present-participle codas** — ", creating…," ", highlighting…," ", reflecting…"
   bolted onto a claim as unearned synthesis. (Wikipedia "superficial analyses.") *NEW — scan.*
7. **Fake balance / diplomatic symmetry** — "While X is true, Y is also important"; hedged
   both-sides constructions that avoid commitment. (Decrypt + copyadscontent.) *NEW.*
8. **Elegant variation** — cycling synonyms to avoid repeating a term the argument should
   repeat. (Wikipedia.) *NEW. Note the false positive: repetition-avoidance is also drilled
   into human academic writers.*
9. **Vague attribution** — "observers argue," "critics note," "industry reports" without named
   agents. (Wikipedia.) *Covered by the house named-agents rule — the highest-leverage fix.*
10. **Ta-da openers and canned closers** — "Here's the thing," "In conclusion," "Ultimately,"
    prompt-restatement openers, "Remember…" closers. (copyadscontent + Decrypt.) *Partially
    covered by banned openers; add the closers.*
11. **Verb cosplay** — leverage, harness, unlock, empower, elevate. (copyadscontent; kin to
    house inflation list.) *Scan.*
12. **Boosters without data** — "significantly," "substantially," "dramatically" unanchored.
    (copyadscontent.) *NEW.*
13. **Emotional flatness / uniform sentiment** — no abrupt modulation, unfailingly gracious
    concessions. (Decrypt.) *Judgment call, not scannable; panel's general reader owns it.*
14. **Evolving-vocab watch** — "delve" era over; current risers per Decrypt: "core," "modern."
    Treat word-lists as perishable; structure endures.

## False-positive cautions (all sources + harness Step 0)

- **Em-dashes are not a tell** (copyadscontent devotes its "one that isn't" to this; Duey calls
  removal cosmetic). The house style agrees: cut only the paired dash-parenthetical crutch.
- Wikipedia's own guide: no single sign proves AI authorship; combined signal only; humans
  detect at chance; LLM patterns are bleeding into human prose.
- This chapter's protected text (harness Step 0): quoted material, accepted-abstract verbatim
  lines (e.g., "Cities do this. Matchmakers do this. Apps do this." — the author's own voice,
  already once false-flagged), and the piece's few signature lines. Flags on these are
  auto-declined.
- First person, contractions, questions-answered-in-stride are the piece's deliberate register
  (see `style_models.md`), not slop.

## Sources

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- https://decrypt.co/348923/5-biggest-tells-something-written-ai
- https://copyadscontent.com/signs-of-ai-writing/
- https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/
- https://www.npr.org/2025/09/04/nx-s1-5519267/wikipedia-editors-publish-new-guide-to-help-readers-detect-entries-written-by-ai
- https://www.forbes.com/sites/jodiecook/2025/09/08/the-10-giveaway-signs-of-ai-writing-wikipedia-reveals/
