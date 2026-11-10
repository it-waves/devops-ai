import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw
im=theme.backdrop().resize((1280,720)); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,48,640,100],radius=14,fill=ACC); d.text((72,56),'FUNDAMENTALS  ·  LESSON 10',font=F('b',34),fill=(8,24,26))
d.text((50,130),'WHY IS',font=F('x',130),fill=ACC); d.text((50,270),'IT SLOW?',font=F('x',130),fill=TXT)
d.text((54,640),'CPU, memory, storage and processes',font=F('m',34),fill=TXT)
x=900
for i,(n,c) in enumerate([('CPU',ACC),('Memory',GOOD),('Storage',WARN),('Processes',(150,160,240)),('Threads',(200,170,240))]):
    d.rounded_rectangle([x,110+i*88,x+330,172+i*88],radius=16,fill=PANEL,outline=c,width=4); d.text((x+26,119+i*88),n,font=F('b',38),fill=TXT)
im.convert('RGB').save('/home/claude/academy/lesson10/build/thumbnail.png')
