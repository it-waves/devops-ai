"""Record the Lesson 13 practical lab. usage: lab_record.py STAGE   (stages: all | boot1 | login | walk | notes | snapvb | snaphost | boot2 | breakit | resthost | boot3 | verify)
VM runs in QEMU on Xvfb :98 (720x405); VirtualBox GUI on :99 (880x480). Clips -> lesson13/build/clip_<scene>.mp4"""
import os, sys, time, json, socket, subprocess
sys.path.insert(0, '/home/claude/academy/common')
import lab_times
B = '/home/claude/academy/lesson13/build/'; LAB = '/home/claude/lab'
dur = json.load(open('/home/claude/academy/lesson13/vo/dur.json'))
E98 = dict(os.environ, DISPLAY=':98'); E99 = dict(os.environ, DISPLAY=':99', HOME='/tmp/guihome')
QP = None
def sh(*a, env=E98, **k): return subprocess.run(list(map(str, a)), env=env, **k)
def xt(*a, env=E98): sh('xdotool', *a, env=env)
def typ(s, delay=95, env=E98): xt('type', '--delay', delay, s, env=env)
def key(k): xt('key', k)
def shot(n): sh('import', '-window', 'root', f'/tmp/gui/lab_{n}.png')
def ensure_x():
    if subprocess.run(['pgrep', '-f', 'Xvfb :98'], capture_output=True).returncode: subprocess.Popen(['Xvfb', ':98', '-screen', '0', '720x400x24'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(2)
def vm_start():
    global QP; ensure_x()
    QP = subprocess.Popen(['qemu-system-x86_64', '-m', '1024', '-smp', '2', '-cpu', 'qemu64', '-accel', 'tcg', '-kernel', LAB + '/vmlinuz', '-initrd', LAB + '/initrd.img', '-append', 'root=/dev/vda rw console=tty0 nomodeset loglevel=5 systemd.show_status=1', '-drive', f'file={LAB}/lab.qcow2,if=virtio', '-netdev', 'user,id=n0,hostfwd=tcp:127.0.0.1:2230-:22', '-device', 'virtio-net-pci,netdev=n0', '-vga', 'std', '-display', 'sdl', '-name', 'lab'], env=E98, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); fix_win()
def fix_win():
    t = time.time()
    while time.time() - t < 15:
        for w in subprocess.run(['xdotool', 'search', '--name', 'lab'], env=E98, capture_output=True, text=True).stdout.split():
            g = subprocess.run(['xdotool', 'getwindowgeometry', w], env=E98, capture_output=True, text=True).stdout
            if '720x400' in g: xt('windowmove', w, 0, 0); return
        time.sleep(0.3)
def ssh_up():
    try:
        s = socket.create_connection(('127.0.0.1', 2230), 2); s.settimeout(3); d = s.recv(8); s.close(); return d.startswith(b'SSH')
    except Exception: return False
def wait_boot(maxs=240):
    t = time.time()
    while time.time() - t < maxs:
        if ssh_up(): time.sleep(4); return time.time() - t
        time.sleep(2)
    raise SystemExit('boot timeout')
def vm_wait_off(maxs=120):
    t = time.time()
    while QP.poll() is None and time.time() - t < maxs: time.sleep(1)
    return QP.poll() is not None
def rec_start(out, secs, env=E98, size='720x400'):
    ensure_x()
    return subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '0', '-framerate', '30', '-video_size', size, '-i', env['DISPLAY'], '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '15', '-pix_fmt', 'yuv420p', out], env=env, stdin=subprocess.PIPE)
def rec_stop(p):
    try: p.stdin.write(b'q'); p.stdin.flush()
    except Exception: pass
    p.wait()
def clips():
    f = B + 'clips.json'; return json.load(open(f)) if os.path.exists(f) else {}
def save_clip(scene, **kw):
    d = clips(); d[scene] = kw; json.dump(d, open(B + 'clips.json', 'w'))
def boot_stage(scene):
    out = B + f'raw_{scene}.mp4'; ff = rec_start(out, 400); time.sleep(1.0); t0 = time.time(); vm_start(); n = wait_boot(); rec_stop(ff); save_clip(scene, mode='fit', file=out); print(scene, 'boot', round(n, 1), 's')
class Run:
    """sync recorder: clip t=0 is scene time 0 (first second trimmed by overlay)"""
    def __init__(s, scene, env=E98, size='720x400'):
        s.scene = scene; s.C, s.D, s.first = lab_times.times(scene); s.out = B + f'clip_{scene}.mp4'
        s.ff = rec_start(s.out, s.D + 6, env, size); time.sleep(1.0); s.T0 = time.time()
    def at(s, cid, off=0.0):
        t = s.T0 + s.C[cid] + off - time.time()
        if t > 0: time.sleep(t)
    def end(s):
        t = s.T0 + s.D + 0.6 - time.time()
        if t > 0: time.sleep(t)
        rec_stop(s.ff); save_clip(s.scene, mode='sync', file=s.out); print(s.scene, 'recorded', round(s.D, 1))
def focus(): xt('mousemove', 360, 200); xt('click', 1)
def login(r, cu, cp, uoff, poff):
    r.at(cu, uoff); typ('student'); key('Return'); r.at(cp, poff); typ('student', 110); key('Return')
def stage_login():
    r = Run('login'); focus(); d = dur
    r.at('l1', d['l1'] - 2.6); typ('student'); key('Return')
    r.at('l2', d['l2'] - 4.6); typ('student', 110); key('Return')
    r.at('l4', d['l4'] - 2.0); typ('whoami'); key('Return')
    r.at('l5', d['l5'] - 1.4); typ('hostname'); key('Return'); r.end()
def stage_walk():
    r = Run('walk'); d = dur; key('ctrl+l'); focus()
    r.at('k1', d['k1'] - 2.8); typ('pwd'); key('Return')
    r.at('k2', d['k2'] - 3.6); typ('ls'); key('Return')
    r.at('k3', 0.2); key('ctrl+l'); r.at('k3', d['k3'] - 5.2); typ('ls /'); key('Return')
    r.at('k4', 0.2); key('ctrl+l'); r.at('k4', d['k4'] - 2.4); typ('head -n 3 /etc/os-release'); key('Return')
    r.at('k5', 0.2); key('ctrl+l'); r.at('k5', d['k5'] - 1.5); typ('ip -br a'); key('Return')
    r.at('k6', 0.2); key('ctrl+l'); r.at('k6', d['k6'] - 1.8); typ('df -h /'); key('Return'); r.end()
def stage_notes():
    r = Run('notes'); d = dur; key('ctrl+l'); focus()
    r.at('n1', d['n1'] - 6.8); typ('echo "my first lab note" > notes.txt', 100); key('Return')
    r.at('n2', d['n2'] - 1.6); typ('cat notes.txt'); key('Return')
    r.at('n3', d['n3'] - 5.0); typ('sudo poweroff'); key('Return'); time.sleep(2.6); typ('student', 110); key('Return')
    r.end(); print('off', vm_wait_off())
def xterm():
    p = subprocess.Popen(['xterm', '-geometry', '88x24+0+0', '-fa', 'DejaVu Sans Mono', '-fs', '13', '-bg', 'black', '-fg', 'white', '-xrm', 'XTerm*borderWidth:6', '-e', 'bash', '--norc', '-c', f'cd {LAB}; PS1="host$ " exec bash --norc'], env=E98); time.sleep(2.5); return p
def stage_snaphost():
    p = xterm(); r = Run('snaphost'); xt('mousemove', 360, 200); xt('click', 1); d = dur
    r.at('sh1', d['sh1'] - 4.8); typ('qemu-img snapshot -c clean-install lab.qcow2', 85); key('Return')
    r.at('sh1', d['sh1'] + 3.2); typ('qemu-img snapshot -l lab.qcow2', 85); key('Return'); r.end(); p.terminate()
def stage_resthost():
    p = xterm(); r = Run('resthost'); xt('mousemove', 360, 200); xt('click', 1); d = dur
    r.at('rh1', d['rh1'] - 4.5); typ('qemu-img snapshot -a clean-install lab.qcow2', 85); key('Return')
    r.at('rh1', d['rh1'] + 4.0); typ('qemu-img snapshot -l lab.qcow2', 85); key('Return'); r.end(); p.terminate()
def stage_breakit():
    r = Run('breakit'); d = dur; focus()
    r.at('q1', 1.0); typ('student'); key('Return'); r.at('q1', 3.4); typ('student', 110); key('Return')
    r.at('q3', 0.4); typ('sudo rm -rf /etc/ssh', 100); key('Return'); time.sleep(2.2); typ('student', 110); key('Return')
    r.at('q4', d['q4'] - 3.2); typ('ls /etc/ssh'); key('Return')
    r.at('q5', d['q5'] - 2.0); typ('sudo poweroff'); key('Return'); r.end(); print('off', vm_wait_off())
def stage_verify():
    r = Run('verify'); d = dur; focus()
    r.at('vf1', 0.6); typ('student'); key('Return'); r.at('vf1', 3.0); typ('student', 110); key('Return')
    r.at('vf1', 5.5); typ('ls /etc/ssh'); key('Return')
    r.at('vf2', d['vf2'] - 1.8); typ('cat notes.txt'); key('Return'); r.end()
def stage_snapvb(): raise SystemExit('snapvb handled separately')
if __name__ == '__main__':
    st = sys.argv[1]
    order = ['boot1', 'login', 'walk', 'notes', 'snaphost', 'boot2', 'breakit', 'resthost', 'boot3', 'verify']
    for s in (order if st == 'all' else [st]):
        print('==', s, flush=True)
        if s == 'boot1': boot_stage('bootvm')
        elif s == 'boot2': boot_stage('boot2')
        elif s == 'boot3': boot_stage('boot3')
        else: globals()['stage_' + s]()
