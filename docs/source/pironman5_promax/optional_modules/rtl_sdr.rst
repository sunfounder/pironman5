
.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

RTL-SDR Blog V4
==============================================

.. note::

    Los productos de la serie Pironman 5 no incluyen los siguientes módulos.
    Necesita preparar uno usted mismo o comprarlo en nuestro sitio web oficial:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Esta guía cubre un procedimiento de instalación confiable para el RTL-SDR Blog V4, un receptor de radio definida por software (SDR) USB popular y asequible.
La versión V4 presenta un sintonizador R828D mejorado, modo de muestreo directo, mejor sensibilidad y bias-tee integrado para alimentar antenas activas.
Funciona bien para recibir FM comercial, banda aérea, radioaficionado, ADS-B y muchas otras señales en sistemas Linux y Raspberry Pi.

Para la documentación original del fabricante, consulte la guía oficial de RTL-SDR Blog V4: https://www.rtl-sdr.com/V4/

----

Instalar Controlador para RTL-SDR Blog V4
-------------------------------------------

En Linux el procedimiento también es sencillo: basta con eliminar los controladores RTL-SDR existentes e instalar una versión actualizada.

**1. Eliminar el controlador anterior**

.. code-block:: shell

   sudo apt purge ^librtlsdr
   sudo rm -rvf /usr/lib/librtlsdr* /usr/include/rtl-sdr* /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* /usr/local/include/rtl_* /usr/local/bin/rtl_*

Verificación A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: no se encontró librtlsdr en la caché del sistema."

**2. Instalar los controladores más recientes**

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

Nota:
    Si también se desea probar la recepción de FM desde la línea de comandos (ver más abajo),
    se necesita ``sox``, que proporciona el comando ``play``.

    .. code-block:: shell

       sudo apt install -y sox

Verificación B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Debe apuntar a /usr/local/lib/librtlsdr.so

**3. Bloquear los controladores DVB-T TV**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

**4. Reiniciar**

.. code-block:: shell

   sudo reboot

**5. Verificar el controlador después del reinicio**

.. code-block:: shell

   rtl_test -t

Resultado esperado:
    La salida debería incluir ``RTL-SDR Blog V4 Detected`` sin mensajes ``[R82XX] PLL not locked!``.
    La línea ``Using device 0: Generic RTL2832U OEM`` es normal — es solo el nombre USB.

**6. Probar Recepción FM desde la Línea de Comandos**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Consejos:

    * ``-g``: Pruebe entre 25–35 dB; más alto no siempre es mejor.
    * Reduzca ``-s`` a ~170k–180k para disminuir el ruido.
    * Ajuste ligeramente la frecuencia (ej. ``97.1005M``) para un ajuste fino.
    * Cierre cualquier otro software SDR que pueda tener el dispositivo.

----

Instalación de Software de Radio Común
----------------------------------------------------------------------

Esta sección presenta cuatro aplicaciones SDR ampliamente utilizadas, con descripciones breves, instrucciones de instalación y consejos básicos de configuración para sistemas basados en Debian.

* :ref:`install_gqrx_promax`
* :ref:`install_sdrpp_promax`
* :ref:`install_rtl433_promax`
* :ref:`install_dump1090_promax`

----

.. _install_gqrx_promax:

GQRX
^^^^^^^^^^^^

GQRX es una aplicación receptora SDR simple y fácil de usar con interfaz gráfica. Soporta una amplia gama de dispositivos SDR y es ideal para escuchar FM, AM, SSB y otras señales con visualización de espectro en tiempo real y waterfall.

También puede consultar la guía oficial de instalación para Raspberry Pi aquí: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Opción 1 – Instalación Rápida (Recomendada para la mayoría de usuarios)**

Rápida, simple y se integra con las actualizaciones del sistema — pero puede no ser la última versión.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Opción 2 – Compilar desde el Código Fuente (Opcional, Últimas Características)**

Asegura la última versión y personalización completa, pero tarda más en compilar y requiere más dependencias.

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

**Prevenir la Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` obsoleto.
Después de cada instalación, verifique:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecute:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puede probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Resultado esperado:

   * Contiene RTL-SDR Blog V4 Detected.
   * No hay mensajes [R82XX] PLL not locked!.

**Configuración del Primer Inicio**

* **I/O Devices**:

  * Device: ``RTL-SDR (V4)``.
  * Input Rate: ``1.8 MSPS`` (1800000).

* **Input Controls**:

  * **LNA Gain**: Comience alrededor de 25–35 dB, ajuste según sea necesario

* **Receiver Options**:

  * Establezca Frequency Correction (PPM) a partir de su calibración.
  * Mode: ``WFM (mono or stereo)`` para FM comercial.

----

.. _install_sdrpp_promax:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ es un receptor de radio definida por software (SDR) moderno, rápido y multiplataforma que soporta una variedad de dispositivos, incluyendo el RTL-SDR Blog V4. Ofrece una interfaz limpia y fácil de usar, amplio soporte de modulación, filtrado DSP avanzado y capacidades de grabación.

Puede consultar el manual de usuario oficial aquí: https://www.sdrpp.org/manual.pdf

**Instalar desde el Código Fuente**

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

**Prevenir la Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` obsoleto.
Después de cada instalación, verifique:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecute:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puede probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Resultado esperado:

   * Contiene RTL-SDR Blog V4 Detected.
   * No hay mensajes [R82XX] PLL not locked!.

**Notas del Primer Inicio:**

Después de la instalación, SDR++ aparecerá en su menú de escritorio (generalmente bajo "Other"), o puede ejecutar:

   .. code-block:: shell

      sdrpp

* **Device:** Seleccione **RTL-SDR (V4)** en el menú **Source**.
* **Sample Rate:** 1.8 MSPS es típico; más bajo si la carga de CPU es alta.
* **Gain:** Desactive AGC y establezca la ganancia manual (comience ~35 dB).
* **PPM Correction:** Ingrese su valor de calibración de ``rtl_test -p``.
* **Demodulation Mode:** Elija WFM para FM comercial, SSB para bandas de aficionados, etc.

----

.. _install_rtl433_promax:

rtl_433
^^^^^^^^^^^^

rtl_433 es una herramienta de línea de comandos para decodificar transmisiones de radio de dispositivos que operan en la banda ISM de 433 MHz, como estaciones meteorológicas, sensores de presión de neumáticos y termómetros inalámbricos.

**Instalar:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prevenir la Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` obsoleto.
Después de cada instalación, verifique:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecute:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puede probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Resultado esperado:

   * Contiene RTL-SDR Blog V4 Detected.
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecute ``rtl_433`` para detectar y decodificar automáticamente dispositivos comunes de 433 MHz.
* Use ``rtl_433 -G`` para listar todos los protocolos soportados.

----

.. _install_dump1090_promax:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability es un decodificador Mode S para datos de transpondedores de aeronaves ADS-B. Recibe y decodifica posiciones de aeronaves, velocidades y otros datos de vuelo, y puede servir un mapa en vivo a través de un navegador web.

**Instalar:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prevenir la Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` obsoleto.
Después de cada instalación, verifique:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecute:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig

Puede probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Resultado esperado:

   * Contiene RTL-SDR Blog V4 Detected.
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecute: ``dump1090 --interactive --net``.
* Abra ``http://<ip-de-la-raspberrypi>:8080`` en su navegador para ver el seguimiento de aeronaves en vivo.
