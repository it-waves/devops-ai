import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
sys.path.insert(0,'/home/claude/academy/lesson48')
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson48/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,560,100],radius=14,fill=ACC); d.text((72,50),'PYTHON  ·  LESSON 48',font=F('b',34),fill=(8,24,26))
d.text((50,130),'WRITE YOUR',font=F('x',56),fill=TXT)
for i,(t,c) in enumerate([('TYPES',ACC),('LOOPS',WARN),('FUNCTIONS',GOOD)]):
    d.text((50,200+i*135),t,font=F('x',104),fill=c)
d.text((54,620),'first Python for DevOps',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',72)
for i,(t,c) in enumerate([('[80, 443]',ACC),('for x in',WARN),('def run():',GOOD)]):
    y=150+i*170; d.rounded_rectangle([800,y,1240,y+135],radius=28,fill=PANEL,outline=c,width=6)
    f=mono if len(t)<=6 else ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',56)
    w=d.textlength(t,font=f); d.text((1020-w/2,y+68-f.size*0.6),t,font=f,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
