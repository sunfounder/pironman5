#!/usr/bin/env python3
import sys
import time
import struct
from app_info import __app_name__

def log(msg:str=None,level='DEBUG',end='\n',flush=False,timestamp=True):
    with open('/opt/%s/log'%__app_name__,'a+') as log_file:
        if timestamp == True:
            _time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
            ct = time.time()
            _msecs = '%03d '%((ct - int(ct)) * 1000)
            print('%s,%s[%s] %s'%(_time,_msecs,level,msg), end=end, flush=flush, file=log_file)
            print('%s,%s[%s] %s'%(_time,_msecs,level,msg), end=end, flush=flush, file=sys.stdout)
        else:
            print('%s'%msg, end=end, flush=flush, file=log_file)
            print('%s'%msg, end=end, flush=flush, file=sys.stdout)

def run_command(cmd):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode()
    status = p.poll()
    return status, result


def read_rpi5_power_button():
    '''
    !!! This is blocking reading !!!

    command: evtest --grab /dev/input/event0

    Event type 0 (EV_SYN)
    Event type 1 (EV_KEY)
    Event code 116 (KEY_POWER)

    struct input_event {
        struct timeval time;
        unsigned short type;
        unsigned short code;
        unsigned int value;
    };
    '''
    event_file = '/dev/input/event0'
    event_format = 'llHHI'
    event_size = struct.calcsize(event_format)

    with open(event_file, 'rb') as f:
        event_data = f.read(event_size)
        _time, time_us, type, code, value = struct.unpack(event_format, event_data)
        if type == 1 and code == 116 and value == 1:
            return 1
        else:
            return 0
