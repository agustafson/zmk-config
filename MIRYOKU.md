# Miryoku Totem for macOS — trial draft

A Miryoku-based ZMK configuration for the 38-key Totem. The urob-inspired alternative is preserved separately in `alternatives/urob/`. The purpose is to experience Miryoku's coordinated layers, mouse controls and clipboard while retaining the most important requested Mac and coding changes.

## Thumb and number-layer decisions

This trial uses Miryoku's six thumb tap/layer roles. The unused Delete tap has been changed to a second Escape. **Magic Shift and automatic Num Word are not implemented in this trial**: keeping the Miryoku thumb roles leaves no spare thumb for the former, and the Num thumb already taps Backspace. As selected for this trial, Miryoku's double-tap layer lock is available for longer numeric entry, but it is not Num Word and does not exit automatically. These choices can be revisited after trying the layout.

## Assumed hardware and Mac

The local shield assumes a wireless GEIGEIGEIST Totem with a Seeed XIAO nRF52840 on each half, left central, and original matrix/pins. You confirmed the Seeed Studio XIAO BLE/nRF52840 controller; the Totem+ matrix and pin wiring have not been independently verified, and this build has not been tested on the physical keyboard. The keyboard emits Colemak-DH directly: use the macOS U.S. or ABC input source while using it. Set your preferred source separately for the MacBook's built-in keyboard.

## Base and thumb roles

Colemak-DH letters; the modifiers use the previously preferred order, outside to inside **Ctrl, Option, Shift, Command**, mirrored between hands. The additional left pinky is Hyper (Ctrl+Option+Shift+Cmd) and the right is Meh (Ctrl+Option+Shift).

Left thumbs, outside to inside:

| Tap | Hold |
|---|---|
| Escape | Media |
| Space | Nav |
| Tab | Mouse |

Right thumbs, inside to outside:

| Tap | Hold |
|---|---|
| Enter | Sym |
| Backspace | Num |
| Escape | Fun |

In the default stock Miryoku, the right outer tap is Delete; it is Escape here. The two Escape thumb keys are deliberate duplicates for this trial. Holding a thumb typically activates the layer after the tapping term; these starting timings require physical testing.

## Coherent layer relationships

- **Nav and Mouse:** right-hand arrows and pointer movement use the same inverted-T positions. Page Up/Down are on the inner index column; vertical scrolling uses those same positions on Mouse. Clipboard keys, including Undo and Redo, occupy the right-hand bottom row on both layers. Mouse buttons are the right thumbs while Mouse is active. Media also follows the Miryoku Inverted-T arrangement.
- **Num and Fun:** F7–F9, F4–F6 and F1–F3 follow the same positions as 7–9, 4–6 and 1–3.
- **Sym:** many symbols are in the positions associated with their shifted U.S. number keys, with parentheses and underscore on the left thumbs.
- **Mac clipboard:** Undo Cmd+Z, Redo Cmd+Shift+Z, Cut Cmd+X, Copy Cmd+C and Paste Cmd+V. Nav line-start/line-end keys send Cmd+Left/Right. Behavior can differ in terminal programs and individual applications.

On Nav, the right-hand keys are arranged as follows, from the inner index column toward the pinky:

```text
PgUp   Line start   Up     Line end   Insert
PgDn   Left         Down   Right      Caps Word
Redo   Paste        Copy   Cut        Undo
```

This follows Miryoku Inverted-T, except that Page Up/Down exchange places with Insert and Caps Word. Caps Word capitalizes identifiers; it is not a Caps Lock toggle. Line start/end retain this Mac configuration's Cmd+Left/Right shortcuts. `MIRYOKU_NAV_INVERTEDT` records the selected variant; the custom layer definitions implement these preferences and the matching mouse alignment.

Holding the right Backspace thumb gives the Num layer. To lock Num for repeated input, hold Nav (left Space) and double-tap the left bottom-row middle position, labelled `Lock Num 2×` in the diagram; this invokes Miryoku's `to` layer behavior. To leave a locked layer, use its `Base 2×` action. Locking is not automatic Num Word; test cancellation before relying on it.

## Backtick and fence

- **F+P:** backtick on Base. Hold Cmd and use the chord for Cmd+backtick. The keys must arrive within 50 ms.
- **W+F+P:** Raycast fence on Base, also 50 ms. It overlaps F+P; test recognition and timing.
- **Nav:** hold left Space, then press the left inner index top key (B position) for backtick.
- **Fun:** hold the right outer thumb; the left inner index top key is backtick, the matching home key invokes the Raycast fence, and the bottom key is empty. These replace Print Screen, Scroll Lock and Pause/Break. Insert is on the Nav right pinky top key.

The fence behavior types the Raycast trigger `;;fence`; it does **not** send Enter. Import `raycast-code-fence.json` using Raycast's Import Snippets action. Expansion and multiline insertion depend on Raycast and the host application; test in a safe unsent field in each desktop/browser and terminal workflow. Without an active Raycast snippet the trigger text remains literal.

## Frequently missed symbols

- `?`: hold the left home-row `S` key for Shift, then tap the right-hand `/` key on the bottom row, beside the outer Meh key. Holding `/` instead activates the Button layer.
- `)`: hold the right inner Enter/Sym thumb, then tap the left middle Space thumb. The Space position sends `)` on the Sym layer.
- `<`, `>` and `"`: hold Shift and tap `,`, `.` and `'` respectively. The diagram and HUD now show these shifted symbols above their base keys. This assumes a macOS U.S. or ABC input source.

## Diagrams

- [Nav and Mouse side-by-side](draw/miryoku-nav-mouse.png)
- [Base](draw/miryoku-base.png)
- [All working layers](draw/miryoku-layers.png)

The diagrams are generated from `config/totem.keymap` and the included Miryoku source with keymap-drawer. Green marks the thumb held for the displayed layer. The Base diagram omits combo overlays; F+P and W+F+P are described above.

To regenerate with Python 3 and Cairo:

```sh
python3 -m venv .venv
.venv/bin/pip install -r draw/requirements.txt
.venv/bin/python draw/render.py
.venv/bin/python draw/validate.py
```

## Implementation notes

Miryoku ZMK is vendored from upstream commit `559aa4beae75cb3206ab411b7da2adb9665c6896`. Personal layer overrides live in `config/miryoku/custom_config.h`; the exact switch mapping and chord behaviors are in `config/totem.keymap`. ZMK and Zephyr are pinned in `config/west.yml`. The custom root ZMK module (`zephyr/`, `src/` and `dts/`) supplies the fence behavior.

The main alphabet, modifiers and layer mapping are intended to be understandable and editable through normal ZMK source. This is not an Oryx import. GitHub Actions is configured to build both halves, but no remote was created or workflow run. For a local west workspace, copy `config/` into a **separate** workspace before `west init -l config`; the repo's `zephyr/` folder contains the custom ZMK module.

The QWERTY Extra layer and its activation keys are removed. An unreachable `Unused` placeholder preserves the other layers' numeric IDs for the HUD; it has no typing bindings, though the two outer pinky switches still map to Hyper and Meh. The plain Colemak-DH Tap layer remains available through a guarded double tap; it removes dual-function holds and can require a keyboard reset to return to Base. Bootloader access requires a guarded double tap in this configuration.

See `VALIDATION.md` for tested and untested behavior. Original sources: https://github.com/manna-harbour/miryoku and https://github.com/manna-harbour/miryoku_zmk.
