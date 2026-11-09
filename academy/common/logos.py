"""Real brand logos (Simple Icons, CC0 SVG paths) rendered on a clean white chip so every logo stays legible.
Logos are shown only to identify the tool being taught (nominative use); no endorsement is implied."""
import json, subprocess, io, re
from PIL import Image, ImageDraw
IDX = json.load(open('/home/claude/academy/common/logos/index.json'))
_c = {}
def raw(name, px, color=None):
    k = (name, px, color)
    if k in _c: return _c[k]
    d = IDX[name]; col = color or '#' + d['hex']
    if col.lower() in ('#000000', '#181717', '#000'): col = '#' + d['hex']
    svg = d['svg'].replace('<svg ', f'<svg fill="{col}" ', 1)
    png = subprocess.run(['rsvg-convert', '-w', str(px), '-h', str(px), '-a'], input=svg.encode(), capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(png)).convert('RGBA'); _c[k] = im; return im
def chip(name, size=120, label=None, F=None, ring=None):
    """white rounded chip with the real logo centred; optional label below."""
    S = 3; w = size * S; im = Image.new('RGBA', (w, w), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    bg = (250, 252, 252, 255)
    hx = IDX[name]['hex']; lum = (0.299 * int(hx[0:2], 16) + 0.587 * int(hx[2:4], 16) + 0.114 * int(hx[4:6], 16)) / 255
    if lum > 0.62: bg = (22, 36, 42, 255)
    d.rounded_rectangle([0, 0, w - 1, w - 1], radius=int(w * 0.22), fill=bg, outline=ring, width=4 * S if ring else 0)
    lg = raw(name, int(w * 0.62)); im.alpha_composite(lg, ((w - lg.width) // 2, (w - lg.height) // 2))
    im = im.resize((size, size), Image.LANCZOS)
    if not label: return im
    from engine import text_img, TXT
    t = text_img(label, F, TXT, None, 1.1, 'center'); out = Image.new('RGBA', (max(size, t.width), size + 8 + t.height), (0, 0, 0, 0))
    out.alpha_composite(im, ((out.width - size) // 2, 0)); out.alpha_composite(t, ((out.width - t.width) // 2, size + 8)); return out
