#!/usr/bin/env python3
"""Parse the actual ZMK files, then render offline Totem diagrams with keymap-drawer."""
from pathlib import Path
from io import StringIO
import copy, json, os, subprocess, sys, re
import xml.etree.ElementTree as ET
import yaml
from keymap_drawer.config import Config
from keymap_drawer.draw import KeymapDrawer
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
DRAW = ROOT / 'draw'

subprocess.run([sys.executable, '-m', 'keymap_drawer', '-c', 'draw/config.yaml',
                'parse', '-z', 'config/totem.keymap', '-o', 'draw/keymap.yaml'], check=True)
data = yaml.safe_load((DRAW/'keymap.yaml').read_text())
data['layout'] = {'qmk_info_json': 'draw/totem-layout.json'}
# Custom hold-taps have explicit labels in the parser config; annotate their
# activation positions because raw labels hide this information from the parser.
for name, held in {'Nav':{33:'Nav'}, 'Fn':{34:'Fn'}, 'Num':{35:'Num'}, 'Sys':{34:'Fn',35:'Num'}}.items():
    for position, label in held.items():
        data['layers'][name][position] = {'t':label,'type':'held'}
(DRAW/'keymap.yaml').write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
cfgdata = yaml.safe_load((DRAW/'config.yaml').read_text())

def render(filename, payload, columns=1, separate=False):
    cfg = copy.deepcopy(cfgdata)
    cfg['draw_config'].update(n_columns=columns, separate_combo_diagrams=separate)
    stream = StringIO()
    drawer = KeymapDrawer(config=Config(**cfg), out=stream, **payload)
    drawer.print_board()
    svg = stream.getvalue()
    # Resolve relative tspan font sizes explicitly. CairoSVG's percentage-font
    # handling differs from browser rendering; fixed sizes keep both identical.
    ns = '{http://www.w3.org/2000/svg}'
    doc = ET.fromstring(svg)
    for node in doc.iter(ns+'text'):
        classes = node.get('class','').split()
        size = 14
        if 'label' in classes: size = 19
        elif 'footer' in classes: size = 12
        elif 'combo' in classes: size = 8 if any(x in classes for x in ['hold','shifted']) else 13
        elif any(x in classes for x in ['hold','shifted']): size = 10
        for span in node.iter(ns+'tspan'):
            style = span.get('style','')
            m = re.search(r'font-size:\s*([\d.]+)%',style)
            if m: span.set('style', f'font-size: {size*float(m[1])/100:.2f}px')
    bg = ET.Element(ns+'rect', {'width':'100%','height':'100%','fill':'#f4f6fa'})
    doc.insert(0,bg)
    svg = ET.tostring(doc,encoding='unicode')
    (DRAW/f'{filename}.svg').write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(DRAW/f'{filename}.png'), scale=1.75)
    return svg

layers = copy.deepcopy(data)
layers['combos'] = []
render('totem-mac-layers', layers, columns=2)
base = copy.deepcopy(layers)
base['layers'] = {'Base': layers['layers']['Base']}
render('totem-mac-base', base)

# Separate diagrams make every overlapping pair/triple unambiguous. The cards
# show the actual 38-key layout with exactly the triggering positions highlighted.
cards = copy.deepcopy(data)
cards['layers'] = {'Base': layers['layers']['Base']}
for combo in cards['combos']:
    combo['draw_separate'] = True
    combo['l'] = ['Base']
render('totem-mac-combos', cards, columns=2, separate=True)

# A compact overview in urob's style: an uncluttered base plus each shape family
# in its own panel. All panel memberships are derived from parsed key positions.
overview = copy.deepcopy(layers)
overview['layers'] = {'Base': layers['layers']['Base']}
overview['combos'] = []
families = [
    ('Adjacent index + middle', lambda labels: set(k[-1] for k in labels) == {'1','2'}),
    ('Adjacent middle + ring', lambda labels: set(k[-1] for k in labels) == {'2','3'}),
    ('Skip middle: index + ring', lambda labels: set(k[-1] for k in labels) == {'1','3'}),
    ('Three fingers: index + middle + ring', lambda labels: len(labels) == 3),
    ('Adjacent ring + pinky', lambda labels: set(k[-1] for k in labels) == {'3','4'}),
]
spec = json.loads((DRAW/'combo-spec.json').read_text())
parsed_by_pos = {tuple(sorted(c['p'])): c for c in data['combos'] if not c.get('hidden')}
for title, accepts in families:
    overview['layers'][title] = [dict(t=k.get('t', '') if isinstance(k,dict) else str(k), type='ghost') for k in layers['layers']['Base']]
    for entry in spec:
        if not accepts(entry['labels']): continue
        combo = copy.deepcopy(parsed_by_pos[tuple(sorted(entry['positions']))])
        combo.update(l=[title], a='top', o=0.2, draw_separate=False)
        if isinstance(combo['k'],dict):
            key = combo['k']
            combo['k'] = {'t': key.get('t') or (key.get('h', '') + ' hold')}
        overview['combos'].append(combo)
render('totem-mac-overview', overview, columns=2)
complete = copy.deepcopy(layers)
complete['layers'].update({n: k for n,k in overview['layers'].items() if n != 'Base'})
complete['combos'] = overview['combos']
render('totem-mac-keymap', complete, columns=2)
print('Rendered Base, five layers, combo cards, and the compact overview.')
