.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message




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

.. note::

    Two variants are in circulation: the **RTL-SDR Blog V4** and the **RTL-SDR Blog V4 Lite**.
    They carry different EEPROM product strings, so ``rtl_test`` reports either
    ``RTL-SDR Blog V4 Detected`` or ``RTL-SDR Blog V4 Lite Detected``. Both are correct, and
    everything below applies to both.

----

Install Driver for RTL-SDR Blog V4
-----------------------------------

On Linux the procedure is also simple and just involves removing any existing RTL-SDR drivers, and installing an updated version.

**1. Purge the Previous Driver**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

Verification A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No librtlsdr found in system cache."

**2. Install the Latest Drivers**

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

Note:
    If you also want to test FM reception from the command line (see below), install ``sox``,
    which provides the ``play`` command:

    .. code-block:: shell

       sudo apt install -y sox

Verification B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Should point to /usr/local/lib/librtlsdr.so

**3. Blacklist the DVB-T TV Drivers**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. Reboot**

.. code-block:: shell

   sudo reboot

**5. Verify Driver After Reboot**

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr
   rtl_test -t

Expected:
    The first command must print a path under ``/usr/local/lib/``. If it prints
    ``/lib/aarch64-linux-gnu/librtlsdr.so.0`` or any other system path, the loader is still
    picking up the outdated package library — see *Preventing Driver Overwrite* below.

    The second command should include ``RTL-SDR Blog V4 Detected`` — or
    ``RTL-SDR Blog V4 Lite Detected`` if you have the V4 Lite variant — with no
    ``[R82XX] PLL not locked!`` messages.
    The line ``Using device 0: Generic RTL2832U OEM`` is normal — it is just the USB name.


**6. Test FM Reception from Command Line**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

``scan.csv`` lists the measured power for every 100 kHz step; the highest values are your
local stations.

.. note::

   ``97.1M`` is only an example used in older versions of this page. Many areas have no
   station on that frequency, and you will hear nothing but noise even when the driver is
   working perfectly. Always pick a frequency from the scan above.

   ``-M wbfm`` outputs the 180 kHz MPX composite signal, not 48 kHz audio, and ``-r`` has no
   effect in that mode. The playback rate must therefore match ``-s`` (``180k`` above);
   otherwise the audio plays at the wrong speed.

Tips:

    * ``-g``: Try between 25–35 dB; higher is not always better.
    * Reduce ``-s`` to ~170k–180k to lower noise.
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

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall an outdated
``librtlsdr``. After each installation, check which library the tools actually load:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it does not point to ``/usr/local/lib/librtlsdr.so``, make the loader prefer
``/usr/local/lib`` — the prefix ``make install`` used. This leaves the Debian package
installed, so packages that depend on it (such as ``gqrx-sdr``) stay intact:

.. code-block:: shell

    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

Only if that does not help, remove the package and reinstall the driver:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Then verify immediately (or after a reboot for a clean environment):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr
   rtl_test -t

Expected output:

   * ``ldd`` resolves to ``/usr/local/lib/librtlsdr.so``.
   * Contains ``RTL-SDR Blog V4 Detected`` (or ``RTL-SDR Blog V4 Lite Detected``).
   * No ``[R82XX] PLL not locked!`` messages.

**First Run Setup**

* **I/O Devices**:

  * Device: ``RTL-SDR (V4)``.
  * Input Rate: ``1.8 MSPS`` (1800000).
  * Audio Output: select your USB speaker or sound card. On a Raspberry Pi 5 the default
    output may be HDMI, and a USB speaker connected through it stays silent.

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
     libfftw3-dev libvolk-dev libglfw3-dev libglew-dev \
     libzstd-dev librtaudio-dev

   git clone https://github.com/AlexandreRouma/SDRPlusPlus
   cd SDRPlusPlus
   mkdir build && cd build
   cmake .. -DOPT_BUILD_RTL_SDR_SOURCE=ON
   make
   sudo make install

