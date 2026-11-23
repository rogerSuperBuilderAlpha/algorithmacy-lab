"""Compare each problem's statement + example text in the key (lines 2815-6025) with the student sheet (1570-3145)."""
import re, sys
KEY = "/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Solutions.md"
SHEET = "/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_In_Class_Board_Problems.md"
def blocks(path, lo, hi, stop):
    lines = open(path).read().split("\n")[lo - 1:hi]
    out, cur, title = {}, None, None
    for ln in lines:
        m = re.match(r"\*\*#(\d+) ", ln)
        if m:
            title = m.group(1); cur = []; out[title] = cur; continue
        if title and cur is not None:
            if ln.startswith(stop):
                cur = None; continue
            cur.append(ln)
    return {k: " ".join(" ".join(v).split()) for k, v in out.items()}
k = blocks(KEY, 2815, 6025, "**Solution")
s = blocks(SHEET, 1570, 3145, "Start with")
for pid in k:
    same = k[pid] == s.get(pid)
    print(f"#{pid:<5} identical statement+example: {same}")
    if not same:
        print("   KEY  :", k[pid][:400]); print("   SHEET:", s.get(pid, "")[:400])
