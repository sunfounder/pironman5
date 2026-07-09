.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Raspberry Pi OS/Ubuntu/Kali Linux/Homebridgeでのセットアップ
==================================================================

.. image:: ../img/pironman5_pic.jpg
    :width: 400
    :align: center


Raspberry PiにRaspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合は、コマンドラインを使用してPironman 5を設定する必要があります。

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式サイト（|link_rpi_get_start|）を参照してください。


.. _safe_shutdown_5:

1. GPIO電源を停止時に無効化する設定
------------------------------------------------------------

Raspberry PiのGPIOによって電力供給されているOLEDディスプレイやGPIOファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を停止時に無効化する設定を行う必要があります。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に進みます。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off...** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。設定を有効にするために再起動を求められます。


.. _install_pironman5_module_5:

2. ``pironman5`` モジュールのインストール
-----------------------------------------------------------

.. .. note::

..    Raspberry Pi OS Lite版システムの場合は、まず ``git`` や ``python3`` などの必要なツールをインストールしてください。

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHubから ``pironman5`` モジュールをダウンロードしてインストールします。

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash



   .. note::

      1. **Ubuntu** を使用している場合は、先に ``curl`` をインストールしてください：``sudo apt install curl -y``

      2. Pironman 5シリーズを **PiPower 5** と併用する場合は、代わりに次のコマンドを実行してください：

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash -s -- --pipower5

#. インストーラー実行後、Pironman 5のモデル（1〜4）を選択します。

   .. code-block:: shell

      Pironman 5 Installer v1.0.1
      Supports: 5 | 5 Mini | 5 Max | 5 Pro Max

      Please select your product model:
      1) Pironman 5
      2) Pironman 5 Mini
      3) Pironman 5 Max
      4) Pironman 5 Pro Max

      Enter number [1-4]:

#. インストールが完了したら、画面の指示に従ってRaspberry Piを再起動します。初回起動時は、サービスの初期化に最大30秒かかる場合があります。

#. Pironman 5が正常に起動したら、次の各コンポーネントが正しく動作していることを確認してください。

   * **OLEDスクリーン**

     * CPU使用率、RAM使用率、CPU温度、IPアドレスを表示します。
     * 10秒後に自動的に消灯します。
     * 電源ボタンを短く押すと、画面を起動またはページを切り替えます。

   * **電源ボタン**

     * 短く押す：電源オン / OLED画面を起動 / OLEDページを切り替え。
     * 2秒間長押し：安全なシャットダウン（:ref:`safe_shutdown_5` が必要です）。
     * 5秒間長押し：強制シャットダウン。

   * **WS2812 RGB LED**

     * 青色の呼吸モードで点灯します。

   * **2つのGPIOファン**

     * デフォルトでは **常時オン** モードに設定されています。
     * 動作モードはコマンドまたはダッシュボードから変更できます。


   * **CPUファン（タワークーラーファン）**

     * CPU温度に基づいて自動的に速度を調整します。
     * デフォルトのファンカーブ：

       * < 50°C：オフ（0%）
       * 50°C以上：低速（30%）
       * 60°C以上：中速（50%）
       * 67.5°C以上：高速（70%）
       * 75°C以上：最大速度（100%）

#. ``systemctl`` を使用して、``pironman5.service`` を管理します。

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   必要に応じて ``restart`` を ``start``、``stop``、または ``status`` に置き換えて、サービスを管理します。

.. note::

   Pironman 5のセットアップは完了しました。すぐに使用を開始できます。

   詳細な制御方法やダッシュボード機能については、:ref:`control_commands_dashboard_5` を参照してください。
