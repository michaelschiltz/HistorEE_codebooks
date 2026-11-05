# Census incised_flag against the 2026-11-03 layer: each act's text from its header to the next header
# (pdftotext -raw, pages p-1..p+1) is searched for "Carta incisa" and OCR variants. Disagreements were read on the page image.
import csv,sys,re,subprocess,collections as co
C=list(csv.DictReader(open(sys.argv[1],encoding='utf-8')))
INC=re.compile(r"[Cc]ar[tl]a\s*['’i]?\s*[il1]?n?[cec][i'’1l]?[sx]a|\bincis[ae]\b|ncisa|inc['’]sa",re.I)
pages={v:subprocess.run(['pdftotext','-raw',f,'-'],capture_output=True,text=True).stdout.split('\f') for v,f in (('1','v1.pdf'),('2','v2.pdf'))}
byvol=co.defaultdict(list)
for r in C: byvol[r['vol']].append(r)
for v,rows in byvol.items():
    rows.sort(key=lambda r:int(r['act']))
    for i,r in enumerate(rows):
        p=int(r['pdf_page']); t='\n'.join(pages[v][p-2:p+1]); off=len('\n'.join(pages[v][p-2:p-1]))+1 if p>=2 else 0
        c=list(re.finditer(r'(?m)^\s*\S{0,2}?'+r['act']+r'\s*[\.,]\s',t)); m=min(c,key=lambda m:abs(m.start()-off)) if c else None
        s=m.end() if m else off; nxt=rows[i+1]['act'] if i+1<len(rows) else None
        mm=re.search(r'(?m)^\s*\S{0,2}?'+nxt+r'\s*[\.,]\s',t[s:]) if nxt else None
        seg=t[s:(s+mm.start() if mm else s+1500)][:1500]; layer=1 if INC.search(seg) else 0
        if str(layer)!=r['incised_flag']: print(r['act'],v,p,'census',r['incised_flag'],'layer',layer)
