class Pironman5:
    NAME = "Pironman 5"
    ID = "pironman5"
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
        "clear_history",
        "delete_log_file",
        'debug_level',
        'ip_address',
        'mac_address',
        "restart_service",
        
        "oled",
        "oled_sleep",
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        "ws2812",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "pi5_power_button",
    ]
    EVENT_MAP = {
        'pi5_power_button_click': 'oled_wake_page_next',
        'pi5_power_button_double_click': 'oled_page_prev',
        'pi5_power_button_long_press': 'oled_show_shutdown_screen',
        'pi5_power_button_long_press_released': 'shutdown',
    }
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'database_retention_days': 30,
        "temperature_unit": "C",
        'enable_history': True,
        "oled_enable": True,
        "oled_rotation": 0,
        'oled_sleep_timeout': 10,
        'oled_pages': [
            'mix',
            'performance',
            'ips',
            'disk',
        ],
        "rgb_enable": True,
        "rgb_color": "#0a1aff",
        "rgb_brightness": 100,
        "rgb_style": "breathing",
        "rgb_speed": 50,
        "rgb_led_count": 4,
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 0,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5.dtbo',
    ]
