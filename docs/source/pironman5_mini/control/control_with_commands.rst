.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ情熱を持つ仲間たちと共に、Raspberry Pi・Arduino・ESP32の世界をさらに深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的課題を、コミュニティおよびサポートチームがサポートします。
    - **Learn & Share**：ヒントやチュートリアルを共有し、スキルの向上を目指しましょう。
    - **Exclusive Previews**：新製品の先行情報や発表をいち早く入手可能。
    - **Special Discounts**：最新製品の限定割引をご提供します。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンに参加できます。

    👉 一緒に創造と学びの旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _view_control_commands_mini:

コマンドによる制御
========================================
Pironman 5 Mini のデータをダッシュボードで表示・操作できるだけでなく、コマンドによっても制御可能です。

.. note::

  * **Home Assistant** システムでは、 ``http://<ip>:34001`` にアクセスしてダッシュボードからのみ操作が可能です。
  * 設定を変更した場合は、 ``pironman5 restart`` によるサービス再起動が必要です。再起動しないと変更は反映されません。

基本設定の確認
-----------------------------------

``pironman5`` モジュールには基本構成情報があり、以下のコマンドで確認できます。

.. code-block:: shell

  pironman5 -c

標準設定の例：

.. code-block::

  {
      "system": {
          "rgb_color": "feff00",
          "rgb_brightness": 30,
          "rgb_style": "hue_cycle",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 12,
          "temperature_unit": "C",
          "gpio_fan_pin": 5,
          "gpio_fan_mode": 0,
          "gpio_fan_led": "follow",
          "gpio_fan_led_pin": 6
      }
  }

用途に合わせて設定をカスタマイズしてください。

使用方法は ``pironman5`` または ``pironman5 -h`` で確認できます。

.. code-block::

  usage: pironman5-service [-h] [-v] [-c] [-dl {debug,info,warning,error,critical}] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]]
                                [-rp [RGB_SPEED]] [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]] [-fl [GPIO_FAN_LED]] [-fp [GPIO_FAN_LED_PIN]]
                                [--background [BACKGROUND]]
                                [{start,restart,stop}]

  Pironman5 Mini

  ositional arguments:
   {start,restart,stop}  Command

  ptions:
   -h, --help            show this help message and exit
   -v, --version         Show version
   -c, --config          Show config
   -dl {debug,info,warning,error,critical}, --debug-level {debug,info,warning,error,critical}
                         Debug level
   -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                         RGB color in hex format without # (e.g. 00aabb)
   -rb [RGB_BRIGHTNESS], --rgb-brightness [RGB_BRIGHTNESS]
                         RGB brightness 0-100
   -rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}], --rgb-style [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]
                         RGB style
   -rp [RGB_SPEED], --rgb-speed [RGB_SPEED]
                         RGB speed 0-100
   -re [RGB_ENABLE], --rgb-enable [RGB_ENABLE]
                         RGB enable True/False
   -rl [RGB_LED_COUNT], --rgb-led-count [RGB_LED_COUNT]
                         RGB LED count int
   -u [{C,F}], --temperature-unit [{C,F}]
                         Temperature unit
   -gm [GPIO_FAN_MODE], --gpio-fan-mode [GPIO_FAN_MODE]
                         GPIO fan mode, 0: Always On, 1: Performance, 2: Cool, 3: Balanced, 4: Quiet
   -gp [GPIO_FAN_PIN], --gpio-fan-pin [GPIO_FAN_PIN]
                         GPIO fan pin
   -fl [GPIO_FAN_LED], --gpio-fan-led [GPIO_FAN_LED]
                         GPIO fan LED state on/off/follow
   -fp [GPIO_FAN_LED_PIN], --gpio-fan-led-pin [GPIO_FAN_LED_PIN]
                         GPIO fan LED pin
   --background [BACKGROUND]
                         Run in background
.. note::

  ``pironman5.service`` の状態を変更した後は、以下のコマンドで再起動し、設定を反映させてください。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``systemctl`` ツールで ``pironman5`` のステータスを確認：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* またはログファイルを確認：

  .. code-block:: shell

    ls /var/log/pironman5/
    cat /var/log/pironman5/main.log

RGB LEDの制御
----------------------
基板には4つのWS2812 RGB LEDが搭載されており、点灯・消灯、色変更、明るさ調整、表示モード変更、速度設定が可能です。

.. note::

  ``pironman5.service`` の状態を変更するたびに、以下のコマンドを実行して設定を反映させる必要があります。

.. code-block:: shell

  sudo systemctl restart pironman5.service

* RGB LED のオン／オフを切り替えるには、 ``true`` で点灯、 ``false`` で消灯します。

.. code-block:: shell

  pironman5 -re true

* 色を変更するには、希望するカラーコード（例： ``fe1a1a``）を16進数で入力します。

.. code-block:: shell

  pironman5 -rc fe1a1a

* RGB LED の明るさを変更するには（範囲：0〜100%）：

.. code-block:: shell

  pironman5 -rb 100

* RGB LED の表示モードを変更するには、以下のモードから選択します： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle``

.. note::

  表示モードを ``rainbow``、 ``rainbow_reverse``、または ``hue_cycle`` に設定した場合、 ``pironman5 -rc`` を使用して色を変更することはできません。

.. code-block:: shell

  pironman5 -rs breathing

* RGB LED の変化速度を変更するには（範囲：0〜100%）：

.. code-block:: shell

  pironman5 -rp 80

* デフォルトでは4つのRGB LEDが搭載されています。追加のLEDを接続した場合は、以下のコマンドで個数を更新してください：

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan_mini:

RGBファンの制御
---------------------
IO拡張ボードは、5V 非PWMファンに対応しています。

.. note::

  ``pironman5.service`` の状態を変更した後は、以下のコマンドを実行して設定を反映させてください。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* RGBファンの動作モードを設定できます。各モードによりファンが動作する温度条件が異なります。

たとえば、 **1: Performance** モードに設定すると、RGBファンは50°Cで起動します。


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：70°Cで起動  
* **3: Balanced**：67.5°Cで起動  
* **2: Cool**：60°Cで起動  
* **1: Performance**：50°Cで起動  
* **0: Always On**：常時起動

* RGBファンの制御ピンを別のGPIOピンに接続している場合は、以下のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18
