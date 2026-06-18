.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _max_set_up_pironman5:

4. ソフトウェアのセットアップまたはインストール
================================================

システムをMicro SDカードまたはNVMe SSDに書き込んだら、それをPironman 5 MAXのスロットに挿入し、電源ボタンを押してデバイスの電源を入れます。

起動後は各種電源LEDが点灯しますが、OLEDスクリーン、RGB LED、GPIOファン（側面の2つのファン）はまだ動作しません。これらは別途設定が必要です。画面が乱れる場合もありますが、後ほどの設定で解消されるため、今は無視してください。

設定を行う前に、まずRaspberry Piを起動しログインする必要があります。ログイン方法がわからない場合は、公式Raspberry Piサイトをご参照ください：|link_rpi_get_start|

その後、お使いのシステムに応じた設定チュートリアルを選択してください。


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel

.. set_up_batocera
    


**About Power Button**

この電源ボタンは、Raspberry Pi 5 の電源ボタンと同様の機能を果たします。

* **シャットダウン**

    * **Raspberry Pi OS Desktop** システムをご利用の場合、電源ボタンを素早く2回押すことでシャットダウンできます。
    * **Raspberry Pi OS Lite** システムをご利用の場合、電源ボタンを1回押すとシャットダウンを開始します。
    * 強制的に電源を切りたい場合は、ボタンを長押ししてください。

* **電源オン**

    * Raspberry Pi 本体がシャットダウン状態で通電している場合、ボタンを1回押すことで起動します。
* シャットダウンボタン非対応のシステムをご利用の場合は、電源ボタンを5秒以上長押しで強制終了、1回押しで起動が可能です。
