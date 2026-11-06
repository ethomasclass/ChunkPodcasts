import re, sys
SRC='/home/user/ethomasclass/15minhistorystyle/brand/chunk-history/final/chunk-history-horizontal.svg'
s=open(SRC).read()
paths=re.findall(r'<path fill="(#\w+)" fill-rule="evenodd" d="([^"]+)"',s)
mark_teal, mark_coral = paths[0][1], paths[1][1]
chunk_d, history_d = paths[2][1], paths[3][1]
subs=[x.strip() for x in re.split(r'(?=M)',history_d) if x.strip()]
def xr(sp): xs=[float(a) for a in re.findall(r'(-?[\d.]+) -?[\d.]+',sp)]; return min(xs),max(xs)
glyph={}  # letter -> list of subpaths (outline + counters)
order='HISTORY'; outlines=sorted([sp for sp in subs[1:] if xr(sp)[1]-xr(sp)[0]>30 or len(re.findall('L',sp))>5],key=lambda sp:xr(sp)[0])
for L,sp in zip(order,outlines): glyph[L]=[sp]
for sp in subs[1:]:
    if sp in outlines: continue
    a,b=xr(sp)
    for L in order:
        g0,g1=xr(glyph[L][0])
        if g0<=a and b<=g1: glyph[L].append(sp)
def shift(sp,dx,dy=0):
    return re.sub(r'(-?[\d.]+) (-?[\d.]+)',lambda m:f'{float(m.group(1))+dx:.1f} {float(m.group(2))+dy:.1f}',sp)
def slab(word,x0=0,pad=20,gap=18):
    x=x0+pad; parts=[]
    for L in word:
        g0,g1=xr(glyph[L][0]); parts+= [shift(sp,x-g0,-35) for sp in glyph[L]]; x+=g1-g0+gap
    x1=x-gap+pad
    outer=f'M{x1-16} 0 L{x0+16} 0 L{x0} 16 L{x0} 124 L{x0+16} 140 L{x1-16} 140 L{x1} 124 L{x1} 16 Z'
    return outer+' '+' '.join(parts), x1-x0
if __name__=='__main__':
    print({k:len(v) for k,v in glyph.items()})
    d,w=slab('SHORTS'); print('SHORTS slab width',w)
