# Validation

Validated locally on 16 November 2026 against Miryoku ZMK source `559aa4beae75cb3206ab411b7da2adb9665c6896`, ZMK `4dd95d7840eb3d5a3f59bb29fbf1ab054715ef85` and Zephyr `10ba6d0cb38bc3d258775d27982f707599320085`.

- Both wireless XIAO nRF52840 Totem halves compiled and linked locally.
- After reorganizing this repository, both halves were built again with the configuration copied to a separate directory, matching the important file-placement behavior of the planned GitHub workflow. The workflow itself has not yet run on GitHub.
- Nine ZMK keyboard simulator scenarios passed with the customized Inverted-T layout: F+P backtick, Cmd+backtick, W+F+P typing `;;fence` with no Enter, thumb Backspace, Nav Page Up, Page Down, Up, Mac Undo and Mac Copy. A separate simulation of the new Mouse Up position produced negative vertical pointer movement. The click check was run before the Inverted-T change; the current mouse position mappings are also checked by `draw/validate.py`.
- keymap-drawer parsed 38 positions for each layer; `draw/validate.py` checks the visual alignment, selected Mac clipboard bindings, Backspace and replaced keys.

## Layer-only HUD integration

- Both halves built locally against HUD module v1.2.0 (`ddf52fb44a29fd7de2b260a465604c016b934458`) and the existing pinned ZMK and Zephyr sources. The left build enables the USB and Bluetooth signal transports; its generated devicetree sets `positions` to false. The right UF2 matches the previous right build byte for byte.
- The nine existing ZMK simulator scenarios passed with the HUD module included. The HUD module's standalone firmware tests passed 45 checks. The host test suite ran 590 tests with 22 skipped; it was isolated from the user's home directory. A targeted check verified that `Feed(keys=False, sessions=False)` creates neither the HID key reader nor a session store, drops key and position messages, and still passes layer messages.
- The HUD imported the generated drawing with 38 keys and ten layers; the configured IDs 0 through 9 matched the Miryoku layer list. The pinned Mac-panel patch was checked against a clean copy of v1.2.0.
- The user subsequently confirmed the HUD displayed the keyboard's layers. The newly rebuilt firmware and updated drawing have not yet been tested together on the physical keyboard. The dependency was reviewed only for the integration and layer-only data path, not comprehensively audited for security.

## QWERTY removal and punctuation

- Both halves rebuilt successfully. The right-hand UF2 is byte-for-byte unchanged; the left-hand firmware must be reflashed to remove QWERTY.
- Twelve simulator scenarios passed, including checks that the old QWERTY shortcut no longer changes the alphabet, Shift plus slash emits `?`, and Sym plus the Space thumb emits `)`. These cover firmware behavior, not the user's macOS input source or physical timing.
- The compiled keymap contains no `Extra` layer or Extra activation behavior. Its unreachable `Unused` placeholder preserves the other HUD layer IDs. The regenerated HUD data includes shifted punctuation and retains the same IDs.

The user confirmed Seeed Studio XIAO BLE/nRF52840 controllers. Not verified: the actual purchased Totem+ matrix, pin wiring, bootloader, physical keycaps, Bluetooth pairing, macOS pointer feel, timing, Homerow, Raycast snippet expansion, or GitHub Actions. The mouse-up and click log checks were inspected manually; the keyboard HID regression scenarios are preserved in `tests/`. Simulation cannot prove physical comfort or reliability.
