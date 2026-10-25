import json,re
d=json.load(open('seg3.json')); cands=d['cands']; H={int(k):v for k,v in d['H'].items()}
used={c['p'] for c in H.values()}
miss=[n for n in range(1,866) if n not in H]
def bounds(n):
    lo=max([H[k]['p'] for k in H if k<n],default=0); hi=min([H[k]['p'] for k in H if k>n],default=10**9)
    return lo,hi
amb=[]
for n in miss:
    lo,hi=bounds(n)
    cs=[c for c in cands if lo<c['p']<hi and c['p'] not in used]
    if len(cs)==1: H[n]=cs[0]; used.add(cs[0]['p']); H[n]['how']='gapfill'
    else: amb.append((n,lo,hi,[(c['p'],c['raw'],c['first'][:40]) for c in cs]))
for a in amb: print(a)
json.dump({k:v for k,v in H.items()},open('H.json','w'),ensure_ascii=False)
print(len(H))
