.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32愛好者向けFacebookコミュニティへようこそ！このコミュニティでは、Raspberry Pi、Arduino、ESP32についてより深く学び、同じ趣味を持つ仲間たちと交流できます。

    **Why Join?**

    - **Expert Support**: 購入後のサポートや技術的な課題を、私たちのチームとコミュニティが協力して解決します。
    - **Learn & Share**: ヒントやチュートリアルを共有しながら知識とスキルを向上させましょう。
    - **Exclusive Previews**: 新製品の発表や先行情報をいち早くチェックできます。
    - **Special Discounts**: 最新製品を対象にした特別割引をご利用いただけます。
    - **Festive Promotions and Giveaways**: プレゼント企画や季節イベントにご参加いただけます。

    👉 一緒に楽しみましょう！今すぐ [|link_sf_facebook|] をクリックして参加！

.. _max_set_up_batocera:

Batocera.linuxのセットアップ
=========================================================

Batocera.linux OSをインストールした場合、SSH経由でこのシステムにリモートログインし、以下の手順で設定を完了させることができます。

#. システムが起動したら、sshでPironman5にリモート接続します。Windowsでは **Powershell** を開き、Mac OS XやLinuxでは **Terminal** を使用してください。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batoceraシステムのデフォルトホスト名は ``batocera``、ユーザー名は ``root``、パスワードは ``linux`` です。そのため、以下のように入力してログインできます： ``ssh root@batocera.local`` パスワードには ``linux`` を入力してください。

   .. image:: img/batocera_login.png
      :width: 90%

#. 次に、以下のコマンドを実行して設定メニューに入ります： ``/etc/init.d/S92switch setup``

   .. image:: img/batocera_configure.png  
      :width: 90%

#. ↓キーを使って最後までスクロールし、 **Pironman5** サービスを選択・有効化してください。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Pironman5サービスを有効化したら、 **OK** を選択します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. ``reboot`` コマンドを実行して、Pironman5 を再起動します。

   .. code-block:: shell

      reboot

#. 再起動後、自動的に ``pironman5.service`` が起動します。Pironman 5の主な構成は以下の通りです：

   * OLEDスクリーンには、CPU・RAM・ディスク使用量・CPU温度・Raspberry PiのIPアドレスが表示されます。
   * 4つのWS2812 RGB LEDは、青色のブリージングモードで点灯します。

   .. note::

     RGBファンは、温度が60°Cを超えるまで回転しません。起動温度を変更したい場合は、:ref:`max_cc_control_fan` を参照してください。

Pironman 5にディスプレイ、ゲームコントローラー、ヘッドホンなどを接続し、ゲームの世界に没入しましょう。
