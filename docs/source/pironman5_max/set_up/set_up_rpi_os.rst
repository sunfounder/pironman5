.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ趣味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32 の世界をより深く楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的課題を、コミュニティとサポートチームがサポートします。
    - **Learn & Share**：ヒントやチュートリアルを共有しながらスキルアップ。
    - **Exclusive Previews**：新製品の先行発表やプレビューにいち早くアクセス。
    - **Special Discounts**：最新製品に対する限定割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにもご参加いただけます。

    👉 私たちと一緒に創造と探求を始めましょう！[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _max_set_up_pi_os:

Raspberry Pi/Ubuntu/Kali/Homebridge OS でのセットアップ
============================================================

Raspberry Pi に Raspberry Pi OS、Ubuntu、Kali Linux、または Homebridge をインストールしている場合、Pironman 5 MAX の設定はコマンドラインで行う必要があります。詳細な手順は以下をご覧ください：

.. note::

  設定を行う前に、Raspberry Pi を起動してログインしてください。ログイン方法が分からない場合は、公式サイトをご参照ください：|link_rpi_get_start|


シャットダウン時にGPIO電源を無効化する設定
------------------------------------------------------------

Raspberry Pi のシャットダウン後もOLEDスクリーンやRGBファン（GPIO駆動）が動作し続けるのを防ぐため、GPIOの電源をオフにする設定が必要です。

#. 次のコマンドで ``EEPROM`` 設定ファイルを編集します：

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. ファイル内の ``POWER_OFF_ON_HALT`` を ``1`` に設定します。例：

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. ``Ctrl + X``、 ``Y``、 ``Enter`` を押して保存し、終了します。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

#. Lite システムの場合、まず ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHub からコードをダウンロードし、 ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b max https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   インストールが完了すると、再起動のプロンプトが表示されますので、指示に従って再起動してください。

   再起動後、 ``pironman5.service`` が自動的に起動します。主な機能は以下の通りです：

   * OLEDスクリーンにCPU、RAM、ディスク使用率、CPU温度、IPアドレスを表示。

   .. note:: OLEDスクリーンは、省電力のため一定時間操作がないと自動的にオフになる場合があります。ケースを軽くタップすると振動センサーが反応し、スクリーンを再表示できます。


   * 4つのWS2812 RGB LEDが青色で呼吸モードに点灯。

   .. note::

     RGBファンは温度が60°Cを超えない限り回転しません。動作温度の変更については :ref:`max_cc_control_fan` をご参照ください。

#. ``systemctl`` を使用して ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、 ``status`` を操作できます。

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart``：設定を変更した際に再読み込みします。
   * ``start/stop``：サービスの有効化・無効化を行います。
   * ``status``： ``pironman5`` プログラムの動作状態を確認します。

.. note::

   この時点で、Pironman 5 MAX のセットアップが正常に完了し、使用可能な状態になっています。
   
   各コンポーネントを高度に制御する方法については、:ref:`control_commands_dashboard_max` を参照してください。
