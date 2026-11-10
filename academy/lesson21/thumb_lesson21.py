import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
sys.path.insert(0,'/home/claude/academy/lesson21')
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson21/build'
import json, term, video as V
sys.path.insert(0,'/home/claude/academy/lesson21')
dur=json.load(open('/home/claude/academy/lesson21/vo/dur.json'))
def fr(scene, cid):
    C,D,f=term.cue_times(V,dur,scene); t=C[cid]+dur[cid]+1.5
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{B}/clip_{scene}.mp4','-frames:v','1','/tmp/th.png']); return Image.open('/tmp/th.png').convert('RGB')
def crop(im, box, w):
    c=im.crop(box); return c.resize((w,int(c.height*w/c.width)),Image.LANCZOS)
tr=fr('tracedemo','t3'); pg=fr('pingdemo','p4'); rf=fr('diagdemo','d8')
blocks=[crop(tr,(0,66,360,126),500), crop(pg,(520,216,760,246),380), crop(rf,(153,36,420,66),440)]
cols=[tuple(ACC)[:3],tuple(WARN)[:3],tuple(BAD)[:3]]
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC)
panel=Image.new('RGB',(580,520),(10,24,28)); pd=ImageDraw.Draw(panel)
pd.text((24,20),'REAL TERMINAL  ·  live lab',font=F('b',26),fill=tuple(ACC)[:3])
y=76
for i,b in enumerate(blocks):
    h=b.height+36; pd.rounded_rectangle([20,y,560,y+h],radius=14,outline=cols[i],width=4); panel.paste(b,(40,y+18)); y+=h+22
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255); im.paste(panel,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'NETWORKING  ·  LESSON 21',font=F('b',34),fill=(8,24,26))
d.text((50,150),'FIND THE',font=F('x',84),fill=ACC); d.text((50,270),'FAULT',font=F('x',96),fill=TXT); d.text((54,420),'ping · traceroute · ss · curl',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40); x=54
for t,c in [('PING',ACC),('TRACE',GOOD),('REFUSED',BAD)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save(B+'/thumbnail.png')
