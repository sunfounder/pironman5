.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_view_control_commands:

コマンドによる制御
========================================
Pironman 5 Pro MAX のデータ表示や各種デバイスの制御は、ダッシュボード経由だけでなく、コマンドを使用しても行うことができます。

基本設定の表示
-----------------------------------

``pironman5`` モジュールは Pironman の基本設定を提供しており、以下のコマンドで確認できます。

.. code-block:: shell

  sudo pironman5 -c

標準設定は以下のように表示されます：

.. code-block:: 

  {
      "system": {
          "data_interval": 1,
          "enable_history": true,
          "rgb_color": "#ff3dbe",
          "rgb_brightness": 50,
          "rgb_style": "breathing",
          "rgb_speed": 50,
          "rgb_enable": true,
          "rgb_led_count": 18,
          "temperature_unit": "C",
          "oled_enable": true,
          "oled_rotation": 0,
          "oled_sleep_timeout": 10,
          "default_dashboard_page": "small",
          "oled_pages": [
              "mix",
              "performance",
              "ips",
              "disk"
          ],
          "debug_level": "INFO"
      }
  }

これらの設定は、必要に応じてカスタマイズできます。

``pironman5`` または ``pironman5 -h`` で使用方法を確認してください。

.. code-block::

  usage: pironman5 [-h] [-v] [-c] [-drd [DATABASE_RETENTION_DAYS]] [-dl [{DEBUG,INFO,WARNING,ERROR,CRITICAL,debug,info,warning,error,critical}]] [-rd] [-cp [CONFIG_PATH]]
                  [-eh [ENABLE_HISTORY]] [-re [RGB_ENABLE]] [-rs [RGB_STYLE]] [-rc [RGB_COLOR]] [-rb [RGB_BRIGHTNESS]] [-rp [RGB_SPEED]] [-rl [RGB_LED_COUNT]] [-u [{C,F}]] [-oe [OLED_ENABLE]]
                  [-or [{0,180}]] [-op [OLED_PAGES]] [-os [OLED_SLEEP_TIMEOUT]]
                  {start,stop,launch-browser} ...

  Pironman 5 Pro Max command line interface

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

  ``pironman5.service`` の状態を変更するたびに、設定変更を有効にするために以下のコマンドを使用する必要があります。

  .. code-block:: shell

    sudo systemctl restart pironman5.service


* ``systemctl`` ツールを使用して ``pironman5`` プログラムの状態を確認します。

  .. code-block:: shell

    sudo systemctl status pironman5.service

* または、プログラムが生成するログファイルを確認します。

  .. code-block:: shell

    ls /var/log/pironman5/


RGB LEDの制御
----------------------
ボードには18基のWS2812BアドレッサブルRGB LEDが搭載されています：6基がオンボード、12基がGPIOファンに内蔵されています。ユーザーは電源、色、明るさ、表示モード、アニメーション速度、アクティブなLEDの数を制御できます。

.. note::

  ``pironman5.service`` の設定を変更した後は、変更を有効にするためにサービスを再起動する必要があります：

  .. code-block:: shell

    sudo systemctl restart pironman5.service

* **RGB LEDの有効化／無効化**： ``true`` でオン、 ``false`` でオフにします。

.. code-block:: shell

  sudo pironman5 -re true

* **色の変更**：16進数値（ `#` なし）で色を設定します。例：赤色の場合は ``fe1a1a`` 。

.. code-block:: shell

  sudo pironman5 -rc fe1a1a

* **明るさの調整**：0%から100%の間で明るさを設定します。

.. code-block:: shell

  sudo pironman5 -rb 75

* **表示モードの変更**：以下のアニメーションモードから選択できます：

  * ``solid`` ： 単色表示。
  * ``breathing`` ： フェードイン／フェードアウトを繰り返す呼吸モード。
  * ``flow`` ／ ``flow_reverse`` ： 一方向に色が流れるモード。
  * ``rainbow`` ／ ``rainbow_reverse`` ： レインボースペクトラムを循環させるモード。
  * ``hue_cycle`` ： 色相値をスムーズに循環させるモード。

.. code-block:: shell

  sudo pironman5 -rs breathing

.. note::

  ``rainbow`` 、 ``rainbow_reverse`` 、または ``hue_cycle`` モードを使用する場合、 ``pironman5 -rc`` で設定した色は、モードによる自動的な色の循環によって上書きされます。

* **アニメーション速度の調整**：効果の速度を0%（最遅）から100%（最速）の間で制御します。

.. code-block:: shell

  sudo pironman5 -rp 50

* **LED数の設定**：システムはデフォルトで18個のLEDを制御します。追加の外部WS2812B LEDでチェーンを拡張した場合は、それに応じて総数を更新します。

.. code-block:: shell

  sudo pironman5 -rl 12


