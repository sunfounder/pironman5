class Pironman5UPS:
    NAME = "Pironman 5 UPS"
    ID = "pironman5-ups"
    PRODUCT_VERSION = "V2"
    PERIPHERALS = [
        'storage',
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "spc",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "oled",
        "clear_history",
        "delete_log_file",
        "pwm_fan_speed",
        "oled_sleep",
        "rgb_matrix",
        # ----
        "input_voltage",
        "input_current",
        "is_input_plugged_in",
        "output_voltage",
        "output_current",
        "output_power",
        "power_source",
        "battery_voltage",
        "battery_current",
        "battery_percentage",
        "is_charging",
        "shutdown_percentage",
        "default_on",
        "data_interval",
        "power-failure-simulation",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "rgb_color": "#0a1aff",
        "rgb_brightness": 50,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_enable": True,
        "rgb_led_count": 4,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        "oled_disk": "total",
        "oled_network_interface": "all",
        'oled_sleep_timeout': 10,
        'oled_pages': [# set
            'performance',
            'ips',
            'disk',
            'battery',
            'input',
            'output',
        ],
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5.dtbo',
    ]

