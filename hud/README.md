# Layer-only ZMK Layer HUD

This config adds [ZMK Layer HUD](https://github.com/rafaelromao/zmk-layer-hud) v1.2.0 to the Totem. The firmware reports the active layers, and the Mac panel shows their existing 38-key diagrams. It does not ask the keyboard to report physical key positions. The accompanying Mac-side patch prevents the panel from opening its normal typed-key HID reader or recording typing sessions. As a result, key lighting, typed characters and typing statistics are intentionally unavailable.

The integration is pinned to HUD commit `ddf52fb44a29fd7de2b260a465604c016b934458`. The firmware module uses a separate USB serial interface when cabled and an encrypted, bonded GATT service when the keyboard is using Bluetooth. Only the left, central half needs reflashing. Layer changes themselves remain visible to the HUD and can reveal when you are using a layer.

## 1. Flash the updated left half

The latest locally built file, if present, is `~/dev/zmk-config/build/firmware/totem_left_colemak_only.uf2`. It is ignored by Git and will not appear in a fresh clone. To build it yourself, follow the [main build instructions](../README.md#build-and-flash-the-totem); the left build now includes `-S layer-hud-usb-uart`. The build instructions produce `totem_left.uf2` and `totem_right.uf2`.

1. Connect the **left** half over USB and press its reset button twice quickly.
2. Copy `totem_left_colemak_only.uf2` (or your freshly built `totem_left.uf2`) to the `XIAO-SENSE` bootloader drive.
3. After the drive disappears and the half restarts, connect the left half to the Mac and test normal typing.

On this Mac, the older `totem_left_layer_hud.uf2` includes the QWERTY fallback; `totem_left_before_layer_hud.uf2` is older still and has no HUD. Both are rollback files, not the current layout. The regular `totem_left.uf2` name is used by the main build instructions and will be overwritten by a new build, so do not assume it remains a rollback. The freshly built right-hand firmware is byte-for-byte identical to the previous right-hand build in our local test, so the right half does not need reflashing. A macOS copy warning can appear when a successful UF2 write causes the drive to restart; test the keyboard rather than relying on that warning alone. See [ZMK's flash instructions](https://zmk.dev/docs/user-setup#flash-uf2-files).

## 2. Install the Mac HUD from the pinned source

The project runs Python code and installs dependencies; open source is not a security audit and this version has not been independently audited. The project's installer recommends running a downloaded script, but these instructions use a pinned clone so you can inspect it and the patch first. The source, module and host version should stay together. This repo does not install or start anything automatically.

Prerequisites: Homebrew, Python 3.10 or later, and internet access. The commands below use the Python 3.12 already present at `/opt/homebrew/bin/python3.12` on this Mac. `make install` invokes the project's setup: it installs Homebrew `hidapi` if needed, creates a virtual environment under the HUD clone, installs its Python dependencies, and links a command into `~/.local/bin`. The upstream launcher currently requires the `hid` Python package to be present even though our patch disables its key reader. Review `Makefile`, `host/cli.py`, `host/requirements.txt` and the patch before running if desired.

In Terminal:

```sh
git clone https://github.com/rafaelromao/zmk-layer-hud.git "$HOME/dev/zmk-layer-hud"
cd "$HOME/dev/zmk-layer-hud"
git checkout --detach ddf52fb44a29fd7de2b260a465604c016b934458
git apply --check "$HOME/dev/zmk-config/hud/layer-only-v1.2.0.patch"
git apply "$HOME/dev/zmk-config/hud/layer-only-v1.2.0.patch"
ZMKHUD_PYTHON=/opt/homebrew/bin/python3.12 make install
```

The clone step requires `~/dev/zmk-layer-hud` not to exist already. If it does, inspect it first instead of overwriting it. The patch is specific to v1.2.0; do not update the clone without re-evaluating and reapplying an appropriate layer-only patch. `git diff` in the HUD clone shows the change. The firmware dependency in this repository is pinned to the same commit.

Link this repository's HUD config and already generated drawing, check it, then start the panel:

```sh
HUD="$HOME/dev/zmk-layer-hud/bin/zmk-layer-hud"
"$HUD" config link "$HOME/dev/zmk-config/hud/config.yaml"
"$HUD" keymap
"$HUD" start
```

`config link` keeps an existing non-symlink HUD config as a `.bak` file. The panel opens on the screen with focus; drag and resize it, and change `hud.opacity` in `hud/config.yaml` to adjust transparency. The upstream default shortcut is Ctrl+Option+L to show or hide it. Stop it with `"$HOME/dev/zmk-layer-hud/bin/zmk-layer-hud" stop`.

The upstream setup may print generic advice to grant **Input Monitoring** for typed-key display. The layer-only patch disables that reader, so do not grant it for this setup. For Bluetooth, macOS may request Bluetooth permission for the process running the HUD. The project says a re-pair may be needed if macOS caches the old Bluetooth service; try the existing pairing first. Do not run `feed --raw` when privacy matters: upstream documents that raw logs can contain key data.

## 3. Verify and maintain

- With the updated left half connected, hold Space/Nav, Enter/Sym, or Backspace/Num. The HUD should follow the current layer and return to Base on release. Try both USB and Bluetooth if you use both; test those paths separately.
- If it does not follow, run `"$HOME/dev/zmk-layer-hud/bin/zmk-layer-hud" doctor` and `"$HOME/dev/zmk-layer-hud/bin/zmk-layer-hud" status`. See the [upstream troubleshooting guide](https://github.com/rafaelromao/zmk-layer-hud#troubleshooting). If Bluetooth still shows no service, forget and re-pair the keyboard as the project recommends.
- `config.yaml` maps the ten numeric layer IDs explicitly and names `~/dev/zmk-config/draw/keymap.yaml`. If you move this repository, update both drawing paths in that config. Regenerate the drawing after a keymap change and run `"$HOME/dev/zmk-layer-hud/bin/zmk-layer-hud" sync` to refresh the HUD definitions. If firmware layer numbers change, update `layers.map` as well. The importer cannot select this repo by name because the archived alternatives contain identically named keymaps, so this setup imports the already generated drawing directly.
- The HUD's generated `config.definitions.json` accompanies the config for a reproducible first run. Base and Num show shifted punctuation above the tap legend. The QWERTY layer is removed; an unreachable placeholder keeps existing HUD layer numbers stable. The firmware and host component have been built or checked locally, but the updated firmware and HUD display still require testing together on the physical keyboard.
