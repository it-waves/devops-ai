import json, subprocess, sys, shutil
sys.path.insert(0,'/home/claude/academy/common'); sys.path.insert(0,'/home/claude/academy/lesson45')
import term, video as V
B='/home/claude/academy/lesson45/build/'; dur=json.load(open('/home/claude/academy/lesson45/vo/dur.json'))
P='/tmp/app45/'
def L(sc):
    C,D,f=term.cue_times(V,dur,sc); return C
def total(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
PLAN={
 'layout':lambda C,T:[('p_v1',C['l4'],T)],
 'deploy':lambda C,T:[('p_v1',C['d1'],C['d2']),('p_v2',C['d2'],T)],
 'rollback':lambda C,T:[('p_v2',C['r1'],C['r2']),('p_v2k',C['r2'],C['r6']),('p_v1',C['r6'],T)],
}
for sc,fn in PLAN.items():
    src=B+sc+'.mp4'; keep=B+sc+'_t.mp4'; shutil.copy(src,keep)
    T=total(keep); segs=fn(L(sc),T); ins=[]; fc=''; last='0:v'
    for i,(p,a,b) in enumerate(segs):
        ins+=['-i',P+p+'.png']; fc+=f"[{last}][{i+1}:v]overlay=120:500:enable='between(t,{a:.2f},{b:.2f})'[o{i}];"; last=f'o{i}'
    fc=fc.rstrip(';')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',keep]+ins+['-filter_complex',fc,'-map','['+last+']','-an','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-t',str(T),src],check=True); print('app',sc)
