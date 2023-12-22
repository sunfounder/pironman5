import os
import subprocess
import shutil

'''
Use subprocess.popen instead of os.popen to avoid some errors
'''

# # Return CPU temperature as a character string
# def getCPUtemperature():
#     cmd = 'vcgencmd measure_temp'
#     try:
#         res = subprocess.check_output(cmd,shell=True).decode()
#         return(res.replace("temp=","").replace("'C\n",""))
#     except Exception as e:
#         print('getCPUtemperature: %s' %e)
#         return 0.0

# Return CPU temperature as a character string
def getCPUtemperature():
    cmd = 'cat /sys/class/thermal/thermal_zone0/temp'
    try:
        temp = int(subprocess.check_output(cmd,shell=True).decode())
        return round(temp/1000, 2)
    except Exception as e:
        print('getCPUtemperature: %s' %e)
        return 0.0

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    cmd = "free |awk 'NR==2 {print $2,$3,$4}'"
    ram = subprocess.check_output(cmd, shell=True).decode()
    return(ram.split())

# Return % of CPU used as a character string
def getCPUuse():
    # execute top twice, ignoring the first data
    cmd = "top -d 0.005 -bn2 | grep '%Cpu'| awk 'NR==2' | awk -F'ni|id' '{print $2}'"
    # might be: ",100.0 " or ",100,0 "
    try:
        
        result = subprocess.check_output(cmd,shell=True).decode().replace(' ', '').split(',')
        if len(result) == 2:
            CPU_usage = round(100 - float(result[1]),1)
        elif len(result) == 3:
            CPU_usage = round(100 - float(result[1]+'.'+result[2]),1)
        else: # error
            return 0.0
    except Exception as e:
        print('getCPUuse: %s' %e)
        return 0.0
    return CPU_usage

# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
# def getDiskSpace():
#     cmd ="df -h |grep /dev/root"
#     disk = subprocess.check_output(cmd ,shell=True).decode().replace(',', '.')
#     disk = disk.replace("G", "").replace("%", "").split()
#     return(disk[1:5])
def getDiskSpace():
    total, used, free = shutil.disk_usage("/")
    total = round(total / (2**30), 2)
    used = round(used / (2**30), 2)
    free = round(free / (2**30), 2)
    perc = int(used/ total * 100)
    return(total, used, free, perc)

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
    CPU_temp = getCPUtemperature()
    CPU_usage = getCPUuse()
    # RAM information
    # Output is in kb, here I convert it in Mb for readability
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1024,1)
    RAM_used = round(int(RAM_stats[1]) / 1024,1)
    RAM_free = round(int(RAM_stats[2]) / 1024,1)
    RAM_usage = round(RAM_used/RAM_total*100,1)
    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]
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


    print('')
    print('CPU Temperature = %s \'C' % CPU_temp)
    print('CPU Use = %s %%'%CPU_usage)
    print('')
    print('RAM Total = %s MB'%RAM_total)
    print('RAM Used = %s MB'%RAM_used)
    print('RAM Free = %s MB'%RAM_free)
    print('RAM Usage = %s %%'%RAM_usage)
    print('')
    print('DISK Total Space = %s GB'%DISK_total)
    print('DISK Used Space = %s GB'%DISK_used)
    print('DISK Used Percentage = %s %%'%DISK_perc)
    print('wlan0 : %s'%wlan0)
    print('eth0 : %s'%eth0)
    print(f'fan1_state: {fan1_state}, fan1_speed: {fan1_speed}')



