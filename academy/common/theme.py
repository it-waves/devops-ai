"""Academy theme: deep indigo ink + amber / mint / coral. Different from the RHCSA navy+cyan look."""
import sys; sys.path.insert(0, '/home/claude/osi')
import engine as E
E.BG0 = (11, 33, 38); E.BG1 = (5, 16, 21)
E.PANEL = (19, 46, 53); E.EDGE = (54, 94, 104)
E.TXT = (240, 247, 246); E.MUTED = (146, 178, 180); E.DIM = (92, 124, 130)
E.ACC = (240, 200, 120); E.GOOD = (110, 214, 188); E.BAD = (240, 120, 130); E.WARN = (244, 170, 132)
E.TERM_BG = (8, 22, 26); E.TERM_BAR = (20, 46, 52); E.OUT = (208, 226, 222)
E.rrect.__defaults__ = (18, E.PANEL, E.EDGE, 2)
E.icon.__defaults__ = (E.TXT, E.ACC)
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
def backdrop():
    W, H = E.W, E.H
    g = np.linspace(0, 1, H)[:, None]
    arr = (np.array(E.BG0)[None, None, :] * (1 - g[..., None]) + np.array(E.BG1)[None, None, :] * g[..., None])
    im = Image.fromarray(np.repeat(arr, W, axis=1).astype(np.uint8), 'RGB').convert('RGBA')
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(glow)
    d.ellipse([W - 700, -300, W + 300, 500], fill=(110, 214, 188, 30)); d.ellipse([-400, H - 420, 600, H + 380], fill=(140, 164, 240, 34))
    glow = glow.filter(ImageFilter.GaussianBlur(120)); im.alpha_composite(glow)
    return im
