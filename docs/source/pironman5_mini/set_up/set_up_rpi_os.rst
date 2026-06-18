.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Raspberry Pi OS／Ubuntu／Kali Linux／Homebridgeでのセットアップ
======================================================================

.. image:: ../img/pironman5_mini_pic.jpg
    :width: 400
    :align: center

Raspberry PiにRaspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合は、コマンドラインを使用してPironman 5 Miniを設定する必要があります。詳細なチュートリアルは以下を参照してください。

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式サイト（|link_rpi_get_start|）を参照してください。


GPIO電源を停止時に無効化する設定
------------------------------------------------------------
Raspberry PiのGPIOによって電力供給されているGPIOファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を停止時に無効化する設定を行う必要があります。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に進みます。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。設定を有効にするために再起動を求められます。

.. _mini_download_pironman5_module:

``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

.. .. note::

..    Lite版システムの場合、まず ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールしてください。

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHub から ``pironman5`` モジュールをダウンロードしてインストールします。

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash



   .. note::

      1. **Ubuntu** を使用している場合は、最初に ``curl`` をインストールしてください： ``sudo apt install curl -y``

      2. Pironman 5 シリーズを**PiPower 5**と併用している場合は、代わりに以下のコマンドを実行してください：

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

   再起動後、 ``pironman5.service`` が自動的に起動します。Pironman 5 Mini の主な初期設定は以下の通りです：

   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。
   * GPIOファンはデフォルトで **常時オン** モードに設定されています。異なる作動温度の設定については、:ref:`cc_control_fan_mini` を参照してください。

#. ``systemctl`` ツールを使用して、 ``pironman5.service`` を ``start``、 ``stop``、 ``restart``、または ``status`` で操作できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：Pironman 5 Miniの設定変更を適用する際に使用します。
   * ``start/stop``： ``pironman5.service`` を有効または無効にします。
   * ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   これでPironman 5 Miniのセットアップは完了です。すぐに使用を開始できます。
   
   各コンポーネントの詳細な制御方法については、:ref:`control_commands_dashboard_mini` を参照してください。
