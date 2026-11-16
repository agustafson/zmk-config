# Totem ZMK configurations

A personal collection of ZMK layouts for a 38-key Totem-style split keyboard, used with macOS. **The root configuration is the current Miryoku-based Colemak-DH trial.** See the [layout and setup guide](MIRYOKU.md) and [typing plan](docs/typing-plan.md).

| Configuration | What it is | Status |
| --- | --- | --- |
| [Miryoku + Colemak-DH](MIRYOKU.md) | Coordinated Nav, Mouse, Num, Sym and function layers; six thumb-layer roles; Hyper and Meh. | **Current default**; root GitHub Actions workflow builds this option. |
| [Urob-inspired](alternatives/urob/README.md) | Colemak-DH, more symbol combos, Magic Shift and automatic Num Word. | Preserved alternative; separate build needed. |
| [Multi-alphabet v8](alternatives/v8-multialpha/GUIDE.md) | Earlier shared chassis with Colemak, Colemak-DH, Graphite and Gallium selectable at runtime. | Historical experiment; separate build needed. Its defaults and shortcuts differ from the current layout. |

The alternatives are source snapshots inside this repository, not independently active build targets. Their documentation reflects the respective versions and should not be mistaken for the current mapping. To try one, copy the contents of its folder into a separate working config root and build against its own dependency manifest and custom module. The root GitHub workflow builds **only** the Miryoku configuration.

## Current layout at a glance

The extra left pinky is Hyper (Cmd+Ctrl+Option+Shift); the extra right pinky is Meh (Ctrl+Option+Shift). For thumbs, tap sends the named key and hold activates the layer:

| Left, outer to inner | Right, inner to outer |
| --- | --- |
| Escape / Media | Enter / Sym |
| Space / Nav | Backspace / Num |
| Tab / Mouse | Escape / Fun |

F+P sends a backtick. W+F+P types the Raycast snippet trigger `;;fence` and does not itself send Enter. See [MIRYOKU.md](MIRYOKU.md) for configuration and testing, and [the full layer diagram](draw/miryoku-layers.png).

For the optional, layer-only on-screen overlay, see the [ZMK Layer HUD setup](hud/README.md). The firmware build includes its layer signal; the Mac app requires the documented pinned source and privacy patch.

## Build and flash the Totem

These instructions are for the **default Miryoku configuration**, a Mac and a wireless Totem with a XIAO nRF52840 in each half. This config assumes the original Totem matrix and left-central wiring; the controller model is confirmed, but the purchased board's wiring has not yet been verified. Check the seller's wiring or source against `config/boards/shields/totem/` before flashing.

The left and right halves need **different firmware files** and must each be connected and flashed separately. The UF2 files are generated locally in `build/firmware/`, which Git ignores. They are not included when you clone the repository.

### Build locally with Docker

Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/) first. The first build downloads the ZMK image and the pinned ZMK/Zephyr dependencies, so it needs internet access and can take a while. It creates a new workspace under `~/dev/` on every run; you can remove that workspace after retrieving the UF2 files. This keeps the dependency workspace separate from this repository's own `zephyr/` module.

Run the following in Terminal. Copy the whole block into one Terminal session, since it uses shell variables:

```sh
ZMK_REPO="$HOME/dev/zmk-config"
ZMK_WORKSPACE=$(mktemp -d "$HOME/dev/totem-zmk-work.XXXXXX")
mkdir "$ZMK_WORKSPACE/config"
cp -R "$ZMK_REPO/config/." "$ZMK_WORKSPACE/config/"

docker run --rm \
  -v "$ZMK_WORKSPACE:/workspace" \
  -v "$ZMK_REPO:/repo:ro" \
  -w /workspace zmkfirmware/zmk-build-arm:stable /bin/sh -c '
    set -eu
    west init -l /workspace/config
    west update --fetch-opt=--filter=tree:0
    west zephyr-export
    west build -s zmk/app -d /workspace/build-left -b xiao_ble//zmk -S layer-hud-usb-uart -- \
      -DSHIELD=totem_left -DZMK_CONFIG=/workspace/config -DZMK_EXTRA_MODULES=/repo
    west build -s zmk/app -d /workspace/build-right -b xiao_ble//zmk -- \
      -DSHIELD=totem_right -DZMK_CONFIG=/workspace/config -DZMK_EXTRA_MODULES=/repo
  ' && \
mkdir -p "$ZMK_REPO/build/firmware" && \
cp "$ZMK_WORKSPACE/build-left/zephyr/zmk.uf2" "$ZMK_REPO/build/firmware/totem_left.uf2" && \
cp "$ZMK_WORKSPACE/build-right/zephyr/zmk.uf2" "$ZMK_REPO/build/firmware/totem_right.uf2" && \
open "$ZMK_REPO/build/firmware"
```

