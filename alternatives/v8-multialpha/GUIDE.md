# Totem 38: four layouts, Advantage-inspired thumbs (revision 8)

This ZMK firmware provides Colemak, matrix Colemak-DH, Graphite and your Gallium variant on one shared 38-key chassis. This revision starts in standard Colemak and adds a left-hand number pad on NAV, plus a matching double-tap Num Word mode. F+P sends backtick; W+F+P triggers the optional Raycast fenced-block snippet; L+U sends Backspace; the far-left pinky is Hyper. Escape remains on the left thumb. The optional Raycast snippet trigger sends no Enter key. The left and right halves each have 15 finger keys, one outer pinky key beside the bottom row, and three thumb keys.

**Confirm the hardware before flashing:** this targets the original [Totem shield wiring](https://github.com/GEIGEIGEIST/zmk-config-totem), Seeed XIAO nRF52840 / XIAO BLE controllers and ZMK's `xiao_ble/nrf52840/zmk` board, with split Bluetooth. A seller calling a 38-key keyboard “Totem+” does not confirm its controller, bootloader or wiring. Ask the seller for their controller model and ZMK source; compare their shield overlays and matrix transform with `config/boards/shields/totem/`. Don't flash if they differ until the config is adapted. This firmware is not for an RP2040 or nice!nano without adaptation.

## Thumbs and modifiers

On each diagram below, the bottom line is the six thumbs in physical left-to-right order:

```text
        Left thumb keys          Right thumb keys
    Esc  Backspace   SYM       NAV   Enter   Space
```

The outer left pinky key is Hyper (Cmd+Ctrl+Option+Shift), a held modifier that you can use to invoke a Homerow shortcut. It remains Hyper on NAV; on the system layer it sends Tab. The outer right pinky key is apostrophe. All four alphabet layouts have the same thumb and modifier positions. Each home-row modifier sends the letter when tapped; hold it for the modifier:

```text
              Left hand                  Right hand
          Ctrl Opt Cmd Shift         Shift Cmd Opt Ctrl
          pinky ────── index         index ────── pinky
```

`Cmd` is on the middle finger, nearer the index finger than before. Home-row mods use ZMK `balanced` with a 230 ms tapping term and 175 ms quick-tap term, and positional hold triggers on the opposite hand. Same-hand shortcuts can require a deliberate hold beyond the tapping term. These settings are a starting point to tune after trying the board. See [ZMK hold-tap](https://zmk.dev/docs/keymaps/behaviors/hold-tap).

Set macOS **System Settings → Keyboard → Text Input → Input Sources** to **U.S.** while using this firmware: the keyboard itself sends the selected layout. Selecting Colemak on macOS as well would remap it a second time. The MacBook's built-in keyboard will use the current macOS input source when the Totem is disconnected.

## Homerow

In Homerow settings, configure the desired activation shortcut. The far-left pinky sends all four Hyper modifiers together, without a tap/hold delay or a character. Homerow supports modifier-only shortcuts as well as shortcuts using an additional key; test the binding on the actual Mac and check for conflicts with other apps. Hyper is present on the base, SYM, NAV and Num Word layers; its position is Tab on the system layer. [Homerow changelog](https://homerow.app/changelog).

## Switch between the four layouts

Colemak is the power-on default. Hold **SYM + NAV** together, then press one of the left-hand top-row keys, from pinky toward index:

```text
        Colemak   Colemak-DH   Graphite   Gallium
```

Release the layer thumbs. Your choice remains until you choose another or restart; it returns to Colemak after a restart. ZMK layers are identified in the source as 0–3 for alphabets, 4 for Num Word, 5 for SYM, 6 for NAV and 7 for system settings.

## Alphabets

Hyper and the apostrophe at the edges are the separate outer pinky keys. In standard Colemak, F+P sends backtick; on every layout there is also a backtick on SYM. The home-row modifier order is shown once above and applies in every diagram. Every thumb row is `Esc  Backspace  SYM | NAV  Enter  Space`.

### Graphite

```text
      B  L  D  W  Z      '  F  O  U  J
      N  R  T  S  G      Y  H  A  E  I
Hyper Q  X  M  C  V      K  P  .  ,  /   '
```

The letters match [Graphite](https://github.com/rdavison/graphite-layout); punctuation is adapted to fit this board. Comma occupies the original bottom-row minus position, and minus is on SYM. The right outer apostrophe duplicates the upper-row apostrophe.

### Gallium (your supplied variant)

```text
      B  L  D  C  V      J  Y  O  U  ,
      N  R  T  S  G      P  H  A  E  I
Hyper X  Q  M  W  Z      K  F  '  ;  .   '
```

This follows the 30 positions in your supplied Gallium block. The Voyager-specific custom top-row shifted pairs do not fit this chassis; its symbols are on SYM.

### Colemak (startup)

```text
      Q  W  F  P  G      J  L  U  Y  ;
      A  R  S  T  D      H  N  E  I  O
Hyper Z  X  C  V  B      K  M  ,  .  /   '
```

### Colemak-DH (matrix/column-staggered form)

```text
      Q  W  F  P  B      J  L  U  Y  ;
      A  R  S  T  G      M  N  E  I  O
Hyper Z  X  C  D  V      K  H  ,  .  /   '
```

## New top-row combos on Colemak

The new combos apply only on the **standard Colemak base layer**. The keys refer to their physical positions on that layer.

| Chord | Result |
| --- | --- |
| F + P | Backtick |
| W + F + P | Sends `;;fence` for the optional Raycast fenced-block snippet |
| L + U | Backspace |
| Cmd + F + P | Cmd+backtick (macOS window cycling in supported apps) |

Press the chord keys within **50 ms** of each other. Since F+P is also part of W+F+P, the shorter chord can wait for the key release or for the 50 ms window to expire while ZMK distinguishes them. The new chords do not require a pause after typing. This makes Backspace immediate, but L followed quickly by U can unintentionally trigger Backspace during normal typing, including words such as `value` or `include`, if both keys overlap within 50 ms. Test this in a scratch field; a prior-idle guard can reduce misfires at the cost of needing a pause before the shortcut. The left thumb still sends Escape. The left pinky now sends Hyper instead of backtick. Cmd+F+P sends normal Cmd+backtick when the Command modifier has resolved; this no longer triggers the Raycast snippet.

**Home-row Command timing:** when using the left S/Command key with F+P on the same hand, first hold Command long enough to resolve (about 230 ms). A faster roll was previously simulated as `s` followed by backtick; test your own shortcuts in a scratch field. W+F+P does not need Command.

The shortcut emits no Enter. The optional Raycast snippet expands it into a multiline block, and the receiving application controls how that insertion behaves; test in a disposable draft in each agent or terminal before relying on it.

## Editing combos on Colemak

Press both keys close together while on the **standard Colemak base**. They send the normal macOS shortcuts:

| Keys | Action | Sent to macOS |
| --- | --- | --- |
| Z + X | Undo | Cmd+Z |
| X + C | Copy | Cmd+C |
| C + V | Paste | Cmd+V |

Combos use physical positions and are deliberately limited to standard Colemak: the same positions are different letters in the other three layouts. Start the combo after a short pause in typing: the key presses must arrive within **40 ms**, and a previous non-modifier key within **100 ms** prevents the combo. This helps protect normal rolls such as `xc` in `exception`, but rapid repeated editing combos immediately after typing may need a brief pause. Tune based on real use; the thresholds do not guarantee that accidental triggers are impossible. Backspace, normal single letters and the home-row modifiers remain available. See [ZMK combos](https://zmk.dev/docs/keymaps/combos).

## SYM: hold the inner left thumb

```text
       1    2    3    4    5          6    7    8    9    0
       _    {    }    [    ]          :    (    )    <    >
Hyper  ;    \    |    `    "          +    -    =    *    /    '
        Shift Backspace SYM      NAV Enter Shift
```

In standard Colemak, F+P sends backtick; all layouts also have backtick on SYM under the left index finger, the fourth key in the left 3×5 bottom row. Escape is the left outer thumb. When SYM is held, both outer thumbs become Shift; for example, hold the right outer thumb while tapping a number to produce its usual shifted symbol. This temporarily replaces Space, so release SYM for Space. Backspace and Enter remain available. Symbols assume the U.S. input source and normal shift semantics. SYM activates as you hold it. Double-tapping it activates the separate Num Word number pad described below.

## NAV: hold the inner right thumb

```text
Left hand: number pad                 Right hand: navigation

   =    7       8        9      +        PgUp  Home  Up    End   PgDn
 Ctrl   4/Opt   5/Cmd    6/Shift 0       Opt←  Left  Down  Right Opt→
Hyper   -       1        2       3   .    Del   Home  End   PgUp  PgDn   '
          Esc   Backspace  SYM          NAV    Enter   Tab
```

`4/Opt` means tap the key for `4`, hold it for Option; `5/Cmd` and `6/Shift` work likewise. On the NAV layer, the left home-row letters are replaced by digits, but the modifiers remain where your fingers expect them. Hold Shift and press an arrow to select; hold Cmd and press Left/Right in many Mac editors to move to the line start/end. The leftmost home key retains A on tap and Ctrl on hold.

Hold NAV and tap the Space thumb to send Tab. When NAV is held, this thumb sends Tab rather than Space; release NAV for Space. Function keys F1–F12 are on the system layer (SYM+NAV), on the right-hand finger keys.

The right-hand `Opt←` and `Opt→` send Option+arrow for macOS word movement. Home and End send actual Home and End keycodes; many macOS apps interpret those as document scrolling. Editors often use Cmd+Left/Right for line start/end and Cmd+Up/Down for document start/end.

## Num Word: double-tap SYM

Double-tap the left inner SYM thumb within 200 ms to activate a numbers-only layer. The left-hand number pad and operators use the **same positions as NAV**. The rest of the keys fall through to the base layer; home-row 4, 5 and 6 still hold Option, Cmd and Shift. F+P, W+F+P and other base-only combos are inactive while Num Word is active.

- Type digits, decimal point, `+`, `-`, `=`, slash or comma and Num Word remains active. Backspace, Delete and modifiers also keep it active.
- Press Space or Enter, or another non-continuation key, to exit automatically. With Num Word active, Space is the normal right thumb unless NAV is also held.
- Double-tap SYM again while Num Word is active to cancel manually. If it already exited automatically, double-tapping activates it again.
- Holding SYM temporarily gives the regular symbols layer; SYM+NAV still accesses system settings. Double-tapping SYM is different from holding it.
- Selecting an alphabet on the system layer also cancels Num Word.

**Watch the mode:** number-pad positions will continue to send digits even if you intend the underlying letter. For example, after `123`, the Colemak S position sends `5` until Num Word ends. Use Space, Enter, another key outside the pad, or the double-tap cancel before returning to such letters. The terminating key sends whatever its current binding resolves to; symbol and editing behavior can differ while a higher-priority layer is held.

Num Word uses the [ZMK Auto Layer module](https://github.com/urob/zmk-auto-layer), pinned in `config/west.yml`. Its configured continuation list includes decimal point, comma, arithmetic operators, Backspace, Delete and modifiers. Test the tap timing and reliable exit on your hardware.

## System settings: hold SYM + NAV

Function keys, layout selection, Caps Word and Bluetooth settings share this system layer. Hold both layer thumbs to access it.

```text
       Cole  C-DH  Graph   Gall   —        F1   F2    F3   F4   F5
       Ctrl  Opt   Cmd     Shift  CapsWord F6   F7    F8   F9   F10
Tab    BT1   BT2   BT3     BT4    BT5      F11  F12   —    —    —    Del
              Esc Backspace SYM       NAV Enter Tab
```

The first four top-row keys select the alphabet. BT1–BT5 select Bluetooth profiles; an empty profile can be paired as a new device. Caps Word helps type `SCREAMING_CASE`. The left modifiers on this layer are ordinary held keys. There is no Bluetooth-clear key. When both layers are held, the right outer thumb inherits Tab from NAV; Escape remains on the left outer thumb.

## W + F + P: Raycast snippet

This version sends **no Enter or Cmd+Enter** when you press W+F+P. Instead, the firmware types the literal trigger `;;fence`, without its held Command or Shift modifiers. Raycast can then expand that trigger into a multi-line snippet containing opening and closing fences with the cursor on the blank line between them:

````text
```
{cursor}
```
````

The `{cursor}` placeholder is interpreted by Raycast; it is not intended to appear in the resulting text. If Raycast isn't running, the snippet isn't imported, expansion is disabled, or the target app blocks expansion, the fallback is the literal `;;fence` text: the **keyboard itself does not send Enter**. As with any paste or text-injection tool, the receiving app controls how inserted content and cursor placement behave; no keyboard firmware can guarantee that every terminal, agent or app treats injected newlines safely. Validate each actual agent and terminal in a disposable chat or test session before relying on it. In a terminal, use the agent's composer, not a shell prompt where pasted text might be interpreted as commands. Some terminal or app settings may interfere with expansion or cursor movement.

### Install the snippet

1. Open Raycast and run **Import Snippets**. Select `raycast-code-fence.json` supplied with this configuration and confirm the import. It contains one snippet, **Markdown fenced code block**.
2. In Raycast **Settings → Snippets**, enable snippet expansion. This trigger contains no delimiter or Return, so set **Expansion Mode → Immediately** for automatic expansion. This is a global Raycast setting and may also change how your other snippets expand; review it before changing it. Raycast may need accessibility permissions, and some apps may be excluded in Snippets settings.
3. First test in a scratch text editor. Then test in a disposable draft in each browser/desktop chat and each actual terminal agent you use. Confirm that the result is three backticks, a blank line with the cursor, and three closing backticks, and that nothing is submitted. Check that the agent accepts multi-line paste and that the cursor is in the correct place. Do not test with an important unsent prompt.

The trigger is `;;fence`; the Raycast snippet's text is three backticks, a newline, `{cursor}`, a newline and three backticks. See [Raycast Snippets](https://manual.raycast.com/snippets) and [dynamic placeholders](https://manual.raycast.com/dynamic-placeholders). Raycast is a host-side dependency for the full block; this cannot be provided by the firmware alone without emitting application-dependent newline input.

This firmware masks any held modifiers briefly while sending the trigger and queues its keystrokes over roughly 140 ms; wait for expansion to finish before typing more. Source: `src/behavior_fence.c`.

## Build, flash and test

Both firmware halves were compiled with the pinned ZMK revision and `xiao_ble/nrf52840/zmk` board, together with the pinned ZMK Auto Layer module. This is a ZMK source package, not an Oryx import. The repository root includes a small ZMK module (`zephyr/`, `src/`, and `dts/`) for the shortcut and safe alphabet switching, plus `config/`, `build.yaml`, and `.github/workflows/build.yml`.

1. Confirm the seller's exact controller, PCB wiring, bootloader and recovery procedure. Keep their original firmware handy.
2. If using the prebuilt UF2 files supplied alongside this archive, match **left** to the left half and **right** to the right half. Do not flash an unverified clone.
3. To change the configuration and rebuild, put the contents of this folder at the root of a new GitHub repository, including hidden `.github`; push it and run **Actions → Build firmware**. Download the build artifact, then extract the left and right UF2 files. The workflow loads this repository's ZMK module and fetches the pinned Auto Layer module declared in the manifest.
4. Enter each controller's UF2 bootloader as specified by the seller and copy the matching UF2 to the USB drive that appears. Repeat for the other half. Pair from macOS Bluetooth settings, selecting an empty BT profile first if needed. The left half is the central half in the original Totem configuration.
5. Test every switch and layer, Hyper, F+P, W+F+P, L+U, NAV digits, modifiers with arrows, Num Word activation and exit, SYM+NAV F-keys, the snippet shortcut in a safe field, and both halves' wireless operation before relying on it for work.

Compiling and simulated key events do not verify a third-party clone's electrical compatibility, physical layout, Bluetooth operation or how the modifier timing feels. Source documentation: [ZMK builds](https://zmk.dev/docs/user-setup), [flashing](https://zmk.dev/docs/user-setup#installing-the-firmware), and [conditional layers](https://zmk.dev/docs/keymaps/conditional-layers).
