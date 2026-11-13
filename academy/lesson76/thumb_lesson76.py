import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson76/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,520,100],radius=14,fill=ACC); d.text((72,50),'JAVA FOR DEVOPS',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('JDK',ACC),('JRE',WARN),('JVM',GOOD)]): d.text((50,130+i*140),t,font=F('x',120),fill=c)
d.text((54,590),'what runs what?',font=F('m',40),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40)
ys=[150,285,420]
for i,(t,c) in enumerate([('Hello.java',ACC),('Hello.class',WARN),('java Hello',GOOD)]):
    d.rounded_rectangle([740,ys[i],1240,ys[i]+100],radius=24,fill=PANEL,outline=c,width=6); d.text((775,ys[i]+26),t,font=mono,fill=TXT)
    if i<2: d.polygon([(970,ys[i]+105),(1010,ys[i]+105),(990,ys[i]+130)],fill=c)
d.text((750,560),'cafe babe',font=mono,fill=WARN)
im.save(B+'/thumbnail.png'); print('ok')
