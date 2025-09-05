.. note:: 

    こんにちは！FacebookのSunFounder Raspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ興味を持つ仲間たちと一緒により深く探究しましょう。

    **Why Join?**

    - **Expert Support**：購入後の問題や技術的な課題も、コミュニティやSunFounderチームのサポートで安心。
    - **Learn & Share**：役立つヒントやチュートリアルを共有して、スキルをさらにレベルアップ。
    - **Exclusive Previews**：新製品の発表やプレビューにいち早くアクセス可能。
    - **Special Discounts**：最新製品を対象とした特別割引が受けられます。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節限定キャンペーンにも参加可能！

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _set_up_pironman5_mini:

Raspberry Pi OS/Ubuntu/Kali Linux/Homebridgeでのセットアップ
======================================================================

Raspberry PiにRaspberry Pi OS、Ubuntu、Kali Linux、またはHomebridgeをインストールしている場合、Pironman 5 Miniの設定はコマンドラインを使って行います。詳細なチュートリアルは以下をご参照ください。

.. note::

  設定を始める前に、Raspberry Piを起動しログインしておく必要があります。ログイン方法が不明な場合は、公式Raspberry Piサイト（|link_rpi_get_start|）をご確認ください。


シャットダウン時にGPIOの電源を無効にする設定
------------------------------------------------------------
Raspberry PiのGPIOから電源供給されているRGBファンが、シャットダウン後も回り続けるのを防ぐため、GPIOの電源を無効化する設定を行います。

#. 以下のコマンドで ``EEPROM`` 設定ファイルを手動で編集します：

   .. code-block:: shell
   
     sudo rpi-eeprom-config -e

#. 設定ファイル内の ``POWER_OFF_ON_HALT`` を ``1`` に変更します。例：

   .. code-block:: shell
   
     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. ``Ctrl + X``、 ``Y``、 ``Enter`` の順で保存・終了します。


``pironman5`` モジュールのダウンロードとインストール
-----------------------------------------------------------

#. 最小構成のシステムでは、まず ``git``、 ``python3``、 ``pip3``、 ``setuptools`` などのツールをインストールします。

   .. code-block:: shell
  
     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. GitHubからコードをダウンロードし、 ``pironman5`` モジュールをインストールします。

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   インストール完了後は、画面の指示に従ってシステムを再起動してください。

   再起動後、 ``pironman5.service`` が自動的に起動します。主な設定内容は以下の通りです：

   * 4つのWS2812 RGB LEDが青色でブリージングモードに点灯します。
     
   .. note::

     RGBファンは温度が60°Cに達するまで回転しません。起動温度を変更したい場合は、:ref:`cc_control_fan_mini` を参照してください。

#. ``systemctl`` コマンドを使って ``pironman5.service`` の ``start``、 ``stop``、 ``restart``、 ``status`` を管理できます。

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service

   * ``restart``：設定変更を適用する際に使用します。
   * ``start/stop``： ``pironman5.service`` の有効／無効を切り替えます。
   * ``status``： ``pironman5`` プログラムの動作状況を確認できます。



.. note::

   この時点で、Pironman 5 Mini のすべての構成要素を正しく設定できました。  
   Pironman 5 Mini の設定は完了です。  
   これで Pironman 5 Mini を使って Raspberry Pi やその他の機器を操作できます。  
   この Pironman 5 Mini のウェブページに関する詳細や使用方法については、:ref:`view_control_dashboard_mini` を参照してください。