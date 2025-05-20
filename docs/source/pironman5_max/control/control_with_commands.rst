.. note:: 

    こんにちは！SunFounder の Facebook コミュニティ「Raspberry Pi & Arduino & ESP32 愛好者グループ」へようこそ！Raspberry Pi、Arduino、ESP32 に情熱を注ぐ仲間たちとともに、より深く学び、創造しましょう。

    **参加するメリット**

    - **専門サポート**：購入後の技術的な問題を、コミュニティとチームが協力してサポートします。
    - **学びと共有**：チュートリアルやヒントを交換し、スキルを高めましょう。
    - **新製品の先行プレビュー**：開発中の製品や情報をいち早く入手。
    - **限定割引**：最新製品を対象とした特別割引を提供。
    - **キャンペーン & プレゼント企画**：イベントやプレゼントに参加できます。

    👉 私たちと一緒に創造と探求の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _max_view_control_commands:

コマンドによる制御
========================================

ダッシュボードを使って Pironman 5 の各種デバイスを操作するだけでなく、コマンドでも制御できます。

.. note::

  * **Home Assistant** システムでは、 ``http://<ip>:34001`` にアクセスしてダッシュボードからのみ制御・監視が可能です。
  * **Batocera.linux** システムでは、コマンドからのみ操作が可能です。構成を変更した場合は ``pironman5 restart`` によるサービスの再起動が必要です。

基本設定の確認
-----------------------------------

``pironman5`` モジュールには、以下のコマンドで確認できる基本設定が含まれています。

.. code-block:: shell

  pironman5 -c

標準設定の例：

.. code-block:: 

  {
      "auto": {
          "rgb_color": "#0a1aff",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 4,
          "temperature_unit": "C",
          "gpio_fan_mode": 2,
          "gpio_fan_pin": 6
      }
  }

必要に応じて、これらの設定をカスタマイズしてください。

``pironman5`` または ``pironman5 -h`` を実行すると、使用方法が表示されます。

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc RGB_COLOR] [-rb RGB_BRIGHTNESS] [-rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}] [-rp RGB_SPEED] [-re RGB_ENABLE]
                          [-rl RGB_LED_COUNT] [-u {C,F}] [-gm GPIO_FAN_MODE] [-gp GPIO_FAN_PIN]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc RGB_COLOR, --rgb-color RGB_COLOR
                          RGB color
    -rb RGB_BRIGHTNESS, --rgb-brightness RGB_BRIGHTNESS
                          RGB brightness
    -rs {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}, --rgb-style {solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}
                          RGB style
    -rp RGB_SPEED, --rgb-speed RGB_SPEED
                          RGB speed
    -re RGB_ENABLE, --rgb-enable RGB_ENABLE
                          RGB enable
    -rl RGB_LED_COUNT, --rgb-led-count RGB_LED_COUNT
                          RGB LED count
    -u {C,F}, --temperature-unit {C,F}
                          Temperature unit
    -gm GPIO_FAN_MODE, --gpio-fan-mode GPIO_FAN_MODE
                          GPIO fan mode, 0-4, ['Always On', 'Performance', 'Cool', 'Balanced', 'Quiet']
    -gp GPIO_FAN_PIN, --gpio-fan-pin GPIO_FAN_PIN
                          GPIO fan pin



.. note::

  ``pironman5.service`` の状態を変更した後は、次のコマンドで設定を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``systemctl`` で ``pironman5`` のステータスを確認：

  .. code-block:: shell

    sudo systemctl status pironman5.service

* または、ログファイルを確認：

  .. code-block:: shell

    ls /var/log/pironman5/


RGB LED の制御
----------------------
ボードにはカスタマイズ可能な WS2812 RGB LED が4個搭載されており、点灯・消灯、色変更、明るさ調整、スタイル変更、変化速度の設定が可能です。

.. note::

``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには、以下のコマンドを実行してください。

.. code-block:: shell

    sudo systemctl restart pironman5.service

* RGB LEDのオン・オフ状態を変更するには、 ``true`` で点灯、 ``false`` で消灯となります。

.. code-block:: shell

  pironman5 -re true

* 色変更（例： ``fe1a1a``）：

.. code-block:: shell

  pironman5 -rc fe1a1a

* 明るさ変更（0〜100%）：

.. code-block:: shell

  pironman5 -rb 100

* RGB LEDの表示モードを切り替えるには、次のオプションから選択してください： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` 。

.. note::

  スタイルを ``rainbow`` 、 ``rainbow_reverse`` 、 ``hue_cycle`` に設定した場合は、 ``pironman5 -rc`` による色変更は無効になります。

.. code-block:: shell

  pironman5 -rs breathing

* 変化速度の設定（0〜100%）：

.. code-block:: shell

  pironman5 -rp 80

* デフォルトは4個のLED。LED数を変更するには：

.. code-block:: shell

  pironman5 -rl 12

.. _max_cc_control_fan:

RGBファンの制御
---------------------
IO拡張ボードは最大2基の5V非PWMファンに対応し、同時制御されます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、設定の変更を反映させるには次のコマンドを実行する必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* RGBファンの動作モードを設定可能：

例： **1: Performance** に設定すると、50℃で起動します。


.. code-block:: shell

  sudo pironman5 -gm 3

* **4: Quiet**：70℃で起動  
* **3: Balanced**：67.5℃で起動  
* **2: Cool**：60℃で起動  
* **1: Performance**：50℃で起動  
* **0: Always On**：常に起動状態  

* RGBファンの制御ピンをRaspberry Piの別のピンに接続する場合は、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18


OLED画面の確認
-----------------------------------

``pironman5`` ライブラリをインストールすると、CPU・RAM・ディスク使用量・CPU温度・IPアドレスなどが再起動時にOLED画面へ表示されます。

表示されない場合は、まずFPCケーブルの接続状態を確認してください。

次にログを確認：

.. code-block:: shell

  cat /var/log/pironman5/pm_auto.oled.log

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

