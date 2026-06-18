.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



IOエキスパンダー
================

.. image:: img/io_board.png


RGB LED
------------

.. image:: img/io_board_rgb.png

このボードには、18個のWS2812BアドレッサブルRGB LEDが搭載されています。内訳は、6個がオンボード、12個がGPIOファンに統合されており、カスタマイズ可能な制御を実現します。ユーザーはそれらをオン/オフしたり、色を変更したり、明るさを調整したり、表示モードを切り替えたり、変化の速度を設定したりできます。






RGB制御ピン
-------------------------

RGB LEDはSPIによって駆動され、SPI MOSIピンでもある **GPIO10** に接続されています。表示されている2つのピンは、RGBをGPIO10に接続するために使用されます。必要ない場合は、ジャンパーを取り外すことができます。

  .. image:: img/io_board_rgb_pin.png

RGB OUTピン
-------------------------

.. image:: img/io_board_rgb_out.png

WS2812 RGB LEDはシリアル接続をサポートしており、外部RGB LEDストリップを取り付けることができます。拡張するには、 **SIG** ピンを外部ストリップの **DIN** ピンに接続します。

このボードには、18個のWS2812BアドレッサブルRGB LEDが搭載されています。内訳は、6個がオンボード、12個がGPIOファンに統合されており、カスタマイズ可能な制御を実現します。追加のLEDを接続し、以下のコマンドを使用して数を更新します：

.. code-block:: shell

  sudo pironman5 --rgb-led-count [数量]

例：

.. code-block:: shell

  sudo pironman5 --rgb-led-count 24



OLEDスクリーンコネクタ
----------------------------

アドレスが0x3CのOLEDスクリーンコネクタは、重要な機能です。

.. image:: img/io_board_oled.png

OLEDスクリーンが表示されない、または正しく表示されない場合は、以下の手順に従って問題をトラブルシューティングできます：

OLEDスクリーンのFPCケーブルが正しく接続されているか確認します。

#. 以下のコマンドを使用してプログラムの実行ログを表示し、エラーメッセージを確認します。

    .. code-block:: shell

        cat /var/log/pironman5/pironman5.log

#. または、以下のコマンドを使用して、OLEDのi2cアドレス0x3Cが認識されているか確認します：
    
    .. code-block:: shell
        
        sudo i2cdetect -y 1

#. 最初の2つの手順で問題が明らかにならない場合は、pironman5サービスを再起動して問題が解決するか確認します。


    .. code-block:: shell

        sudo systemctl restart pironman5.service



赤外線レシーバー
---------------------------

.. image:: img/io_board_receiver.png

* **モデル**: IRM-56384、38KHzで動作。
* **接続**: IRレシーバーは **GPIO13** に接続します。
* **D7**: 信号受信時に点滅する赤外線受信インジケーター。
* **J6**: 赤外線機能を有効にするためのピン。デフォルトではジャンパーキャップが挿入されており、即座に機能します。IRレシーバーを使用しない場合は、キャップを取り外してGPIO13を解放します。

IRレシーバーを利用するには、接続を確認し、必要なモジュールをインストールします：

* 接続をテストします：

  .. code-block:: shell

    sudo ls /dev |grep lirc

* ``lirc`` モジュールをインストールします：

  .. code-block:: shell

    sudo apt-get install lirc -y

* 次に、以下のコマンドを実行してIRレシーバーをテストします。

  .. code-block:: shell

    mode2 -d /dev/lirc0

* コマンド実行後、リモコンのボタンを押すと、そのボタンのコードが表示されます。


GPIOファンピン
---------------

.. image:: img/io_board_pin_fan.png

IO拡張ボードは、最大3基の5V CPUファンをサポートします。すべてのファンは一緒に制御されます。

ファン制御信号はIO拡張ボードの **FAN IN** ポートに接続され、その後3つの専用ファンポートから出力されます。これらのポートは上から **REAR UPPER**、 **REAR LOWER**、 **CPU FAN** と番号が付けられています。シルク印刷に従って接続してください。そうしないと、ファンのRGB制御に影響します。

ピンヘッダー
--------------

.. image:: img/io_board_pin_header.png

2つのライトアングルヘッダーコネクタがRaspberry PiのGPIOを拡張しますが、IRレシーバー、RGB LED、ファンがいくつかのピンを占有することに注意してください。これらのピンを他の機能に使用するには、対応するジャンパーキャップを取り外します。

.. list-table:: 
  :widths: 25 25
  :header-rows: 1

  * - Pironman 5 MAX
    - Raspberry Pi 5
  * - IRレシーバー（オプション）
    - GPIO13
  * - OLED SDA
    - SDA
  * - OLED SCL
    - SCL
  * - ファン（オプション）
    - GPIO6
  * - FLED（オプション）
    - GPIO5  
  * - RGB（オプション）
    - GPIO10