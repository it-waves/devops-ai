import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson69/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,520,100],radius=14,fill=ACC); d.text((72,50),'TEST ANY ENDPOINT',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('curl -v',ACC),('time it.',WARN),('exit 22?',BAD)]): d.text((50,150+i*150),t,font=F('x',112),fill=c)
d.text((54,620),'inspect any API',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
d.rounded_rectangle([640,150,1240,270],radius=24,fill=PANEL,outline=GOOD,width=6); d.text((668,190),'< X-API-Version: 2.3',font=mono,fill=TXT)
d.rounded_rectangle([640,300,1240,420],radius=24,fill=PANEL,outline=BAD,width=6); d.text((668,340),'200  0.901348s',font=mono,fill=TXT)
d.rounded_rectangle([640,450,1240,670],radius=24,fill=PANEL,outline=ACC,width=6); d.text((668,500),'exit=22',font=mono,fill=BAD); d.text((668,560),'X-Request-Id: lab69',font=mono,fill=TXT)
im.save(B+'/thumbnail.png'); print('ok')
