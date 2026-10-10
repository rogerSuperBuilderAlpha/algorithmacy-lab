"""Build the APA 7 reference list at the end of part4_phygital/DRAFT.md from references.bib and cited_keys.txt.

Run: python3 literature/build_references.py  (from the arm directory or anywhere).
Formatting only: it never changes metadata. Year suffixes (2022a/2022b) are assigned to entries whose
author lists and year are identical, ordered by title, as APA 7 requires; the body text must use the
same suffixes by hand.
"""
import re
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CITED = [k for k in (HERE / 'cited_keys.txt').read_text().split() if k]
BIB = (HERE / 'references.bib').read_text()

ENTS = {}
for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}', BIB, flags=re.S):
    typ, key, body = m.groups()
    fields = {}
    for fm in re.finditer(r'(\w+)\s*=\s*(\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}|"[^"]*"|\w+)', body):
        v = fm.group(2).strip()
        fields[fm.group(1).lower()] = v[1:-1] if v[0] in '{"' else v
    ENTS[key] = (typ.lower(), fields)
missing = [k for k in CITED if k not in ENTS]
assert not missing, f"cited but not in bib: {missing}"

# Order matters: longer / more specific macros first.
TEX = [
    (r"\ldots", "..."), (r"{\v s}", "š"), (r"\v{s}", "š"), (r"{\v c}", "č"), (r"\v{c}", "č"),
    (r"{\c{c}}", "ç"), (r"\c{c}", "ç"), (r"{\'\i}", "í"), (r"\'\i", "í"), (r"{\k{e}}", "ę"), (r"\k{e}", "ę"),
    (r"{\'a}", "á"), (r"\'a", "á"), (r"{\'c}", "ć"), (r"\'c", "ć"), (r"{\'e}", "é"), (r"\'e", "é"), (r"{\'o}", "ó"), (r"\'o", "ó"), (r"{\'s}", "ś"), (r"\'s", "ś"),
    (r"{\'n}", "ń"), (r"\'n", "ń"), (r"\'z", "ź"), (r"\.z", "ż"), (r"{\.e}", "ė"), (r"\.e", "ė"),
    (r'{\"o}', "ö"), (r'\"o', "ö"), (r'{\"u}', "ü"), (r'\"u', "ü"), (r'{\"a}', "ä"), (r'\"a', "ä"),
    (r"{\ae}", "æ"), (r"\ae", "æ"), (r"{\l}", "ł"), (r"\l{}", "ł"), (r"\l", "ł"),
    ("---", "—"), ("--", "–"), ("``", "“"), ("''", "”"), ("`", "‘"),
    (r"\&", "&"), (r"\%", "%"), ("~", " "),
]


def clean(s):
    for a, b in TEX:
        s = s.replace(a, b)
    s = re.sub(r'\\url\{([^}]*)\}', r'\1', s)
    s = s.replace('{', '').replace('}', '')
    s = s.replace("‘", "'") if s.count("‘") and not s.count("’") and s.count("'") else s
    return re.sub(r'\s+', ' ', s).strip()


def split_authors(a):
    return [x.strip() for x in re.split(r'\s+and\s+', a) if x.strip()]


def fmt_name(raw):
    if raw.startswith('{') and raw.endswith('}'):          # corporate author
        return clean(raw), clean(raw)
    p = clean(raw)
    jr = ''
    parts = [x.strip() for x in p.split(',')]
    if len(parts) == 3:                                     # "Last, Jr, First" or "Last, First, Jr"
        if parts[2].rstrip('.') in ('Jr', 'Sr', 'II', 'III'):
            fam, giv, suffix = parts
        else:
            fam, suffix, giv = parts
        jr = f", {suffix.rstrip('.')}." if suffix.rstrip('.') in ('Jr', 'Sr') else f", {suffix}"
    elif len(parts) == 2:
        fam, giv = parts
    else:
        bits = p.split()
        if len(bits) == 1:
            return p, p
        fam, giv = bits[-1], ' '.join(bits[:-1])
    giv = re.sub(r'\([^)]*\)', '', giv).strip()
    inits = []
    for g in giv.split():
        if re.fullmatch(r'([A-Z]\.)+', g):
            inits.append(g)
        else:
            inits.append('-'.join(x[0] + '.' for x in g.split('-') if x and x[0].isalpha()))
    name = f"{fam}, {' '.join(i for i in inits if i)}".rstrip(', ') + jr
    return name, fam


def authors_str(a):
    out = [fmt_name(x)[0] for x in split_authors(a)]
    if len(out) == 1:
        return out[0]
    if len(out) <= 20:
        return ', '.join(out[:-1]) + ', & ' + out[-1]
    return ', '.join(out[:19]) + ', . . . ' + out[-1]


def link(f):
    doi = f.get('doi', '')
    if doi:
        return ' https://doi.org/' + doi.replace('https://doi.org/', '')
    for fld in ('url', 'howpublished'):
        m = re.search(r'https?://[^\s}]+', f.get(fld, ''))
        if m:
            return ' ' + m.group(0).rstrip('.,')
    return ''


