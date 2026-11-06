import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import mark_teal, mark_coral, chunk_d, history_d, slab
TEAL,CORAL,INK,CREAM,ORANGE='#2FE0C4','#FF6F61','#111111','#F4EFE6','#FF9F1C'
import base64
FONT='data:font/woff2;base64,'+base64.b64encode(open('/home/user/ethomasclass/15minhistorystyle/brand/fonts/IBMPlexMono.woff2','rb').read()).decode()
def bars(cx,y,w,h,n=23):
    random.seed(7); bw=w/(n*1.6); out=[]
    for i in range(n):
        t=abs(i-(n-1)/2)/((n-1)/2); hh=h*(0.22+0.78*(1-t**1.6))*random.uniform(0.55,1.0)
        x=cx-w/2+i*bw*1.6; c=CORAL if i in (9,10,11,12,13) else TEAL; ch=min(bw*0.35,12)
        y0=y+(h-hh)/2
        out.append(f'<path fill="{c}" d="M{x+ch} {y0} L{x+bw-ch} {y0} L{x+bw} {y0+ch} L{x+bw} {y0+hh-ch} L{x+bw-ch} {y0+hh} L{x+ch} {y0+hh} L{x} {y0+hh-ch} L{x} {y0+ch} Z"/>')
    return ''.join(out)
def svg(W,H,slabcol,layout='square',label=True):
    sd,sw=slab('SHORTS')
    if layout=='square':
        ms=4.6; mx=(W-210*ms)/2; my=300
        ws=2.25; wx=(W-1142*ws)/2-262.5*ws; wy=my+210*ms+230-35*ws
        sx=(W-sw*ws)/2; sy=wy+35*ws+140*ws+70
        bar=bars(W/2, sy+140*ws+150, 1500, 260)
        lab=f'<text x="{W/2}" y="{H-190}" text-anchor="middle" font-family="Plex" font-size="78" letter-spacing="14" fill="{CREAM}" opacity="0.8">A HISTORY PODCAST</text>' if label else ''
    else:  # 16:9: mark left, words right, the whole block centred
        ms=2.0; gap=80; ws=0.98; ww=1142*ws; total=210*ms+gap+ww
        mx=(W-total)/2; my=(H-210*ms)/2
        wx=mx+210*ms+gap-262.5*ws; blockh=140*ws*2+30; wy=(H-blockh)/2-35*ws-24
        sx=mx+210*ms+gap; sy=wy+35*ws+140*ws+30
        bar=bars(sx+sw*ws+(ww-sw*ws)/2, sy+14, ww-sw*ws-70, 110, n=13)
        lab=f'<text x="{sx}" y="{sy+140*ws+72}" font-family="Plex" font-size="30" letter-spacing="7" fill="{CREAM}" opacity="0.8">A HISTORY PODCAST</text>' if label else ''
    ink_on = INK
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><style>@font-face{{font-family:Plex;src:url({FONT}) format("woff2")}}</style>
<radialGradient id="g" cx="50%" cy="42%" r="75%"><stop offset="0" stop-color="#1b1b1b"/><stop offset="1" stop-color="#0b0b0b"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#g)"/>
<g transform="translate({mx},{my}) scale({ms})"><path fill="{TEAL}" fill-rule="evenodd" d="{mark_teal}"/><path fill="{CORAL}" fill-rule="evenodd" d="{mark_coral}"/></g>
<g transform="translate({wx},{wy}) scale({ws})"><path fill="{TEAL}" fill-rule="evenodd" d="{chunk_d}"/><path fill="{CORAL}" fill-rule="evenodd" d="{history_d}"/></g>
<g transform="translate({sx},{sy}) scale({ws})"><path fill="{slabcol}" fill-rule="evenodd" d="{sd}"/></g>
{bar}{lab}</svg>'''
if __name__=='__main__':
    out=sys.argv[1]; os.makedirs(out,exist_ok=True)
    for name,col in (('A_cream',CREAM),('B_orange',ORANGE)):
        open(f'{out}/cover_{name}.svg','w').write(svg(3000,3000,col))
        open(f'{out}/wide_{name}.svg','w').write(svg(1920,1080,col,'wide'))
