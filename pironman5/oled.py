# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from __future__ import division
import logging
from i2c import I2C
from PIL import Image, ImageDraw, ImageFont
from app_info import __app_name__

# Constants
SSD1306_I2C_ADDRESS_1 = 0x3C
SSD1306_I2C_ADDRESS_2 = 0x3D
SSD1306_SETCONTRAST = 0x81
SSD1306_DISPLAYALLON_RESUME = 0xA4
SSD1306_DISPLAYALLON = 0xA5
SSD1306_NORMALDISPLAY = 0xA6
SSD1306_INVERTDISPLAY = 0xA7
SSD1306_DISPLAYOFF = 0xAE
SSD1306_DISPLAYON = 0xAF
SSD1306_SETDISPLAYOFFSET = 0xD3
SSD1306_SETCOMPINS = 0xDA
SSD1306_SETVCOMDETECT = 0xDB
SSD1306_SETDISPLAYCLOCKDIV = 0xD5
SSD1306_SETPRECHARGE = 0xD9
SSD1306_SETMULTIPLEX = 0xA8
SSD1306_SETLOWCOLUMN = 0x00
SSD1306_SETHIGHCOLUMN = 0x10
SSD1306_SETSTARTLINE = 0x40
SSD1306_MEMORYMODE = 0x20
SSD1306_COLUMNADDR = 0x21
SSD1306_PAGEADDR = 0x22
SSD1306_COMSCANINC = 0xC0
SSD1306_COMSCANDEC = 0xC8
SSD1306_SEGREMAP = 0xA0
SSD1306_CHARGEPUMP = 0x8D
SSD1306_EXTERNALVCC = 0x1
SSD1306_SWITCHCAPVCC = 0x2

# Scrolling constants
SSD1306_ACTIVATE_SCROLL = 0x2F
SSD1306_DEACTIVATE_SCROLL = 0x2E
SSD1306_SET_VERTICAL_SCROLL_AREA = 0xA3
SSD1306_RIGHT_HORIZONTAL_SCROLL = 0x26
SSD1306_LEFT_HORIZONTAL_SCROLL = 0x27
SSD1306_VERTICAL_AND_RIGHT_HORIZONTAL_SCROLL = 0x29
SSD1306_VERTICAL_AND_LEFT_HORIZONTAL_SCROLL = 0x2A


class SSD1306Base(object):
    """Base class for SSD1306-based OLED displays.  Implementors should subclass
    and provide an implementation for the _initialize function.
    """

    def __init__(self, width, height, dc=None, sclk=None, din=None, cs=None,
                 gpio=None, spi=None, i2c_bus=None, i2c_address=SSD1306_I2C_ADDRESS_1,
                 i2c=None):
        self._log = logging.getLogger('Adafruit_SSD1306.SSD1306Base')
        self._spi = None
        self._i2c = I2C()
        self.addr = i2c_address
        self.width = width
        self.height = height
        self._pages = height//8
        self._buffer = [0]*(width*self._pages)
        # Default to platform GPIO if not provided.
        self._gpio = gpio

    def _initialize(self):
        raise NotImplementedError

    def write_command(self, c):
        """Send write_command byte to display."""
        if self._spi is not None:
            # SPI write.
            self._gpio.set_low(self._dc)
            self._spi.write([c])
        else:
            # I2C write.
            control = 0x00   # Co = 0, DC = 0
            self._i2c._i2c_write_byte_data(self.addr, control, c)

    def write_data(self, c):
        """Send byte of data to display."""
        if self._spi is not None:
            # SPI write.
            self._gpio.set_high(self._dc)
            self._spi.write([c])
        else:
            # I2C write.
            control = 0x40   # Co = 0, DC = 0
            self._i2c._i2c_write_byte_data(self.addr, control, c)

    def begin(self, vccstate=SSD1306_SWITCHCAPVCC):
        """Initialize display."""
        # Save vcc state.
        self._vccstate = vccstate
        # Reset and initialize display.
        self._initialize()
        # Turn on the display.
        self.on()


    def on(self):
        self.write_command(SSD1306_DISPLAYON)

    def off(self):
        self.write_command(SSD1306_DISPLAYOFF)

    def display(self):
        """Write display buffer to physical display."""
        self.write_command(SSD1306_COLUMNADDR)
        self.write_command(0)              # Column start address. (0 = reset)
        self.write_command(self.width-1)   # Column end address.
        self.write_command(SSD1306_PAGEADDR)
        self.write_command(0)              # Page start address. (0 = reset)
        self.write_command(self._pages-1)  # Page end address.
        # Write buffer data.
        if self._spi is not None:
            # Set DC high for data.
            self._gpio.set_high(self._dc)
            # Write buffer.
            self._spi.write(self._buffer)
        else:
            for i in range(0, len(self._buffer), 16):
                control = 0x40   # Co = 0, DC = 0
                self._i2c._i2c_write_i2c_block_data(self.addr, control, self._buffer[i:i+16])

    def image(self, image):
        """Set buffer to value of Python Imaging Library image.  The image should
        be in 1 bit mode and a size equal to the display size.
        """
        if image.mode != '1':
            raise ValueError('Image must be in mode 1.')
        imwidth, imheight = image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display ({0}x{1}).' \
                .format(self.width, self.height))
        # Grab all the pixels from the image, faster than getpixel.
        pix = image.load()
        # Iterate through the memory pages
        index = 0
        for page in range(self._pages):
            # Iterate through all x axis columns.
            for x in range(self.width):
                # Set the bits for the column of pixels at the current position.
                bits = 0
                # Don't use range here as it's a bit slow
                for bit in [0, 1, 2, 3, 4, 5, 6, 7]:
                    bits = bits << 1
                    bits |= 0 if pix[(x, page*8+7-bit)] == 0 else 1
                # Update buffer byte and increment to next byte.
                self._buffer[index] = bits
                index += 1

    def clear(self):
        """Clear contents of image buffer."""
        self._buffer = [0x00]*(self.width*self._pages)

    def set_contrast(self, contrast):
        """Sets the contrast of the display.  Contrast should be a value between
        0 and 255."""
        if contrast < 0 or contrast > 255:
            raise ValueError('Contrast must be a value from 0 to 255 (inclusive).')
        self.write_command(SSD1306_SETCONTRAST)
        self.write_command(contrast)

    def dim(self, dim):
        """Adjusts contrast to dim the display if dim is True, otherwise sets the
        contrast to normal brightness if dim is False.
        """
        # Assume dim display.
        contrast = 0
        # Adjust contrast based on VCC if not dimming.
        if not dim:
            if self._vccstate == SSD1306_EXTERNALVCC:
                contrast = 0x9F
            else:
                contrast = 0xCF
            self.set_contrast(contrast)

