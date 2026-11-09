import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,480,100],radius=14,fill=ACC); d.text((72,56),'ROLES  ·  LESSON 5',font=F('b',34),fill=(8,24,26))
d.text((50,130),'WHO DOES',font=F('x',130),fill=ACC); d.text((50,275),'WHAT?',font=F('x',170),fill=TXT)
d.text((54,640),'Developer, QA, security, operations and DevOps',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('Product',WARN),('Developers',ACC),('QA',GOOD),('Security',(240,130,140)),('Operations',(140,164,240)),('DevOps',(200,170,240))]):
    d.rounded_rectangle([x,70+i*93,x+330,132+i*93],radius=16,fill=PANEL,outline=c,width=4); d.text((x+26,78+i*93),n,font=F('b',38),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson05/build/thumbnail.png')
