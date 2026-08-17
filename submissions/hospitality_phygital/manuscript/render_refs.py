#!/usr/bin/env python3
"""Render references.bib into Intellect Harvard for Hospitality & Society.

House rules (JOURNAL_SPEC.md, from HOSP_NFC_May_26.pdf):
  - year of publication in brackets
  - commas, not full stops, between parts of each reference
  - no 'no.' for the journal number; a colon between volume and number
  - 'pp.' before page extents
  - article titles in single quotes, journal and book titles italic
  - 'Anon.' where there is no author
  - the list is titled 'References' and holds only works cited in the text

Entries marked DO-NOT-CITE in their note field are refused, loudly.

Usage: python3 render_refs.py --cited cited_keys.txt
"""
import argparse
import re
import unicodedata
import sys
from pathlib import Path

BIB = Path(__file__).resolve().parent.parent / "literature" / "references.bib"


def parse_bib(text):
    entries = {}
    for block in re.split(r"\n@", text)[1:]:
        m = re.match(r"(\w+)\s*\{\s*([^,]+),", block)
        if not m:
            continue
        kind, key = m.group(1).lower(), m.group(2).strip()
        fields = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", block):
            name, i, depth, buf = fm.group(1).lower(), fm.end(), 1, []
            while i < len(block) and depth:
                c = block[i]
                depth += (c == "{") - (c == "}")
                if depth:
                    buf.append(c)
                i += 1
            fields[name] = re.sub(r"\s+", " ", "".join(buf)).strip()
        entries[key] = (kind, fields)
    return entries


ACCENTS = {"k": "\u0328", "r": "\u030a", '"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302", "~": "\u0303",
           "c": "\u0327", "v": "\u030c", "=": "\u0304", ".": "\u0307", "u": "\u0306"}


def clean(s):
    """Unescape LaTeX into Unicode. Accents are handled generically, not by table:
    a hardcoded list silently passed \\"a and \\'o straight through to the rendered
    reference list, which is how 'Sch\\"anzel' reached a draft. Braced or bare."""
    import unicodedata
    for a, b in [("\\&", "&"), ("\\#", "#"), ("\\%", "%"), ("\\_", "_"), ("--", "\u2013"), ("``", "\u2018"), ("''", "\u2019"),
                 ("{\\dh}", "\u00f0"), ("{\\TH}", "\u00de"), ("{\\o}", "\u00f8"),
                 ("{\\ss}", "\u00df"), ("{\\aa}", "\u00e5"),
                 ("{\\i}", "\u0131"), ("\\i ", "\u0131"), ("{\\j}", "\u0237"),
                 ("{\\l}", "\u0142"), ("{\\L}", "\u0141"), ("{\\O}", "\u00d8"),
                 ("{\\AA}", "\u00c5"), ("{\\ae}", "\u00e6"), ("{\\AE}", "\u00c6")]:
        s = s.replace(a, b)

    def sub(m):
        mark = ACCENTS.get(m.group(1))
        return unicodedata.normalize("NFC", m.group(2) + mark) if mark else m.group(2)

    s = re.sub(r'\{\\(["\'`^~cvkr=.u])\s*\{?([A-Za-z])\}?\}', sub, s)   # {\"a} {\"{a}} {\k{a}} {\k a}
    s = re.sub(r'\\(["\'`^~cvkr=.u])\s*\{([A-Za-z])\}', sub, s)      # \k{a}  \c{c}  \v{s}
    s = re.sub(r'\\(["\'`^~])\{?([A-Za-z])\}?', sub, s)              # bare \"a
    # single-backtick / straight-apostrophe quotes inside titles, left after `` and '' pass
    s = re.sub(r"`([^`']+)'", "\u2018\\1\u2019", s)
    return s.replace("{", "").replace("}", "").strip()


def authors(raw):
    """Intellect gives full forenames: 'Surname, Firstname and Surname, Firstname'."""
    people = [clean(a).strip() for a in raw.split(" and ")]
    out = []
    for person in people:
        if "," in person:
            surname, given = [p.strip() for p in person.split(",", 1)]
            out.append(f"{surname}, {given}")
        else:
            out.append(person)
    if len(out) == 1:
        return out[0]
    return ", ".join(out[:-1]) + " and " + out[-1]


