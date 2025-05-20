.. note::

    こんにちは！SunFounder Raspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！Raspberry Pi、Arduino、ESP32に情熱を持つ仲間たちとともに、より深く学び、楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的な課題を、コミュニティおよび当社サポートチームがしっかりサポートします。
    - **Learn & Share**：チュートリアルやヒントを交換して、スキルをさらに磨きましょう。
    - **Exclusive Previews**：新製品の発表や先行情報をいち早くチェックできます。
    - **Special Discounts**：最新製品を対象に、会員限定の特別割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節限定のキャンペーンや豪華プレゼント企画に参加しましょう。

    👉 一緒にモノづくりと探究の旅を始めませんか？[|link_sf_facebook|] をクリックして今すぐ参加！

.. _install_batocera_mini:

Batocera Linuxのインストール
======================================================

|link_batocera| は、あらゆるPCやナノコンピュータを一時的または恒久的にレトロゲームコンソールに変えることを目的とした、完全無料かつオープンソースのレトロゲーム向けLinuxディストリビューションです。USBメモリやSDカードにコピーして使用できます。

インストール方法は、お手元にMicro SDカードがあるかNVMe SSDがあるかによって選択できます。

NVMe SSDへ直接インストールする場合、Micro SDカードへのインストールよりも一手間必要です。それは、Raspberry Piのブートローダーを更新することです。初期状態ではMicro SDからの起動が優先されているため、NVMe SSDを優先起動に設定する必要があります。

.. toctree::
    :maxdepth: 1

    install_to_sd_batocera
    install_to_nvme_batocera

