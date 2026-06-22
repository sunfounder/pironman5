.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


RTL-SDR Blog V4
==============================================

.. note::

   Pironman 5 系列产品 **不包含以下模块**\ 。  
   需要用户自行准备，或从我们的官方网站购买：

   * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

本指南介绍 RTL-SDR Blog V4 的完整安装流程。这是一款流行且价格实惠的 USB 软件定义无线电（SDR）接收器。  
V4 版本采用改进的 R828D 调谐器，支持直接采样模式，具有更高的灵敏度，并内置 bias-tee，可为有源天线供电。  
它适用于在 Linux 和 Raspberry Pi 系统上接收 FM 广播、航空频段、业余无线电、ADS-B 等多种信号。 :contentReference[oaicite:0]{index=0}

官方文档参考：https://www.rtl-sdr.com/V4/

----

安装 RTL-SDR Blog V4 驱动
-----------------------------------

**0. 准备环境**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

说明：
   ``sox`` （提供 ``play`` 命令）用于直接音频测试。

**1. 完全清理旧版本库与程序（关键步骤）**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

验证 A：

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. 编译并安装 RTL-SDR Blog V4 驱动**

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

验证 B：

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # 应指向 /usr/local/lib/librtlsdr.so

**3. 禁用 DVB 内核模块并重启**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

说明：
   如果立即重启，则无需执行 ``udevadm control --reload-rules`` 等命令。

**4. 重启后验证驱动**

.. code-block:: shell

   rtl_test -t

预期结果：

   输出中应包含 ``RTL-SDR Blog V4 Detected``\ ，且不应出现 ``[R82XX] PLL not locked!``\ 。  
   出现 ``Using device 0: Generic RTL2832U OEM`` 属正常现象，仅为 USB 设备名称。


**6. 命令行测试 FM 接收**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

提示：

   * ``-g``\ ：建议在 25–35 dB 之间调整，增益并非越大越好。
   * 将 ``-s`` 调低到约 170k–180k 可降低噪声。
   * 可微调频率（例如 ``97.1005M``\ ）进行精确调谐。
   * 关闭其他可能占用 SDR 设备的软件。

----

安装常用无线电软件
----------------------------------

本节介绍四款常用 SDR 软件，包括简要说明、安装方法及基本配置建议（适用于 Debian 系统）。

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`

----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRX 是一款简单易用的 SDR 接收软件，提供图形界面，支持多种 SDR 设备，适合接收 FM、AM、SSB 等信号，并具备实时频谱和瀑布图显示功能。

官方安装指南：https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**方式 1 – 快速安装（推荐）**

简单快速，并可随系统更新，但版本可能不是最新。

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**方式 2 – 从源码编译（可选）**

可获取最新版本并进行自定义，但编译时间较长且依赖较多。

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

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装旧版本 ``librtlsdr``\ 。  
安装完成后请检查：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr

如果路径不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请执行：

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo ldconfig
   cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

测试：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected
   * 无 [R82XX] PLL not locked! 错误

**首次运行设置**

* **I/O Devices（输入设备）**\ ：

  * Device： ``RTL-SDR (V4)``
  * Input Rate： ``1.8 MSPS`` （1800000）

* **输入控制（Input Controls）**\ ：

  * **LNA 增益**\ ：建议从 25–35 dB 开始，根据需要调整

* **接收器设置（Receiver Options）**\ ：

  * 设置频率校准（PPM）
  * 模式选择： ``WFM (mono 或 stereo)`` 用于 FM 广播

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^^^

SDR++ 是一款现代化、高性能、跨平台的软件定义无线电（SDR）接收软件，支持包括 RTL-SDR Blog V4 在内的多种设备。  
它提供简洁直观的界面、广泛的调制方式支持、先进的 DSP 滤波能力，以及录制功能。 :contentReference[oaicite:0]{index=0}

官方手册：https://www.sdrpp.org/manual.pdf


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

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装旧版本 ``librtlsdr``\ 。  
安装完成后请检查：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr

如果路径不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请执行：

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo ldconfig
   cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

测试：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected  
   * 无 [R82XX] PLL not locked! 错误  


**首次运行说明：**

安装完成后，SDR++ 会出现在桌面菜单（通常在 “Other” 分类下），也可以通过命令运行：

.. code-block:: shell

   sdrpp

* **设备（Device）：** 在 **Source** 菜单中选择 **RTL-SDR (V4)**  
* **采样率（Sample Rate）：** 通常使用 1.8 MSPS；CPU 负载高时可降低  
* **增益（Gain）：** 关闭 AGC，手动设置（建议从 ~35 dB 开始）  
* **PPM 校准：** 使用 ``rtl_test -p`` 得到的值  
* **解调模式（Demodulation）：**  

  * FM 广播 → WFM  
  * 业余无线电 → SSB 等  

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^

``rtl_433`` 是一个命令行工具，用于解码工作在 433 MHz ISM 频段的无线设备信号，例如气象站、胎压传感器和无线温度计。 :contentReference[oaicite:1]{index=1}

**安装：**

.. code-block:: shell

   sudo apt install -y rtl-433

**防止驱动被覆盖**

在安装相关 SDR 软件后，请检查：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr

如果驱动路径异常，请执行：

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo ldconfig
   cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

测试：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 RTL-SDR Blog V4 Detected  
   * 无错误信息  

**基础用法：**

* 直接运行：

  .. code-block:: shell

     rtl_433

  自动检测并解码常见 433 MHz 设备信号  

* 查看支持的协议列表：

  .. code-block:: shell

     rtl_433 -G
     
-------

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability 是一个用于接收和解码 ADS-B（Automatic Dependent Surveillance–Broadcast）飞机应答机数据的 Mode S 解码器。  
它可以解析飞机的位置、速度和飞行信息，并通过浏览器提供实时地图显示。

**安装：**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**防止驱动被覆盖**

在安装 GQRX、SDR++、gnuradio-dev 或 gr-osmosdr 时，系统可能会重新安装旧版本 ``librtlsdr``\ 。  
安装完成后请检查：

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr

如果路径不再指向 ``/usr/local/lib/librtlsdr.so``\ ，请执行：

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo ldconfig
   cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig

测试：

.. code-block:: shell

   rtl_test -t

预期输出：

   * 包含 ``RTL-SDR Blog V4 Detected``  
   * 没有 ``[R82XX] PLL not locked!`` 错误

**基础使用：**

* 运行：

.. code-block:: shell

   dump1090 --interactive --net

* 在浏览器中打开：

::

   http://<raspberrypi-ip>:8080

即可查看实时飞机航班追踪地图。