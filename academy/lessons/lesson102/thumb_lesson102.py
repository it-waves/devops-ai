import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
VIO = (140,164,240)
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson102/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,860,100],radius=14,fill=ACC); d.text((72,50),'BUILD TOOLS  ·  LESSON 102',font=F('b',34),fill=(8,24,26))
d.text((50,125),'MAVEN',font=F('x',110),fill=ACC); d.text((50,255),'vs GRADLE',font=F('x',110),fill=VIO)
d.text((54,420),'same project, both builds',font=F('b',44),fill=TXT)
d.text((54,590),'then you choose',font=F('m',40),fill=MUTED)
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
for i,(t_,c_) in enumerate([('pom.xml',ACC),('build.gradle',VIO)]):
    y=190+i*160; d.rounded_rectangle([830,y,1250,y+110],radius=24,fill=PANEL,outline=c_,width=6); d.text((862,y+34),t_,font=M,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
