"""Copy MODEL_FULL.md (git-ignored, verbatim) to MODEL.md (committed).

Copies only. Each quoted model sentence becomes its first five and last four
words joined by an ellipsis; displayed quotations become a pointer. The
analysis lines are copied unchanged. Usage: redact_model.py FULL OUT
"""
import re, sys

full, out = sys.argv[1], sys.argv[2]
lines = open(full, encoding="utf-8").read().splitlines()
res = []
for ln in lines:
    if ln.startswith('> "') and ln.endswith('"'):
        words = ln[3:-1].split()
        if len(words) > 10:
            ln = '> "' + " ".join(words[:5]) + " … " + " ".join(words[-4:]) + '"'
    elif ln.startswith("> [Displayed"):
        ln = "> [Displayed quotation: the text is in the git-ignored MODEL_FULL.md.]"
    res.append(ln)
text = "\n".join(res) + "\n"
text = text.replace(
    "GIT-IGNORED: this file quotes the whole article and stays in the corpus folder. The committed v8_2026-11/MODEL.md is copied from it with each quotation cut to its opening and closing words.",
    "COMMITTED COPY of the git-ignored rewrite_2026-11/journal/corpus/germannmolz2018/MODEL_FULL.md, made by v8_2026-11/tools/redact_model.py: each sentence of ten words or more is cut to its first five and last four words, because the article is under copyright and this repository is public.")
text = text.replace("# MODEL_FULL — Germann Molz (2018), every sentence", "# MODEL — Germann Molz (2018), every sentence")
open(out, "w", encoding="utf-8").write(text)
print("entries:", len(re.findall(r"^### GM\.", text, re.M)))
