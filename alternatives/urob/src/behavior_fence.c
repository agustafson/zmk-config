/* Copyright (c) 2026. SPDX-License-Identifier: MIT */
#define DT_DRV_COMPAT custom_behavior_fence

#include <zephyr/device.h>
#include <zephyr/logging/log.h>
#include <drivers/behavior.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/modifiers.h>
#include <zmk/behavior.h>
#include <zmk/behavior_queue.h>
#include <zmk/endpoints.h>
#include <zmk/events/keycode_state_changed.h>
#include <zmk/hid.h>

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

/* Each press is paired with its release even if the macro is still running. */
static bool press_was_macro;
static bool macro_running;

static int finish_pressed(struct zmk_behavior_binding *binding,
                          struct zmk_behavior_binding_event event) {
    ARG_UNUSED(binding);
    ARG_UNUSED(event);
    zmk_hid_masked_modifiers_clear();
    zmk_endpoint_send_report(HID_USAGE_KEY);
    macro_running = false;
    return ZMK_BEHAVIOR_OPAQUE;
}

static int finish_released(struct zmk_behavior_binding *binding,
                           struct zmk_behavior_binding_event event) {
    ARG_UNUSED(binding);
    ARG_UNUSED(event);
    return ZMK_BEHAVIOR_OPAQUE;
}

static const struct behavior_driver_api finish_api = {
    .binding_pressed = finish_pressed,
    .binding_released = finish_released,
};

/* An internal queue sentinel restores the real physical modifiers only after
 * all macro events have been emitted, even if the user taps the trigger fast. */
BEHAVIOR_DT_DEFINE(DT_NODELABEL(fence_finish), NULL, NULL, NULL, NULL, POST_KERNEL,
                   CONFIG_KERNEL_INIT_PRIORITY_DEFAULT, &finish_api);

static int fence_action_pressed(struct zmk_behavior_binding *binding,
                                struct zmk_behavior_binding_event event,
                                bool shift_required, bool force_fence) {
    ARG_UNUSED(binding);
    const zmk_mod_flags_t mods = zmk_hid_get_explicit_mods();
    const bool command = (mods & (MOD_LGUI | MOD_RGUI)) != 0;
    const bool shift = (mods & (MOD_LSFT | MOD_RSFT)) != 0;
    press_was_macro = (force_fence || (command && (!shift_required || shift))) && !macro_running;
    if (!press_was_macro) {
        return raise_zmk_keycode_state_changed_from_encoded(GRAVE, true, event.timestamp);
    }

    macro_running = true;
    zmk_hid_masked_modifiers_set(0xFF);
    zmk_endpoint_send_report(HID_USAGE_KEY);

    struct zmk_behavior_binding key = { .behavior_dev = DEVICE_DT_NAME(DT_NODELABEL(kp)) };
    /* Raycast expands this trigger into a pasted multiline fence. */
    const uint32_t keys[] = { SEMI, SEMI, F, E, N, C, E };
    for (size_t i = 0; i < ARRAY_SIZE(keys); i++) {
        key.param1 = keys[i];
        if (zmk_behavior_queue_add(&event, key, true, 10) < 0 ||
            zmk_behavior_queue_add(&event, key, false, 10) < 0) {
            LOG_ERR("Fence macro queue full");
            zmk_hid_masked_modifiers_clear();
            zmk_endpoint_send_report(HID_USAGE_KEY);
            macro_running = false;
            return ZMK_BEHAVIOR_OPAQUE;
        }
    }
    const struct zmk_behavior_binding finish = {
        .behavior_dev = DEVICE_DT_NAME(DT_NODELABEL(fence_finish)),
    };
    if (zmk_behavior_queue_add(&event, finish, true, 0) < 0) {
        LOG_ERR("Fence macro cleanup queue full");
        zmk_hid_masked_modifiers_clear();
        zmk_endpoint_send_report(HID_USAGE_KEY);
        macro_running = false;
    }
    return ZMK_BEHAVIOR_OPAQUE;
}

static int fence_released(struct zmk_behavior_binding *binding,
                          struct zmk_behavior_binding_event event) {
    ARG_UNUSED(binding);
    if (press_was_macro) {
        press_was_macro = false;
        return ZMK_BEHAVIOR_OPAQUE;
    }
    return raise_zmk_keycode_state_changed_from_encoded(GRAVE, false, event.timestamp);
}

/* Optional command-aware backtick behavior retained for the F+P chord. */
static int fence_pressed(struct zmk_behavior_binding *binding,
                         struct zmk_behavior_binding_event event) {
    return fence_action_pressed(binding, event, true, false);
}
static int combo_fence_pressed(struct zmk_behavior_binding *binding,
                               struct zmk_behavior_binding_event event) {
    return fence_action_pressed(binding, event, false, false);
}
static const struct behavior_driver_api combo_fence_api = {
    .binding_pressed = combo_fence_pressed,
    .binding_released = fence_released,
};
#undef DT_DRV_COMPAT
#define DT_DRV_COMPAT custom_behavior_combo_fence
#define COMBO_FENCE_INST(n) \
    BEHAVIOR_DT_INST_DEFINE(n, NULL, NULL, NULL, NULL, POST_KERNEL, \
                            CONFIG_KERNEL_INIT_PRIORITY_DEFAULT, &combo_fence_api);
DT_INST_FOREACH_STATUS_OKAY(COMBO_FENCE_INST)
#undef DT_DRV_COMPAT
#define DT_DRV_COMPAT custom_behavior_fence

/* The W+F+P chord invokes the snippet trigger without a modifier. */
static int direct_fence_pressed(struct zmk_behavior_binding *binding,
                                struct zmk_behavior_binding_event event) {
    return fence_action_pressed(binding, event, false, true);
}
static const struct behavior_driver_api direct_fence_api = {
    .binding_pressed = direct_fence_pressed,
    .binding_released = fence_released,
};
#undef DT_DRV_COMPAT
#define DT_DRV_COMPAT custom_behavior_direct_fence
#define DIRECT_FENCE_INST(n) \
    BEHAVIOR_DT_INST_DEFINE(n, NULL, NULL, NULL, NULL, POST_KERNEL, \
                            CONFIG_KERNEL_INIT_PRIORITY_DEFAULT, &direct_fence_api);
DT_INST_FOREACH_STATUS_OKAY(DIRECT_FENCE_INST)
#undef DT_DRV_COMPAT
#define DT_DRV_COMPAT custom_behavior_fence

static const struct behavior_driver_api fence_api = {
    .binding_pressed = fence_pressed,
    .binding_released = fence_released,
};

#define FENCE_INST(n) \
    BEHAVIOR_DT_INST_DEFINE(n, NULL, NULL, NULL, NULL, POST_KERNEL, \
                            CONFIG_KERNEL_INIT_PRIORITY_DEFAULT, &fence_api);
DT_INST_FOREACH_STATUS_OKAY(FENCE_INST)
