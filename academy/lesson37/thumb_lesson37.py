import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
sys.path.insert(0,'/home/claude/academy/lesson37')
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson37/build'
import json, term, video as V
dur=json.load(open('/home/claude/academy/lesson37/vo/dur.json'))
def fr(scene, cid):
    C,D,f=term.cue_times(V,dur,scene); t=C[cid]+dur[cid]+3.0
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{B}/clip_{scene}.mp4','-frames:v','1','/tmp/th.png']); return Image.open('/tmp/th.png').convert('RGB')
def crop(im, box, w):
    c=im.crop(box); return c.resize((w,int(c.height*w/c.width)),Image.LANCZOS)
t1=fr('run','r3'); t2=fr('quote','q3'); t3=fr('exit','x4')
blocks=[crop(t1,(0,0,500,66),500), crop(t2,(0,0,540,66),500), crop(t3,(0,0,400,66),500)]
cols=[tuple(BAD)[:3],tuple(WARN)[:3],tuple(GOOD)[:3]]
tags=['REAL RUN · PERMISSION DENIED','REAL QUOTES · LITERAL','REAL EXIT STATUS · 2 = FAILED']
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC)
panel=Image.new('RGB',(580,520),(10,24,28)); pd=ImageDraw.Draw(panel)
y=16
for i,b in enumerate(blocks):
    pd.text((24,y),tags[i],font=F('b',22),fill=cols[i]); y+=30
    h=b.height+30; pd.rounded_rectangle([20,y,560,y+h],radius=14,outline=cols[i],width=4); panel.paste(b,(30+(520-b.width)//2 if b.width<520 else 30,y+15)); y+=h+12
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255); im.paste(panel,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'BASH  ·  LESSON 37',font=F('b',34),fill=(8,24,26))
d.text((50,160),'BASH BASICS',font=F('x',84),fill=ACC); d.text((50,282),'READ THE LINE',font=F('x',50),fill=TXT); d.text((54,410),'quotes, expansion, exit status',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40); x=54
for t,c in [('echo',GOOD),('$?',WARN),('&&',ACC)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save(B+'/thumbnail.png'); print('ok')
