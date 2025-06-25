```bash
usage: pironman5 [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [-rd]
                 [-cp [CONFIG_PATH]] [-eh [ENABLE_HISTORY]] [-u [{C,F}]]
                 [-oe [OLED_ENABLE]] [-or [{0,180}]] [-os [OLED_SLEEP_TIMEOUT]]     
                 [-rmc [RGB_MATRIX_COLOR]] [-rmb [RGB_MATRIX_BRIGHTNESS]]
                 [-rms [{solid,breathing,rainbow,rotate,rotate_dual,rotate_hsv,rotate_hsv_2}]]
                 [-rmp [RGB_MATRIX_SPEED]] [-rme [RGB_MATRIX_ENABLE]]
                 [{start,restart,stop}]

Pironman 5 UPS command line interface

positional arguments:
  {start,restart,stop}  Command

options:
  -h, --help            show this help message and exit
  -v, --version         Show version
  -c, --config          Show config
  -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                        Debug level
  -rd, --remove-dashboard
                        Remove dashboard
  -cp [CONFIG_PATH], --config-path [CONFIG_PATH]
                        Config path
  -eh [ENABLE_HISTORY], --enable-history [ENABLE_HISTORY]
                        Enable history, True/true/on/On/1 or False/false/off/Off/0  
  -u [{C,F}], --temperature-unit [{C,F}]
                        Temperature unit
  -oe [OLED_ENABLE], --oled-enable [OLED_ENABLE]
                        OLED enable True/true/on/On/1 or False/false/off/Off/0      
  -or [{0,180}], --oled-rotation [{0,180}]
                        Set to rotate OLED display, 0, 180
  -os [OLED_SLEEP_TIMEOUT], --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                        OLED sleep timeout in seconds
  -rmc [RGB_MATRIX_COLOR], --rgb-matrix-color [RGB_MATRIX_COLOR]
                        RGB color in hex format without # (e.g. 00aabb)
  -rmb [RGB_MATRIX_BRIGHTNESS], --rgb-matrix-brightness [RGB_MATRIX_BRIGHTNESS]     
                        RGB brightness 0-100
  -rms [{solid,breathing,rainbow,rotate,rotate_dual,rotate_hsv,rotate_hsv_2}], --rgb-matrix-style [{solid,breathing,rainbow,rotate,rotate_dual,rotate_hsv,rotate_hsv_2}]
                        RGB style
  -rmp [RGB_MATRIX_SPEED], --rgb-matrix-speed [RGB_MATRIX_SPEED]
                        RGB speed 0-100
  -rme [RGB_MATRIX_ENABLE], --rgb-matrix-enable [RGB_MATRIX_ENABLE]
                        RGB enable True/False

```