import json, re, sys
sys.path.insert(0, '/home/claude/academy/lesson13')
import importlib; V = importlib.import_module('video')
SENT = re.compile(r'[.?!:]$')
def times(scene):
    dur = json.load(open('/home/claude/academy/lesson13/vo/dur.json')); C = {}
    for name, cues in V.SCENES:
        if name != scene: continue
        t = 0.5
        for c in cues:
            gap = c[3] if len(c) > 3 and c[3] is not None else (0.55 if SENT.search(c[1]) else 0.13)
            C[c[0]] = t; t += dur[c[0]] + gap + V.EXTRA.get(c[0], 0)
        return C, round(t - 0.4 + 0.9, 3), cues[0][0]
