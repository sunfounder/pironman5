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

    SUDOER_PERMISSION = [
        "/usr/sbin/shutdown",
        "/usr/sbin/reboot",
        "/usr/sbin/poweroff",
        "/usr/sbin/halt",
        "/usr/bin/systemctl",
        "/usr/bin/vcgencmd",
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
        if description is None:
            self.description = f'Installer for {self.friendly_name}'
        else:
            self.description = description
        if work_dir is None:
            self.work_dir = self.WORK_DIR.format(name=self.name)
        else:
            self.work_dir = work_dir
        if log_dir is None:
            self.log_dir = f'/var/log/{self.name}'
        else:
            self.log_dir = log_dir
        self.log_file = f'{self.log_dir}/{self.name}.log'

        self.add_groups = set()
        self.build_dependencies = set()
        self.before_install_scripts = set()
        self.custom_apt_dependencies = set()
        self.custom_pip_dependencies = set()
        self.python_source = {}
        self.symlinks = set()
        self.config_txt = {}
        self.modules = set()
        self.service_files = set()
        self.bin_files = set()
        self.dtoverlays = set()
        self.venv_options = set()

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
        self.user = self.name
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
        if 'add_groups' in settings:
            self.add_groups.update(settings['add_groups'])
        if 'build_dependencies' in settings:
            self.build_dependencies.update(settings['build_dependencies'])
        if 'run_scripts_before_install' in settings:
            self.before_install_scripts.update(settings['run_scripts_before_install'])
        if 'apt_dependencies' in settings:
            self.custom_apt_dependencies.update(settings['apt_dependencies'])
        if 'pip_dependencies' in settings:
            self.custom_pip_dependencies.update(settings['pip_dependencies'])
        if 'python_source' in settings:
            self.python_source.update(settings['python_source'])
        if 'symlinks' in settings:
            self.symlinks.update(settings['symlinks'])
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

    def get_current_username(self):
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
        char = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        i = 0
        while self.is_running:
            i = (i + 1) % len(char)
            sys.stdout.write('\033[?25l')  # cursor invisible
            sys.stdout.write(f'\r\033[36m[{char[i]}]\033[0m')
            sys.stdout.flush()
            time.sleep(0.1)

        sys.stdout.write(' \033[1D')
        sys.stdout.write('\033[?25h')  # cursor visible
        sys.stdout.flush()

    def do(self, msg="", cmd="", ignore_error=False):
        print(f"[ ] {msg}", end='', flush=True)
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
            print(f'\r{self.SUCCESS}')
        else:
            if ignore_error:
                print(f'\r{self.SKIPPED}')
            else:
                print(f'\r{self.FAILED}')
                self.errors.append(
                    f"{self.FAILED} {msg} error:\n  Command: {cmd}\n  Status: {status}\n  Result: {result}\n  Error: {error}\n"
                )

    def print_title(self, title, end='\n', flush=False):
        if not self.args.plain_text:
            print(f"\n\033[1;34m{title}\033[0m", end=end, flush=flush)
        else:
            print(f"\n{title}", end=end, flush=flush)

    def print_error(self, msg, end='\n', flush=False):
        if self.args.plain_text:
            print(f'\r[✗] {msg}', end=end, flush=flush)
        else:
            print(f'\r\033[1;35m[✗]\033[0m {msg}', end=end, flush=flush)   

    @property
    def SUCCESS(self):
        if self.args.plain_text:
            return "[✓]"
        else:
            return "\033[32m[✓]\033[0m"

    @property
    def SKIPPED(self):
        if self.args.plain_text:
            return "[✓]"
        else:
            return "\033[1;33m[✓]\033[0m"

    @property
    def FAILED(self):
        if self.args.plain_text:
            return "[✗]"
        else:
            return "\033[1;35m[✗]\033[0m"

    def check_admin(self):
        if os.geteuid() != 0:
            self.print_error('This script must be run as root')
            sys.exit(1)

    def remove_work_dir(self):
        if not os.path.exists(self.work_dir):
            print(f"{self.SKIPPED} Work directory {self.work_dir} already removed Skip")
            return
        self.do('Remove work directory', f'rm -r {self.work_dir}')

    def install_python_source(self, name, url='./'):
        self.do(f'Uninstall {name} old package',
                f'{self.venv_pip} uninstall -y {name}')
        self.do(f'Install {name} from source',
                f'{self.venv_pip} install {url}')

    def add_user_to_group(self, user, group):
        _, users, _ = self.run_command(f'getent group {group}')
        users = users.strip().split(':')
        if user in users:
            print(f"{self.SKIPPED} User {user} already in group {group} Skip")
        else:
            self.do(f'Add user {user} to group {group}', f'usermod -aG {group} {user}')

    # Install Steps:

    def setup_user(self):
        # Create group if not exist
        if self.run_command(f'getent group {self.user}')[0] == 0:
            print(f"{self.SKIPPED} Group {self.user} already exist Skip")
        else:
            self.do(f'Create group {self.user}', f'groupadd -r {self.user}')

        # Create user if not exist
        if self.run_command(f'getent passwd {self.user}')[0] == 0:
            print(f"{self.SKIPPED} User {self.user} already exist Skip")
        else:
            self.do(f'Create user {self.user}', f'useradd -r -g {self.user} -s /sbin/nologin -d /opt/{self.user} -m {self.user}')

        # Add current user to group
        current_user = self.get_current_username()
        self.add_user_to_group(current_user, self.user)

        # Add shutdown permission to user
        self.do(f'Add shutdown permission to user {self.user}', f'echo "{self.user} ALL=(ALL) NOPASSWD: {", ".join(self.SUDOER_PERMISSION)}" | sudo tee /etc/sudoers.d/{self.user}-shutdown > /dev/null')
        self.do(f'Change sudoers file permission', f'sudo chmod 0440 /etc/sudoers.d/{self.user}-shutdown')
        self.do(f'Check sudoers file', f'sudo visudo -c -f /etc/sudoers.d/{self.user}-shutdown')

        # Add gpio group to user
        for group in self.add_groups:
            self.add_user_to_group(self.user, group)

    def wait_for_dpkg(self):
        os.system('bash scripts/wait_for_dpkg.sh')

    def install_build_dep(self):
        self.print_title("Install build dependencies...")
        self.do('Update package list', 'DEBIAN_FRONTEND=noninteractive apt-get update')
        deps = [ *self.APT_DEPENDENCIES ]

        if self.build_dependencies is not None:
            deps += self.build_dependencies

        deps = " ".join(deps)
        msg = f'Install build dependencies: {deps}'
        width = int(os.environ.get('COLUMNS', 80))
        if len(msg) > width - 3:
            msg = msg[:width-3] + '...'
        self.do(msg, f'DEBIAN_FRONTEND=noninteractive apt-get install -y {deps}')

    def run_scripts_before_install(self):
        if len(self.before_install_scripts) == 0:
            return
        self.print_title("Run scripts before install...")
        for script in self.before_install_scripts:
            self.do(f'Run scripts before install: {script}', f'bash scripts/{script}')

    def install_apt_dep(self):
        if ('no_dep' in self.args and self.args.no_dep) or \
            len(self.custom_apt_dependencies) == 0:
            return
        self.print_title("Install APT dependencies...")

        deps = " ".join(self.custom_apt_dependencies)
        msg = f'Install APT dependencies: {deps}'
        width = int(os.environ.get('COLUMNS', 80))
        if len(msg) > width-3:
            msg = msg[:width-3] + '...'
        self.do(msg, f'DEBIAN_FRONTEND=noninteractive apt-get install -y {deps}')

    def create_working_dir(self):
        self.print_title("Create working directory...")
        self.do('Create work directory', f'mkdir -p {self.work_dir}')
        self.do('Change work directory mode', f'chmod 775 {self.work_dir}')
        self.do('Change work directory owner', f'chown -R {self.user}:{self.user} {self.work_dir}')
        self.do('Create log directory', f'mkdir -p {self.log_dir}')
        self.do('Change log directory mode', f'chmod 775 {self.log_dir}')
        self.do('Change log directory owner', f'chown -R {self.user}:{self.user} {self.log_dir}')
        self.do(f'Create log file: {self.log_file}', f'touch {self.log_file}')
        self.do(f'Change log file mode to 664', f'chmod 664 {self.log_file}')
        self.do(f'Change log file owner to {self.user}', f'chown {self.user}:{self.user} {self.log_file}')
        if os.path.exists(self.venv_path):
            self.do('Remove old virtual environment', f'rm -r {self.venv_path}')
        self.do('Create virtual environment', f'python3 -m venv {self.venv_path} {" ".join(self.venv_options)}')

    def install_pip_dep(self):
        if ('no_dep' in self.args and self.args.no_dep) or \
            len(self.custom_pip_dependencies) == 0:
            return
        self.print_title("Install PIP dependencies...")
        deps = [ *self.PIP_DEPENDENCIES ]
        if self.custom_pip_dependencies is not None:
            deps += self.custom_pip_dependencies

        for dep in deps:
            self.do(f'Install {dep}', f'{self.venv_pip} install --upgrade {dep}')

    def install_py_src_pkgs(self):
        if len(self.python_source) == 0:
            return
        self.print_title("Install Python source packages...")
        for package, url in self.python_source.items():
            if self.args.gitee:
                url = url.replace('github.com', 'gitee.com')
            self.install_python_source(package, url)

    def create_symlinks(self):
        if len(self.symlinks) == 0:
            return
        self.print_title("Create symlinks...")
        for script in self.symlinks:
            self.do(f'Create symbolic link: {self.venv_path}/bin/{script} -> /usr/local/bin/{script}',
                    f'ln -s -f {self.venv_path}/bin/{script} /usr/local/bin/{script}')

    def setup_auto_start(self):
        if ('skip_auto_start' in self.args and self.args.skip_auto_start) or \
            (len(self.service_files) == 0 and len(self.bin_files) == 0):
            return
        self.print_title("Setup auto start...")
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
        self.print_title("Setup config.txt...")
        for name, value in self.config_txt.items():
            self.set_config_txt(name, value)
        self.need_reboot = True

    def modules_probe(self):
        if ('skip_modules' in self.args and self.args.skip_modules) or \
            len(self.modules) == 0:
            return
        self.print_title("Probe modules...")
        for module in self.modules:
            self.do(f'add module: {module}',
                f'sh -c "echo {module} >> /etc/modules-load.d/modules.conf"'
            )

    def copy_dtoverlay(self):
        # Copy device tree overlay
        if ('skip_dtoverlay' in self.args and self.args.skip_dtoverlay) or \
            len(self.dtoverlays) == 0:
            return
        self.print_title("Copy device tree overlay...")
        POSSIBLE_OVERLAY_PATHS = [
            '/boot/overlays',
            '/boot/firmware/overlays',
            '/boot/firmware/current/overlays',
        ]
        overlays_path = None
        for path in POSSIBLE_OVERLAY_PATHS:
            if os.path.exists(path):
                overlays_path = path
                break
        if overlays_path is None:
            self.errors.append(f"Device tree overlay directory {POSSIBLE_OVERLAY_PATHS} not found")
            return
        
        for overlay in self.dtoverlays:
            # If is online dtoverlay, download it first
            if overlay.startswith('http'):
                self.do(f'Download dtoverlay {overlay}', f'wget {overlay}')
                overlay = overlay.split('/')[-1]
                self.do(f'Move dtoverlay {overlay}', f'mv {overlay} {overlays_path}/')
            else:
                if not os.path.exists(f'overlays/{overlay}'):
                    self.errors.append(f"Device tree overlay file {overlay} not found")
                    continue
                self.do(f'Copy dtoverlay {overlay}', f'cp overlays/{overlay} {overlays_path}/')

        self.need_reboot = True

    def change_work_dir_owner(self):
        self.print_title("Fix work directory permission...")
        self.do('Add excution permission to directory', f'chmod +x {self.work_dir}')
        self.do(f'Change work directory owner to {self.user}', f'chown -R {self.user}:{self.user} {self.work_dir}')

    # Uninstall Steps:

    def remove_symlinks(self):
        if len(self.symlinks) == 0:
            return
        self.print_title("Remove symlinks...")
        for link in self.symlinks:
            self.do(f'Remove symbolic link: {link}',
                    f'rm -f /usr/local/bin/{link}')

    def uninstall_scripts(self):
        if len(self.before_install_scripts) == 0:
            return
        self.print_title("Uninstall scripts...")
        for script in self.before_install_scripts:
            self.do(f'Uninstall script: {script}', f'bash scripts/{script} --uninstall')

    def remove_auto_start(self):
        if len(self.service_files) == 0 and len(self.bin_files) == 0:
            return
        self.print_title("Remove auto start...")
        for bin in self.bin_files:
            self.do('Remove binary file', f'rm -f /usr/local/bin/{bin}')
        for service in self.service_files:
            if not os.path.exists(f'/etc/systemd/system/{service}'):
                self.errors.append(f"{self.SKIPPED} Service file {service} not found Skip")
                continue
            self.do('Stop service', f'systemctl stop {service}')
            self.do('Disable service', f'systemctl disable {service}')
            self.do('Remove service file', f'rm -f /etc/systemd/system/{service}')
        self.do('Reload systemd', 'systemctl daemon-reload')

    def remove_dtoverlay(self):
        if len(self.dtoverlays) == 0:
            return
        self.print_title("Remove device tree overlay...")
        OVERLAY_PATH_DEFAULT = '/boot/overlays'
        OVERLAY_PATH_BACKUP = '/boot/firmware/overlays'
        overlays_path = OVERLAY_PATH_DEFAULT
        if not os.path.exists(overlays_path):
            overlays_path = OVERLAY_PATH_BACKUP
            if not os.path.exists(overlays_path):
                self.errors.append(f"{self.SKIPPED} Device tree overlay directory {OVERLAY_PATH_DEFAULT} or {OVERLAY_PATH_BACKUP} not found")
                return
        
        for overlay in self.dtoverlays:
            # if it's a online dtoverlay, skip it
            if overlay.startswith('http'):
                overlay = overlay.split('/')[-1]
            if not os.path.exists(f'{overlays_path}/{overlay}'):
                self.errors.append(f"{self.SKIPPED} Device tree overlay {overlay} not found Skip")
                continue
            self.do(f'Remove dtoverlay {overlay}', f'rm {overlays_path}/{overlay}')
            self.need_reboot = True

    def remove_logs(self):
        self.print_title("Remove logs...")
        self.do('Remove logs', f'rm -rf {self.log_dir}', ignore_error=True)

    def reboot_prompt(self):
        self.print_title("Reboot to apply the changes? (Y/N): ", end='')
        while True:
            key = input()
            if key == 'Y' or key == 'y':
                self.print_title(f'Reboot')
                self.run_command('reboot')
            elif key == 'N' or key == 'n':
                self.print_title(f'Canceled')
                return False
            else:
                self.print_error("Please enter Y or N: ", end='')
                continue

    def cleanup(self):
        self.do(f'Remove build', f'rm -r ./build', ignore_error=True)

    def install(self):
        self.print_title(f"Installing {self.friendly_name} {self.version}")
        self.wait_for_dpkg()
        self.setup_user()
        self.install_build_dep()
        self.run_scripts_before_install()
        self.install_apt_dep()
        self.create_working_dir()
        self.install_pip_dep()
        self.install_py_src_pkgs()
        self.create_symlinks()
        self.setup_auto_start()
        self.setup_config_txt()
        self.modules_probe()
        self.copy_dtoverlay()
        self.custom_install()
        self.change_work_dir_owner()
        self.print_title("Finished")

    def uninstall(self):
        self.print_title(f"Uninstall for {self.friendly_name}")
        self.remove_symlinks()
        self.uninstall_scripts()
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
            self.print_title("\n\nCanceled.")
        finally:
            sys.stdout.write(' \033[1D')
            sys.stdout.write('\033[?25h')  # cursor visible
            sys.stdout.flush()
            self.print_title('Cleanup')
            self.cleanup()
            if len(self.errors) == 0:
                if self.need_reboot and not self.args.skip_reboot:
                    self.reboot_prompt()
            else:
                print(f"\n\n{self.FAILED} Error happened in install process:")
                for error in self.errors:
                    print(error)
                print(
                    "Try to fix it yourself, or contact service@sunfounder.com with this message"
                )
                sys.exit(1)

