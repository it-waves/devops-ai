"""Live browser recording helpers: real Chrome on Xvfb :98 (1920x1080), real X mouse/keyboard via xdotool, screen captured by ffmpeg."""
import os, sys, time, json, subprocess, random
sys.path.insert(0, '/home/claude/academy/common')
from playwright.sync_api import sync_playwright
DISP = ':98'; E = dict(os.environ, DISPLAY=DISP)
CURSOR_JS = r"""
(()=>{ if(window.__cur) return; const s=document.createElement('style'); s.textContent='*{cursor:none!important}'; document.documentElement.appendChild(s);
 const c=document.createElement('div'); c.style.cssText='position:fixed;left:0;top:0;width:34px;height:34px;z-index:2147483647;pointer-events:none;transform:translate(-100px,-100px);filter:drop-shadow(0 2px 3px rgba(0,0,0,.55))';
 c.innerHTML='<svg width="34" height="34" viewBox="0 0 24 24"><path d="M3 2 L3 19 L8 14.5 L11.5 22 L14.5 20.6 L11.2 13.3 L18 13 Z" fill="#fff" stroke="#111" stroke-width="1.4" stroke-linejoin="round"/></svg>';
 document.documentElement.appendChild(c); window.__cur=c;
 addEventListener('mousemove',e=>{c.style.transform='translate('+e.clientX+'px,'+e.clientY+'px)'},true);
 addEventListener('mousedown',e=>{const r=document.createElement('div'); r.style.cssText='position:fixed;pointer-events:none;z-index:2147483646;border:4px solid #ffd24a;border-radius:50%;width:16px;height:16px;left:'+(e.clientX-8)+'px;top:'+(e.clientY-8)+'px;transition:all .45s ease-out;opacity:1'; document.documentElement.appendChild(r); requestAnimationFrame(()=>{r.style.width='64px';r.style.height='64px';r.style.left=(e.clientX-32)+'px';r.style.top=(e.clientY-32)+'px';r.style.opacity='0'}); setTimeout(()=>r.remove(),600)},true);
})();
"""
def xd(*a): subprocess.run(['xdotool', *map(str, a)], env=E)
class UI:
    def __init__(s, out=None, secs=600, rec=True):
        if subprocess.run(['pgrep', '-f', 'Xvfb ' + DISP], capture_output=True).returncode:
            subprocess.Popen(['Xvfb', DISP, '-screen', '0', '1920x1080x24'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(2)
        subprocess.run('rm -rf /tmp/ui/prof', shell=True)
        os.makedirs('/tmp/ui/prof/Default', exist_ok=True); open('/tmp/ui/prof/Default/Preferences', 'w').write(json.dumps({'credentials_enable_service': False, 'profile': {'password_manager_enabled': False}, 'autofill': {'profile_enabled': False}}))
        s.pw = sync_playwright().start()
        s.ctx = s.pw.chromium.launch_persistent_context('/tmp/ui/prof', executable_path='/usr/bin/google-chrome', headless=False, no_viewport=True,
            args=['--no-sandbox', '--kiosk', '--window-size=1920,1080', '--window-position=0,0', '--disable-infobars', '--no-first-run', '--disable-features=Translate', '--force-device-scale-factor=1', '--password-store=basic', '--disable-save-password-bubble'], env=E)
        s.ctx.add_init_script(CURSOR_JS)
        s.pg = s.ctx.pages[0]; s.x, s.y = 960, 540; s.ff = None; s.dwell = 0.0
        if rec and out: s.ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '0', '-framerate', '30', '-video_size', '1920x1080', '-i', DISP, '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', out], env=E, stdin=subprocess.PIPE)
        time.sleep(1.0); s.T0 = time.time()
    def goto(s, url):
        s.pg.goto(url); s.pg.wait_for_load_state('domcontentloaded'); s.pg.evaluate(CURSOR_JS); time.sleep(0.4); xd('mousemove', s.x, s.y); xd('mousemove', s.x + 1, s.y)
    def move(s, x, y, dur=0.7):
        n = max(8, int(dur / 0.025)); x0, y0 = s.x, s.y
        for i in range(1, n + 1):
            t = i / n; t = t * t * (3 - 2 * t); xd('mousemove', int(x0 + (x - x0) * t), int(y0 + (y - y0) * t)); time.sleep(dur / n)
        s.x, s.y = int(x), int(y)
    def box(s, sel, nth=0):
        l = s.pg.locator(sel).nth(nth); l.scroll_into_view_if_needed(); time.sleep(0.25); b = l.bounding_box(); return b
    def click(s, sel, nth=0, dx=0.5, dy=0.5, dur=0.7):
        b = s.box(sel, nth); x = b['x'] + b['width'] * dx; y = b['y'] + b['height'] * dy
        s.move(x, y, dur); time.sleep(0.2); xd('click', 1); time.sleep(0.35)
    def type(s, text, delay=55): xd('type', '--delay', delay, '--clearmodifiers', text)
    def key(s, k): xd('key', k)
    def shot(s, path): s.pg.screenshot(path=path)
    def wait(s, t): time.sleep(t)
    def close(s):
        if s.ff:
            try: s.ff.stdin.write(b'q'); s.ff.stdin.flush()
            except Exception: pass
            s.ff.wait()
        s.ctx.close(); s.pw.stop()
def _clickxy(s, x, y, dur=0.7): s.move(x, y, dur); time.sleep(0.2); xd('click', 1); time.sleep(0.4)
UI.clickxy = _clickxy
