import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme, logos as LG
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson59/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,610,100],radius=14,fill=ACC); d.text((72,50),'GIT & GITHUB  ·  LESSON 59',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('BRANCH.',ACC),('MERGE.',WARN),('RESOLVE.',GOOD)]): d.text((50,150+i*150),t,font=F('x',100),fill=c)
d.text((54,620),'switch · merge · conflicts',font=F('m',38),fill=MUTED)
for i,(n,x) in enumerate([('git',820),('github',1040)]):
    lg=LG.chip(n,170,None,None,None); d.rounded_rectangle([x-10,150,x+200,360],radius=30,fill=PANEL,outline=[ACC,GOOD][i],width=6); im.paste(lg,(x+(210-lg.width)//2-10,150+(210-lg.height)//2),lg if lg.mode=='RGBA' else None)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',46)
d.rounded_rectangle([820,420,1240,550],radius=28,fill=PANEL,outline=WARN,width=6); w=d.textlength('<<< == >>>',font=mono); d.text((1030-w/2,455),'<<< == >>>',font=mono,fill=TXT)
d.text((830,575),'never fear a conflict',font=F('b',34),fill=WARN)
im.save(B+'/thumbnail.png'); print('ok')
