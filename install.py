#!/usr/bin/env python3

from tools.sf_installer import SF_Installer
from pironman5.version import __version__
from pironman5.variants import NAME, DT_OVERLAYS

installer = SF_Installer(
    name='pironman5',
    friendly_name=NAME,

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

    # - Build required apt dependencies, default to []
    build_dependencies=[
        'curl', # for influxdb key download
    ],

    # - Before install script, default to {}
    run_commands_before_install={
        # download influxdb key and add to trusted key list https://docs.influxdata.com/influxdb/v2/install/?t=Linux
        'Download influxdb key': 'curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key',
        'Setup influxdb install source': 'echo "943666881a1b8d9b849b74caebf02d3465d6beb716510d86a39f6c8e8dac7515  influxdata-archive.key" | sha256sum --check - && cat influxdata-archive.key | gpg --dearmor | tee /etc/apt/trusted.gpg.d/influxdata-archive.gpg > /dev/null && echo "deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main" | tee /etc/apt/sources.list.d/influxdata.list',
    },

    # - Install from apt
    apt_dependencies=[
        'influxdb', # for pm_dashboard
        'lsof', # for pm_dashboard
        'libjpeg-dev', # for Pillow on 32 bit OS
        'libfreetype6-dev', # for Pillow on 32 bit OS
        'libopenjp2-7', # for Pillow on 32 bit OS
        'kmod',
        'i2c-tools',
        'python3-gpiozero', # for pm_auto fan control
    ],

    # - Install from pip
    pip_dependencies=[
        # 'influxdb',
        # 'Pillow',
        # 'adafruit-circuitpython-ssd1306',
        'gpiozero',
    ],

    # - Install python source code from git
    python_source={
        'pironman5': './',
        'pm_auto': 'git+https://github.com/sunfounder/pm_auto.git',
        'pm_dashboard': 'git+https://github.com/sunfounder/pm_dashboard.git',
        'sf_rpi_status': 'git+https://github.com/sunfounder/sf_rpi_status.git',
    },

    # - Setup config txt
    # config_txt = {
    #     'dtparam=spi': 'on',
    #     'dtparam=i2c_arm': 'on',
    #     'dtoverlay=gpio-ir,gpio_pin': '13',
    # },

    # add modules
    # sudo nano /etc/modules
    modules = [
        "i2c-dev",
    ],

    # - Autostart settings
    # - Set service filenames
    service_files = ['pironman5.service'],
    # - Set bin files
    bin_files = ['pironman5'],

    # - Copy device tree overlay to /boot/overlays
    dtoverlay = DT_OVERLAYS,
)

installer.parser.add_argument("--disable-dashboard", action='store_true', help="Disable dashboard")
args = installer.parser.parse_args()
if args.disable_dashboard:
    installer.python_source.pop('pm_dashboard')
    installer.build_dependencies.pop(installer.build_dependencies.index('curl'))
    installer.run_commands_before_install.pop(installer.run_commands_before_install.index('Download influxdb key'))
    installer.run_commands_before_install.pop(installer.run_commands_before_install.index('Setup influxdb install source'))
    installer.custom_apt_dependencies.pop(installer.custom_apt_dependencies.index('influxdb'))
    installer.custom_apt_dependencies.pop(installer.custom_apt_dependencies.index('lsof'))
installer.main()
