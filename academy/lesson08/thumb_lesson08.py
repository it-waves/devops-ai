import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,560,100],radius=14,fill=ACC); d.text((72,56),'MASTERY  ·  LESSON 8',font=F('b',34),fill=(8,24,26))
d.text((50,130),'DESIGN THE',font=F('x',120),fill=ACC); d.text((50,290),'WORKFLOW',font=F('x',108),fill=TXT)
d.text((54,640),'Your CloudCart SDLC, with a pass or fail rubric',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('1  Stages',ACC),('2  Owners',(140,164,240)),('3  Artifacts',GOOD),('4  Handoffs',WARN),('5  Rollback',(240,130,130))]):
    d.rounded_rectangle([x,90+i*90,x+330,150+i*90],radius=16,fill=PANEL,outline=c,width=4); d.text((x+26,98+i*90),n,font=F('b',38),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson08/build/thumbnail.png')
