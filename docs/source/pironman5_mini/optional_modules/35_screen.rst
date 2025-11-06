.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

3.5インチ タッチスクリーン
=============================

.. note::

    Pironman 5 シリーズには 3.5インチタッチスクリーンは含まれていません。  
    ご自身で用意するか、公式サイトから購入してください:

   * `3.5インチ タッチスクリーン <https://www.sunfounder.com/products/touchscreen-02>`_

3.5インチタッチスクリーンは Raspberry Pi の GPIO ヘッダーに直接接続され、  
Pironman 5 にディスプレイとタッチ制御を提供します。  
正しく取り付け、ハードウェアの損傷を避けるために手順を慎重に従ってください。

詳細はこちらをご覧ください:  
`3.5インチ タッチスクリーン ドキュメント <http://wiki.sunfounder.cc/index.php?title=3.5_Inch_LCD_Touch_Screen_Monitor_for_Raspberry_Pi>`_.


**組み立て**

.. image:: img/lcd_to_mini1.jpg
    :width: 340

.. image:: img/lcd_to_mini2.jpg
    :width: 340


.. warning:: 
   
   Pironman 5 に 3.5インチタッチスクリーンを取り付ける際は、ピンが完全に揃っていることを確認してください。  
   ヘッダーは Raspberry Pi の GPIO インターフェースとずれなく一致している必要があります。  
   ずれるとスクリーンや Raspberry Pi が破損する可能性があります。  
   電源を入れる前に必ず接続を再確認してください！

**RGB ジャンパーの取り外し**

Pironman 5 を 3.5インチタッチスクリーンと併用する場合、  
IO Expander 上の RGB LED はスクリーンと同じ SPI MOSI ピン (GPIO10) を共有しています。  
競合を避け、正常に動作させるためには次の対応を行ってください:

1. IO Expander 上で **RGB LED ピン** (J9の上) からジャンパーキャップを外します。

   .. image:: img/lcd_to_mini0.jpg
      :width: 600
      :align: center

2. RGB LED 制御サービスを無効化します:

   .. code-block:: bash

      sudo pironman5 -re false
      sudo systemctl restart pironman5.service

これにより SPI インターフェースがタッチスクリーン用に解放され、表示の不具合を防ぎます。


**ドライバーのインストール**

3.5インチタッチスクリーンを使用する前に、ドライバーをインストールする必要があります。

一般的な注意点:

* git がインストールされていることを確認してください (``sudo apt install git``)。  
* ドライバーのインストールには 1〜3分かかります。  
* システムは自動的に再起動します。

以下の OS に応じて手順に従ってください:

* **Raspberry Pi OS の場合**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show 
     git clone https://github.com/sunfounder/LCD-show.git 
     chmod -R 755 LCD-show 
     cd LCD-show/ 
     sudo ./LCD35-show
  
  インストール後、デスクトップが 3.5インチタッチスクリーンに表示されます。
  
  画面を回転するには:
  
  .. code-block:: bash
  
     cd LCD-show/
     sudo ./rotate.sh 90   
  
  システムが再起動し、画面が90°回転します。  
  ``90`` は ``0``、 ``180``、 ``270`` に置き換えることができます。



* **Ubuntu の場合**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-ubuntu 
     git clone https://github.com/sunfounder/LCD-show-ubuntu.git 
     chmod -R 755 LCD-show-ubuntu 
     cd LCD-show-ubuntu/ 
     sudo ./LCD35-show
  
  インストール後、デスクトップが 3.5インチタッチスクリーンに表示されます。
  
  回転させるには:
  
  .. code-block:: bash
  
     cd LCD-show-ubuntu/
     sudo ./rotate.sh 90   
  
  自動的に再起動されます。  
  ``90`` は ``0``、 ``180``、 ``270`` に置き換えることができます。



* **Kali Linux の場合**:

  .. code-block:: bash
  
     sudo rm -rf LCD-show-kali 
     git clone https://github.com/sunfounder/LCD-show-kali.git 
     chmod -R 755 LCD-show-kali 
     cd LCD-show-kali/ 
     sudo ./LCD35-show
  
  インストール後、デスクトップが 3.5インチタッチスクリーンに表示されます。
  
  回転させるには:
  
  .. code-block:: bash
  
     cd LCD-show-kali/
     sudo ./rotate.sh 90   
  
  システムは新しい回転設定で再起動します。  
  ``90`` は ``0``、 ``180``、 ``270`` に置き換えることができます。
