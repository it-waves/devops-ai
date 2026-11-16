import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
VIO = (140,164,240)
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson117/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,640,100],radius=14,fill=ACC); d.text((72,50),'CLOUDCART V0  ·  LESSON 117',font=F('b',32),fill=(8,24,26))
d.text((50,130),'PROVE',font=F('x',100),fill=ACC); d.text((50,250),'IT.',font=F('x',150),fill=VIO)
d.text((54,440),'v0 mastery evidence',font=F('b',44),fill=TXT)
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
x=54
for t_,c_ in [('CLONE',ACC),('BUILD',(245,185,66)),('TAG',(120,230,160))]:
    w=int(d.textlength(t_,font=M))+48; d.rounded_rectangle([x,525,x+w,595],radius=22,fill=PANEL,outline=c_,width=5); d.text((x+24,539),t_,font=M,fill=TXT); x+=w+18
d.text((54,630),'real git, Maven and Tomcat',font=F('m',34),fill=MUTED)
for j,(a,b,c_) in enumerate([('5 CHECKS','one command judges you',ACC),('32 TESTS','run by Maven',(245,185,66)),('1 TAG','cloudcart-v0',(120,230,160))]):
    y=170+j*150
    d.rounded_rectangle([700,y,1235,y+125],radius=26,fill=PANEL,outline=c_,width=6)
    d.text((730,y+16),a,font=F('x',46),fill=c_); d.text((730,y+78),b,font=F('b',34),fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
