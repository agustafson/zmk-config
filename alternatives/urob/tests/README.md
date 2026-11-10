# ZMK native simulation fixtures

Each scenario starts with a dummy Q and 300 ms pause so prior-idle guards start from a known state. Snapshots record actual HID key events, including the initial Q.

Create a **separate** west workspace using a copy of this repository's `config/` directory: the repository's own `zephyr/module.yml` is needed for the custom fence behavior, so do not initialize west at the repository root. Run `west init -l config`, `west update`, and `west zephyr-export` in that separate workspace. Then run the ZMK test runner from its ZMK app directory, with this repository registered as an extra module. Replace the two paths below with your own absolute paths:

```sh
cd /path/to/workspace/zmk/app
ZMK_EXTRA_MODULES=/path/to/totem-mac-zmk ./run-test.sh /path/to/totem-mac-zmk/tests
```

The other modules must be present in the workspace via `west update`. Tests use the `native_sim` mock board and do not validate physical switches, Bluetooth, the host OS or Raycast.
