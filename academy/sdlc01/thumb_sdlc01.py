import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,520,100],radius=14,fill=ACC); d.text((72,56),'SDLC  ·  LESSON 1',font=F('b',34),fill=(8,24,26))
d.text((50,130),'IDEA TO',font=F('x',130),fill=ACC); d.text((50,270),'CUSTOMER',font=F('x',140),fill=TXT)
d.text((54,640),'The 7 stages of software delivery',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('1  Plan',WARN),('2  Requirements',ACC),('3  Design',(140,164,240)),('4  Build',GOOD),('5  Test',(200,170,240)),('6  Deploy',WARN),('7  Operate',(140,164,240))]):
    d.rounded_rectangle([x,50+i*80,x+330,108+i*80],radius=16,fill=PANEL,outline=c,width=4); d.text((x+24,56+i*80),n,font=F('b',36),fill=TXT)
im.convert('RGB').save('/home/claude/academy/sdlc01/build/thumbnail.png')
