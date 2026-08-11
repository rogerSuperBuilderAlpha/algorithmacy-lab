#!/usr/bin/env python3
"""Scan a draft for the constructions four review panels kept cutting out of it.

Every pattern here was found in a real draft of this chapter and named in
reviews/2026-08-02/11_bans.md, reviews/2026-08-02-panel3/11_bans.md,
reviews/2026-08-01/00_breakdown.md, or research/slop_trends_2026.md. The rate
thresholds are the panels' own measurements, not invented budgets.

The record shows these regrow under revision -- constructions killed in one round
came back in the next, hardest in material no panel had seen. A regex does not get
tired, so it runs after every applied fix rather than once at the end.

Two things this script does NOT do. It does not flag first person, contractions,
em-dashes used as beats, or pointed concessions: those are protected for this
chapter and five reviewers named the concessions its best feature. And it does not
issue verdicts. It reports locators and rates; the judgment stays with the author.

Usage:
    python3 v4/tools/check_bans.py chapter/chapter_v4.md
    python3 v4/tools/check_bans.py chapter/chapter_v4.md --quiet   # rates only
"""
import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------- text handling

def body_of(text):
    return re.split(r"(?m)^##\s*Notes\s*$", text)[0]


def paragraphs(body):
    """(line_number, text) for each body paragraph, headings and block quotes dropped."""
    out, line = [], 1
    for block in body.split("\n\n"):
        stripped = block.strip()
        if stripped and not stripped.startswith(("#", ">", "|", "---")):
            out.append((line, " ".join(stripped.split())))
        line += block.count("\n") + 2
    return out


SENT_SPLIT = re.compile(r"(?<=[.!?])[\s\"”']+(?=[A-Z“\"'(])")


def sentences(para):
    return [s.strip() for s in SENT_SPLIT.split(para) if s.strip()]


def wordcount(s):
    return len(re.findall(r"[A-Za-z][A-Za-z'’-]*", s))


# ---------------------------------------------------------------- verbatim bans
# Constructions cut by name in a previous round. These are zero-tolerance: each one
# is a sentence a reviewer already deleted from this chapter.

VERBATIM = [
    # throat-clearing -- announcing a point, then delivering it
    (r"\bWatch (?:what happens|the first|closely)", "throat-clear: 'Watch what happens…' (cut twice already)"),
    (r"\bWhat I am claiming is\b", "throat-clear: 'What I am claiming is narrow(er)'"),
    (r"\bThe best evidence for this\b", "throat-clear: 'The best evidence for this power is not where…'"),
    (r"\bWhat is actually measured is\b", "throat-clear: 'What is actually measured is this.'"),
    (r"\b(?:Economists|Sociologists|Film scholars) have a name for\b", "throat-clear: 'X have a name for what…'"),
    (r"\bTwo qualifications\b", "throat-clear: 'Two qualifications, both real.'"),
    (r"\bare worth having\b|\bis worth keeping\b|\bworth keeping\b", "the 'worth' tic (banned as a family)"),
    (r"\bHere is (?:what|the|how)\b", "throat-clear: 'Here is what the film then does.'"),
    (r"\bThe mechanism is concrete\b", "throat-clear: 'The mechanism is concrete.'"),
    (r"\bThe answer runs back\b", "throat-clear: 'The answer runs back a century.'"),
    (r"\bwhich raises a question\b", "throat-clear: 'Which raises a question the parallel can't answer'"),
    (r"\bOne more thing\b", "throat-clear: 'One more thing the questions do not do…'"),
    (r"\bIt is worth (?:saying|noting|adding)\b", "self-narrating rigor: 'It is worth saying where…'"),
    (r"\bStart (?:with|on) (?:what|the street)\b", "directive opener: 'Start with what the reviews show'"),

    # meta-commentary and cross-reference
    (r"\bdescribed above\b|\bthe two definitions above\b|\bas (?:noted|described) (?:above|earlier)\b",
     "meta-commentary: backward reference"),
    (r"\bmatters later\b|\bgets settled\b|\bthe constraint matters\b", "meta-commentary: forward reference"),
    (r"\bsharpens the distinction\b|\bmakes the point sharper\b|\bwhich makes the point\b",
     "meta-commentary: narrating the argument's own effect"),
    (r"\bthe scale to hold in mind\b", "meta-commentary: instructing the reader"),
    (r"\bthe difference the rest of this turns on\b", "meta-commentary: announcing load-bearing status"),
    (r"\bI am not claiming it as one\b|\bmy claim, not his\b|\bI will assert\b",
     "attribution-marking habit (keep at most one, for contested evidence)"),
    (r"\bwhat follows is\b", "meta-commentary: roadmap"),

    # self-narrating rigor -- the house style's cardinal ban
    (r"\bstated plainly\b|\bsaid plainly\b|\bto be clear\b|\bthe blunt version\b",
     "self-narrating rigor (house style, banned outright)"),
    (r"\bnames its load-bearing\b|\bone honest qualifier\b", "self-narrating rigor"),

    # figures that carried claims, cut by name
    (r"\bHer own floor is the answer\b", "banned metaphor: 'Her own floor is the answer'"),
    (r"\bthe earlier gate had responded\b", "banned metaphor: 'The earlier gate had responded'"),
    (r"\bone route across a field\b|\bthe only route across\b", "banned metaphor: 'one route across a field'"),
    (r"\bwent invisible as convention\b", "banned metaphor"),
    (r"\bthe seat shifts\b|\bone seat, three occupants\b", "banned: 'seat' is retired apparatus"),
    (r"\bbuys unstructured time\b", "banned metaphor: 'Cheap space buys unstructured time'"),

    # factual traps that keep coming back
    (r"\b97 characters\b", "FACT: 97 is the runtime, not the cast. 'about a hundred'"),
    (r"\bran for a year\b|\bheld it a year\b", "FACT: the Dobie run was eleven weeks"),
    (r"\bseven weeks (?:after|later)\b", "FACT: the interval is eight weeks"),
    (r"\bstayed at the bus station\b", "FACT: the credit has no definite article"),
    (r"\bscarcely (?:goes )?a mile east\b", "FACT: false"),
    (r"\bdeclared Austin the Live Music Capital\b", "FACT: the council authorised a slogan"),
    (r"\bthe least auteur film ever made\b", "FACT: Lee Daniel's quip, not Macor's thesis"),
    (r"\baccounts but no accountability\b", "FACT: not a Stark & Pais quotation"),
    (r"\bits temporal dimension for ever\b", "FACT: fabricated Moretti quotation"),
    (r"\bnot the same thing as apathy\b", "CHECK: the card's wording is disc-dependent"),
]

