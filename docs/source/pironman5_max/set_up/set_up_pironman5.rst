.. note::

    こんにちは！SunFounderのRaspberry Pi・Arduino・ESP32 愛好者向けFacebookコミュニティへようこそ！同じ趣味を持つ仲間たちと一緒に、Raspberry Pi・Arduino・ESP32 の世界をより深く楽しみましょう。

    **Why Join?**

    - **Expert Support**：購入後のサポートや技術的なトラブルは、コミュニティとチームがサポートします。
    - **Learn & Share**：チュートリアルやノウハウを共有してスキルアップ。
    - **Exclusive Previews**：新製品の情報や先行リリースをいち早くゲット。
    - **Special Discounts**：新製品を対象とした限定割引をお届け。
    - **Festive Promotions and Giveaways**：プレゼント企画や季節ごとのキャンペーンにも参加可能。

    👉 一緒にモノづくりと探求を始めませんか？[|link_sf_facebook|] をクリックして、今すぐ参加！

.. _max_set_up_pironman5:

4. ソフトウェアのセットアップまたはインストール
================================================

システムをMicro SDカードまたはNVMe SSDに書き込んだら、それをPironman 5のスロットに挿入し、電源ボタンを押してデバイスの電源を入れます。

起動後は各種電源LEDが点灯しますが、OLEDスクリーン、RGB LED、RGBファン（側面の2つのファン）はまだ動作しません。これらは別途設定が必要です。画面が乱れる場合もありますが、後ほどの設定で解消されるため、今は無視してください。

設定を行う前に、まずRaspberry Piを起動しログインする必要があります。ログイン方法がわからない場合は、公式Raspberry Piサイトをご参照ください：|link_rpi_get_start|

その後、お使いのシステムに応じた設定チュートリアルを選択してください。


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    
    
.. set_up_batocera


**About Power Button**

この電源ボタンは、Raspberry Pi 5 の電源ボタンと同様の機能を果たします。

* **シャットダウン**

    * Raspberry Pi **Bookworm Desktop** システムをご利用の場合、電源ボタンを素早く2回押すことでシャットダウンできます。
    * Raspberry Pi **Bookworm Lite** システムをご利用の場合、電源ボタンを1回押すとシャットダウンを開始します。
    * 強制的に電源を切りたい場合は、ボタンを長押ししてください。

* **電源オン**

    * Raspberry Pi 本体がシャットダウン状態で通電している場合、ボタンを1回押すことで起動します。
* シャットダウンボタン非対応のシステムをご利用の場合は、電源ボタンを5秒以上長押しで強制終了、1回押しで起動が可能です。
