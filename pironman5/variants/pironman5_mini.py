class Pironman5Mini:
    NAME = "Pironman 5 Mini"
    ID = "pironman5-mini"
    PERIPHERALS = [
        "storage",
        "cpu",
        "network",
        "memory",
        "history",
        "log",
        "ws2812",
        "temperature_unit",
        "clear_history",
        "delete_log_file",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "gpio_fan_led",
    ]
    AUTO_DEFAULT_CONFIG = {
        'temperature_unit': 'C',
        'rgb_led_count': 4,
        'rgb_enable': True,
        'rgb_color': '#ff00ff',
        'rgb_brightness': 100,
        'rgb_style': 'rainbow',
        'rgb_speed': 0,
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 1,
        'gpio_fan_led': 'follow',
        'gpio_fan_led_pin': 5,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5mini.dtbo',
    ]

