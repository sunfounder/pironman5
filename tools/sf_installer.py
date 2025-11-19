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
        'git',
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
                work_dir=None,
                log_dir=None,):
        if name is None:
            print("Please specify a name for the software")
            sys.exit(1)
        else:
            self.name = name
        if friendly_name is None:
            self.friendly_name = name
        else:
            self.friendly_name = friendly_name
        self.description = description
        if work_dir is None:
            self.work_dir = self.WORK_DIR.format(name=self.name)
        else:
            self.work_dir = work_dir
        if log_dir is None:
            self.log_dir = f'/var/log/{self.name}'
        else:
            self.log_dir = log_dir

        self.build_dependencies = set()
        self.before_install_commands = {}
        self.custom_apt_dependencies = set()
        self.custom_pip_dependencies = set()
        self.python_source = {}
        self.config_txt = {}
        self.modules = set()
        self.service_files = set()
        self.bin_files = set()
        self.dtoverlays = set()
        self.venv_options = set()

        description = description or f'Installer for {self.friendly_name}'
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument('--uninstall', action='store_true', help='Uninstall')
        self.parser.add_argument('--gitee', action='store_true', help='Use gitee')
        self.parser.add_argument('--no-dep',
                                 action='store_true',
                                 help='Do not install dependencies')
        self.parser.add_argument('--skip-reboot',
                                 action='store_true',
                                 help='Skip reboot even needed')
        self.parser.add_argument('--plain-text',
                                 action='store_true',
                                 help='Plain text mode')
        self.parser.add_argument('--skip-auto-start',
                                    action='store_true',
                                    help='Skip auto start')
        self.parser.add_argument('--skip-config-txt',
                                    action='store_true',
                                    help='Skip config.txt')
        self.parser.add_argument('--skip-dtoverlay',
                                    action='store_true',
                                    help='Skip dtoverlay')
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
        self.custom_install = lambda: None

        self.version = self.get_version()

    def get_version(self):
        version_file = f'{self.name}/version.py'
        if os.path.exists(version_file):
            with open(version_file, 'r') as f:
                for line in f:
                    if line.startswith('__version__'):
                        return line.split('=')[1].strip().strip("'")

    def update_settings(self, settings):
        if 'build_dependencies' in settings:
            self.build_dependencies.update(settings['build_dependencies'])
        if 'run_commands_before_install' in settings:
            self.before_install_commands.update(settings['run_commands_before_install'])
        if 'apt_dependencies' in settings:
            self.custom_apt_dependencies.update(settings['apt_dependencies'])
        if 'pip_dependencies' in settings:
            self.custom_pip_dependencies.update(settings['pip_dependencies'])
        if 'python_source' in settings:
            self.python_source.update(settings['python_source'])
        if 'config_txt' in settings:
            self.config_txt.update(settings['config_txt'])
        if 'modules' in settings:
            self.modules.update(settings['modules'])
        if 'service_files' in settings:
            self.service_files.update(settings['service_files'])
        if 'bin_files' in settings:
            self.bin_files.update(settings['bin_files'])
        if 'dtoverlays' in settings:
            self.dtoverlays.update(settings['dtoverlays'])
        if 'venv_options' in settings:
            self.venv_options.update(settings['venv_options'])

    def set_friendly_name(self, name):
        self.friendly_name = name
        if self.description is None:
            self.parser.description = f'Installer for {self.friendly_name}'

    def set_config_txt(self, name="", value=""):
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

    def do(self, msg="", cmd="", ignore_error=False):
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
            if ignore_error:
                print('\033[1;35mError Ignored\033[0m')
            else:
                print('\033[1;35mError\033[0m')
                self.errors.append(
                    f"{msg} error:\n  Command: {cmd}\n  Status: {status}\n  Result: {result}\n  Error: {error}"
                )

    def check_admin(self):
        if os.geteuid() != 0:
            print('This script must be run as root')
            sys.exit(1)

    def remove_work_dir(self):
        if not os.path.exists(self.work_dir):
            print(f" - Work directory {self.work_dir} already removed Skip")
            return
        self.do('Remove work directory', f'rm -r {self.work_dir}')

    def install_python_source(self, name, url='./'):
        self.do(f'Uninstall {name} old package',
                f'{self.venv_pip} uninstall -y {name}')
        self.do(f'Install {name} from source',
                f'{self.venv_pip} install {url}')

    # Install Steps:

    def wait_for_dpkg(self):
        os.system('bash scripts/wait_for_dpkg.sh')

    def install_build_dep(self):
        print("Install build dependencies...")
        self.do('Update package list', 'apt-get update')
        deps = [ *self.APT_DEPENDENCIES ]

        if self.build_dependencies is not None:
            deps += self.build_dependencies

        deps = " ".join(deps)
        self.do(f'Install build dependencies: {deps}',
                f'DEBIAN_FRONTEND=noninteractive apt-get install -y {deps}')

    def run_commands_before_install(self):
        if len(self.before_install_commands) == 0:
            return
        print("Run commands before install...")
        for name in self.before_install_commands:
            command = self.before_install_commands[name]
            self.do(f'Run command before install: {name}', f'{command}')

    def install_apt_dep(self):
        if ('no_dep' in self.args and self.args.no_dep) or \
            len(self.custom_apt_dependencies) == 0:
            return
        print("Install APT dependencies...")
        # for dep in self.custom_apt_dependencies:
        #     self.do(f'Install {dep}', f'apt-get install -y {dep}')
        deps = " ".join(self.custom_apt_dependencies)
        self.do(f'Install APT dependencies: {deps}',
                f'apt-get install -y {deps}')

    def create_working_dir(self):
        print("Create working directory...")
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
        if ('no_dep' in self.args and self.args.no_dep) or \
            len(self.custom_pip_dependencies) == 0:
            return
        print("Install PIP dependencies...")
        deps = [ *self.PIP_DEPENDENCIES ]
        if self.custom_pip_dependencies is not None:
            deps += self.custom_pip_dependencies

        for dep in deps:
            self.do(f'Install {dep}', f'{self.venv_pip} install --upgrade {dep}')

    def install_py_src_pkgs(self):
        if len(self.python_source) == 0:
            return
        print("Install Python source packages...")
        for package, url in self.python_source.items():
            if self.args.gitee:
                url = url.replace('github.com', 'gitee.com')
            self.install_python_source(package, url)

    def setup_auto_start(self):
        if ('skip_auto_start' in self.args and self.args.skip_auto_start) or \
            (len(self.service_files) == 0 and len(self.bin_files) == 0):
            return
        print("Setup auto start...")
        for bin in self.bin_files:
            self.do('Copy binary file', f'cp bin/{bin} /usr/local/bin/')
            self.do('Change binary file mode', f'chmod +x /usr/local/bin/{bin}')
        for service in self.service_files:
            self.do('Copy service file', f'cp bin/{service} /etc/systemd/system/')
            self.do('Enable service', f'systemctl enable {service}')
            self.do('Reload systemd', 'systemctl daemon-reload')

    def setup_config_txt(self):
        if ('skip_config_txt' in self.args and self.args.skip_config_txt) or \
            len(self.config_txt) == 0:
            return
        print("Setup config.txt...")
        for name, value in self.config_txt.items():
            self.set_config_txt(name, value)
        self.need_reboot = True

    def modules_probe(self):
        if ('skip_modules' in self.args and self.args.skip_modules) or \
            len(self.modules) == 0:
            return
        print("Probe modules...")
        for module in self.modules:
            self.do(f'add module: {module}',
                f'sh -c "echo {module} >> /etc/modules-load.d/modules.conf"'
            )

    def copy_dtoverlay(self):
        # Copy device tree overlay
        if ('skip_dtoverlay' in self.args and self.args.skip_dtoverlay) or \
            len(self.dtoverlays) == 0:
            return
        print("Copy device tree overlay...")
        OVERLAY_PATH_DEFAULT = '/boot/overlays'
        OVERLAY_PATH_BACKUP = '/boot/firmware/overlays'
        overlays_path = OVERLAY_PATH_DEFAULT
        if not os.path.exists(overlays_path):
            overlays_path = OVERLAY_PATH_BACKUP
            if not os.path.exists(overlays_path):
                self.errors.append(f"Device tree overlay directory {OVERLAY_PATH_DEFAULT} or {OVERLAY_PATH_BACKUP} not found")
                return
        
        for overlay in self.dtoverlays:
            if not os.path.exists(overlay):
                self.errors.append(f"Device tree overlay file {overlay} not found")
                continue
            self.do(f'Copy dtoverlay {overlay}', f'cp {overlay} {overlays_path}/')

        self.need_reboot = True

    def change_work_dir_owner(self):
        print("Change work directory owner...")
        self.do('Change work directory owner', f'chown -R {self.user}:{self.user} {self.work_dir}')

    # Uninstall Steps:
    def remove_auto_start(self):
        if len(self.service_files) == 0 and len(self.bin_files) == 0:
            return
        print("Remove auto start...")
        for bin in self.bin_files:
            if not os.path.exists(f'/usr/local/bin/{bin}'):
                print(f" - Binary file {bin} not found Skip")
                continue
            self.do('Remove binary file', f'rm /usr/local/bin/{bin}')
        for service in self.service_files:
            if not os.path.exists(f'/etc/systemd/system/{service}'):
                print(f" - Service file {service} not found Skip")
                continue
            self.do('Stop service', f'systemctl stop {service}')
            self.do('Disable service', f'systemctl disable {service}')
            self.do('Remove service file', f'rm /etc/systemd/system/{service}')
        self.do('Reload systemd', 'systemctl daemon-reload')

    def remove_dtoverlay(self):
        if len(self.dtoverlays) == 0:
            return
        print("Remove device tree overlay...")
        OVERLAY_PATH_DEFAULT = '/boot/overlays'
        OVERLAY_PATH_BACKUP = '/boot/firmware/overlays'
        overlays_path = OVERLAY_PATH_DEFAULT
        if not os.path.exists(overlays_path):
            overlays_path = OVERLAY_PATH_BACKUP
            if not os.path.exists(overlays_path):
                self.errors.append(f"Device tree overlay directory {OVERLAY_PATH_DEFAULT} or {OVERLAY_PATH_BACKUP} not found")
                return
        
        for overlay in self.dtoverlays:
            if not os.path.exists(f'{overlays_path}/{overlay}'):
                print(f" - Device tree overlay {overlay} not found Skip")
                continue
            self.do(f'Remove dtoverlay {overlay}', f'rm {overlays_path}/{overlay}')
            self.need_reboot = True

    def remove_logs(self):
        print("Remove logs...")
        self.do('Remove logs', f'rm -r {self.log_dir}')

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
                print("\033[1;35mPlease enter Y or N: \033[0m", end='')
                continue

    def cleanup(self):
        self.do(f'Remove build', f'rm -r ./build', ignore_error=True)

    def install(self):
        print(f"Installing for {self.friendly_name}")
        print(f"Version: {self.version}")
        print(" ")
        self.wait_for_dpkg()
        self.install_build_dep()
        self.run_commands_before_install()
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

    def uninstall(self):
        print(f"Uninstall for {self.friendly_name}")
        self.remove_auto_start()
        self.remove_work_dir()
        self.remove_dtoverlay()
        self.remove_logs()

    def main(self):
        self.check_admin()
        self.args = self.parser.parse_args()
        try:
            if self.args.uninstall:
                self.uninstall()
            else:
                self.install()
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

