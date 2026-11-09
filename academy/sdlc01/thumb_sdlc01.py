import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/sdlc01')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,520,100],radius=14,fill=ACC); d.text((72,56),'SDLC  ·  LESSON 1',font=F('b',34),fill=(8,24,26))
d.text((50,150),'IDEA',font=F('x',170),fill=TXT); d.text((50,330),'TO',font=F('x',110),fill=MUTED); d.text((50,440),'CUSTOMER',font=F('x',150),fill=ACC)
d.text((54,630),'The 7 stages of software delivery',font=F('m',44),fill=TXT)
x=760
for i,n in enumerate(['Plan','Design','Build','Test','Deploy']):
    d.rounded_rectangle([x,150+i*100,x+420,220+i*100],radius=16,fill=PANEL,outline=[ACC,(140,164,240),GOOD,WARN,(198,172,240)][i],width=4); d.text((x+26,162+i*100),f'{i+1}  {n}',font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/sdlc01/build/thumbnail.png')
