import json,re
v1=open('v1.txt').read(); v2=open('v2.txt').read(); full=v1+v2; v2start=len(v1)
e1=v1.find('\x0cERRATA'); e2=full.find('INDICE',v2start+200000)
H={int(k):v for k,v in json.load(open('H3.json')).items()}
H[346]=dict(p=907305,raw='346',first='(fragment) Pellegrino Fabro promette',how='manual')
H[364]=dict(p=948734,raw='364',first='Giovanni Conciaboile fa quietanza',how='manual')
B=json.load(open('B.json'))
END=re.compile(r'(roborav\w*|complev\w*|corroborav\w*|interfui|subscripsi|scripsi|ampliavi)[\.,]?')
def nb(a,b): return [x for x in B if a<=x<b]
def runs():
    ks=sorted(n for n in H); out=[]
    for i,k in enumerate(ks[:-1]):
        c=len(nb(H[k]['p'],H[ks[i+1]]['p']))
        out.append((k,ks[i+1],c))
    return out
mis=[r for r in runs() if r[2]!=r[1]-r[0]]
# cluster adjacent mismatches
cl=[]
for r in mis:
    if cl and cl[-1][1]==r[0]: cl[-1]=(cl[-1][0],r[1],cl[-1][2]+r[2])
    else: cl.append(r)
fixed=[];left=[]
for a,b,c in cl:
    if c==b-a and c>0:
        bl=nb(H[a]['p'],H[b]['p'])
        for j,n in enumerate(range(a,b)):
            if j==0:
                # first act keeps its start unless its header is after its block
                if H[a]['p']>bl[0]: pass
                continue
            prevb=bl[j-1]; bpos=bl[j]
            ends=[m for m in END.finditer(full,prevb,bpos)]
            if not ends: left.append((a,b,'noend',n)); break
            sp=full.find('\n',ends[-1].end()); sp=sp if 0<sp<bpos else ends[-1].end()
            H[n]=dict(p=sp,raw='',first=re.sub(r'\s+',' ',full[sp:sp+70]).strip(),how='blockrenumber')
        fixed.append((a,b))
    else: left.append((a,b,c))
print('fixed',fixed); print('left',left)
mis2=[r for r in runs() if r[2]!=r[1]-r[0]]
print('remaining mismatch intervals',len(mis2),mis2)
print('missing',[n for n in range(1,866) if n not in H])
json.dump({k:v for k,v in H.items()},open('H4.json','w'),ensure_ascii=False)
