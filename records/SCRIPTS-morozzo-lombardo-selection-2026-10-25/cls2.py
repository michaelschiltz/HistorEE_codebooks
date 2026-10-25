import re,json,csv,collections
acts=json.load(open('acts3.json'))
F=[('Museo di Paleografia (prov. S. Zaccaria)',r'Museo\s+di\s+Paleogr'),
   ('Procuratori di S. Marco',r'\bProc[\.,]|Procurator[ie]\s+di\s+S'),
   ('Cancelleria Inferiore',r'\bC[ao]n[ce][\.,]?\s*,?\s*(?:pag\.\s*\d+\.\s*)?Inf|\bBusta\s+[A-Z]\.?\s*[I1l]|Canc\.'),
   ('S. Giorgio Maggiore',r'Giorg'),
   ('S. Zaccaria',r'Za[cv]e\b|Z[aonu][ce]{1,2}c?[\.,]|\bZac\b|\bZa\b|\bLace\b|\bacc\.\s*B|\bcc\.,?\s*B|\bZacc\b|S\.\s*Z\s'),
   ('Mensa Patriarcale',r'Mensa'),('S. Eufemia di Mazzorbo',r'Eufemia'),('S. Matteo di Mazzorbo',r'S\.\s*Matteo'),('Dimesse di Murano',r'Dimesse'),('S. Daniele',r'S\.\s*Daniele'),
   ('S. Andrea del Lido',r'S\.?\s*Andrea\s+del'),('S. Nicolò del Lido',r'Nicol[oò]\s+del\s+Lido'),('Ducali ed Atti Diplomatici',r'Ducali'),
   ('Miscellanea',r'\bMisc'),('Pergamene Dandolo (donate 1865/66)',r'donate\s+dal\s+Co|Perg\.?\s+donate'),('S. Damiano di Murano',r'Damiano\s+di\s+Murano'),('Verona',r'Pergamene\s+Verona|Verona,\s*Arch|Arch\w*\s+di\s+Stato\s+di\s+Verona'),('S. Lorenzo',r'S\.\s*Lorenzo\s+B'),('S. Maria della Celestia',r'Celestia')]
BUSTA=[(r'\bB\.\s*(1|24|25|26|40|135|95)\b','S. Zaccaria'),(r'\bB\.\s*28\b','S. Giorgio Maggiore'),(r'\bB\.\s*(C[CXLVIO]{2,}|29\d|3[01]\d)\b|\bC[CXLVIMO]{4,}\b','Procuratori di S. Marco'),(r'\b(24|25|26|40)\s*-\s*\w','S. Zaccaria')]
COND=re.compile(r'\b(Buona|Bnona|Mediocre|Ottima|Ottim|Otti|Cattiva|Calliva|Pessima|Discreta|Discrela|Frammento)\b|\b\d{2,3}\s*[xX×»]\s*\d{2,3}\b')
INN=re.compile(r'In\s+nomine|[Il1]n\s+no[mn][iíl]ne|In\s+Christi\s+nomine|In\s+Dei\s+nomine|In\s+noinine|nomine\s+Domini')
FORM=[('securitas',r'securi[tl]a[tl]|plenam\s+et\s+i[nr]{1,2}e?r?evocabil|plenam\s+e[tl]{1,2}\s+i\w*vocab'),
 ('manifestus',r'mani\s*-?\s*f\s*-?\s*\n*\s*est|manifest|[Aa]ccepi\s+ego|[Rr]ecepi\s+ego'),
 ('testificor',r'[Tt]estific|testamur|testimonium\s+perhib|dicimus\s+testimon'),('breve/recordatio',r'[Bb]reve\s+(?:fac|recordac|securit|de\b)|[Bb]reviari|recordac|memoratori'),
 ('commissio/procura',r'Committens|commi[tl]{2}\w*\s+(?:ego\s+)?commi[tl]{2}|commissionis\s+cartul|[Oo]mnis\s+commissio|plen\w+\s+virtutem|in\s+loco\s+meo|meum\s+missum|procurator\w*\s+(?:meum|nostrum)|constituo|facio\s+\w*\s*procurator'),
 ('iudicium',r'iudic[ea]s\s+|diiudicat|ante\s+nos|sentenc|laudamus|condemp|placit|iudicamus|in\s+curia'),
 ('promissio',r'[Pp]romi[tl]{1,2}en[sl]\s+promi[tl]{1,2}o|promission\w*\s+cartul|promitto\s+ego|promittimus|obligo\s+me|obligavit\s+se|se\s+obligav'),('testamentum',r'testament|ultimam\s+voluntatem|ordinare\s+bona'),
 ('venditio/donatio/investitio',r'vendicion|vendition|donacion|donation|investicion|investition|investivit|refutacion|concession|do\s+atque\s+trado|venundo|vendidit|dedit\s+et\s+vendidit|investitur'),
 ('notitia/confessio',r'notum\s+(?:sit|facio|facimus)|scire\s+volo|recognosc|confess|fateor|confiteor'),('dux scribit',r'Dei\s+gratia\s+(?:Veneci|dux)')]
