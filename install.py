#!/usr/bin/env python3

from tools.sf_installer import SF_Installer

installer = SF_Installer(
    name='pironman5',
    friendly_name='Pironman 5',

    # - Setup install command description if needed, default to "Installer for {friendly_name}""
    # description='Installer for Pironman 5',

    # - Setup venv options if needed, default to []
    venv_options=[
        '--system-site-packages',
    ],

    # - Setup Work Dir if needed, default to /opt/{name}
    # work_dir='/opt/pironman5',

    # - Setup log dir if needed, default to /var/log/{name}
    # log_dir='/var/log/pironman5',

    # - Install from apt
    apt_dependencies=[
        'influxdb',
        "libjpeg-dev", # for Pillow
        'libfreetype6-dev', # for Pillow
        # Below are for ubuntu 23 which have no spi in dev, don't know why, but 
        # according to https://forums.raspberrypi.com/viewtopic.php?t=363505#p2199981
        # this actually work, so add it here first, will find the exact package enables
        # spi later.
        'i2c-tools',
        'python3-gpiozero', # for pm_auto fan control
        # 'libblas3',
        # 'libgfortran5',
        # 'libi2c0',
        # 'liblapack3',
        # 'liblgpio1',
        # 'python3-cbor2',
        # 'python3-ftdi',
        # 'python3-lgpio',
        # 'python3-luma.core',
        # 'python3-luma.lcd',
        # 'python3-luma.oled',
        # 'python3-numpy',
        # 'python3-rpi-lgpio',
        # 'python3-serial',
        # 'python3-smbus',
        # 'python3-smbus2',
        # 'python3-usb',
        # 'read-edid',
        # 'swig',
        # 'swig4.0',
        # Stops here
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
        'pm_auto': 'git+http://github.com/sunfounder/pm_auto.git',
        'pm_dashboard': 'git+http://github.com/sunfounder/pm_dashboard.git',
        'sf_rpi_status': 'git+http://github.com/sunfounder/sf_rpi_status.git',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # add modules
    # sudo modprobe xxx
    modules = [
        "i2c-dev",
    ],

    # - Autostart settings
    # - Set service filenames
    service_files = ['pironman5.service'],
    # - Set bin files
    bin_files = ['pironman5'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = ['sunfounder-pironman5.dtbo'],
)
installer.install()
