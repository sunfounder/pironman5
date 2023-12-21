import os


__app_name__ = 'pironman5'
__version__ = '1.0.0_beta'

try:
    username = os.getlogin() # can run at boot
except:
    username = os.popen("echo ${SUDO_USER:-$(who -m | awk '{ print $1 }')}").readline().strip()

config_file = f'/opt/{__app_name__}/config.txt'

