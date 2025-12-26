import json
import time
import os
from importlib.resources import files as resource_files
import signal

from pm_auto.pm_auto import PMAuto
from pm_auto import __version__ as pm_auto_version
from .logger import Logger
from .utils import merge_dict, log_error
from .version import __version__ as pironman5_version
from .variants import NAME, ID, PRODUCT_VERSION, PERIPHERALS, SYSTEM_DEFAULT_CONFIG, EVENT_MAP
from ._constants import CONFIG_PATH, APP_NAME, DEFAULT_DEBUG_LEVEL

from sf_rpi_status import restart_service

log = Logger(APP_NAME)
__package_name__ = __name__.split('.')[0]

PMDashboard = None
try:
    from pm_dashboard.pm_dashboard import PMDashboard
    from pm_dashboard import __version__ as pm_dashboard_version
except ImportError:
    pass

class Pironman5:

    def __init__(self, config_path=CONFIG_PATH):
        self.peripherals = PERIPHERALS
        self.log = log

        # Load config
        # -----------------------------------------
        self.config = {
            'system': SYSTEM_DEFAULT_CONFIG,
        }
        self.config['system']['debug_level'] = DEFAULT_DEBUG_LEVEL

        self.config_path = config_path
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            config = self.upgrade_config(config)
            self.config = merge_dict(self.config, config)
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

        # Set debug level
        # -----------------------------------------
        _debug_level = self.config['system']['debug_level'].upper()
        if _debug_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            self.log.warning(f"Invalid debug level '{_debug_level}', using default '{DEFAULT_DEBUG_LEVEL}'")
            _debug_level = DEFAULT_DEBUG_LEVEL
        self.set_debug_level(_debug_level)

        # LOG HEADER
        log.info(f"")
        log.info(f"{'#'*60}")
        log.debug(f"Config path: {CONFIG_PATH}")
        log.info(f"Pironman5 Start")

        if 'enable_history' in self.config['system']:
            _p = set(self.peripherals)
            if self.config['system']['enable_history']:
                _p.add('history')
                _p.add('clear_history')
            else:
                if 'history' in _p:
                    _p.remove('history')
                if 'clear_history' in _p:
                    _p.remove('clear_history')
            self.peripherals = list(_p)

        # init PMAuto and PMDashboard
        # -----------------------------------------
        device_info = {
            'name': NAME,
            'id': ID,
            'peripherals': self.peripherals,
            'version': pironman5_version,
            'app_name': APP_NAME,
            'config_path': self.config_path,
        }
        self.log.info(f"Pironman5 version: {pironman5_version}")
        self.log.info(f"Variant: {NAME} {PRODUCT_VERSION}")

        _config_json = json.dumps(self.config, indent=4)
        self.log.info(f"Config:")
        for line in _config_json.splitlines():
            self.log.info(line)
        _device_info_json = json.dumps(device_info, indent=4)
        self.log.info(f"Device info:")
        for line in _device_info_json.splitlines():
            self.log.info(line)

        self.log.info(f"PM_Auto version: {pm_auto_version}")
        if PMDashboard is not None:
            self.log.info(f"PM_Dashboard version: {pm_dashboard_version}")

        self.pm_auto = PMAuto(self.config['system'],
                              peripherals=self.peripherals,
                              device_info=device_info,
                              event_map=EVENT_MAP,
                              log=log)
        if PMDashboard is None:
            self.pm_dashboard = None
            self.log.warning('PM Dashboard not found skipping')
        else:
            self.pm_dashboard = PMDashboard(device_info=device_info,
                                            database=ID,
                                            config=self.config,
                                            log=log)
            self.pm_dashboard.set_read_data(self.pm_auto.read)
            if 'send_email' in self.peripherals:
                self.pm_dashboard.set_test_smtp(self.pm_auto.test_smtp)
            self.pm_dashboard.set_on_config_changed(self.update_config)
            self.pm_dashboard.set_on_restart_service(restart_service)

    @log_error
    def set_debug_level(self, level):
        self.log.setLevel(level)

    @log_error
    def upgrade_config(self, config):
        ''' upgrade old config to new config converting 'auto' to'system' '''
        if 'auto' in config:
            return {'system': config['auto']}
        return config

    @log_error
    def update_config(self, config):
        patch = {}
        if 'debug_level' in config['system']:
            level = config['system']['debug_level'].upper()
            self.set_debug_level(level)
            patch['debug_level'] = level
        pm_auto_patch = self.pm_auto.update_config(config['system'])
        patch.update(pm_auto_patch)
        if len(patch) > 0:
            self.log.debug(f"Update config: {patch}")
            self.config['system'].update(patch)
            self.log.debug(f"New config: {json.dumps(self.config, indent=4)}")
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=4)

        return self.config

    @log_error
    def start(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGABRT, self.signal_handler)
        self.pm_auto.start()
        if self.pm_dashboard:
            self.pm_dashboard.start()
        while True:
            time.sleep(1)

    @log_error
    def stop(self):
        self.log.info('Stopping Pironman5')
        self.log.info('Stopping PMAuto')
        self.pm_auto.stop()
        if self.pm_dashboard:
            self.log.info('Stopping PmDashboard')
            self.pm_dashboard.stop()
        self.log.info('Pironman5 stopped')
        # Check if there's any thread still alive
        import threading
        for t in threading.enumerate():
            if t is not threading.main_thread():
                self.log.warning(f"Thread {t.name} is still alive")
        quit()

    @log_error
    def signal_handler(self, signum, frame):
        self.log.info(f'Received signal "{signal.strsignal(signum)}", cleaning up...')
        self.stop()
