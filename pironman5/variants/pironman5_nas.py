class Pironman5NAS:
    NAME = "Pironman 5 NAS"
    ID = "pironman5-nas"
    PRODUCT_VERSION = ""
    PERIPHERALS = [
        'storage',
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "restart_service",
        "clear_history",
        "delete_log_file",

        "oled",
        "pwm_fan_speed",
        "oled_sleep",
        "pironman_mcu",
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
            ],
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5nas.dtbo',
    ]

