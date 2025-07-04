
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

    current_config = None
    debug_level = 'INFO'
    new_sys_config = {}

    parser = argparse.ArgumentParser(description=f'{NAME} command line interface')
    parser.add_argument("command",
                        choices=["start", "restart", "stop"],
                        nargs="?",
                        help="Command")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--config", action="store_true", help="Show config")
    parser.add_argument("-dl", "--debug-level", nargs='?', default='', choices=['debug', 'info', 'warning', 'error', 'critical'], help="Debug level")
    parser.add_argument("--background", nargs='?', default='', help="Run in background")
    parser.add_argument("-rd", "--remove-dashboard", action="store_true", help="Remove dashboard")
    parser.add_argument("-cp", "--config-path", nargs='?', default='', help="Config path")
    if is_included(PERIPHERALS, "ws2812"):
        from pm_auto.ws2812 import RGB_STYLES
        parser.add_argument("-rc", "--rgb-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
        parser.add_argument("-rb", "--rgb-brightness", nargs='?', default='', help="RGB brightness 0-100")
        parser.add_argument("-rs", "--rgb-style", choices=RGB_STYLES, nargs='?', default='', help="RGB style")
        parser.add_argument("-rp", "--rgb-speed", nargs='?', default='', help="RGB speed 0-100")
        parser.add_argument("-re", "--rgb-enable", nargs='?', default='', help="RGB enable True/False")
        parser.add_argument("-rl", "--rgb-led-count", nargs='?', default='', help="RGB LED count int")
    if is_included(PERIPHERALS, "temperature_unit"):
        parser.add_argument("-u", "--temperature-unit", choices=["C", "F"], nargs='?', default='', help="Temperature unit")
    if is_included(PERIPHERALS, "gpio_fan_mode"):
        from pm_auto.fan_control import GPIO_FAN_MODES
        parser.add_argument("-gm", "--gpio-fan-mode", nargs='?', default='', help=f"GPIO fan mode, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
        parser.add_argument("-gp", "--gpio-fan-pin", nargs='?', default='', help="GPIO fan pin")
    if is_included(PERIPHERALS, "gpio_fan_led"):
        parser.add_argument("-fl", "--gpio-fan-led", nargs='?', default='', help="GPIO fan LED state on/off/follow")
        parser.add_argument("-fp", "--gpio-fan-led-pin", nargs='?', default='', help="GPIO fan LED pin")
    if is_included(PERIPHERALS, "oled"):
        parser.add_argument("-oe", "--oled-enable", nargs='?', default='', help="OLED enable True/true/on/On/1 or False/false/off/Off/0")
        parser.add_argument("-od", "--oled-disk", nargs='?', default='', help="Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme")
        parser.add_argument("-oi", "--oled-network-interface", nargs='?', default='', help="Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or wlan0")
        parser.add_argument("-or", "--oled-rotation", nargs='?', default=-1, type=int, choices=[0, 180], help="Set to rotate OLED display, 0, 180")
    if is_included(PERIPHERALS, "vibration_switch"):
        parser.add_argument("-vp", "--vibration-switch-pin", nargs='?', default='', help="Vibration switch pin")
        parser.add_argument("-vu", "--vibration-switch-pull-up", nargs='?', default='', help="Vibration switch pull up True/False")
        parser.add_argument("-os", "--oled-sleep-timeout", nargs='?', default='', help="OLED sleep timeout in seconds")

    # parse args
    # ========================================
    args = parser.parse_args()

    # no args, show help
    # ----------------------------------------
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

    # load config file
    # ----------------------------------------
    if not path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({'system': {}}, f, indent=4)
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
        # oled disk
        if args.oled_disk != '':
            from sf_rpi_status import get_disks
            disks = ['total']
            disks.extend(get_disks())
            if args.oled_disk == None:
                print(f"OLED disk: {current_config['system']['oled_disk']}, options: {disks}")
            else:
                if args.oled_disk not in disks:
                    print(f"Invalid value for OLED disk, it should be in {disks}")
                    quit()
                new_sys_config['oled_disk'] = args.oled_disk
                print(f"Set OLED disk: {args.oled_disk}")
        # oled network interface
        if args.oled_network_interface != '':
            from sf_rpi_status import get_ips
            interfaces = ['all']
            interfaces.extend(get_ips().keys())
            if args.oled_network_interface == None:
                print(f"OLED Network Interface: {current_config['system']['oled_network_interface']}, options: {interfaces}")
            else:
                if args.oled_network_interface not in interfaces:
                    print(f"Invalid value for OLED Network Interface, it should be in {interfaces}")
                    quit()
                new_sys_config['oled_network_interface'] = args.oled_network_interface
                print(f"Set OLED Network Interface: {args.oled_network_interface}")
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
    # Vibration switch settings
    # ----------------------------------------
    if is_included(PERIPHERALS, "vibration_switch"):
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

    # update config
    # =========================================
    new_config = {
        'system': new_sys_config,
    }

    update_config_file(new_config, config_path)

    # start, restart, stop
    # =========================================
    if args.command == "start":
        pironman5 = Pironman5(config_path=config_path)
        pironman5.start()

    if args.command == "restart":
        print("This is a placeholder for pironman5 binary help, you should run pironman5 instead")
        quit()

    if args.command == "stop":
        import os
        os.system('kill -15 $(pgrep -f "pironman5 start")')
        os.system('kill -15 $(pgrep -f "pironman5-service start")')
        pironman5 = Pironman5()
        pironman5.stop()
        quit()

    if args.background != '':
        print("This is a placeholder for pironman5 binary help, you should run pironman5 instead")
        quit()