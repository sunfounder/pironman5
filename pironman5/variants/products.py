import copy

PRODUCT_DEFINITIONS = {
    "base": {
        "name": "Pironman 5",
        "id": "pironman5",
        "product_version": "",
        "modules": [
            "core", "network_info", "history", "oled",
            "ws2812", "pwm_fan", "gpio_fan", "pi5_power_button",
        ],
        "config_overrides": {},
        "event_map_overrides": {},
        "dt_overlays": ["sunfounder-pironman5.dtbo"],
    },
    "max": {
        "name": "Pironman 5 Max",
        "id": "pironman5-max",
        "product_version": "V2",
        "modules": [
            "core", "network_info", "history", "oled",
            "ws2812", "pwm_fan", "gpio_fan", "gpio_fan_led",
            "pi5_power_button",
        ],
        "config_overrides": {},
        "event_map_overrides": {},
        "dt_overlays": ["sunfounder-pironman5.dtbo"],
    },
    "mini": {
        "name": "Pironman 5 Mini",
        "id": "pironman5-mini",
        "product_version": "",
        "modules": [
            "core", "network_info", "history", "ws2812",
            "pwm_fan", "gpio_fan", "gpio_fan_led",
        ],
        "config_overrides": {
            "rgb_style": "rainbow",
            "rgb_color": "#ff00ff",
        },
        "event_map_overrides": {},
        "dt_overlays": ["sunfounder-pironman5mini.dtbo"],
    },
    "nas": {
        "name": "Pironman 5 NAS",
        "id": "pironman5-nas",
        "product_version": "",
        "modules": [
            "core", "network_info", "oled", "pwm_fan",
            "pironman_mcu", "rtl8125",
        ],
        "config_overrides": {},
        "event_map_overrides": {},
        "dt_overlays": ["sunfounder-pironman5nas.dtbo"],
    },
    "ups": {
        "name": "Pironman 5 UPS",
        "id": "pironman5-ups",
        "product_version": "V1",
        "modules": [
            "core", "network_info", "history", "oled",
            "oled_ups_pages", "pwm_fan", "sf_rgb_led", "pipower5",
        ],
        "config_overrides": {
            "debug_level": "INFO",
            "enable_history": True,
            "oled_pages": ["mix", "battery", "input", "rpi_power"],
        },
        "event_map_overrides": {},
        "dt_overlays": [],
    },
    "pipower5": {
        "name": "PiPower 5",
        "id": "pipower5",
        "product_version": "",
        "modules": [
            "core", "network_info", "history", "pipower5",
        ],
        "config_overrides": {
            "debug_level": "INFO",
            "enable_history": True,
        },
        "event_map_overrides": {},
        "dt_overlays": [],
    },
    "pro_max": {
        "name": "Pironman 5 Pro Max",
        "id": "pironman5-pro-max",
        "product_version": "",
        "modules": [
            "core", "network_info", "history", "oled", "ws2812",
            "pi5_power_button",
        ],
        "config_overrides": {
            "debug_level": "INFO",
            "default_dashboard_page": "small",
            "rgb_color": "#ff3dbe",
            "rgb_brightness": 50,
            "rgb_led_count": 18,
            "rgb_led_count_min": 18,
            "rgb_position": [
                17, 16, 15, 14,
                7, 6, 5, 4,
                13, 12,
                11, 10, 9, 8,
                3, 2, 1, 0,
            ],
        },
        "event_map_overrides": {},
        "dt_overlays": ["sunfounder-pironman5promax.dtbo"],
    },
}


# Compatibility: the product was renamed from "Pironman 5 UPS" to
# "Pironman 5 Ultra" (2026-10). Older installations may still have
# ".variant" set to "ultra" while running this release, and the config
# wizard/newer installers may write "ultra" as the variant name. Register
# "ultra" as an alias of the "ups" definition so the correct module set
# (I2C RGB "sf_rgb_led", OLed UPS pages, pipower5 ...) is loaded instead of
# silently falling back to "base".
PRODUCT_DEFINITIONS["ultra"] = copy.deepcopy(PRODUCT_DEFINITIONS["ups"])
PRODUCT_DEFINITIONS["ultra"]["name"] = "Pironman 5 Ultra"
