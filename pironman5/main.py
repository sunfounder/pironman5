import os
import sys
import time
import threading
import signal

from app_info import __app_name__, config_file
from configparser import ConfigParser

import gpiozero # https://gpiozero.readthedocs.io/en/latest/installing.html

from PIL import Image,ImageDraw,ImageFont
from oled import SSD1306_128_64, Rect
from system_status import *
from utils import *
from ws2812_RGB import WS2812, RGB_styles

from ha_api import HA_API

ha = HA_API()

# read config
# =================================================================
fan_pin = 6
rgb_pin = 10
rgb_num = 10
update_frequency = 1  # second

temp_unit = 'C' # 'C' or 'F'
screen_always_on = True
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

oled = None
draw = None
image = None
font_8 = None
font_12 = None
fan = None
enable_fan1_control = False
cur_fan_level = 0
rgb_strip = None
cpu_temp_c = None
cpu_temp_f = None

TEMP_CONTROL_MAP = {
    '0': [50 , 0], # 'level': [min temp, level]
    '1': [50 , 1],
    '2': [60 , 2],
    '3': [67.5 , 3],
    '4': [75 , 4],
}
TEMP_HYSTERESIS = 5 # celsius

# oled init
# =================================================================

def oled_init():
    global oled, draw, image, font_8, font_12
    try:
        run_command("sudo modprobe i2c-dev")
        oled = SSD1306_128_64()
        oled.begin()
        oled.clear()
        oled.on()

        image = Image.new('1', (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        font_8 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 8)
        font_12 = ImageFont.truetype('/opt/%s/Minecraftia-Regular.ttf'%__app_name__, 12)

        log('oled init success')
    except Exception as e:
        log('oled init failed:\n%s'%e)

def draw_text(text,x,y,fill=1):
    text = str(text)
    draw.text((x, y), text=text, font=font_8, fill=fill)

def oled_display_power_off():
    if oled != None:
        oled.on()
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        # draw_text('POWER OFF',36,24)
        left, top, right, bottom = font_12.getbbox('POWER OFF')
        text_width = right - left
        text_height = bottom - top
        text_x = int((oled.width - text_width) / 2 - 1)
        text_y = int((oled.height - text_height) / 2 - 1)
        draw.text((text_x, text_y), text='POWER OFF', font=font_12, fill=1)
        oled.image(image)
        oled.display()

def handle_oled():
    ip = 'DISCONNECT'
    last_ip = 'DISCONNECT'

    if oled != None:
        # ---- oled.on() ----
        oled.on()
        # ---- get system status data ----
        # CPU usage
        cpu_usage = float(get_cpu_usage())
        # clear draw buffer
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        # RAM
        ram_info = get_ram_info()
        ram_total = round(ram_info['total'], 1)
        ram_used = round(ram_info['used'], 1)
        ram_percent = round(ram_info['percent'], 1)
        # Disk information
        disk_info = get_disk_info()
        disk_total = disk_info['total']
        disk_used = disk_info['used']
        disk_percent = disk_info['percent']

        disk_unit = 'G1'
        if disk_total >= 1000:
            disk_unit = 'T'
            disk_total = round(disk_total/1000, 3)
            disk_used = round(disk_used/1000, 3)
        elif disk_total >= 100:
            disk_unit = 'G2'

        ip = getIPAddress()

        if last_ip != ip:
            last_ip = ip
            log("Get IP: %s" %ip)

        # ---- display info ----
        ip_rect = Rect(39, 0, 88, 10)
        ram_info_rect = Rect(39, 17, 88, 10)
        ram_rect = Rect(39, 29, 88, 10)
        rom_info_rect = Rect(39, 41, 88, 10)
        rom_rect = Rect(39, 53, 88, 10)
        # cpu usage
        draw_text('CPU',6,0)
        draw.pieslice((0, 12, 30, 42), start=180, end=0, fill=0, outline=1)
        draw.pieslice((0, 12, 30, 42), start=180, end=int(180+180*cpu_usage*0.01), fill=1, outline=1)
        draw_text('{:^5.1f} %'.format(cpu_usage),2,27)
        # cpu temp
        if temp_unit == 'C':
            draw_text('{:>4.1f} \'C'.format(cpu_temp_c),2,38)
            draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
            draw.pieslice((0, 33, 30, 63), start=int(180-180*cpu_temp_c*0.01), end=180, fill=1, outline=1)
        elif temp_unit == 'F':
            draw_text('{:>4.1f} \'F'.format(cpu_temp_f),2,38)
            draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
            pcent = (cpu_temp_f-32)/1.8
            draw.pieslice((0, 33, 30, 63), start=int(180-180*pcent*0.01), end=180, fill=1, outline=1)
        # RAM
        draw_text(f'RAM:  {ram_used:^4.1f}/{ram_total:^4.1f} G',*ram_info_rect.coord())
        draw.rectangle(ram_rect.rect(), outline=1, fill=0)
        draw.rectangle(ram_rect.rect(ram_percent), outline=1, fill=1)
        # Disk
        if disk_unit == 'G1':
            _dec = 1
            if disk_used < 10:
                _dec = 2              
            draw_text(f'DISK: {disk_used:>2.{_dec}f}/{disk_total:<2.1f} G', *rom_info_rect.coord())
        elif disk_unit == 'G2':
            _dec = 0
            if disk_used < 100:
                _dec = 1
            draw_text(f'DISK: {disk_used:>3.{_dec}f}/{disk_total:<3.0f} G', *rom_info_rect.coord())
        elif disk_unit == 'T':
            draw_text(f'DISK: {disk_used:>2.2f}/{disk_total:<2.2f} T', *rom_info_rect.coord())

        draw.rectangle(rom_rect.rect(), outline=1, fill=0)
        draw.rectangle(rom_rect.rect(disk_percent), outline=1, fill=1)
        # IP
        draw.rectangle((ip_rect.x-13,ip_rect.y,ip_rect.x+ip_rect.width,ip_rect.height), outline=1, fill=1)
        draw.pieslice((ip_rect.x-25,ip_rect.y,ip_rect.x-3,ip_rect.height+10), start=270, end=0, fill=0, outline=0)
        draw_text(ip,*ip_rect.coord(),0)
        # draw the image buffer.
        oled.image(image)
        oled.display()

# fan control
# =================================================================
def fan_init():
    global fan, enable_fan1_control, cur_fan_level
    _, os_id = run_command("lsb_release -a |grep ID | awk -F ':' '{print $2}'")
    os_id = os_id.strip()
    _, os_code_name = run_command("lsb_release -a |grep Codename | awk -F ':' '{print $2}'")
    os_code_name = os_code_name.strip()

    # Systems that need to replace system pwm fan control
    # Please use all lowercase
    TEMP_CONTROL_INTERVENE_OS = [
        'ubuntu',
    ]
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

def handle_fan():
    if enable_fan1_control:
        fan1_control(cpu_temp_c)

    # get fan1 state
    fan1_state = get_fan1_state()
    # fan1_speed = get_fan1_speed()
    if (fan1_state > 0):
        fan_on()
    else:
        fan_off()



# rgb_strip init
# =================================================================

def rgb_init():
    global rgb_strip
    try:
        # rgb_strip = WS2812(LED_COUNT=rgb_num, LED_PIN=rgb_pin, LED_FREQ_HZ=rgb_freq*1000)
        rgb_strip = WS2812(LED_COUNT=rgb_num)
        log('WS2812 init success')
    except Exception as e:
        log('rgb_strip init failed:\n%s'%e)
        rgb_strip = None

    if rgb_strip != None:
        if rgb_enable:
            rgb_thread = threading.Thread(target=rgb_show)
            rgb_thread.daemon = True
            rgb_thread.start()
        else:
            rgb_strip.clear()


def rgb_show():
    try:
        if rgb_style in RGB_styles:
            log('rgb_show: %s'%rgb_style)
            rgb_strip.display(rgb_style, rgb_color, rgb_blink_speed)
        else:
            log('rgb_style not in RGB_styles')
    except Exception as e:
        log(e, level='ERROR')


# get IP
# =================================================================
def getIPAddress():
    ip = None
    if ha.is_homeassistant_addon():
        IPs = ha.get_ip()
        if len(IPs) == 0:
            IPs = getIP()
    else:
        IPs = getIP()
    # log("Got IPs: %s" %IPs)
    if 'wlan0' in IPs and IPs['wlan0'] != None and IPs['wlan0'] != '':
        ip = IPs['wlan0']
    elif 'eth0' in IPs and IPs['eth0'] != None and IPs['eth0'] != '':
        ip = IPs['eth0']
    elif 'end0' in IPs and IPs['end0'] != None and IPs['end0'] != '':
        ip = IPs['end0']
    else:
        ip = 'DISCONNECT'

    return ip


# main
# =================================================================
def main():
    global rgb_color, rgb_pin
    global cpu_temp_c, cpu_temp_f

    # close rgb
    if 'close_rgb' in sys.argv:
        log('close_rgb in sys.argv')
        if rgb_strip != None:
            log('rgb_strip clear')
            rgb_strip.clear()
        sys.exit(0)

    print_info()

    fan_init()
    oled_init()
    rgb_init()

    # ---- main loop ----
    while True:

        # ---- get CPU temperature ----
        cpu_temp_c = float(get_cpu_temperature()) # celcius
        cpu_temp_f = float(cpu_temp_c * 1.8 + 32) # fahrenheit

        handle_fan()
        handle_oled()

        # ---- delay ----
        time.sleep(update_frequency)


# exit handler
# =================================================================
def exit_handler():
    # oled off
    if oled != None:
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


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log('error')
        log(e)
    finally:
        exit_handler()


