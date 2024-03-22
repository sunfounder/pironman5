import json
import time
from pkg_resources import resource_filename

from pm_auto.pm_auto import PMAuto
from pm_dashboard.pm_dashboard import PMDashboard
from .logger import create_get_child_logger

get_child_logger = create_get_child_logger('pironman5')
__package_name__ = __name__.split('.')[0]
CONFIG_PATH = resource_filename(__package_name__, 'config.json')

PERIPHERALS = [
    'ws2812',
    'oled',
    'gpio_fan',
    'pwm_fan',
]
DEVICE_INFO = {
    'name': 'Pironman 5',
    'id': 'pironman5',
    'peripherals': PERIPHERALS,
}
AUTO_DEFAULT_CONFIG = {
    'temperature_unit': 'C',
    'rgb_led_count': 4,
    'rgb_enable': True,
    'rgb_color': '#ff00ff',
    'rgb_brightness': 100,
    'rgb_style': 'rainbow',
    'rgb_speed': 0,
    'gpio_fan_pin': 6,
}
PERIPHERALS = [
    'ws2812',
    'oled',
    'gpio_fan',
    'pwm_fan',
]
DASHBOARD_SETTINGS = {
    "database": "pironman5",
    "interval": 1,
    "spc": False,
}


def merge_dict(dict1, dict2):
    for key in dict2:
        if isinstance(dict2[key], dict):
            if key not in dict1:
                dict1[key] = {}
            merge_dict(dict1[key], dict2[key])
        elif isinstance(dict2[key], list):
            if key not in dict1:
                dict1[key] = []
            dict1[key].extend(dict2[key])
        else:
            dict1[key] = dict2[key]


class Pironman5:

    def __init__(self):
        self.log = get_child_logger('main')
        self.config = {
            'auto': AUTO_DEFAULT_CONFIG,
        }
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        merge_dict(self.config, config)

        self.pm_auto = PMAuto(self.config['auto'],
                              peripherals=PERIPHERALS,
                              get_logger=get_child_logger)
        self.pm_dashboard = PMDashboard(device_info=DEVICE_INFO,
                                        settings=DASHBOARD_SETTINGS,
                                        config=self.config,
                                        get_logger=get_child_logger)
        self.pm_dashboard.set_on_config_changed(self.update_config)

    def update_config(self, config):
        merge_dict(self.config, config)
        self.pm_auto.update_config(self.config['auto'])
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.config, f, indent=4)

    # @classmethod
    @staticmethod
    def update_config_file(config):
        current = None
        with open(CONFIG_PATH, 'r') as f:
            current = json.load(f)
        merge_dict(current, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(current, f, indent=4)

    def start(self):
        self.pm_auto.start()
        self.log.info('PMAuto started')
        self.pm_dashboard.start()
        self.log.info('PmDashboard started')
        while True:
            time.sleep(1)

    def stop(self):
        self.pm_auto.stop()
        self.pm_dashboard.stop()
