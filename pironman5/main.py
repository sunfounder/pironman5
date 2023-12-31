import os
import sys
import time
import threading
import signal
import platform

from app_info import __app_name__, __version__, username, config_file
from configparser import ConfigParser

import gpiozero # https://gpiozero.readthedocs.io/en/latest/installing.html

from PIL import Image,ImageDraw,ImageFont
from oled import SSD1306_128_64
from system_status import *
from utils import *
from ws2812_RGB import WS2812, RGB_styles

from ha_api import HomeAssistantSupervisorAPI

# Check if the environment is Home Assistant
# =================================================================
NORMAL = 0
HOME_ASSISTANT_ADDON = 1

mode = NORMAL

if 'SUPERVISOR_TOKEN' in os.environ:
    mode = HOME_ASSISTANT_ADDON
    ha = HomeAssistantSupervisorAPI(
        "http://supervisor/",
        os.environ['SUPERVISOR_TOKEN']
    )
    log('Home Assistant Addon mode')

# print info
# =================================================================
line = '-'*24
_time = time.strftime("%y/%m/%d %H:%M:%S", time.localtime())
log('\n%s%s%s'%(line,_time,line), timestamp=False)
log('%s version: %s'%(__app_name__, __version__), timestamp=False)
log('username: %s'%username, timestamp=False)
log('config_file: %s'%config_file, timestamp=False)
# Kernel Version
status, result = run_command("uname -a")
if status == 0:
    log("\nKernel Version:", timestamp=False)
    log(f"{result}", timestamp=False)
# OS Version
status, result = run_command("lsb_release -a")
if status == 0:
    log("release:", timestamp=False)
    log(f"{result}", timestamp=False)
# PCB information
status, result = run_command("cat /proc/cpuinfo|grep -E \'Revision|Model\'")
if status == 0:
    log("PCB info:", timestamp=False)
    log(f"{result}", timestamp=False)

# read config
# =================================================================
power_key_pin = 16
fan_pin = 6
rgb_pin = 10
rgb_num = 10
update_frequency = 0.5  # second

temp_unit = 'C' # 'C' or 'F'
screen_always_on = True
screen_off_time = 60
rgb_enable = True
rgb_style = 'breath'  # 'breath', 'leap', 'flow', 'raise_up', 'colorful', 'colorful_leap'
rgb_color = '0a1aff'
rgb_blink_speed = 50
rgb_freq = 1000 # kHz


config = ConfigParser()
# check config_file
if not os.path.exists(config_file):
    log('Configuration file does not exist, recreating ...')
    # create config_file
    status, result = run_command(cmd=f'sudo touch {config_file}'
        + f' && sudo chmod 774 {config_file}'
    )
    if status != 0:
        log('create config_file failed:\n%s'%result)
        raise Exception(result)

# read config_file
try:
    config.read(config_file)
    temp_unit = config['all']['temp_unit']
    rgb_enable = (config['all']['rgb_enable'])
    if rgb_enable == 'False':
        rgb_enable = False
    else:
        rgb_enable = True
    rgb_num = int(config['all']['rgb_num'])
    rgb_style = str(config['all']['rgb_style'])
    rgb_color = str(config['all']['rgb_color'])
    rgb_blink_speed = int(config['all']['rgb_blink_speed'])
    rgb_freq = int(config['all']['rgb_freq'])
    rgb_pin = int(config['all']['rgb_pin'])
except Exception as e:
    log(f"read config error: {e}")
    config['all'] ={
                    'temp_unit':temp_unit,
                    'rgb_enable':rgb_enable,
                    'rgb_num': rgb_num,
                    'rgb_style':rgb_style,
                    'rgb_color':rgb_color,
                    'rgb_blink_speed':rgb_blink_speed,
                    'rgb_freq':rgb_freq,
                    'rgb_pin':rgb_pin,
                    }
    with open(config_file, 'w') as f:
        config.write(f)

