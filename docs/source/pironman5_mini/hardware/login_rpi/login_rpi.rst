.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ情熱を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32の世界をより深く探求しましょう。

    **Why Join?**

    - **Expert Support**：購入後のトラブルや技術的な問題を、コミュニティおよび専門スタッフがサポートします。
    - **Learn & Share**：チュートリアルやヒントを共有し、スキルを向上させましょう。
    - **Exclusive Previews**：新製品情報をいち早く入手できます。
    - **Special Discounts**：最新製品の特別割引をご利用いただけます。
    - **Festive Promotions and Giveaways**：季節のプロモーションやプレゼント企画に参加できます。

    👉 一緒に創造と発見の旅を始めましょう！[|link_sf_facebook|] をクリックして今すぐ参加！

.. _login_rpi_mini:

Raspberry Pi OSへのログイン方法
=====================================

この章では、Raspberry Piへのログイン方法について説明します。モニターを接続して操作する場合でも、リモートからアクセスする場合でも、本章を通じて今後使用するターミナルの開き方を学びます。

.. note::

    すでにRaspberry Piの操作に慣れている方は、この章をスキップして構いません。

画面を使ってログインする
---------------------------

モニターを接続することで、Raspberry Piに直接アクセスし操作することが可能になります。

**必要な機材**

* Pironman 5 Mini
* 電源アダプター
* Raspberry Pi OS をインストール済みの Micro SD カードまたは NVMe SSD
* モニター用電源アダプター
* HDMIケーブル
* モニター
* マウス
* キーボード

**手順**

#. Micro SDカードをPironman 5 Miniに挿入します。

#. マウスとキーボードをPironman 5 MiniのUSBポートに接続します。

#. HDMIケーブルを使用してモニターとPironman 5 MiniのHDMIポートを接続します。モニターの電源が入っていることを確認してください。

#. 電源アダプターでPironman 5 Miniに電力を供給します。まもなくモニターにRaspberry Pi OSのデスクトップが表示されるはずです。

   .. image:: img/bookwarm.png
      :width: 90%


#. デスクトップが表示されたら、ターミナルアイコンをクリックするか、メニューから検索してターミナルを開き、コマンドの入力を開始します。

画面を使わずリモートでログインする
----------------------------------------------

モニターが手元にない場合でも、Raspberry Piにはリモートでアクセスできます。

コマンドライン操作を希望する場合は、SSHを使用してRaspberry PiのBashシェル（Linuxの標準シェル）に接続することで、コマンドベースで操作可能です。

GUI操作を希望する場合は、VNC Viewerなどのリモートデスクトップアプリを利用することで、視覚的にファイルや操作を行うことができます。

**必要な機材**

* Pironman 5 Mini
* 電源アダプター
* Raspberry Pi OS をインストール済みの Micro SD カードまたは NVMe SSD

**手順**

#. Micro SDカードをPironman 5 Miniに挿入します。

#. 電源アダプターを接続して、Pironman 5 Miniを起動します。

#. お使いのパソコンのOSに応じたリモート接続の詳細な設定手順は、以下のセクションをご参照ください：

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


