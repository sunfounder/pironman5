.. note:: 

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！Facebook上で他の愛好者たちと一緒に、Raspberry Pi、Arduino、ESP32についてより深く掘り下げていきましょう。

    **参加する理由**

    - **専門サポート**：コミュニティやSunFounderチームのサポートを受けながら、購入後のトラブルや技術的課題を解決できます。
    - **学びと共有**：スキル向上に役立つヒントやチュートリアルを共有し合いましょう。
    - **限定プレビュー**：新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**：最新製品を対象とした限定割引をご利用いただけます。
    - **フェスティブプロモーションとプレゼント企画**：季節ごとのプロモーションやプレゼントキャンペーンにも参加可能です。

    👉 探索と創造の準備はできていますか？[|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

.. _set_up_batocera:

Batocera.linuxのセットアップ
=========================================================

Batocera.linux OSをインストールした場合は、SSH経由でリモートログインし、以下の手順でPironman 5の設定を完了させることができます。

#. システムが起動したら、SSHを使用してPironman 5にリモート接続します。Windowsでは **Powershell**、Mac OS XやLinuxでは **Terminal** を起動してください。

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Batoceraのデフォルトホスト名は ``batocera``、デフォルトユーザー名は ``root``、パスワードは ``linux`` です。そのため、 ``ssh root@batocera.local`` と入力し、パスワード ``linux`` を入力すればログインできます。

   .. image:: img/batocera_login.png
      :width: 90%

#. コマンド ``/etc/init.d/S92switch setup`` を実行して、設定メニューに入ります。

   .. image:: img/batocera_configure.png  
      :width: 90%

#. 下矢印キーでリストの最後まで移動し、 **Pironman5** サービスを選択して有効化します。

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Pironman5サービスを有効にしたら、 **OK** を選択して設定を確定します。

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. コマンド ``reboot`` を実行してPironman 5を再起動します。

   .. code-block:: shell

      reboot

#. 再起動後、 ``pironman5.service`` が自動的に起動します。Pironman 5の主な表示機能は以下のとおりです：

   * OLED画面には、CPU使用率、メモリ使用量、ディスク使用量、CPU温度、IPアドレスが表示されます。
   * 4つのWS2812 RGB LEDが青色のブリージングモードで点灯します。

   .. note::

      RGBファンはCPU温度が60°Cに達するまでは回転しません。ファンの起動温度を変更したい場合は :ref:`cc_control_fan` をご参照ください。


さあ、Pironman 5をディスプレイ、ゲームコントローラー、ヘッドホンなどに接続して、レトロゲームの世界に飛び込みましょう。