log("power_key_pin : %s"%power_key_pin)
log("fan_pin : %s"%fan_pin)
log("update_frequency : %s"%update_frequency)
log("temp_unit : %s"%temp_unit)
log("rgb_enable: %s"%rgb_enable)
log("rgb_num: %s"%rgb_num)
log("rgb_style : %s"%rgb_style)
log("rgb_color : %s"%rgb_color)
log("rgb_blink_speed : %s"%rgb_blink_speed)
log("rgb_freq : %s"%rgb_freq)
log("rgb_pin : %s"%rgb_pin)
log(">>>", timestamp=False)

# oled init
# =================================================================
oled_ok = False
oled_status = False
screen_timer = 0

try:
    run_command("sudo modprobe i2c-dev")
    oled = SSD1306_128_64()
    width = oled.width
    height = oled.height
    oled.begin()
    oled.clear()
    oled.on()

    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font_8 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 8)
    font_12 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 12)

    def draw_text(text,x,y,fill=1):
        text = str(text)
        draw.text((x, y), text=text, font=font_8, fill=fill)

    oled_ok = True
    oled_status = True
    log('oled init success')
except Exception as e:
    log('oled init failed:\n%s'%e)
    oled_ok = False
    oled_status = False

def oled_display_power_off():
    if oled_ok:
        oled.on()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        # draw_text('POWER OFF',36,24)
        left, top, right, bottom = font_12.getbbox('POWER OFF')
        text_width = right - left
        text_height = bottom - top
        text_x = int((width - text_width)/2-1)
        text_y = int((height - text_height)/2-1)
        draw.text((text_x, text_y), text='POWER OFF', font=font_12, fill=1)
        oled.image(image)
        oled.display()

# fan control
# =================================================================
_, os_id = run_command("lsb_release -a |grep ID | awk -F ':' '{print $2}'")
os_id = os_id.strip()
_, os_code_name = run_command("lsb_release -a |grep Codename | awk -F ':' '{print $2}'")
os_code_name = os_code_name.strip()

# Systems that need to replace system pwm fan control
# Please use all lowercase
TEMP_CONTROL_INTERVENE_OS = [
    'ubuntu',
]
TEMP_CONTROL_MAP = {
    '0': [50 , 0], # 'level': [min temp, level]
    '1': [50 , 1],
    '2': [60 , 2],
    '3': [67.5 , 3],
    '4': [75 , 4],
}
TEMP_HYSTERESIS = 5 # celsius
cur_fan_level = 0
enable_fan1_control = False

if os_id.lower() in TEMP_CONTROL_INTERVENE_OS or os_code_name.lower() in TEMP_CONTROL_INTERVENE_OS:
    enable_fan1_control = True

fan = gpiozero.OutputDevice(fan_pin)

def fan_on():
   fan.on()

def fan_off():
   fan.off()

def fan1_control(temp):
    global cur_fan_level
    if temp < (TEMP_CONTROL_MAP[str(cur_fan_level)][0] - 5):
        cur_fan_level -= 1
        if cur_fan_level < 0:
            cur_fan_level = 0
        set_fan1_state(cur_fan_level)
    elif (cur_fan_level < 4) and (temp > TEMP_CONTROL_MAP[str(cur_fan_level+1)][0]):
        cur_fan_level += 1
        set_fan1_state(cur_fan_level)


# rgb_strip init
# =================================================================
rgb_strip = None
try:
    # rgb_strip = WS2812(LED_COUNT=rgb_num, LED_PIN=rgb_pin, LED_FREQ_HZ=rgb_freq*1000)
    rgb_strip = WS2812(LED_COUNT=rgb_num)
    log('WS2812 init success')
except Exception as e:
    log('rgb_strip init failed:\n%s'%e)
    rgb_strip = None

def rgb_show():
    try:
        if rgb_style in RGB_styles:
            log('rgb_show: %s'%rgb_style)
            rgb_strip.display(rgb_style, rgb_color, rgb_blink_speed)
        else:
            log('rgb_style not in RGB_styles')
    except Exception as e:
        log(e,level='rgb_strip')


# get IP
# =================================================================
def getIPAddress():
    ip = None
    if mode == NORMAL:
        IPs = getIP()
    elif mode == HOME_ASSISTANT_ADDON:
        IPs = ha.get_ip()
        if len(IPs) == 0:
            IPs = getIP()
    # log("Got IPs: %s" %IPs)
    if 'wlan0' in IPs and IPs['wlan0'] != None and IPs['wlan0'] != '':
        ip = IPs['wlan0']
    elif 'eth0' in IPs and IPs['eth0'] != None and IPs['eth0'] != '':
        ip = IPs['eth0']
    else:
        ip = 'DISCONNECT'

    return ip

