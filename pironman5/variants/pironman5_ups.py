class Pironman5UPS:
    NAME = "Pironman 5 UPS"
    ID = "pironman5-ups"
    PRODUCT_VERSION = "V1"
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
        "restart_service",
        "clear_history",
        "delete_log_file",
        "data_interval",

        "oled",
        "oled_sleep",
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        'oled_page_battery',
        'oled_page_input',
        'oled_page_output',
        "pwm_fan_speed",
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
        "power-failure-simulation",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        'oled_sleep_timeout': 10,
        'oled_pages': [
            'mix',
            'performance',
            'ips',
            'disk',
            'battery',
            'input',
            'output',
        ],
        'rgb_matrix_enable': True,
        'rgb_matrix_style': "rainbow",
        'rgb_matrix_color': "#0a1aff",
        'rgb_matrix_color2': "#00ff00",
        'rgb_matrix_speed': 50,
        'rgb_matrix_brightness': 100,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5ups.dtbo',
    ]

