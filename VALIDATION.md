# Validation

Validated locally on 11 November 2026 against Miryoku ZMK source `559aa4beae75cb3206ab411b7da2adb9665c6896`, ZMK `4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85` and Zephyr `10ba6d0cb38bc3d258775d27982f707599320085`.

- Both wireless XIAO nRF52840 Totem halves compiled and linked locally.
- After reorganizing this repository, both halves were built again with the configuration copied to a separate directory, matching the important file-placement behavior of the planned GitHub workflow. The workflow itself has not yet run on GitHub.
- Six ZMK keyboard simulator scenarios passed against the Colemak-DH version: F+P backtick, Cmd+backtick, W+F+P typing `;;fence` with no Enter, thumb Backspace, Nav Page Up and Mac Undo. Mouse Up and left click were also simulated on the earlier Colemak-DH version, using the same Mouse layer: Mouse Up produced negative vertical pointer movement and left click produced both press and release reports.
- keymap-drawer parsed 38 positions for each layer; `draw/validate.py` checks the visual alignment, selected Mac clipboard bindings, Backspace and replaced keys.

The user confirmed Seeed Studio XIAO BLE/nRF52840 controllers. Not verified: the actual purchased Totem+ matrix, pin wiring, bootloader, physical keycaps, Bluetooth pairing, macOS pointer feel, timing, Homerow, Raycast snippet expansion, or GitHub Actions. The mouse-up and click log checks were inspected manually; the keyboard HID regression scenarios are preserved in `tests/`. Simulation cannot prove physical comfort or reliability.
