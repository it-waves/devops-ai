"""Cursor highlight for UI recordings: a glowing ring follows the mouse, pulses when it rests, and a ripple fires on every click.
It is a real (shaped, click-through) X window, so the screen recorder captures it exactly in sync with the pointer.
usage: DISPLAY=:97 python3 cursorfx.py   (stop it with SIGTERM). The ring hides while the mouse is parked in the bottom-right corner."""
import math, os, signal, sys, time
from Xlib import X, display
from Xlib.ext import shape

S = 120                      # window size (px), the ring is always smaller
AMBER, CYAN = 0xFFB300, 0x19D3F3
d = display.Display(); scr = d.screen(); root = scr.root
cmap = scr.default_colormap
def pix(rgb): return cmap.alloc_color((rgb >> 16 & 255) * 257, (rgb >> 8 & 255) * 257, (rgb & 255) * 257).pixel
PIX = {AMBER: pix(AMBER), CYAN: pix(CYAN)}
win = root.create_window(0, 0, S, S, 0, scr.root_depth, X.InputOutput, X.CopyFromParent, background_pixel=PIX[AMBER], override_redirect=1)
try: win.shape_rectangles(shape.SO.Set, shape.SK.Input, X.Unsorted, 0, 0, [])
except Exception: pass
mask = win.create_pixmap(S, S, 1)
gc = mask.create_gc(foreground=0, background=0)
c = S // 2; cur = [None, AMBER]
def ring(ro, ri, col):
    key = (ro, ri, col)
    if cur[0] == key: return
    cur[0] = key
    gc.change(foreground=0); mask.fill_rectangle(gc, 0, 0, S, S)
    gc.change(foreground=1); mask.fill_arc(gc, c - ro, c - ro, 2 * ro, 2 * ro, 0, 360 * 64)
    gc.change(foreground=0)
    if ri > 0: mask.fill_arc(gc, c - ri, c - ri, 2 * ri, 2 * ri, 0, 360 * 64)
    win.shape_mask(shape.SO.Set, shape.SK.Bounding, 0, 0, mask)
    if cur[1] != col:
        cur[1] = col; win.change_attributes(background_pixel=PIX[col]); win.clear_area(0, 0, S, S)
def stop(*a): sys.exit(0)
signal.signal(signal.SIGTERM, stop)
shown = False; last = (-1, -1); still_since = time.time(); down_prev = False; rip = None
while True:
    q = root.query_pointer(); x, y = q.root_x, q.root_y; down = bool(q.mask & X.Button1Mask); now = time.time()
    parked = x >= 1070 and y >= 588
    if (x, y) != last: still_since = now; last = (x, y)
    if down and not down_prev: rip = now
    down_prev = down
    if parked:
        if shown: win.unmap(); shown = False
        d.flush(); time.sleep(0.02); continue
    if rip is not None and now - rip < 0.45:
        t = (now - rip) / 0.45; ro = int(20 + 38 * t); th = max(2, int(10 * (1 - t))); ring(ro, ro - th, CYAN)
    else:
        rip = None
        pulse = 0.5 + 0.5 * math.sin((now - still_since) * 6.0) if now - still_since > 0.25 else 0.0
        ro = 25 + int(5 * pulse); ring(ro, ro - 5, AMBER)
    win.configure(x=x - S // 2, y=y - S // 2, stack_mode=X.Above)
    if not shown: win.map(); shown = True
    d.flush(); time.sleep(0.016)