# --------------------------------------------------------------- rate-based tells
# Not bans. Panels measured these and named a rate at which the shape stops reading
# as emphasis and starts reading as a machine. Thresholds are per 1,000 body words
# except the landing-line rate, which is a share of paragraphs.

RATE = [
    (r"(?m)\bWhat (?:a |an |the )?[a-z][\w'’-]*(?: [a-z][\w'’-]*){0,4} (?:is|does|was|did|makes|gives|adds)\b",
     "pseudo-cleft 'What X is/does…' opener", 1.5),
    (r"\brather than\b", "'rather than' (decorative unless load-bearing)", 1.2),
    (r",\s+not\b", "antithesis machine: ', not X'", 2.0),
    (r"\b(?:It|This|That) is not (?:a|an|the)\b", "antithesis machine: 'It is not a…'", 1.0),
    (r"\b(?:has|have|had) been \w+(?:ed|n)\b", "agentless passive (house style cardinal ban)", 0.8),
    (r"\bThe (?:first|second|third) thing is\b", "enumerator drift: drop the 'thing'", 0.4),
]

# Terms the panels found left bare in a cross-disciplinary collection. The chapter
# glossed its sociology and assumed its cinema and its economics; this is that list.
JARGON = [
    "co-presence", "nonterminal", "ordered triple", "diegetic", "the 180-degree rule",
    "assortative matching", "observationally equivalent", "agglomeration", "take rate",
    "divide et impera", "subject-access", "preliminary injunction", "second window",
    "third tier", "middle tier", "structural hole", "tertius gaudens", "elasticity",
]


def corpus_bands():
    """Punctuation bands measured from the calibrated film-essay corpus.

    Em-dashes are protected in this chapter's register: they are not a defect and no
    naive ban applies. That is not the same as leaving them unmeasured, which is how a
    draft reached 23 per 1,000 words against a 42-essay corpus whose mean is 4.1 and
    whose heaviest user runs 10.9. A construction can be legitimate and still be a tell
    at five times the rate anyone in the genre uses it.
    """
    import json
    p = Path.home() / ".claude" / "skills" / "draft" / "registers" / "slacker" / "floors.json"
    if not p.exists():
        return {}
    try:
        rules = json.loads(p.read_text()).get("rules", {})
    except Exception:
        return {}
    # floors.json carries em-dash; the colon and semicolon bands live in targets.json
    # under different keys. Reading only the first file is how a colon rate above the
    # corpus maximum went unreported while the em-dash problem was being fixed.
    dims = {}
    tp = p.parent / "targets.json"
    if tp.exists():
        try:
            dims = json.loads(tp.read_text()).get("dimensions", {})
        except Exception:
            dims = {}

    out = {}
    for name, pattern, keys in (("emdash", "—", ("emdash",)),
                                ("colon", ":", ("colon_prose_1k",)),
                                ("semicolon", ";", ("semi_prose_1k",))):
        band = rules.get(name)
        if not isinstance(band, dict) or "mean" not in band:
            for k in keys:
                cand = dims.get(k)
                if isinstance(cand, dict) and "mean" in cand:
                    band = cand
                    break
        if isinstance(band, dict) and "mean" in band:
            out[name] = (pattern, band)
    return out


