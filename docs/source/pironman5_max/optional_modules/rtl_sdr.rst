
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

----

安装 RTL-SDR Blog V4 驱动
-----------------------------------

**0. 准备工作**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

说明:  

    ``sox`` （提供 ``play`` 命令）用于直接进行音频测试。

**1. 清理旧库和二进制文件（非常关键）**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

验证 A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. 构建并安装 RTL-SDR Blog V4 驱动**

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

验证 B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # 应该指向 /usr/local/lib/librtlsdr.so

**3. 禁用 DVB 内核模块并重启**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

说明:  
    如果计划立即重启，可以省略以下命令：  
    ``udevadm control --reload-rules`` 和 ``udevadm trigger``

**4. 重启后验证驱动**

.. code-block:: shell

   rtl_test -t

预期结果:  
    输出应包含 ``RTL-SDR Blog V4 Detected``，并且不出现 ``[R82XX] PLL not locked!`` 错误。  
    出现 ``Using device 0: Generic RTL2832U OEM`` 是正常的 —— 这只是 USB 名称。

**6. 命令行测试 FM 接收**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

技巧:

    * ``-g``: 建议尝试 25–35 dB；数值越高不一定越好。  
    * 将 ``-s`` 降低到 ~170k–180k 可以减少噪声。  
    * 可以微调频率（如 ``97.1005M``）以获得更好的效果。  
    * 确保关闭可能占用设备的其他 SDR 软件。

----

安装常用的无线电软件
----------------------------------

本章节介绍了四款常用的 SDR 应用程序，包含简短说明、安装方法，以及在基于 Debian 系统上的基本设置提示。

* :ref:`install_gqrx`
* :ref:`install_sdrpp`
* :ref:`install_rtl433`
* :ref:`install_dump1090`


----

.. _install_gqrx:

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

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``，请运行：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**首次运行设置**

* **I/O 设备**:

  * Device: ``RTL-SDR (V4)``  
  * Input Rate: ``1.8 MSPS`` (1800000)

* **输入控制**:

  * **LNA 增益**: 从 25–35 dB 开始，根据需要调整。

* **接收器选项**:

  * 设置频率校正 (PPM)，根据你的校准值输入。  
  * 模式: 广播 FM 使用 ``WFM (mono or stereo)``。

----

.. _install_sdrpp:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ 是一款现代、快速、跨平台的软件无线电（SDR）接收器，支持包括 RTL-SDR Blog V4 在内的多种设备。它提供简洁友好的界面、广泛的调制支持、先进的 DSP 滤波，以及录音功能。

你可以参考官方用户手册： https://www.sdrpp.org/manual.pdf

**从源码安装**

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

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``，请运行：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**首次运行说明：**

安装完成后，SDR++ 会出现在桌面菜单中（通常在“Other”分类下），也可以通过命令运行：

   .. code-block:: shell

      sdrpp

* **Device:** 在 **Source** 菜单中选择 **RTL-SDR (V4)**。  
* **Sample Rate:** 通常使用 1.8 MSPS；如果 CPU 负载过高可以降低。  
* **Gain:** 关闭 AGC，设置手动增益（推荐起始值 ~35 dB）。  
* **PPM Correction:** 输入通过 ``rtl_test -p`` 获得的校准值。  
* **解调模式:** 广播 FM 选择 WFM，业余波段选择 SSB，等等。

----

.. _install_rtl433:

rtl_433
^^^^^^^^^^^^

rtl_433 是一个命令行工具，用于解码在 433 MHz ISM 波段工作的设备信号，例如气象站、胎压传感器和无线温度计。

**安装：**

.. code-block:: shell

   sudo apt install -y rtl-433

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``，请运行：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**基本用法：**

* 运行 ``rtl_433``，自动检测并解码常见的 433 MHz 设备。  
* 使用 ``rtl_433 -G`` 列出所有支持的协议。

----

.. _install_dump1090:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability 是一款 Mode S 解码器，用于 ADS-B 飞机应答机数据。它可以接收并解码飞机的位置、速度和其他飞行数据，并通过网页提供实时地图显示。

**安装：**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装过时的 ``librtlsdr``。  
在每次安装后，请检查：

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

如果它不再指向 ``/usr/local/lib/librtlsdr.so``，请运行：

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


你可以立即测试（或者在重启后获得更干净的环境）：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected。  
   * 没有 [R82XX] PLL not locked! 报错。

**基本用法：**

* 运行： ``dump1090 --interactive --net``  
* 在浏览器中打开 ``http://<raspberrypi-ip>:8080`` 查看实时航班跟踪。
