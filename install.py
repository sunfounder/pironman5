#!/usr/bin/env python3

from tools.sf_installer import SF_Installer
from pironman5.version import __version__
from pironman5.variants import NAME, DT_OVERLAYS, PERIPHERALS

settings = {
    # - Setup venv options if needed, default to []
    'venv_options': [
        '--system-site-packages',
    ],

    # - Build required apt dependencies, default to []
    # 'build_dependencies': [
    #     'curl', # for influxdb key download
    # ],

    # - Before install scripts, default to []
    # 'run_scripts_before_install': [
    #     "install_lgpio.sh",
    # ],

    # - Install from apt
    # 'apt_dependencies': [
    # ],

    # - Install from pip
    # 'pip_dependencies': [
    #     'gpiozero',
    # ],

    # - Install python source code from git
    'python_source': {
        'pironman5': './',
        'pm_auto': 'git+https://github.com/sunfounder/pm_auto.git@1.4.1',
        'sf_rpi_status': 'git+https://github.com/sunfounder/sf_rpi_status.git@1.1.4',
    },

    # create symbolic links from venv/bin/ to /usr/local/bin/
    'symlinks':
    [
        'pironman5',
    ],

    # - Setup config txt
    # 'config_txt':  {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # add modules
    # sudo nano /etc/modules
    # 'modules': [
    #     "i2c-dev",
    # ],

    # - Autostart settings
    # - Set service filenames
    'service_files': ['pironman5.service'],
    # - Set bin files
    'bin_files': [],

    # - Copy device tree overlay to /boot/overlays
    'dtoverlays': DT_OVERLAYS,
}



ws2812_settings = {
    # - Install from pip
    'pip_dependencies': [
        'adafruit-circuitpython-neopixel-spi',
        'Adafruit-Blinka==8.59.0',
    ],
}

oled_settings = {
    # - Install from apt
    'apt_dependencies': [
        'libjpeg-dev', # for Pillow on 32 bit OS
        'libfreetype6-dev', # for Pillow on 32 bit OS
        'libopenjp2-7', # for Pillow on 32 bit OS
        'kmod',
        'i2c-tools',
    ],
    # - Install from pip
    'pip_dependencies': [
        'Pillow',
        'smbus2',
    ],
    # add modules
    # sudo nano /etc/modules
    'modules': [
        "i2c-dev",
    ],
}

gpio_settings = {
    # - Before install scripts, default to []
    'run_scripts_before_install': [
        "install_lgpio.sh",
    ],

    # - Install from apt
    'apt_dependencies': [
        'python3-gpiozero', # for pm_auto fan control
    ],
    # - Install from pip
    'pip_dependencies': [
        'gpiozero',
        'gpiod',
        'rpi.lgpio',
    ],
}

pi5_pwr_btn_settings = {
    # - Install from pip
    'pip_dependencies': [
        'evdev',
    ],
}

rgb_matrix_settings = {
    # - Install from pip
    'pip_dependencies': [
        'smbus2',
        'numpy',
    ],
}

dashboard_settings = {
    # - Build required apt dependencies, default to []
    'build_dependencies': [
        'curl', # for influxdb key download
    ],
    # - Before install scripts, default to []
    'run_scripts_before_install': [
        "setup_influxdb.sh",
    ],
    # - Install from apt
    'apt_dependencies': [
        'influxdb', # for pm_dashboard
        'lsof', # for pm_dashboard
    ],
    'python_source': {
        'pm_dashboard': 'git+https://github.com/sunfounder/pm_dashboard.git@1.3.11',
    },
}

pipower5_settings = {
    # Install python packages from source
    'python_source': {
        'pipower5': 'git+https://github.com/sunfounder/pipower5.git@1.2.1',
        'spc': 'git+https://github.com/sunfounder/spc.git',
    },
    # Add symbolic links
    'symlinks': [
        'pipower5',
    ],
    # Before install scripts, default to []
    'run_scripts_before_install': [
        "setup_pipower5.sh",
    ],
    # - Copy device tree overlay to /boot/overlays
    'dtoverlays': [
        'https://github.com/sunfounder/pipower5/raw/refs/heads/main/sunfounder-pipower5.dtbo'
    ],
}

installer = SF_Installer(
    name='pironman5',
    friendly_name=NAME,
    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for Pironman 5',
    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pironman5',
    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pironman5',
)

installer.parser.add_argument("--disable-dashboard", action='store_true', help="Disable dashboard")
installer.update_settings(settings)
args = installer.parser.parse_args()
if not args.disable_dashboard:
    installer.update_settings(dashboard_settings)
if 'oled' in PERIPHERALS:
    installer.update_settings(oled_settings)
if 'gpio_fan_state' in PERIPHERALS or \
    'vibration_switch' in PERIPHERALS:
    installer.update_settings(gpio_settings)
if 'ws2812' in PERIPHERALS:
    installer.update_settings(ws2812_settings)
if 'pi5_pwr_btn' in PERIPHERALS:
    installer.update_settings(pi5_pwr_btn_settings)
if 'rgb_matrix' in PERIPHERALS:
    installer.update_settings(rgb_matrix_settings)
if 'pipower5' in PERIPHERALS:
    installer.update_settings(pipower5_settings)
installer.main()
