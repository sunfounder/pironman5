.. note::

    こんにちは！SunFounderのRaspberry Pi & Arduino & ESP32エンスージアストコミュニティへようこそ！Facebookで他のエンスージアストたちと共に、Raspberry Pi、Arduino、ESP32の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティやチームの支援を受けて、アフターサポートや技術的な課題を解決します。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換しましょう。
    - **限定プレビュー**: 新製品の発表や先行情報にいち早くアクセスできます。
    - **特別割引**: 最新製品の特別割引をお楽しみください。
    - **イベントやプレゼント企画**: プレゼント企画や季節のプロモーションに参加できます。

    👉 探索と創造の旅に出る準備はできましたか？[|link_sf_facebook|]をクリックして、今日から参加しましょう！

RTL-SDR Blog V4
==============================================

.. note::

    Pironman 5 シリーズ製品には以下のモジュールは含まれていません。  
    ご自身で用意するか、公式サイトから購入してください:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

このガイドでは、人気があり手頃な価格の USB ソフトウェア無線（SDR）受信機である RTL-SDR Blog V4 の信頼できるインストール手順を説明します。  
V4 バージョンは改良された R828D チューナー、ダイレクトサンプリングモード、より良い感度、アクティブアンテナ用の内蔵バイアステーを備えています。  
Linux および Raspberry Pi システムで FM 放送、航空無線、アマチュア無線、ADS-B、その他多くの信号を受信するのに適しています。

オリジナルのメーカー提供ドキュメントについては公式 RTL-SDR Blog V4 ガイドをご覧ください: https://www.rtl-sdr.com/V4/

----

RTL-SDR Blog V4 ドライバーのインストール
---------------------------------------------

**0. 準備**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

注:  
    ``sox``（``play`` コマンドを提供）は直接オーディオテスト用に含まれています。

**1. 古いライブラリとバイナリの完全削除（重要）**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

確認 A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. RTL-SDR Blog V4 ドライバーのビルドとインストール**

.. code-block:: shell

   cd ~
   git clone https://github.com/rtlsdrblog/rtl-sdr-blog.git
   cd rtl-sdr-blog
   mkdir build && cd build
   cmake .. -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

確認 B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # /usr/local/lib/librtlsdr.so を指しているはずです

**3. DVB カーネルモジュールを無効化して再起動**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

注:  
    即時リロードコマンド（``udevadm control --reload-rules`` および ``udevadm trigger``）は、すぐに再起動する予定がある場合は省略可能です。

**4. 再起動後のドライバー確認**

.. code-block:: shell

   rtl_test -t

期待される結果:  
    出力に ``RTL-SDR Blog V4 Detected`` が含まれ、``[R82XX] PLL not locked!`` メッセージが表示されないこと。  
    ``Using device 0: Generic RTL2832U OEM`` という行は正常で、単に USB 名を示しているだけです。

**6. コマンドラインから FM 受信をテスト**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

ヒント:

    * ``-g``: 25〜35 dB の範囲で試してください。高ければ良いとは限りません。  
    * ``-s`` を ~170k–180k に下げてノイズを減らします。  
    * 周波数を微調整します（例: ``97.1005M``）。  
    * 他の SDR ソフトがデバイスを使用している場合は終了してください。

----

一般的な無線ソフトウェアのインストール
---------------------------------------

このセクションでは、広く使われている4つのSDRアプリケーションを紹介します。  
それぞれの概要、インストール手順、Debian系システムでの基本セットアップ方法を説明します。

* :ref:`install_gqrx`
* :ref:`install_sdrpp`
* :ref:`install_rtl433`
* :ref:`install_dump1090`

----

.. _install_gqrx:

GQRX
^^^^^^^^^^^^

GQRX はシンプルでユーザーフレンドリーな SDR 受信アプリケーションで、グラフィカルインターフェースを備えています。  
幅広いSDRデバイスをサポートし、FM、AM、SSB などの信号をリアルタイムのスペクトラム表示とウォーターフォール表示で受信するのに適しています。

公式の Raspberry Pi インストールガイドはこちらをご参照ください: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**オプション1 – 簡易インストール（推奨）**

高速・簡単でシステム更新と統合されますが、最新版ではない可能性があります。

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**オプション2 – ソースからビルド（最新版機能を利用可能）**

最新版を確実に利用でき、完全なカスタマイズが可能ですが、コンパイルに時間がかかり依存関係も多くなります。

.. code-block:: shell

   sudo apt update

   sudo apt-get install -y --no-install-recommends \
     cmake gnuradio-dev gr-osmosdr qt6-base-dev qt6-svg-dev \
     libasound2-dev libjack-jackd2-dev portaudio19-dev libpulse-dev

   git clone https://github.com/gqrx-sdr/gqrx.git
   cd gqrx
   mkdir build && cd build
   cmake ..
   make
   sudo make install

**ドライバー上書き防止**

