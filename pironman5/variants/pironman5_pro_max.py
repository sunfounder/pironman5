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
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        "clear_history",
        "delete_log_file",
        "oled_sleep",
        "pi5_power_button",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "rgb_color": "#ff3dbe",
        "rgb_brightness": 50,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_enable": True,
        "rgb_led_count": 18,
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
    EVENT_MAP = {
        'pi5_power_button_click': 'oled_wake_page_next',
        'pi5_power_button_double_click': 'oled_page_prev',
        'pi5_power_button_long_press': 'oled_show_shutdown_screen',
        'pi5_power_button_long_press_released': 'shutdown',
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5promax.dtbo',
    ]

