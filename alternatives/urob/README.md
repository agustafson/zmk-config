# Totem Mac: Colemak-DH, home-row mods and combos

A personal ZMK configuration for a 38-key wireless Totem on macOS. It adapts urob's configuration and includes the decisions discussed for this keyboard. **This is a starting point for physical testing and timing adjustments**, not a claim that the timings are perfect for your hands.

## Before flashing

The included shield assumes the original GEIGEIGEIST Totem matrix and a **Seeed XIAO nRF52840 on each half**, with the left half as central. Check that your purchased Totem or Totem+ actually uses those controllers, wiring and bootloader; other hardware needs different firmware. The built source has not been tested on the physical keyboard.

Set the Mac input source to **U.S. or ABC** while using this firmware: Colemak-DH is implemented by the keyboard. Selecting a Colemak input source as well remaps it twice. For the built-in MacBook keyboard, choose whichever macOS input source you prefer.

## Base and thumbs

```text
 Q   W   F   P   B      J   L   U   Y   '
 A   R   S   T   G      M   N   E   I   O
 Z   X   C   D   V      K   H   ,   .   ?
     Ctrl Opt Shift Cmd   Cmd Shift Opt Ctrl

     Tab  Space/Nav  Enter/Fn    Num Word/Num  Magic/Shift  Backspace
 Extra left pinky: Hyper                 Extra right pinky: Meh
```

The home-row modifier order shown below the letters is left-to-right as seen on each hand. Hold the letter to activate its modifier; tap it for the letter. Hyper is Ctrl+Option+Shift+Cmd; Meh is Ctrl+Option+Shift. Assign Hyper to your preferred Homerow shortcut in Homerow.

- **Backspace:** right outer thumb; hold to repeat. There is no forward-Delete combo.
- **Magic Shift:** right middle thumb. Hold for Shift. Tap after a recently typed letter to repeat that letter; otherwise tap for one-shot Shift. Double-tap or Shift+tap activates Caps Word. Some timing and modifier conditions apply.
- **Space/Nav:** tap for Space, hold for navigation. Shift+Space is inherited from urob: it sends period, space, then one-shot Shift.
- **Enter/Fn:** tap Enter, hold for function and media controls.
- **Smart Num:** tap for Num Word; tap again to cancel. Hold for a momentary number pad. Double-tap selects ZMK's sticky number layer, which is distinct from Num Word.

## Most useful combos

See [COMBOS.md](COMBOS.md) for every shape and hold action. Letters denote the physical **Colemak-DH** positions and the keys must be pressed together.

| Chord | Action |
|---|---|
| F+P | Backtick; available on Base and Nav |
| W+F+P | Raycast fence trigger; Base only |
| W+F | Escape |
| L+U | `#` |
| U+Y | `*` |
| L+Y | `+` |
| H+comma / comma+period | `[` / `]`; Shift produces braces |
| Z+X | Cmd+Z (undo) |
| X+C / C+D / X+D | Cmd+C / Cmd+V / Cmd+X |

To use Cmd+[ or Cmd+], hold the left index home-row Cmd and press the bracket chord with the right hand. Most chords use a deliberately tight **18 ms** window and **150 ms** prior-idle gate. F+P and W+F+P use a **50 ms** window without the idle gate so they can be used after typing. They overlap each other and W+F Escape; test intentionally. F+P is disabled on Num, where the same positions are 8 and 9, so fast numeric entry cannot turn into a backtick.

Home-row combos are also hold-taps: holding a chord can produce the union of its home-row modifiers. S+T and R+S+T have no tap action, but retain Shift+Cmd and Shift+Option+Cmd when held. Multi-modifier transitions and the prior-idle interaction should be tested on the keyboard.

## Number and navigation layers

Num Word uses urob's auto-layer module: tap the Num Word thumb, then use the left-hand number pad. It stays active for numbers, Backspace, Delete keycodes, decimal point, comma and common arithmetic operators; modifiers are ignored. Space, Enter or another non-continuation key ends it. The positions containing digits keep sending digits until the mode exits; tap the Num Word thumb again to cancel when necessary.

```text
        7   8   9
    0   4   5   6
        1   2   3
```

On Nav, right-hand keys provide arrows, word navigation and editing; the top-row Y position sends Escape. Some arrows are hold-taps: hold Left/Right for line start/end and Up/Down for document start/end. Hold the Backspace navigation key for Option+Backspace. Application behavior may vary. The left side provides sticky modifiers and app switching. Fn provides F1–F12, media and macOS controls. Hold Num first, then Fn, for Bluetooth and system controls.

Blank positions in the diagrams are transparent and fall through. There is no dedicated symbol layer, leader key or mouse layer in this revision. The diagram footer and combo reference distinguish chords whose behavior changes on Nav.

## Raycast fenced block

Import [raycast-code-fence.json](raycast-code-fence.json) into Raycast snippets and enable the snippet. On Base, W+F+P types the keyword `;;fence`; Raycast is expected to expand it into a fenced block and position the cursor. **The firmware sends no Enter key.** The expansion method and multiline support can differ across apps and terminals: test in a safe unsent input before relying on it in AI agent windows. Without Raycast or the snippet, the literal trigger appears.

## Diagrams

- [Overview: base and combo families](draw/totem-mac-overview.png)
- [All five layers](draw/totem-mac-layers.png)
- [Individual combo cards](draw/totem-mac-combos.png)
- [Complete keymap](draw/totem-mac-keymap.png)

The SVG counterparts are in `draw/`. Diagrams are generated using [keymap-drawer](https://github.com/caksoylar/keymap-drawer) from `config/totem.keymap` and includes. To regenerate, use Python 3 and Cairo:

```sh
python3 -m venv .venv
.venv/bin/pip install -r draw/requirements.txt
.venv/bin/python draw/render.py
.venv/bin/python draw/validate.py
```

If changing combo positions, update `draw/combo-spec.json` too. The validator checks the shapes and selected mappings; it does not replace behavior tests or hardware testing.

## Build

This folder is an archived, self-contained alternative, not the root default build. The root GitHub Actions workflow builds Miryoku only. To try this alternative, copy the contents of this folder into a separate repository or workspace root, including `config/`, `build.yaml`, `zephyr/`, `src/`, `dts/`, and the remaining supporting files. Add the standard ZMK build workflow to that separate repository or use a local ZMK/Zephyr workspace and this alternative's `config/west.yml`; its custom fence module must be included as an extra ZMK module. No standalone build workflow is included in this archived folder. Rebuild and test rather than assuming the root firmware contains this layout.

This config derives from [urob/zmk-config](https://github.com/urob/zmk-config) and the [GEIGEIGEIST Totem hardware](https://github.com/GEIGEIGEIST/TOTEM). See `VALIDATION.md` for what has been checked.
