#!/usr/bin/env python3
"""Stage S2 of the literature run: de-duplication registry of existing source notes.

Copied 2026-11-05 from D/current/peircean_triad/library/tools/build_registry.py for run
dxda-lib-2026-11 (submissions/dxd_animation/library); re-copied 2026-11-08 for pta-lib-2026-11
(submissions/pt_ai_as_animation/library: OUT_PATH -> pt_ai_animation_local, library "pta" added;
ROOT stays the main checkout, which holds the dxda cards). Changes: LIBRARIES widened to every lab
library, each with a format (h1 | yaml | spaces); OUT_PATH moved outside the public repo, because the
registry lists titles and paths in the private nested repos. Writes one row per
note, with a header row. Checks are printed at the end; the exit status is 1
if a path is missing or a DOI does not start with 10.

  research   dissertation/research/library/*.md                 H1 citation + Identifier line
  triadic    submissions/triadic_reduction/library/cards/*.md   YAML frontmatter
  monograph  dissertation/current/monograph/library/cards/*.md   YAML frontmatter

Stdlib only. Run as:  python3 -I build_registry.py
"""

import os
import re
import sys
import unicodedata

ROOT = "/Users/ludwitt/iit-playground/pyphi-experiments"
J = os.path.join
LIBRARIES = (
    ("research", J(ROOT, "dissertation", "research", "library"), "h1"),
    ("monograph", J(ROOT, "dissertation", "current", "monograph", "library", "cards"), "yaml"),
    ("peircean", J(ROOT, "dissertation", "current", "peircean_triad", "library", "cards"), "yaml"),
    ("triadic", J(ROOT, "submissions", "triadic_reduction", "library", "cards"), "yaml"),
    ("dxdfound", J(ROOT, "submissions", "dxd_foundation", "literature", "library"), "h1"),
    ("lima", J(ROOT, "submissions", "lima_pdw", "literature", "cards"), "h1"),
    ("designeth", J(ROOT, "submissions", "algorithmacy_design_ethics", "literature", "library"), "h1"),
    ("coordsov", J(ROOT, "submissions", "coordinative_sovereignty", "literature", "library", "cards"), "yaml"),
    ("hospitality", J(ROOT, "submissions", "hospitality_phygital", "library", "cards"), "yaml"),
    ("dial", J(ROOT, "submissions", "dial_response_algorithmacy", "literature", "cards"), "yaml"),
    ("slacker", J(ROOT, "submissions", "slacker_thirds", "library", "cards"), "yaml"),
    ("spaces", J(ROOT, "spaces", "research", "notes"), "spaces"),
    ("dxdanimator", J(ROOT, "submissions", "dxd_animator", "literature", "library", "cards"), "h1"),
    ("dxda", J(ROOT, "submissions", "dxd_animation", "library", "cards"), "yaml"),
    ("pta", "/Users/ludwitt/iit-playground/wt-pt-animation/submissions/pt_ai_as_animation/library/cards", "yaml"),
)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.expanduser("~/iit-playground/pt_ai_animation_local/registry.tsv")
COLUMNS = ["key", "library", "path", "doi", "norm_title", "first_author",
           "first_initial", "year", "read_depth", "h1"]

# First 10.nnnn/... token in a field. Label and URL prefixes (DOI, doi:, https://doi.org/)
# are skipped because the search starts at the token itself.
DOI_TOKEN = re.compile(r"10\.\d{4,9}/[^\s`'\"<>·*]+")
IDENT_LINE = re.compile(r"^\*\*Identifier:\*\*(.*)$")
NEXT_BOLD_LABEL = re.compile(r"\*\*[A-Za-z][^*]*:\*\*")
READ_DEPTH = re.compile(r"\*\*Read depth:\*\*\s*([^\s·]+)")
PAREN_GROUP = re.compile(r"\(([^()]*)\)")
FOUR_DIGITS = re.compile(r"(?<!\w)(\d{4})(?!\d)")
BARE_YEAR = re.compile(r"(?<![\w/])((?:1[5-9]|20)\d{2})[a-z]?(?!\w)")
QUOTE_OR_ITALIC_START = re.compile(r"\.\s+(?=[\"“*])")
TITLE_END_ITALIC = re.compile(r"[.?!][\"”]?\s+(?=\*)")
TITLE_END_CAPITAL = re.compile(r"[.?!][\"”]?\s+(?=[A-Z\"“(*]|arXiv\b|https?:)")
QUOTED_TITLE_TAIL = re.compile(r"\s*[.,?!]?\s*(?:\*|In\b|https?:|$)")
IMPLAUSIBLE_AUTHOR = re.compile(r"[:?—]")
FRONTMATTER_LINE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*?)\s*$")


