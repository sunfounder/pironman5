class Pironman5V10:
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
    ]
    SYSTEM_DEFAULT_CONFIG = {
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
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 1,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5.dtbo',
    ]
