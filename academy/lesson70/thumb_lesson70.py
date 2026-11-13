import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson70/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,560,100],radius=14,fill=ACC); d.text((72,50),'LOGIN, TOKENS, SECRETS',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('401.',BAD),('403.',WARN),('Bearer.',ACC)]): d.text((50,150+i*150),t,font=F('x',112),fill=c)
d.text((54,620),'who are you?',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
d.rounded_rectangle([640,150,1240,270],radius=24,fill=PANEL,outline=BAD,width=6); d.text((668,190),'HTTP/1.1 401 Unauthorized',font=mono,fill=TXT)
d.rounded_rectangle([640,300,1240,420],radius=24,fill=PANEL,outline=WARN,width=6); d.text((668,340),'HTTP/1.1 403 Forbidden',font=mono,fill=TXT)
d.rounded_rectangle([640,450,1240,670],radius=24,fill=PANEL,outline=ACC,width=6); d.text((668,500),'-rw-------  secrets.env',font=mono,fill=GOOD); d.text((668,560),'Authorization: Bearer ...',font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
