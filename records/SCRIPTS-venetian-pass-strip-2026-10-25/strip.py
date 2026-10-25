import json,re,sys
A=json.load(open('acts3.json'))
LAT_START=re.compile(r'(?:\+\s*)?\[?\b[IT1l]\s*n\s+n\s*o\s*m\s*[iíl]?\s*n?\s*[eci]?\b|\bIn\s+n[oe]m|\bIn\s+(?:eterni|Christi|Dei)\b|\bAnn[oi]\s+(?:Domini|ab\s+incarna|incarna|eiusdem)|\bIn\s+no\b|\bNomine\s+Domini|\bRecorda[ct]ion|\bVobis\s+(?:\w+\s+){0,6}recorda|\bPromisit\b|\bPromi[tl]{2}ens\b|\bManifest(?:us|um)\s+(?:sum|facio)|\bPlenam\s+et|\bTestific(?:or|amur)|\bCommi[tl]{2}ens|\b[IJ]acobus\s+Teupulo\s+Dei\s+gratia|\bDomini\s+millesimo|\bOmnis\s+commissio|\bcartules?\s+de\s+iste')
RUN=re.compile(r'^\s*(?:\d{1,3}|[ivxlc]+|R\.\s*MOROZZO.*|MOROZZO.*|DELLA\s*ROCCA.*|.*\bLOMBARDO\b.*|.*DOCUMENTI.*|.*COMMERCIO.*|.*VENEZIANO.*|NEI|DEL|SEC[\.,]?.*|XI\s*-\s*X\w*\.?|Documenti\s+del.*|commercio.*|veneziano.*|nei\s+sec.*|Vol\.\s*I+\.?|-|—|\.|,|:|;|\*)\s*$')
FOOT=re.compile(r'^\s*\(\d+\)\s')
ARCH=re.compile(r'\b(?:S\.?\s*Z[a-z]{1,3}c?\.?|Zacc|Proc\.?|Canc?e?\.?\s*,?\s*Inf|Busta|Buona|Ottima|Mediocre|Cattiva|Pessima|Discreta|Calliva|Att\.|AU\.|Alt\.|coev[oi]|L\.?\s*B\.|I\.\s*B\.|Copia|incisa|Edita|Ed\.\s+dal|op\.\s*cit|Cfr\.?|sottoscrizion\w*|inchiostro|sopralinea|cancellat\w*|corrett\w*|riscritt\w*|abras\w*|margine|Museo|Paleografia|Mensa|Patr\.|Giorg\.|Magg\.|Misc\.|Rigatura|Frammento|op\.|Ba\w{0,3}acc\w*|Sac\w{0,3}(?:rd|rnb|mb|rmb|nb)\w*|lita\s+dal|dal\s+[A-Z]\w+\s*:)\b|\b\d{2,3}\s*[xX×»]\s*\d{2,3}\b')
IT=set('del della dello dei degli delle il lo gli che fa fanno con sono suoi loro ai agli dalla nel nella nelle quietanza somma prestito stipula riceve dà mandato attesta attestano dichiara fratello figlio figlia moglie vedova defunto marittimo cambio colleganza commerciare trafficare dovunque altrove ritorno atto atti precedente seguente prov quietation quietacion securtà segurtà fata fato fatta procuration debito recever lire zugno luio avosto settembrio setembrio ottubrio otubrio novembrio decembrio dezembrio fevrer zener april marzo maio mazo zuan piero domenego'.split())
LA=set('a ad amplius anno atque aut capite capitulis cartula cartulam caucionis collegancia colligancia compellere complevi confinio cum dare de debeam debeat debebas debuisti dei deliberare domini ego eius est et fecisti fecit habere habet hec heredibus in inde indicione inditione ingenium inter ipsa ipse ipsum irrevocabilem latitudinem libras longitudinem manifestacionis meis mense michi mihi minus nec nobis non nos nostra nostri nostro notarius omnia omnibus parte pedes per perperos plenam plus presbiter prode quam que quia quidem quod requirere rivoalto roboravi sancte sancti securitatem securitatis sed si sicut sua subscripsi suis sunt suo suprascript te testis tibi tu tua tuis tuo ullum unde ut vel vero videlicet vobis vos'.split())
POST=[r'D\w{1,3}menti\s+(?:del\s+)?(?:commercio\s+)?(?:veneziano\s+)?nei\s+se\w[\.,]?\s*[XI][\w\-\.]*\.?(?:\s*-\s*Vol\.\s*\S+)?(?:\s*\d+\.?)?\s?',
 r'[A-Z]?\.?\s*MOROZZO\s+[DP]ELLA\s+ROCCA(?:\s*-?\s*A\.?)?(?:\s*[LT]OMBARDO)?',
 r'\b(?:DOCUMENTI|DEL\s+COMMERCIO|VENEZIANO|NEI\s+SEC\.?)\b',
 r'\b1[0-2]\d\d\s+(?:gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)\b',
 r'\bRialto[\.,]?',
 r"\(?D?\s*Per la datazione.*?Introduzione\.(?:\s*Documenti)?",
 r'\(\d\)\s*Nota che[^.]*\.',
 r'\bB\.\s*\d+\s*-\s*Att\.?\s*[LI]\.?\s*B\.?:[^.]*\.',
 r'Ducali\s+Att\..{0,60}?dipl,?',
 r'D[oc]\w{0,2}menti\b(?:\s+(?:del|commercio|veneziano|venezi\w*|rvenezimo|nei|see?c?[\.,]?|A|-|ROCCA|X[\w\-\.,]+|\d+\.?|Vol\.\s*\w+)){0,8}',
 r'\b[A-Z]{0,2}\.?\s*MOROZZO\b', r"mese di l'atto\. gennaio - La", r'\bagosto\.\s*S\.', r'ROCCA(?:\s*-)?\s*', r'\bTW\.', r'\(\d\)\s*\w+\s+corretto\s+sopra\s+\w+\.']
