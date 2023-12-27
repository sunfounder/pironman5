import time

# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel_SPI
import board
import neopixel_spi as neopixel

# import random
from utils import log

# LED strip configuration:
# LED_COUNT      = 16      # Number of LED pixels.
# LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
# LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA        = 10      # DMA channel to use for generating signal (try 5)
# LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

RGB_styles = [
    'breath', 'leap', 'flow', 'colorful', 'colorful_leap'
]
colorful_leds = [
    "#ff0000",
    "#00ff00",
    "#ffa500",
    "#0000ff",
    "#ffC800",
    "#00ff00",
    "#0000ff",
    "#00ffb4",
    "#ff0000",
    "#00ff00",
    "#e71164",
    "#8b00ff",
    "#8b00ff",
    "#8b00ff",
    "#0000ff",
    "#e71164",
    "#0000ff",
]


class WS2812():


    lights_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,]
    leap_order = [0, 3, 1, 2, 4, 12, 5, 11, 6, 10, 7, 9, 8, 15, 13, 14]


    def __init__(
        self,
        LED_COUNT,
    ):
        self.led_count = LED_COUNT

        self.init()

    def init(self):
        spi = board.SPI()
        PIXEL_ORDER = neopixel.GRB

        self.strip = neopixel.NeoPixel_SPI(
                spi, self.led_count, pixel_order=PIXEL_ORDER, auto_write=False
        )
        time.sleep(0.01)
        self.strip.fill(0)

    # str or hex, eg: 'ffffff', '#ffffff', '#FFFFFF'
    def hex_to_rgb(self, hex):
        try:
            hex = hex.strip().replace('#', '')
            r = int(hex[0:2], 16)
            g = int(hex[2:4], 16)
            b = int(hex[4:6], 16)
            return [r, g, b]
        except Exception as e:
            log('color parameter error: \n%s' % e)

    def clear(self):
        self.strip.fill(0)
        self.strip.show()

    def fill(self, color:str='#000000'):
        self.strip.fill(color)
        self.strip.show()

    def display(self,
                style: str,
                color: str = '#0a1aff',
                speed=50):
        color = list(self.hex_to_rgb(color))
        self.clear()
        try:
            fuc = getattr(self, style)
            fuc(color, speed)
        except KeyError as e:
            log(f'LED strip parameter error: {e}')
        except Exception as e:
            log(f'LED display error: {type(e)} {e}')

# styles
    def breath(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        while True:
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                self.strip.fill((r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            time.sleep(0.01 * speed)
            for i in range(100, 1, -1):
                r, g, b = [int(x * i * 0.01) for x in color]
                self.strip.fill((r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

            # --- no breath ---
            # r, g, b =  color
            # self.strip.fill((r, g, b))
            # self.strip.show()
            # time.sleep(2)

    def leap(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color

        # check leap order
        _leap_order = [0]*self.led_count
        num = 0
        for i in self.leap_order:
            if i < self.led_count:
                _leap_order[num] = i
                num += 1
            else:
                continue
            if num == self.led_count:
                break

        while True:
            for i in range(self.led_count):
                self.strip.fill(0)
                index =_leap_order[i]
                self.strip[index] = (r, g, b)
                self.strip.show()
                time.sleep(0.0035 * speed)

    def flow(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            for i in range(self.led_count):
                index =self.lights_order[i]
                self.strip[index] = (r, g, b)
                self.strip.show()
                time.sleep(0.0015 * speed)
            self.strip.fill(0)
            self.strip.show()
            time.sleep(0.005 * speed)

    def colorful(self, color: list = None, speed=50):
        speed = 101 - speed
        _color = list(self.hex_to_rgb(colorful_leds[i]) for i in range(self.led_count))
        while True:
            for i in range(2, 101):
                for j in range(self.led_count):
                    r, g, b = [int(x * i * 0.01) for x in _color[j]]
                    index =self.lights_order[j]
                    self.strip[index] = (r, g, b)
                self.strip.show()
                time.sleep(0.001 * speed)
            time.sleep(0.01 * speed)
            for i in range(100, 1, -1):
                for j in range(self.led_count):
                    r, g, b = [int(x * i * 0.01) for x in _color[j]]
                    index =self.lights_order[j]
                    self.strip[index] = (r, g, b)
                self.strip.show()
                time.sleep(0.001 * speed)

            # --- no breath ---
            # for j in range(self.led_count):
            #     r, g, b = _color[j]
            #     index =self.lights_order[j]
            #     self.strip[index] = (r, g, b)
            # self.strip.show()
            # time.sleep(2)

    def colorful_leap(self, color: list = None, speed=50):
        speed = 101 - speed

        # check leap order
        _leap_order = [0]*self.led_count
        num = 0
        for i in self.leap_order:
            if i < self.led_count:
                _leap_order[num] = i
                num += 1
            else:
                continue
            if num == self.led_count:
                break

        while True:
            for i in range(self.led_count):
                r, g, b = self.hex_to_rgb(colorful_leds[i])
                self.strip.fill(0)
                index =_leap_order[i]
                self.strip[index] = (r, g, b)
                self.strip.show()
                time.sleep(0.01 * speed)

if __name__ == "__main__":
    try:
        speed = 50
        strip = WS2812(4)  # LED_COUNT, LED_PIN
        # strip.display('breath','#0000ff', speed=speed)
        # strip.display(style='leap',color='#0000ff', speed=speed)
        # strip.display(style='flow',color='#1a1aff', speed=speed)
        strip.display(style='colorful', speed=speed)
        # strip.display(style='colorful_leap',  speed=speed)
    finally:
        strip.clear()