# read rpi5 power button thread
# =================================================================
POWER_KEY_RELEASED = 0
POWER_KEY_PRESSED = 1
power_key_status = POWER_KEY_RELEASED
power_key_thread_lock = threading.Lock()
power_key_timer = 0
power_off = False

def power_key_event_loop():
    global power_key_status, power_key_timer, oled_status, screen_timer, power_off
    while True:
         # read power key with blocking
        _val = read_rpi5_power_button()
        with power_key_thread_lock:
            power_key_status = (POWER_KEY_PRESSED if _val == 1 else POWER_KEY_RELEASED)

        # if power key pressed
        if power_key_status == POWER_KEY_PRESSED:
            # oled on
            with power_key_thread_lock:
                screen_timer = 0
                oled_status = True

        time.sleep(0.02)


power_key_thread = threading.Thread(target=power_key_event_loop)
power_key_thread.daemon = True

# exit handler
# =================================================================
def exit_handler():
    # oled off
    if oled_ok:
        oled.off()
    # fan off
    fan_off()
    fan.close() # release gpio resource
    # rgb off
    if rgb_strip != None:
        rgb_strip.clear()
        time.sleep(0.1)
    sys.exit(0)

def signal_handler(signo, frame):
    if signo == signal.SIGTERM or signo == signal.SIGINT:
        log("Received SIGTERM or SIGINT signal. Cleaning up...")
        exit_handler()

# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# main
# =================================================================
def main():
    global fan_temp, power_key_pin, screen_off_time, rgb_color, rgb_pin
    global oled_status, power_key_status, power_key_timer, screen_timer, power_off

    ip = 'DISCONNECT'
    last_ip = 'DISCONNECT'

    # close rgb
    if 'close_rgb' in sys.argv:
        log('close_rgb in sys.argv')
        if rgb_strip != None:
            log('rgb_strip clear')
            rgb_strip.clear()
        sys.exit(0)
    # ---- power_key_thread start ----
    # power_key_thread.start()

    # ---- rgb_thread start ----
    if rgb_strip != None:
        if rgb_enable:
            rgb_thread = threading.Thread(target=rgb_show)
            rgb_thread.daemon = True
            rgb_thread.start()
        else:
            rgb_strip.clear()

    # ---- main loop ----
    while True:

        # ---- get CPU temperature ----
        CPU_temp_C = float(getCPUtemperature()) # celcius
        CPU_temp_F = float(CPU_temp_C * 1.8 + 32) # fahrenheit

        # ---- fan control ----
        if enable_fan1_control:
            fan1_control(CPU_temp_C)

        # get fan1 state
        fan1_state = get_fan1_state()
        # fan1_speed = get_fan1_speed()
        if (fan1_state > 0):
            fan_on()
        else:
            fan_off()

        # ---- oled control ----
        with power_key_thread_lock:
            _oled_status = oled_status
        if oled_ok and _oled_status == True:
            # ---- oled.on() ----
            if screen_timer == 0:
                screen_timer = time.time()
            oled.on()
            # ---- get system status data ----
            # CPU usage
            CPU_usage = float(getCPUuse())
            # clear draw buffer
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            # RAM
            RAM_stats = getRAMinfo()
            RAM_total = round(int(RAM_stats[0]) / 1024/1024,1)
            RAM_used = round(int(RAM_stats[1]) / 1024/1024,1)
            RAM_usage = round(RAM_used/RAM_total*100,1)
            # Disk information
            DISK_stats = getDiskSpace()
            DISK_total = DISK_stats[0]
            DISK_used = DISK_stats[1]
            DISK_perc = float(DISK_stats[3])

            DISK_unit = 'G1'
            if DISK_total >= 1000:
                DISK_unit = 'T'
                DISK_total = round(DISK_total/1000, 3)
                DISK_used = round(DISK_used/1000, 3)
            elif DISK_total >= 100:
                DISK_unit = 'G2'
  
            # get ip if disconnected
            if mode == NORMAL:
                ip = getIPAddress()
            elif mode == HOME_ASSISTANT_ADDON and ip == 'DISCONNECT':
                ip = getIPAddress()

            if last_ip != ip:
                last_ip = ip
                log("Get IP: %s" %ip)

            # ---- display info ----
            ip_rect = Rect(46, 0, 87, 10)
            ram_info_rect = Rect(45, 17, 87, 10)
            ram_rect = Rect(45, 29, 87, 10)
            rom_info_rect = Rect(45, 41, 87, 10)
            rom_rect = Rect(45, 53, 87, 10)
            # cpu usage
            draw_text('CPU',6,0)
            draw.pieslice((0, 12, 30, 42), start=180, end=0, fill=0, outline=1)
            draw.pieslice((0, 12, 30, 42), start=180, end=int(180+180*CPU_usage*0.01), fill=1, outline=1)
            draw_text('{:^5.1f} %'.format(CPU_usage),2,27)
            # cpu temp
            if temp_unit == 'C':
                draw_text('{:>4.1f} \'C'.format(CPU_temp_C),2,38)
                draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
                draw.pieslice((0, 33, 30, 63), start=int(180-180*CPU_temp_C*0.01), end=180, fill=1, outline=1)
            elif temp_unit == 'F':
                draw_text('{:>4.1f} \'F'.format(CPU_temp_F),2,38)
                draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
                pcent = (CPU_temp_F-32)/1.8
                draw.pieslice((0, 33, 30, 63), start=int(180-180*pcent*0.01), end=180, fill=1, outline=1)
            # RAM
            draw_text(f'RAM:  {RAM_used:^4.1f}/{RAM_total:^4.1f} G',*ram_info_rect.coord())
            # draw_text('{:>5.1f}'.format(RAM_usage)+' %',92,0)
            draw.rectangle(ram_rect.rect(), outline=1, fill=0)
            draw.rectangle(ram_rect.rect(RAM_usage), outline=1, fill=1)
            # Disk
            # draw_text(f'DISK:{DISK_used:^5.1f}/{DISK_total:^5.1f} {DISK_unit}', *rom_info_rect.coord())
            if DISK_unit == 'G1':
                _dec = 1
                if DISK_used < 10:
                    _dec = 2              
                draw_text(f'DISK: {DISK_used:>2.{_dec}f}/{DISK_total:<2.1f} G', *rom_info_rect.coord())
            elif DISK_unit == 'G2':
                _dec = 0
                if DISK_used < 100:
                    _dec = 1
                draw_text(f'DISK: {DISK_used:>3.{_dec}f}/{DISK_total:<3.0f} G', *rom_info_rect.coord())
            elif DISK_unit == 'T':
                draw_text(f'DISK: {DISK_used:>2.2f}/{DISK_total:<2.2f} T', *rom_info_rect.coord())

            draw.rectangle(rom_rect.rect(), outline=1, fill=0)
            draw.rectangle(rom_rect.rect(DISK_perc), outline=1, fill=1)
            # IP
            draw.rectangle((ip_rect.x-13,ip_rect.y,ip_rect.x+ip_rect.width,ip_rect.height), outline=1, fill=1)
            draw.pieslice((ip_rect.x-25,ip_rect.y,ip_rect.x-3,ip_rect.height+10), start=270, end=0, fill=0, outline=0)
            draw_text(ip,*ip_rect.coord(),0)
            # draw the image buffer.
            oled.image(image)
            oled.display()

            # ---- screen saver ----
            # screen off timer
            if screen_always_on == False:
                with power_key_thread_lock:
                    _screen_timer = screen_timer
                if (time.time()-_screen_timer) > screen_off_time:
                    oled.off()
                    with power_key_thread_lock:
                        oled_status = False


        # ---- delay ----
        time.sleep(update_frequency)


# class Rect
# =================================================================
class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

    def coord(self):
        return (self.x, self.y)
    def rect(self, pecent=100):
        return (self.x, self.y, self.x + int(self.width*pecent/100.0), self.y2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log('error')
        log(e)
    finally:
        exit_handler()


