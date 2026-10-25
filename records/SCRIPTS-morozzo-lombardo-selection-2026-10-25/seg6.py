import json,re
v1=open('v1.txt').read(); v2=open('v2.txt').read(); full=v1+v2; v2start=len(v1)
e1=v1.find('\x0cERRATA'); e2=full.find('INDICE',v2start+200000)
H={int(k):v for k,v in json.load(open('H2.json')).items()}
# fix 238: must not start at 'Zacc'
del H[238]
INN=re.compile(r'In\s+nomine|[Il1]n\s+nom[iíl]ne|In\s+Christi\s+nomine|In\s+Dei')
SIZE=re.compile(r'\b\d{2,3}\s*[xX×»]\s*\d{2,3}\b|\b(Buona|Mediocre|Ottima|Cattiva|Calliva|Pessima|Discreta)\b')
END=re.compile(r'(roborav\w*|complev\w*|corroborav\w*|interfui\w*|subscripsi)[\.,]?')
def blocks(a,b):
    """archival-block positions: SIZE hits not inside Latin body — i.e. after an END and before the next INN"""
    out=[];cur=a
    while True:
        m=SIZE.search(full,cur,b)
        if not m: break
        out.append(m.start())
        i=INN.search(full,m.end(),b)
        if not i: break
        cur=i.end()
    return out
miss=sorted(n for n in range(1,866) if n not in H)
log={}
for n in miss:
    prv=max(k for k in H if k<n); nxt=min(k for k in H if k>n)
    a,b=H[prv]['p'],H[nxt]['p']
    bl=blocks(a,b)
    need=nxt-prv  # number of acts expected in [a,b)
    if len(bl)==need:
        # split before the block belonging to act n: block index n-prv
        k=n-prv; bpos=bl[k]
        ends=[m.end() for m in END.finditer(full,bl[k-1],bpos)]
        if ends:
            sp=full.find('\n',ends[-1]); sp=sp if sp<bpos else ends[-1]
            H[n]=dict(p=sp,raw='',first=re.sub(r'\s+',' ',full[sp:sp+60]),how='blocksplit')
            log[n]='ok'; continue
    log[n]=f'blocks={len(bl)} need={need}'
print({k:v for k,v in log.items()})
print('missing now',[n for n in range(1,866) if n not in H])
json.dump({k:v for k,v in H.items()},open('H3.json','w'),ensure_ascii=False)
