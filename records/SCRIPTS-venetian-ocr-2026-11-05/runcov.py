import json,sys,cover
from concurrent.futures import ProcessPoolExecutor
acts=json.load(open('acts.json')); layer=sys.argv[1]  # 'o' old, 'v' new
pages=sorted({(a['vol'],p) for a in acts for p in range(a['p0'],a['p1']+1)})
def run(vp):
    v,p=vp; n,f=cover.check(f'{layer}{v}.pdf',p); return v,p,n,f
with ProcessPoolExecutor(8) as ex: R=list(ex.map(run,pages))
out={f'{v}:{p}':f for v,p,n,f in R if f}
print(layer,len(pages),'pages',sum(n for _,_,n,_ in R),'lines; flagged lines',sum(len(f) for f in out.values()),'on',len(out),'pages')
json.dump(out,open(f'cov_{layer}.json','w'))
