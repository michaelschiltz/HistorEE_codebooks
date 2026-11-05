import subprocess,re,json,sys,numpy as np
from PIL import Image
def page(pdf,p,dpi=150):
    fn=f'/tmp/r_{pdf}_{p}'; 
    subprocess.run(['pdftoppm','-r',str(dpi),'-gray','-png','-singlefile','-f',str(p),'-l',str(p),pdf,fn])
    a=np.array(Image.open(fn+'.png').convert('L'))
    x=subprocess.run(['pdftotext','-bbox','-f',str(p),'-l',str(p),pdf,'-'],capture_output=True,text=True).stdout
    W,H=map(float,re.search(r'<page width="([\d.]+)" height="([\d.]+)"',x).groups()); s=a.shape[1]/W
    ws=[(float(q)*s,float(b)*s,float(c)*s,float(d)*s,t) for q,b,c,d,t in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<',x)]
    return a,ws
def bands(a):
    ink=a<110
    # remove page-edge noise: ignore 3% margins
    h,w=ink.shape; m=int(w*0.04); ink[:, :m]=False; ink[:, w-m:]=False; ink[:int(h*0.02)]=False; ink[int(h*0.985):]=False
    rows=ink.sum(1); on=rows>max(3,w*0.004)
    out=[];i=0
    while i<h:
        if on[i]:
            j=i
            while j<h and on[j]: j+=1
            if j-i>=6:
                cols=np.where(ink[i:j].sum(0)>0)[0]
                # drop isolated specks: require column runs
                if len(cols)>15: out.append((i,j,cols.min(),cols.max(),len(cols)))
            i=j
        else: i+=1
    return out
def check(pdf,p):
    a,ws=page(pdf,p); B=bands(a); flags=[]
    for (y0,y1,x0,x1,n) in B:
        cy=(y0+y1)/2
        lw=[w for w in ws if w[1]-3<=cy<=w[3]+3 and w[4].strip()]
        if not lw: flags.append(dict(y0=y0,y1=y1,x0=int(x0),x1=int(x1),why='no words')); continue
        wx0=min(w[0] for w in lw); wx1=max(w[2] for w in lw)
        # uncovered ink spans
        cov=np.zeros(a.shape[1],bool)
        for w in lw: cov[int(w[0])-4:int(w[2])+4]=True
        ink=(a[y0:y1]<110).sum(0)>0
        m=int(a.shape[1]*0.04); ink[:m]=False; ink[-m:]=False
        k=np.ones(9,int); ink=np.convolve(ink.astype(int),k,'same')>0
        unc=ink & ~cov
        # find longest uncovered run
        runs=[];k=0;L=len(unc)
        while k<L:
            if unc[k]:
                j=k
                while j<L and unc[j]: j+=1
                runs.append((k,j)); k=j
            else: k+=1
        big=[(r0,r1) for r0,r1 in runs if r1-r0>=25 and (r1-r0>=25)]
        if big: flags.append(dict(y0=y0,y1=y1,x0=int(x0),x1=int(x1),why='uncovered ink x='+','.join(f'{r0}-{r1}' for r0,r1 in big)))
    return len(B),flags
if __name__=='__main__':
    pdf,p=sys.argv[1],int(sys.argv[2]); n,f=check(pdf,p); print(n,'bands'); [print(x) for x in f]
