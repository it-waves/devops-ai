import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson72/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,560,100],radius=14,fill=ACC); d.text((72,50),'STATE, SERVERS, DATA',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('CART.',ACC),('GONE.',BAD),('FIXED.',GOOD)]): d.text((50,150+i*150),t,font=F('x',112),fill=c)
d.text((54,620),'stateful vs stateless',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
d.rounded_rectangle([640,150,1240,270],radius=24,fill=PANEL,outline=BAD,width=6); d.text((668,190),'server 5000: cart [1]',font=mono,fill=TXT)
d.rounded_rectangle([640,300,1240,420],radius=24,fill=PANEL,outline=WARN,width=6); d.text((668,340),'server 5001: cart []',font=mono,fill=TXT)
d.rounded_rectangle([640,450,1240,670],radius=24,fill=PANEL,outline=ACC,width=6); d.text((668,500),'STORAGE=db  shared',font=mono,fill=GOOD); d.text((668,560),'cart: [2]  survives',font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
