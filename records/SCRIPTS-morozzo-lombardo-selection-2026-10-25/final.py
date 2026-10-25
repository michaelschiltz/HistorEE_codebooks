import json,re,collections as co,difflib,csv
R=json.load(open('R.json'))
N=len(R)
def pct(a,b): return f"{a} ({100*a/b:.0f}%)" if b else "0"
def clean(g): 
    g=re.sub(r'(\w)-\s+(\w)',r'\1\2',g); g=re.sub(r'^\s*\S{1,5}\.\s*','',g)
    return re.split(r'\b(?:Rialto|Rivoalto|Costantinopoli|Candia)\b',g)[0][:160].lower()
# near-duplicate regests to the immediately preceding act (copies/exempla printed next to mater, or parallel acts)
dups=[]
for i in range(1,N):
    a,b=clean(R[i-1]['regest']),clean(R[i]['regest'])
    s=difflib.SequenceMatcher(None,a,b).ratio()
    R[i]['sim_prev']=round(s,2)
    if s>0.85 and not re.search(r'lo stesso',b): dups.append((R[i]['n'],s,R[i]['copy_in_head']))
R[0]['sim_prev']=0
print('near-dup regests',len(dups), 'of which copy flag',sum(1 for d in dups if d[2]=='1'))
print(dups[:30])
# investment-related
for r in R:
    g=re.sub(r'(\w)-\s+(\w)',r'\1\2',r['regest'])
    r['invest_rel']=int(bool(re.search(r'collegan|compagni|commerc|traffic|negozi|societ|rogadi',g,re.I)))
    r['overseas']=int(bool(r['place']) and r['place']!='Venice' and r['place'] not in ('Chioggia','Torcello','Murano','Treviso','Padova','Verona'))
T=co.Counter(r['T'] for r in R)
print('N',N); 
for k,v in T.most_common(): print(f'  {k}: {v} ({100*v/N:.1f}%)')
inv=[r for r in R if r['T']=='investment contract']
print('investment contracts',len(inv),'incised',sum(int(r['incised']) for r in inv))
print(' by fondo',co.Counter(r['F'] for r in inv)); print(' by period',co.Counter(r['period'] for r in inv))
rel=[r for r in R if r['T']=='release (securitas)']
ri=[r for r in rel if r['invest_rel']]
print('releases',len(rel),'investment-related releases',len(ri),'by period',co.Counter(r['period'] for r in ri))
print('invest-related acts all types',sum(r['invest_rel'] for r in R), co.Counter(r['T'] for r in R if r['invest_rel']).most_common(8))
print('incised by type',co.Counter(r['T'] for r in R if r['incised']=='1').most_common())
print('releases incised',sum(1 for r in rel if r['incised']=='1'))
print('mairano',sum(r['mairano'] for r in R),'by T',co.Counter(r['T'] for r in R if r['mairano']).most_common(5))
print('overseas',sum(r['overseas'] for r in R),'no place',sum(1 for r in R if not r['place']))
print('overseas by period',{p:(sum(r['overseas'] for r in R if r['period']==p),sum(1 for r in R if r['period']==p)) for p in ['<1150','1150-1199','1200-1229','1230-1261']})
print('copy_head',sum(int(r['copy_in_head']) for r in R),'by F',co.Counter(r['F'] for r in R if r['copy_in_head']=='1'))
print('edited before',sum(int(r['edited_before']) for r in R))
print('release share by fondo',{f:pct(sum(1 for r in R if r['F']==f and r['T']=='release (securitas)'),sum(1 for r in R if r['F']==f)) for f in ['S. Zaccaria','Procuratori','Canc. Inferiore']})
print('inv share by fondo',{f:pct(sum(1 for r in R if r['F']==f and r['T']=='investment contract'),sum(1 for r in R if r['F']==f)) for f in ['S. Zaccaria','Procuratori','Canc. Inferiore']})
print('release share by period',{p:pct(sum(1 for r in R if r['period']==p and r['T']=='release (securitas)'),sum(1 for r in R if r['period']==p)) for p in ['<1150','1150-1199','1200-1229','1230-1261']})
print('inv share by period',{p:pct(sum(1 for r in R if r['period']==p and r['T']=='investment contract'),sum(1 for r in R if r['period']==p)) for p in ['<1150','1150-1199','1200-1229','1230-1261']})
print('dispute-ish (judgment+attestation+cession) by fondo',{f:pct(sum(1 for r in R if r['F']==f and r['T'] in ('judgment / process','attestation')),sum(1 for r in R if r['F']==f)) for f in ['S. Zaccaria','Procuratori','Canc. Inferiore']})
# seg method
print('seg',co.Counter(r['seg'] for r in R))
json.dump(R,open('R2.json','w'),ensure_ascii=False)
