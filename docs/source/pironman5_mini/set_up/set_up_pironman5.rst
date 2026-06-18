.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_pironman5_mini:

4. ソフトウェアのセットアップまたはインストール
================================================

OSがMicro SDカードまたはNVMe SSDに書き込まれたら、それをRaspberry Piのスロットに挿入し、電源ボタンを押して起動します。

起動後、複数の電源LEDが点灯しますが、RGB LEDおよびGPIOファンはまだ動作しません。これらは後で設定が必要です。また、画面が乱れることがありますが、設定後に解消されますので無視してください。

設定を始める前に、Raspberry Piを起動しログインする必要があります。ログイン方法が分からない場合は、公式Raspberry Piサイトをご参照ください：|link_rpi_get_start|

その後、ご使用のシステムに応じて適切な設定チュートリアルを選択してください。


.. toctree::
    :maxdepth: 1

    set_up_rpi_os 
    set_up_home_assistant
    set_up_umbrel
    set_up_batocera

**電源ボタンについて**

この電源ボタンは、Raspberry Pi 5 の物理電源ボタンを引き出す設計となっており、Raspberry Pi 5の電源ボタンと同様に機能します。

* **シャットダウン**

    * **Raspberry Pi OS Desktop** システムを使用している場合、電源ボタンを素早く2回押すことでシャットダウンします。
    * **Raspberry Pi OS Lite** システムの場合、電源ボタンを1回押すだけでシャットダウンが始まります。
    * 強制的に電源を切るには、電源ボタンを長押ししてください。

* **起動**

    * Raspberry Piの基板がシャットダウン状態でも電源が供給されている場合、ボタンを1回押すことで電源をオンにできます。


* シャットダウンボタンに対応していないシステムをご利用の場合でも、電源ボタンを5秒以上長押しすることで強制シャットダウンが可能です。その後、1回押しで電源を入れられます。
