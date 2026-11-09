import sys; sys.path.insert(0,'/home/claude/academy/common')
from kit import *
import random
def base(): return theme.backdrop().resize((1280, 720)).convert('RGBA')
# INTRO
im = base(); d = ImageDraw.Draw(im)
d.rounded_rectangle([50, 48, 300, 104], radius=16, fill=EN.ACC); d.text((76, 58), 'INTRO', font=F('x', 38), fill=INK)
d.text((50, 160), 'DEVOPS', font=F('x', 130), fill=EN.TXT); d.text((50, 310), 'BOOTCAMP', font=F('x', 130), fill=EN.ACC)
d.text((54, 500), 'Zero to production.', font=F('m', 52), fill=EN.TXT); d.text((54, 580), 'What you will learn, in 3 minutes', font=F('m', 38), fill=EN.MUTED)
names = ['docker', 'kubernetes', 'jenkins', 'terraform', 'git', 'ansible', 'prometheus', 'grafana', 'maven']
wall = Image.new('RGBA', (500, 500), (0, 0, 0, 0))
for i, n in enumerate(names): wall.alpha_composite(LG.chip(n, 140), ((i % 3) * 165, (i // 3) * 165))
src = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]]); dst = np.float32([[880, 150], [1240, 105], [1250, 560], [880, 600]])
w = cv2.warpPerspective(np.asarray(wall), cv2.getPerspectiveTransform(src, dst), (1280, 720), borderValue=(0, 0, 0, 0)); im.alpha_composite(Image.fromarray(w, 'RGBA'))
im.convert('RGB').save('/home/claude/academy/welcome/build/thumbnail.png')
# LESSON 1
im = base(); d = ImageDraw.Draw(im)
d.rounded_rectangle([50, 48, 420, 104], radius=16, fill=EN.ACC); d.text((76, 58), 'LESSON 1', font=F('x', 38), fill=INK)
d.text((50, 150), 'IDEA', font=F('x', 170), fill=EN.TXT); d.text((50, 330), 'TO', font=F('x', 110), fill=EN.MUTED); d.text((50, 440), 'CUSTOMER', font=F('x', 118), fill=EN.ACC)
d.text((54, 630), 'The 7 stages of software delivery', font=F('m', 44), fill=EN.TXT)
SCc = [EN.ACC, VIO, EN.GOOD, EN.WARN, PINK, EN.ACC, VIO]
for i in reversed(range(7)):
    b, ox, oy = iso.box(70, 70, 26 + i * 12, SCc[i]); sx = 800 + i * 62; sy = 600 - i * 42; im.alpha_composite(b, (int(sx - ox), int(sy - oy)))
pk, ox, oy = iso.box(50, 50, 44, EN.ACC, tape=(255, 246, 220)); im.alpha_composite(pk, (int(1150 - ox), int(130 - oy))); im.alpha_composite(bulb(110), (760, 190))
im.convert('RGB').save('/home/claude/academy/sdlc01/build/thumbnail.png')