ファン
--------------------------------

これらのファンは、Raspberry Pi 5の専用4ピンCPUファンポートに接続します。デフォルトの制御方式は、CPU温度に基づいたファームウェアによる多段階のインテリジェントな速度調整です。つまり、公式または互換性のあるCPUファンを正しく接続すれば、CPU温度の変化（50℃を超えると動作開始）に応じて、システムがファン速度を自動的に調整します。ユーザーによる手動操作は一切不要です。


OLED画面の確認
-----------------------------------

0.96インチのOLED画面は、 ``pironman5`` ライブラリをインストールして再起動すると、デフォルトでシステム情報（CPU、RAM、ディスク、温度、IP）を表示します。

OLED画面が表示されない場合：

1. OLEDのFPCケーブルがメインボードに確実に接続されていることを確認します。
2. サービスのログでエラーを確認します：

    .. code-block:: shell

      sudo journalctl -u pironman5.service -f

    または、OLED固有のログを確認します：

    .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

3. I2Cバス上でOLEDが検出されていることを確認します（アドレス `0x3C` ）：

    .. code-block:: shell

      i2cdetect -y 1

**OLED設定コマンド**

* **OLEDの有効化／無効化**：OLEDディスプレイをオンまたはオフにします。

    .. code-block:: shell

      sudo pironman5 -oe false

* **画面の回転**：画面の向きを ``0`` （デフォルト）または ``180`` 度に設定します。

    .. code-block:: shell

      sudo pironman5 -or 180

* **表示ページの設定**：循環表示する情報ページを選択します。ページは： ``mix`` （概要）、 ``performance`` （詳細なCPU/RAM）、 ``ips`` （ネットワークIP）、 ``disk`` （ストレージ）です。複数のページはカンマで区切ります。

    .. code-block:: shell

      sudo pironman5 -op mix,ips,disk

* **スリープタイムアウトの設定**：OLEDがオフになるまでの非アクティブ時間を秒単位で定義します（0の場合はスリープしません）。

    .. code-block:: shell

      sudo pironman5 -os 120

赤外線レシーバーの確認
---------------------------------------

内蔵のIRレシーバーにより、リモコンでの操作が可能になります。

1. 必要なソフトウェアをインストールします：

    .. code-block:: shell

      sudo apt-get install lirc -y

2. レシーバーをテストします。以下のコマンドを実行し、リモコンをケースに向けてボタンを押します。生のコード出力が表示されるはずです。

    .. code-block:: shell

      mode2 -d /dev/lirc0

3. 特定のリモコンボタンのマッピング（例：KodiやVolumio用）を設定するには、 `/etc/lirc/lircd.conf` ファイルにリモコンのコードを設定する必要があります。




一般システムコマンド
----------------------------

* **バージョン表示**：インストールされている ``pironman5`` パッケージのバージョンを表示します。

.. code-block:: shell

  sudo pironman5 -v

* **現在の設定表示**：すべての現在の設定を表示します。

.. code-block:: shell

  sudo pironman5 -c

* **温度単位の設定**：温度表示を摂氏（ ``C`` ）と華氏（ ``F`` ）の間で切り替えます。

.. code-block:: shell

  sudo pironman5 -u F

* **データロギングの設定**：

  * **データベース保持日数の設定**：履歴データ（温度ログなど）を保持する日数を制御します。

    .. code-block:: shell

      sudo pironman5 -drd 30

  * **履歴ロギングの有効化／無効化**：データ収集をオンまたはオフにします。

    .. code-block:: shell

      sudo pironman5 -eh false

* **ログ詳細度の設定**：システムログの詳細レベルを調整します。オプション： ``DEBUG`` 、 ``INFO`` 、 ``WARNING`` 、 ``ERROR`` 、 ``CRITICAL`` 。

.. code-block:: shell

  sudo pironman5 -dl DEBUG

* **ウェブダッシュボードの削除**：オプションのウェブベース管理インターフェースをアンインストールします。

.. code-block:: shell

  sudo pironman5 -rd

* **カスタム設定パスの指定**：標準以外の場所にある設定ファイルを使用します。

.. code-block:: shell

  sudo pironman5 -cp /home/pi/my_custom_config.json

サービス管理サブコマンド
-----------------------------------

* **Pironman5サービスの起動**：LED、ファン、OLEDなどを管理するバックグラウンドサービスを手動で起動します。

.. code-block:: shell

  sudo pironman5 start

* **Pironman5サービスの停止**：バックグラウンドサービスを適切に停止します。

.. code-block:: shell

  sudo pironman5 stop

* **ウェブダッシュボードをブラウザで起動**：ウェブダッシュボードがインストールされている場合、このコマンドはデフォルトのブラウザでダッシュボードを開きます。

.. code-block:: shell

  sudo pironman5 launch-browser