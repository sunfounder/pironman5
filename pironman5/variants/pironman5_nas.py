class Pironman5NAS:
    NAME = "Pironman 5 NAS"
    ID = "pironman5-nas"
    PRODUCT_VERSION = ""
    PERIPHERALS = [
        'storage',
        "cpu",
        "network",
        "memory",
        "log",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "delete_log_file",
        'debug_level',
        'ip_address',
        'mac_address',
        "restart_service",

        "oled",
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        "pwm_fan_speed",
        "oled_sleep",
        "pironman_mcu",
    ]
    EVENT_MAP = {
        'pironman_mcu_button_click': 'oled_wake_page_next',
        'pironman_mcu_button_double_click': 'oled_page_prev',
        'pironman_mcu_button_long_press': 'shutdown',
    }
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'database_retention_days': 30,
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
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5nas.dtbo',
    ]

