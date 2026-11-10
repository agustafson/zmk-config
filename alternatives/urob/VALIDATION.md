# Validation

Checked locally on 10 November 2026 with ZMK `4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85`, Zephyr `10ba6d0cb38bc3d258775d27982f707599320085`, and the module revisions in `config/west.yml`.

## Passed

- Full firmware compilation and linking for `xiao_ble/nrf52840/zmk` with `totem_left` and `totem_right`. Both UF2 outputs were generated.
- Eight ZMK native-simulator scenarios against this actual 38-key keymap. Keycode events were inspected for: F+P backtick, W+F+P typing `;;fence` with no Enter, left Cmd plus the right `[` chord, `#`, magic-thumb letter repeat, Num Word followed by Space and a letter, Num Word manual cancellation, and simultaneous 8/9 while Num Word is active.
- keymap-drawer 0.23.0 parsed the source and generated the diagrams. `draw/validate.py` checked five 38-key layers, 29 unique chord shapes, 10 home-row combo hold definitions and selected physical bindings.

The simulator fixtures are in `tests/`; each starts with a dummy Q and a pause to establish prior-idle timing. The fixtures use a four-row mock matrix, not actual GPIO or Bluetooth.

## Not yet validated

- Controller model, wiring, bootloader or compatibility with the purchased Totem/Totem+ unit.
- Flashing, wireless pairing, timing and physical comfort, rollover, actual Homerow bindings or typing in macOS applications.
- Raycast snippet expansion, cursor placement and multiline insertion in each browser, desktop and terminal agent input. The firmware sends the snippet trigger without Enter, but the host app and Raycast determine expansion behavior.
- The included GitHub Actions workflow was not run. The local build included the pinned modules and the repository's fence module explicitly.

The supplied original ZIP failed both builds due to parameterized tap bindings inside combo hold-taps. This revision separates the tap behavior and its parameter in `ZMK_COMBO_9`; the full builds above include that correction. F+P is disabled on Num so it cannot intercept the number keys 8 and 9.
