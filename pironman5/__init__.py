
def update_config_file(config, config_path):
    import json
    from .utils import merge_dict
    current = None
    with open(config_path, 'r') as f:
        current = json.load(f)
    current = merge_dict(current, config)
    with open(config_path, 'w') as f:
        json.dump(current, f, indent=4)

def main():
    from .variants import NAME, ID, PERIPHERALS
    
    import argparse
    from .pironman5 import Pironman5
    from .version import __version__
    from .utils import is_included
    from importlib.resources import files as resource_files
    import json
    import sys
    from os import path

    TRUE_LIST = ['true', 'True', 'TRUE', '1', 'on', 'On', 'ON']
    FALSE_LIST = ['false', 'False', 'FALSE', '0', 'off', 'Off', 'OFF']

    __package_name__ = __name__.split('.')[0]
    CONFIG_PATH = str(resource_files(__package_name__).joinpath('config.json'))
    PIP_PATH = "/opt/pironman5/venv/bin/pip"
    DEBUG_LEVELS = ['debug', 'info', 'warning', 'error', 'critical']

    current_config = None
    debug_level = 'INFO'
    new_sys_config = {}

    parser = argparse.ArgumentParser(prog='pironman5',
                                    description=f'{NAME} command line interface')
    parser.add_argument("command", choices=['start'], nargs='?', help="Command")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--config", action="store_true", help="Show config")
    parser.add_argument("-dl", "--debug-level", nargs='?', default='', choices=['debug', 'info', 'warning', 'error', 'critical'], help="Debug level")
    parser.add_argument("--background", nargs='?', default='', help="Run in background")
    parser.add_argument("-rd", "--remove-dashboard", action="store_true", help="Remove dashboard")
    parser.add_argument("-cp", "--config-path", nargs='?', default='', help="Config path")
    parser.add_argument("-eh", "--enable-history", nargs='?', default='', help="Enable history, True/true/on/On/1 or False/false/off/Off/0")
    # ws2812
    if is_included(PERIPHERALS, "ws2812"):
        from pm_auto.services.ws2812_service import RGB_STYLES
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
        from pm_auto.services.fan_service import GPIO_FAN_MODES
        parser.add_argument("-gm", "--gpio-fan-mode", nargs='?', default='', help=f"GPIO fan mode, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
        parser.add_argument("-gp", "--gpio-fan-pin", nargs='?', default='', help="GPIO fan pin")
    if is_included(PERIPHERALS, "gpio_fan_led"):
        parser.add_argument("-fl", "--gpio-fan-led", nargs='?', default='', help="GPIO fan LED state on/off/follow")
        parser.add_argument("-fp", "--gpio-fan-led-pin", nargs='?', default='', help="GPIO fan LED pin")
    # oled
    if is_included(PERIPHERALS, "oled"):
        AVAILABLE_PAGES = []
        for item in PERIPHERALS:
            if item.startswith("oled_page_"):
                AVAILABLE_PAGES.append(item.split("oled_page_")[1])
        parser.add_argument("-oe", "--oled-enable", nargs='?', default='', help="OLED enable True/true/on/On/1 or False/false/off/Off/0")
        parser.add_argument("-or", "--oled-rotation", nargs='?', default=-1, type=int, choices=[0, 180], help="Set to rotate OLED display, 0, 180")
        parser.add_argument("-op", "--oled-pages", nargs='*', default=[], help=f"OLED pages: {', '.join(AVAILABLE_PAGES)}")
        if is_included(PERIPHERALS, "oled_sleep"):
            parser.add_argument("-os", "--oled-sleep-timeout", nargs='?', default='', help="OLED sleep timeout in seconds")
    # vibration_switch
    if is_included(PERIPHERALS, "vibration_switch"):
        parser.add_argument("-vp", "--vibration-switch-pin", nargs='?', default='', help="Vibration switch pin")
        parser.add_argument("-vu", "--vibration-switch-pull-up", nargs='?', default='', help="Vibration switch pull up True/False")
    # rgb_matrix
    if is_included(PERIPHERALS, "rgb_matrix"):
        from pm_auto.services.rgb_matrix_service import EFFECT_LIST
        parser.add_argument("-rme", "--rgb-matrix-enable", nargs='?', default='', help="RGB enable True/False")
        parser.add_argument("-rms", "--rgb-matrix-style",  nargs='?', default='', help=f"RGB style: {EFFECT_LIST}")
        parser.add_argument("-rmc", "--rgb-matrix-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rmc2", "--rgb-matrix-color2", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rmp", "--rgb-matrix-speed", nargs='?', default='', help="RGB speed 0-100")
        parser.add_argument("-rmb", "--rgb-matrix-brightness", nargs='?', default='', help="RGB brightness 0-100")
    
    # parse args
    # -----------------------------------------------------------
    args = parser.parse_args()

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
    if not path.exists(config_path):
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
                current_config = json.loads(content)
            except json.JSONDecodeError:
                print(f"Invalid config file: {config_path}")
                quit()

    # show config
    # ----------------------------------------
    if args.config:
        print(json.dumps(current_config, indent=4))
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

    # remove dashboard
    # ----------------------------------------    
    if args.remove_dashboard:
        import os
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

    # ws2812 settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "ws2812"):
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
        # ws2812 rgb_led_count
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
                try:
                    args.oled_sleep_timeout = int(args.oled_sleep_timeout)
                except ValueError:
                    print(f"Invalid value for OLED sleep timeout, it should be an integer")
                    quit()
                if args.oled_sleep_timeout < 0:
                    print(f"Invalid value for OLED sleep timeout, it should be greater than or equal to 0")
                    quit()
                new_sys_config['oled_sleep_timeout'] = args.oled_sleep_timeout
                print(f"Set OLED sleep timeout: {args.oled_sleep_timeout}")
        # oled_pages
        if args.oled_pages != []:
            if args.oled_pages == None:
                print(f"OLED pages: {', '.join(current_config['system']['oled_pages'])}")
            else:
                for page in args.oled_pages:
                    if page not in AVAILABLE_PAGES:
                        print(f"Invalid value for OLED pages: '{page}', it should be {', '.join(AVAILABLE_PAGES)}")
                        quit()
                new_sys_config['oled_pages'] = args.oled_pages
                print(f"Set OLED pages: {args.oled_pages}")
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
    # rgb_matrix
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

    # update config
    # ----------------------------------------
    new_config = {
        'system': new_sys_config,
    }

    update_config_file(new_config, config_path)

    # start
    if args.command == 'start':
        pironman5 = Pironman5(config_path=config_path)
        pironman5.start()
