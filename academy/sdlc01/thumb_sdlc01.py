import sys; sys.path.insert(0,'/home/claude/osi')
from engine import *
from PIL import Image, ImageDraw
im=Image.new('RGBA',(1280,720),BG0); d=ImageDraw.Draw(im)
for y in range(720): d.line([(0,y),(1280,y)],fill=tuple(int(BG0[i]*(1-y/720)+BG1[i]*(y/720)) for i in range(3))+(255,))
d.rounded_rectangle([50,48,520,100],radius=14,fill=ACC); d.text((72,56),'SDLC  ·  LESSON 1',font=F('b',34),fill=(12,18,28))
d.text((50,150),'IDEA',font=F('x',170),fill=TXT); d.text((50,330),'TO',font=F('x',110),fill=MUTED); d.text((50,440),'CUSTOMER',font=F('x',150),fill=ACC)
d.text((54,630),'The 7 stages of software delivery',font=F('m',44),fill=TXT)
x=760
for i,n in enumerate(['Plan','Design','Build','Test','Deploy']):
    d.rounded_rectangle([x,150+i*100,x+420,220+i*100],radius=16,fill=PANEL,outline=[ACC,(167,139,250),GOOD,WARN,(244,114,182)][i],width=4); d.text((x+26,162+i*100),f'{i+1}  {n}',font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/sdlc01/build/thumbnail.png')