.. note::

   The package is called ``libvolk-dev`` on Debian 13 (trixie) and later. On Debian 12
   (bookworm) — and Raspberry Pi OS based on it — the name is ``libvolk2-dev``; using the
   wrong one makes ``apt`` report *Unable to locate package*.

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall an outdated
``librtlsdr``. After each installation, check which library the tools actually load:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it does not point to ``/usr/local/lib/librtlsdr.so``, make the loader prefer
``/usr/local/lib`` — the prefix ``make install`` used. This leaves the Debian package
installed, so packages that depend on it (such as ``gqrx-sdr``) stay intact:

.. code-block:: shell

    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

Only if that does not help, remove the package and reinstall the driver:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Then verify immediately (or after a reboot for a clean environment):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr
   rtl_test -t

Expected output:

   * ``ldd`` resolves to ``/usr/local/lib/librtlsdr.so``.
   * Contains ``RTL-SDR Blog V4 Detected`` (or ``RTL-SDR Blog V4 Lite Detected``).
   * No ``[R82XX] PLL not locked!`` messages.


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

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall an outdated
``librtlsdr``. After each installation, check which library the tools actually load:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it does not point to ``/usr/local/lib/librtlsdr.so``, make the loader prefer
``/usr/local/lib`` — the prefix ``make install`` used. This leaves the Debian package
installed, so packages that depend on it (such as ``gqrx-sdr``) stay intact:

.. code-block:: shell

    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

Only if that does not help, remove the package and reinstall the driver:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Then verify immediately (or after a reboot for a clean environment):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr
   rtl_test -t

Expected output:

   * ``ldd`` resolves to ``/usr/local/lib/librtlsdr.so``.
   * Contains ``RTL-SDR Blog V4 Detected`` (or ``RTL-SDR Blog V4 Lite Detected``).
   * No ``[R82XX] PLL not locked!`` messages.

**Basic Use:**

* Run ``rtl_433`` to automatically detect and decode common 433 MHz devices.
* Run ``rtl_433 -R`` without an argument to list all supported protocols.
  The older ``-G`` flag no longer lists them; it is deprecated since 25.02.

----

.. _install_dump1090_max:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability is a Mode S decoder for ADS-B aircraft transponder data. It receives and decodes aircraft positions, speeds, and other flight data, and can serve a live map via a web browser.

**Install:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

.. note::

   ``dump1090-mutability`` is available in Debian 12 (bookworm), bullseye and earlier, but
   **not in Debian 13 (trixie)** — the package was removed from the archive, so ``apt``
   reports *Unable to locate package dump1090-mutability*.

   On Debian 13 there is no drop-in replacement in the archive: the ``readsb`` package is
   built **without** RTL-SDR support (``readsb --device-type rtlsdr`` answers *SDR type
   'rtlsdr' not recognized*). On those systems, build a decoder from source — for example
   ``readsb`` with ``make RTLSDR=yes``, or ``dump1090-fa``.

**Preventing Driver Overwrite**

When installing GQRX, SDR++, gnuradio-dev, or gr-osmosdr, the system may reinstall an outdated
``librtlsdr``. After each installation, check which library the tools actually load:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

If it does not point to ``/usr/local/lib/librtlsdr.so``, make the loader prefer
``/usr/local/lib`` — the prefix ``make install`` used. This leaves the Debian package
installed, so packages that depend on it (such as ``gqrx-sdr``) stay intact:

.. code-block:: shell

    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

Only if that does not help, remove the package and reinstall the driver:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Then verify immediately (or after a reboot for a clean environment):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr
   rtl_test -t

Expected output:

   * ``ldd`` resolves to ``/usr/local/lib/librtlsdr.so``.
   * Contains ``RTL-SDR Blog V4 Detected`` (or ``RTL-SDR Blog V4 Lite Detected``).
   * No ``[R82XX] PLL not locked!`` messages.

**Basic Use:**

* Run: ``dump1090 --interactive --net``.
* Open ``http://<raspberrypi-ip>:8080`` in your browser to view live aircraft tracking.



