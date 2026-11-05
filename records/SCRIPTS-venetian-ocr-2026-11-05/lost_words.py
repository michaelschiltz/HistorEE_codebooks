# Separates words genuinely missing from the 2026-10-24 text layer from words that are present but misplaced.
# Input: dropped.json (dropped.py). For each flagged span, the words of the 2026-11-03 layer under the
# uncovered ink are searched (fuzzy, t/l c/e u/v folded, ratio >= 0.75) in the old layer's text of the page
# and in the bundle text of the act. Output: dropped2.json with status lost / displaced/partial / fragment.
import re,json,sys,subprocess,difflib
BUNDLE=sys.argv[1]
B=open(BUNDLE,encoding='utf-8').read()
parts=re.split(r'(?m)^=== act (\d+) \| [^\n]*===\n',B); A={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
def norm(s): return re.sub(r'[^a-z]','',s.lower().replace('l','t').replace('c','e').replace('u','v'))
D=json.load(open('dropped.json')); cache={}
def oldtext(v,p):
    if (v,p) not in cache: cache[(v,p)]=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),f'o{v}.pdf','-'],capture_output=True,text=True).stdout
    return cache[(v,p)]
def present(word,text):
    w=norm(word)
    if len(w)<3: return True
    toks=[norm(t) for t in re.split(r'\s+',text.replace('-\n',''))]
    return w in toks or any(difflib.SequenceMatcher(None,w,t).ratio()>=0.75 for t in toks if abs(len(t)-len(w))<=3)
for d in D:
    words=[w for w in d['dropped'].split() if len(norm(w))>=3]
    if not words: d['status']='fragment'; continue
    d['miss_old']=[w for w in words if not present(w,oldtext(d['vol'],d['pdf']))]
    d['miss_bundle']=[w for w in words if not present(w,A.get(d['act'],''))]
    d['status']='lost' if d['miss_old'] else 'displaced/partial'
json.dump(D,open('dropped2.json','w'),ensure_ascii=False)
