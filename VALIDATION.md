# Validation

Validated locally on 16 November 2026 against Miryoku ZMK source `559aa4beae75cb3206ab411b7da2adb9665c6896`, ZMK `4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85` and Zephyr `10ba6d0cb38bc3d258775d27982f707599320085`.

- Both wireless XIAO nRF52840 Totem halves compiled and linked locally.
- After reorganizing this repository, both halves were built again with the configuration copied to a separate directory, matching the important file-placement behavior of the planned GitHub workflow. The workflow itself has not yet run on GitHub.
- Nine ZMK keyboard simulator scenarios passed with the customized Inverted-T layout: F+P backtick, Cmd+backtick, W+F+P typing `;;fence` with no Enter, thumb Backspace, Nav Page Up, Page Down, Up, Mac Undo and Mac Copy. A separate simulation of the new Mouse Up position produced negative vertical pointer movement. The click check was run before the Inverted-T change; the current mouse position mappings are also checked by `draw/validate.py`.
- keymap-drawer parsed 38 positions for each layer; `draw/validate.py` checks the visual alignment, selected Mac clipboard bindings, Backspace and replaced keys.

The user confirmed Seeed Studio XIAO BLE/nRF52840 controllers. Not verified: the actual purchased Totem+ matrix, pin wiring, bootloader, physical keycaps, Bluetooth pairing, macOS pointer feel, timing, Homerow, Raycast snippet expansion, or GitHub Actions. The mouse-up and click log checks were inspected manually; the keyboard HID regression scenarios are preserved in `tests/`. Simulation cannot prove physical comfort or reliability.
