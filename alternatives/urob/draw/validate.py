#!/usr/bin/env python3
"""Check the actual parsed mapping against the agreed Totem design. Run after render.py."""
from pathlib import Path
import json, re, yaml

ROOT = Path(__file__).resolve().parents[1]
data = yaml.safe_load((ROOT/'draw/keymap.yaml').read_text())
spec = json.loads((ROOT/'draw/combo-spec.json').read_text())
assert list(data['layers']) == ['Base','Nav','Fn','Num','Sys']
assert all(len(keys)==38 for keys in data['layers'].values())
visible = [c for c in data['combos'] if not c.get('hidden')]
assert len(data['combos'])==33 and len(visible)==29
actual = {tuple(sorted(c['p'])) for c in visible}
assert len(actual)==29
assert actual=={tuple(sorted(s['positions'])) for s in spec}
for s in spec:
    assert len({k[:2] for k in s['labels']})==1, ('vertical/cross-hand chord',s)
    columns={int(k[-1]) for k in s['labels']}
    assert columns in [{1,2},{2,3},{1,3},{1,2,3},{3,4}], ('unapproved finger shape',s)
    assert bool(s['hold']) == all(k[1]=='M' for k in s['labels'])
assert sum(bool(s['hold']) for s in spec)==10
base=data['layers']['Base']
for pos,letter,mod in [(10,'A','Ctrl'),(11,'R','Opt'),(12,'S','Shift'),(13,'T','Cmd'),
                       (16,'N','Cmd'),(17,'E','Shift'),(18,'I','Opt'),(19,'O','Ctrl')]:
    assert base[pos]['t']==letter and base[pos]['h']==mod,(pos,base[pos])
assert base[20]['t']=='Hyper' and base[31]['t']=='Meh'
assert base[32]=='Tab' and base[37]=='Bspc'
for c in visible:
    if c['k'] in ['Cut','Copy','Paste']:
        assert set(c['p']).issubset({22,23,24})
combos=(ROOT/'config/combos.dtsi').read_text()
for text in ['&kp LG(X)','&kp LG(C)','&kp LG(V)']: assert text in combos
assert re.search(r'COMBO_TERM_FAST\s+18',combos)
assert re.search(r'COMBO_IDLE_FAST\s+150',combos)
assert any(c['p']==[2,3] and c['k']=='`' for c in visible)
assert any(c['p']==[1,2,3] and c['k']=='Fence' for c in visible)
print('PASS: five 38-key layers; 29 unique horizontal chords; 10 combined modifier holds; Mac HRMs; Hyper/Meh; clipboard; fence.')
