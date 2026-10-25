import json,re
v1=open('v1.txt').read(); v2=open('v2.txt').read(); full=v1+v2; v2start=len(v1)
e1=v1.find('\x0cERRATA'); e2=full.find('INDEX LOCORUM',v2start+200000)
H={int(k):v for k,v in json.load(open('H4.json')).items()}
B=json.load(open('B.json'))
END=re.compile(r'(roborav\w*|complev\w*|corroborav\w*|interfui|subscripsi|scripsi)[\.,]?')
H[760]=dict(H[759]); H[760]['how']='manual (OCR 769)'
a=H[758]['p']; bl=[x for x in B if a<=x<H[760]['p']]
assert len(bl)==2,bl
ends=list(END.finditer(full,bl[0],bl[1])); sp=full.find('\n',ends[-1].end())
H[759]=dict(p=sp,raw='',first=re.sub(r'\s+',' ',full[sp:sp+70]).strip(),how='blockrenumber')
order=sorted(H,key=lambda n:H[n]['p'])
acts=[]
for i,n in enumerate(order):
    p=H[n]['p']; q=H[order[i+1]]['p'] if i+1<len(order) else e2
    if p<e1<q: q=e1
    acts.append(dict(n=n,vol=1 if p<v2start else 2,p=p,how=H[n].get('how','anchor'),text=full[p:q]))
acts.sort(key=lambda a:a['n'])
assert [a['n'] for a in acts]==list(range(1,866))
json.dump(acts,open('acts3.json','w'),ensure_ascii=False)
from collections import Counter
print(Counter(a['how'] for a in acts)); print(Counter(a['vol'] for a in acts))
for n in [14,15,112,113,357,358,759,760,270,271]:
    a=acts[n-1]; print(n,a['how'],repr(re.sub(r'\s+',' ',a['text'][:110])))
