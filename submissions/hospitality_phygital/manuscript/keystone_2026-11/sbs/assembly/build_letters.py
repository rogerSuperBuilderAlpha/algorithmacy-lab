# Fills the two letter templates from final.json (sentence text by ledger id) and loc.json (section, paragraph),
# writes them to submission/*_v7.md, and checks every quoted sentence string-for-string against DRAFT_v7.md.
import json,re,subprocess
SP='/private/tmp/claude-501/-Users-ludwitt/726e3364-a25c-4111-89c8-312a57b9f782/scratchpad/assembly'
M='/Users/ludwitt/iit-playground/wt-hs-rr/submissions/hospitality_phygital/manuscript'
f=json.load(open(SP+'/final.json')); loc=json.load(open(SP+'/loc.json'))
draft=open(M+'/DRAFT_v7.md',encoding='utf-8').read()
ORD=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth']
def L(k):
    name,p=loc[k]
    if k=='S-196': return "'Assembled hosts at the touchpoint', subsection 'Six questions and four cases', after the list"
    return f"'{name}', {ORD[p-1]} paragraph"
words=re.search(r'BODY\s+([\d,]+)',subprocess.run(['python3','-I',M+'/wordcount.py',M+'/DRAFT_v7.md'],capture_output=True,text=True).stdout).group(1)
bad=[]
for src,dst in [('letter_reviewers_template.md','submission/RESPONSE_TO_REVIEWERS_v7.md'),('letter_editor_template.md','submission/RESPONSE_TO_EDITOR_v7.md')]:
    t=open(SP+'/'+src,encoding='utf-8').read()
    t=t.replace('{{WORDS}}',words)
    t=re.sub(r'\{\{L:(S-\d{3})\}\}',lambda m:L(m.group(1)),t)
    def q(m):
        k=m.group(1); s=f[k][1]
        if s not in draft: bad.append((dst,k))
        return s
    t=re.sub(r'\{\{((?:S|A)-\d+)\}\}',q,t)
    assert '{{' not in t, re.findall(r'\{\{[^}]*\}\}',t)
    # capitalise a location that opens an italic 'Changed in' clause or a table cell
    t=t.replace("| 'Assembled","| In 'Assembled").replace("| 'Conclusion'","| In 'Conclusion'")
    open(M+'/'+dst,'w',encoding='utf-8').write(t)
print('words',words,'| quotes not found in draft:',bad or 'none')
