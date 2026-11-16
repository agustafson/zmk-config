#!/usr/bin/env python3
"""Render diagrams from the actual Miryoku Totem ZMK keymap."""
from pathlib import Path
from io import StringIO
import os, subprocess, sys, copy, re
import xml.etree.ElementTree as ET
import yaml
from keymap_drawer.config import Config
from keymap_drawer.draw import KeymapDrawer
import cairosvg

root=Path(__file__).resolve().parents[1]
os.chdir(root)
subprocess.run([sys.executable,'-m','keymap_drawer','-c','draw/config.yaml','parse','-z','config/totem.keymap','-o','draw/keymap.yaml'],check=True)
data=yaml.safe_load((root/'draw/keymap.yaml').read_text())
assert all(len(keys)==38 for keys in data['layers'].values())
assert [c['p'] for c in data['combos']]==[[2,3],[1,2,3]]
# keymap-drawer does not infer US-layout shifted characters from &kp or hold-taps.
# Display them explicitly, while retaining the actual tap and hold bindings.
shifted={'Base':{9:'"',28:'<',29:'>',30:'?'},
         'Num':{0:'{',1:'&',2:'*',3:'(',4:'}',10:':',11:'$',12:'%',13:'^',14:'+',
                21:'~',22:'!',23:'@',24:'#',25:'|',32:'>',33:')',34:'_'}}
for layer, keys in shifted.items():
 for pos, symbol in keys.items():
  key=data['layers'][layer][pos]
  data['layers'][layer][pos]={**(key if isinstance(key,dict) else {'t':key}),'s':symbol}
data['layout']={'qmk_info_json':'draw/totem-layout.json'}
held={'Nav':(33,'Nav'), 'Mouse':(34,'Mouse'), 'Media':(32,'Media'), 'Num':(36,'Num'), 'Sym':(35,'Sym'), 'Fun':(37,'Fun')}
for layer,(pos,name) in held.items(): data['layers'][layer][pos]={'t':name,'type':'held'}
(root/'draw/keymap.yaml').write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True))
config=yaml.safe_load((root/'draw/config.yaml').read_text())
def render(name,layers,columns=2):
 payload=copy.deepcopy(data); payload['layers']={k:payload['layers'][k] for k in layers}; payload['combos']=[]
 opts=copy.deepcopy(config);opts['draw_config']['n_columns']=columns
 buffer=StringIO(); KeymapDrawer(config=Config(**opts),out=buffer,**payload).print_board()
 doc=ET.fromstring(buffer.getvalue());ns='{http://www.w3.org/2000/svg}'
 for node in doc.iter(ns+'text'):
  classes=node.get('class','').split(); size=19 if 'label' in classes else 12 if 'footer' in classes else 10 if any(x in classes for x in ['hold','shifted']) else 14
  for span in node.iter(ns+'tspan'):
   m=re.search(r'font-size:\s*([\d.]+)%',span.get('style',''))
   if m: span.set('style',f'font-size: {size*float(m[1])/100:.2f}px')
 doc.insert(0,ET.Element(ns+'rect',{'width':'100%','height':'100%','fill':'#f4f6fa'}))
 svg=ET.tostring(doc,encoding='unicode');(root/f'draw/{name}.svg').write_text(svg)
 cairosvg.svg2png(bytestring=svg.encode(),write_to=str(root/f'draw/{name}.png'),scale=2)
render('miryoku-base',['Base'],1)
render('miryoku-nav-mouse',['Nav','Mouse'])
render('miryoku-layers',['Base','Nav','Mouse','Num','Sym','Fun','Media','Button'])
print('Rendered 38-key Miryoku diagrams from the ZMK source.')