def score(line):
    w=re.findall(r"[a-zàèéìòùÀ-ÿ']+",line.lower())
    it=sum(1 for x in w if x in IT); la=sum(1 for x in w if x in LA or x.startswith('suprascript'))
    return it,la,len(w)
def clean(text):
    m=LAT_START.search(text)
    if m: body=text[m.start():]
    else:
        body=''; pos=0
        for line in text.split('\n'):
            it,la,n=score(line)
            if la>=3 and it==0 and not ARCH.search(line): body=text[pos:]; break
            pos+=len(line)+1
    out=[]; dropped=[]
    for line in body.split('\n'):
        l=line.replace('\x0c','')
        if not l.strip(): out.append(''); continue
        if RUN.match(l): dropped.append(('run',l)); continue
        if FOOT.match(l):
            it0,la0,n0=score(l)
            if it0>0 or re.search(r'sopralinea|inchiostr|riscritt|abras|cancellat|corrett|aggiunt|margine|calce|mano\b|lacuna|guast|corros|macchi|lettura|nel testo|\bsic\b|\bcosì\b',l) or la0<2:
                dropped.append(('foot',l)); continue
            l=re.sub(r'^\s*\(\d+\)\s*','',l)
        it,la,n=score(l)
        if ARCH.search(l) and la<=it+1: dropped.append(('arch',l)); continue
        if it>la and it>=2: dropped.append(('it',l)); continue
        if it>=1 and la==0 and n<=4 and it*2>=n: dropped.append(('it-short',l)); continue
        out.append(l)
    s=' '.join(x.strip() for x in out if x.strip())
    s=re.sub(r'(\w)-\s+(\w)',r'\1\2',s); s=re.sub(r'\s+',' ',s)
    s=re.sub(r'\(\s*[\dDIl]\s*[\)\];:l]?\s*[^()]{0,60}?(?:in\s+sopralinea(?:\s+su\s+\w+\s+cancellat\w*)?|riscri\w*\s+su\s+abras\w*|espunt\w*|cancellat\w*)[,\.]?(?:\s*R\.)?(?:\s*D\w*menti\s+del\s+commercio\s+\S+)?',' ',s)
    s=re.sub(r'\s+',' ',s)
    for p in POST: s=re.sub(p,'',s)
    s=re.sub(r'\s+',' ',s)
    s=re.sub(r'\s*(\+\s*Ego\b|S\.\s*T\.\s*Ego\b|Signum\b|Notitia\s+testium\b)',r'\n\1',s).strip()
    return s,dropped,(m.start() if m else None)
if __name__=='__main__':
    for n in map(int,sys.argv[1:]):
        s,d,st=clean(A[n-1]['text'])
        print('=====',n,'start',st,'kept',len(s),'dropped',len(d)); print(s[:1500]); print('--- dropped:',[x[1][:60] for x in d][:25])
