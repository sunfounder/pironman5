.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32愛好家向けFacebookコミュニティへようこそ！ラズパイ、Arduino、ESP32をより深く探求し、情熱を共有しましょう。

    **なぜ参加するのか？**

    - **エキスパートサポート**：購入後のトラブルや技術的課題を、コミュニティとチームがサポートします。
    - **学びと共有**：チュートリアルやヒントを交換しながらスキルを高めましょう。
    - **新製品の先行公開**：製品発表やプレビューをいち早くチェックできます。
    - **特別割引**：最新製品に適用される特別割引が利用可能です。
    - **季節のキャンペーンやプレゼント企画**：抽選や特別イベントに参加しましょう。

    👉 一緒に探求・創造したい方は、今すぐ [|link_sf_facebook|] をクリックしてご参加ください！

.. _max_install_to_sd_ubuntu:

Micro SDカードへのOSインストール
=============================================

Micro SDカードを使用している場合は、以下の手順に従ってOSをインストールしてください。


**必要なもの**

* パーソナルコンピュータ
* Micro SDカードおよびカードリーダー

**手順**

#. 最初に |link_batocera_download| ページへアクセスし、 **Raspberry Pi 5 B** を選択してダウンロードを開始します。

   .. image:: img/batocera_download.png
      :width: 90%
      
#. ダウンロードした ``batocera-xxx-xx-xxxxxxxx.img.gz`` ファイルを解凍します。

#. SDカードをカードリーダーに挿入し、パソコンまたはノートPCに接続します。

#. |link_rpi_imager| を開き、 **Operating System** タブをクリックします。

   .. image:: img/os_choose_os.png
      :width: 90%

#. ページ下部までスクロールし、 **Use Custom** を選択します。

   .. image:: img/batocera_os_use_custom.png
      :width: 90%


#. 先ほど解凍した ``batocera-xxx-xx-xxxxxxxx.img`` ファイルを選択し、 **Open** をクリックします。

   .. image:: img/batocera_os_choose.png
      :width: 90%


#. **Choose Storage** をクリックし、インストール先となる適切なストレージデバイスを選びます。

   .. image:: img/os_choose_sd.png
      :width: 90%


#. **NEXT** をクリックします。ストレージに既存データがある場合は、事前にバックアップを取ってください。バックアップが不要であれば、 **Yes** をクリックして続行します。

   .. image:: img/os_continue.png
      :width: 90%


#. 「Write Successful」というポップアップが表示されれば、イメージの書き込みと検証が完了です。これでRaspberry PiをMicro SDカードから起動する準備が整いました！
