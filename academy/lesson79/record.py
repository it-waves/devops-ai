"""Record Lesson 79 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson79')
from term import *
import video as V
LD = '/home/claude/academy/lesson79'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'inspect': [('cmd', 'i0', 'cd shop'), ('cmd', 'i1', 'java -Xmx256m -Xms64m -Dserver.port=9090 -Dcurrency=EUR Server &'), ('cmd', 'i2', 'jps -l'), ('cmd', 'i3', 'pgrep -a java'), ('cmd', 'i4', 'PID=$(pgrep -f Server)'), ('cmd', 'i5', "tr '\\0' ' ' < /proc/$PID/cmdline; echo"), ('cmd', 'i6', 'jcmd $PID VM.command_line')],
 'settings': [('cmd', 's0', 'cd shop'), ('cmd', 's1', 'java -Xmx256m -Xms64m -Dserver.port=9090 -Dcurrency=EUR Server > /dev/null &'), ('cmd', 's2', "jcmd Server VM.flags | tr ' ' '\\n' | grep -E 'MaxHeapSize|InitialHeapSize|UseG1GC'"), ('cmd', 's3', "jcmd Server VM.system_properties | grep -E 'server.port|currency'"), ('cmd', 's4', "java -XX:+PrintFlagsFinal -version 2>&1 | grep MaxHeapSize | tr -s ' '"), ('cmd', 's5', 'JAVA_TOOL_OPTIONS=-Xmx100m java -version 2>&1 | head -n 1')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
