class Pironman5ProMax:
    NAME = "Pironman 5 Pro Max"
    ID = "pironman5-pro-max"
    PRODUCT_VERSION = ""
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
        "vibration_switch",
        "oled_sleep",
        "pi5_power_button",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "rgb_color": "#0a1aff",
        "rgb_brightness": 50,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_enable": True,
        "rgb_led_count": 15,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        "oled_disk": "total",
        "oled_network_interface": "all",
        'oled_sleep_timeout': 10,
        'vibration_switch_pin': 26,
        'vibration_switch_pull_up': False,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5promax.dtbo',
    ]

