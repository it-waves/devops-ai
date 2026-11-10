import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common'); sys.path.insert(0,'/home/claude/academy/lesson17')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageOps, ImageFont
import video as V
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
art=V.router_art(740,500).convert('RGB').crop((18,18,730,490)); ph=Image.new('RGB',(580,520),(12,30,34)); ph.paste(art.resize((580,384),Image.LANCZOS),(0,68))
m=Image.new('L',(580,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,579,519],radius=30,fill=255)
d.rounded_rectangle([654,84,1246,616],radius=40,fill=ACC); im.paste(ph,(660,90),m)
d.rounded_rectangle([50,48,690,100],radius=14,fill=ACC); d.text((72,56),'NETWORKING  ·  LESSON 17',font=F('b',34),fill=(8,24,26))
d.text((50,150),'IP ADDRESSES',font=F('x',78),fill=ACC); d.text((50,270),'DECODED',font=F('x',96),fill=TXT); d.text((54,420),'Private · CIDR · gateway, live',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40)
x=54
for t,c in [('/24',ACC),('PRIVATE',GOOD),('GATEWAY',WARN)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save('/home/claude/academy/lesson17/build/thumbnail.png')
