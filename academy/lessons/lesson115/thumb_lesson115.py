import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
VIO = (140,164,240)
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson115/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,640,100],radius=14,fill=ACC); d.text((72,50),'CLOUDCART V0  ·  LESSON 115',font=F('b',32),fill=(8,24,26))
d.text((50,130),'DEPLOY',font=F('x',92),fill=ACC); d.text((50,240),'IT.',font=F('x',150),fill=VIO)
d.text((54,425),'war file to live app',font=F('b',44),fill=TXT)
for i,(t_,c_) in enumerate([('COPY',ACC),('CLICK',(245,185,66)),('REMOVE',(120,230,160))]):
    x=54+i*(0 if i==0 else 0); 
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
x=54
for t_,c_ in [('COPY',ACC),('CLICK',(245,185,66)),('REMOVE',(120,230,160))]:
    w=int(d.textlength(t_,font=M))+48; d.rounded_rectangle([x,525,x+w,595],radius=22,fill=PANEL,outline=c_,width=5); d.text((x+24,539),t_,font=M,fill=TXT); x+=w+18
d.text((54,630),'real Tomcat · by hand + Manager',font=F('m',34),fill=MUTED)
shot=Image.open('/home/claude/academy/lesson115/th_app.png').convert('RGB').crop((0,330,1150,780)).resize((570,223))
m=Image.new('L',shot.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,shot.size[0]-1,shot.size[1]-1],radius=26,fill=255)
fr=Image.new('RGB',(shot.size[0]+16,shot.size[1]+16),ACC); fm=Image.new('L',fr.size,0); ImageDraw.Draw(fm).rounded_rectangle([0,0,fr.size[0]-1,fr.size[1]-1],radius=32,fill=255)
im.paste(fr,(672,250),fm); im.paste(shot,(680,258),m)
im.save(B+'/thumbnail.png'); print('ok')