# Words that stay capitalized inside a sentence-cased title. Proper nouns, places,
# instruments and traditions drawn from this bibliography; extend rather than widen the
# heuristics, because a wrong lowercase in a title is a visible error.
PROPER = {
    "africa", "african", "airbnb", "america", "american", "arabic", "asia", "asian",
    "australia", "australian", "bauman", "britain", "british", "canada", "canadian",
    "china", "chinese", "covid", "derrida", "douyin", "dutch", "england", "english",
    "europe", "european", "facebook", "france", "french", "germany", "german",
    "instagram", "internet", "japan", "japanese", "kant", "kantian", "korea", "korean",
    "kingdom", "london", "meituan", "netherlands", "new", "singapore", "spain",
    "spanish", "states", "tiktok", "twitter", "uber", "united", "vietnam", "vietnamese",
    "wechat", "york", "zealand",
    # forms of address and fixed names that survive down-casing
    "mr", "mrs", "ms", "dr", "st", "domo", "arigato", "roboto",
    "belgium", "chef", "derrida", "kingdom", "kiwi", "le", "macromarketing",
    "petit", "seoul",
}

def nest_quotes(title):
    """Intellect: single quotes delimit a title, so a quotation inside it takes double."""
    title = re.sub("\u2018([^\u2018\u2019]+)\u2019", r'"\1"', title)
    return re.sub(r"(?<![A-Za-z])'([^']+)'(?![A-Za-z])", r'"\1"', title)

def sentence_case(title):
    """Down-case a Title Case title, Intellect house style, protecting real names.

    Left alone: the first word, the first word after a colon or question mark, anything
    already containing an internal capital (Airbnb, TikTok, McDonald), anything fully
    capitalized (AI, XAI, HCI, EU), anything hyphenated with an internal capital, and the
    protected list above. Everything else that is Capitalized becomes lower case.
    """
    out, start_of_sentence = [], True
    for tok in title.split(" "):
        core = tok.strip("'\u2018\u2019\"()[]{},.;:?")
        bare = core[:-2] if core.lower().endswith("'s") else core
        bare = bare.replace("\u2019s", "")
        letters = "".join(ch for ch in core if ch.isalpha())
        keep = (
            start_of_sentence
            or not letters
            or any(ch.isdigit() for ch in core)         # 7Es, COVID-19
            or letters.isupper()                        # AI, XAI, EU, US
            or ("-" not in core and any(ch.isupper() for ch in letters[1:]))  # Airbnb, TikTok
            # a hyphenated compound falls through and is judged part by part below
            or core.lower() in PROPER
            or bare.lower() in PROPER
        )
        if keep and start_of_sentence and "-" in tok:
            # "Real-Time Feedback" opening a title becomes "Real-time feedback": the first
            # element keeps its capital, the rest are judged like any other word.
            head, _, tail = tok.partition("-")
            def _low(part):
                ls = "".join(c for c in part if c.isalpha())
                if not ls or ls.isupper() or any(c.isupper() for c in ls[1:]):
                    return part
                i = next((j for j, ch in enumerate(part) if ch.isalpha()), None)
                return part if i is None else part[:i] + part[i].lower() + part[i + 1:]
            out.append(head + "-" + "-".join(_low(p2) for p2 in tail.split("-")))
        elif keep:
            out.append(tok)
        else:
            # Hyphenated compounds are down-cased part by part, so "Well-Being" becomes
            # "well-being" while "Human-AI" keeps the acronym.
            def lower_part(part):
                ls = "".join(c for c in part if c.isalpha())
                if not ls or ls.isupper() or any(c.isupper() for c in ls[1:]) \
                   or part.strip("'\u2018\u2019\"()[]{},.;:?").lower() in PROPER:
                    return part
                i = next((j for j, ch in enumerate(part) if ch.isalpha()), None)
                return part if i is None else part[:i] + part[i].lower() + part[i + 1:]
            out.append("-".join(lower_part(pt) for pt in tok.split("-")))
        stripped = tok.rstrip("'\u2019\"))]")
        start_of_sentence = stripped.endswith(":") or stripped.endswith("?")
    return " ".join(out)


def fix_dashes(text):
    """LaTeX `--`, the stray `--`-plus-hyphen, and hyphenated volume ranges."""
    text = text.replace("–-", "—").replace("--", "–")
    return re.sub(r"\b(\d+):(\d+)-(\d+)\b", "\g<1>:\g<2>–\g<3>", text)


