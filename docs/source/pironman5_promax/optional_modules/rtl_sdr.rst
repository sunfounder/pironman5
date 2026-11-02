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

.. note::

    流通しているのは **RTL-SDR Blog V4** と **RTL-SDR Blog V4 Lite** の 2 種類です。
    EEPROM の製品文字列が異なるため、``rtl_test`` は
    ``RTL-SDR Blog V4 Detected`` または ``RTL-SDR Blog V4 Lite Detected`` のいずれかを表示します。
    どちらも正常で、以降の手順は両方に当てはまります。

----

RTL-SDR Blog V4のドライバーインストール
----------------------------------------------------

Linux でも手順は同じように簡単で、既存の RTL-SDR ドライバーを削除し、更新版をインストールするだけです。

**1. 以前のドライバーを削除**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

確認 A：

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: システムキャッシュに librtlsdr が見つかりません。"

**2. 最新のドライバーをインストール**

.. code-block:: shell

   sudo apt-get install libusb-1.0-0-dev git cmake pkg-config build-essential
   git clone https://github.com/osmocom/rtl-sdr
   cd rtl-sdr
   mkdir build
   cd build
   cmake ../ -DINSTALL_UDEV_RULES=ON
   make
   sudo make install
   sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
   sudo ldconfig

注意：
    コマンドラインで FM 受信もテストする場合（下記参照）、play コマンドを提供する sox が必要です。

    .. code-block:: shell

       sudo apt install -y sox

確認 B：

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # /usr/local/lib/librtlsdr.so を指している必要があります

**3. DVB-T TV ドライバーをブラックリストに登録**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. 再起動**

.. code-block:: shell

   sudo reboot

**5. 再起動後のドライバー確認**

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

期待される出力：
    出力に ``RTL-SDR Blog V4 Detected`` が含まれ、 ``[R82XX] PLL not locked!`` メッセージがないこと。
    ``Using device 0: Generic RTL2832U OEM`` という行は正常です — これは単なるUSB名です。


**6. コマンドラインからのFM受信テスト**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   #    Note: -M wbfm outputs the 180 kHz MPX, not 48 kHz audio, and -r is ignored.
   #    The playback rate must match -s, otherwise the audio plays at the wrong speed.
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

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

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**初回起動時の設定**

* **I/O Devices**:

  * Device: ``RTL-SDR (V4)`` を選択します。
  * Input Rate: ``1.8 MSPS`` （1800000）。
  * Audio Output（音声出力）: USB スピーカーまたはサウンドカードを選択してください。
    Raspberry Pi 5 では既定の出力が HDMI になっていることがあり、そこに接続した USB
    スピーカーからは音が出ません。

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
     libfftw3-dev libvolk-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

.. note::

   Debian 13（trixie）以降ではパッケージ名は ``libvolk-dev`` です。Debian 12（bookworm）
   およびそれをベースにした Raspberry Pi OS では ``libvolk2-dev`` です。名前を間違えると
   ``apt`` が *Unable to locate package* を返します。

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
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

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**基本的な使い方:**

* ``rtl_433`` を実行すると、一般的な433 MHzデバイスを自動的に検出しデコードします。
* ``rtl_433 -R`` を引数なしで実行すると、対応している全プロトコルを一覧表示できます。
  旧オプション ``-G`` は一覧表示しなくなり、25.02 以降は非推奨です。

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutabilityは、ADS-B航空機トランスポンダデータ用のMode Sデコーダーです。航空機の位置、速度、その他の飛行データを受信してデコードし、Webブラウザ経由でライブマップを提供できます。

**インストール:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

.. note::

   ``dump1090-mutability`` は Debian 12（bookworm）、bullseye 以前で利用できますが、
   **Debian 13（trixie）にはありません**。アーカイブから削除されたため、``apt`` は
   *Unable to locate package dump1090-mutability* を返します。

   Debian 13 のアーカイブに直接の代替はありません。``readsb`` パッケージは RTL-SDR 対応を
   **有効にせず** ビルドされているため（``readsb --device-type rtlsdr`` は *SDR type
   'rtlsdr' not recognized* を返します）、そのような環境ではデコーダをソースからビルドする
   必要があります。たとえば ``readsb`` を ``make RTLSDR=yes`` で、または ``dump1090-fa`` を
   使用します。

**ドライバーの上書き防止**

GQRX、SDR++、gnuradio-dev、またはgr-osmosdrをインストールすると、システムが古い ``librtlsdr`` を再インストールする可能性があります。
各インストール後、以下を確認してください：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

これが ``/usr/local/lib/librtlsdr.so`` を指さなくなった場合は、以下を実行します：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


すぐにテストするか（またはクリーンな環境のために再起動後）、以下を実行します：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

期待される出力：

   * RTL-SDR Blog V4 Detected が含まれていること。
   * [R82XX] PLL not locked! メッセージがないこと。

**基本的な使い方:**

* 実行： ``dump1090 --interactive --net``
* ブラウザで ``http://<raspberrypi-ip>:8080`` を開き、ライブ航空機追跡を表示します。
