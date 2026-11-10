import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common'); sys.path.insert(0,'/home/claude/academy/lesson19')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson19/build'
def line(clip, t):
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{B}/{clip}','-frames:v','1','/tmp/th.png'])
    return Image.open('/tmp/th.png').convert('RGB').crop((0,37,540,66))
rows=[line('clip_methoddemo.mp4',14), line('clip_statusdemo.mp4',17), line('clip_statusdemo.mp4',44)]
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC)
panel=Image.new('RGB',(580,520),(10,24,28)); pd=ImageDraw.Draw(panel)
pd.text((24,22),'REAL TERMINAL  ·  curl',font=F('b',26),fill=tuple(ACC)[:3])
cols=[tuple(GOOD)[:3],tuple(WARN)[:3],tuple(BAD)[:3]]
for i,r in enumerate(rows):
    r2=r.resize((r.width,r.height)); y=100+i*135
    pd.rounded_rectangle([20,y-14,560,y+58],radius=14,outline=cols[i],width=4); panel.paste(r2.crop((0,0,520,r2.height)),(30,y+4))
pd.text((24,470),'Read the status first',font=F('m',28),fill=tuple(MUTED)[:3])
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255); im.paste(panel,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'NETWORKING  ·  LESSON 19',font=F('b',34),fill=(8,24,26))
d.text((50,150),'HTTP & HTTPS',font=F('x',78),fill=ACC); d.text((50,270),'EXPLAINED',font=F('x',92),fill=TXT); d.text((54,420),'Status codes · TLS · live',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40); x=54
for t,c in [('200',GOOD),('404',WARN),('500',BAD)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save(B+'/thumbnail.png')