class SSD1306_128_64(SSD1306Base):
    def __init__(self, dc=None, sclk=None, din=None, cs=None, gpio=None,
                 spi=None, i2c_bus=None, i2c_address=SSD1306_I2C_ADDRESS_1,
                 i2c=None):
        # Call base class constructor.
        super(SSD1306_128_64, self).__init__(128, 64, dc, sclk, din, cs,
                                             gpio, spi, i2c_bus, i2c_address, i2c)

    def _initialize(self):
        # 128x64 pixel specific initialization.
        self.write_command(SSD1306_DISPLAYOFF)                    # 0xAE
        self.write_command(SSD1306_SETDISPLAYCLOCKDIV)            # 0xD5
        self.write_command(0x80)                                  # the suggested ratio 0x80
        self.write_command(SSD1306_SETMULTIPLEX)                  # 0xA8
        self.write_command(0x3F)
        self.write_command(SSD1306_SETDISPLAYOFFSET)              # 0xD3
        self.write_command(0x0)                                   # no offset
        self.write_command(SSD1306_SETSTARTLINE | 0x0)            # line #0
        self.write_command(SSD1306_CHARGEPUMP)                    # 0x8D
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x10)
        else:
            self.write_command(0x14)
        self.write_command(SSD1306_MEMORYMODE)                    # 0x20
        self.write_command(0x00)                                  # 0x0 act like ks0108
        self.write_command(SSD1306_SEGREMAP | 0x1)
        self.write_command(SSD1306_COMSCANDEC)
        self.write_command(SSD1306_SETCOMPINS)                    # 0xDA
        self.write_command(0x12)
        self.write_command(SSD1306_SETCONTRAST)                   # 0x81
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x9F)
        else:
            self.write_command(0xCF)
        self.write_command(SSD1306_SETPRECHARGE)                  # 0xd9
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x22)
        else:
            self.write_command(0xF1)
        self.write_command(SSD1306_SETVCOMDETECT)                 # 0xDB
        self.write_command(0x40)
        self.write_command(SSD1306_DISPLAYALLON_RESUME)           # 0xA4
        self.write_command(SSD1306_NORMALDISPLAY)                 # 0xA6


