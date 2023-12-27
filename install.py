#!/usr/bin/env python3
import os
import sys
import time
import threading

sys.path.append('./pironman5')
from app_info import __app_name__, __version__, username, config_file

if os.geteuid() != 0:
    print("Script must be run as root. Try 'sudo python3 install.py'")
    sys.exit(1)

errors = []

avaiable_options = ['-h', '--help', '--no-dep', '--skip-config-txt', '--skip-auto-startup', '--skip-reboot']

usage = '''
Usage:
    python3 install.py [option]

Options:
               --no-dep             Do not download dependencies
               --skip-config-txt    Skip config /boot/config.txt
               --skip-auto-startup  Skip enable auto startup
               --skip-reboot        Skip reboot after install
    -h         --help               Show this help text and exit
'''


APT_INSTALL_LIST = [
    # 'libraspberrypi-bin',
    # 'raspi-config', # http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/
    'python3-gpiozero',
    'net-tools',
    'python3-smbus2',
    'i2c-tools',
    'libtiff5-dev', # https://pillow.readthedocs.io/en/latest/installation.html
    'libopenjp2-7-dev',
    'zlib1g-dev',
    'libfreetype6-dev',
    'libpng-dev',
    'libxcb1-dev',
    'build-essential', # arm-linux-gnueabihf-gcc for pip building
    'python3-rpi.gpio',
    'python3-dev', # for RPi.GPIO, rpi-ws281x pip building
]


PIP_INSTALL_LIST = [
    # 'rpi-ws281x',
   'adafruit-circuitpython-neopixel-spi',
    # 'pillow --no-binary :all:', # https://pillow.readthedocs.io/en/latest/installation.html
    'pillow --no-cache-dir',
    'requests',
]

def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    p.wait()
    result = p.stdout.read()
    status = p.poll()
    return status, result

at_work_tip_sw = False
def working_tip():
    char = ['/', '-', '\\', '|']
    i = 0
    global at_work_tip_sw
    while at_work_tip_sw:  
            i = (i+1)%4 
            sys.stdout.write('\033[?25l') # cursor invisible
            sys.stdout.write('%s\033[1D'%char[i])
            sys.stdout.flush()
            time.sleep(0.5)

    sys.stdout.write(' \033[1D')
    sys.stdout.write('\033[?25h') # cursor visible 
    sys.stdout.flush() 

def do(msg="", cmd=""):
    print(" - %s... " % (msg), end='', flush=True)
    # at_work_tip start 
    global at_work_tip_sw
    at_work_tip_sw = True
    _thread = threading.Thread(target=working_tip)
    _thread.daemon = True
    _thread.start()
    # process run
    status, result = run_command(cmd)
    # print(status, result)
    # at_work_tip stop
    at_work_tip_sw = False
    while _thread.is_alive():
        time.sleep(0.01)
    # status
    if status == 0:
        print('Done')
    else:
        print('\033[1;35mError\033[0m')
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      (msg, status, result))

def set_config(msg="", name="", value=""):
    print(" - %s... " % (msg), end='', flush=True)
    try:
        Config().set(name, value)
        print('Done')
    except Exception as e:
        print('\033[1;35mError\033[0m')
        errors.append("%s error:\n Error:%s" %(msg, e))       

class Config(object):
    '''
        To setup /boot/config.txt (Raspbian, Kali OSMC, etc)
        /boot/firmware/config.txt (Ubuntu)
     
    '''
    DEFAULT_FILE_1 = "/boot/config.txt" # raspbian
    DEFAULT_FILE_2 = "/boot/firmware/config.txt" # ubuntu

    def __init__(self, file=None):
        # check if file exists
        if file is None:
            if os.path.exists(self.DEFAULT_FILE_1):
                self.file = self.DEFAULT_FILE_1
            elif os.path.exists(self.DEFAULT_FILE_2):
                self.file = self.DEFAULT_FILE_2
            else:
                raise FileNotFoundError(f"{self.DEFAULT_FILE_1} or {self.DEFAULT_FILE_2} are not found.")
        else:
            self.file = file
            if not os.path.exists(file):
                raise FileNotFoundError(f"{self.file} is not found.")
        # read config file
        with open(self.file, 'r') as f:
            self.configs = f.read()
        self.configs = self.configs.split('\n')

    def remove(self, expected):
        for config in self.configs:
            if expected in config:
                self.configs.remove(config)
        return self.write_file()

    def set(self, name, value=None, device="[all]"):
        '''
        device : "[all]", "[pi3]", "[pi4]" or other
        '''
        have_excepted = False
        for i in range(len(self.configs)):
            config = self.configs[i]
            if name in config:
                have_excepted = True
                tmp = name
                if value != None:
                    tmp += '=' + value
                self.configs[i] = tmp
                break

        if not have_excepted:
            self.configs.append(device)
            tmp = name
            if value != None:
                tmp += '=' + value
            self.configs.append(tmp)
        return self.write_file()

    def write_file(self):
        try:
            config = '\n'.join(self.configs)
            with open(self.file, 'w') as f:
                f.write(config)
            return 0, config
        except Exception as e:
            return -1, e


