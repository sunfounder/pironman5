#!/usr/bin/env python3
import argparse
import sys
import time
import threading
import os


class ConfigTxt(object):
    DEFAULT_BOOT_FILE = "/boot/firmware/config.txt"
    BACKUP_BOOT_FILE = "/boot/config.txt"

    def __init__(self, file=None):
        # check if file exists
        self.__isready = True
        if file is None:
            if os.path.exists(self.DEFAULT_BOOT_FILE):
                self.file = self.DEFAULT_BOOT_FILE
            elif os.path.exists(self.BACKUP_BOOT_FILE):
                self.file = self.BACKUP_BOOT_FILE
            else:
                print("No config.txt file found.")
                self.__isready = False
                return
        else:
            self.file = file
            if not os.path.exists(file):
                print(f"config.txt not found at {file}")
                self.__isready = False
                return
        # read config file
        with open(self.file, 'r') as f:
            self.configs = f.read()
        self.configs = self.configs.split('\n')

    def isready(self):
        return self.__isready

    def remove(self, expected):
        for key in self.configs:
            if expected in key:
                self.configs.remove(key)
        return self.write_file()

    def comment(self, expected):
        for i in range(len(self.configs)):
            line = self.configs[i]
            if expected in line:
                self.configs[i] = '#' + line
        return self.write_file()

    def set(self, name, value=None, device="[all]"):
        '''
        device : "[all]", "[pi3]", "[pi4]" or other
        '''
        have_excepted = False
        for i in range(len(self.configs)):
            line = self.configs[i]
            if name in line:
                have_excepted = True
                tmp = name
                if value != None:
                    tmp += '=' + value
                if line == tmp:
                    return 1, line
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
            content = '\n'.join(self.configs)
            with open(self.file, 'w') as f:
                f.write(content)
            return 0, content
        except Exception as e:
            return -1, e


