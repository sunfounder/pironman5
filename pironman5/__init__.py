from .version import __version__

def main():
    TRUE_LIST = ['true', 'True', 'TRUE', '1', 'on', 'On', 'ON']
    FALSE_LIST = ['false', 'False', 'FALSE', '0', 'off', 'Off', 'OFF']

    import argparse
    from .pironman5 import Pironman5
    from .utils import get_hat_version
    from pm_auto.ws2812 import RGB_STYLES
    from pm_auto.fan_control import GPIO_FAN_MODES
    from importlib.resources import files as resource_files
    import json
    import sys
    from os import path

    CONFIG_PATH = resource_files('pironman5').joinpath('config.json')

    current_config = None
    debug_level = 'INFO'
    new_auto = {}

    parser = argparse.ArgumentParser(description='Pironman5')
    parser.add_argument("command",
                        choices=["start", "restart", "stop"],
                        nargs="?",
                        help="Command")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--config", action="store_true", help="Show config")
    parser.add_argument("-dl", "--debug-level", choices=['debug', 'info', 'warning', 'error', 'critical'], help="Debug level")
    parser.add_argument("-rc", "--rgb-color", nargs='?', default='', help='RGB color in hex format without # (e.g. 00aabb)')
    parser.add_argument("-rb", "--rgb-brightness", nargs='?', default='', help="RGB brightness 0-100")
    parser.add_argument("-rs", "--rgb-style", choices=RGB_STYLES, nargs='?', default='', help="RGB style")
    parser.add_argument("-rp", "--rgb-speed", nargs='?', default='', help="RGB speed 0-100")
    parser.add_argument("-re", "--rgb-enable", nargs='?', default='', help="RGB enable True/False")
    parser.add_argument("-rl", "--rgb-led-count", nargs='?', default='', help="RGB LED count int")
    parser.add_argument("-u", "--temperature-unit", choices=["C", "F"], nargs='?', default='', help="Temperature unit")
    parser.add_argument("-gm", "--gpio-fan-mode", nargs='?', default='', help=f"GPIO fan mode, {', '.join([f'{i}: {mode}' for i, mode in enumerate(GPIO_FAN_MODES)])}")
    parser.add_argument("-gp", "--gpio-fan-pin", nargs='?', default='', help="GPIO fan pin")
    if get_hat_version() >= 11:
        parser.add_argument("-fl", "--gpio-fan-led", nargs='?', default='', help="GPIO fan LED state on/off/follow")
        parser.add_argument("-fp", "--gpio-fan-led-pin", nargs='?', default='', help="GPIO fan LED pin")
    parser.add_argument("-od", "--oled-disk", nargs='?', default='', help="Set to display which disk on OLED. 'total' or the name of the disk, like mmbclk or nvme")
    parser.add_argument("-oi", "--oled-network-interface", nargs='?', default='', help="Set to display which ip of network interface on OLED, 'all' or the interface name, like eth0 or wlan0")
    parser.add_argument("--background", nargs='?', default='', help="Run in background")

    args = parser.parse_args()

    if not (len(sys.argv) > 1):
        parser.print_help()
        quit()
    
    if not path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as f:
            json.dump({'auto': {}}, f, indent=4)
    else:
        with open(CONFIG_PATH, 'r') as f:
            current_config = json.load(f)

    if args.config:
        print(json.dumps(current_config, indent=4))
        quit()

    if args.debug_level != None:
        debug_level = args.debug_level.upper()

    if args.command == "restart":
        print("This is a placeholder for pironman5 binary help, you should run pironman5 instead")
        quit()

    if args.command == "stop":
        import os
        os.system('kill -9 $(pgrep -f "pironman5 start")')
        os.system('kill -9 $(pgrep -f "pironman5-service start")')
        pironman5 = Pironman5()
        pironman5.stop()
        quit()

    if args.version:
        print(__version__)
        quit()
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
            new_auto['rgb_color'] = args.rgb_color
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
            new_auto['rgb_brightness'] = args.rgb_brightness
    if args.rgb_style != '':
        if args.rgb_style == None:
            print(f"RGB style: {current_config['system']['rgb_style']}")
        else:
            if args.rgb_style not in RGB_STYLES:
                print(f"Invalid value for RGB style, it should be one of {RGB_STYLES}")
                quit()
            new_auto['rgb_style'] = args.rgb_style
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
            new_auto['rgb_speed'] = args.rgb_speed
    if args.rgb_enable != '':
        if args.rgb_enable == None:
            print(f"RGB enable: {current_config['system']['rgb_enable']}")
        else:
            if args.rgb_enable in TRUE_LIST:
                new_auto['rgb_enable'] = True
            elif args.rgb_enable in FALSE_LIST:
                new_auto['rgb_enable'] = False
            else:
                print(f"Invalid value for RGB enable, it should be True or False")
                quit()
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
            new_auto['rgb_led_count'] = args.rgb_led_count
    if args.temperature_unit != '':
        if args.temperature_unit == None:
            print(f"Temperature unit: {current_config['system']['temperature_unit']}")
        else:
            if args.temperature_unit not in ['C', 'F']:
                print(f"Invalid value for Temperature unit, it should be C or F")
                quit()
            new_auto['temperature_unit'] = args.temperature_unit
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
            new_auto['gpio_fan_mode'] = args.gpio_fan_mode
    if args.gpio_fan_pin != '':
        if args.gpio_fan_pin == None:
            print(f"GPIO fan pin: {current_config['system']['gpio_fan_pin']}")
        else:
            try:
                args.gpio_fan_pin = int(args.gpio_fan_pin)
            except ValueError:
                print(f"Invalid value for GPIO fan pin, it should be an integer")
                quit()
            new_auto['gpio_fan_pin'] = args.gpio_fan_pin
    if get_hat_version() >= 11:
        if args.gpio_fan_led != '':
            if args.gpio_fan_led == None:
                print(f"GPIO fan LED state: {current_config['system']['gpio_fan_led']}")
            else:
                state = args.gpio_fan_led.lower()
                if state not in ['on', 'off', 'follow']:
                    print(f"Invalid value for GPIO fan LED state, it should be on, off or follow")
                    quit()
                new_auto['gpio_fan_led'] = state
        if args.gpio_fan_led_pin != '':
            if args.gpio_fan_led_pin == None:
                print(f"GPIO fan LED pin: {current_config['system']['gpio_fan_led_pin']}")
            else:
                try:
                    args.gpio_fan_led_pin = int(args.gpio_fan_led_pin)
                except ValueError:
                    print(f"Invalid value for GPIO fan LED pin, it should be an integer")
                    quit()
                new_auto['gpio_fan_led_pin'] = args.gpio_fan_led_pin
    if args.oled_disk != '':
        from sf_rpi_status import get_disks
        disks = ['total']
        disks.extend(get_disks().keys())
        if args.oled_disk == None:
            print(f"OLED disk: {current_config['system']['oled_disk']}, options: {disks}")
        else:
            if args.oled_disk not in disks:
                print(f"Invalid value for OLED disk, it should be in {disks}")
                quit()
            new_auto['oled_disk'] = args.oled_disk
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
            new_auto['oled_network_interface'] = args.oled_network_interface
    if args.background != '':
        print("This is a placeholder for pironman5 binary help, you should run pironman5 instead")
        quit()

    new_config = {
        'system': new_auto,
    }

    Pironman5.update_config_file(new_config)

    if args.command == "start":
        pironman5 = Pironman5()
        pironman5.set_debug_level(debug_level)
        pironman5.start()