def install():
    print(f"{__app_name__} {__version__} install process starts for {username}:\n")

    # print Kernel Version
    status, result = run_command("uname -a")
    if status == 0:
        print(f"Kernel Version:\n{result}")
    # print OS Version
    status, result = run_command("lsb_release -a|grep Description")
    if status == 0:
        print(f"OS Version:\n{result}")
    # print PCB information
    status, result = run_command("cat /proc/cpuinfo|grep -E \'Revision|Model\'")
    if status == 0:
        print(f"PCB info:\n{result}")

    options = []
    if len(sys.argv) > 1:
        options = sys.argv[1:]
        for opt in options:
            if opt not in avaiable_options:
                print("Option {} is not found.".format(opt))
                print(usage)
                sys.exit(1)
        if "-h" in options or "--help" in options:
            print(usage)
            quit()
    #
    if "--no-dep" not in options:
        # update apt
        do(msg="update apt",
            cmd='apt update -y'
        )
        # check whether pip has the option "--break-system-packages"
        _is_bsps = ''
        status, _ = run_command("pip3 help install|grep break-system-packages")
        if status == 0: # if true
            _is_bsps = "--break-system-packages"
            print("pip3 install need --break-system-packages")
        # update pip
        do(msg="update pip3",
            cmd=f'python3 -m pip install --upgrade pip {_is_bsps}'
        )
        ##
        print("Install dependencies with apt-get")
        # do(msg="apt --fix-broken", # Might be stuck in a loop
        #     cmd="apt --fix-broken install -y"
        # )
        # # check & install raspi-config
        # _status, _ = run_command("raspi-config nonint")
        # if _status != 0:
        #     _link = "http://archive.raspberrypi.org/debian/pool/main/r/raspi-config/"
        #     _cmd = f"curl -s '{_link}' | grep -o '\"raspi-config.*.deb\"' |sort |tail -1"
        #     _,_last_version = run_command(_cmd)
        #     _last_version = _last_version.replace('\n', '').replace('\r', '').replace('"', ' ').strip()
        #     _link = _link + _last_version

        #     do(msg="install raspi-config",
        #         cmd="apt install lua5.1 alsa-utils triggerhappy curl -y"
        #         +f" && wget -N {_link}"
        #         +f" && dpkg -i {_last_version}"
        #         +"&& apt --fix-broken install -y"
        #     )
        #
        for dep in APT_INSTALL_LIST:
            do(msg="install %s"%dep,
                cmd='apt install %s -y'%dep)

        print("Install dependencies with pip3")
        for dep in PIP_INSTALL_LIST:
            do(msg="install %s"%dep,
                cmd=f'pip3 install {dep} {_is_bsps}')
    # 
    print("Config gpio")
    #
    if "--skip-config-txt" not in options:
        _status, _ = run_command("raspi-config nonint")
        if _status == 0:
            do(msg="enable i2c ",
                cmd='raspi-config nonint do_i2c 0'
            )
            do(msg="enable spi ",
                cmd='raspi-config nonint do_spi 0'
            )
        #
        set_config(msg="enable i2c in config",
            name="dtparam=i2c_arm",
            value="on"
        )
        set_config(msg="enable spi in config",
            name="dtparam=spi",
            value="on"
        )
        # set_config(msg="disable audio",
        #     name="dtparam=audio",
        #     value="off"
        # )
        set_config(msg="set core_freq to 500",
            name="core_freq",
            value="500"
        )
        set_config(msg="set core_freq_min to 500",
            name="core_freq_min",
            value="500"
        )     
        # dtoverlay=gpio-ir,gpio_pin=13
        set_config(msg="config gpio-ir",
            name="dtoverlay=gpio-ir,gpio_pin",
            value="13"
        )
    #
    print('create WorkingDirectory')
    do(msg="create dir",
        cmd='mkdir -p /opt/%s'%__app_name__
        +' && chmod -R 774 /opt/%s'%__app_name__
        +' && chown %s:%s /opt/%s'%(username, username, __app_name__)
    )
    #
    if "--skip-auto-startup" not in options:
        do(msg='copy service file',
            cmd='cp -rpf ./bin/%s.service /usr/lib/systemd/system/%s.service '%(__app_name__, __app_name__)
        )
        do(msg="add excutable mode for service file",
            cmd='chmod +x /usr/lib/systemd/system/%s.service'%__app_name__
        )
    do(msg='copy bin file',
        cmd='cp -rpf ./bin/%s /usr/local/bin/%s'%(__app_name__, __app_name__)
        +' && cp -rpf ./%s/* /opt/%s/'%(__app_name__, __app_name__)
    )
    do(msg="add excutable mode for bin file",
        cmd='chmod +x /usr/local/bin/%s'%__app_name__
        +' && chmod -R 774 /opt/%s'%__app_name__
        +' && chown -R %s:%s /opt/%s'%(username, username, __app_name__)
    )
    do(msg='copy config file',
        cmd=f'cp -rpf ./config.txt {config_file}'
    )
    #
    if "--skip-auto-startup" not in options:
        do(msg='enable the service to auto-start at boot',
            cmd='systemctl daemon-reload'
            + f' && systemctl enable {__app_name__}.service'
        )
    # 
    do(msg='run the service',
        cmd=f'{__app_name__} restart'
    )

    if len(errors) == 0:
        print("Finished.")
        if "--skip-reboot" not in options:
            print("\033[1;32mWhether to restart for the changes to take effect(Y/N):\033[0m")
            while True:
                key = input()
                if key == 'Y' or key == 'y':
                    print(f'reboot')
                    run_command('reboot')
                elif key == 'N' or key == 'n':
                    print(f'exit')
                    sys.exit(0)
                else:
                    continue
        else:
            print("\033[1;32mPlease reboot for the changes to take effect.\033[0m")
            sys.exit(0)
    else:
        print('\n\n\033[1;35mError happened in install process:\033[0m')
        for error in errors:
            print(error)
        print("Try to fix it yourself, or contact service@sunfounder.com with this message")
        sys.exit(1)


if __name__ == "__main__":
    try:
       install()
    except KeyboardInterrupt:
        print("\n\nCanceled.")
    finally:
        sys.stdout.write(' \033[1D')
        sys.stdout.write('\033[?25h') # cursor visible 
        sys.stdout.flush()