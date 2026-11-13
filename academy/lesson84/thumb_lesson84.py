import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson84/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,610,100],radius=14,fill=ACC); d.text((72,50),'JAVA MASTERY LAB',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('FIX',ACC),('THE',MUTED),('RELEASE',WARN)]): d.text((50,125+i*135),t,font=F('x',118),fill=c)
d.text((54,590),'4 faults, 1 checker, 1 report',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',38)
ys=[90,225,360,495]
for i,(t,c) in enumerate([('TEST FAILS',BAD),('NO MAIN-CLASS',WARN),('PORT: eighty',GOOD),('HEAP: 8 MB',ACC)]):
    d.rounded_rectangle([700,ys[i],1240,ys[i]+105],radius=24,fill=PANEL,outline=c,width=6); d.text((730,ys[i]+28),t,font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
