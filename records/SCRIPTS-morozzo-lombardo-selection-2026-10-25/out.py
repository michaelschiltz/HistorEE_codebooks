import json,csv,collections as co,re
R=json.load(open('R2.json'))
chk1={3:'type ok (only the regest opening is on the page checked; fondo and year not seen)',27:'ok',89:'ok',196:'ok',301:'ok',303:'ok after rule change (first pass: loan)',315:'ok after rule change (first pass: attestation)',328:'ok after rule change (first pass: attestation)',386:'ok; place not extracted',436:'ok after rule change (first pass: attestation); place not extracted',492:'ok',525:'ok',556:'ok',557:'ok (Testificor of a ministerialis: enforcement report)',585:'ok',592:'ok',637:'ok',744:'ok',788:'ok after incision fix (first pass: incised missed)',824:'ok'}
extra={52:'ok after year fix (first pass took endorsement year)',297:'fondo unresolved by script; image: S. Zacc. B. 25; year ok after fix',356:'ok',389:'ok',829:'ok after regex fix (first pass: property, "Donato" matched)'}
chk2={21:'ok',60:'ok (debt obligation classed loan / deposit: defensible)',83:'ok',115:'ok',213:'ok',226:'ok',252:'ok',334:'ok; place not extracted',433:'ok (Testificamur on a judicial decision)',644:'ok',690:'type wrong (other; "Lo stesso" series not inherited) -> fixed',811:'incised missed: the OCR text layer lost the line -> stays missed'}
rows=[]
for r in R:
    n=int(r['n'])
    v=''
    if n in chk1: v='sample1: '+chk1[n]
    elif n in extra: v='extra: '+extra[n]
    elif n in chk2: v='sample2: '+chk2[n]
    rows.append(dict(act=n,vol=r['vol'],pdf_page=r['pdfpage'],segmentation=r['seg'],fondo=r['fondo'],fondo_group=r['F'],year=r['year'] or '',period=r['period'],place=r['place'],dispositive_formula=r['opening'],act_type=r['T'],type_basis=r['T_src'],type_from_regest=r['T_regest'],formula_regest_agree=r['agree'],copy_flag=r['copy_in_head'],incised_flag=r['incised'],previously_edited_flag=r['edited_before'],mairano_flag=r['mairano'],investment_related=r['invest_rel'],written_overseas=r['overseas'],regest_similarity_prev=r['sim_prev'],image_check=v))
with open('CORPUS-morozzo-lombardo-2026-10-25.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# padded md tables
def md(header,data):
    cols=list(zip(*([header]+data))); wd=[max(len(str(x)) for x in c) for c in cols]
    line=lambda row:'| '+' | '.join(str(x).ljust(wd[i]) for i,x in enumerate(row))+' |'
    return '\n'.join([line(header),'| '+' | '.join('-'*wd[i] for i in range(len(wd)))+' |']+[line(r) for r in data])
P=['<1150','1150-1199','1200-1229','1230-1261']
FO=['S. Zaccaria','Procuratori','Canc. Inferiore','other convents','miscellanies','unresolved']
TY=[k for k,_ in co.Counter(r['T'] for r in R).most_common()]
def ct(rows_,key,val): return sum(1 for r in rows_ if r[key]==val)
t1=[[t]+[ct([r for r in R if r['F']==f],'T',t) for f in FO]+[ct(R,'T',t)] for t in TY]+[['total']+[ct(R,'F',f) for f in FO]+[len(R)]]
print(md(['act type']+FO+['all'],t1)); print()
t2=[[t]+[ct([r for r in R if r['period']==p],'T',t) for p in P]+[ct([r for r in R if r['period']==''],'T',t)] for t in TY]+[['total']+[ct(R,'period',p) for p in P]+[ct(R,'period','')]]
print(md(['act type']+P+['undated'],t2)); print()
t3=[[f]+[ct([r for r in R if r['period']==p],'F',f) for p in P]+[ct([r for r in R if r['period']==''],'F',f),ct(R,'F',f)] for f in FO]
print(md(['fondo']+P+['undated','all'],t3)); print()
print(co.Counter(r['fondo'] for r in R).most_common())
