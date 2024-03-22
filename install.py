#!/usr/bin/env python3

from tools.sf_installer import SF_Installer

installer = SF_Installer(
    name='pironman5',
    friendly_name='Pironman 5',

    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for Pironman 5',

    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pironman5',

    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pironman5',

    # - Install from apt
    apt_dependencies=[
        'wget',
        'unzip',
        'influxdb',
        "libjpeg-dev", # for Pillow
        'libfreetype6-dev', # for Pillow
    ],

    # - Install from pip
    # pip_dependencies=[
    #     'influxdb',
    #     'Pillow',
    #     'adafruit-circuitpython-ssd1306',
    # ]

    # - Install python source code from git
    python_source={
        'pironman5': './',
        'pm_auto': 'http://github.com/sunfounder/pm_auto.git',
        'pm_dashboard': 'http://github.com/sunfounder/pm_dashboard.git',
        'sf_rpi_status': 'http://github.com/sunfounder/sf_rpi_status.git',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # - Autostart settings
    # - Set service filenames
    service_files = ['pironman5.service'],
    # - Set bin files
    bin_files = ['pironman5'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = ['sunfounder-pironman5.dtbo'],
)
installer.install()
