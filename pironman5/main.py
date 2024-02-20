import os
import sys
import time
import threading
import signal

from app_info import __app_name__, config_file
from configparser import ConfigParser

from oled import OLED, Rect
from system_status import *
from utils import *
from ws2812_RGB import WS2812, RGB_styles
from fan import fan_init, fan_control, fan_deinit
from api import APIServer

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

api_server = APIServer()
oled = OLED()
config = ConfigParser()

# check config_file
if not os.path.exists(config_file):
    log('Configuration file does not exist, recreating ...')
    # create config_file
    status, result = run_command(cmd=f'touch {config_file}'
        + f' && chmod 774 {config_file}'
    )
    if status != 0:
        log('create config_file failed:\n%s'%result)
        raise Exception(result)

# read config_file
try:
    config.read(config_file)
    temp_unit = config['all']['temp_unit']
    rgb_enable = config['all']['rgb_enable'] == 'True'
    rgb_num = int(config['all']['rgb_num'])
    rgb_style = str(config['all']['rgb_style'])
    rgb_color = str(config['all']['rgb_color'])
    rgb_blink_speed = int(config['all']['rgb_blink_speed'])
    rgb_freq = int(config['all']['rgb_freq'])
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

rgb_strip = None
cpu_temp_c = None
cpu_temp_f = None
last_ip = 'DISCONNECT'
rgb_changed = False

# oled init
# =================================================================
def handle_oled():
    global last_ip

    if not oled.is_ready():
        return
    
    # ---- get system status data ----
    # CPU usage
    cpu_usage = float(get_cpu_usage())
    # clear draw buffer
    oled.draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
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

    ip = get_ip()

    if last_ip != ip:
        last_ip = ip
        log("Get IP: %s" %ip)

    # ---- display info ----
    ip_rect = Rect(39, 0, 88, 10)
    ram_info_rect = Rect(39, 17, 88, 10)
    ram_rect = Rect(39, 29, 88, 10)
    rom_info_rect = Rect(39, 41, 88, 10)
    rom_rect = Rect(39, 53, 88, 10)

    oled.clear()
    # cpu usage
    oled.draw_text('CPU', 6, 0)
    oled.draw.pieslice((0, 12, 30, 42), start=180, end=0, fill=0, outline=1)
    oled.draw.pieslice((0, 12, 30, 42), start=180, end=int(180+180*cpu_usage*0.01), fill=1, outline=1)
    oled.draw_text('{:^5.1f} %'.format(cpu_usage),2,27)
    # cpu temp
    if temp_unit == 'C':
        oled.draw_text('{:>4.1f} \'C'.format(cpu_temp_c),2,38)
        oled.draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
        oled.draw.pieslice((0, 33, 30, 63), start=int(180-180*cpu_temp_c*0.01), end=180, fill=1, outline=1)
    elif temp_unit == 'F':
        oled.draw_text('{:>4.1f} \'F'.format(cpu_temp_f),2,38)
        oled.draw.pieslice((0, 33, 30, 63), start=0, end=180, fill=0, outline=1)
        pcent = (cpu_temp_f-32)/1.8
        oled.draw.pieslice((0, 33, 30, 63), start=int(180-180*pcent*0.01), end=180, fill=1, outline=1)
    # RAM
    oled.draw_text(f'RAM:  {ram_used:^4.1f}/{ram_total:^4.1f} G',*ram_info_rect.coord())
    oled.draw.rectangle(ram_rect.rect(), outline=1, fill=0)
    oled.draw.rectangle(ram_rect.rect(ram_percent), outline=1, fill=1)
    # Disk
    if disk_unit == 'G1':
        _dec = 1
        if disk_used < 10:
            _dec = 2              
        oled.draw_text(f'DISK: {disk_used:>2.{_dec}f}/{disk_total:<2.1f} G', *rom_info_rect.coord())
    elif disk_unit == 'G2':
        _dec = 0
        if disk_used < 100:
            _dec = 1
        oled.draw_text(f'DISK: {disk_used:>3.{_dec}f}/{disk_total:<3.0f} G', *rom_info_rect.coord())
    elif disk_unit == 'T':
        oled.draw_text(f'DISK: {disk_used:>2.2f}/{disk_total:<2.2f} T', *rom_info_rect.coord())

    oled.draw.rectangle(rom_rect.rect(), outline=1, fill=0)
    oled.draw.rectangle(rom_rect.rect(disk_percent), outline=1, fill=1)
    # IP
    oled.draw.rectangle((ip_rect.x-13,ip_rect.y,ip_rect.x+ip_rect.width,ip_rect.height), outline=1, fill=1)
    oled.draw.pieslice((ip_rect.x-25,ip_rect.y,ip_rect.x-3,ip_rect.height+10), start=270, end=0, fill=0, outline=0)
    oled.draw_text(ip,*ip_rect.coord(),0)
    # draw the image buffer
    oled.display()

# rgb_strip init
# =================================================================
def rgb_init():
    global rgb_strip
    try:
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

def handleConfigChanged(data):
    global rgb_enable, rgb_style, rgb_color, rgb_num, rgb_blink_speed, rgb_freq
    log(f'handleConfigChanged: {data}')
    rgb_enable = data['rgb_enable']
    rgb_style = data['rgb_style']
    rgb_color = data['rgb_color']
    rgb_num = data['rgb_num']
    rgb_blink_speed = data['rgb_speed']
    rgb_freq = data['rgb_freq']


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
    api_server.set_on_change(handleConfigChanged)
    api_server.set_config({
        'unit': temp_unit,
        'rgb_enable': rgb_enable,
        'rgb_style': rgb_style,
        'rgb_color': rgb_color,
        'rgb_num': rgb_num,
        'rgb_speed': rgb_blink_speed,
        'rgb_freq': rgb_freq,
    })

    fan_init(fan_pin)
    rgb_init()
    api_server.run()

    # ---- main loop ----
    while True:

        # ---- get CPU temperature ----
        cpu_temp_c = float(get_cpu_temperature()) # celcius
        cpu_temp_f = float(cpu_temp_c * 1.8 + 32) # fahrenheit

        fan_control(cpu_temp_c)
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
    fan_deinit() # release gpio resource
    # rgb off
    if rgb_strip != None:
        rgb_strip.clear()
        time.sleep(0.1)
    
    api_server.stop()
    log('exit')
    sys.exit(0)

def signal_handler(signo, frame):
    if signo == signal.SIGTERM or signo == signal.SIGINT:
        log("Received SIGTERM or SIGINT signal. Cleaning up...")
        exit_handler()

# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    # try:
        main()
    # except Exception as e:
    #     log(f'error: {e}')
    # finally:
    #     exit_handler()


