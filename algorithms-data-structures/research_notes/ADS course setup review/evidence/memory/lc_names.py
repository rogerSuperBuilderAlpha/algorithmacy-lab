"""Compare each take-home row (number | name) with its LeetCode URL slug (slug must equal the slugified name)."""
import re
L=open("/private/tmp/claude-501/-Users-ludwitt/a080b693-6f9a-4f5c-ae23-c8dd636db04a/scratchpad/ads/ADS_Take_Homes.md").read().split("\n")
rows=[];cur=None
for l in L:
    m=re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(Easy|Medium|Hard)\s*\|",l)
    if m: cur=(m.group(1),m.group(2)); continue
    u=re.search(r"leetcode\.com/problems/([^/)\]]+)",l)
    if u and cur: rows.append((cur[0],cur[1],u.group(1))); cur=None
bad=0
for n,name,slug in rows:
    s=re.sub(r"[^a-z0-9]+","-",name.lower()).strip("-")
    if s!=slug: bad+=1; print("MISMATCH",n,name,"->",s,"vs",slug)
print("rows",len(rows),"mismatch",bad)
