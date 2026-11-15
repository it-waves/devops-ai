import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
VIO = (140,164,240)
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson114/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,640,100],radius=14,fill=ACC); d.text((72,50),'CLOUDCART V0  ·  LESSON 114',font=F('b',32),fill=(8,24,26))
d.text((50,130),'BUILD THE',font=F('x',92),fill=ACC); d.text((50,240),'WAR.',font=F('x',150),fill=VIO)
d.text((54,425),'one command, one file',font=F('b',44),fill=TXT)
for i,(t_,c_) in enumerate([('POM',ACC),('TEST',(245,185,66)),('PACKAGE',(120,230,160))]):
    x=54+i*(0 if i==0 else 0); 
M=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34)
x=54
for t_,c_ in [('POM',ACC),('TEST',(245,185,66)),('PACKAGE',(120,230,160))]:
    w=int(d.textlength(t_,font=M))+48; d.rounded_rectangle([x,525,x+w,595],radius=22,fill=PANEL,outline=c_,width=5); d.text((x+24,539),t_,font=M,fill=TXT); x+=w+18
d.text((54,630),'Maven · real build · real WAR',font=F('m',34),fill=MUTED)
px=Image.new('RGB',(570,365),(10,22,26)); pd=ImageDraw.Draw(px); MF=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',23)
pd.rectangle([0,0,570,40],fill=(24,44,50))
for i_,c_ in enumerate([(255,95,86),(255,189,46),(39,201,63)]): pd.ellipse([16+i_*30,12,32+i_*30,28],fill=c_)
for j,(t_,c_) in enumerate([('$ mvn package',TXT),('--- compiler:compile',MUTED),('--- surefire:test',MUTED),('Tests run: 32',(245,185,66)),('--- war:war',MUTED),('Building war: cloudcart.war',(120,230,160)),('BUILD SUCCESS',(120,230,160))]): pd.text((20,58+j*43),t_,font=MF,fill=c_)
shot=px
m=Image.new('L',shot.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,shot.size[0]-1,shot.size[1]-1],radius=26,fill=255)
fr=Image.new('RGB',(shot.size[0]+16,shot.size[1]+16),ACC); fm=Image.new('L',fr.size,0); ImageDraw.Draw(fm).rounded_rectangle([0,0,fr.size[0]-1,fr.size[1]-1],radius=32,fill=255)
im.paste(fr,(672,170),fm); im.paste(shot,(680,178),m)
im.save(B+'/thumbnail.png'); print('ok')
