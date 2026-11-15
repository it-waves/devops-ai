import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson101/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,900,100],radius=14,fill=ACC); d.text((72,50),'FIX GRADLE FAILURES  ·  LESSON 101',font=F('b',34),fill=(8,24,26))
for i,(t_,c_) in enumerate([('READ THE ERROR',WARN),('FIND THE PHASE',ACC),('FIX IT',GOOD)]): d.text((50,125+i*135),t_,font=F('x',76),fill=c_)
d.text((54,590),'daemon  ·  dependency  ·  task',font=F('m',36),fill=MUTED)
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',30)
ys=[150,285,420]
for i,(t_,c_) in enumerate([('Unable to start',BAD),('Could not find',WARN),('Execution failed',ACC)]):
    d.rounded_rectangle([850,ys[i],1250,ys[i]+100],radius=24,fill=PANEL,outline=c_,width=6); d.text((872,ys[i]+32),t_,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',27),fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
