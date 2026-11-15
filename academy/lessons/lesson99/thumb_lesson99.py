import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson99/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,780,100],radius=14,fill=ACC); d.text((72,50),'GRADLE SPEED  ·  LESSON 99',font=F('b',34),fill=(8,24,26))
for i,(t_,c_) in enumerate([('SKIP WORK',GOOD),('USE CACHE',ACC),('SAME JAR',WARN)]): d.text((50,125+i*135),t_,font=F('x',100),fill=c_)
d.text((54,590),'faster builds you can prove, byte for byte',font=F('m',36),fill=MUTED)
ys=[150,285,420]
for i,(t_,c_) in enumerate([('UP-TO-DATE',GOOD),('FROM-CACHE',ACC),('sha256 = sha256',WARN)]):
    d.rounded_rectangle([700,ys[i],1250,ys[i]+100],radius=24,fill=PANEL,outline=c_,width=6); d.text((722,ys[i]+30),t_,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34),fill=TXT)
    if i<2: d.polygon([(955,ys[i]+105),(995,ys[i]+105),(975,ys[i]+130)],fill=c_)
im.save(B+'/thumbnail.png'); print('ok')
