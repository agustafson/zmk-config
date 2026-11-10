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
