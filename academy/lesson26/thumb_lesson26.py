import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
sys.path.insert(0,'/home/claude/academy/lesson26')
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson26/build'
import json, term, video as V
dur=json.load(open('/home/claude/academy/lesson26/vo/dur.json'))
def fr(scene, cid):
    C,D,f=term.cue_times(V,dur,scene); t=C[cid]+dur[cid]+1.5
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{B}/clip_{scene}.mp4','-frames:v','1','/tmp/th.png']); return Image.open('/tmp/th.png').convert('RGB')
def crop(im, box, w):
    c=im.crop(box); return c.resize((w,int(c.height*w/c.width)),Image.LANCZOS)
t1=fr('tour','t2'); t2=fr('tour','t4')
blocks=[crop(t1,(0,0,860,100),520), crop(t2,(0,0,860,130),520)]
cols=[tuple(BAD)[:3],tuple(GOOD)[:3]]
tags=['REAL TERMINAL · ONE TREE','REAL TERMINAL · LINKS INTO /USR']
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC)
panel=Image.new('RGB',(580,520),(10,24,28)); pd=ImageDraw.Draw(panel)
y=22
for i,b in enumerate(blocks):
    pd.text((24,y),tags[i],font=F('b',22),fill=cols[i]); y+=34
    h=b.height+30; pd.rounded_rectangle([20,y,560,y+h],radius=14,outline=cols[i],width=4); panel.paste(b,(30+(520-b.width)//2 if b.width<520 else 30,y+15)); y+=h+26
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255); im.paste(panel,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'LINUX  ·  LESSON 26',font=F('b',34),fill=(8,24,26))
d.text((50,160),'THE MAP',font=F('x',84),fill=ACC); d.text((50,282),'PATHS AND MANUALS',font=F('x',50),fill=TXT); d.text((54,410),'where, move, find help',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40); x=54
for t,c in [('pwd',GOOD),('cd',WARN),('man',ACC)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save(B+'/thumbnail.png'); print('ok')
