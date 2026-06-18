.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



.. _promax_set_up_pi_os:

Raspberry Pi/Ubuntu/Kali/Homebridge OSでの設定
==================================================

.. image:: ../img/Pironman-5-Pro-Max.png
    :width: 400
    :align: center

Raspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをRaspberry Piにインストールした場合は、コマンドラインを使用してPironman 5 Pro MAXを設定する必要があります。詳細なチュートリアルは以下をご覧ください：

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式ウェブサイト |link_rpi_get_start| にアクセスしてください。


.. _safe_shutdown_promax:

シャットダウン時のGPIO電源無効化設定
------------------------------------------------------------

Raspberry Pi GPIOから電源供給を受けるOLED画面やGPIOファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を無効化するようにRaspberry Piを設定することが重要です。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に移動します。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。新しい設定を有効にするために再起動を促すプロンプトが表示されます。


.. _promax_download_pironman5_module:

``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

.. note::

   Liteシステムの場合、最初に ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHub から ``pironman5`` モジュールをダウンロードしてインストールします。

   .. tip::

      **Ubuntu** を使用している場合は、最初に ``curl`` をインストールしてください：

      .. code-block:: shell

         sudo apt install curl -y

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

   .. note::

      Pironman 5 シリーズを PiPower 5 と併用している場合は、代わりに以下のコマンドを実行してください：

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash -s -- --pipower5

#. インストーラーを実行した後、Pironman 5 モデル（1〜4）を選択します。

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. インストールが完了したら、画面の指示に従って Raspberry Pi を再起動します。最初の起動時は、サービスが初期化されるまで最大30秒かかる場合があります。

   再起動後、 ``pironman5.service`` が自動的に起動します。Pironman 5 Pro MAX の主な初期設定は以下の通りです：

   * OLED 画面に CPU、RAM、ディスク使用量、CPU温度、Raspberry Pi の IP アドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。

#. ``systemctl`` ツールを使用して、 ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、または ``status`` の確認ができます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``： Pironman 5 Pro MAXの設定に変更を加えた場合に、このコマンドを使用して適用します。
   * ``start/stop``： ``pironman5.service`` を有効化または無効化します。
   * ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   この時点で、Pironman 5 Pro MAXのセットアップは正常に完了し、使用可能な状態になりました。
   
   コンポーネントの高度な制御については、 :ref:`control_commands_dashboard_promax` を参照してください。