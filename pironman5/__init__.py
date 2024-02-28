from .version import __version__

def main():
    import argparse
    from .pironman5 import Pironman5
    from pm_auto.ws2812 import RGB_STYLES

    AUTO_CONFIG_KEYS = [
        'rgb_color',
        'rgb_brightness',
        'rgb_style',
        'rgb_speed',
        'rgb_enable',
        'rgb_led_count',
        'temperature_unit',
        'gpio_fan_pin',
    ]

    parser = argparse.ArgumentParser(description='Pironman5')
    parser.add_argument("command", choices=["start", "stop", "restart"], nargs="?", help="Command")
    parser.add_argument("--rgb-color", help="RGB color")
    parser.add_argument("--rgb-brightness", type=int, help="RGB brightness")
    parser.add_argument("--rgb-style", choices=RGB_STYLES, help="RGB style")
    parser.add_argument("--rgb-speed", type=int, help="RGB speed")
    parser.add_argument("--rgb-enable", action="store_true", default=True, help="Enable RGB")
    parser.add_argument("--rgb-led-count", type=int, help="RGB LED count")
    parser.add_argument("--temperature-unit", choices=["C", "F"], help="Temperature unit")
    parser.add_argument("--gpio-fan-pin", type=int, help="GPIO fan pin")

    args = parser.parse_args()
    args = vars(args)
    auto_config = {}
    for key in AUTO_CONFIG_KEYS:
        if args[key] is not None:
            auto_config[key] = args[key]
    config = {
        'auto': auto_config,
    }

    pironman5 = Pironman5()
    pironman5.update_config(config)
    if args['command'] == "start":
        pironman5.start()
    elif args['command'] == "stop":
        import os
        os.system("kill -9 $(pgrep -f pironman5)")
    elif args['command'] == "restart":
        pironman5.stop()
        pironman5.start()