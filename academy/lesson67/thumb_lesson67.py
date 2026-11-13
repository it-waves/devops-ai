import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson67/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,560,100],radius=14,fill=ACC); d.text((72,50),'APP ARCHITECTURE',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('FRONT.',ACC),('BACK.',WARN),('DATA.',GOOD)]): d.text((50,150+i*150),t,font=F('x',100),fill=c)
d.text((54,620),'who does what?',font=F('m',40),fill=MUTED)
s=Image.open('/home/claude/academy/lesson67/shots/page.png').convert('RGB').crop((0,0,1100,330)).resize((560,168))
d.rounded_rectangle([660,150,1240,370],radius=24,fill=PANEL,outline=ACC,width=6); im.paste(s,(670,192))
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
d.rounded_rectangle([660,400,1240,520],radius=24,fill=PANEL,outline=WARN,width=6); d.text((690,440),'{"name":"Backpack"}',font=mono,fill=TXT)
d.rounded_rectangle([660,550,1240,660],radius=24,fill=PANEL,outline=GOOD,width=6); d.text((690,585),'shop.db  ·  3 rows',font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