def render(kind, f, suffix=""):
    who = authors(f["author"]) if "author" in f else "Anon."
    year = f.get("year", "n.d.") + suffix
    title = nest_quotes(sentence_case(clean(f.get("title", ""))))
    head = f"{who} ({year}), "

    if kind == "article":
        vol = f.get("volume", "")
        num = f.get("number", "")
        vn = f"{vol}:{num}" if vol and num else vol
        pages = clean(f.get("pages", ""))
        bits = [f"'{title}'", f"*{clean(f.get('journal',''))}*"]
        if vn:
            bits.append(vn)
        if pages:
            # 'pp.' introduces an extent; a bare article number takes neither 'pp.' nor 'p.'
            bits.append(pages if "–" not in pages and "-" not in pages else f"pp. {pages}")
        return fix_dashes(head + ", ".join(bits) + ".")

    if kind == "book":
        addr = clean(f.get("address", ""))
        pub = clean(f.get("publisher", ""))
        return head + f"*{title}*, {addr}: {pub}."

    if kind == "incollection":
        eds = authors(f["editor"]) if f.get("editor") else ""
        pages = clean(f.get("pages", ""))
        n_eds = len(f.get("editor", "").split(" and ")) if f.get("editor") else 0
        lead = f"in {eds} ({'eds' if n_eds > 1 else 'ed.'}), " if eds else "in "
        tail = f", pp. {pages}" if pages else ""
        return (head + f"'{title}', {lead}*{clean(f.get('booktitle',''))}*, "
                f"{clean(f.get('address',''))}: {clean(f.get('publisher',''))}{tail}.")

    if kind == "inproceedings":
        pages = clean(f.get("pages", ""))
        tail = f", pp. {pages}" if pages else ""
        return head + f"'{title}', *{clean(f.get('booktitle',''))}*{tail}."

    return head + f"*{title}*."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cited", required=True, help="file of bib keys, one per line")
    args = ap.parse_args()

    entries = parse_bib(BIB.read_text(encoding="utf-8"))
    keys = [l.strip() for l in Path(args.cited).read_text().splitlines()
            if l.strip() and not l.lstrip().startswith("#")]

    missing = [k for k in keys if k not in entries]
    if missing:
        print("ABORT: keys not in references.bib: " + ", ".join(missing), file=sys.stderr)
        return 1

    seen_doi = {}
    for k in keys:
        doi = entries[k][1].get("doi", "").lower().strip()
        if doi and doi in seen_doi:
            print(f"ABORT: {k} and {seen_doi[doi]} are the same work (DOI {doi}). "
                  f"Merge the bib entries before rendering.", file=sys.stderr)
            return 1
        if doi:
            seen_doi[doi] = k

    refused = [k for k in keys if "DO-NOT-CITE" in entries[k][1].get("note", "")]
    if refused:
        print("ABORT: refused DO-NOT-CITE entries: " + ", ".join(refused), file=sys.stderr)
        return 1

    unverified = [k for k in keys
                  if "verified" not in entries[k][1].get("note", "")
                  and "crossref-verified" not in entries[k][1].get("note", "")]
    if unverified:
        print("WARNING: cited but not marked verified: " + ", ".join(unverified), file=sys.stderr)

    # Harvard requires a/b suffixes when the same authors publish twice in one year,
    # and the manuscript already cites them that way ("Lynch et al. 2021a, 2021b").
    # Without this the rendered list printed two bare 2021 entries and the citation
    # check reported a disagreement that was the renderer's, not the author's.
    # The signature is FIRST AUTHOR + year, not the whole author list: two works can
    # share a first author and a year while differing further down the list, and in
    # text they both read "Lynch et al. 2021". That is the collision a reader hits.
    def first_surname(f):
        if "author" not in f:
            return "Anon."
        first = clean(f["author"].split(" and ")[0]).strip()
        return first.split(",")[0].strip() if "," in first else first.split()[-1]

    by_author_year = {}
    for k in keys:
        kind, f = entries[k]
        by_author_year.setdefault((first_surname(f), f.get("year", "n.d.")), []).append(k)
    suffix = {}
    for sig, ks in by_author_year.items():
        if len(ks) > 1 and sig[1] != "n.d.":
            # order by title so the letters are stable across runs
            for i, k in enumerate(sorted(ks, key=lambda k: clean(entries[k][1].get("title", "")).lower())):
                suffix[k] = chr(ord("a") + i)

    def sort_key(entry):
        folded = unicodedata.normalize("NFKD", entry)
        return "".join(c for c in folded if not unicodedata.combining(c)).lower()

    rendered = sorted((render(*entries[k], suffix=suffix.get(k, "")) for k in keys),
                      key=sort_key)
    print("## References\n")
    for r in rendered:
        print(r + "\n")
    print(f"<!-- {len(rendered)} entries -->", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
