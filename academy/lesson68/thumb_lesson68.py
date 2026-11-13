import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson68/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,520,100],radius=14,fill=ACC); d.text((72,50),'REQUEST & RESPONSE',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('GET.',ACC),('POST.',WARN),('404?',BAD)]): d.text((50,150+i*150),t,font=F('x',112),fill=c)
d.text((54,620),'read the status code',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
d.rounded_rectangle([640,150,1240,270],radius=24,fill=PANEL,outline=GOOD,width=6); d.text((668,190),'HTTP/1.0 201 Created',font=mono,fill=TXT)
d.rounded_rectangle([640,300,1240,420],radius=24,fill=PANEL,outline=BAD,width=6); d.text((668,340),'HTTP/1.0 404 Not Found',font=mono,fill=TXT)
s=Image.open('/home/claude/academy/lesson68/shots/after.png').convert('RGB').resize((560,168))
d.rounded_rectangle([640,450,1240,670],radius=24,fill=PANEL,outline=ACC,width=6); im.paste(s,(660,476)); d.text((668,640),'',font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
