.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32愛好者向けFacebookコミュニティへようこそ！
    このコミュニティでは、Raspberry Pi、Arduino、ESP32についてさらに深く学び、同じ興味を持つ仲間と交流できます。

    **Why Join?**

    - **Expert Support**: ご購入後の問題や技術的な課題について、コミュニティメンバーや私たちのチームがサポートします。
    - **Learn & Share**: 技術的なヒントやチュートリアルを共有・交換し、スキルを磨けます。
    - **Exclusive Previews**: 新製品のアナウンスや先行情報をいち早く入手できます。
    - **Special Discounts**: 最新製品を会員限定の特別価格でご購入いただけます。
    - **Festive Promotions and Giveaways**: 季節のキャンペーンやプレゼント企画にご参加いただけます。

    👉 探索とものづくりの旅に出る準備はできましたか？[|link_sf_facebook|] をクリックして今すぐ参加しましょう！

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