# Letters that NFKD does not decompose, mapped to their ASCII spelling.
TRANSLIT = str.maketrans({
    "ı": "i", "ø": "o", "æ": "ae", "œ": "oe", "ß": "ss",
    "đ": "d", "ł": "l", "þ": "th", "ð": "d",
})


def fold(text):
    """Lowercase and fold diacritics to ASCII: NFKD, drop combining marks, then TRANSLIT."""
    decomposed = unicodedata.normalize("NFKD", text)
    kept = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return kept.lower().translate(TRANSLIT)


def norm_title(title):
    """Keep a-z0-9; every other run becomes one space."""
    return re.sub(r"[^a-z0-9]+", " ", fold(title)).strip()


def norm_surname(surname):
    """Keep a-z only."""
    return re.sub(r"[^a-z]", "", fold(surname))


def initial_of(given):
    """First a-z letter of the given name(s), or ''."""
    m = re.search(r"[a-z]", fold(given))
    return m.group(0) if m else ""


def doi_of(text):
    """Lowercase DOI from the first 10.nnnn/ token in text, or ''."""
    m = DOI_TOKEN.search(text or "")
    if not m:
        return ""
    token = m.group(0).rstrip(".,;:")
    while token.endswith(")") and token.count(")") > token.count("("):
        token = token[:-1].rstrip(".,;:")
    return token.lower()


def first_author_parts(author):
    """Split 'Surname, Given ...' at the first comma. No comma: the whole string is the surname."""
    surname, comma, given = author.partition(",")
    return surname.strip(), (given if comma else "")


def spec_year_of(h1):
    """The brief's literal rule: the first 4-digit number in parentheses, or ''."""
    for group in PAREN_GROUP.finditer(h1):
        digits = FOUR_DIGITS.search(group.group(1))
        if digits:
            return digits.group(1)
    return ""


def split_h1(h1):
    """Parse a research H1 into (author, year, title, year_is_bare), or None.

    Year: the earliest 4-digit year in the H1, either parenthetical ('(2012)') or
    bare ('Author. 1972. Title.'). Taking the earliest keeps a later reprint note,
    such as '(Reprinted 1984)', from replacing the publication year.

    Author list: it ends at the year, or at '. "' or '. *' when a quoted or italic
    title comes first. In the second case the year may sit after the title (a
    venue-final citation), and an H1 with no year but a quoted title parses with year ''.
    """
    body = re.sub(r"^#\s*", "", h1)
    year_hit = None  # (start, end, year, is_bare)
    for group in PAREN_GROUP.finditer(body):
        digits = FOUR_DIGITS.search(group.group(1))
        if digits:
            year_hit = (group.start(), group.end(), digits.group(1), False)
            break
    bare = BARE_YEAR.search(body)
    if bare and (year_hit is None or bare.start() < year_hit[0]):
        year_hit = (bare.start(), bare.end(), bare.group(1), True)
    boundary = QUOTE_OR_ITALIC_START.search(body)
    if boundary and (year_hit is None or boundary.start() < year_hit[0]):
        author, rest = body[:boundary.start()], body[boundary.end():]
        year, is_bare = (year_hit[2], year_hit[3]) if year_hit else ("", False)
    elif year_hit:
        start, end, year, is_bare = year_hit
        author = body[:start]
        rest = re.sub(r"^/\d+", "", body[end:]).lstrip(" .,:;)")
    else:
        return None
    author = author.strip(" .,;[*")
    if not author or IMPLAUSIBLE_AUTHOR.search(author):
        return None
    rest = rest.lstrip()
    title = None
    if rest[:1] in ('"', "“"):
        close = re.search(r'["”]', rest[1:])
        if close:
            quoted = rest[1:1 + close.start()]
            tail = rest[1 + close.end():]
            if quoted.rstrip()[-1:] in (".", "?", "!") or QUOTED_TITLE_TAIL.match(tail):
                title = quoted
    if title is None and rest[:1] == "*":
        close = rest.find("*", 1)
        title = rest[1:close] if close > 0 else rest[1:]
    if title is None:
        stop = TITLE_END_ITALIC.search(rest) or TITLE_END_CAPITAL.search(rest)
        title = rest[:stop.start()] if stop else rest
    return author, year, title.strip(" *.,\"“”"), is_bare


