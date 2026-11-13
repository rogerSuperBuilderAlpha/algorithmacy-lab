"""Counts for STYLE_PROFILE.md. Counts only; writes no prose.

  style_counts.py model MODEL_FULL.md    hand-split sentences from the model entries
  style_counts.py draft FILE.md          regex-split body of a Markdown draft
  style_counts.py check MODEL_FULL.md    runs the regex splitter on the model's own
                                         paragraphs and compares with the hand split
"""
import re, sys, statistics as st

ABBR = ["et al.", "e.g.", "i.e.", "cf.", "pp.", "p.", "vs.", "v.", "U.S.", "No.", "Art.",
        "para.", "paras.", "ch.", "ed.", "eds.", "Ltd.", "Co.", "Inc.", "Mr.", "Dr.", "St.",
        "n.d.", "s.", "ss.", "Sch.", "reg.", "c.", "Cal.", "App.", "Supp.", "F.", "N.Y.", "Ill."]

def split_sentences(par):
    t = par
    for i, a in enumerate(ABBR):   # whole-word matches only
        t = re.sub(r"(?<![A-Za-z])" + re.escape(a), a.replace(".", f"\u0000{i}\u0000"), t)
    t = re.sub(r"\b([A-Z])\.(?=\s[A-Z])", "\\1\u0001", t)          # initials
    parts = re.split(r"(?<=[.?!])(?:['’\"”)]*)\s+(?=[A-Z‘'\"“(\[])", t)
    out = []
    for p in parts:
        p = re.sub(r"\u0000\d+\u0000", ".", p).replace("\u0001", ".")
        if p.strip():
            out.append(p.strip())
    return out

def words(s):
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9’'-]+", s))

FP_I = re.compile(r"\b(I|my|me|myself)\b")
FP_WE = re.compile(r"\b(we|We|our|Our|us|ourselves)\b")
CITE_PAREN = re.compile(r"\([^()]*\b(1[89]|20)\d\d[a-z]?(:[^()]*)?\)")
TAG = re.compile(r"\b(anthropologist|geographer|sociologist|philosopher|historian|legal scholar|Legal scholar|brand consultant|economist|lawyer|jurist|theorist|scholar)\s+[A-Z][a-z]+\s+[A-Z]")

def report(name, paras):
    sents = [s for p in paras for s in p]
    wl = [words(s) for s in sents]
    pw = [sum(words(s) for s in p) for p in paras]
    W = sum(wl)
    text = " ".join(sents)
    q = sum(1 for s in sents if s.rstrip("'’\"”)").endswith("?"))
    k = lambda n: round(1000 * n / W, 2)
    qs = st.quantiles(wl, n=10)
    print(f"== {name}")
    print(f"words {W} | sentences {len(sents)} | paragraphs {len(paras)}")
    print(f"sentence words: mean {st.mean(wl):.1f} median {st.median(wl)} sd {st.pstdev(wl):.1f} "
          f"p10 {qs[0]:.0f} p90 {qs[8]:.0f} max {max(wl)}")
    print(f"  share <=10w {sum(w<=10 for w in wl)/len(wl):.0%} | share >=40w {sum(w>=40 for w in wl)/len(wl):.0%}")
    print(f"paragraph words: mean {st.mean(pw):.0f} median {st.median(pw)} min {min(pw)} max {max(pw)}")
    print(f"questions {q} ({k(q)}/1000w)")
    print(f"first person I/my/me {len(FP_I.findall(text))} ({k(len(FP_I.findall(text)))}/1000w); "
          f"we/our/us {len(FP_WE.findall(text))} ({k(len(FP_WE.findall(text)))}/1000w)")
    dash = text.count(" – ") + text.count("—") + text.count(" -- ")
    print(f"dashes {dash} ({k(dash)}/1000w) | semicolons {text.count(';')} ({k(text.count(';'))}/1000w) | colons {text.count(':')} ({k(text.count(':'))}/1000w)")
    print(f"'In other words' {text.count('In other words')} | parenthetical citations {len(CITE_PAREN.findall(text))} ({k(len(CITE_PAREN.findall(text)))}/1000w) | trade tags {len(TAG.findall(text))}")
    print(f"single-quote marks ‘/' {text.count('‘') + len(re.findall(chr(39)+'[A-Za-z]', text))} | double “/\" {text.count('“') + text.count(chr(34))}")

def model_paras(path):
    paras, cur, key = [], [], None
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"^### GM\.\d+ · (\w+) ¶(\d+) (\S+)", ln)
        if m:
            k2 = (m.group(1), m.group(2))
            disp = m.group(3) == "DISPLAY"
            if k2 != key:
                if cur: paras.append(cur)
                cur, key = [], k2
            continue
        if ln.startswith('> "') and not disp:
            cur.append(ln.strip()[3:-1])
    if cur: paras.append(cur)
    return paras

def draft_paras(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if re.match(r"^##\s+(\d+\.\s+)?Introduction", l))
    end = next(i for i, l in enumerate(lines) if i > start and re.match(r"^##\s+(Acknowledg|References)", l))
    blocks, cur = [], []
    for l in lines[start:end] + [""]:
        if not l.strip() or l.startswith("#") or l.startswith("|") or l.startswith("!["):
            if cur: blocks.append(" ".join(cur)); cur = []
            continue
        if l.startswith(">") or l.startswith("<!--"):
            continue
        cur.append(re.sub(r"^\s*([-*]|\d+\.)\s+", "", l).strip())
    return [split_sentences(re.sub(r"\*\*?|`", "", b)) for b in blocks if words(b) > 3]

mode, path = sys.argv[1], sys.argv[2]
if mode == "model":
    report("model (hand split)", model_paras(path))
elif mode == "draft":
    report(path.split("/")[-1], draft_paras(path))
elif mode == "check":
    hand = model_paras(path)
    regex = [split_sentences(" ".join(p)) for p in hand]
    nh, nr = sum(map(len, hand)), sum(map(len, regex))
    agree = sum(1 for h, r in zip(hand, regex) if len(h) == len(r))
    print(f"splitter check on the model: hand {nh} sentences, regex {nr}; paragraphs with equal counts {agree}/{len(hand)}")
    for h, r in zip(hand, regex):
        if len(h) != len(r):
            print("  differs:", len(h), "vs", len(r), "|", h[0][:60])
    report("model (regex split)", regex)
