import subprocess,re,sys,difflib,os
from PIL import Image,ImageDraw,ImageFont
PDF={'I':'v1.pdf','II':'v2.pdf'}; OFF={'I':33,'II':7}
def norm(w): return re.sub(r'[^a-z]','',w.lower().replace('l','t').replace('c','e').replace('u','v'))
def words(vol,p):
    x=subprocess.run(['pdftotext','-bbox','-f',str(p),'-l',str(p),PDF[vol],'-'],capture_output=True,text=True).stdout
    W,H=map(float,re.search(r'<page width="([\d.]+)" height="([\d.]+)"',x).groups())
    ws=[(float(a),float(b),float(c),float(d),t) for a,b,c,d,t in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<',x)]
    return W,H,ws
def find(vol,pages,q):
    qn=[norm(w) for w in q.split() if norm(w)]
    best=None
    for p in pages:
        W,H,ws=words(vol,p); wn=[norm(w[4]) for w in ws]
        # sliding window score on first ~6 words then extend
        for i in range(len(wn)):
            k=min(len(qn),len(wn)-i)
            if k<3: continue
            sc=sum(difflib.SequenceMatcher(None,a,b).ratio() for a,b in zip(qn[:k],wn[i:i+k]))/len(qn)
            if not best or sc>best[0]: best=(sc,p,i,k,W,H,ws)
    return best
def crop(vol,p,ws,i,k,W,H,tag):
    y0=min(w[1] for w in ws[i:i+k]); y1=max(w[3] for w in ws[i:i+k])
    img=f'/tmp/pg_{vol}_{p}.png'
    if not os.path.exists(img): subprocess.run(['pdftoppm','-r','300','-gray','-png','-singlefile','-f',str(p),'-l',str(p),PDF[vol],img[:-4]])
    im=Image.open(img); s=im.width/W
    return im.crop((0,int((y0-6)*s),im.width,int((y1+6)*s)))
if __name__=='__main__':
    vol,pp,q=sys.argv[1],int(sys.argv[2]),sys.argv[3]
    p=pp+OFF[vol]; b=find(vol,[p,p+1,p-1],q); print(round(b[0],2),b[1],' '.join(w[4] for w in b[6][b[2]:b[2]+b[3]]))
