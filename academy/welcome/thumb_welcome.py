import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/sdlc01')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,420,100],radius=14,fill=ACC); d.text((72,56),'START HERE',font=F('b',34),fill=(8,24,26))
d.text((50,150),'DEVOPS',font=F('x',170),fill=TXT); d.text((50,330),'BOOTCAMP',font=F('x',140),fill=ACC)
d.text((54,540),'Zero to production.',font=F('b',58),fill=TXT); d.text((54,620),'What you will learn, step by step',font=F('m',40),fill=MUTED)
for i,n in enumerate(['Learn','Build','Break','Fix','Operate']):
    d.rounded_rectangle([900,140+i*100,1230,210+i*100],radius=16,fill=PANEL,outline=[ACC,(140,164,240),WARN,GOOD,(198,172,240)][i],width=4); d.text((926,152+i*100),n,font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/welcome/build/thumbnail.png')
