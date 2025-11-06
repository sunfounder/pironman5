.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ情熱を持つ仲間たちと一緒に深く探究しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的な課題を、コミュニティとサポートチームがサポートします。
    - **学びと共有**：ヒントやチュートリアルを共有し、スキル向上を図りましょう。
    - **新製品の先行公開**：新製品の発表や先行情報を誰よりも早くチェックできます。
    - **特別割引**：最新製品を対象とした限定割引をご利用いただけます。
    - **季節イベントとプレゼント企画**：季節のイベントやプレゼント企画に参加できます。

    👉 私たちと一緒にものづくりを始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _install_to_sd_ubuntu_mini:

Micro SDカードへのOSインストール
=============================================

Micro SDカードを使用する場合は、以下の手順に従ってシステムをインストールしてください。


**必要な機材**

* パーソナルコンピューター
* Micro SDカードとカードリーダー

**手順**

#. |link_batocera_download| ページにアクセスし、 **Raspberry Pi 5 B** を選択してダウンロードを開始します。

   .. image:: img/batocera_download.png
      :width: 90%


#. ダウンロードしたファイル ``batocera-xxx-xx-xxxxxxxx.img.gz`` を解凍します。



#. カードリーダーを使って、SDカードをパソコンまたはノートPCに挿入します。

#. |link_rpi_imager| を開き、 **Operating System** タブをクリックします。


   .. image:: img/os_choose_os.png
      :width: 90%

#. ページの一番下までスクロールし、 **Use Custom** を選択します。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%



#. 解凍したシステムファイル ``batocera-xxx-xx-xxxxxxxx.img`` を選び、 **Open** をクリックします。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. **Choose Storage** をクリックし、インストール先のストレージデバイスを選択します。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。ストレージに既存データがある場合は、データ損失を防ぐためにバックアップを行ってください。バックアップが不要であれば **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」と表示されたら、イメージの書き込みと検証は正常に完了しています。これでMicro SDカードからRaspberry Piを起動する準備が整いました！
