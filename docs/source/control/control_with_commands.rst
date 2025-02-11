.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

.. _view_control_commands:

コマンドによる制御
========================================
Pironman 5のデータを確認し、さまざまなデバイスをダッシュボードで制御するだけでなく、コマンドを使用しても制御できます。

.. note::

  * **Home Assistant** システムの場合、 ``http://<ip>:34001`` を開いてダッシュボードを通じてのみPironman 5を監視および制御することができます。
  * **Batocera.linux** システムの場合、コマンドを使用してのみPironman 5を監視および制御できます。設定の変更を反映させるには、 ``pironman5 restart`` コマンドを使用してサービスを再起動する必要があることに注意してください。


基本設定の確認
-----------------------------------

``pironman5`` モジュールはPironman用の基本設定を提供しており、以下のコマンドで確認できます。

.. code-block:: shell

  pironman5 -c

標準の設定は次のように表示されます：

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

これらの設定をニーズに合わせてカスタマイズできます。

``pironman5`` または ``pironman5 -h`` を使用して指示を確認してください。

.. code-block::

  usage: pironman5-service [-h] [-c] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]]
                          [-rs [{solid,breathing,flow,flow_reverse,rainbow,rainbow_reverse,hue_cycle}]] [-rp [RGB_SPEED]]
                          [-re [RGB_ENABLE]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-gm [GPIO_FAN_MODE]] [-gp [GPIO_FAN_PIN]]
                          [{start,stop}]

  Pironman5

  positional arguments:
    {start,stop}          Command

  options:
    -h, --help            show this help message and exit
    -c, --config          Show config
    -rc [RGB_COLOR], --rgb-color [RGB_COLOR]
                          RGB color in hex format with or without # (e.g. #FF0000 or 00aabb)
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

.. note::

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``pironman5`` プログラムのステータスを ``systemctl`` ツールを使って確認してください。

  .. code-block:: shell

    sudo systemctl status pironman5.service

* もしくは、プログラムが生成したログファイルを確認してください。

  .. code-block:: shell

    cat /opt/pironman5/log


RGB LEDの制御
----------------------
このボードには4つのWS2812 RGB LEDが搭載されており、カスタマイズが可能です。ユーザーはLEDのオン/オフ、色の変更、明るさの調整、RGB LED表示モードの切り替え、そして変化速度の設定を行うことができます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* RGB LEDのオン/オフを切り替えるには、 ``true`` でオン、 ``false`` でオフにします。

.. code-block:: shell

  pironman5 -re true

* 色を変更するには、目的の16進数の色値を入力します。例： ``fe1a1a`` 

.. code-block:: shell

  pironman5 -rc fe1a1a

* RGB LEDの明るさを変更するには（範囲: 0 ~ 100%）：

.. code-block:: shell

  pironman5 -rb 100

* RGB LEDの表示モードを切り替えるには、次のオプションから選択します： ``solid/breathing/flow/flow_reverse/rainbow/rainbow_reverse/hue_cycle`` 

.. note::

  RGB LEDの表示モードを ``rainbow`` , ``rainbow_reverse`` , ``hue_cycle`` に設定した場合、 ``pironman5 -rc`` で色を設定することはできません。

.. code-block:: shell

  pironman5 -rs breathing

* 変化速度を変更するには（範囲: 0 ~ 100%）：

.. code-block:: shell

  pironman5 -rp 80

* デフォルト設定では4つのRGB LEDが含まれています。追加のLEDを接続し、以下のコマンドで数を更新します：

.. code-block:: shell

  pironman5 -rl 12

.. _cc_control_fan:

RGBファンの制御
---------------------
IO拡張ボードは最大2つの5V非PWMファンをサポートしています。両方のファンは一緒に制御されます。

.. note::

  ``pironman5.service`` のステータスを変更するたびに、以下のコマンドを使用して設定変更を反映させる必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* 2つのRGBファンの動作モードを設定するためのコマンドを使用できます。これらのモードは、RGBファンが作動する条件を決定します。

例えば、 **1: パフォーマンス** モードに設定すると、RGBファンは50°Cで作動します。

.. code-block:: shell

  sudo pironman5 -gm 3

* **4: 静音**: RGBファンは70°Cで作動します。
* **3: バランス**: RGBファンは67.5°Cで作動します。
* **2: 冷却**: RGBファンは60°Cで作動します。
* **1: パフォーマンス**: RGBファンは50°Cで作動します。
* **0: 常時オン**: RGBファンは常に作動します。

* RGBファンの制御ピンをRaspberry Piの他のピンに接続した場合、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18


OLEDスクリーンの確認
-----------------------------------

``pironman5`` ライブラリをインストールすると、OLEDスクリーンにCPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示され、再起動するたびにこれが表示されます。

OLEDスクリーンにコンテンツが表示されない場合は、まずOLEDのFPCケーブルが正しく接続されているか確認してください。

次に、以下のコマンドを使用して、プログラムのログを確認し、問題が何であるかを確認できます。

.. code-block:: shell

  cat /var/log/pironman5/

また、OLEDのi2cアドレス0x3Cが認識されているか確認してください：

.. code-block:: shell

  i2cdetect -y 1

赤外線受信機の確認
---------------------------------------

赤外線受信機を利用するには、接続を確認し、必要なモジュールをインストールしてください。

* 接続をテストします：

  .. code-block:: shell

    sudo ls /dev |grep lirc

* ``lirc`` モジュールをインストールします：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 次のコマンドを実行して赤外線受信機をテストします。

  .. code-block:: shell

    mode2 -d /dev/lirc0

* コマンド実行後、リモコンのボタンを押すと、そのボタンのコードが表示されます。
