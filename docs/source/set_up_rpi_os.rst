.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _set_up_pironman5:

Raspberry Pi/Ubuntu/Kali OSでPironman5をセットアップする
======================================================================

.. note::

  設定を行う前に、画面を接続するかリモートログインを通じてRaspberry Piにログインできるようにする必要があります。以下はRaspberry Pi OSにログインするためのチュートリアルです。UbuntuおよびKaliシステムの場合は、追加のリソースを参照してください。

  * :ref:`login_rpi`


GPIO電源を無効にするためのシャットダウン設定
------------------------------------------------------------
Raspberry Pi GPIOから電源を供給されるOLEDスクリーンやRGBファンがシャットダウン後もアクティブのままにならないようにするためには、GPIO電源を無効にするようRaspberry Piを設定することが重要です。

* 次のコマンドを使用して ``EEPROM`` 構成ファイルを手動で編集します：

  .. code-block:: shell

    sudo rpi-eeprom-config -e

* ファイル内の ``POWER_OFF_ON_HALT`` 設定を ``1`` に変更します。例えば：

  .. code-block:: shell

    BOOT_UART=1
    POWER_OFF_ON_HALT=1
    BOOT_ORDER=0xf41

* ``Ctrl + X``、 ``Y``、そして ``Enter`` を押して変更を保存します。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

.. note::

  Liteシステムの場合、まず ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。
  
  .. code-block:: shell
  
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python3 python3-pip python3-setuptools -y

次に、GitHubからコードをダウンロードして ``pironman5`` モジュールをインストールします。

.. code-block:: shell

  cd ~
  git clone https://github.com/sunfounder/pironman5.git
  cd ~/pironman5
  sudo python3 install.py

インストールが成功したら、インストールを有効にするためにシステムを再起動する必要があります。画面の再起動プロンプトに従います。

再起動後、 ``pironman5.service`` が自動的に開始されます。ここにPironman 5の主な設定があります：

  * OLEDスクリーンには、CPU、RAM、ディスク使用量、CPU温度、およびRaspberry PiのIPアドレスが表示されます。
  * 四つのWS2812 RGB LEDがブルーの呼吸モードで点灯します。
  * RGBファンは60°Cで起動します。

``systemctl`` ツールを使用して ``pironman5.service`` を ``start``、 ``stop``、 ``restart``、または ``status`` を確認することができます。

.. code-block:: shell

  sudo systemctl restart pironman5.service

* ``restart``：pironman 5の設定に対する変更を適用するためにこのコマンドを使用します。
* ``start/stop``： ``pironman5.service`` を有効または無効にします。
* ``status``： ``systemctl`` ツールを使用して ``pironman5`` プログラムの動作状況を確認します。


.. note::

  * 次に、ダッシュボードからPironman 5のコンポーネントを表示および制御できます。詳細については :ref:`view_control_dashboard` を参照してください。
  * コマンドを使用したい場合は、 :ref:`view_control_commands` を参照してください。
