.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ趣味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32 の世界をより深く楽しみましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的課題を、コミュニティとサポートチームがサポートします。
    - **学びと共有**：ヒントやチュートリアルを共有しながらスキルアップ。
    - **新製品の先行公開**：新製品の先行発表やプレビューにいち早くアクセス。
    - **Special Discounts**：最新製品に対する限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにもご参加いただけます。

    👉 私たちと一緒に創造と探求を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _max_set_up_pi_os:

Raspberry Pi／Ubuntu／Kali／Homebridge OSでのセットアップ
==========================================================

Raspberry PiにRaspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合は、コマンドラインを使用してPironman 5 MAXを設定する必要があります。詳細なチュートリアルは以下を参照してください。

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式サイト（|link_rpi_get_start|）を参照してください。


GPIO電源を停止時に無効化する設定
------------------------------------------------------------

Raspberry PiのGPIOによって電力供給されているOLEDディスプレイやRGBファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を停止時に無効化する設定を行う必要があります。

#. EEPROM設定ツールを開きます：

   .. code-block::

      sudo raspi-config

#. **Advanced Options → A12 Shutdown Behaviour** に進みます。

   .. image:: img/shutdown_behaviour.png

#. **B1 Full Power Off** を選択します。

   .. image:: img/run_power_off.png

#. 変更を保存します。設定を有効にするために再起動を求められます。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

.. note::

   Lite版システムの場合、まず ``git``、``python3``、``pip3``、``setuptools`` などのツールをインストールしてください。
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHubからコードをダウンロードし、``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   インストールが完了すると、システムの再起動が必要です。画面の指示に従って再起動を行ってください。

   再起動後、``pironman5.service`` が自動的に起動します。Pironman 5 MAXの主な初期設定は以下の通りです：
   
   * OLEDディスプレイには、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。

   .. note:: OLEDディスプレイは、省電力のため一定時間操作がないと自動的にオフになる場合があります。ケースを軽く叩くと、振動センサーが反応して画面が再点灯します。

   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。
   * RGBファンはデフォルトで **常時オン** モードに設定されています。作動温度の調整に関する情報は、:ref:`cc_control_fan_max` を参照してください。

#. ``systemctl`` ツールを使用して、``pironman5.service`` を ``start``、``stop``、``restart``、または ``status`` で操作できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``： Pironman 5 MAXの設定変更を適用する際に使用します。
   * ``start/stop``： ``pironman5.service`` を有効または無効にします。
   * ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   これでPironman 5 MAXのセットアップは完了です。すぐに使用を開始できます。
   
   各コンポーネントの詳細な制御方法については、:ref:`control_commands_dashboard_max` を参照してください。
