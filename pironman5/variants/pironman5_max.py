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
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        "ws2812",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "gpio_fan_led",
        "vibration_switch",
        "pi5_power_button",
        "oled_sleep",
    ]
    EVENT_MAP = {
        'pi5_power_button_click': 'oled_wake_page_next',
        'pi5_power_button_double_click': 'oled_page_prev',
        'pi5_power_button_long_press_2s': 'oled_show_shutdown_screen',
        'pi5_power_button_long_press_2s_released': 'shutdown',
    }
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'database_retention_days': 30,
        'enable_history': True,
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
        'oled_sleep_timeout': 10,
        'vibration_switch_pin': 26,
        'vibration_switch_pull_up': False,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5max.dtbo',
    ]

