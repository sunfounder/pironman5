class Pironman5Mini:
    NAME = "Pironman 5 Mini"
    ID = "pironman5-mini"
    PRODUCT_VERSION = ""
    PERIPHERALS = [
        "storage",
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "ws2812",
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "clear_history",
        "delete_log_file",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "gpio_fan_led",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'temperature_unit': 'C',
        'rgb_led_count': 4,
        'rgb_enable': True,
        'rgb_color': '#ff00ff',
        'rgb_brightness': 50,
        'rgb_style': 'rainbow',
        'rgb_speed': 50,
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 0,
        'gpio_fan_led': 'follow',
        'gpio_fan_led_pin': 5,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5mini.dtbo',
    ]