When the build succeeds, Finder opens a folder containing `totem_left.uf2` and `totem_right.uf2`. If the build fails, fix the error and run the block again; do not assume older files in `build/firmware/` match the latest config. For other local toolchain setups, see [ZMK's build documentation](https://zmk.dev/docs/development/local-toolchain/build-flash): this repo requires both `ZMK_CONFIG` and `ZMK_EXTRA_MODULES`.

### Flash each half over USB

1. Locate the two generated UF2 files in `~/dev/zmk-config/build/firmware/`. If they are already present, confirm they were built from the revision you intend to use; otherwise build them first.
2. Connect the **left** half to the Mac with a USB data cable. Quickly press its reset button twice to enter the bootloader. Use the reset button on the Totem PCB, or the XIAO reset button if accessible. A removable drive should appear in Finder; its name depends on the bootloader.
3. Copy `totem_left.uf2` to the root of that drive. Wait for the copy to finish: the drive normally disappears as the controller flashes and restarts.
4. Connect the **right** half separately. Double-press its reset button, then copy `totem_right.uf2` to the new bootloader drive. Wait for it to disappear and restart.
5. Power both halves. Connect the left half by USB and try keys on both halves in a scratch text field. The left is the central half for this config; the right half communicates with it wirelessly. If they do not connect, reset both halves at about the same time and allow a few seconds. Then test Bluetooth if desired.

Use the macOS **U.S. or ABC** input source when testing: the firmware produces Colemak-DH. First try the basic letters, thumb keys, Nav and Backspace; the layout and timing are not yet verified on this particular board. If no bootloader drive appears, try a known data-capable cable and double-press reset again. See [ZMK's flashing instructions](https://zmk.dev/docs/user-setup#flash-uf2-files) and [connection troubleshooting](https://zmk.dev/docs/troubleshooting/connection-issues) if needed. A settings-reset firmware erases stored settings and Bluetooth pairings, so follow that troubleshooting procedure only if required.

### Build later with GitHub Actions

Once this repository has a GitHub remote and has been pushed, a push triggers the included build workflow. Open the repository's **Actions** tab, select a successful **Build Totem firmware** run, download its `firmware` artifact and extract it. Match the filenames containing `totem_left` and `totem_right` to the corresponding halves, then follow the USB steps above. The workflow builds the default configuration only and has not yet been run on GitHub.

## Structure and building

- `config/` contains the active ZMK configuration, Totem shield and vendored Miryoku files. `config/miryoku/custom_config.h` contains the personal layer overrides.
- `build.yaml` selects the left and right XIAO BLE targets. `.github/workflows/build.yml` is prepared for GitHub Actions; it has not yet run on GitHub.
- `zephyr/`, `src/` and `dts/` form the custom ZMK module for the fence trigger; they are needed to build the active layout.
- `draw/` contains generated diagrams and their generator. `tests/` contains simulator checks; [VALIDATION.md](VALIDATION.md) describes what has and has not been tested.
- `alternatives/` contains other layouts for reference and separate builds. `docs/` contains the learning plan.

This repository has no GitHub remote yet. Once you create a remote and push, the workflow should build the default on changes; verify its first run before relying on the artifacts. Dependencies are pinned in `config/west.yml`. The prior local builds and simulated key tests are documented in [VALIDATION.md](VALIDATION.md). Do not treat the firmware as verified on physical hardware.

## Hardware and input source

The user confirmed Seeed Studio XIAO BLE/nRF52840 controllers. The shield also assumes the original Totem's matrix, pin wiring and left-central arrangement; those details and the physical device still need verification. On the Mac, select **U.S. or ABC** while using this keyboard, because the firmware already emits Colemak-DH. A MacBook without the Totem needs its own chosen input source.

The code and layout include material from Miryoku, urob's ZMK configuration and the GEIGEIGEIST Totem project; see the individual configuration guides for attribution and licenses.
