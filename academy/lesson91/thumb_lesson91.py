import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson91/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,640,100],radius=14,fill=ACC); d.text((72,50),'MAVEN  ·  LESSON 91',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('PUBLISH',ACC),('TO REAL',MUTED),('NEXUS',WARN)]): d.text((50,125+i*135),t,font=F('x',118),fill=c)
d.text((54,590),'snapshot, release, and the 409 rule',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',38)
ys=[150,285,420]
for i,(t,c) in enumerate([('mvn deploy',ACC),('SNAPSHOT',WARN),('409',GOOD)]):
    d.rounded_rectangle([690,ys[i],1240,ys[i]+100],radius=24,fill=PANEL,outline=c,width=6); d.text((712,ys[i]+(28 if len(t)<24 else 34)),t,font=mono if len(t)<24 else ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',29),fill=TXT)
    if i<2: d.polygon([(940,ys[i]+105),(980,ys[i]+105),(960,ys[i]+130)],fill=c)
im.save(B+'/thumbnail.png'); print('ok')
