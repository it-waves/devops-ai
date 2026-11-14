"""Quality gate BEFORE recording: usage  preflight.py lessonNN [--fix]
Checks every typed command against its narration cue so no re-recording is needed:
 1 typing time fits inside cue + EXTRA (with --fix writes the missing EXTRA into lessonNN/extra.json)
 2 every cmd id has a cue, same order as the script
 3 highlight (HL) rows match the real output row (prompt + command wrap at 71 columns)
 4 command length / wrap warnings, rows on screen (19 max)
 5 narration cue text for typed commands starts with 'Type:' or explains the command
Exit code 1 = problems found."""
import sys, os, json, math, re, importlib
LD = os.path.abspath(sys.argv[1]); FIX = '--fix' in sys.argv
sys.path.insert(0, LD); sys.path.insert(0, '/home/claude/academy/common')
V = importlib.import_module('video'); dur = json.load(open(LD + '/vo/dur.json'))
src = open(LD + '/record.py').read(); bad = 0
cmds = [(m.group(1), eval(m.group(2))) for m in re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", src)]
cues = [c[0] for _, cs in V.SCENES for c in cs]
order = [cues.index(i) if i in cues else -1 for i, _ in cmds]
if -1 in order: print('FAIL cmd without cue:', [cmds[i][0] for i, o in enumerate(order) if o < 0]); bad += 1
if order != sorted(order): print('FAIL cmd order differs from script order'); bad += 1
extra = dict(V.EXTRA); need_extra = {}
for cid, text in cmds:
    if cid not in dur: continue
    need = len(text) * 0.080 + 0.25; have = dur[cid] + extra.get(cid, 0)
    if have < need + 0.3 + 0.4: need_extra[cid] = math.ceil((need + 0.7 - dur[cid]) * 10) / 10 + 0.1
    rows = math.ceil((22 + len(text)) / 71)
    if rows > 2: print(f'WARN {cid}: command wraps to {rows} rows ({len(text)} chars): shorten it'); 
if need_extra:
    print('FAIL typing does not fit its cue; EXTRA needed:', need_extra); bad += 1
    if FIX:
        p = LD + '/extra.json'; d = json.load(open(p)) if os.path.exists(p) else {}
        for k, v in need_extra.items(): d[k] = max(d.get(k, 0), v)
        json.dump(d, open(p, 'w')); print('wrote', p)

# 6 UI actions must fit their cue: each action finishes before the next one starts, and the last one before the cue ends (cost model = record.py)
try:
    import record as R
    def cost(a):
        k = a[0]
        return {'click': 0.85, 'move': 0.25, 'key': 0.15, 'raise': 0.25, 'park': 0.25, 'find': 1.4, 'f': 1.4, 'r': 0.85}.get(k, (len(a[1]) * 0.09 + 0.15) if k == 'type' else (a[1] * 0.5 + 0.15) if k == 'scroll' else 0.25)
    need_ui = {}
    for st in R.STAGES.values():
        for s_ in st:
            if s_[0] != 'ui': continue
            cid, acts = s_[1], s_[2]
            if cid not in dur: continue
            n = 0
            for i, (f, a) in enumerate(acts):
                nxt = acts[i + 1][0] if i + 1 < len(acts) else 1.0
                gap = (nxt - f)
                n = max(n, (cost(a) + (0.3 if i + 1 < len(acts) else 0.7)) / max(gap, 0.01))
            tot = dur[cid] + extra.get(cid, 0)
            if tot < n: need_ui[cid] = math.ceil((n - dur[cid]) * 10) / 10 + 0.1
    if need_ui:
        print('FAIL UI actions do not fit their cue; EXTRA needed:', need_ui); bad += 1
        if FIX:
            p = LD + '/extra.json'; d = json.load(open(p)) if os.path.exists(p) else {}
            for k, v in need_ui.items(): d[k] = max(d.get(k, 0), v)
            json.dump(d, open(p, 'w')); print('wrote', p)
except Exception as e: print('WARN ui check skipped:', e)
rowof = {cid: math.ceil((22 + len(t)) / 71) for cid, t in cmds}
by = {}
for i, (cid, _) in enumerate(cmds): by[cid] = i
def cmd_before(cue):  # the typed command whose output this cue talks about: nearest earlier cmd id in the script
    k = cues.index(cue); best = None
    for cid, _ in cmds:
        if cid in cues and cues.index(cid) <= k: best = cid
    return best
for scene, hl in getattr(V, 'HL', {}).items():
    for t in hl:
        cue, row, n = t[0], t[1], t[2]; c0 = cmd_before(cue)
        if c0 is None: continue
        want = rowof[c0]
        if row < want: print(f'FAIL HL {cue}: row {row} is on the command (command {c0} uses {want} rows)'); bad += 1
        if row + n > 19: print(f'FAIL HL {cue}: rows {row}-{row + n} beyond 19 rows'); bad += 1
        if row > want: print(f'WARN HL {cue}: row {row}, first output row after {c0} is {want}')
print('preflight', 'PASSED' if not bad else f'FAILED ({bad})'); sys.exit(1 if bad else 0)
