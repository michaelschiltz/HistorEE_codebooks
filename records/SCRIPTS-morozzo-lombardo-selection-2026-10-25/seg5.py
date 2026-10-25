import json,re
v1=open('v1.txt').read(); v2=open('v2.txt').read(); full=v1+v2
H={int(k):v for k,v in json.load(open('H.json')).items()}
VERB=re.compile(r"\b(fa|fanno|stipula|stipulano|riceve|ricevono|dà|danno|attesta|attestano|dichiara|dichiarano|contrae|contraggono|compra|comprano|vende|vendono|si obblig|costituisce|promette|promettono|depositano|deposita|cede|rilascia|nomina|sentenza|giudizio|Giudizio|procede|scrive|conferma|restituisce|assume|consegna|presta|prende|concede|investe|riconosce|testimonia|chiede|incarica|affida|garantisce|accetta|rinuncia|elegge|delega|libera|impegna)\b")
HDRL=re.compile(r'(?m)^[ \t]*(\S{1,5}?)[\.,]?[ \t]*$|(?m)^[ \t]*(\d{1,3})[\.,][ \t]+(?=[A-Z])')
def parse(s):
    s=(s or '').translate(str.maketrans('OoIlSs$A]|M','00115561111'))
    return int(s) if s.isdigit() else None
miss=[n for n in range(1,866) if n not in H]
order=sorted(H)
res={}
for n in miss:
    lo=max([H[k]['p'] for k in H if k<n],default=40000); hi=min([H[k]['p'] for k in H if k>n],default=len(full))
    if n==271: lo=max(H[k]['p'] for k in H if k<n-1)  # print order 269,271,270
    best=[]
    for m in HDRL.finditer(full,lo+1,hi):
        raw=m.group(1) or m.group(2)
        if not raw or not re.search(r'\d',raw): continue
        if re.match(r'\s*\(',raw): continue
        after=full[m.end():m.end()+400]
        txt=re.sub(r'(?m)^\s*(R\.\s*MOROZZO.*|.*DOCUMENTI.*|.*COMMERCIO.*|\d{1,3}|-|A\. ?LOMBARDO|ROCCA|MOROZZO|DELLA|SEC.*|XI.*|NEI|VENEZIANO)\s*$','',after)
        txt=re.sub(r'\s+',' ',txt).strip()
        if not re.match(r"[A-ZÈ«\|\[][a-zà-ù'’]",txt): continue
        vm=VERB.search(txt[:160])
        if not vm: continue
        if re.search(r'\b(Ego|testis|subscripsi|quidem|nostri)\b',txt[:vm.start()]): continue
        num=parse(raw); score=(0 if num==n else 1, abs((num or 9999)-n))
        best.append((score,m.start(),raw,txt[:70]))
    best.sort()
    res[n]=best[:3]
    if best and (len(best)==1 or best[0][0]<best[1][0] or n in (99,)):
        H[n]=dict(p=best[0][1],raw=best[0][2],first=best[0][3],how='gapfill2')
for n in miss: print(n,'->',('OK ' if n in H else '?? '),res[n][:2])
json.dump({k:v for k,v in H.items()},open('H2.json','w'),ensure_ascii=False)
print(len(H),[n for n in range(1,866) if n not in H])
