.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ興味を持つ仲間たちと一緒により深く探究しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後の問題や技術的な課題も、コミュニティやSunFounderチームのサポートで安心。
    - **学びと共有**：役立つヒントやチュートリアルを共有して、スキルをさらにレベルアップ。
    - **新製品の先行公開**：新製品の発表やプレビューにいち早くアクセス可能。
    - **Special Discounts**：最新製品を対象とした特別割引が受けられます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにも参加可能！

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _set_up_pironman5_mini:

Raspberry Pi OS／Ubuntu／Kali Linux／Homebridgeでのセットアップ
======================================================================

Raspberry PiにRaspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合は、コマンドラインを使用してPironman 5 Miniを設定する必要があります。詳細なチュートリアルは以下を参照してください。

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、Raspberry Pi公式サイト（|link_rpi_get_start|）を参照してください。


GPIO電源を停止時に無効化する設定
------------------------------------------------------------
Raspberry PiのGPIOによって電力供給されているRGBファンがシャットダウン後も動作し続けるのを防ぐために、GPIO電源を停止時に無効化する設定を行う必要があります。

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
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   インストールが完了すると、システムの再起動が必要です。画面の指示に従って再起動を行ってください。

   再起動後、``pironman5.service`` が自動的に起動します。Pironman 5 Miniの主な初期設定は以下の通りです：
   
   * 4つのWS2812 RGB LEDが青色の呼吸モードで点灯します。
     
   .. note::
    
     * RGBファンはデフォルトで **常時オン** モードに設定されています。異なる作動温度の設定については、:ref:`cc_control_fan_mini` を参照してください。

#. ``systemctl`` ツールを使用して、``pironman5.service`` を ``start``、``stop``、``restart``、または ``status`` で操作できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``：Pironman 5 Miniの設定変更を適用する際に使用します。
   * ``start/stop``：``pironman5.service`` を有効または無効にします。
   * ``status``：``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状態を確認します。

.. note::

   これでPironman 5 Miniのセットアップは完了です。すぐに使用を開始できます。
   
   各コンポーネントの詳細な制御方法については、:ref:`control_commands_dashboard_mini` を参照してください。
