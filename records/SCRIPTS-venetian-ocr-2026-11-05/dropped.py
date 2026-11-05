import json,re,cover
acts=json.load(open('acts.json')); F=json.load(open('cov_o.json'))
# act header y positions on new layer, per page
def hdrs(v,p):
    a,ws=cover.page(f'v{v}.pdf',p); W=a.shape[1]
    return [(w[1],int(w[4].rstrip('.'))) for w in ws if re.fullmatch(r'\d{1,3}\.',w[4]) and w[0]<W*0.3]
out=[]
for key,flags in F.items():
    v,p=key.split(':'); p=int(p)
    a,ws=cover.page(f'v{v}.pdf',p); H=hdrs(v,p)
    for f in flags:
        cy=(f['y0']+f['y1'])/2
        spans=[tuple(map(int,s.split('-'))) for s in f['why'].replace('uncovered ink x=','').split(',')] if 'uncovered' in f['why'] else [(0,10**6)]
        lw=sorted([w for w in ws if w[1]-3<=cy<=w[3]+3],key=lambda w:w[0])
        drop=[w[4] for w in lw if any(w[0]-4<=s1 and w[2]+4>=s0 for s0,s1 in spans)]
        line=' '.join(w[4] for w in lw)
        # which act: last header above cy on this page, else first act whose range covers page
        above=[n for y,n in H if y<=cy]
        cands=[x['act'] for x in acts if x['vol']==v and x['p0']<=p<=x['p1']]
        act=above[-1] if above and above[-1] in cands else (max([c for c in cands if c<=(H[0][1] if H else 10**6)] or cands or [None]))
        out.append(dict(vol=v,pdf=p,y=f['y0'],act=act,dropped=' '.join(drop),line=line))
json.dump(out,open('dropped.json','w'),ensure_ascii=False)
print(len(out))
