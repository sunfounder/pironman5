.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _view_control_commands_5:

コマンドによる制御
========================================
Pironman 5のデータを確認し、さまざまなデバイスをダッシュボードで制御するだけでなく、コマンドを使用しても制御できます。

.. note::

  * **Home Assistant** システムの場合、 ``http://<ip>:34001`` を開いてダッシュボードを通じてのみPironman 5を監視および制御することができます。

基本設定の確認
-----------------------------------

``pironman5`` モジュールはPironman用の基本設定を提供しており、以下のコマンドで確認できます。

.. code-block:: shell

  sudo pironman5 -c

標準の設定は次のように表示されます：

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
          "debug_level": "INFO"
      }
  }

これらの設定をニーズに合わせてカスタマイズできます。

``pironman5`` または ``pironman5 -h`` を使用して指示を確認してください。

.. code-block::


  usage: pironman5-service [-h] [-v] [-c] [-dl [{debug,info,warning,error,critical}]] [--background [BACKGROUND]] [-rd] [-cp [CONFIG_PATH]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-oe [OLED_ENABLE]]
                          [-od [OLED_DISK]] [-oi [OLED_NETWORK_INTERFACE]] [-or [{0,180}]]
                          [{start,restart,stop}]

  Pironman 5 command line interface

  positional arguments:
    {start,restart,stop}  Command

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

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``pironman5`` プログラムのステータスを ``systemctl`` ツールを使って確認してください。

  .. code-block:: shell

    sudo systemctl status pironman5.service

* もしくは、プログラムが生成したログファイルを確認してください。

  .. code-block:: shell

    cat /var/log/pironman5/pironman5.log


RGB LEDの制御
----------------------
このボードには4つのWS2812 RGB LEDが搭載されており、カスタマイズが可能です。ユーザーはLEDのオン/オフ、色の変更、明るさの調整、RGB LED表示モードの切り替え、そして変化速度の設定を行うことができます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* RGB LEDのオン/オフを切り替えるには、 ``true`` でオン、 ``false`` でオフにします。

.. code-block:: shell

  sudo pironman5 -re true

* 色を変更するには、目的の16進数の色値を入力します。例： ``fe1a1a``

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* RGB LEDの明るさを変更するには（範囲: 0 ~ 100%）：

.. code-block:: shell

  sudo pironman5 -rb 100

* RGB LEDの表示モードを切り替えるには、次のオプションから選択します： ``solid`` / ``breathing`` / ``flow`` / ``flow_reverse`` / ``rainbow`` / ``rainbow_reverse`` / ``hue_cycle``

.. note::

  RGB LEDの表示モードを ``rainbow``、 ``rainbow_reverse``、または ``hue_cycle`` に設定した場合、 ``pironman5 -rc`` で色を設定することはできません。

.. code-block:: shell

  sudo pironman5 -rs breathing

* 変化速度を変更するには（範囲: 0 ~ 100%）：

.. code-block:: shell

  sudo pironman5 -rp 80

* デフォルト設定では4つのRGB LEDが含まれています。追加のLEDを接続し、以下のコマンドで数を更新します：

.. code-block:: shell

  sudo pironman5 -rl 12


.. _cc_control_fan:

GPIOファンの制御
---------------------
IO拡張ボードは最大2つの5V非CPUファンをサポートしています。両方のファンは一緒に制御されます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 2つのGPIOファンの動作モードを設定するためのコマンドを使用できます。これらのモードは、GPIOファンが作動する温度しきい値を決定します。

例えば、 **1: パフォーマンス** モードに設定すると、GPIOファンは ``50°C`` で作動します。

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: 静音**: GPIOファンは ``70°C`` で作動します。
* **3: バランス**: GPIOファンは ``67.5°C`` で作動します。
* **2: 冷却**: GPIOファンは ``60°C`` で作動します。
* **1: パフォーマンス**: GPIOファンは ``50°C`` で作動します。
* **0: 常時オン**: GPIOファンは常に作動します。

* GPIOファンの制御ピンをRaspberry Piの他のピンに接続した場合、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18


CPUファンについて
------------------------

CPUファンは、Raspberry Pi 5の専用4ピンCPUファンポートに接続します。

デフォルトの制御方式は、ファームウェアによって管理され、CPU温度に基づく多段階のインテリジェントな速度調整スキームです。公式または互換性のあるCPUファンを正しく接続して使用する場合、システムはCPU温度の変化（50°C以上で作動開始）に応じてファン速度を自動的に調整するため、手動での介入は必要ありません。


OLEDスクリーンの確認
-----------------------------------

``pironman5`` ライブラリをインストールすると、OLEDスクリーンにCPU使用率、RAM使用量、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示され、再起動するたびに自動的に表示されます。

OLEDスクリーンにコンテンツが表示されない場合は、まずOLEDのFPCケーブルが正しく接続されているか確認してください。

次に、以下のコマンドを使用して、プログラムのログを確認し、問題を特定できます：

.. code-block:: shell

  cat /var/log/pironman5/pironman5.log

また、OLEDのI2Cアドレス ``0x3C`` が認識されているか確認してください：

.. code-block:: shell

  i2cdetect -y 1


赤外線受信機の確認
---------------------------------------

* ``lirc`` モジュールをインストールします：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 次のコマンドを実行して赤外線受信機をテストします：

  .. code-block:: shell

    mode2 -d /dev/lirc0

* コマンド実行後、リモコンのボタンを押すと、そのボタンのコードが表示されます。
