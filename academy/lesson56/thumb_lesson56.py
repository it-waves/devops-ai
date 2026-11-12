import sys, subprocess; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
sys.path.insert(0,'/home/claude/academy/lesson56')
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson56/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,560,100],radius=14,fill=ACC); d.text((72,50),'PYTHON  ·  LESSON 56',font=F('b',34),fill=(8,24,26))
d.text((50,135),'PROVE IT',font=F('x',46),fill=TXT)
for i,(t,c) in enumerate([('MASTERY',ACC),('SCENARIO',WARN),('4 FAULTS',GOOD)]):
    d.text((50,200+i*135),t,font=F('x',78),fill=c)
d.text((54,620),'fix it, check it, clean up',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',72)
for i,(t,c) in enumerate([('FAIL x4',BAD),('PASS x4',GOOD),('lab down',ACC)]):
    y=150+i*170; d.rounded_rectangle([800,y,1240,y+135],radius=28,fill=PANEL,outline=c,width=6)
    f=mono if len(t)<=6 else ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',56)
    w=d.textlength(t,font=f); d.text((1020-w/2,y+68-f.size*0.6),t,font=f,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
