import json,re,sys,subprocess,os
sys.path.insert(0,'/home/claude/academy/lesson13'); import video as V
dur=json.load(open('/home/claude/academy/lesson13/vo/dur.json')); SENT=re.compile(r'[.?!:]$'); C={}
for n,cues in V.SCENES:
    if n!='vbox': continue
    t=0.5
    for c in cues:
        gap=c[3] if len(c)>3 and c[3] is not None else (0.55 if SENT.search(c[1]) else 0.13)
        C[c[0]]=t; t+=dur[c[0]]+gap+V.EXTRA.get(c[0],0)
b='/home/claude/academy/lesson13/build/'; st=max(C['b2'],C['b3']-1.5)
os.replace(b+'vbox.mp4',b+'vbox_base.mp4')
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',b+'vbox_base.mp4','-ss','1.0','-i',b+'vbox_live.mp4','-filter_complex',
 f"[1:v]setpts=PTS-STARTPTS,scale=1080:589[c];[0:v][c]overlay=110:335:enable='gte(t,{st})':eof_action=pass,format=yuv420p[o]",
 '-map','[o]','-an','-c:v','libx264','-preset','veryfast','-crf','17',b+'vbox.mp4'],check=True)
print('ok',st)
