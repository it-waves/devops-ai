import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,520,100],radius=14,fill=ACC); d.text((72,56),'TRACE  ·  LESSON 6',font=F('b',34),fill=(8,24,26))
d.text((50,130),'TRACE ONE',font=F('x',120),fill=ACC); d.text((50,270),'CHANGE',font=F('x',170),fill=TXT)
d.text((54,640),'Requirement to feedback in seven steps',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('1  Requirement',WARN),('2  Code',ACC),('3  Review',(140,164,240)),('4  Test',GOOD),('5  Release',(200,170,240)),('6  Deploy',WARN),('7  Feedback',(140,164,240))]):
    d.rounded_rectangle([x,50+i*80,x+330,108+i*80],radius=16,fill=PANEL,outline=c,width=4); d.text((x+24,56+i*80),n,font=F('b',36),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson06/build/thumbnail.png')
