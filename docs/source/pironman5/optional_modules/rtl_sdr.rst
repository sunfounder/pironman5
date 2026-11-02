.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



RTL-SDR Blog V4
==============================================

.. note::

    Pironman 5 系列产品不包含以下模块。  
    你需要自行准备，或在我们的官方网站购买：

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

本指南介绍了 RTL-SDR Blog V4 的可靠安装步骤。  
它是一款流行且价格实惠的 USB 软件无线电（SDR）接收器。  
V4 版本配备了改进的 R828D 调谐器、直采模式、更高的灵敏度，以及集成的偏置供电（bias-tee）功能，可为有源天线供电。  
在 Linux 和树莓派系统上，它可以很好地接收调频广播（FM）、航空波段（airband）、业余无线电、ADS-B 以及许多其他信号。

如需原厂文档，请参考官方指南： https://www.rtl-sdr.com/V4/

.. note::

    市面上有 **RTL-SDR Blog V4** 和 **RTL-SDR Blog V4 Lite** 两种型号。
    两者的 EEPROM 产品字符串不同，因此 ``rtl_test`` 会分别显示
    ``RTL-SDR Blog V4 Detected`` 或 ``RTL-SDR Blog V4 Lite Detected``\ ，都属于正常情况，
    下文所有步骤对两种型号均适用。

----

安装 RTL-SDR Blog V4 驱动
-----------------------------------

在 Linux 上，操作同样简单：移除已有的 RTL-SDR 驱动，然后安装更新版本即可。

**1. 卸载旧驱动**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

验证 A：

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: 系统缓存中未找到 librtlsdr。"

**2. 安装最新驱动**

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
    如果还需要在命令行测试 FM 收音（见下文），需安装 sox，它提供 play 命令：

    .. code-block:: shell

       sudo apt install -y sox

验证 B：

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # 应指向 /usr/local/lib/librtlsdr.so

**3. 屏蔽 DVB-T 电视驱动**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. 重启**

.. code-block:: shell

   sudo reboot

**5. 重启后验证驱动**

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

预期结果:  
    输出应包含 ``RTL-SDR Blog V4 Detected``\ ，并且不出现 ``[R82XX] PLL not locked!`` 错误。  
    出现 ``Using device 0: Generic RTL2832U OEM`` 是正常的 —— 这只是 USB 名称。

**6. 命令行测试 FM 接收**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   #    Note: -M wbfm outputs the 180 kHz MPX, not 48 kHz audio, and -r is ignored.
   #    The playback rate must match -s, otherwise the audio plays at the wrong speed.
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

技巧:

    * ``-g``: 建议尝试 25–35 dB；数值越高不一定越好。  
    * 将 ``-s`` 降低到 ~170k–180k 可以减少噪声。  
    * 可以微调频率（如 ``97.1005M``\ ）以获得更好的效果。  
    * 确保关闭可能占用设备的其他 SDR 软件。

----

安装常用的无线电软件
----------------------------------

本章节介绍了四款常用的 SDR 应用程序，包含简短说明、安装方法，以及在基于 Debian 系统上的基本设置提示。

* :ref:`install_gqrx_5`
* :ref:`install_sdrpp_5`
* :ref:`install_rtl433_5`
* :ref:`install_dump1090_5`


----

.. _install_gqrx_5:

GQRX
^^^^^^^^^^^^

GQRX 是一个简单易用的 SDR 接收器应用，带有图形化界面。它支持多种 SDR 设备，非常适合收听 FM、AM、SSB 等信号，并提供实时频谱和瀑布图显示。

你也可以参考官方的树莓派安装指南： https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**选项 1 – 快速安装（推荐大多数用户使用）**

快速、简单，并且能随系统更新集成 —— 但可能不是最新版本。

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**选项 2 – 从源码构建（可选，获取最新功能）**

确保安装最新版本并可完全自定义，但编译时间较长，并需要更多依赖。

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

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``\ 。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请运行：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**首次运行设置**

