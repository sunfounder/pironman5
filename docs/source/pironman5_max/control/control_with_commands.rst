.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _max_view_control_commands:

コマンドによる制御
========================================

ダッシュボードを使って Pironman 5 MAX のデータを確認し、さまざまなデバイスを制御するだけでなく、コマンドでも制御できます。

.. note::

  * **Home Assistant** システムでは、 ``http://<ip>:34001`` にアクセスしてダッシュボードからのみ制御・監視が可能です。

基本設定の確認
-----------------------------------

``pironman5`` モジュールには、以下のコマンドで確認できる基本設定が含まれています。

.. code-block:: shell

  sudo pironman5 -c

標準設定の例：

.. code-block::

  {
      "system": {
          "data_interval": 1,
          "database_retention_days": 30,
          "temperature_unit": "C",
          "enable_history": true,
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "rgb_enable": true,
          "rgb_color": "#0a1aff",
          "rgb_brightness": 100,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_led_count": 4,
          "rgb_led_count_min": 4,
          "gpio_fan_pin": 6,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "on",
          "gpio_fan_led_pin": 5,
          "debug_level": "INFO"
      }
  }

必要に応じて、これらの設定をカスタマイズしてください。

``pironman5`` または ``pironman5 -h`` を実行すると、使用方法が表示されます。

.. code-block::

    usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]] [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]]
                    [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]] [-oe [OLED_ENABLE]] [-or [{0,180}]]
                    [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                    {start,stop,launch-browser} ...

    Pironman 5 Max command line interface

    options:
      -h, --help            show this help message and exit
      -v, --version         Show version
      -c, --config          Show config
      -drd, --database-retention-days [DATABASE_RETENTION_DAYS]
                            Database retention days
      -dl, --debug-level [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]
                            Debug level
      -rd, --remove-dashboard
                            Remove dashboard
      -cp, --config-path [CONFIG_PATH]
                            Config path
      -eh, --enable-history [ENABLE_HISTORY]
                            Enable history, True/true/on/On/1 or False/false/off/Off/0
      -re, --rgb-enable [RGB_ENABLE]
                            RGB enable True/False
      -rs, --rgb-style [RGB_STYLE]
                            RGB style: ['solid', 'breathing', 'flow', 'flow_reverse', 'rainbow', 'rainbow_reverse', 'hue_cycle']
      -rc, --rgb-color [RGB_COLOR]
                            RGB color in hex format without # (e.g. 00aabb)
      -rb, --rgb-brightness [RGB_BRIGHTNESS]
                            RGB brightness 0-100
      -rp, --rgb-speed [RGB_SPEED]
                            RGB speed 0-100
      -rl, --rgb-led-count [RGB_LED_COUNT]
                            RGB LED count int
      -u, --temperature-unit [{C,F}]
                            Temperature unit
      -gm, --gpio-fan-mode [GPIO_FAN_MODE]
                            GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
      -gp, --gpio-fan-pin [GPIO_FAN_PIN]
                            GPIO fan pin
      -fl, --gpio-fan-led [GPIO_FAN_LED]
                            GPIO fan LED state on/off/follow
      -fp, --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                            GPIO fan LED pin
      -oe, --oled-enable [OLED_ENABLE]
                            OLED enable True/true/on/On/1 or False/false/off/Off/0
      -or, --oled-rotation [{0,180}]
                            Set to rotate OLED display, 0, 180
      -op, --oled-pages [OLED_PAGES]
                            OLED pages, split by ',': mix,performance,ips,disk
      -os, --oled-sleep-timeout [OLED_SLEEP_TIMEOUT]
                            OLED sleep timeout in seconds

    Subcommands:
      {start,stop,launch-browser}
        start               Start Pironman5
        stop                Stop Pironman5
        launch-browser      Launch browser

.. note::

  ``pironman5.service`` の状態を変更した後は、次のコマンドで設定を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``systemctl`` で ``pironman5`` のステータスを確認：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* または、プログラムが生成したログを確認：

  .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


RGB LED の制御
----------------------
ボードにはカスタマイズ可能な WS2812 RGB LED が4個搭載されており、点灯・消灯、色変更、明るさ調整、スタイル変更、変化速度の設定が可能です。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには、以下のコマンドを実行してください。

.. code-block:: shell

    sudo systemctl restart pironman5.service

* RGB LEDのオン・オフ状態を変更するには、 ``true`` で点灯、 ``false`` で消灯となります。

.. code-block:: shell

  sudo pironman5 -re true

* 色変更（例： ``fe1a1a``）：

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* 明るさ変更（0〜100%）：

.. code-block:: shell

  sudo pironman5 -rb 100

* RGB LEDの表示モードを切り替えるには、次のオプションから選択してください： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` 。

.. note::

  スタイルを ``rainbow``、 ``rainbow_reverse``、または ``hue_cycle`` に設定した場合は、 ``pironman5 -rc`` による色変更は無効になります。

.. code-block:: shell

  sudo pironman5 -rs breathing

* 変化速度の設定（0〜100%）：

.. code-block:: shell

  sudo pironman5 -rp 80

* デフォルトは4個のLED。LED数を変更するには：

.. code-block:: shell

  sudo pironman5 -rl 12

.. _cc_control_fan_max:

GPIOファンの制御
---------------------
IO拡張ボードは最大2基の5V非CPUファンに対応し、同時制御されます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには次のコマンドを実行する必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* GPIOファンの動作モードを設定可能です。これらのモードは、GPIOファンが作動する温度しきい値を決定します。

例： **1: Performance** に設定すると、GPIOファンは50°Cで起動します。

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：GPIOファンは70°Cで起動します。
* **3: Balanced**：GPIOファンは67.5°Cで起動します。
* **2: Cool**：GPIOファンは60°Cで起動します。
* **1: Performance**：GPIOファンは50°Cで起動します。
* **0: Always On**：GPIOファンは常に起動します。

* GPIOファンの制御ピンをRaspberry Piの別のピンに接続する場合は、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18


**CPUファンについて**

CPUファンは、Raspberry Pi 5の専用4ピンCPUファン端子に接続します。その標準の制御方式は、ファームウェアによって管理され、CPU温度に基づく多段階の知的回転数調整機構です。つまり、公式または互換性のあるCPUファンを正しく接続して使用する場合、システムはCPU温度の変化に応じてファン回転数を自動的に調整し（50°C以上で作動を開始）、利用者の手動介入は一切不要です。


OLED画面の確認
-----------------------------------

``pironman5`` ライブラリをインストールすると、CPU使用率、RAM使用量、ディスク使用量、CPU温度、IPアドレスなどが再起動時にOLED画面へ表示されます。

表示されない場合は、まずFPCケーブルの接続状態を確認してください。

次にログを確認：

.. code-block:: shell

  cat /var/log/pironman5/pironman5.log

I2Cアドレス 0x3C が認識されているか確認：

.. code-block:: shell

  i2cdetect -y 1

赤外線受信モジュールの確認
---------------------------------------

* ``lirc`` モジュールのインストール：

  .. code-block:: shell

    sudo apt-get install lirc -y

* IR受信確認：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* コマンド実行後にリモコンのボタンを押すと、そのボタンに対応するコードが表示されます。
