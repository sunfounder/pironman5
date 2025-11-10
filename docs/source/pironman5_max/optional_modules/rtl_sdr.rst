.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!


RTL-SDR Blog V4
==============================================

.. note::

    The Pironman 5 series products do not include the following modules.  
    You need to prepare one yourself or purchase it from our official website:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

This guide covers a reliable installation procedure for the RTL-SDR Blog V4, a popular and affordable USB software-defined radio (SDR) receiver.
The V4 version features an improved R828D tuner, direct sampling mode, better sensitivity, and integrated bias-tee for powering active antennas.
It works well for receiving broadcast FM, airband, amateur radio, ADS-B, and many other signals on Linux and Raspberry Pi systems.

For the original manufacturer’s documentation, see the official RTL-SDR Blog V4 guide: https://www.rtl-sdr.com/V4/

----

Install Driver for RTL-SDR Blog V4
-----------------------------------

**0. Preparation**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

Note:
    ``sox`` (provides the ``play`` command) is included for direct audio testing.

**1. Full Cleanup of Old Libraries and Binaries (Critical)**


.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

Verification A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. Build and Install RTL-SDR Blog V4 Driver**

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

Verification B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Should point to /usr/local/lib/librtlsdr.so

**3. Disable DVB Kernel Module and Reboot**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

Note:
    Immediate reload commands (``udevadm control --reload-rules`` and ``udevadm trigger``)  
    are optional if you plan to reboot immediately.

**4. Verify Driver After Reboot**

.. code-block:: shell

   rtl_test -t

Expected:
    Output should include ``RTL-SDR Blog V4 Detected`` with no ``[R82XX] PLL not locked!`` messages.  
    The line ``Using device 0: Generic RTL2832U OEM`` is normal — it is just the USB name.


**6. Test FM Reception from Command Line**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Tips:

    * ``-g``: Try between 25–35 dB; higher is not always better.
    * Reduce ``-s`` to ~170k–180k to lower noise.
    * Adjust frequency slightly (e.g. ``97.1005M``) for fine tuning.
    * Close any other SDR software that might hold the device.

----

Installing Common Radio Software
----------------------------------

This section introduces four widely used SDR applications, with short descriptions, installation instructions, and basic setup tips for Debian-based systems.

* :ref:`install_gqrx_max`
* :ref:`install_sdrpp_max`
* :ref:`install_rtl433_max`
* :ref:`install_dump1090_max`


----

.. _install_gqrx_max:

GQRX
^^^^^^^^^^^^

GQRX is a simple, user-friendly SDR receiver application with a graphical interface. It supports a wide range of SDR devices and is ideal for listening to FM, AM, SSB, and other signals with real-time spectrum and waterfall displays.

You can also refer to the official Raspberry Pi installation guide here: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Option 1 – Quick Installation (Recommended for most users)**

Fast, simple, and integrates with system updates — but may not be the latest version.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Option 2 – Build from Source (Optional, Latest Features)**

Ensures the latest version and full customization, but takes longer to compile and requires more dependencies.

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

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall outdated ``librtlsdr``.  
After each installation, check:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it no longer points to ``/usr/local/lib/librtlsdr.so``, run:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


You can test immediately (or after a reboot for a clean environment):

.. code-block:: shell

   rtl_test -t

Expected output:

   * Contains RTL-SDR Blog V4 Detected.
   * No [R82XX] PLL not locked! messages.

**First Run Setup**

* **I/O Devices**:

  * Device: ``RTL-SDR (V4)``.
  * Input Rate: ``1.8 MSPS`` (1800000).

* **Input Controls**:

  * **LNA Gain**: Start around 25–35 dB, adjust as needed


* **Receiver Options**:

  * Set Frequency Correction (PPM) from your calibration.
  * Mode: ``WFM (mono or stereo)`` for broadcast FM.

----

.. _install_sdrpp_max:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ is a modern, fast, cross-platform software-defined radio (SDR) receiver that supports a variety of devices, including the RTL-SDR Blog V4. It offers a clean, user-friendly interface, wide modulation support, advanced DSP filtering, and recording capabilities.

You can refer to the official user manual here: https://www.sdrpp.org/manual.pdf


**Install from Source**

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

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall outdated ``librtlsdr``.  
After each installation, check:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it no longer points to ``/usr/local/lib/librtlsdr.so``, run:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


You can test immediately (or after a reboot for a clean environment):

.. code-block:: shell

   rtl_test -t

Expected output:

   * Contains RTL-SDR Blog V4 Detected.
   * No [R82XX] PLL not locked! messages.


**First Run Notes:**

After installation, SDR++ will appear in your desktop menu (usually under "Other"), or you can run:

   .. code-block:: shell

      sdrpp

* **Device:** Select **RTL-SDR (V4)** in the **Source** menu.
* **Sample Rate:** 1.8 MSPS is typical; lower if CPU load is high.
* **Gain:** Disable AGC and set manual gain (start ~35 dB).
* **PPM Correction:** Enter your calibration value from ``rtl_test -p``.
* **Demodulation Mode:** Choose WFM for FM broadcast, SSB for amateur bands, etc.

----

.. _install_rtl433_max:

rtl_433
^^^^^^^^^^^^


rtl_433 is a command-line tool to decode radio transmissions from devices operating in the 433 MHz ISM band, such as weather stations, tire pressure sensors, and wireless thermometers.

**Install:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall outdated ``librtlsdr``.  
After each installation, check:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it no longer points to ``/usr/local/lib/librtlsdr.so``, run:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


You can test immediately (or after a reboot for a clean environment):

.. code-block:: shell

   rtl_test -t

Expected output:

   * Contains RTL-SDR Blog V4 Detected.
   * No [R82XX] PLL not locked! messages.

**Basic Use:**

* Run ``rtl_433`` to automatically detect and decode common 433 MHz devices.
* Use ``rtl_433 -G`` to list all supported protocols.

----

.. _install_dump1090_max:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability is a Mode S decoder for ADS-B aircraft transponder data. It receives and decodes aircraft positions, speeds, and other flight data, and can serve a live map via a web browser.

**Install:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall outdated ``librtlsdr``.  
After each installation, check:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it no longer points to ``/usr/local/lib/librtlsdr.so``, run:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


You can test immediately (or after a reboot for a clean environment):

.. code-block:: shell

   rtl_test -t

Expected output:

   * Contains RTL-SDR Blog V4 Detected.
   * No [R82XX] PLL not locked! messages.

**Basic Use:**

* Run: ``dump1090 --interactive --net``.
* Open ``http://<raspberrypi-ip>:8080`` in your browser to view live aircraft tracking.



