import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageOps, ImageFont
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
ph=ImageOps.fit(Image.open('/home/claude/academy/lesson11/assets/photo_l11_laptop_code.jpg').convert('RGB'),(560,520),Image.LANCZOS)
m=Image.new('L',(560,520),0); ImageDraw.Draw(m).rounded_rectangle([0,0,559,519],radius=30,fill=255)
d.rounded_rectangle([664,84,1246,616],radius=40,fill=ACC); im.paste(ph,(670,90),m)
d.rounded_rectangle([50,48,640,100],radius=14,fill=ACC); d.text((72,56),'FUNDAMENTALS  ·  LESSON 11',font=F('b',34),fill=(8,24,26))
d.text((50,135),'LOST IN',font=F('x',100),fill=ACC); d.text((50,265),'THE',font=F('x',100),fill=TXT); d.text((50,395),'TERMINAL?',font=F('x',100),fill=TXT)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',40)
x=54
for t,c in [('pwd',ACC),('ls',GOOD),('cd',WARN)]:
    w=int(mono.getlength(t))+44; d.rounded_rectangle([x,590,x+w,660],radius=16,fill=PANEL,outline=c,width=4); d.text((x+22,600),t,font=mono,fill=TXT); x+=w+22
im.save('/home/claude/academy/lesson11/build/thumbnail.png')
