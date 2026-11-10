import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson20/build'
def fr(t):
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',f'{B}/clip_digdemo.mp4','-frames:v','1','/tmp/th.png']); return Image.open('/tmp/th.png').convert('RGB')
def crop(im, box, w):
    c=im.crop(box); return c.resize((w,int(c.height*w/c.width)),Image.LANCZOS)
a=fr(26); mx=fr(42); nx=fr(55)
blocks=[crop(a,(600,36,930,94),500), crop(mx,(300,37,990,66),500), crop(nx,(455,37,720,66),420)]
cols=[tuple(ACC)[:3],tuple(WARN)[:3],tuple(BAD)[:3]]
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC)
panel=Image.new('RGB',(580,520),(10,24,28)); pd=ImageDraw.Draw(panel)
pd.text((24,20),'REAL TERMINAL  ·  dig',font=F('b',26),fill=tuple(ACC)[:3])
y=76
for i,b in enumerate(blocks):
    h=b.height+36; pd.rounded_rectangle([20,y,560,y+h],radius=14,outline=cols[i],width=4); panel.paste(b,(40,y+18)); y+=h+22
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255); im.paste(panel,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'NETWORKING  ·  LESSON 20',font=F('b',34),fill=(8,24,26))
d.text((50,150),'DNS: NAME',font=F('x',84),fill=ACC); d.text((50,270),'TO PAGE',font=F('x',96),fill=TXT); d.text((54,420),'Lookup · records · one request',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40); x=54
for t,c in [('A',ACC),('CNAME',GOOD),('NXDOMAIN',BAD)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save(B+'/thumbnail.png')
