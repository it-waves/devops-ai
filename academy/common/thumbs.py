import sys; sys.path.insert(0,'/home/claude/academy/common')
from kit import *
import random
def base():
    im = theme.backdrop().resize((1280, 720)); return im
# Welcome
im = base(); d = ImageDraw.Draw(im); rnd = random.Random(3)
d.rounded_rectangle([50, 48, 420, 100], radius=14, fill=EN.ACC); d.text((72, 56), 'START HERE', font=F('b', 34), fill=INK)
d.text((50, 160), 'DEVOPS', font=F('x', 130), fill=EN.TXT); d.text((50, 310), 'BOOTCAMP', font=F('x', 130), fill=EN.ACC); d.text((54, 500), 'Zero to production.', font=F('m', 52), fill=EN.TXT)
d.text((54, 580), 'Step by step', font=F('m', 40), fill=EN.MUTED)
names = ['docker', 'kubernetes', 'jenkins', 'terraform', 'git', 'ansible', 'prometheus', 'grafana', 'maven']
for i, n in enumerate(names): im.alpha_composite(LG.chip(n, 130), (830 + (i % 3) * 150, 130 + (i // 3) * 170))
im.convert('RGB').save('/home/claude/academy/welcome/build/thumbnail.png')
# SDLC
im = base(); d = ImageDraw.Draw(im)
d.rounded_rectangle([50, 48, 520, 100], radius=14, fill=EN.ACC); d.text((72, 56), 'SDLC  ·  LESSON 1', font=F('b', 34), fill=INK)
d.text((50, 150), 'IDEA', font=F('x', 170), fill=EN.TXT); d.text((50, 330), 'TO', font=F('x', 110), fill=EN.MUTED); d.text((50, 450), 'CUSTOMER', font=F('x', 118), fill=EN.ACC)
d.text((54, 630), 'The 7 stages of software delivery', font=F('m', 44), fill=EN.TXT)
im.alpha_composite(bulb(150), (860, 120)); im.alpha_composite(parcel(150), (1060, 120))
for i, n in enumerate(['git', 'maven', 'jenkins', 'docker']): im.alpha_composite(LG.chip(n, 130), (790 + (i % 2) * 150, 330 + (i // 2) * 150))
im.alpha_composite(house(200), (1060, 400))
im.convert('RGB').save('/home/claude/academy/sdlc01/build/thumbnail.png')