class SSD1306_128_32(SSD1306Base):
    def __init__(self, dc=None, sclk=None, din=None, cs=None, gpio=None,
                 spi=None, i2c_bus=None, i2c_address=SSD1306_I2C_ADDRESS_1,
                 i2c=None):
        # Call base class constructor.
        super(SSD1306_128_32, self).__init__(128, 32, dc, sclk, din, cs,
                                             gpio, spi, i2c_bus, i2c_address, i2c)

    def _initialize(self):
        # 128x32 pixel specific initialization.
        self.write_command(SSD1306_DISPLAYOFF)                    # 0xAE
        self.write_command(SSD1306_SETDISPLAYCLOCKDIV)            # 0xD5
        self.write_command(0x80)                                  # the suggested ratio 0x80
        self.write_command(SSD1306_SETMULTIPLEX)                  # 0xA8
        self.write_command(0x1F)
        self.write_command(SSD1306_SETDISPLAYOFFSET)              # 0xD3
        self.write_command(0x0)                                   # no offset
        self.write_command(SSD1306_SETSTARTLINE | 0x0)            # line #0
        self.write_command(SSD1306_CHARGEPUMP)                    # 0x8D
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x10)
        else:
            self.write_command(0x14)
        self.write_command(SSD1306_MEMORYMODE)                    # 0x20
        self.write_command(0x00)                                  # 0x0 act like ks0108
        self.write_command(SSD1306_SEGREMAP | 0x1)
        self.write_command(SSD1306_COMSCANDEC)
        self.write_command(SSD1306_SETCOMPINS)                    # 0xDA
        self.write_command(0x02)
        self.write_command(SSD1306_SETCONTRAST)                   # 0x81
        self.write_command(0x8F)
        self.write_command(SSD1306_SETPRECHARGE)                  # 0xd9
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x22)
        else:
            self.write_command(0xF1)
        self.write_command(SSD1306_SETVCOMDETECT)                 # 0xDB
        self.write_command(0x40)
        self.write_command(SSD1306_DISPLAYALLON_RESUME)           # 0xA4
        self.write_command(SSD1306_NORMALDISPLAY)                 # 0xA6


class SSD1306_96_16(SSD1306Base):
    def __init__(self, dc=None, sclk=None, din=None, cs=None, gpio=None,
                 spi=None, i2c_bus=None, i2c_address=SSD1306_I2C_ADDRESS_1,
                 i2c=None):
        # Call base class constructor.
        super(SSD1306_96_16, self).__init__(96, 16, dc, sclk, din, cs,
                                            gpio, spi, i2c_bus, i2c_address, i2c)

    def _initialize(self):
        # 128x32 pixel specific initialization.
        self.write_command(SSD1306_DISPLAYOFF)                    # 0xAE
        self.write_command(SSD1306_SETDISPLAYCLOCKDIV)            # 0xD5
        self.write_command(0x60)                                  # the suggested ratio 0x60
        self.write_command(SSD1306_SETMULTIPLEX)                  # 0xA8
        self.write_command(0x0F)
        self.write_command(SSD1306_SETDISPLAYOFFSET)              # 0xD3
        self.write_command(0x0)                                   # no offset
        self.write_command(SSD1306_SETSTARTLINE | 0x0)            # line #0
        self.write_command(SSD1306_CHARGEPUMP)                    # 0x8D
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x10)
        else:
            self.write_command(0x14)
        self.write_command(SSD1306_MEMORYMODE)                    # 0x20
        self.write_command(0x00)                                  # 0x0 act like ks0108
        self.write_command(SSD1306_SEGREMAP | 0x1)
        self.write_command(SSD1306_COMSCANDEC)
        self.write_command(SSD1306_SETCOMPINS)                    # 0xDA
        self.write_command(0x02)
        self.write_command(SSD1306_SETCONTRAST)                   # 0x81
        self.write_command(0x8F)
        self.write_command(SSD1306_SETPRECHARGE)                  # 0xd9
        if self._vccstate == SSD1306_EXTERNALVCC:
            self.write_command(0x22)
        else:
            self.write_command(0xF1)
        self.write_command(SSD1306_SETVCOMDETECT)                 # 0xDB
        self.write_command(0x40)
        self.write_command(SSD1306_DISPLAYALLON_RESUME)           # 0xA4
        self.write_command(SSD1306_NORMALDISPLAY)                 # 0xA6


class OLED(object):
    def __init__(self):
        addresses = self.check_oled()
        if len(addresses) == 0:
            self.log.warning("No OLED found")
        else:
            self.oled = SSD1306_128_64(i2c_address=addresses[0])
            self.init()

    def is_ready(self):
        return self.oled is not None

    def check_oled(self):
        addressed = I2C.scan()
        result = []
        if SSD1306_I2C_ADDRESS_1 in addressed:
            result.append(SSD1306_I2C_ADDRESS_1)
        if SSD1306_I2C_ADDRESS_2 in addressed:
            result.append(SSD1306_I2C_ADDRESS_2)
        return result

    def init(self):
        self.width = self.oled.width
        self.height = self.oled.height
        self.oled.begin()
        self.oled.clear()
        self.oled.on()

        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font_8 = ImageFont.truetype(
            '/opt/%s/Minecraftia-Regular.ttf' % __app_name__, 8)
        self.font_12 = ImageFont.truetype(
            '/opt/%s/Minecraftia-Regular.ttf' % __app_name__, 12)

    def draw_text(self, text, x, y, fill=1):
        text = str(text)
        self.draw.text((x, y), text=text, font=self.font_8, fill=fill)

    def clear(self):
        self.oled.clear()

    def display(self):
        self.oled.image(self.image)
        self.oled.display()

    def off(self):
        self.oled.off()

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


