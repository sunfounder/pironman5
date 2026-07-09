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

1. シャットダウン時のGPIO電源無効化設定
------------------------------------------------------------

Raspberry Pi GPIOから電源供給を受けるOLED画面とRGBファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を無効化するようにRaspberry Piを設定することが重要です。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に移動します。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。新しい設定を有効にするために再起動を促すプロンプトが表示されます。


.. _install_pironman5_module_promax:

2. ``pironman5`` モジュールのインストール
-----------------------------------------------------------

.. .. note::

..    Liteシステムの場合、最初に ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。

..    .. code-block:: shell

..       sudo apt-get install git -y
..       sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHub から ``pironman5`` モジュールをダウンロードしてインストールします。

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash



   .. note::

      1. **Ubuntu** を使用している場合は、最初に ``curl`` をインストールしてください： ``sudo apt install curl -y``

      2. Pironman 5 シリーズを**PiPower 5**と併用している場合は、代わりに以下のコマンドを実行してください：

      .. code-block:: shell

         curl -sSL "https://raw.githubusercontent.com/sunfounder/pironman5/v1/install.sh" | sudo bash -s -- --pipower5

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

   #. Pironman 5 Pro MAX が正常に起動したら、以下のコンポーネントが正しく動作しているか確認してください。

   * **OLED画面**

     * CPU使用率、RAM使用率、CPU温度、IPアドレスを表示します。
     * 10秒後に自動的にオフになります。
     * 電源ボタンを短く押して画面を起動するか、ページを切り替えます。

   * **電源ボタン**

     * 短く押す：電源オン / OLED起動 / OLEDページ切り替え。
     * 2秒間長押し：安全なシャットダウン（:ref:`safe_shutdown_promax` が必要です）。
     * 5秒間長押し：強制シャットダウン。

   * **WS2812 RGB LED**

     * 青色の呼吸エフェクトで点灯します。

   * **PWMファン**

     * デフォルトで **常時オン** モードに設定されています。
     * 動作モードはコマンドまたはダッシュボードで設定できます。

   * **CPUファン（タワークーラーファン）**

     * CPU温度に応じて自動的に速度を調整します。
     * デフォルトのファンカーブ：

       * 50°C未満：オフ（0%）
       * 50°C以上：低速（30%）
       * 60°C以上：中速（50%）
       * 67.5°C以上：高速（70%）
       * 75°C以上：最大速度（100%）

#. ``systemctl`` を使用して ``pironman5.service`` を管理します。

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   必要に応じて ``restart`` を ``start``、``stop``、または ``status`` に置き換えてサービスを管理します。

.. note::

   Pironman 5 Pro MAX のセットアップは正常に完了し、使用可能な状態になりました。

   高度な制御とダッシュボード機能については、:ref:`control_commands_dashboard_promax` を参照してください。
