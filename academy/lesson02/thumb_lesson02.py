import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,560,100],radius=14,fill=ACC); d.text((72,56),'REQUIREMENTS  ·  LESSON 2',font=F('b',34),fill=(8,24,26))
d.text((50,130),'"FAST"',font=F('x',170),fill=ACC); d.text((50,330),'MEANS',font=F('x',100),fill=MUTED); d.text((50,440),'WHAT?',font=F('x',150),fill=TXT)
d.text((54,640),'Write requirements everyone reads the same way',font=F('m',34),fill=TXT)
x=830
for i,n in enumerate(['Must','Should','Could',"Won't (now)"]):
    d.rounded_rectangle([x,150+i*110,x+390,225+i*110],radius=16,fill=PANEL,outline=[GOOD,ACC,(140,164,240),WARN][i],width=4); d.text((x+26,164+i*110),n,font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson02/build/thumbnail.png')
