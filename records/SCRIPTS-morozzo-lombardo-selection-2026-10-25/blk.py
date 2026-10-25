import json,re,bisect
v1=open('v1.txt').read(); v2=open('v2.txt').read(); full=v1+v2; v2start=len(v1)
e1=v1.find('\x0cERRATA'); e2=full.find('INDICE',v2start+200000)
H={int(k):v for k,v in json.load(open('H3.json')).items()}
INN=re.compile(r'In\s+nomine|[Il1]n\s+nom[iíl]ne|In\s+Christi\s+nomine|In\s+Dei\s+nomine|In\s+nomine')
SIZE=re.compile(r'\b\d{2,3}\s*[xX×»]\s*\d{2,3}\b|\b(Buona|Mediocre|Ottima|Ottim|Cattiva|Calliva|Pessima|Discreta)\b|Edit[ao]\s+da')
def blocks(a,b):
    out=[];cur=a
    while True:
        m=SIZE.search(full,cur,b)
        if not m: break
        out.append(m.start())
        i=INN.search(full,m.end(),b)
        if not i: break
        cur=i.end()
    return out
B=blocks(H[1]['p'],e1)+blocks(v2start,e2)
print('blocks',len(B))
# compare against headers: for each anchor n, number of blocks between H[n] and H[n+1]
bad=[]
ks=sorted(H)
for i,k in enumerate(ks[:-1]):
    a,b=H[k]['p'],H[ks[i+1]]['p']
    c=sum(1 for x in B if a<=x<b)
    if c!=ks[i+1]-k: bad.append((k,ks[i+1],c))
print(len(bad)); print(bad[:80])
json.dump(B,open('B.json','w'))
