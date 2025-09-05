.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと一緒に、Raspberry Pi、Arduino、ESP32についてさらに深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームのサポートを受け、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセスできます。
    - **特別割引**: 最新製品の特別割引を楽しめます。
    - **フェスティブプロモーションとプレゼント企画**: プレゼント企画や季節ごとのプロモーションに参加できます。

    👉 探索と創造の準備ができましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！


Raspberry Pi/Ubuntu/Kali/Homebridge OSでのセットアップ
===========================================================

Raspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールした場合、Pironman 5をコマンドラインで設定する必要があります。詳細なチュートリアルは以下をご覧ください。

.. note::

  設定を行う前に、Raspberry Piを起動してログインする必要があります。ログイン方法がわからない場合は、公式のRaspberry Piウェブサイトをご覧ください: |link_rpi_get_start|。


GPIO電源を停止するためのシャットダウン設定
------------------------------------------------------------
Raspberry PiのGPIOから供給されるOLED画面やRGBファンがシャットダウン後も動作し続けないように、GPIO電源の停止を設定する必要があります。

#. 次のコマンドを使用して、 ``EEPROM`` 設定ファイルを手動で編集します:

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. ファイル内の ``POWER_OFF_ON_HALT`` 設定を ``1`` に変更します。例:

   .. code-block:: shell
 
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. ``Ctrl + X``、 ``Y`` 、そして ``Enter`` を押して変更を保存します。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

#. Liteシステムでは、最初に ``git`` 、 ``python3`` 、 ``pip3`` 、 ``setuptools`` などのツールをインストールしてください。

   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 次に、GitHubからコードをダウンロードし、 ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

    cd ~
    git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
    cd ~/pironman5
    sudo python3 install.py

   インストールが成功したら、再起動が必要です。画面の指示に従って再起動してください。

   再起動後、 ``pironman5.service`` が自動的に開始されます。Pironman 5の主な設定は次の通りです:

   * OLED画面には、CPU、RAM、ディスク使用量、CPU温度、Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色で呼吸モードに点灯します。
   
   .. note::

      RGBファンは温度が60°Cに達しないと回転しません。異なる起動温度については :ref:`cc_control_fan` を参照してください。


#. ``systemctl`` ツールを使用して、 ``pironman5.service`` の ``start`` 、 ``stop`` 、 ``restart`` 、または ``status`` を確認することができます。

   .. code-block:: shell

     sudo systemctl restart pironman5.service

   * ``restart`` : pironman 5の設定に変更を加えた場合、このコマンドを使用して変更を適用します。
   * ``start/stop`` : ``pironman5.service`` を有効または無効にします。
   * ``status`` : ``systemctl`` ツールを使用して、 ``pironman5`` プログラムの稼働状況を確認します。

.. note::

   この時点で、Pironman 5 のすべての構成要素を正しく設定できました。  
   Pironman 5 の設定は完了です。  
   これで Pironman 5 を使って Raspberry Pi やその他の機器を操作できます。  
   この Pironman 5 のウェブページに関する詳細や使用方法については、:ref:`view_control_dashboard` を参照してください。
