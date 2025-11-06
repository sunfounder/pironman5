.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に情熱を注ぐ仲間たちと一緒に、さらに深く学び、楽しみましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的な課題を、コミュニティおよび当社のサポートチームがサポートします。
    - **学びと共有**：ヒントやチュートリアルを共有してスキルアップを目指しましょう。
    - **新製品の先行公開**：新製品の発表や先行情報をいち早くチェックできます。
    - **Special Discounts**：最新製品を対象とした会員限定の割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画に参加しましょう。

    👉 一緒に創造の旅を始めませんか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _set_up_batocera_mini:

Batocera.linux のセットアップ
=========================================================

Batocera.linux OSをインストール済みの場合は、SSH経由でリモートログインし、以下の手順に従って設定を完了させましょう。

#. システムが起動したら、SSHを使ってPironman 5にリモート接続します。Windowsの場合は **Powershell** を開き、Mac OS XやLinuxでは **ターミナル** を起動してください。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. batoceraシステムのデフォルトホスト名は ``batocera``、ユーザー名は ``root``、パスワードは ``linux`` です。したがって、 ``ssh root@batocera.local`` と入力し、パスワードに ``linux`` を入力することでログインできます。

   .. image:: img/batocera_login.png
      :width: 90%

#. 次のコマンドを実行して、メニュー設定ページを開きます： ``/etc/init.d/S92switch setup``

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 下矢印キーでメニューの一番下まで移動し、 **Pironman5** のサービスを選択して有効化します。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. pironman5サービスを有効化したら、 **OK** を選択します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. ``reboot`` コマンドを実行して、Pironman5 を再起動します。

   .. code-block:: shell

      reboot

#. 再起動後、自動的に ``pironman5.service`` が起動されます。Pironman 5の主な設定内容は以下の通りです：

   * WS2812 RGB LEDが4つ点灯し、青色のブリージングモードになります。
   * RGBファンはデフォルトで **常時オン** モードに設定されています。異なる作動温度の設定については、:ref:`cc_control_fan_mini` を参照してください。

これで、Pironman 5にディスプレイ、ゲームコントローラー、ヘッドホンなどを接続し、ゲームの世界を思う存分楽しめます。


.. note::

   この時点で、Pironman 5 Mini のセットアップが正常に完了し、使用可能な状態になっています。
   
   各コンポーネントを高度に制御する方法については、:ref:`control_commands_dashboard_mini` を参照してください。