GQRX、SDR++、gnuradio-dev、gr-osmosdr のインストール時に、古い ``librtlsdr`` が再インストールされる場合があります。  
各インストール後に確認してください:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

もし ``/usr/local/lib/librtlsdr.so`` を指さなくなっていた場合は以下を実行してください:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

すぐにテスト可能です（またはクリーン環境のために再起動後でも可）:

.. code-block:: shell

   rtl_test -t

期待される出力:

   * RTL-SDR Blog V4 Detected が含まれる。  
   * [R82XX] PLL not locked! メッセージが表示されない。

**初回起動時の設定**

* **I/O デバイス**:
  * Device: ``RTL-SDR (V4)``
  * Input Rate: ``1.8 MSPS`` (1800000)

* **入力コントロール**:
  * **LNA Gain**: 25〜35 dB から開始し、必要に応じて調整

* **受信オプション**:
  * 周波数補正 (PPM) をキャリブレーション値に設定
  * Mode: 放送FM用に ``WFM (mono or stereo)`` を選択

----

.. _install_sdrpp:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ はモダンで高速なクロスプラットフォーム SDR 受信アプリケーションです。  
RTL-SDR Blog V4 を含むさまざまなデバイスをサポートし、クリーンで使いやすいUI、広範な変調方式、先進的なDSPフィルタリング、録音機能を備えています。

公式ユーザーマニュアルはこちら: https://www.sdrpp.org/manual.pdf

**ソースからインストール**

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends build-essential cmake git pkg-config \
     libfftw3-dev libvolk2-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

**ドライバー上書き防止**

GQRX、SDR++、gnuradio-dev、gr-osmosdr のインストール時に、古い ``librtlsdr`` が再インストールされる場合があります。  
各インストール後に確認してください:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

もし ``/usr/local/lib/librtlsdr.so`` を指さなくなっていた場合は以下を実行してください:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

すぐにテスト可能です（またはクリーン環境のために再起動後でも可）:

.. code-block:: shell

   rtl_test -t

期待される出力:

   * RTL-SDR Blog V4 Detected が含まれる。  
   * [R82XX] PLL not locked! メッセージが表示されない。

**初回起動の注意点**

インストール後、SDR++ はデスクトップメニュー（通常「その他」）に表示されます。  
または以下で実行可能です:

   .. code-block:: shell

      sdrpp

* **デバイス:** **RTL-SDR (V4)** を **Source** メニューから選択  
* **サンプルレート:** 1.8 MSPS が一般的。CPU負荷が高ければ下げる  
* **ゲイン:** AGC を無効にし、手動で ~35 dB から調整  
* **PPM 補正:** ``rtl_test -p`` で取得したキャリブレーション値を入力  
* **復調モード:** 放送FMなら WFM、アマチュアバンドなら SSB を選択


----

.. _install_rtl433:

rtl_433
^^^^^^^^^^^^

rtl_433 は、433 MHz ISM バンドで動作するデバイス（気象ステーション、タイヤ空気圧センサー、ワイヤレス温度計など）からの無線送信をデコードするコマンドラインツールです。

**インストール:**

.. code-block:: shell

   sudo apt install -y rtl-433

**ドライバー上書き防止**

GQRX、SDR++、gnuradio-dev、gr-osmosdr のインストール時に、古い ``librtlsdr`` が再インストールされる可能性があります。  
各インストール後に確認してください:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

もし ``/usr/local/lib/librtlsdr.so`` を指していない場合は以下を実行してください:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

すぐにテスト可能です（または再起動後にクリーン環境でテスト可）:

.. code-block:: shell

   rtl_test -t

期待される出力:

   * RTL-SDR Blog V4 Detected が含まれる  
   * [R82XX] PLL not locked! メッセージが表示されない

**基本的な使い方:**

* ``rtl_433`` を実行すると、一般的な 433 MHz デバイスを自動検出してデコードします。  
* ``rtl_433 -G`` でサポートされているすべてのプロトコルを一覧表示できます。

----

.. _install_dump1090:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability は ADS-B 航空機トランスポンダーデータ用の Mode S デコーダーです。  
航空機の位置、速度、その他の飛行データを受信してデコードし、ウェブブラウザ経由でライブマップを提供できます。

**インストール:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**ドライバー上書き防止**

GQRX、SDR++、gnuradio-dev、gr-osmosdr のインストール時に、古い ``librtlsdr`` が再インストールされる可能性があります。  
各インストール後に確認してください:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

もし ``/usr/local/lib/librtlsdr.so`` を指していない場合は以下を実行してください:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

すぐにテスト可能です（または再起動後にクリーン環境でテスト可）:

.. code-block:: shell

   rtl_test -t

期待される出力:

   * RTL-SDR Blog V4 Detected が含まれる  
   * [R82XX] PLL not locked! メッセージが表示されない

**基本的な使い方:**

* 実行: ``dump1090 --interactive --net``  
* ブラウザで ``http://<raspberrypi-ip>:8080`` を開くと、ライブの航空機追跡が表示されます。
