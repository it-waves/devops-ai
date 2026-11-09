import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,500,100],radius=14,fill=ACC); d.text((72,56),'PARTS  ·  LESSON 4',font=F('b',34),fill=(8,24,26))
d.text((50,130),'THE 9 PARTS',font=F('x',110),fill=ACC); d.text((50,260),'OF AN APP',font=F('x',140),fill=TXT)
d.text((54,640),'API, database, build, release and operations',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('Frontend',ACC),('Backend',(140,164,240)),('API',GOOD),('Database',WARN),('Deploy',(200,170,240))]):
    d.rounded_rectangle([x,110+i*100,x+330,180+i*100],radius=16,fill=PANEL,outline=c,width=4); d.text((x+26,122+i*100),n,font=F('b',40),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson04/build/thumbnail.png')
