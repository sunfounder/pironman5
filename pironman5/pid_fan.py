import subprocess
import os
import RPi.GPIO as GPIO
import time


FAN_PWM = 6
LED_PWM = 17
fan_pwn_freq = 100
led_pwn_freq = 1

FAN_MAX = 100
FAN_MIN = 10
fan_power = 0

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
output_list = [FAN_PWM,LED_PWM]
GPIO.setup(output_list, GPIO.OUT)

fan_pwm_pin = GPIO.PWM(FAN_PWM, fan_pwn_freq)
led_pwm_pin = GPIO.PWM(LED_PWM, led_pwn_freq)
fan_pwm_pin.start(0)
led_pwm_pin.start(50)


class PID():
    def __init__(self, P=1, I=1, D=1, expect=0):
        self.P = float(P)
        self.I = float(I)
        self.D = float(D)
        self.expect = expect
        self.error = 0
        self.last_error = 0
        self.error_sum = 0

    @property
    def pval(self):
        return self.error

    @property
    def ival(self):
        self.error_sum += self.error
        return self.error_sum

    @property
    def dval(self):
        return self.error - self.last_error

    def run(self, value, mode="PID"):
        self.last_error = self.error
        self.error = value - self.expect
        # print(self.error, self.last_error, self.pval, self.P)
        result_p = self.P * self.pval
        result_i = self.I * self.ival
        result_d = self.D * self.dval
        mode = mode.upper()
        result = 0.0
        if "P" in mode:
            result += result_p
        if "I" in mode:
            result += result_i
        if "D" in mode:
            result += result_d
        return result

#run_command linux
def run_command(cmd=""):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode()
    status = p.poll()
    # print(result)
    # print(status)
    return status, result

def do(msg="", cmd=""):
    print(" - %s..." % (msg), end='\r')
    print(" - %s... " % (msg), end='')
    status, result = eval(cmd)
    # print(status, result)
    if status == 0 or status == None or result == "":
        print('Done')
    else:
        print('Error')
        errors.append("%s error:\n  Status:%s\n  Error:%s" %
                      (msg, status, result))

def cpu_temperature():          # cpu_temperature
    raw_cpu_temperature = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp") 
    cpu_temperature = round(float(raw_cpu_temperature)/1000,1)               # convert unit
    cpu_temperature = str(cpu_temperature)
    return cpu_temperature

def gpu_temperature():          # gpu_temperature(
    # raw_gpu_temperature = subprocess.getoutput( '/opt/vc/bin/vcgencmd measure_temp' )
    # gpu_temperature = round(float(raw_gpu_temperature.replace( 'temp=', '' ).replace( '\'C', '' )), 1)
    # gpu_temperature = str(gpu_temperature)
    return gpu_temperature

def cpu_usage():                # cpu_usage
    # result = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print($2)}'").readline().strip())
    result = os.popen("mpstat").read().strip()
    result = result.split('\n')[-1].split(' ')[-1]
    result = round(100 - float(result), 2)
    result = str(result)
    # print(result)
    return result

def disk_space():               # disk_space
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()         
        if i==2:
            return line.split()[1:5] 

def portable_hard_disk_info():
    disk_num = os.popen("df -h | grep '/dev/sd' -c")
    phd = os.popen("df -h | grep '/dev/sd'") 
    i = 0
    phd_line = disk_num.readline()

    line_list = []
    if int(phd_line) != 0:
        while 1:
            i = i +1
            line = phd.readline()
            line_list.append(line.split()[0:6])        
            if i==int(phd_line):
                return line_list
    else:
        return []

def ram_info():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return list(map(lambda x:round(int(x) / 1000,1), line.split()[1:4]))   

def pi_read():
    result = {
        "cpu_temperature": cpu_temperature(), 
        "gpu_temperature": gpu_temperature(),
        "cpu_usage": cpu_usage(), 
        "disk": disk_space(), 
        "ram": ram_info(), 
        # "battery": power_read(), 
    }
    return result 

# def fan_control(temp = 0):
#     if temp >=68:
#         fan_duty_cycle = round(float(temp-67)*30,1)
#         led_freq = int(temp-67)
#         if  fan_duty_cycle >= 100:
#             fan_duty_cycle = 100
        
#         fan_pwm_pin.ChangeDutyCycle(fan_duty_cycle)
#         led_pwm_pin.ChangeDutyCycle(100)  
        
#     else:
#         fan_pwm_pin.ChangeDutyCycle(0)
#         led_pwm_pin.ChangeDutyCycle(0) 

def fan_power_read():
    global fan_power
    return round(fan_power,1)



def getIP(ifaces=['wlan0', 'eth0']):
    import re
    if isinstance(ifaces, str):
        ifaces = [ifaces]
    for iface in list(ifaces):
        search_str = 'ip addr show {}'.format(iface)
        result = os.popen(search_str).read()
        com = re.compile(r'(?<=inet )(.*)(?=\/)', re.M)
        ipv4 = re.search(com, result)
        if ipv4:
            ipv4 = ipv4.groups()[0]
            return ipv4
    return False

def pid_control():
    global fan_power
    pid = PID(
        P = 0.5,
        I = 1,
        D = 1,
        expect = 40,
    )
    dc = 100
    i = 0
    while True:
        # temp = (float(cpu_temperature())+float(gpu_temperature()))/2.0
        temp = float(cpu_temperature())
        print(temp, end=' ')
        dc += pid.run(temp, mode="PD")
        dc = min(FAN_MAX, max(FAN_MIN, dc))
        fan_power = dc
        # log_temp(i, temp, dc)
        print(dc )
        fan_pwm_pin.ChangeDutyCycle(dc)
        led_pwm_pin.ChangeDutyCycle(dc)
        i += 1
        # time.sleep(1)

if __name__ == '__main__':
    # print(portable_hard_disk_info())
    pid_control()