def research_record(name, path, text):
    """One research row from the H1 and the Identifier line. Returns (record, year_is_bare)."""
    lines = text.splitlines()
    h1 = lines[0].rstrip() if lines else ""
    doi, read_depth = "", ""
    for line in lines[1:15]:
        m = IDENT_LINE.match(line)
        if m:
            ident = m.group(1)
            cut = NEXT_BOLD_LABEL.search(ident)
            doi = doi_of(ident[:cut.start()] if cut else ident)
            rd = READ_DEPTH.search(line)
            read_depth = rd.group(1).rstrip(",;.") if rd else ""
            break
    parsed = split_h1(h1) if h1.startswith("#") else None
    if parsed:
        author, year, title, is_bare = parsed
        surname, given = first_author_parts(author)
        first_author, first_initial = norm_surname(surname), initial_of(given)
        nt = norm_title(title)
    else:
        is_bare = False
        year, first_author, first_initial, nt = "", "", "", ""
    record = {
        "key": name[:-len(".md")], "library": "research", "path": path, "doi": doi,
        "norm_title": nt, "first_author": first_author, "first_initial": first_initial,
        "year": year, "read_depth": read_depth, "h1": h1,
    }
    return record, is_bare


def unquote(value):
    """Strip one pair of YAML quotes; drop a trailing comment from plain scalars."""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        inner = value[1:-1]
        if value[0] == '"':
            return inner.replace('\\"', '"').replace("\\\\", "\\")
        return inner.replace("''", "'")
    return re.sub(r"\s+#.*$", "", value)


