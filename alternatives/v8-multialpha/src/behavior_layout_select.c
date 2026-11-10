/* SPDX-License-Identifier: MIT */
#define DT_DRV_COMPAT custom_behavior_layout_select

#include <zephyr/device.h>
#include <drivers/behavior.h>
#include <zmk/behavior.h>
#include <zmk/keymap.h>

#if DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT) && DT_NODE_EXISTS(DT_NODELABEL(num_word))
/* Keep the auto-layer module's internal state in sync before &to clears layers. */
static int layout_pressed(struct zmk_behavior_binding *binding,
                          struct zmk_behavior_binding_event event) {
    if (zmk_keymap_layer_active(4)) {
        struct zmk_behavior_binding numword = {
            .behavior_dev = DEVICE_DT_NAME(DT_NODELABEL(num_word)), .param1 = 4,
        };
        int result = zmk_behavior_invoke_binding(&numword, event, true);
        if (result < 0) { return result; }
        zmk_behavior_invoke_binding(&numword, event, false);
    }
    int result = zmk_keymap_layer_to(binding->param1, true);
    return result < 0 ? result : ZMK_BEHAVIOR_OPAQUE;
}
static int layout_released(struct zmk_behavior_binding *binding,
                           struct zmk_behavior_binding_event event) {
    return ZMK_BEHAVIOR_OPAQUE;
}
static const struct behavior_driver_api layout_api = {
    .binding_pressed = layout_pressed,
    .binding_released = layout_released,
};
#define LAYOUT_INST(n) \
    BEHAVIOR_DT_INST_DEFINE(n, NULL, NULL, NULL, NULL, POST_KERNEL, \
                            CONFIG_KERNEL_INIT_PRIORITY_DEFAULT, &layout_api);
DT_INST_FOREACH_STATUS_OKAY(LAYOUT_INST)
#endif
