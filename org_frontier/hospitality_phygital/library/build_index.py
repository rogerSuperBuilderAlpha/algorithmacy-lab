#!/usr/bin/env python3
"""Generate CARDS_INDEX.md for the hospitality-phygital source library.

Deterministic: output depends only on the card files on disk, sorted. Adapted from
org_frontier/hegel_coordination/library/build_index.py, which is the single-manuscript variant of
org_frontier/research/build_cards_index.py.

    python build_index.py                      # rewrite CARDS_INDEX.md
    python build_index.py --check              # exit 1 if the index is stale or any card is bad
    python build_index.py --check --require-complete
                                               # additionally fail when a bib entry has no card

Why the checks are strict: this arm's own conventions — append a FOUNDATION part, update the field
map — were skipped twice, leaving two research rounds unrecorded and the map stale. State that a
human must remember to update is state that goes wrong silently. Everything here is computed from
card frontmatter, and CI runs the check.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARM = os.path.dirname(HERE)
CARDS = os.path.join(HERE, "cards")
INDEX = os.path.join(HERE, "CARDS_INDEX.md")
CLAIMS_FILE = os.path.join(HERE, "CLAIMS.md")
BIB = os.path.join(ARM, "literature", "references.bib")
CITED = os.path.join(ARM, "manuscript", "cited_keys.txt")

CLUSTERS = ["hospitality-theory", "phygital-service", "ai-automation",
            "platform-hospitality", "mediation-sovereignty"]
STATUSES = ["cited", "held", "rejected", "superseded"]
ROLES = ["evidence", "framing", "both", "null", "rival", "governor", "none"]
DEPTHS = ["full-text", "abstract", "metadata"]
TIERS = ["verified", "crossref-verified", "corrected"]
FLAGS = ["do-not-cite", "must-engage", "abstract-only-debt", "swap-candidate"]
SECTIONS = {
    1: "Introduction", 2: "Hospitality beyond seamless service",
    3: "Phygital hospitality as triadic mediation", 4: "Augmentative and substitutive",
    5: "Algorithmacy and coordinative sovereignty", 6: "Five affordances",
    7: "Against frictionless hospitality", 8: "Discussion", 9: "Conclusion",
}
DEPTH_TAG = re.compile(r"\[(full-text|abstract|metadata)\]\s*$")


def parse_list(raw):
    raw = (raw or "").strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
    return [raw.strip('"')] if raw else []


def read_card(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm, body = {}, text[m.end():] if m else text
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"([A-Za-z_]+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm, body


def bib_notes():
    """citekey -> note text, for the verification-tier cross-check."""
    if not os.path.exists(BIB):
        return {}
    text = open(BIB, encoding="utf-8").read()
    out = {}
    for block in re.split(r"\n@", text)[1:]:
        km = re.match(r"\w+\s*\{\s*([^,]+),", block)
        if not km:
            continue
        nm = re.search(r"note\s*=\s*\{(.*?)\}\s*\n?\}", block, re.S)
        out[km.group(1).strip()] = re.sub(r"\s+", " ", nm.group(1)) if nm else ""
    return out


def claim_slugs():
    if not os.path.exists(CLAIMS_FILE):
        return set()
    return set(re.findall(r"^\|\s*`([a-z0-9-]+)`", open(CLAIMS_FILE, encoding="utf-8").read(), re.M))


def validate(cards, claims, notes, cited_keys, require_complete):
    errs = []
    seen = set()
    for path, fm, body in cards:
        base = os.path.basename(path)
        ck = fm.get("citekey", "")
        def bad(msg):
            errs.append(f"{base}: {msg}")
        if not ck:
            bad("missing citekey"); continue
        if ck != base[:-3]:
            bad(f"filename does not match citekey ({ck})")
        seen.add(ck)
        status = fm.get("status", "")
        if status not in STATUSES:
            bad(f"status '{status}' not in {STATUSES}")
        if fm.get("cluster") not in CLUSTERS:
            bad(f"cluster '{fm.get('cluster')}' not in {CLUSTERS}")
        if fm.get("role") not in ROLES:
            bad(f"role '{fm.get('role')}' not in {ROLES}")
        depth = fm.get("read_depth", "")
        if depth not in DEPTHS:
            bad(f"read_depth '{depth}' not in {DEPTHS}")
        if fm.get("verified") not in TIERS:
            bad(f"verified '{fm.get('verified')}' not in {TIERS}")
        for s in parse_list(fm.get("used_by_sections")):
            if not s.isdigit() or not 1 <= int(s) <= 9:
                bad(f"section '{s}' outside 1-9")
        for c in parse_list(fm.get("claims")):
            if c not in claims:
                bad(f"claim '{c}' not in CLAIMS.md")
        for fl in parse_list(fm.get("flags")):
            if fl not in FLAGS:
                bad(f"flag '{fl}' not in {FLAGS}")
        # conditional fields
        if status == "held" and not fm.get("hold_rationale"):
            bad("status held requires hold_rationale")
        if status == "rejected" and not fm.get("rejected_reason"):
            bad("status rejected requires rejected_reason")
        if status == "superseded" and not fm.get("superseded_by"):
            bad("status superseded requires superseded_by")
        # bib reconciliation
        if status != "rejected" and ck not in notes:
            bad("not in references.bib (only rejected cards may be absent)")
        note = notes.get(ck, "")
        # rejected candidates never entered the bibliography, so there is no note to reconcile
        if status != "rejected":
            if fm.get("verified") == "crossref-verified" and "crossref-verified" not in note \
                    and "Crossref" not in note:
                bad("claims crossref-verified but the bib note does not")
        if "do-not-cite" in parse_list(fm.get("flags")) and "DO-NOT-CITE" not in note:
            bad("flagged do-not-cite but the bib note is not")
        # citedness reconciliation
        if cited_keys is not None:
            if status == "cited" and ck not in cited_keys:
                bad("status cited but absent from cited_keys.txt")
            if status != "cited" and ck in cited_keys:
                bad(f"status {status} but present in cited_keys.txt")
        # depth honesty: every key-fact bullet carries a depth tag, and a shallow card
        # may not carry a full-text-tagged line
        kf = re.search(r"^## Key facts.*?$(.*?)(?=^## |\Z)", body, re.S | re.M)
        if kf:
            for line in kf.group(1).splitlines():
                if not line.strip().startswith("- "):
                    continue
                tag = DEPTH_TAG.search(line.strip())
                if not tag:
                    bad("key-fact line without a depth tag: " + line.strip()[:48])
                elif depth in ("abstract", "metadata") and tag.group(1) == "full-text":
                    bad("card is " + depth + " but a key fact claims [full-text]")
    if cited_keys is not None:
        for k in sorted(cited_keys - seen):
            errs.append(f"cited_keys.txt: {k} has no card")
    if require_complete:
        for k in sorted(set(notes) - seen):
            errs.append(f"references.bib: {k} has no card")
    return errs


def build(cards):
    n = len(cards)
    runs = sorted({fm.get("generated_run", "") for _, fm, _ in cards} - {""})
    by_status, by_cluster, by_depth = {}, {}, {}
    for _, fm, _ in cards:
        by_status[fm.get("status", "?")] = by_status.get(fm.get("status", "?"), 0) + 1
        by_cluster.setdefault(fm.get("cluster", "?"), []).append(fm)
        by_depth[fm.get("read_depth", "?")] = by_depth.get(fm.get("read_depth", "?"), 0) + 1

    L = ["# Hospitality phygital — source library card index", "",
         "*Generated by `build_index.py`. Do not edit by hand; edits are overwritten.*", ""]
    if not cards:
        return "\n".join(L + ["*No cards yet.*", ""]).rstrip() + "\n"
    L += [f"**{n} cards.** Newest run: `{runs[-1] if runs else '—'}`.", "",
          "Status: " + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items()))
          + ".  Read depth: " + ", ".join(f"{k} {v}" for k, v in sorted(by_depth.items())) + ".", "",
          "A card exists for every source the research touched, including candidates that were "
          "weighed and declined. `rejected` cards carry the displacement argument that kept them "
          "out; that is the record a reviewer response needs. Claim slugs are defined in "
          "[`CLAIMS.md`](CLAIMS.md); venue-level exclusions in "
          "[`VENUE_RULINGS.md`](VENUE_RULINGS.md).", ""]

    open_debts = [fm for _, fm, _ in cards
                  if set(parse_list(fm.get("flags"))) & {"abstract-only-debt", "must-engage"}]
    if open_debts:
        L += ["## Open debts", "", "| citekey | flags | what it needs |", "|---|---|---|"]
        for fm in sorted(open_debts, key=lambda f: f.get("citekey", "")):
            need = ("full text read" if "abstract-only-debt" in parse_list(fm.get("flags"))
                    else "engagement in the manuscript")
            L.append(f"| [{fm['citekey']}](cards/{fm['citekey']}.md) | "
                     f"{', '.join(parse_list(fm.get('flags')))} | {need} |")
        L.append("")

    L += ["## By manuscript section", "",
          "The contextual view: which sources carry which claim, where. Unmarked entries are cited in the "
          "manuscript; the rest are held, rejected or superseded and are listed so the alternatives "
          "considered for each claim stay visible.", ""]
    for num in sorted(SECTIONS):
        rows = [fm for _, fm, _ in cards if str(num) in parse_list(fm.get("used_by_sections"))]
        if not rows:
            continue
        L.append(f"**§{num}. {SECTIONS[num]}**")
        MARK = {"cited": "", "held": " *(held)*", "rejected": " *(rejected)*",
                "superseded": " *(superseded)*"}
        by_claim = {}
        for fm in rows:
            label = fm["citekey"] + MARK.get(fm.get("status"), "")
            for c in parse_list(fm.get("claims")) or ["(unassigned)"]:
                by_claim.setdefault(c, []).append(label)
        for c in sorted(by_claim):
            # cited sources first, so the section's actual support reads at a glance
            items = sorted(set(by_claim[c]), key=lambda s: ("*" in s, s))
            L.append(f"- `{c}` — " + ", ".join(items))
        L.append("")

    L += ["## By cluster", ""]
    for cl in CLUSTERS:
        rows = by_cluster.get(cl, [])
        if not rows:
            continue
        counts = {}
        for fm in rows:
            counts[fm.get("status")] = counts.get(fm.get("status"), 0) + 1
        L.append(f"**{cl}** — {len(rows)} cards ("
                 + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + ")")
        L.append("")

    L += ["## All cards", "",
          "| citekey | title | year | cluster | status | role | §§ | depth | verified |",
          "|---|---|---|---|---|---|---|---|---|"]
    for _, fm, _ in cards:
        title = (fm.get("title", "") or "").replace("|", "\\|")
        if len(title) > 62:
            title = title[:59] + "…"
        L.append("| [{ck}](cards/{ck}.md) | {t} | {y} | {cl} | {st} | {ro} | {se} | {dp} | {ve} |"
                 .format(ck=fm.get("citekey", "?"), t=title, y=fm.get("year", "—"),
                         cl=fm.get("cluster", "—"), st=fm.get("status", "—"),
                         ro=fm.get("role", "—"),
                         se=" ".join(parse_list(fm.get("used_by_sections"))) or "—",
                         dp=fm.get("read_depth", "—"), ve=fm.get("verified", "—")))
    return "\n".join(L).rstrip() + "\n"


def main():
    paths = sorted(glob.glob(os.path.join(CARDS, "*.md")))
    cards = []
    for p in paths:
        fm, body = read_card(p)
        cards.append((p, fm, body))
    cited = None
    if os.path.exists(CITED):
        cited = {l.strip() for l in open(CITED) if l.strip() and not l.startswith("#")}
    errs = validate(cards, claim_slugs(), bib_notes(), cited, "--require-complete" in sys.argv)
    out = build(cards)

    if "--check" in sys.argv:
        cur = open(INDEX).read() if os.path.exists(INDEX) else ""
        if cur != out:
            errs.append("CARDS_INDEX.md is STALE — run build_index.py")
        if errs:
            print(f"hospitality library FAIL ({len(errs)} problems)")
            for e in errs[:40]:
                print("  " + e)
            if len(errs) > 40:
                print(f"  … and {len(errs) - 40} more")
            sys.exit(1)
        print("hospitality library OK")
        return
    with open(INDEX, "w") as f:
        f.write(out)
    print(f"wrote {INDEX} ({len(cards)} cards)")
    if errs:
        print(f"WARNING {len(errs)} problems:")
        for e in errs[:20]:
            print("  " + e)


if __name__ == "__main__":
    main()
