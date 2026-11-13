import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson75/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,640,100],radius=14,fill=ACC); d.text((72,50),'APIs & ARCHITECTURE  ·  MASTERY',font=F('b',32),fill=(8,24,26))
for i,(t,c) in enumerate([('FIX',ACC),('THE BROKEN',WARN),('SHOP.',GOOD)]): d.text((50,140+i*140),t,font=F('x',100 if i!=1 else 92),fill=c)
d.text((54,620),'4 faults · 1 checker',font=F('m',38),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40)
rows=[('web  200',GOOD),('api  000',BAD)]
d.rounded_rectangle([780,150,1240,330],radius=28,fill=PANEL,outline=BAD,width=6)
for i,(t,c) in enumerate(rows): d.text((820,180+i*65),t,font=mono,fill=c)
d.rounded_rectangle([780,370,1240,560],radius=28,fill=PANEL,outline=WARN,width=6)
for i,(t,c) in enumerate([('FAIL 1  FAIL 2',BAD),('FAIL 3  FAIL 4',BAD)]): d.text((810,400+i*65),t,font=mono,fill=c)
d.text((800,590),'find the broken layer',font=F('b',34),fill=WARN)
im.save(B+'/thumbnail.png'); print('ok')
