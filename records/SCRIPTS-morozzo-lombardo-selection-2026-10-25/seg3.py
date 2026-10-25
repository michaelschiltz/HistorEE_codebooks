import re,json,bisect
v1=open('v1.txt').read(); v2=open('v2.txt').read()
full=v1+v2; v2start=len(v1); e1=v1.find('\x0cERRATA')
e2=full.find('INDICE',v2start+200000)
HDR=re.compile(r'(?m)^[ \t]*([0-9IlOoSsAM\$\]\|]{1,4})([\.,]?)[ \t]*(?:\n|(?=[ \t]+[A-Z][a-zà-ù]+\s))')
ARCH=re.compile(r'(Buona|Bnona|Mediocre|Ottima|Ottim|Otti\b|Cattiva|Calliva|Pessima|Discreta|Discrela|Busta|Edit[ao]\s|\b\d{2,3}\s*[xX×»]\s*\d{2,3}\b)')
RUN=re.compile(r'^\s*(R\.\s*MOROZZO.*|.*DOCUMENTI.*|DEL COMMERCIO.*|.*COMMERCIO.*|\d{1,3}|-|A\. ?LOMBARDO|ROCCA|MOROZZO|DELLA|SEC[\.,].*|XI.*|NEI|VENEZIANO|\s*|.{0,3})\s*$')
BADFIRST=re.compile(r'^(Ego|Zac|Zacc|Giorgio|Notitia|Signum|S\.T|Proc|Canc|Museo|Att|In nomine|Dominicus|Iohannes|Petrus|Domini|Anno|Rivo)')
def parse(s):
    s=s.translate(str.maketrans('OoIlSs$A]|M','00115561111'))
    return int(s) if s.isdigit() else None
cands=[]
for m in HDR.finditer(full):
    p=m.start()
    if (e1<p<v2start) or p>e2 or p<60000: continue
    after=full[m.end():m.end()+1400]
    inn=re.search(r'In\s+nomine|[Il1]n\s+nom[iíl]ne|In\s+Christi|In\s+Dei',after)
    zone=after[:inn.start()] if inn else after[:1000]
    lines=[l for l in zone.split('\n') if not RUN.match(l)]
    if not lines: continue
    first=lines[0].strip()
    if BADFIRST.match(first) or not re.match(r'[A-ZÈÀ«\[\(|][a-zà-ù\'’ ,]',first): continue
    if not ARCH.search(zone): continue
    cands.append(dict(p=p,raw=m.group(1),dot=m.group(2),num=parse(m.group(1)),first=first[:60]))
# anchors: dotted, parsed, LIS by number over position
C=[c for c in cands if c['dot'] and c['num'] and 1<=c['num']<=865]
# LIS with strictly increasing num
import itertools
tails=[];tidx=[];prev=[None]*len(C)
for i,c in enumerate(C):
    k=bisect.bisect_left(tails,c['num'])
    if k==len(tails): tails.append(c['num']); tidx.append(i)
    else: tails[k]=c['num']; tidx[k]=i
    prev[i]=tidx[k-1] if k>0 else None
seq=[];i=tidx[-1]
while i is not None: seq.append(C[i]); i=prev[i]
seq=seq[::-1]
H={c['num']:c for c in seq}
print('cands',len(cands),'anchors',len(H))
missing=[n for n in range(1,866) if n not in H]
print('missing',len(missing),missing)
json.dump(dict(cands=cands,H={k:v for k,v in H.items()}),open('seg3.json','w'),ensure_ascii=False)
