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
        "pi5_pwr_btn",
    ]
    EVENT_MAP = {
        'pi5_power_button_click': 'oled_wake_page_next',
        'pi5_power_button_double_click': 'oled_page_prev',
        'pi5_power_button_long_press': 'shutdown',
    }
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        "temperature_unit": "C",
        "oled_enable": True,
        "oled_rotation": 0,
        "oled_disk": "total",
        "oled_network_interface": "all",
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
