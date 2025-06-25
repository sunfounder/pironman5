class Pironman5Max:
    NAME = "Pironman 5 Max"
    ID = "pironman5-max"
    PRODUCT_VERSION = "V2"
    PERIPHERALS = [
        'storage',
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "ws2812",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "oled",
        "clear_history",
        "delete_log_file",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "gpio_fan_led",
        "vibration_switch",
        "oled_sleep",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "rgb_color": "#0a1aff",
        "rgb_brightness": 100,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_enable": True,
        "rgb_led_count": 4,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        'oled_sleep_timeout': 10,
        'oled_pages': [
            'mix',
            'performance',
            'ips',
            'disk',
        ],
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 0,
        'gpio_fan_led': 'follow',
        'gpio_fan_led_pin': 5,
        'vibration_switch_pin': 26,
        'vibration_switch_pull_up': False,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5max.dtbo',
    ]

