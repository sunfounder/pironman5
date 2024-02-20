import os
import subprocess
import shutil
import psutil

def get_cpu_temperature():
    return psutil.sensors_temperatures()['cpu_thermal'][0].current

def get_ram_info():
    memory_info = psutil.virtual_memory()
    memory = {
        'total': memory_info.total / 1024 / 1024 / 1024,
        'percent': memory_info.percent,
        'used': memory_info.used / 1024 / 1024 / 1024,
    }
    return memory

def get_cpu_usage():
    return psutil.cpu_percent()

# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def get_disk_info():
    total, used, free = shutil.disk_usage("/")
    disk = {
        'total': round(total / (2**30), 2),
        'used': round(used / (2**30), 2),
        'free': round(free / (2**30), 2),
        'percent': round(used/ total * 100, 2),
    }
    return(disk)


# IP address
def getIP():
    IPs = {}
    NIC_devices = []
    NIC_devices = os.listdir('/sys/class/net/')
    # print(NIC_devices)

    for NIC in NIC_devices:
        if NIC == 'lo':
            continue
        try:
            IPs[NIC] = subprocess.check_output('ifconfig ' + NIC + ' | grep "inet " | awk \'{print $2}\'', shell=True).decode().strip('\n')
        except:
            continue
        # print(NIC, IPs[NIC])

    return IPs

def getMAC():
    MACs = {}
    NIC_devices = []
    NIC_devices = os.listdir('/sys/class/net/')
    # print(NIC_devices)
    for NIC in NIC_devices:
        if NIC == 'lo':
            continue
        try:
            with open('/sys/class/net/' + NIC + '/address', 'r') as f:
                MACs[NIC] = f.readline().strip()
        except:
            continue
        # print(NIC, MACs[NIC])

    return MACs


def get_fan1_state():
    path = '/sys/class/thermal/cooling_device0/cur_state'
    try:
        with open(path, 'r') as f:
            cur_state = int(f.read())
        return cur_state
    except Exception as e:
        print(f'read fan1 state error: {e}')
        return 0

def get_fan1_speed():
    '''
    path =  '/sys/devices/platform/cooling_fan/hwmon/*/fan1_input'
    '''
    dir = '/sys/devices/platform/cooling_fan/hwmon/'
    secondary_dir = os.listdir(dir)
    path = f'{dir}/{secondary_dir[0]}/fan1_input'

    os.listdir
    try:
        with open(path, 'r') as f:
            speed = int(f.read())
        return speed
    except Exception as e:
        print(f'read fan1 speed error: {e}')
        return 0


def set_fan1_state(level: int):
    '''
    level: 0 ~ 3
    '''
    if (isinstance(level, int)):
        if level > 3:
            level = 3
        elif level < 0:
            level = 0

        cmd = f"echo '{level}' | sudo tee -a /sys/class/thermal/cooling_device0/cur_state"
        result = subprocess.check_output(cmd,shell=True)

        return result
        

if __name__ == '__main__':
    # CPU informatiom
    cpu_temp = get_cpu_temperature()
    cpu_usage = get_cpu_usage()
    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    ram_info = get_ram_info()
    ram_total = ram_info['total']
    ram_used = ram_info['used']
    ram_percent = ram_info['percent']
    # Disk information
    disk_info = get_disk_info()
    disk_total = disk_info['total']
    disk_used = disk_info['used']
    disk_percent = disk_info['percent']
    # IP
    IPs = getIP()
    wlan0 = None
    eth0 = None
    if 'wlan0' in IPs and IPs['wlan0'] != None and IPs['wlan0'] != '':
        wlan0 = IPs['wlan0']
    if 'eth0' in IPs and IPs['eth0'] != None and IPs['eth0'] != '':
        eth0 = IPs['eth0']
    # fan1
    fan1_state = get_fan1_state()
    fan1_speed = get_fan1_speed()

    print(f'CPU Temperature = {cpu_temp} \'C')
    print(f'CPU Use = {cpu_usage} %')
    print('')
    print(f'RAM Total = {ram_total} GB')
    print(f'RAM Used = {ram_used} GB')
    print(f'RAM Usage = {ram_percent} %')
    print('')
    print(f'DISK Total Space = {disk_total} GB')
    print(f'DISK Used Space = {disk_used} GB')
    print(f'DISK Used Percentage = {disk_percent} %')
    print('')
    print(f'wlan0 : {wlan0}')
    print(f'eth0 : {eth0}')
    print(f'fan1_state: {fan1_state}, fan1_speed: {fan1_speed}')
    print('')
