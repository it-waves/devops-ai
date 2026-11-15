import sys; sys.path.insert(0,'/home/claude/osi'); sys.path.insert(0,'/home/claude/academy/common')
import theme
from engine import *
from PIL import Image, ImageDraw, ImageFont
B='/home/claude/academy/lesson97/build'
im=theme.backdrop().resize((1280,720)).convert('RGB'); d=ImageDraw.Draw(im)
d.rounded_rectangle([50,40,780,100],radius=14,fill=ACC); d.text((72,50),'GRADLE DEPENDENCIES  ·  LESSON 97',font=F('b',34),fill=(8,24,26))
for i,(t,c) in enumerate([('SCOPES,',MUTED),('CATALOG',ACC),('& PUBLISH',GOOD)]): d.text((50,125+i*135),t,font=F('x',100),fill=c)
d.text((54,590),'dependencies, versions and plugins in Gradle',font=F('m',36),fill=MUTED)
mono=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',38)
ys=[150,285,420]
for i,(t,c) in enumerate([('testImplementation',BAD),('libs.versions.toml',GOOD),('./gradlew publish',WARN)]):
    d.rounded_rectangle([700,ys[i],1250,ys[i]+100],radius=24,fill=PANEL,outline=c,width=6); d.text((722,ys[i]+30),t,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',34),fill=TXT)
    if i<2: d.polygon([(955,ys[i]+105),(995,ys[i]+105),(975,ys[i]+130)],fill=c)
im.save(B+'/thumbnail.png'); print('ok')