def report_corpus(body_text, total_words):
    bands = corpus_bands()
    if not bands:
        return 0
    print("PUNCTUATION AGAINST THE CORPUS  (42 single-author film essays)")
    over = 0
    for name, (ch, band) in bands.items():
        n = body_text.count(ch)
        rate = 1000 * n / total_words
        mean, sd = band["mean"], band.get("sd") or 1
        z = (rate - mean) / sd
        flag = "ok"
        if rate > band.get("max", 1e9):
            flag = "ABOVE THE CORPUS MAXIMUM"
            over += 1
        elif z > 2:
            flag = "high"
        print("  %-10s %6.1f /1k   corpus mean %5.2f  max %5.2f  z=%+5.1f  %s"
              % (name, rate, mean, band.get("max", float("nan")), z, flag))
    print("  A rate above the corpus maximum is not a style preference. It means no")
    print("  author in the reference genre writes this way.")
    print()
    return over


def scan(path, quiet=False):
    raw = Path(path).read_text(encoding="utf-8")
    body = body_of(raw)
    paras = paragraphs(body)
    total_words = sum(wordcount(p) for _, p in paras)
    if not total_words:
        sys.exit("no body text found in %s" % path)

    print("ban scan: %s" % Path(path).name)
    print("  %d body paragraphs, %d words" % (len(paras), total_words))
    print()

    # --- verbatim bans
    hits = []
    for line, para in paras:
        for pat, label in VERBATIM:
            for m in re.finditer(pat, para, re.I):
                hits.append((line, label, m.group()))

    print("VERBATIM BANS  (zero tolerance -- each was cut from a previous draft)")
    if hits:
        for line, label, text in hits:
            print("  para@%-5d %-58s %r" % (line, label, text))
    else:
        print("  none")
    print()

    # --- landing-line metronome
    closers = [sentences(p)[-1] for _, p in paras if sentences(p)]
    short = [s for s in closers if wordcount(s) <= 13]
    share = len(short) / len(closers) if closers else 0
    print("LANDING LINES  (paragraph-final sentences of 13 words or fewer)")
    print("  %d of %d paragraphs = %.0f%%   threshold 25%%   %s"
          % (len(short), len(closers), 100 * share, "OVER" if share > 0.25 else "ok"))
    if not quiet and share > 0.25:
        print("  cure by ending on the evidence sentence already in the paragraph;")
        print("  do not write a replacement epigram")
        for (line, _), closer in zip(paras, closers):
            if wordcount(closer) <= 13:
                print("    para@%-5d %s" % (line, closer))
    print()

    # --- rates
    print("RATE-BASED TELLS  (per 1,000 body words)")
    over = 0
    for pat, label, budget in RATE:
        n = sum(len(re.findall(pat, p)) for _, p in paras)
        rate = 1000 * n / total_words
        flag = "OVER" if rate > budget else "ok"
        over += rate > budget
        print("  %-52s %5.2f  budget %4.2f  %s" % (label, rate, budget, flag))
        if not quiet and rate > budget:
            shown = 0
            for line, para in paras:
                for m in re.finditer(pat, para):
                    if shown < 6:
                        print("      para@%-5d %r" % (line, m.group()))
                        shown += 1
    print()

    over += report_corpus(" ".join(p for _, p in paras), total_words)

    # --- bare jargon
    bare = []
    for line, para in paras:
        for term in JARGON:
            if re.search(r"\b%s\b" % re.escape(term), para, re.I):
                bare.append((line, term))
    print("JARGON  (glossed or cut -- the chapter glossed its sociology and assumed its cinema)")
    if bare:
        for line, term in bare:
            print("  para@%-5d %s" % (line, term))
    else:
        print("  none present")
    print()

    # --- sentence-shape variance, reported not judged
    lens = [wordcount(s) for _, p in paras for s in sentences(p)]
    if lens:
        mean = sum(lens) / len(lens)
        sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        print("SENTENCE SHAPE  (reported, not judged)")
        print("  %d sentences, mean %.1f words, sd %.1f, CV %.2f" % (len(lens), mean, sd, sd / mean))
        print("  the August rhythm pass established that this chapter's short-sentence share")
        print("  is a genre difference from the film-essay corpus, not a defect")
    print()

    failed = bool(hits)
    print("RESULT: %s" % ("FAIL -- verbatim bans present" if failed else
                          "no verbatim bans; %d rate tells over budget" % over))
    return 1 if failed else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    sys.exit(scan(a.draft, a.quiet))
