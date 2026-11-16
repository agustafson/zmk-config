#!/usr/bin/env python3
"""Check important relationships in the keymap-drawer parse output."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
data = yaml.safe_load((root / 'draw/keymap.yaml').read_text())
layers = data['layers']
assert all(len(keys) == 38 for keys in layers.values())
assert [key['t'] if isinstance(key, dict) else key for key in layers['Base'][:10]] == ['Q', 'W', 'F', 'P', 'B', 'J', 'L', 'U', 'Y', "'"]
assert [key['t'] if isinstance(key, dict) else key for key in layers['Base'][10:20]] == list('ARSTGMNEIO')
assert [key['t'] if isinstance(key, dict) else key for key in layers['Base'][21:31]] == ['Z', 'X', 'C', 'D', 'V', 'K', 'H', ',', '.', '/']
assert [combo['p'] for combo in data['combos']] == [[2, 3], [1, 2, 3]]
assert layers['Nav'][5:10] == ['PgUp', 'Line start', 'Up', 'Line end', 'Ins']
assert layers['Nav'][15:19] == ['PgDn', 'Left', 'Down', 'Right']
assert layers['Nav'][19]['t'] == 'Caps Word'
assert layers['Nav'][4] == '`'
assert layers['Mouse'][5:9] == ['Scroll Up', 'Scroll Left', 'Mouse Up', 'Scroll Right']
assert layers['Mouse'][15:19] == ['Scroll Down', 'Mouse Left', 'Mouse Down', 'Mouse Right']
assert layers['Nav'][26:31] == layers['Mouse'][26:31] == ['Redo', 'Paste', 'Copy', 'Cut', 'Undo']
assert layers['Base'][36]['t'] == 'Bspc' and layers['Base'][37]['t'] == 'Esc'
assert layers['Fun'][4] == '`' and layers['Fun'][14] == 'Fence'
assert layers['Base'][30]['t'] == '/' and layers['Base'][30]['s'] == '?'
assert layers['Sym'][33] == ')' and layers['Num'][33]['s'] == ')'
assert 'Extra' not in layers
assert all(not key for i, key in enumerate(layers['Unused']) if i not in (20, 31))
print('PASS: layer sizes, navigation/mouse alignment, clipboard, Backspace and custom slots')