* **I/O 设备**:

  * Device: ``RTL-SDR (V4)``  
  * Input Rate: ``1.8 MSPS`` (1800000)
  * Audio Output（音频输出）：选择你的 USB 喇叭或声卡。树莓派 5 的默认输出可能是 HDMI，
    这时接在 USB 上的喇叭不会有声音。

* **输入控制**:

  * **LNA 增益**: 从 25–35 dB 开始，根据需要调整。

* **接收器选项**:

  * 设置频率校正 (PPM)，根据你的校准值输入。  
  * 模式: 广播 FM 使用 ``WFM (mono or stereo)``\ 。

----

.. _install_sdrpp_5:

SDR++ (SDRpp)
^^^^^^^^^^^^^^^

SDR++ 是一款现代、快速、跨平台的软件无线电（SDR）接收器，支持包括 RTL-SDR Blog V4 在内的多种设备。它提供简洁友好的界面、广泛的调制支持、先进的 DSP 滤波，以及录音功能。

你可以参考官方用户手册： https://www.sdrpp.org/manual.pdf

**从源码安装**

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

   Debian 13（trixie）及更高版本中该软件包名为 ``libvolk-dev``\ ；Debian 12（bookworm）
   及基于它的 Raspberry Pi OS 中名为 ``libvolk2-dev``\ 。用错会提示 *Unable to locate package*。

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``\ 。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请运行：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**首次运行说明：**

安装完成后，SDR++ 会出现在桌面菜单中（通常在“Other”分类下），也可以通过命令运行：

   .. code-block:: shell

      sdrpp

* **Device:** 在 **Source** 菜单中选择 **RTL-SDR (V4)**\ 。  
* **Sample Rate:** 通常使用 1.8 MSPS；如果 CPU 负载过高可以降低。  
* **Gain:** 关闭 AGC，设置手动增益（推荐起始值 ~35 dB）。  
* **PPM Correction:** 输入通过 ``rtl_test -p`` 获得的校准值。  
* **解调模式:** 广播 FM 选择 WFM，业余波段选择 SSB，等等。

----

.. _install_rtl433_5:

rtl_433
^^^^^^^^^^^^

rtl_433 是一个命令行工具，用于解码在 433 MHz ISM 波段工作的设备信号，例如气象站、胎压传感器和无线温度计。

**安装：**

.. code-block:: shell

   sudo apt install -y rtl-433

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``\ 。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请运行：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**基本用法：**

* 运行 ``rtl_433``\ ，自动检测并解码常见的 433 MHz 设备。  
* 不带参数运行 ``rtl_433 -R``\ ，可列出所有支持的协议。
  旧参数 ``-G`` 已不再列协议，自 25.02 起被弃用。

----

.. _install_dump1090_5:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability 是一款 Mode S 解码器，用于 ADS-B 飞机应答机数据。它可以接收并解码飞机的位置、速度和其他飞行数据，并通过网页提供实时地图显示。

**安装：**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

.. note::

   ``dump1090-mutability`` 在 Debian 12（bookworm）、bullseye 及更早版本中可用，
   但 **Debian 13（trixie）已从软件源中移除该包**\ ，``apt`` 会提示
   *Unable to locate package dump1090-mutability*。

   Debian 13 的软件源中没有可直接替代的包：``readsb`` 编译时**未启用 RTL-SDR 支持**
   （``readsb --device-type rtlsdr`` 会返回 *SDR type 'rtlsdr' not recognized*）。
   这类系统需要从源码编译，例如用 ``make RTLSDR=yes`` 编译 ``readsb``\ ，或改用 ``dump1090-fa``。

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``\ 。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请运行：

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**基本用法：**

* 运行： ``dump1090 --interactive --net``  
* 在浏览器中打开 ``http://<raspberrypi-ip>:8080`` 查看实时航班跟踪。
