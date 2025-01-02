.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターセールスの問題や技術的な課題を解決。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

IOエクスパンダー
===================

RGB LED
--------------

.. image:: img/io_board_rgb.png

このボードには4つのWS2812 RGB LEDが搭載されており、カスタマイズが可能です。ユーザーはLEDのオン/オフ、色の変更、明るさの調整、表示モードの切り替え、変化速度の設定を行うことができます。

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

RGB制御ピン
-------------------------

RGB LEDはSPIによって駆動され、 **GPIO10** （SPI MOSIピンでもある）に接続されています。J9上部の2つのピンは、RGB LEDをGPIO10に接続するために使用されます。不要な場合は、ジャンパーを取り外すことができます。

  .. image:: img/io_board_rgb_pin.png

RGB OUTピン
-------------------------

.. image:: img/io_board_rgb_out.png

WS2812 RGB LEDはシリアル接続をサポートしており、外部のRGB LEDストリップを接続することが可能です。 **SIG** ピンを外部ストリップの **DIN** ピンに接続して拡張できます。

デフォルト設定では4つのRGB LEDが含まれています。追加のLEDを接続し、以下のコマンドで数を更新します：

.. code-block:: shell

  pironman5 -rl 12


OLEDスクリーンコネクター
----------------------------

OLEDスクリーンコネクターは、アドレス0x3Cで動作します。

.. image:: img/io_board_oled.png

OLEDスクリーンが表示されない、または正しく表示されていない場合は、以下の手順で問題を解決できます。

OLEDスクリーンのFPCケーブルが正しく接続されているか確認してください。

#. 次のコマンドを使用して、プログラムの実行ログを表示し、エラーメッセージを確認します。

    .. code-block:: shell

        cat /opt/pironman5/log

#. もしくは、次のコマンドでOLEDのi2cアドレス0x3Cが認識されているか確認します。
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. 上記の手順で問題が解決しない場合は、pironman5サービスを再起動してみてください。


    .. code-block:: shell

        sudo systemctl restart pironman5.service


赤外線受信機
---------------------------

.. image:: img/io_board_receiver.png

* **モデル**: IRM-56384、38KHzで動作。
* **接続**: 赤外線受信機は **GPIO13** に接続されます。
* **D1**: 信号検出時に点滅する赤外線受信インジケーター。
* **J8**: 赤外線機能を有効にするためのピン。デフォルトではジャンパーキャップが挿入されており、すぐに機能します。IR受信機を使用しない場合は、ジャンパーキャップを取り外してGPIO13を解放できます。

赤外線受信機を使用するには、接続を確認し、必要なモジュールをインストールしてください。

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


RGBファンピン
---------------

IO拡張ボードは最大2つの5V非PWMファンをサポートしています。両方のファンは一緒に制御されます。

**FAN1** と **FAN 2** は2セットのファンピンです。ファンの赤い線を「+」、黒い線を「-」に接続する必要があります。

.. image:: img/io_board_fan.png

J9の下にある2つのピンはRGBファン用の有効化ピンです。デフォルトではこれらのピンにジャンパーが挿入されており、GPIO6を使用してファンのオンオフを制御できます。ファンの動作が不要な場合は、ジャンパーを取り外してGPIO6を解放します。

.. image:: img/io_board_fan_j9.png

**D2** はファンが動作中であることを示す信号インジケーターです。

.. image:: img/io_board_fan_d2.png

2つのRGBファンの動作モードを設定するためのコマンドを使用できます。これらのモードは、RGBファンが作動する条件を決定します。

例えば、 **1: パフォーマンス** モードに設定すると、RGBファンは50°Cで作動します。

.. code-block:: shell

  pironman5 -gm 3

* **4: 静音**: RGBファンは70°Cで作動します。
* **3: バランス**: RGBファンは67.5°Cで作動します。
* **2: 冷却**: RGBファンは60°Cで作動します。
* **1: パフォーマンス**: RGBファンは50°Cで作動します。
* **0: 常時オン**: RGBファンは常に作動します。

RGBファンの制御ピンをRaspberry Piの他のピンに接続した場合、次のコマンドでピン番号を変更できます。

.. code-block:: shell

  sudo pironman5 -gp 18

ピンヘッダー
-----------------

.. image:: img/io_board_pin_header.png

2つの直角ヘッダーコネクターがRaspberry PiのGPIOを拡張しますが、赤外線受信機、RGB LED、ファンは一部のピンを占有しています。これらのピンを他の機能に利用するには、対応するジャンパーキャップを取り外してください。

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5
    - Raspberry Pi 5
  * - 赤外線受信機（オプション）
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - ファン（オプション）
    - GPIO6
  * - RGB（オプション）
    - GPIO10
  * - RGB（オプション）
    - GPIO12
  * - RGB（オプション）
    - GPIO21
