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
        "cpu_temperature",
        "gpu_temperature",
        "temperature_unit",
        "restart_service",
        "clear_history",
        "delete_log_file",
        
        "ws2812",
        "pwm_fan_speed",
        "gpio_fan_state",
        "gpio_fan_mode",
        "gpio_fan_led",
    ]
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'temperature_unit': 'C',
        'rgb_enable': True,
        'rgb_led_count': 4,
        'rgb_style': 'rainbow',
        'rgb_color': '#ff00ff',
        'rgb_brightness': 100,
        'rgb_speed': 50,
        'gpio_fan_pin': 6,
        'gpio_fan_mode': 0,
        'gpio_fan_led': 'follow',
        'gpio_fan_led_pin': 5,
    }
    DT_OVERLAYS = [
        'sunfounder-pironman5mini.dtbo',
    ]

