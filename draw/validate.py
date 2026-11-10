#!/usr/bin/env python3
"""Check important relationships in the keymap-drawer parse output."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
data = yaml.safe_load((root / 'draw/keymap.yaml').read_text())
layers = data['layers']
assert all(len(keys) == 38 for keys in layers.values())
assert layers['Base'][:10] == ['Q', 'W', 'F', 'P', 'B', 'J', 'L', 'U', 'Y', "'"]
assert [key['t'] if isinstance(key, dict) else key for key in layers['Base'][10:20]] == list('ARSTGMNEIO')
assert [key['t'] if isinstance(key, dict) else key for key in layers['Base'][21:31]] == ['Z', 'X', 'C', 'D', 'V', 'K', 'H', ',', '.', '/']
assert [combo['p'] for combo in data['combos']] == [[2, 3], [1, 2, 3]]
assert layers['Nav'][18] == 'Up' and layers['Nav'][29] == 'PgUp'
assert layers['Mouse'][18] == 'Mouse Up' and layers['Mouse'][29] == 'Scroll Up'
assert layers['Nav'][5] == layers['Mouse'][5] == 'Redo'
assert layers['Nav'][9] == layers['Mouse'][9] == 'Undo'
assert layers['Base'][36]['t'] == 'Bspc' and layers['Base'][37]['t'] == 'Esc'
assert layers['Fun'][4] == '`' and layers['Fun'][14] == 'Fence'
print('PASS: layer sizes, navigation/mouse alignment, clipboard, Backspace and custom slots')