class SF_Installer():
    WORK_DIR = '/opt/{name}'
    APT_DEPENDENCIES = [
        'python3-pip',
        'python3-venv',
    ]

    PIP_DEPENDENCIES = [
        'pip',
        'setuptools',
        'build',
    ]

    def __init__(self,
                 name=None,
                 friendly_name=None,
                 description=None,
                 venv_options=[],
                 apt_dependencies=None,
                 pip_dependencies=None,
                 python_source=None,
                 work_dir=None,
                 log_dir=None,
                 config_txt=None,
                 modules=None,
                 service_files=None,
                 bin_files=None,
                 dtoverlay=None
                 ):
        if name is None:
            raise ValueError("name is required")
        if friendly_name is None:
            friendly_name = name
        if description is None:
            description = "Installer for {self._friendly_name}"
        self.name = name

        if work_dir is None:
            work_dir = self.WORK_DIR.format(name=self.name)
        if log_dir is None:
            log_dir = f'/var/log/{self.name}'

        self.friendly_name = friendly_name
        self.work_dir = work_dir
        self.log_dir = log_dir
        self.custom_apt_dependencies = apt_dependencies
        self.custom_pip_dependencies = pip_dependencies
        self.python_source = python_source
        self.config_txt = config_txt
        self.modules = modules
        self.service_files = service_files
        self.bin_files = bin_files
        self.dtoverlay = dtoverlay

        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument('--no-dep',
                                 action='store_true',
                                 help='Do not install dependencies')
        self.parser.add_argument('--skip-reboot',
                                 action='store_true',
                                 help='Skip reboot even needed')
        self.parser.add_argument('--plain-text',
                                 action='store_true',
                                 help='Plain text mode')
        if self.service_files is not None and len(self.service_files) > 0:
            self.parser.add_argument('--skip-auto-start',
                                     action='store_true',
                                     help='Skip auto start')
        if self.config_txt is not None and len(self.config_txt) > 0:
            self.parser.add_argument('--skip-config-txt',
                                     action='store_true',
                                     help='Skip config.txt')
        if self.dtoverlay is not None:
            self.parser.add_argument('--skip-dtoverlay',
                                     action='store_true',
                                     help='Skip dtoverlay')
        if self.modules is not None:
            self.parser.add_argument('--skip-modules',
                                     action='store_true',
                                     help='Skip probe modules')

        self.config_txt_handler = ConfigTxt()
        self.user = self.get_username()
        self.errors = []
        self.is_running = False
        self.need_reboot = False
        self.args = None

        self.venv_path = f'{self.work_dir}/venv'
        self.venv_python = f'{self.venv_path}/bin/python3'
        self.venv_pip = f'{self.venv_path}/bin/pip3'
        self.venv_options = venv_options
        self.custom_install = lambda: None

    def set_config(self, name="", value=""):
        msg = f"Setting config.txt: {name}={value}"
        print(" - %s... " % (msg), end='', flush=True)
        try:
            code, _ = self.config_txt_handler.set(name, value)
            if code == 0:
                self.need_reboot = True
                print('Done')
            else:
                print('Already')
        except Exception as e:
            print('\033[1;35mError\033[0m')
            self.errors.append("%s error:\n Error:%s" % (msg, e))

    def get_username(self):
        try:
            user = os.getlogin()  # can run at boot
        except:
            user = os.popen("echo ${SUDO_USER:-$(who -m | awk '{ print $1 }')}"
                            ).readline().strip()
        return user

    def run_command(self, cmd=""):
        import subprocess
        p = subprocess.Popen(cmd,
                             shell=True,
                             executable="/bin/bash",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
        p.wait()
        result = p.stdout.read()
        error = p.stderr.read()
        status = p.poll()
        return status, result, error

    def spinner(self):
        char = ['/', '-', '\\', '|']
        i = 0
        while self.is_running:
            i = (i + 1) % 4
            sys.stdout.write('\033[?25l')  # cursor invisible
            sys.stdout.write(f'{char[i]}\033[1D')
            sys.stdout.flush()
            time.sleep(0.5)

        sys.stdout.write(' \033[1D')
        sys.stdout.write('\033[?25h')  # cursor visible
        sys.stdout.flush()

    def do(self, msg="", cmd=""):
        print(f" - {msg}... ", end='', flush=True)
        if not self.args.plain_text:
            self.is_running = True
            _thread = threading.Thread(target=self.spinner)
            _thread.daemon = True
            _thread.start()
        # process run
        status, result, error = self.run_command(cmd)
        if not self.args.plain_text:
            # at_work_tip stop
            self.is_running = False
            while _thread.is_alive():
                time.sleep(0.01)
        # status
        if status == 0:
            print('Done')
        else:
            print('\033[1;35mError\033[0m')
            self.errors.append(
                f"{msg} error:\n  Command: {cmd}\n  Status: {status}\n  Result: {result}\n  Error: {error}"
            )

    # def install_python_source(self, name, url='./'):
    #     print(f'Installing {name}...')
    #     if url.startswith("http"):
    #         self.do(f'Clone package', f'git clone {url}')
    #         subdir = url.split('/')[-1].replace('.git', "")
    #     else:
    #         subdir = url
    #     self.do(f'Build package',
    #             f'cd {subdir} && {self.venv_python} -m build')
    #     self.do(f'Uninstall old package',
    #             f'{self.venv_pip} uninstall -y {name}')
    #     self.do(f'Install package',
    #             f'cd {subdir}/dist && {self.venv_pip} install *.whl')

    def install_python_source(self, name, url='./'):
        print(f'Installing {name}...')
        self.do(f'Uninstall old package',
                f'{self.venv_pip} uninstall -y {name}')
        self.do(f'Install package',
                f'{self.venv_pip} install {url}')

    def check_admin(self):
        if os.geteuid() != 0:
            print('This script must be run as root')
            sys.exit(1)

    def install_apt_dep(self):
        if not self.args.no_dep:
            self.do('Update package list', 'apt-get update')
            deps = [ *self.APT_DEPENDENCIES ]
            if self.custom_apt_dependencies is not None:
                deps += self.custom_apt_dependencies

            for dep in deps:
                self.do(f'Install {dep}', f'apt-get install -y {dep}')

    def create_working_dir(self):
        self.do('Create work directory', f'mkdir -p {self.work_dir}')
        self.do('Change work directory mode', f'chmod 777 {self.work_dir}')
        self.do('Change work directory owner', f'chown -R {self.user}:{self.user} {self.work_dir}')
        self.do('Create log directory', f'mkdir -p {self.log_dir}')
        self.do('Change log directory mode', f'chmod 777 {self.log_dir}')
        self.do('Change log directory owner', f'chown -R {self.user}:{self.user} {self.log_dir}')
        if os.path.exists(self.venv_path):
            self.do('Remove old virtual environment', f'rm -r {self.venv_path}')
        self.do('Create virtual environment', f'python3 -m venv {self.venv_path} {" ".join(self.venv_options)}')

    def install_pip_dep(self):
        if not self.args.no_dep:
            deps = [ *self.PIP_DEPENDENCIES ]
            if self.custom_pip_dependencies is not None:
                deps += self.custom_pip_dependencies

            for dep in deps:
                self.do(f'Install {dep}', f'{self.venv_pip} install --upgrade {dep}')

    def install_py_src_pkgs(self):
        for package, url in self.python_source.items():
            self.install_python_source(package, url)

    def setup_auto_start(self):
        if 'skip_auto_start' in self.args and not self.args.skip_auto_start:
            print("Setup auto start...")
            for bin in self.bin_files:
                self.do('Copy binary file', f'cp bin/{bin} /usr/local/bin/')
                self.do('Change binary file mode', f'chmod +x /usr/local/bin/{bin}')
            for service in self.service_files:
                self.do('Copy service file', f'cp bin/{service} /etc/systemd/system/')
                self.do('Enable service', f'systemctl enable {service}')
            self.do('Reload systemd', 'systemctl daemon-reload')
            self.do('Start service', f'systemctl start {service}')

    def setup_config_txt(self):
        if 'skip_config_txt' in self.args and not self.args.skip_config_txt:
            for name, value in self.config_txt.items():
                self.set_config(name, value)
            self.need_reboot = True

    def modules_probe(self):
        if 'skip_modules' in self.args and not self.args.skip_modules:
            for module in self.modules:
                self.do(f'modprobe {module}',
                    f'modprobe {module}'
                )

    def copy_dtoverlay(self):
        # Copy device tree overlay
        if self.dtoverlay is None or 'skip_dtoverlay' in self.args and self.args.skip_dtoverlay:
            return
        OVERLAY_PATH_DEFAULT = '/boot/overlays'
        OVERLAY_PATH_BACKUP = '/boot/firmware/overlays'
        overlays_path = OVERLAY_PATH_DEFAULT
        if not os.path.exists(overlays_path):
            overlays_path = OVERLAY_PATH_BACKUP
            if not os.path.exists(overlays_path):
                self.errors.append(f"Device tree overlay directory {OVERLAY_PATH_DEFAULT} or {OVERLAY_PATH_BACKUP} not found")
                return
        
        if isinstance(self.dtoverlay, str):
            self.dtoverlay = [self.dtoverlay]
        for overlay in self.dtoverlay:
            if not os.path.exists(overlay):
                self.errors.append(f"Device tree overlay file {overlay} not found")
                continue
            self.do(f'Copy dtoverlay {overlay}', f'cp {overlay} {overlays_path}/')

        self.need_reboot = True

    def change_work_dir_owner(self):
        self.do('Change work directory owner', f'chown -R {self.user}:{self.user} {self.work_dir}')

    def reboot_prompt(self):
        print("\033[1;32mWhether to restart for the changes to take effect(Y/N): \033[0m", end='')
        while True:
            key = input()
            if key == 'Y' or key == 'y':
                print(f'reboot')
                self.run_command('reboot')
            elif key == 'N' or key == 'n':
                print(f'canceled')
                return False
            else:
                continue

    def cleanup(self):
        pass
        # for package in self.python_source:
        #     url = self.python_source[package]
        #     if url.startswith("http"):
        #         self.do(f'Remove {package}', f'rm -r {package}')
        #     else:
        #         self.do(f'Remove {package} build files',
        #                 f'rm -r {url}/*.egg-info {url}/dist')

    def install(self):
        print(f"{self.friendly_name} Insataller")
        try:
            self.check_admin()
            self.args = self.parser.parse_args()

            self.install_apt_dep()
            self.create_working_dir()
            self.install_pip_dep()
            self.install_py_src_pkgs()
            self.setup_auto_start()
            self.setup_config_txt()
            self.modules_probe()
            self.copy_dtoverlay()
            self.custom_install()
            self.change_work_dir_owner()
            print("Finished")
        except KeyboardInterrupt:
            print("\n\nCanceled.")
        finally:
            sys.stdout.write(' \033[1D')
            sys.stdout.write('\033[?25h')  # cursor visible
            sys.stdout.flush()
            print('Cleanup')
            self.cleanup()
            if len(self.errors) == 0:
                if self.need_reboot and not self.args.skip_reboot:
                    self.reboot_prompt()
            else:
                print("\n\nError happened in install process:")
                for error in self.errors:
                    print(error)
                print(
                    "Try to fix it yourself, or contact service@sunfounder.com with this message"
                )
                sys.exit(1)
