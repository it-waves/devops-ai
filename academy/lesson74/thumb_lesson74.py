import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson74/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,520,100],radius=14,fill=ACC); d.text((72,50),'FOLLOW THE REQUEST',font=F('b',30),fill=(8,24,26))
for i,(t,c) in enumerate([('DRAW.',ACC),('TRACE.',WARN),('FIND IT.',GOOD)]): d.text((50,150+i*150),t,font=F('x',100),fill=c)
d.text((54,620),'web, API, database',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',32)
bx=[('browser',(140,164,240)),('web   :8080',ACC),('api   :5000',GOOD),('shop.db',WARN)]
for i,(t,c) in enumerate(bx):
    y=36+i*140
    d.rounded_rectangle([700,y,1230,y+100],radius=24,fill=PANEL,outline=c,width=6); d.text((730,y+30),t,font=mono,fill=TXT)
    if i<3:
        cx=965; d.line([(cx,y+104),(cx,y+136)],fill=c,width=8); d.polygon([(cx-16,y+126),(cx+16,y+126),(cx,y+140)],fill=c)
d.rounded_rectangle([700,610,1230,670],radius=16,fill=PANEL,outline=BAD,width=4); d.text((724,624),'trace-1  web.log  api.log',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',28),fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
