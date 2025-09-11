class Pironman5UPS:
    NAME = 'Pironman 5 UPS'
    ID = 'pironman5-ups'
    PRODUCT_VERSION = 'V1'
    PERIPHERALS = [
        'storage',
        'cpu',
        'network',
        'memory',
        'history',
        'log',
        'cpu_temperature',
        'gpu_temperature',
        'temperature_unit',
        'clear_history',
        'delete_log_file',
        'data_interval',
        'debug_level',
        'ip_address',
        'mac_address',
        'restart_service',

        'oled',
        'oled_sleep',
        'oled_page_mix',
        'oled_page_performance',
        'oled_page_ips',
        'oled_page_disk',
        'oled_page_battery',
        'oled_page_input',
        'oled_page_rpi_power',
        'pwm_fan_speed',
        'rgb_matrix',
        # ----
        'pipower5',
        'input_voltage',
        'input_current',
        'is_input_plugged_in',
        'output_voltage',
        'output_current',
        'output_power',
        'power_source',
        'battery_voltage',
        'battery_current',
        'battery_percentage',
        'is_charging',
        'shutdown_percentage',
        'default_on',
        'power-failure-simulation',
        'send_email',
    ]
    EVENT_MAP = {
        'pipower5_button_click': 'oled_wake_page_next',
        'pipower5_button_double_click': 'oled_page_prev',
        'pipower5_low_battery_shutdown': 'shutdown',
        'pipower5_button_long_press': 'oled_show_shutdown_screen',
        'pipower5_button_long_press_released': 'shutdown',
        'pipower5_low_voltage_shutdown': 'shutdown',
    }
    SYSTEM_DEFAULT_CONFIG = {
        'data_interval': 1,
        'debug_level': 'INFO',
        'database_retention_days': 30,
        'temperature_unit': 'C',
        'oled_enable': True,
        'oled_rotation': 0,
        'oled_sleep_timeout': 10,
        'shutdown_percentage': 10,
        'enable_history': True,
        'oled_pages': [
            'mix',
            'battery',
            'input',
            'rpi_power',
        ],
        'rgb_matrix_enable': True,
        'rgb_matrix_style': 'rainbow',
        'rgb_matrix_color': '#0a1aff',
        'rgb_matrix_color2': '#00ff00',
        'rgb_matrix_speed': 50,
        'rgb_matrix_brightness': 100,
        'send_email_on': [
            "low_battery",
            "power_disconnected",
            "power_restored",
            "power_insufficient",
            "battery_critical_shutdown",
            "battery_voltage_critical_shutdown",
        ],
        'send_email_to': '',
        'smtp_email': '',
        'smtp_password': '',
        'smtp_server': '',
        'smtp_port': 465,
        'smtp_security': 'ssl',
        "pipower5_buzzer_volume": 5,
        "pipower5_buzz_on": [
            "battery_activated",
            "low_battery",
            "power_disconnected",
            "power_restored",
            "power_insufficient",
            "battery_critical_shutdown",
            "battery_voltage_critical_shutdown",
        ],
        "pipower5_buzz_sequence": {
            "battery_activated": [
                ["A4", 200],  # 中等音调起始
                ["pause", 100],
                ["B4", 200]   # 小幅上升，体现激活状态
            ],
            "low_battery": [
                ["A4", 250],  # 中等音调
                ["pause", 150],
                ["A4", 250],  # 重复提醒
            ],
            "power_disconnected": [
                ["D5", 150],
                ["G4", 150],
            ],
            "power_restored": [
                ["G4", 150],
                ["D5", 150],
            ],
            "power_insufficient": [
                ["B4", 200],
                ["pause", 100],
                ["B4", 200],
                ["pause", 100],
                ["B4", 300] 
            ],
            "battery_critical_shutdown": [
                ["C6", 120],
                ["pause", 60],
                ["C6", 120],
                ["pause", 60],
                ["C6", 400],
            ],
            "battery_voltage_critical_shutdown": [
                ["C6", 120],
                ["pause", 60],
                ["C6", 120],
                ["pause", 60],
                ["C6", 400],
                ["pause", 60],
                ["C6", 400],
            ]
        },
    }
    DT_OVERLAYS = []

