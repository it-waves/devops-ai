import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson100/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,860,100],radius=14,fill=ACC); d.text((72,50),'GRADLE IN CI  ·  LESSON 100',font=F('b',34),fill=(8,24,26))
for i,(t_,c_) in enumerate([('PUSH CODE',GOOD),('CI BUILDS IT',ACC),('JAR SAVED',WARN)]): d.text((50,125+i*135),t_,font=F('x',100),fill=c_)
d.text((54,590),'GitHub Actions workflow, fixed step by step',font=F('m',36),fill=MUTED)
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
ys=[150,285,420]
for i,(t_,c_) in enumerate([('on: push',GOOD),('setup-gradle',ACC),('upload-artifact',WARN)]):
    d.rounded_rectangle([760,ys[i],1250,ys[i]+100],radius=24,fill=PANEL,outline=c_,width=6); d.text((782,ys[i]+30),t_,font=M,fill=TXT)
    if i<2: d.polygon([(985,ys[i]+105),(1025,ys[i]+105),(1005,ys[i]+130)],fill=c_)
im.save(B+'/thumbnail.png'); print('ok')
