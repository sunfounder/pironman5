#!/usr/bin/env python3
import argparse
import subprocess
import sys
import time
import threading
import os

class SF_Installer():
    WORK_DIR = '/opt/{name}'
    DEPENDENCIES = [
        'python3-pip',
        'python3-venv',
        'python3-build',
        'influxdb',
    ]

    PIP_DEPENDENCIES = [
        'build',
    ]

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.work_dir = self.WORK_DIR.format(name=name)
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument('--no-dep', action='store_true', help='Do not install dependencies')
        self.parser.add_argument('--skip-reboot', action='store_true', help='Skip reboot even needed')
        self.parser.add_argument('--skip-auto-start', action='store_true', help='Skip auto start')
        self.parser.add_argument('--plain-text', action='store_true', help='Plain text mode')
        self.errors = []
        self.sf_packages = []
        self.is_running = False
        self.user = self.get_username()
        self.need_reboot = False

        self.venv_path = f'{self.work_dir}/venv'
        self.venv_python = f'{self.venv_path}/bin/python3'
        self.venv_pip = f'{self.venv_path}/bin/pip3'
        self.custom_install = lambda: None

    def get_username(self):
        try:
            user = os.getlogin() # can run at boot
        except:
            user = os.popen("echo ${SUDO_USER:-$(who -m | awk '{ print $1 }')}").readline().strip()
        return user

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def add_dependency(self, *args):
        for dep in args:
            self.DEPENDENCIES.append(dep)

    def add_sf_package(self, *args):
        for package in args:
            self.sf_packages.append(package)


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
                i = (i+1)%4 
                sys.stdout.write('\033[?25l') # cursor invisible
                sys.stdout.write(f'{char[i]}\033[1D')
                sys.stdout.flush()
                time.sleep(0.5)

        sys.stdout.write(' \033[1D')
        sys.stdout.write('\033[?25h') # cursor visible 
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
            self.errors.append(f"{msg} error:\n  Command: {cmd}\n  Status: {status}\n  Result: {result}\n  Error: {error}")

    def install_sf_package(self, name):
        print(f'Installing {name}...')
        self.do(f'Clone package', f'git clone https://github.com/sunfounder/{name}.git')
        self.do(f'Build package', f'cd {name} && {self.venv_python} -m build')
        self.do(f'Uninstall old package', f'{self.venv_pip} uninstall -y {name}')
        self.do(f'Install package', f'cd {name}/dist && {self.venv_pip} install *.whl')

    def check_admin(self):
        if os.geteuid() != 0:
            print('This script must be run as root')
            sys.exit(1)

    def reboot_prompt(self):
        print("\033[1;32mWhether to restart for the changes to take effect(Y/N):\033[0m")
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
        for package in self.sf_packages:
            self.do(f'Remove {package}', f'rm -rf {package}')
        self.do('Remove build files', f'rm -rf pironman5.egg-info dist')

    def _install(self):
        self.check_admin()
        self.args = self.parser.parse_args()

        if not self.args.no_dep:
            self.do('Update package list', 'apt-get update')
            for dep in self.DEPENDENCIES:
                self.do(f'Install {dep}', f'apt-get install -y {dep}')

        self.do('Create work directory', f'mkdir -p {self.work_dir}')
        self.do('Change work directory mode', f'chmod 777 {self.work_dir}')
        self.do('Change work directory owner', f'chown -R {self.user}:{self.user} {self.work_dir}')
        self.do('Create log directory', f'mkdir -p /var/log/{self.name}')
        self.do('Change log directory mode', f'chmod 777 /var/log/{self.name}')
        self.do('Change log directory owner', f'chown -R {self.user}:{self.user} /var/log/{self.name}')
        self.do('Create virtual environment', f'python3 -m venv {self.venv_path}')

        if not self.args.no_dep:
            for dep in self.PIP_DEPENDENCIES:
                self.do(f'Install {dep}', f'{self.venv_pip} install {dep}')

        for package in self.sf_packages:
            self.install_sf_package(package)

        print(f"Installing {self.name} package...")
        self.do(f'Build package', f'{self.venv_python} -m build')
        self.do(f'Uninstall old package', f'{self.venv_pip} uninstall -y {self.name}')
        self.do(f'Install package', f'{self.venv_pip} install dist/*.whl')

        if not self.args.skip_auto_start:
            print("Setup auto start...")
            self.do('Copy binary file', f'cp bin/{self.name} /usr/local/bin/')
            self.do('Change binary file mode', f'chmod +x /usr/local/bin/{self.name}')
            self.do('Copy service file', f'cp bin/{self.name}.service /etc/systemd/system/')
            self.do('Enable service', f'systemctl enable {self.name}.service')
            self.do('Reload systemd', 'systemctl daemon-reload')

        self.custom_install()

        print("Finished")

    def install(self):
        print(f"{self.name} Insataller")
        try:
            self._install()
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
                print("Try to fix it yourself, or contact service@sunfounder.com with this message")
                sys.exit(1)

DEPENDENCIES = [
    'wget',
    'unzip',
    "libjpeg-dev", # for Pillow
]
SF_PACKAGES = [
    'pm_auto',
    'pm_dashboard',
    'sf_rpi_status',
]

installer = SF_Installer('pironman5', description='Install Pironman 5')
installer.add_dependency(*DEPENDENCIES)
installer.add_sf_package(*SF_PACKAGES)

installer.install()