def read_frontmatter(text):
    """Top-level 'key: value' pairs of a leading YAML block, or None if there is none."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        m = FRONTMATTER_LINE.match(line)
        if m and m.group(1) not in fields:
            fields[m.group(1)] = unquote(m.group(2))
    return None


def card_record(lib, name, path, text):
    """One triadic or monograph row from the YAML frontmatter."""
    fields = read_frontmatter(text)
    if fields is None:
        fields = {}
    key = fields.get("key") or fields.get("citekey") or fields.get("id") or ""
    read_depth = fields.get("read_depth") or fields.get("verified") or ""
    if fields.get("status", "") == "dropped":
        read_depth = f"{read_depth};dropped" if read_depth else "dropped"
    authors = fields.get("authors", "").strip().strip("[]")
    first = re.split(r";|\" ?, ?\"| and ", authors)[0].strip().strip('"\' ')
    surname, given = first_author_parts(first) if first.strip() else ("", "")
    year = fields.get("year", "").strip()
    return {
        "key": key.strip() or name[:-len(".md")], "library": lib, "path": path,
        "doi": doi_of(fields.get("doi", "")),
        "norm_title": norm_title(fields.get("title", "")),
        "first_author": norm_surname(surname),
        "first_initial": initial_of(given),
        "year": year if re.fullmatch(r"\d{4}", year) else "",
        "read_depth": read_depth.strip(),
        "h1": "",
    }


def spaces_record(name, path, text):
    """One row from a spaces note: '# key: Title' then 'Full citation: Author, A. (YEAR). ...'."""
    lines = text.splitlines()
    h1 = lines[0].rstrip() if lines else ""
    title = h1.split(":", 1)[1].strip() if ":" in h1 else ""
    cite = next((ln for ln in lines[1:6] if ln.startswith("Full citation:")), "")
    m = re.search(r"Full citation:\s*([^,(]+),\s*([^,(]*)[^(]*\((\d{4})", cite)
    surname, given, year = (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")
    head = "\n".join(lines[:6])
    return {
        "key": name[:-len(".md")], "library": "spaces", "path": path, "doi": doi_of(head),
        "norm_title": norm_title(title), "first_author": norm_surname(surname),
        "first_initial": initial_of(given), "year": year,
        "read_depth": "", "h1": h1,
    }


def clean(value):
    """Keep one TSV field on one line."""
    return re.sub(r"[\t\r\n]+", " ", str(value))


def main():
    rows, unparsed, no_year, skipped = [], [], [], []
    excluded = {"pre-R40": 0, "README": 0}
    bare_year_notes, year_differs = [], []
    strict_doi_missing, h1_doi_only = [], []
    lib_counts = {}

    for lib, directory, fmt in LIBRARIES:
        if not os.path.isdir(directory):
            print(f"skip (missing): {directory}")
            lib_counts[lib] = 0
            continue
        count = 0
        for name in sorted(os.listdir(directory)):
            path = os.path.join(directory, name)
            if not name.endswith(".md") or not os.path.isfile(path):
                continue
            if name.startswith("."):
                skipped.append(path)
                continue
            if fmt == "h1" and name.endswith(".pre-R40.md"):
                excluded["pre-R40"] += 1
                continue
            if name.lower() in ("readme.md", "index.md") or "readme" in name.lower():
                excluded["README"] += 1
                continue
            try:
                with open(path, "rb") as fh:
                    text = fh.read().decode("utf-8-sig")
            except UnicodeDecodeError:
                record = {c: "" for c in COLUMNS}
                record.update({"key": name[:-len(".md")], "library": lib, "path": path})
                unparsed.append((lib, name, "not UTF-8"))
                rows.append(record)
                count += 1
                continue
            if fmt == "h1":
                record, is_bare = research_record(name, path, text)
                record["library"] = lib
                if is_bare:
                    bare_year_notes.append(name)
                spec = spec_year_of(record["h1"])
                if record["year"] and spec and spec != record["year"]:
                    year_differs.append(name)
                ident = next((ln for ln in text.splitlines()[1:15] if IDENT_LINE.match(ln)), None)
                if ident and record["doi"] and not re.match(
                        r"\*\*Identifier:\*\*\s*(?:`|https?://doi\.org/)?10\.", ident):
                    strict_doi_missing.append(name)
                if doi_of(record["h1"]) and not record["doi"]:
                    h1_doi_only.append(name)
            elif fmt == "spaces":
                record = spaces_record(name, path, text)
            else:
                record = card_record(lib, name, path, text)
            if not (record["first_author"] and record["norm_title"]):
                unparsed.append((lib, name, "no first_author or norm_title"))
            elif not record["year"]:
                no_year.append(name)
            rows.append(record)
            count += 1
        lib_counts[lib] = count

    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as out:
        out.write("\t".join(COLUMNS) + "\n")
        for record in rows:
            out.write("\t".join(clean(record[c]) for c in COLUMNS) + "\n")

    print(f"wrote {OUT_PATH}")
    print("row counts: " + " ".join(f"{lib}={lib_counts[lib]}" for lib, _, _ in LIBRARIES)
          + f" total={len(rows)}")
    print(f"excluded: .pre-R40.md={excluded['pre-R40']} README={excluded['README']}")
    if skipped:
        print("skipped dot-files: " + ", ".join(skipped))

    failures = 0
    missing = [r["path"] for r in rows if not os.path.exists(r["path"])]
    print(f"path check: {len(rows) - len(missing)}/{len(rows)} exist")
    failures += len(missing)
    bad_doi = [r for r in rows if r["doi"] and not r["doi"].startswith("10.")]
    doi_rows = sum(1 for r in rows if r["doi"])
    print(f"doi check: {doi_rows} non-empty DOIs, {len(bad_doi)} not starting with 10.")
    failures += len(bad_doi)

    print(f"unparsed (no first_author or norm_title): {len(unparsed)}")
    for lib, name, why in unparsed:
        print(f"  {lib}: {name} ({why})")
    print(f"parsed but no year: {len(no_year)}" + (f" ({', '.join(no_year)})" if no_year else ""))

    by_doi = {}
    for r in rows:
        if r["doi"]:
            by_doi.setdefault(r["doi"], []).append(r)
    cross = {d: rs for d, rs in by_doi.items() if len({r["library"] for r in rs}) > 1}
    pairs = []
    for d in sorted(cross):
        rs = cross[d]
        for i in range(len(rs)):
            for j in range(i + 1, len(rs)):
                if rs[i]["library"] != rs[j]["library"]:
                    pairs.append((d, rs[i], rs[j]))
    print(f"duplicate DOIs across libraries: {len(cross)} DOIs, {len(pairs)} cross-library pairs")
    for d, a, b in pairs[:10]:
        print(f"  {d}  {a['library']}:{a['key']}  <->  {b['library']}:{b['key']}")

    by_key = {}
    for r in rows:
        by_key.setdefault(r["key"], []).append(r)
    key_coll = {k: rs for k, rs in by_key.items() if len({r["library"] for r in rs}) > 1}
    print(f"keys colliding across libraries: {len(key_coll)}")
    for k in sorted(key_coll)[:10]:
        print(f"  {k}: " + ", ".join(r["library"] for r in key_coll[k]))

    print("notes on the parse (informational):")
    print(f"  research years taken from a bare year (none in parentheses first): {len(bare_year_notes)}")
    print(f"  research years that differ from the brief's parenthetical-only rule: {len(year_differs)}"
          + (f" (first 10: {', '.join(year_differs[:10])})" if year_differs else ""))
    print(f"  research DOIs from a labelled or mid-line identifier "
          f"(strict 'starts with 10.' would blank them): {len(strict_doi_missing)}")
    print(f"  research notes with a DOI in the H1 but none in the Identifier line: {len(h1_doi_only)}")
    within = {}
    for r in rows:
        if r["doi"]:
            within[(r["library"], r["doi"])] = within.get((r["library"], r["doi"]), 0) + 1
    dup_within = sum(1 for v in within.values() if v > 1)
    print(f"  DOIs carded more than once inside one library: {dup_within}")

    if failures:
        print(f"FAILED checks: {failures}")
        sys.exit(1)


if __name__ == "__main__":
    main()
