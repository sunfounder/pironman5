import time
import random
from rpi_ws281x import PixelStrip, Color  # https://github.com/jgarff/rpi_ws281x
from utils import log

# LED strip configuration:
# LED_COUNT      = 16      # Number of LED pixels.
# LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
# LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA        = 10      # DMA channel to use for generating signal (try 5)
# LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

RGB_styles = [
    'breath', 'leap', 'flow', 'raise_up', 'colorful', 'colorful_leap'
]
colorful_leds = [
    "#ff0000",
    "#e71164",
    "#ffa500",
    "#0000ff",
    "#ffC800",
    "#00ff00",
    "#0000ff",
    "#00ffb4",
    "#ff0000",
    "#00ff00",
    "#00ff00",
    "#8b00ff",
    "#8b00ff",
    "#8b00ff",
    "#0000ff",
    "#0000ff",
]


class WS2812():

    lights_order = [1, 3, 5, 7, 0, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15]

    def __init__(
        self,
        LED_COUNT,
        LED_PIN,
        LED_BRIGHTNESS=255,
        LED_FREQ_HZ=1000000,
        LED_DMA=10,
        LED_INVERT=False,
    ):
        self.led_count = LED_COUNT
        self.led_pin = LED_PIN
        self.led_brightness = LED_BRIGHTNESS
        self.led_freq_hz = LED_FREQ_HZ
        self.led_dma = LED_DMA
        self.led_invert = LED_INVERT
        self.strip = None
        self.init()

    def init(self):
        self.strip = PixelStrip(self.led_count, self.led_pin, self.led_freq_hz,
                                self.led_dma, self.led_invert,
                                self.led_brightness)
        time.sleep(0.01)
        self.strip.begin()

    def reinit(self):
        # if self.strip is not None:
        # 	# del self.strip
        # 	self.strip._cleanup()
        # 	self.strip = None
        # self.init()

        if self.strip is None:
            self.init()

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

    def clear(self, color: str = '#000000'):
        r, g, b = self.hex_to_rgb(color)
        self.reinit()
        self.strip.begin()
        for i in range(self.led_count):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def display(self,
                style: str,
                color: str = '#0a1aff',
                speed=50,
                brightness=255):
        color = list(self.hex_to_rgb(color))
        self.clear()
        # eval is evil, list The list is split into individual characters
        # eval('self.%s(color="%s", speed=%s)'%(style, color, speed))
        try:
            fuc = getattr(self, style)
            fuc(color, speed)
        except KeyError as e:
            log(f'LED strip parameter error: {e}')
        except Exception as e:
            log(f'LED display error: {e}')


# styles

    def breath(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        while True:
            self.reinit()
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for i in range(100, 1, -1):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

            # --- no breath ---
            # r, g, b =  color
            # for index in self.lights_order:
            # 	self.strip.setPixelColor(index, Color(r,g,b))
            # self.strip.show()
            # time.sleep(2)

    def leap(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for i in range(self.led_count):
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(0, 0, 0))
                self.strip.setPixelColor(i, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

    def flow(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for index in self.lights_order:
                self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for j in range(self.led_count):
                self.strip.setPixelColor(j, Color(0, 0, 0))
            self.strip.show()
            time.sleep(0.005 * speed)

    def raise_up(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(0, 4, 1):
                    self.strip.setPixelColor(self.lights_order[index],
                                             Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(4, 8, 1):
                    self.strip.setPixelColor(self.lights_order[index],
                                             Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(8, 16, 1):
                    self.strip.setPixelColor(self.lights_order[index],
                                             Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            # turn off
            time.sleep(10 * 0.0005 * speed)
            for index in self.lights_order:
                self.strip.setPixelColor(self.lights_order[index],
                                         Color(0, 0, 0))
                self.strip.show()
                time.sleep(0.001 * speed)

    def colorful(self, color: list = None, speed=50):
        speed = 101 - speed
        _color = list(
            self.hex_to_rgb(colorful_leds[i]) for i in range(self.led_count))
        while True:
            self.reinit()
            for i in range(2, 101):
                for index in self.lights_order:
                    r, g, b = [int(x * i * 0.01) for x in _color[index]]
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for i in range(100, 1, -1):
                for index in self.lights_order:
                    r, g, b = [int(x * i * 0.01) for x in _color[index]]
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

    def colorful_leap(self, color: list = None, speed=50):
        speed = 101 - speed
        while True:
            self.reinit()
            for i in range(self.led_count):
                r, g, b = self.hex_to_rgb(colorful_leds[i])
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(0, 0, 0))
                self.strip.setPixelColor(i, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

if __name__ == "__main__":
    speed = 80
    strip = WS2812(16, 10)  # LED_COUNT, LED_PIN

    # strip.display('breath','#0000ff', speed=speed)
    # strip.display(style='leap',color='#0000ff', speed=speed)
    # strip.display(style='colorful', speed=speed)
    # strip.display(style='flow',color='#1a1aff', speed=speed)
    # strip.display(style='raise_up',color='#1a1aff', speed=speed)
    strip.display(style='colorful_leap', speed=speed)
