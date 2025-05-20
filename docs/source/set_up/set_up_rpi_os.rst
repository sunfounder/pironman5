.. note:: 

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Facebookで他の愛好者たちとともに、Raspberry Pi、Arduino、ESP32の世界をさらに深く探究しましょう。

    **参加する理由**

    - **専門サポート**：購入後の課題や技術的なトラブルも、コミュニティやチームのサポートで安心して解決できます。
    - **学びと共有**：スキル向上につながるヒントやチュートリアルを気軽に交換できます。
    - **限定プレビュー**：新製品の先行発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品を対象とした限定ディスカウントが受けられます。
    - **フェスティブプロモーションとプレゼント企画**：季節限定のキャンペーンや抽選企画に参加可能です。

    👉 探索と創造を始める準備はできていますか？今すぐ [|link_sf_facebook|] をクリックして参加しましょう！


Raspberry Pi / Ubuntu / Kali / Homebridge OSでのセットアップ
===============================================================

Raspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合、Pironman 5はコマンドラインから設定を行う必要があります。詳細な手順は以下をご覧ください。

.. note::

  設定を行う前に、Raspberry Piを起動してログインしておく必要があります。ログイン方法が分からない場合は、公式Raspberry Piウェブサイト（ |link_rpi_get_start| ）を参照してください。


GPIO電源をシャットダウン時に無効化する設定
------------------------------------------------------------
OLEDディスプレイやRGBファンが、シャットダウン後もGPIOから電力供給されて動作し続けないようにするため、GPIO電源を停止する設定が必要です。

#. 以下のコマンドで ``EEPROM`` 設定ファイルを手動で編集します：

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. ファイル内の ``POWER_OFF_ON_HALT`` の値を ``1`` に設定します。例：

   .. code-block:: shell
 
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. ``Ctrl + X`` → ``Y`` → ``Enter`` を順に押して変更を保存・終了します。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

#. Lite系OSでは、まず以下のツールをインストールしてください： ``git``、 ``python3``、 ``pip3``、 ``setuptools``

   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. 次に、GitHubからコードをクローンして ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

     cd ~
     git clone https://github.com/sunfounder/pironman5.git --depth 1
     cd ~/pironman5
     sudo python3 install.py

   インストールが完了すると、再起動を促されます。画面の指示に従ってRaspberry Piを再起動してください。

   再起動後、 ``pironman5.service`` が自動で起動します。Pironman 5の主な動作内容は以下の通りです：

   * OLED画面にCPU、RAM、ディスク使用量、CPU温度、IPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色でブリージングモード（呼吸点灯）になります。

   .. note::

      RGBファンは、CPU温度が60°C以上にならないと回転しません。起動温度のカスタマイズについては :ref:`cc_control_fan` を参照してください。


#. ``systemctl`` コマンドを使用して、 ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、 ``status`` の操作が可能です。

   .. code-block:: shell

     sudo systemctl restart pironman5.service

   * ``restart``：Pironman 5の設定を変更した際に、その内容を反映させるために使用します。
   * ``start/stop``： ``pironman5.service`` を起動または停止します。
   * ``status``： ``systemctl`` コマンドで ``pironman5`` の動作状態を確認します。

