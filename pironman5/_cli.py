# PYTHON_ARGCOMPLETE_OK

import argparse
import json
import sys
import os
import argcomplete
from importlib.resources import files as resource_files

from ._launch_browser import run as launch_browser
from .variants import NAME, PERIPHERALS
from .pironman5 import Pironman5
from .version import __version__
from .utils import is_included, constrain, build_effective_config

AVAILABLE_PAGES = []
AVAILABLE_EMAIL_MODES = []

def update_config_file(config, config_path):
    import json
    current = None
    with open(config_path, 'r') as f:
        current = json.load(f)
    for key in config:
        if key in current:
            current[key].update(config[key])
        else:
            current[key] = config[key]
    with open(config_path, 'w') as f:
        json.dump(current, f, indent=4)

def main():
    global AVAILABLE_PAGES, AVAILABLE_EMAIL_MODES

    TRUE_LIST = ['true', 'True', 'TRUE', '1', 'on', 'On', 'ON']
    FALSE_LIST = ['false', 'False', 'FALSE', '0', 'off', 'Off', 'OFF']

    __package_name__ = __name__.split('.')[0]
    CONFIG_PATH = "/opt/pironman5/config.json"
    PIP_PATH = "/opt/pironman5/venv/bin/pip"
    DEBUG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',\
        'debug', 'info', 'warning', 'error', 'critical']

    current_config = None
    debug_level = 'INFO'
    new_sys_config = {}

    parser = argparse.ArgumentParser(prog='pironman5',
                                    description=f'{NAME} command line interface')
    
    subparsers = parser.add_subparsers(dest="subcommand", title="Subcommands")

    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--config", action="store_true", help="Show config")
    parser.add_argument("-drd", "--database-retention-days", nargs='?', default='', help="Database retention days")
    parser.add_argument("-dl", "--debug-level", nargs='?', default='', choices=DEBUG_LEVELS, help="Debug level")
    parser.add_argument("-rd", "--remove-dashboard", action="store_true", help="Remove dashboard")
    parser.add_argument("-cp", "--config-path", nargs='?', default='', help="Config path")
    parser.add_argument("-eh", "--enable-history", nargs='?', default='', help="Enable history, True/true/on/On/1 or False/false/off/Off/0")
    # ws2812 / sf_rgb_led
    if is_included(PERIPHERALS, "ws2812") or is_included(PERIPHERALS, "sf_rgb_led"):
        from pm_auto.libs.sunfounder_rgb_led import RGB_STYLES
        parser.add_argument("-re", "--rgb-enable", nargs='?', default='', help="RGB enable True/False")
        parser.add_argument("-rs", "--rgb-style", nargs='?', default='', help=f"RGB style: {RGB_STYLES}")
        parser.add_argument("-rc", "--rgb-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rb", "--rgb-brightness", nargs='?', default='', help="RGB brightness 0-100")
        parser.add_argument("-rp", "--rgb-speed", nargs='?', default='', help="RGB speed 0-100")
        parser.add_argument("-rl", "--rgb-led-count", nargs='?', default='', help="RGB LED count int")
    # temperature_unit
    if is_included(PERIPHERALS, "temperature_unit"):
        parser.add_argument("-u", "--temperature-unit", choices=["C", "F"], nargs='?', default='', help="Temperature unit")
    # gpio_fan_mode
    if is_included(PERIPHERALS, "gpio_fan_mode"):
        from pm_auto.addons.fan import GPIO_FAN_MODES
        parser.add_argument("-gm", "--gpio-fan-mode", nargs='?', default='', help=f"GPIO fan mode, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
        parser.add_argument("-gp", "--gpio-fan-pin", nargs='?', default='', help="GPIO fan pin")
    if is_included(PERIPHERALS, "gpio_fan_led"):
        parser.add_argument("-fl", "--gpio-fan-led", nargs='?', default='', help="GPIO fan LED state on/off/follow")
        parser.add_argument("-fp", "--gpio-fan-led-pin", nargs='?', default='', help="GPIO fan LED pin")
    # oled
    if is_included(PERIPHERALS, "oled"):
        from pm_auto.addons.oled import get_available_pages
        global AVAILABLE_PAGES
        AVAILABLE_PAGES = get_available_pages(PERIPHERALS)
        parser.add_argument("-oe", "--oled-enable", nargs='?', default='', help="OLED enable True/true/on/On/1 or False/false/off/Off/0")
        parser.add_argument("-or", "--oled-rotation", nargs='?', default=-1, type=int, choices=[0, 180], help="Set to rotate OLED display, 0, 180")
        parser.add_argument("-op", "--oled-pages", nargs='?', default='', help=f"OLED pages, split by ',': {','.join(AVAILABLE_PAGES)}")
        if is_included(PERIPHERALS, "oled_sleep"):
            parser.add_argument("-os", "--oled-sleep-timeout", nargs='?', default='', help="OLED sleep timeout in seconds")
    # vibration_switch
    if is_included(PERIPHERALS, "vibration_switch"):
        parser.add_argument("-vp", "--vibration-switch-pin", nargs='?', default='', help="Vibration switch pin")
        parser.add_argument("-vu", "--vibration-switch-pull-up", nargs='?', default='', help="Vibration switch pull up True/False")
    # rgb_matrix
    if is_included(PERIPHERALS, "rgb_matrix"):
        from pm_auto.addons.rgb_matrix import EFFECT_LIST
        parser.add_argument("-rme", "--rgb-matrix-enable", nargs='?', default='', help="RGB enable True/False")
        parser.add_argument("-rms", "--rgb-matrix-style",  nargs='?', default='', help=f"RGB style: {EFFECT_LIST}")
        parser.add_argument("-rmc", "--rgb-matrix-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rmc2", "--rgb-matrix-color2", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rmp", "--rgb-matrix-speed", nargs='?', default='', help="RGB speed 0-100")
        parser.add_argument("-rmb", "--rgb-matrix-brightness", nargs='?', default='', help="RGB brightness 0-100")
    # pipower5
    if is_included(PERIPHERALS, "pipower5"):
        # 定义pipower5子命令（用于调用独立的pipower5）
        pipower_parser = subparsers.add_parser(
            "pipower5",
            add_help=False  # 禁用子命令的-h处理，确保透传
        )
    start_parser = subparsers.add_parser("start", help="Start Pironman5")
    stop_parser = subparsers.add_parser("stop", help="Stop Pironman5")
    launch_browser_parser = subparsers.add_parser("launch-browser", help="Launch browser")
    launch_browser_parser.add_argument("-a", "--auto-start", nargs='?', default='', help="Auto start browser on boot")
    update_parser = subparsers.add_parser("update", help="Update Pironman5 to latest version")
    update_parser.add_argument("--variant", nargs='?', default='', help="Override variant (base/mini/max/pro-max/ups/nas)")
    update_parser.add_argument("--pipower5", action="store_true", help="Include PiPower5 support")
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall Pironman5 completely")
    uninstall_parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompts")
    variant_parser = subparsers.add_parser("variant", help="Show or switch product variant")
    variant_parser.add_argument("variant_name", nargs="?", default=None, help="Variant name to switch to (base/mini/max/pro-max/nas)")
    variant_parser.add_argument("--list", action="store_true", help="List available variants")
    variant_parser.add_argument("--current", action="store_true", help="Show current variant")
    plugin_parser = subparsers.add_parser("plugin", help="Manage plugins (e.g. pipower5)")
    plugin_sub = plugin_parser.add_subparsers(dest="plugin_action")
    plugin_list = plugin_sub.add_parser("list", help="List installed plugins")
    plugin_install = plugin_sub.add_parser("install", help="Install a plugin")
    plugin_install.add_argument("plugin_name", help="Plugin name (e.g. pipower5)")
    plugin_remove = plugin_sub.add_parser("remove", help="Remove a plugin")
    plugin_remove.add_argument("plugin_name", help="Plugin name (e.g. pipower5)")

    argcomplete.autocomplete(parser)

    # parse args
    # -----------------------------------------------------------
    # args = parser.parse_args()
    args, remaining_args = parser.parse_known_args()

    # no args, show help
    if not (len(sys.argv) > 1):
        parser.print_help()
        quit()
    
    # show version
    # ----------------------------------------
    if args.version:
        print(__version__)
        quit()

    # get or set config path
    # ----------------------------------------
    config_path = CONFIG_PATH
    if args.config_path != '':
        if args.config_path == None:
            print(f"Config path: {config_path}")
        else:
            config_path = args.config_path
            print(f"Set config path: {config_path}")

    # load config file
    # ----------------------------------------
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({'system': {}}, f, indent=4)
        try:
            os.chmod(config_path, 0o775)
        except Exception as e:
            print(f"Failed to set permissions for config file: {e}")
    else:
        with open(config_path, 'r') as f:
            try:
                content = f.read()
                if content == '':
                    current_config = {'system': {}}
                else:
                    current_config = json.loads(content)
            except json.JSONDecodeError:
                print(f"Invalid config file: {config_path}")
                quit()

    # show config
    # ----------------------------------------
    if args.config:
        effective_config = build_effective_config(current_config)
        print(json.dumps(effective_config, indent=4))
        quit()

    # get or set debug level
    # ----------------------------------------
    if args.debug_level != '':
        if args.debug_level == None:
            print(f"Debug level: {current_config['system']['debug_level']}")
        else:
            if args.debug_level.lower() not in ['debug', 'info', 'warning', 'error', 'critical']:
                print(f"Invalid debug level, it should be one of: debug, info, warning, error, critical")
                quit()
            else:
                debug_level = args.debug_level.upper()
                new_sys_config['debug_level'] = debug_level
                print(f"Set debug level: {debug_level}")

    # Set database retention days
    # ----------------------------------------
    if args.database_retention_days != '':
        if args.database_retention_days == None:
            print(f"Database retention days: {current_config['system']['database_retention_days']}")
        else:
            try:
                database_retention_days = int(args.database_retention_days)
                new_sys_config['database_retention_days'] = database_retention_days
                print(f"Set database retention days: {database_retention_days}")
            except ValueError:
                print(f"Invalid value for database retention days, it should be a number")
                quit()

    # remove dashboard
    # ----------------------------------------    
    if args.remove_dashboard:
        print("Remove Dashboard")
        os.system(f'{PIP_PATH} uninstall pm_dashboard -y')
        while True:
            yesno = input("Do you want to uninstall influxdb? (y/n) ")
            if yesno.lower() == 'y':
                os.system(f'apt-get purge influxdb -y')
                break
            elif yesno.lower() == 'n':
                break
            else:
                print("Invalid input, please enter y or n")
        print("Dashboard removed, restart pironman5 to apply changes: sudo systemctl restart pironman5.service")
        quit()

    # swtich history
    if args.enable_history != '':
        if args.enable_history == None:
            print(f"Enable history: {current_config['system']['enable_history']}")
        else:
            if args.enable_history in TRUE_LIST:
                new_sys_config['enable_history'] = True
                print(f"Set enable history: True")
            elif args.enable_history in FALSE_LIST:
                new_sys_config['enable_history'] = False
                print(f"Set enable history: False")
            else:
                print(f"Invalid value for enable history, it should be True/true/on/On/1 or False/false/off/Off/0")
                quit()

    # ws2812 / sf_rgb_led settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "ws2812") or is_included(PERIPHERALS, "sf_rgb_led"):
        # ws2812 rgb_color
        if args.rgb_color != '':
            if args.rgb_color == None:
                hex = current_config['system']['rgb_color']
                if hex[0] == '#':
                    hex = hex[1:]
                r = int(hex[0:2], 16)
                g = int(hex[2:4], 16)
                b = int(hex[4:6], 16)
                print(f"RGB color: #{hex} ({r}, {g}, {b})")
            else:
                if len(args.rgb_color) != 6:
                    print(f'Invalid value for RGB color, it should be in hex format without # (e.g. 00aabb)')
                    quit()
                if len(args.rgb_color) == 6:
                    try:
                        r = int(args.rgb_color[0:2], 16)
                        g = int(args.rgb_color[2:4], 16)
                        b = int(args.rgb_color[4:6], 16)
                    except ValueError:
                        print(f'Invalid value for RGB color, it should be in hex format without # (e.g. 00aabb)')
                        quit()
                new_sys_config['rgb_color'] = args.rgb_color
                print(f"Set RGB color: #{args.rgb_color} ({r}, {g}, {b})")
        # ws2812 rgb_brightness
        if args.rgb_brightness != '':
            if args.rgb_brightness == None:
                print(f"RGB brightness: {current_config['system']['rgb_brightness']}")
            else:
                try:
                    args.rgb_brightness = int(args.rgb_brightness)
                except ValueError:
                    print(f"Invalid value for RGB brightness, it should be an integer between 0 and 100")
                    quit()
                if args.rgb_brightness < 0 or args.rgb_brightness > 100:
                    print(f"Invalid value for RGB brightness, it should be between 0 and 100")
                    quit()
                new_sys_config['rgb_brightness'] = args.rgb_brightness
                print(f"Set RGB brightness: {args.rgb_brightness}")
        # ws2812 rgb_style
        if args.rgb_style != '':
            if args.rgb_style == None:
                print(f"RGB style: {current_config['system']['rgb_style']}")
            else:
                if args.rgb_style not in RGB_STYLES:
                    print(f"Invalid value for RGB style, it should be one of {RGB_STYLES}")
                    quit()
                new_sys_config['rgb_style'] = args.rgb_style
                print(f"Set RGB style: {args.rgb_style}")
        # ws2812 rgb_speed
        if args.rgb_speed != '':
            if args.rgb_speed == None:
                print(f"RGB speed: {current_config['system']['rgb_speed']}")
            else:
                try:
                    args.rgb_speed = int(args.rgb_speed)
                except ValueError:
                    print(f"Invalid value for RGB speed, it should be an integer between 0 and 100")
                    quit()
                if args.rgb_speed < 0 or args.rgb_speed > 100:
                    print(f"Invalid value for RGB speed, it should be between 0 and 100")
                    quit()
                new_sys_config['rgb_speed'] = args.rgb_speed
                print(f"Set RGB speed: {args.rgb_speed}")
        # ws2812 rgb_enable
        if args.rgb_enable != '':
            if args.rgb_enable == None:
                print(f"RGB enable: {current_config['system']['rgb_enable']}")
            else:
                if args.rgb_enable in TRUE_LIST:
                    new_sys_config['rgb_enable'] = True
                    print(f"Set RGB enable: True")
                elif args.rgb_enable in FALSE_LIST:
                    new_sys_config['rgb_enable'] = False
                    print(f"Set RGB enable: False")
                else:
                    print(f"Invalid value for RGB enable, it should be True or False")
                    quit()
        # ws2812 / sf_rgb_led rgb_led_count
        if args.rgb_led_count != '':
            if args.rgb_led_count == None:
                print(f"RGB LED count: {current_config['system']['rgb_led_count']}")
            else:
                try:
                    args.rgb_led_count = int(args.rgb_led_count)
                except ValueError:
                    print(f"Invalid value for RGB LED count, it should be an integer greater than 0")
                    quit()
                if args.rgb_led_count < 1:
                    print(f"Invalid value for RGB LED count, it should be greater than 0")
                    quit()
                new_sys_config['rgb_led_count'] = args.rgb_led_count
                print(f"Set RGB LED count: {args.rgb_led_count}")

    # temperature unit settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "temperature_unit"):
        if args.temperature_unit != '':
            if args.temperature_unit == None:
                print(f"Temperature unit: {current_config['system']['temperature_unit']}")
            else:
                if args.temperature_unit not in ['C', 'F']:
                    print(f"Invalid value for Temperature unit, it should be C or F")
                    quit()
                new_sys_config['temperature_unit'] = args.temperature_unit
                print(f"Set Temperature unit: {args.temperature_unit}")

    # GPIO fan settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "gpio_fan_mode"):
        # gpio_fan_mode
        if args.gpio_fan_mode != '':
            if args.gpio_fan_mode == None:
                print(f"GPIO fan mode: {current_config['system']['gpio_fan_mode']}")
            else:
                try:
                    args.gpio_fan_mode = int(args.gpio_fan_mode)
                except ValueError:
                    print(f"Invalid value for GPIO fan mode, it should be an integer between 0 and {len(GPIO_FAN_MODES) - 1}, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
                    quit()
                if args.gpio_fan_mode < 0 or args.gpio_fan_mode >= len(GPIO_FAN_MODES):
                    print(f"Invalid value for GPIO fan mode, it should be between 0 and {len(GPIO_FAN_MODES) - 1}, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
                    quit()
                new_sys_config['gpio_fan_mode'] = args.gpio_fan_mode
                print(f"Set GPIO fan mode: {args.gpio_fan_mode}")
        # gpio_fan_pin
        if args.gpio_fan_pin != '':
            if args.gpio_fan_pin == None:
                print(f"GPIO fan pin: {current_config['system']['gpio_fan_pin']}")
            else:
                try:
                    args.gpio_fan_pin = int(args.gpio_fan_pin)
                except ValueError:
                    print(f"Invalid value for GPIO fan pin, it should be an integer")
                    quit()
                new_sys_config['gpio_fan_pin'] = args.gpio_fan_pin
                print(f"Set GPIO fan pin: {args.gpio_fan_pin}")

    # GPIO fan LED settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "gpio_fan_led"):
        if args.gpio_fan_led != '':
            if args.gpio_fan_led == None:
                print(f"GPIO fan LED state: {current_config['system']['gpio_fan_led']}")
            else:
                state = args.gpio_fan_led.lower()
                if state not in ['on', 'off', 'follow']:
                    print(f"Invalid value for GPIO fan LED state, it should be on, off or follow")
                    quit()
                new_sys_config['gpio_fan_led'] = state
                print(f"Set GPIO fan LED state: {args.gpio_fan_led}")
        if args.gpio_fan_led_pin != '':
            if args.gpio_fan_led_pin == None:
                print(f"GPIO fan LED pin: {current_config['system']['gpio_fan_led_pin']}")
            else:
                try:
                    args.gpio_fan_led_pin = int(args.gpio_fan_led_pin)
                except ValueError:
                    print(f"Invalid value for GPIO fan LED pin, it should be an integer")
                    quit()
                new_sys_config['gpio_fan_led_pin'] = args.gpio_fan_led_pin
                print(f"Set GPIO fan LED pin: {args.gpio_fan_led_pin}")

    # OLED settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "oled"):
        # oled enable
        if args.oled_enable != '':
            if args.oled_enable == None:
                print(f"OLED enable: {'enabled' if current_config['system']['oled_enable'] else 'disabled'}")
            else:
                if args.oled_enable in TRUE_LIST:                
                    new_sys_config['oled_enable'] = True
                    print(f"Set OLED enable: Enabled")
                elif args.oled_enable in FALSE_LIST:
                    new_sys_config['oled_enable'] = False
                    print(f"Set OLED enable: Disabled")
                else:
                    print(f"Invalid value for OLED enable, it should be {', '.join(TRUE_LIST)} or {', '.join(FALSE_LIST)}")
                    quit()

        # oled rotation
        if args.oled_rotation != -1:
            if args.oled_rotation == None:
                print(f"OLED rotation: {current_config['system']['oled_rotation']}")
            else:
                try:
                    args.oled_rotation = int(args.oled_rotation)
                except ValueError:
                    print(f"Invalid value for OLED rotation, it should be an integer of 0 or 180")
                    quit()
                if args.oled_rotation not in [0, 180]:
                    print(f"Invalid value for OLED rotation, it should be 0 or 180")
                    quit()
                new_sys_config['oled_rotation'] = args.oled_rotation
                print(f"SetOLED rotation: {args.oled_rotation}")
        # oled_sleep_timeout
        if args.oled_sleep_timeout != '':
            if args.oled_sleep_timeout == None:
                print(f"OLED sleep timeout: {current_config['system']['oled_sleep_timeout']}")
            else:
                from pm_auto.addons.oled import OLEDAddon
                min = OLEDAddon.MIN_SLEEP_TIMEOUT
                max = OLEDAddon.MAX_SLEEP_TIMEOUT
                try:
                    args.oled_sleep_timeout = int(args.oled_sleep_timeout)
                except ValueError:
                    print(f"Invalid value for OLED sleep timeout, it should be an integer")
                    quit()
                if args.oled_sleep_timeout < 0:
                    print(f"Invalid value for OLED sleep timeout, it should be greater than or equal to 0")
                    quit()
                oled_sleep_timeout = args.oled_sleep_timeout
                if args.oled_sleep_timeout < min or args.oled_sleep_timeout > max:
                    print(f"[WARNING] OLED sleep timeout value should be between {min} and {max}")
                    oled_sleep_timeout = constrain(oled_sleep_timeout, min, max)
                new_sys_config['oled_sleep_timeout'] = oled_sleep_timeout
                print(f"Set OLED sleep timeout: {oled_sleep_timeout}")
        # oled_pages
        if args.oled_pages != '':
            if args.oled_pages == None:
                pages = [f' - {page}' for page in current_config['system']['oled_pages']]
                pages = '\n'.join(pages)
                print("OLED pages:")
                print(pages)
            else:
                if ',' in args.oled_pages:
                    pages = args.oled_pages.split(',')
                else:
                    pages = [args.oled_pages]
                pages = [p.lower() for p in pages]
                for page in pages:
                    if page not in AVAILABLE_PAGES:
                        print(f"Invalid value for OLED pages: '{page}', it should be split by ',' and be one of {','.join(AVAILABLE_PAGES)}")
                        quit()
                new_sys_config['oled_pages'] = pages
                print(f"Set OLED pages: {pages}")

    # Vibration switch settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "vibration_switch"):
        # vibration_switch_pin
        if args.vibration_switch_pin != '':
            if args.vibration_switch_pin == None:
                print(f"Vibration switch pin: {current_config['system']['vibration_switch_pin']}")
            else:
                try:
                    pin = int(args.vibration_switch_pin)
                except ValueError:
                    print(f"Invalid value for Vibration switch pin, it should be an integer")
                    quit()
                if pin < 0 or pin > 40:
                    print(f"Invalid value for Vibration switch pin, it should be between 0 and 40")
                    quit()
                new_sys_config['vibration_switch_pin'] = pin
                print(f"Set Vibration switch pin: {pin}")
        # vibration_switch_pull_up
        if args.vibration_switch_pull_up != '':
            if args.vibration_switch_pull_up == None:
                print(f"Vibration switch pull up: {current_config['system']['vibration_switch_pull_up']}")
            else:
                if args.vibration_switch_pull_up in TRUE_LIST:
                    new_sys_config['vibration_switch_pull_up'] = True
                    print(f"Set Vibration switch pull up: True")
                elif args.vibration_switch_pull_up in FALSE_LIST:
                    new_sys_config['vibration_switch_pull_up'] = False
                    print(f"Set Vibration switch pull up: False")
                else:
                    print(f"Invalid value for Vibration switch pull up, it should be {', '.join(TRUE_LIST)} or {', '.join(FALSE_LIST)}")
                    quit()

    # RGB matrix settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "rgb_matrix"):
        # rgb_matrix_enable
        if args.rgb_matrix_enable != '':
            if args.rgb_matrix_enable == None:
                print(f"RGB Matrix enable: {current_config['system']['rgb_matrix_enable']}")
            else:
                if args.rgb_matrix_enable in TRUE_LIST:
                    new_sys_config['rgb_matrix_enable'] = True
                    print(f"Set RGB Matrix enable: True")
                elif args.rgb_matrix_enable in FALSE_LIST:
                    new_sys_config['rgb_matrix_enable'] = False
                    print(f"Set RGB Matrix enable: False")
                else:
                    print(f"Invalid value for RGB Matrix enable, it should be True or False")
                    quit()
        # rgb_matrix_style
        if args.rgb_matrix_style != '':
            if args.rgb_matrix_style == None:
                print(f"RGB Matrix style: {current_config['system']['rgb_matrix_style']}")
            else:
                if args.rgb_matrix_style not in EFFECT_LIST:
                    print(f"Invalid value for RGB Matrix style: {args.rgb_matrix_style}, it should be one of {EFFECT_LIST}")
                    quit()
                new_sys_config['rgb_matrix_style'] = args.rgb_matrix_style
                print(f"Set RGB Matrix style: {args.rgb_matrix_style}")
        # rgb_matrix_speed
        if args.rgb_matrix_speed != '':
            if args.rgb_matrix_speed == None:
                print(f"RGB Matrix speed: {current_config['system']['rgb_matrix_speed']}")
            else:
                try:
                    args.rgb_matrix_speed = int(args.rgb_matrix_speed)
                except ValueError:
                    print(f"Invalid value for RGB Matrix speed, it should be an integer between 0 and 100")
                    quit()
                if args.rgb_matrix_speed < 0 or args.rgb_matrix_speed > 100:
                    print(f"Invalid value for RGB Matrix speed, it should be between 0 and 100")
                    quit()
                new_sys_config['rgb_matrix_speed'] = args.rgb_matrix_speed
                print(f"Set RGB Matrix speed: {args.rgb_matrix_speed}")
        # rgb_matrix_brightness
        if args.rgb_matrix_brightness != '':
            if args.rgb_matrix_brightness == None:
                print(f"RGB Matrix brightness: {current_config['system']['rgb_matrix_brightness']}")
            else:
                try:
                    args.rgb_matrix_brightness = int(args.rgb_matrix_brightness)
                except ValueError:
                    print(f"Invalid value for RGB Matrix brightness, it should be an integer between 0 and 100")
                    quit()
                if args.rgb_matrix_brightness < 0 or args.rgb_matrix_brightness > 100:
                    print(f"Invalid value for RGB Matrix brightness, it should be between 0 and 100")
                    quit()
                new_sys_config['rgb_matrix_brightness'] = args.rgb_matrix_brightness
                print(f"Set RGB Matrix brightness: {args.rgb_matrix_brightness}")
        # rgb_matrix color
        if args.rgb_matrix_color != '':
            from pironman5.utils import hex_to_rgb
            if args.rgb_matrix_color == None:
                hex = current_config['system']['rgb_matrix_color']
                r, g, b = hex_to_rgb(hex)
                print(f"RGB Matrix color: #{hex} ({r}, {g}, {b})")
            else:
                try:
                    r, g, b = hex_to_rgb(args.rgb_matrix_color)
                except ValueError:
                    print(f'Invalid value for RGB Matrix color, it should be in hex format without # (e.g. 00aabb)')
                    quit()
                new_sys_config['rgb_matrix_color'] = args.rgb_matrix_color
                print(f"Set RGB Matrix color: #{args.rgb_matrix_color} ({r}, {g}, {b})")
        # rgb_matrix color2
        if args.rgb_matrix_color2 != '':
            from pironman5.utils import hex_to_rgb
            if args.rgb_matrix_color2 == None:
                print(f"RGB Matrix color2: {current_config['system']['rgb_matrix_color2']}")
            else:
                try:
                    r, g, b = hex_to_rgb(args.rgb_matrix_color2)
                except ValueError:
                    print(f'Invalid value for RGB Matrix color2, it should be in hex format without # (e.g. 00aabb)')
                    quit()
                new_sys_config['rgb_matrix_color2'] = args.rgb_matrix_color2
                print(f"Set RGB Matrix color2: #{args.rgb_matrix_color2} ({r}, {g}, {b})")

    # # PiPower 5 settings
    if is_included(PERIPHERALS, "pipower5"):
        if args.subcommand == "pipower5":
            cmd = [
                "pipower5",
                "-cp", CONFIG_PATH,
                *remaining_args
            ]
            try:
                import subprocess
                result = subprocess.run(
                    cmd,
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e.stderr}", file=sys.stderr)
                sys.exit(1)
            except FileNotFoundError:
                print("Error: pipower5 command not found, please make sure it is installed and in the environment variables", file=sys.stderr)
                sys.exit(1)

    # update
    # ----------------------------------------
    if args.subcommand == 'update':
        variant = args.variant if args.variant else ''
        if not variant:
            try:
                with open('/opt/pironman5/.variant', 'r') as f:
                    variant = f.read().strip()
            except FileNotFoundError:
                print("Error: Cannot detect variant. /opt/pironman5/.variant not found.")
                print("Specify variant manually: pironman5 update --variant base")
                sys.exit(1)

        if not variant:
            print("Error: Empty variant. Specify manually: pironman5 update --variant base")
            sys.exit(1)

        use_pipower5 = args.pipower5
        if not use_pipower5:
            try:
                with open('/opt/pironman5/.custom_module', 'r') as f:
                    if 'pipower5' in f.read():
                        use_pipower5 = True
            except FileNotFoundError:
                pass

        installer_url = "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh"
        cmd_parts = ["echo n | curl -sSL", installer_url, "| sudo bash -s -- --variant", variant]
        if use_pipower5:
            cmd_parts.append("--pipower5")

        cmd = ' '.join(cmd_parts)
        print(f"Updating Pironman 5 ({variant})...")
        print(f"Running: {cmd}")
        ret = os.system(cmd)
        if ret != 0:
            print(f"Update failed with exit code {ret}", file=sys.stderr)
            sys.exit(1)
        print("Update complete. Restarting service...")
        os.system('sudo systemctl restart pironman5.service')
        quit()

    # uninstall
    # ----------------------------------------
    if args.subcommand == 'uninstall':
        if os.geteuid() != 0:
            print("Requesting root privileges...")
            os.execvp('sudo', ['sudo', 'pironman5'] + sys.argv[1:])
            sys.exit(0)

        def _confirm(prompt):
            if args.yes:
                return True
            while True:
                resp = input(prompt + " [y/N] ")
                if resp.lower() in ('y', 'yes'):
                    return True
                elif resp.lower() in ('', 'n', 'no'):
                    return False

        if not _confirm("This will completely remove Pironman 5 and all its data. Continue?"):
            print("Uninstall cancelled.")
            quit()

        print("Stopping service...")
        os.system('systemctl stop pironman5.service')
        os.system('systemctl disable pironman5.service')
        service_file = '/etc/systemd/system/pironman5.service'
        if os.path.exists(service_file):
            os.remove(service_file)
            os.system('systemctl daemon-reload')

        print("Removing symlinks...")
        symlink_path = '/usr/local/bin/pironman5'
        if os.path.exists(symlink_path):
            os.remove(symlink_path)

        print("Removing user and group...")
        os.system('userdel pironman5 2>/dev/null')
        os.system('groupdel pironman5 2>/dev/null')

        print("Removing directories...")
        os.system('rm -rf /opt/pironman5/')
        os.system('rm -rf /var/log/pironman5/')
        sudo_user = os.environ.get('SUDO_USER', '')
        if sudo_user:
            os.system(f'rm -rf /home/{sudo_user}/pironman5')

        # Check if pipower5 is installed
        pipower5_installed = False
        if os.path.exists('/sys/module/pipower5') or os.path.exists('/sys/class/pipower5'):
            pipower5_installed = True
        elif os.path.exists('/opt/pironman5/venv/bin/pipower5'):
            pipower5_installed = True

        if pipower5_installed:
            if _confirm("PiPower5 UPS module detected. Uninstall it as well?"):
                print("Uninstalling PiPower5...")
                pipower5_bin = '/opt/pironman5/venv/bin/pipower5'
                if os.path.exists(pipower5_bin):
                    os.system(f'{pipower5_bin} uninstall')
                else:
                    print("  pipower5 CLI not found, skipping.")
                # Remove pipower5 user/group
                os.system('userdel pipower5 2>/dev/null')
                os.system('groupdel pipower5 2>/dev/null')
                print("  PiPower5 uninstalled.")

        if _confirm("Remove InfluxDB data (pironman5 database)?"):
            os.system('influx -execute "DROP DATABASE pironman5" 2>/dev/null')

        print("Pironman 5 has been uninstalled.")
        quit()

    # variant
    # ----------------------------------------
    if args.subcommand == 'variant':
        VARIANT_CHOICES = ["base", "mini", "max", "pro-max", "nas", "ups"]
        VARIANT_LABELS = {
            "base": "Pironman 5",
            "mini": "Pironman 5 Mini",
            "max": "Pironman 5 Max",
            "pro-max": "Pironman 5 Pro Max",
            "nas": "Pironman 5 NAS",
            "ups": "Pironman 5 UPS",
        }
        variant_path = "/opt/pironman5/.variant"
        current = None
        if os.path.exists(variant_path):
            with open(variant_path, "r") as f:
                current = f.read().strip()

        if args.list:
            print("Available variants:")
            for v in VARIANT_CHOICES:
                marker = " *" if v == current else ""
                print(f"  {v:<10} {VARIANT_LABELS.get(v, '')}{marker}")
            quit()

        if args.current or (not args.variant_name and not args.list):
            label = VARIANT_LABELS.get(current, "Unknown") if current else "Unknown"
            print(f"Current variant: {current} ({label})" if current else "Current variant: not set (default: base)")
            if not args.current:
                print(f"Switch variant: pironman5 variant <name>")
                print(f"Available: {', '.join(VARIANT_CHOICES)}")
            quit()

        if args.variant_name:
            if args.variant_name not in VARIANT_CHOICES:
                print(f"Invalid variant: {args.variant_name}")
                print(f"Available: {', '.join(VARIANT_CHOICES)}")
                sys.exit(1)
            os.makedirs(os.path.dirname(variant_path), exist_ok=True)
            with open(variant_path, "w") as f:
                f.write(args.variant_name)
            try:
                os.chmod(variant_path, 0o664)
            except Exception:
                pass
            print(f"Switched to {args.variant_name} ({VARIANT_LABELS.get(args.variant_name, '')})")
            print("Restart pironman5 to apply: sudo systemctl restart pironman5.service")
            quit()

    # plugin
    # ----------------------------------------
    if args.subcommand == 'plugin':
        CUSTOM_PATH = "/opt/pironman5/.custom_module"
        PLUGIN_SCRIPTS = {
            "pipower5": {
                "label": "PiPower 5 UPS",
                "installer_args": "--plugin pipower5",
            },
        }

        def _read_plugins():
            if not os.path.exists(CUSTOM_PATH):
                return []
            with open(CUSTOM_PATH, "r") as f:
                return [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

        def _write_plugins(plugins):
            os.makedirs(os.path.dirname(CUSTOM_PATH), exist_ok=True)
            with open(CUSTOM_PATH, "w") as f:
                f.write("\n".join(plugins) + "\n")

        if args.plugin_action == "list":
            installed = _read_plugins()
            if installed:
                print("Installed plugins:")
                for p in installed:
                    label = PLUGIN_SCRIPTS.get(p, {}).get("label", p)
                    print(f"  {p}  ({label})")
            else:
                print("No plugins installed.")
            quit()

        plugin_name = args.plugin_name
        if plugin_name not in PLUGIN_SCRIPTS:
            print(f"Unknown plugin: {plugin_name}")
            print(f"Available: {', '.join(PLUGIN_SCRIPTS.keys())}")
            sys.exit(1)

        if args.plugin_action == "install":
            installed = _read_plugins()
            if plugin_name in installed:
                print(f"Plugin '{plugin_name}' is already installed.")
                quit()
            installer_url = "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh"
            installer_args = PLUGIN_SCRIPTS[plugin_name]["installer_args"]
            cmd = f"curl -sSL {installer_url} | sudo bash -s -- {installer_args}"
            print(f"Installing {plugin_name}...")
            ret = os.system(cmd)
            if ret != 0:
                print(f"Plugin install failed with exit code {ret}", file=sys.stderr)
                sys.exit(1)
            print(f"Plugin '{plugin_name}' installed. Restart pironman5 to apply:")
            print("  sudo systemctl restart pironman5.service")
            quit()

        if args.plugin_action == "remove":
            installed = _read_plugins()
            if plugin_name not in installed:
                print(f"Plugin '{plugin_name}' is not installed.")
                quit()
            installed.remove(plugin_name)
            _write_plugins(installed)
            # Also uninstall the python package
            os.system(f"/opt/pironman5/venv/bin/pip uninstall -y {plugin_name} 2>/dev/null")
            print(f"Plugin '{plugin_name}' removed. Restart pironman5 to apply:")
            print("  sudo systemctl restart pironman5.service")
            quit()

    # Update settings
    # ----------------------------------------
    new_config = {
        'system': new_sys_config,
    }

    update_config_file(new_config, config_path)

    # start
    if args.subcommand == 'start':
        pironman5 = Pironman5(config_path=config_path)
        pironman5.start()
    elif args.subcommand == 'stop':
        os.system('pkill -f pironman5')
    elif args.subcommand == 'launch-browser':
        if args.auto_start != '':
            if args.auto_start in TRUE_LIST:
                print(f"Set dashboard auto start") 
                if not os.path.exists(os.path.expanduser("~/.config/autostart")):
                    os.makedirs(os.path.expanduser("~/.config/autostart"))
                with open(os.path.expanduser("~/.config/autostart/pironman5-dashboard.desktop"), "w") as f:
                    f.write("""[Desktop Entry]
Type=Application
Name=Pironman5 Launch Dashboard on Browser
Comment=Auto launch Dashboard on browser for pironman5 on startup
Exec=pironman5 launch-browser
Terminal=false
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
X-KDE-autostart-enabled=true
X-MATE-Autostart-enabled=true
Categories=Utility;Network;Browser;
Keywords=pironman5;browser;autostart;""")
            elif args.auto_start in FALSE_LIST:
                print(f"Remove dashboard auto start") 
                os.system(f'rm -f ~/.config/autostart/pironman5-dashboard.desktop')
            else:
                print(f"Invalid value for auto start, it should be true/on/1 or false/off/0")
                quit()
        else:
            launch_browser()
