.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32の世界を、同じ情熱を持つ仲間たちと一緒に深く掘り下げましょう。

    **Why Join?**

    - **Expert Support**：購入後のサポートや技術的な問題を、コミュニティとサポートチームがしっかりサポートします。
    - **Learn & Share**：チュートリアルやヒントを共有し合い、スキルを高めましょう。
    - **Exclusive Previews**：新製品情報や先行公開を誰よりも早く入手できます。
    - **Special Discounts**：最新製品を対象に、会員限定の特別割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンやプレゼント企画に参加しましょう。

    👉 私たちと一緒にものづくりの冒険を始めませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！

Raspberry Pi OSのインストール
================================================================================
お持ちのデバイスがMicro SDカードかNVMe SSDかによって、インストール方法を選択できます。

**Micro SDカードのみを使用する場合**

  Micro SDカードのみを使用する場合は、以下の最初の方法に従って簡単にインストールできます。

**M.2 NVMe SSDを使用する場合**

  * **M.2 NVMe SSDエンクロージャーアダプター** をお持ちであれば、そのアダプターを使ってSSDをパソコンに接続し、2番目の方法でOSをインストールできます。

    .. image:: img/m2_nvme_adapter.png  
        :width: 300
        :align: center

  * 上記のアダプターがない場合は、まず最初の方法でMicro SDカードにOSをインストールし、その後3番目の方法を使ってMicro SDカードからM.2 NVMe SSDにシステムをコピーすることができます。


.. toctree::
    :maxdepth: 1

    install_to_sd_rpi
    install_to_nvme_rpi
    copy_sd_to_nvme_rpi