import json, os, sys
import soundfile as sf
sys.path.insert(0, '/home/claude/academy/sdlc01')
from script_sdlc01 import SCENES
VO = '/home/claude/academy/sdlc01/vo'
PRON = json.load(open('/home/claude/academy/pronunciation.json'))
from kokoro_onnx import Kokoro
k = Kokoro('/home/claude/tts/kokoro-v1.0.onnx', '/home/claude/tts/voices-v1.0.bin')
dur = {}
for scene, cues in SCENES:
    for cid, text, say in cues:
        p = f'{VO}/{cid}.wav'
        s, sr = k.create(say or text, voice='am_eric', speed=0.97, lang='en-us')
        sf.write(p, s, sr); dur[cid] = sf.info(p).duration
json.dump(dur, open(VO + '/dur.json', 'w'), indent=1)
print(round(sum(dur.values()), 1), 'seconds of speech')
