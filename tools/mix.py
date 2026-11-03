import json, subprocess, sys, re, os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'; W=R+'tools/words/'
VOICE_LUFS=-16; BED_LUFS=-35; SFX_CLEAR=-23; SFX_UNDER=-31
_lufs={}
def lufs(f):
    if f not in _lufs:
        r=subprocess.run(['ffmpeg','-hide_banner','-i',f,'-af','loudnorm=print_format=json','-f','null','-'],capture_output=True,text=True)
        _lufs[f]=float(json.loads(r.stderr[r.stderr.rindex('{'):])['input_i'])
    return _lufs[f]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def build(ep, seq, anchored, music, out):
    E=R+ep+'/audio/'; t=0.0; vo={}; ev=[]   # ev: (file, start, gain_db, trim_from, length, fade_in, fade_out)
    words=lambda n: json.load(open(W+ep[:10]+f'_{n:02d}_VO{n}.json'))
    for it in seq:
        k=it[0]
        if k=='gap': t+=it[1]
        elif k=='vo':
            f=E+f'narration/{it[1]:02d}_VO{it[1]}.mp3'; d=dur(f); vo[it[1]]=(t,t+d)
            ev.append((f,t,VOICE_LUFS-lufs(f),0,d,0,0)); t+=d
        elif k=='sfx':   # ('sfx', name, mode, advance)
            f=E+f'sfx/{it[1]}.mp3'; d=dur(f)
            lvl=SFX_CLEAR if it[2]=='clear' else SFX_UNDER
            ev.append((f,t,lvl-lufs(f),0,d,0.05,min(1.0,d/3))); t+=it[3] if len(it)>3 else d
    end_t=t
    def word_t(n,w,which='start',nth=1):
        c=0
        for x in words(n):
            if re.sub(r'[^\w]','',x[0]).lower()==w.lower():
                c+=1
                if c==nth: return vo[n][0]+(x[1] if which=='start' else x[2])
        raise SystemExit(f'word {w} not in VO{n}')
    def at(a):
        if a[0]=='vo': return vo[a[1]][0 if a[2]=='start' else 1]+a[3]
        if a[0]=='word': return word_t(a[1],a[2],a[3],a[5] if len(a)>5 else 1)+a[4]
        if a[0]=='t': return a[1]
    for an in anchored:
        name,a=an[:2]; f=E+f'sfx/{name}.mp3'; d=dur(f); lvl=an[2] if len(an)>2 else SFX_UNDER+3
        ev.append((f,max(0,at(a)),lvl-lufs(f),0,d,0.1,min(1.5,d/3)))
    for m in music:
        name,a,b,off,fi,fo=m[:6]
        f=E+(name if '/' in name else f'music/{name}')+'.mp3'; s=max(0,at(a)); e=at(b); L=min(e-s, dur(f)-off)
        lvl=m[6] if len(m)>6 else (SFX_UNDER if name.startswith('sfx/') else BED_LUFS)
        ev.append((f,s,lvl-lufs(f),off,L,fi,fo))
    total=max(end_t, max(e[1]+e[4] for e in ev))+0.5
    if os.environ.get("DBG"):
        print("end_t",round(end_t,1)); [print(round(e[1],1),round(e[1]+e[4],1),os.path.basename(e[0])) for e in sorted(ev,key=lambda e:-(e[1]+e[4]))[:6]]; return
    args=['ffmpeg','-hide_banner','-v','error','-y']; fl=[]
    for i,(f,s,g,off,L,fi,fo) in enumerate(ev):
        args+=['-i',f]
        c=f'[{i}:a]aresample=44100,aformat=channel_layouts=stereo,atrim={off:.3f}:{off+L:.3f},asetpts=PTS-STARTPTS,volume={g:.2f}dB'
        if fi: c+=f',afade=t=in:d={fi}'
        if fo: c+=f',afade=t=out:st={max(0,L-fo):.3f}:d={fo}'
        c+=f',adelay={int(s*1000)}|{int(s*1000)}[a{i}]'; fl.append(c)
    fl.append(''.join(f'[a{i}]' for i in range(len(ev)))+f'amix=inputs={len(ev)}:normalize=0:dropout_transition=0,atrim=0:{total:.2f},loudnorm=I=-16:TP=-1.5:LRA=11[out]')
    args+=['-filter_complex',';'.join(fl),'-map','[out]','-ar','44100','-b:a','192k',out]
    subprocess.run(args,check=True)
    print(out, f'{int(total//60)}:{total%60:04.1f}', len(ev),'layers')
