import csv,re,collections as co,json
R=list(csv.DictReader(open('acts3.csv')))
def F(r):
    f=r['fondo'].replace(' (busta)','')
    if f.startswith('S. Zaccaria') or 'prov. S. Zaccaria' in f: return 'S. Zaccaria'
    if f.startswith('Procuratori'): return 'Procuratori'
    if f.startswith('Cancelleria'): return 'Canc. Inferiore'
    if f=='?': return 'unresolved'
    if f.startswith('Miscellanea') or 'Dandolo' in f or f=='Verona': return 'miscellanies'
    return 'other convents'
TYPE={'release':'release (securitas)','contract-commission':'investment contract','contract-colleganza/compagnia':'investment contract','contract-sea-loan/exchange':'sea loan / exchange','contract-loan':'loan / deposit','procura':'mandate (procura)','attestation':'attestation','judgment/process':'judgment / process','testament':'testament','sale/gift/property':'property / sale / pledge','freight/ship':'freight / ship','other':'other'}
def retype(r,prev):
    g=re.sub(r'(\w)-\s+(\w)',r'\1\2',r['regest'])
    g=re.sub(r'^\s*\S{1,5}\.\s*','',g); g=re.sub(r'R\. MOROZZO DELLA ROCCA - A\. LOMBARDO|DEL COMMERCIO VENEZIANO NEI SEC\. XI-XI\w*\s*\d*','',g).strip()
    if re.search(r"\b(Lo\s+stesso|Il\s+medesimo|La\s+stessa|Gli\s+stessi)\b",g[:60]) or re.match(r"[A-Z][a-z]+\s+[A-Z][a-z]+\s+agli\s+stessi",g): return prev,'inherited'
    t=TYPE[r['regest_class']]
    if t=='other':
        if re.search(r'commerc|traffic|coinmerc',g,re.I): t='investment contract'
        elif re.search(r'si\s+obblig|pagher|promett\w*\s+\w*\s*di\s+pagar|per\s+merci\s+ricevut|per\s+formaggio|partita\s+di',g,re.I): t='obligation to pay (credit sale)'
        elif re.search(r'pres[lt]i[lt]o|mutuo',g,re.I): t='loan / deposit'
        elif re.search(r'traspor|nolo',g,re.I): t='freight / ship'
        elif re.search(r'servo|schiav|manomet|al\s+servizio',g,re.I): t='servile / labour'
        elif re.search(r'doge\b.*(scrive|sottoscrive)|copia\s+di\s+atto',g,re.I): t='ducal / authentication'
        elif re.search(r'affitt',g,re.I): t='property / sale / pledge'
    return t,'regest'
OPMAP={'securitas':'release (securitas)','testificor':'attestation','commissio/procura':'mandate (procura)','promissio':'promise / guarantee','testamentum':'testament','iudicium':'judgment / process','venditio/donatio/investitio':'property / sale / pledge','dux scribit':'ducal / authentication'}
prev='other'
for r in R:
    r['F']=F(r); r['T_regest'],r['T_src']=retype(r,prev); prev=r['T_regest']
    g=r['regest']
    if r['opening'] in OPMAP:
        T=OPMAP[r['opening']]
        if T=='release (securitas)' and re.search(r'\bced(?:e|ono)\b|cessione',g): T='cession of claim'
        r['T']=T; r['T_src']='opening'
    else:
        r['T']=r['T_regest']
        if r['T']=='other' and re.search(r'vendut|dichiara\w*\s+d.aver\s+vend',g): r['T']='property / sale / pledge'
    r['agree']=int(r['T']==r['T_regest'])
    reg=r['regest']
    m=re.findall(r"([A-Z][A-Za-zà-ù'\(\) ]{2,30}?)[,\.]\s*\[?\(?\s*(1[0-2]\d\d)",reg)
    pl=m[-1][0].strip() if m else ''
    pl=re.sub(r'^(.*\s)?(Rialto|Rial-?\s*to|Rivoalto|Venezia|Ri- alto|Riallo|Rialio|Riaito|Rialt)$','Venice',pl)
    pl=re.sub(r'^Co[sl]{1,2}antinopoli$','Costantinopoli',pl)
    r['place']=pl
    y=r['year']; r['period']=('' if not y else ('<1150' if int(y)<1150 else '1150-1199' if int(y)<1200 else '1200-1229' if int(y)<1230 else '1230-1261'))
    r['mairano']=int(bool(re.search(r'Mairan|Mayran',reg)))
    r['colleganza']=int(bool(re.search(r'collegan',reg,re.I)))
    r['commerce_contract']=int(bool(re.search(r'per\s+commerci|per\s+traffic|collegan|compagni',reg,re.I)))
    r['cfr_prec']=int(bool(re.search(r"[Cc]fr\.?,?\s*l'atto\s+precedente|[Cc]fr\.?,?\s*il\s+documento\s+precedente",reg+r['archival'])))
def tab(rowkey,colkey,rows=R,order_r=None,order_c=None):
    X=co.Counter((r[rowkey],r[colkey]) for r in rows)
    rs=order_r or [k for k,_ in co.Counter(r[rowkey] for r in rows).most_common()]
    cs=order_c or [k for k,_ in co.Counter(r[colkey] for r in rows).most_common()]
    out='| '+rowkey+' | '+' | '.join(cs)+' | total |\n|'+'---|'*(len(cs)+2)+'\n'
    for a in rs:
        out+='| '+a+' | '+' | '.join(str(X[(a,c)]) for c in cs)+' | '+str(sum(X[(a,c)] for c in cs))+' |\n'
    out+='| total | '+' | '.join(str(sum(X[(a,c)] for a in rs)) for c in cs)+' | '+str(len(rows))+' |\n'
    return out
fo=['S. Zaccaria','Procuratori','Canc. Inferiore','other convents','miscellanies','unresolved']
po=['<1150','1150-1199','1200-1229','1230-1261','']
print(tab('T','F',order_c=fo)); print(tab('F','period',order_r=fo,order_c=po)); print(tab('T','period',order_c=po))
pc=co.Counter(r['place'] for r in R); print(pc.most_common(30))
print('venice',sum(1 for r in R if r['place']=='Venice'),'noplace',sum(1 for r in R if not r['place']))
print('mairano',sum(r['mairano'] for r in R),'colleganza',sum(r['colleganza'] for r in R),'commerce',sum(r['commerce_contract'] for r in R),'cfr_prec',sum(r['cfr_prec'] for r in R))
print(tab('T','F',rows=[r for r in R if r['commerce_contract']],order_c=fo))
print('copy_in_head by F',co.Counter(r['F'] for r in R if r['copy_in_head']=='1'))
print('incised by F',co.Counter(r['F'] for r in R if r['incised']=='1'), 'incised by T',co.Counter(r['T'] for r in R if r['incised']=='1'))
print('edited',co.Counter(r['F'] for r in R if r['edited_before']=='1'))

A_=json.load(open('acts3.json')); v1_=open('v1.txt').read(); v2_=open('v2.txt').read(); L_=len(v1_)
for a,r in zip(A_,R):
    m=re.search(r'\d{1,3}\s*[\.,]\s*\n?\s*[A-Z]|[A-Z][a-z]+ [A-Z]',a['text']); p=a['p']+(m.start() if m else 0)
    r['pdfpage']=(v1_.count('\x0c',0,p)+1) if p<L_ else (v2_.count('\x0c',0,p-L_)+1)
json.dump(R,open('R.json','w'),ensure_ascii=False)
with open('acts_final.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(R[0])); w.writeheader(); w.writerows(R)