REG=[('release',r'quietan|quielan|quictan|quiefan|quietat|quielat|rilascia\s+quiet|fa\s+quiet|assolve|libera'),
 ('attestation',r'attest|testimon|testific'),
 ('procura',r'mandato|procur|commissari|costituisce\s+\w+\s+procur|nomina'),
 ('judgment/process',r'sentenz|giudic|Giudizio|condann|lodo|arbitr|diffida|protest|inadempi|procediment|sequestr|pignoramento|incanto|esecuzion'),
 ('testament',r'testament'),
 ('contract-colleganza/compagnia',r'collegan|compagni|societ'),
 ('contract-sea-loan/exchange',r'cambio|prestito\s+marittim|prestilo\s+marillim|marittim|marillim'),
 ('contract-loan',r'prestit|prestil|mutuo|debito|deposit'),
 ('contract-commission',r'per\s+commerciare|per\s+trafficare|per\s+traffic|per\s+commercia|commercer|commercerà|per\s+com-?\s*merciare|negoziare'),
 ('freight/ship',r'nolo|noleg|nave|ancor'),('sale/gift/property',r'\bvend|\bcompr|\bdona(?:zione|re|no)?\b|\bced(?:e|ono)\b|cessione|\binveste\b|\brefuta|divisione|permuta|affitt|locazione|\bpegno')]
def first(pats,s):
    best=None
    for name,p in pats:
        m=re.search(p,s,re.I)
        if m and (best is None or m.start()<best[1]): best=(name,m.start())
    return best[0] if best else 'other'
def anyof(pats,s): return [name for name,p in pats if re.search(p,s,re.I)]
rows=[]
for a in acts:
    t=a['text']; mi=INN.search(t)
    head=t[:mi.start()] if mi and mi.start()<3500 else t[:1800]
    body=t[mi.start():] if mi and mi.start()<3500 else t[len(head):]
    c=COND.search(head)
    # archival zone: 220 chars before the condition/size hit
    if c: zone=head[max(0,c.start()-220):c.end()+40]
    else: zone=head
    cands=[]
    for name,p in F:
        for m in re.finditer(p,zone): cands.append((m.start(),name))
    if cands:
        # rightmost hit before condition word (closest to it) wins; Museo overrides (prov. S. Zacc.)
        names=[n for _,n in sorted(cands)]
        cpos=min(220,c.start()) if c else len(zone)
        before=[n for p,n in sorted(cands) if p<cpos] or names
        if 'Museo di Paleografia (prov. S. Zaccaria)' in names: fond='Museo di Paleografia (prov. '+('S. Giorgio Magg.' if re.search('Giorg',zone) else 'S. Zaccaria')+')'
        elif 'Miscellanea' in names: fond='Miscellanea'+(' (prov. Proc. di S. Marco)' if 'Procuratori di S. Marco' in names else '')
        else: fond=before[-1]
    else:
        fond='?'
        for p,n in BUSTA:
            if re.search(p,zone): fond=n+' (busta)'; break
    regest=head[:c.start()-0] if c else head
    rg_txt=re.sub(r'\s+',' ',head[:c.start()] if c else head)
    yrs=[int(y) for y in re.findall(r'\b(1[0-2]\d\d)\b',rg_txt) if 1000<=int(y)<=1265]
    if not yrs: yrs=[int(y) for y in re.findall(r'\b(1[0-2]\d\d)\b',re.sub(r'\s+',' ',head)) if 1000<=int(y)<=1265]
    yr=yrs[0] if yrs else None
    edited=bool(re.search(r'Edit[ao]\s+(?:da|dal|in)|lita\s+dal',head))
    copy=bool(re.search(r'[Cc]opia\b|[Ee]semplar',head)) or bool(re.search(r'vid\w*\s+in\s+matre|vidi\s+in\s+mater|exemplav|in\s+filia|exemplum\s+exempl',body,re.I))
    copy_head=bool(re.search(r'[Cc]opia\b',head))
    incised=bool(re.search(r'[CcGg]ar[tl]a\s+[iìíl1]ncis|[iìíl1]ncis[ae]\s*[\.\-,]|\bincis',t[:max(len(head),1500)]))
    op=first(FORM,body[:900])
    rg=first(REG,regest[:600])
    rows.append(dict(n=a['n'],vol=a['vol'],seg=a['how'],year=yr,fondo=fond,opening=op,regest_class=rg,
        regest_flags='|'.join(anyof(REG,regest[:600])),copy_in_head=int(copy_head),exemplum_any=int(copy),incised=int(incised),edited_before=int(edited),
        regest=re.sub(r'\s+',' ',regest)[:400],archival=re.sub(r'\s+',' ',zone)[-260:],latin_start=re.sub(r'\s+',' ',body[:260])))
with open('acts3.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
C=collections.Counter
print(len(rows)); print('fondo',C(r['fondo'] for r in rows).most_common())
print('op',C(r['opening'] for r in rows).most_common()); print('regest',C(r['regest_class'] for r in rows).most_common())
print('copy_head',sum(r['copy_in_head'] for r in rows),'exemplum_any',sum(r['exemplum_any'] for r in rows),'incised',sum(r['incised'] for r in rows),'edited',sum(r['edited_before'] for r in rows),'noyear',sum(1 for r in rows if not r['year']))