def end(s):
    return s if s.endswith(('.', '?', '!')) else s + '.'


def entry(k, year):
    t, f = ENTS[k]
    a = authors_str(f['author']) if f.get('author') else ''
    title = clean(f.get('title', ''))
    if not a:                                               # APA 7: no author -> title moves to author slot
        rest = entry_body(t, f, title_in_front=True)
        return f"{end(title)} ({year}). {rest}".strip() + link(f)
    if not a.endswith('.'):
        a += '.'
    a = a[:-1]
    if t == 'article':
        s = f"{a}. ({year}). {end(title)} *{clean(f.get('journal', ''))}*"
        if f.get('volume'):
            s += f", *{f['volume']}*"
        if f.get('number'):
            s += f"({f['number']})"
        if f.get('pages'):
            s += f", {clean(f['pages'])}"
        s += '.'
    elif t in ('inproceedings', 'incollection'):
        s = f"{a}. ({year}). {end(title)} In "
        if t == 'incollection' and f.get('editor'):
            eds = split_authors(f['editor'])
            ed_names = []
            for e in eds:
                full = fmt_name(e)[0]
                fam, _, ini = full.partition(', ')
                ed_names.append(f"{ini} {fam}".strip())
            joined = ed_names[0] if len(ed_names) == 1 else (', '.join(ed_names[:-1]) + (', & ' if len(ed_names) > 2 else ' & ') + ed_names[-1])
            s += joined + (' (Eds.), ' if len(eds) > 1 else ' (Ed.), ')
        s += f"*{clean(f.get('booktitle', ''))}*"
        pg = clean(f.get('pages', ''))
        if pg:
            s += f" (pp. {pg})" if not pg.lower().startswith('article') else f" ({pg})"
        s += '.'
        if f.get('publisher'):
            s += f" {end(clean(f['publisher']))}"
    elif t == 'book':
        s = f"{a}. ({year}). *{end(title)}*"
        if f.get('publisher'):
            s += f" {end(clean(f['publisher']))}"
    elif t == 'techreport':
        s = f"{a}. ({year}). *{title}*"
        if f.get('number'):
            s += f" ({clean(f.get('type', 'Report'))} No. {f['number']})"
        s += '.'
        if f.get('institution'):
            s += f" {end(clean(f['institution']))}"
    elif t in ('mastersthesis', 'phdthesis'):
        kind = "Master's thesis" if t == 'mastersthesis' else 'Doctoral dissertation'
        s = f"{a}. ({year}). *{title}* [{kind}, {clean(f.get('school', ''))}]."
    else:
        s = f"{a}. ({year}). {end(title)}"
        hp = clean(f.get('howpublished', '') or f.get('institution', '') or f.get('school', ''))
        hp = re.sub(r',?\s*https?://\S+', '', hp).strip(' ,')
        if hp:
            s += f" {end(hp)}"
    if f.get('origdate'):
        s += f" (Original work published {f['origdate']})"
    return s + link(f)


def entry_body(t, f, title_in_front=False):
    if t == 'article':
        s = f"*{clean(f.get('journal', ''))}*"
        if f.get('volume'):
            s += f", *{f['volume']}*"
        if f.get('number'):
            s += f"({f['number']})"
        if f.get('pages'):
            s += f", {clean(f['pages'])}"
        return s + '.'
    return ''


def sort_key(k):
    f = ENTS[k][1]
    auths = split_authors(f['author']) if f.get('author') else ['{' + clean(f.get('title', 'zzz')) + '}']
    names = [fmt_name(x)[0].lower() for x in auths]
    return (names[0], len(names) > 1, names[1:], f.get('year', ''), clean(f.get('title', '')).lower())


keys = sorted(set(CITED), key=sort_key)
# APA year suffixes for identical author lists + year
groups = {}
for k in keys:
    f = ENTS[k][1]
    groups.setdefault((clean(f.get('author', '')), f.get('year', 'n.d.')), []).append(k)
years = {}
for (au, yr), ks in groups.items():
    if len(ks) > 1:
        for i, k in enumerate(sorted(ks, key=lambda x: clean(ENTS[x][1].get('title', '')).lower())):
            years[k] = f"{yr}{'abcdefgh'[i]}"
    else:
        years[ks[0]] = yr

block = ("\n\n### References\n\n*Generated by `literature/build_references.py` from `literature/references.bib` "
         "for the keys in `literature/cited_keys.txt` (APA 7). Each entry's verification basis and read status "
         "are in its facet file; the citation audit is in `literature/audit/`.*\n\n"
         + "\n\n".join(entry(k, years[k]) for k in keys) + "\n")
review = HERE.parent / "DRAFT.md"
text = review.read_text()
if '\n\n### References' in text:
    text = text[:text.index('\n\n### References')]
review.write_text(text + block)
suffixed = {k: v for k, v in years.items() if v[-1].isalpha()}
print(len(keys), 'references written; year suffixes:', suffixed)
