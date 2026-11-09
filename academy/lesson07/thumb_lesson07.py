import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,520,100],radius=14,fill=ACC); d.text((72,56),'RELEASE  ·  LESSON 7',font=F('b',34),fill=(8,24,26))
d.text((50,130),'SHIP IT',font=F('x',140),fill=ACC); d.text((50,290),'SAFELY',font=F('x',170),fill=TXT)
d.text((54,640),'Environments, approvals, risk and rollback',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('Development',ACC),('Test',GOOD),('Production',WARN),('Rollback',(240,130,130))]):
    d.rounded_rectangle([x,110+i*100,x+330,180+i*100],radius=16,fill=PANEL,outline=c,width=4); d.text((x+26,122+i*100),n,font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson07/build/thumbnail.png')
