.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




RTL-SDR Blog V4
==============================================

.. note::

    Pironman 5シリーズ製品には、以下のモジュールは付属していません。
    ご自身でご用意いただくか、公式ウェブサイトからご購入ください：

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

このガイドでは、人気で手頃な価格のUSBソフトウェア定義無線（SDR）レシーバーであるRTL-SDR Blog V4の信頼性の高いインストール手順について説明します。
V4バージョンは、改良されたR828Dチューナー、直接サンプリングモード、改善された感度、アクティブアンテナに電力を供給するための統合バイアスティーを特徴としています。
LinuxやRaspberry Piシステム上で、放送FM、航空無線、アマチュア無線、ADS-B、その他多くの信号を受信するのに適しています。

元の製造元のドキュメントについては、公式RTL-SDR Blog V4ガイドを参照してください： https://www.rtl-sdr.com/V4/

----

RTL-SDR Blog V4のドライバーインストール
----------------------------------------------------

**0. 準備**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

注記：
    ``sox`` （ ``play`` コマンドを提供）は直接オーディオテストのために含まれています。

**1. 古いライブラリとバイナリの完全なクリーンアップ（重要）**


.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

確認A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: システムキャッシュにlibrtlsdrは見つかりません。"

**2. RTL-SDR Blog V4ドライバーのビルドとインストール**

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

確認B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # /usr/local/lib/librtlsdr.so を指しているはず

**3. DVBカーネルモジュールの無効化と再起動**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

注記：
    すぐに再起動する場合は、即時リロードコマンド（ ``udevadm control --reload-rules`` と ``udevadm trigger`` ）はオプションです。

**4. 再起動後のドライバー確認**

.. code-block:: shell

   rtl_test -t

期待される出力：
    出力に ``RTL-SDR Blog V4 Detected`` が含まれ、 ``[R82XX] PLL not locked!`` メッセージがないこと。
    ``Using device 0: Generic RTL2832U OEM`` という行は正常です — これは単なるUSB名です。


**6. コマンドラインからのFM受信テスト**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

ヒント：

    * ``-g``： 25〜35 dBの間で試してください。高いほど良いとは限りません。
    * ノイズを減らすために ``-s`` を〜170k〜180kに下げます。
    * 微調整のために周波数を少し（例： ``97.1005M`` ）調整します。
    * デバイスを保持している可能性のある他のSDRソフトウェアを閉じてください。

----

一般的な無線ソフトウェアのインストール
-----------------------------------------------------

このセクションでは、広く使用されている4つのSDRアプリケーションについて、簡単な説明、インストール手順、Debianベースのシステム向けの基本的なセットアップのヒントを紹介します。

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`


----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRXは、シンプルで使いやすいグラフィカルインターフェースを備えたSDR受信アプリケーションです。幅広いSDRデバイスをサポートし、リアルタイムのスペクトラムとウォーターフォール表示でFM、AM、SSBなどの信号を受信するのに最適です。

公式のRaspberry Piインストールガイドも参照してください： https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**オプション1 – クイックインストール（ほとんどのユーザーに推奨）**

高速でシンプル、システムアップデートと統合されますが、最新バージョンではない場合があります。

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**オプション2 – ソースからのビルド（オプション、最新機能）**

最新バージョンと完全なカスタマイズを保証しますが、コンパイルに時間がかかり、より多くの依存関係が必要です。

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

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**初回起動時の設定**

* **I/O Devices**:

  * Device: ``RTL-SDR (V4)`` を選択します。
  * Input Rate: ``1.8 MSPS`` （1800000）。

* **Input Controls**:

  * **LNA Gain**: 25〜35 dB程度から開始し、必要に応じて調整します。


* **Receiver Options**:

  * キャリブレーションから周波数補正（PPM）を設定します。
  * Mode: 放送FMの場合は ``WFM (mono or stereo)`` を選択します。

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^


SDR++は、RTL-SDR Blog V4を含む様々なデバイスをサポートする、モダンで高速なクロスプラットフォームのソフトウェア定義無線（SDR）レシーバーです。クリーンでユーザーフレンドリーなインターフェース、幅広い変調方式のサポート、高度なDSPフィルタリング、録音機能を提供します。

公式ユーザーマニュアルはこちらを参照してください： https://www.sdrpp.org/manual.pdf


**ソースからのインストール**

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

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。


**初回起動時の注意点：**

インストール後、SDR++はデスクトップメニュー（通常は「その他」の下）に表示されるか、以下で実行できます：

   .. code-block:: shell

      sdrpp

* **Device:** **Source** メニューで **RTL-SDR (V4)** を選択します。
* **Sample Rate:** 1.8 MSPSが標準的です。CPU負荷が高い場合は下げます。
* **Gain:** AGCを無効にし、マニュアルゲインを設定します（開始は〜35 dB）。
* **PPM Correction:** ``rtl_test -p`` から取得したキャリブレーション値を入力します。
* **Demodulation Mode:** FM放送の場合はWFM、アマチュアバンドの場合はSSBなどを選択します。

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^


rtl_433は、気象観測機器、タイヤ空気圧センサー、ワイヤレス温度計など、433 MHz ISMバンドで動作するデバイスからの無線送信をデコードするコマンドラインツールです。

**インストール:**

.. code-block:: shell

   sudo apt install -y rtl-433

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**基本的な使い方:**

* ``rtl_433`` を実行すると、一般的な433 MHzデバイスを自動的に検出しデコードします。
* ``rtl_433 -G`` を使用すると、サポートされているすべてのプロトコルを一覧表示します。

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutabilityは、ADS-B航空機トランスポンダデータ用のMode Sデコーダーです。航空機の位置、速度、その他の飛行データを受信してデコードし、Webブラウザ経由でライブマップを提供できます。

**インストール:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**基本的な使い方:**

* 実行： ``dump1090 --interactive --net``
* ブラウザで ``http://<raspberrypi-ip>:8080`` を開き、ライブ航空機追跡を表示します。
