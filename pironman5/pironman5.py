import json
import time
import os
from importlib.resources import files as resource_files

from pm_auto.pm_auto import PMAuto
from .logger import create_get_child_logger
from .utils import merge_dict, log_error, get_hat_version
from .version import __version__

get_child_logger = create_get_child_logger('pironman5')
log = get_child_logger('main')
__package_name__ = __name__.split('.')[0]
CONFIG_PATH = str(resource_files(__package_name__).joinpath('config.json'))

PMDashboard = None
try:
    from pm_dashboard.pm_dashboard import PMDashboard
except ImportError:
    pass

PERIPHERALS = [
    'storage',
    "cpu",
    "network",
    "memory",
    "history",
    "log",
    "ws2812",
    "temperature_unit",
    "oled",
    "clear_history",
    "delete_log_file",
    "pwm_fan_speed",
    "gpio_fan_state",
    "gpio_fan_mode",
    "gpio_fan_led",
]

if get_hat_version() < 11:
    PERIPHERALS.remove('gpio_fan_led')

DEVICE_INFO = {
    'name': 'Pironman 5',
    'id': 'pironman5',
    'peripherals': PERIPHERALS,
    'version': __version__,
}

AUTO_DEFAULT_CONFIG = {
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
    'gpio_fan_led': 'follow',
    'gpio_fan_led_pin': 5,
}

DASHBOARD_SETTINGS = {
    "database": "pironman5",
    "interval": 1,
    "spc": False,
}


# This is to fix the gpiozero 2.0.1 not working on Pi 5. Try remove this patch on future releases. TODO
# try:
#     if not os.path.exists('/dev/gpiochip4'):
#         os.symlink('/dev/gpiochip0', '/dev/gpiochip4')
# except Exception:
#     log.warning('Failed to create gpiochip4 symlink')

class Pironman5:
    # @log_error
    def __init__(self):
        self.log = get_child_logger('main')
        self.config = {
            'system': AUTO_DEFAULT_CONFIG,
        }
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            self.config = self.upgrade_config(config)
            merge_dict(self.config, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.config, f, indent=4)

        self.pm_auto = PMAuto(self.config['system'],
                              peripherals=PERIPHERALS,
                              get_logger=get_child_logger)
        if PMDashboard is None:
            self.pm_dashboard = None
            self.log.warning('PM Dashboard not found skipping')
        else:
            self.pm_dashboard = PMDashboard(device_info=DEVICE_INFO,
                                            settings=DASHBOARD_SETTINGS,
                                            config=self.config,
                                            peripherals=PERIPHERALS,
                                            get_logger=get_child_logger)
            self.pm_auto.set_on_state_changed(self.pm_dashboard.update_status)
            self.pm_dashboard.set_on_config_changed(self.update_config)

    @log_error
    def set_debug_level(self, level):
        self.log.setLevel(level)
        self.pm_auto.set_debug_level(level)
        self.pm_dashboard.set_debug_level(level)

    @log_error
    def upgrade_config(self, config):
        ''' upgrade old config to new config converting 'auto' to'system' '''
        if 'auto' in config:
            return {'system': config['auto']}
        return config

    @log_error
    def update_config(self, config):
        self.pm_auto.update_config(config['system'])
        merge_dict(self.config, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.config, f, indent=4)

    @log_error
    @staticmethod
    def update_config_file(config):
        current = None
        with open(CONFIG_PATH, 'r') as f:
            current = json.load(f)
        merge_dict(current, config)
        with open(CONFIG_PATH, 'w') as f:
            json.dump(current, f, indent=4)

    @log_error
    def start(self):
        self.pm_auto.start()
        self.log.info('PMAuto started')
        if self.pm_dashboard:
            self.pm_dashboard.start()
            self.log.info('PmDashboard started')
        while True:
            time.sleep(1)

    @log_error
    def stop(self):
        self.pm_auto.stop()
        if self.pm_dashboard:
            self.pm_dashboard.stop()
