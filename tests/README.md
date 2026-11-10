# Simulator regression scenarios

Each fixture starts with a dummy Q and pause to establish prior-idle timing. Recorded snapshots include that Q. The tests are for ZMK native_sim and do not verify the physical keyboard or the host apps.

Create a separate west workspace using a copy of this repository's `config/` directory; do not initialize west at this repo root because its `zephyr/` folder is the fence module. After `west init -l config`, `west update` and `west zephyr-export`, run from that workspace's `zmk/app`, with this repository as an extra module:

```sh
ZMK_EXTRA_MODULES=/path/to/totem-miryoku-zmk ./run-test.sh /path/to/totem-miryoku-zmk/tests
```
