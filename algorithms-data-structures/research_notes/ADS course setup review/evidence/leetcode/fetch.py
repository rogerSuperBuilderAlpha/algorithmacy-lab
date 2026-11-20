import json,subprocess,time
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
slugs=set()
for f in ('Board','Solutions','TH'):
    for r in json.load(open(f+'.json')):
        if r['url']: slugs.add(r['url'].rstrip('/').split('/')[-1])
        else: print('no url',f,r)
res={}
for s in sorted(slugs):
    q=json.dumps({"query":"query q($s:String!){question(titleSlug:$s){questionFrontendId title titleSlug difficulty isPaidOnly topicTags{name} stats}}","variables":{"s":s}})
    for t in range(3):
        o=subprocess.run(['curl','-s','-m','40','-A',UA,'-H','Content-Type: application/json','-H','Referer: https://leetcode.com','-d',q,'https://leetcode.com/graphql'],capture_output=True,text=True).stdout
        try:
            d=json.loads(o)['data']['question']; break
        except Exception: d=None; time.sleep(2)
    res[s]=d
    if d is None: print('FAIL',s,o[:100])
    time.sleep(0.3)
json.dump(res,open('lc.json','w'),indent=1)
print(len(slugs))
