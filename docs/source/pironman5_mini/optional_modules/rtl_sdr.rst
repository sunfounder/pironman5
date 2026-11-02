.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


RTL-SDR Blog V4
==============================================

.. note::

    Los productos de la serie Pironman 5 no incluyen los siguientes módulos.  
    Necesitas preparar uno por tu cuenta o comprarlo en nuestro sitio web oficial:

    * `RTL-SDR Blog V4 <https://www.sunfounder.com/products/rtl-sdr-blog-v4>`_

Esta guía cubre un procedimiento de instalación confiable para el RTL-SDR Blog V4, un receptor de radio definido por software (SDR) USB popular y asequible.  
La versión V4 cuenta con un sintonizador R828D mejorado, modo de muestreo directo, mejor sensibilidad y bias-tee integrado para alimentar antenas activas.  
Funciona bien para recibir FM comercial, banda aérea, radioaficionados, ADS-B y muchas otras señales en sistemas Linux y Raspberry Pi.

Para la documentación del fabricante original, consulta la guía oficial del RTL-SDR Blog V4: https://www.rtl-sdr.com/V4/

.. note::

    Existen dos variantes: el **RTL-SDR Blog V4** y el **RTL-SDR Blog V4 Lite**.
    Tienen cadenas de producto EEPROM distintas, por lo que ``rtl_test`` muestra
    ``RTL-SDR Blog V4 Detected`` o ``RTL-SDR Blog V4 Lite Detected``. Ambas son correctas,
    y todos los pasos siguientes se aplican a las dos.

----

Instalar el Controlador para RTL-SDR Blog V4
-------------------------------------------------

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

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Esperado:  
    La salida debe incluir ``RTL-SDR Blog V4 Detected`` sin mensajes de ``[R82XX] PLL not locked!``.  
    La línea ``Using device 0: Generic RTL2832U OEM`` es normal — solo es el nombre USB.

**6. Probar la Recepción de FM desde la Línea de Comandos**

.. code-block:: shell

   # 1) Scan the FM band and find a frequency that has a station near you
   rtl_power -f 87.5M:108M:100k -i 3 -e 10 scan.csv

   # 2) Listen to one of the strongest ones (replace 104.9M with your own)
   #    Note: -M wbfm outputs the 180 kHz MPX, not 48 kHz audio, and -r is ignored.
   #    The playback rate must match -s, otherwise the audio plays at the wrong speed.
   rtl_fm -f 104.9M -M wbfm -s 180000 -g 28 | play -t raw -r 180k -e s -b 16 -c 1 -

Consejos:

    * ``-g``: Prueba entre 25–35 dB; más alto no siempre es mejor.  
    * Reduce ``-s`` a ~170k–180k para disminuir el ruido.  
    * Ajusta la frecuencia ligeramente (ej. ``97.1005M``) para un ajuste fino.  
    * Cierra cualquier otro software SDR que pueda estar usando el dispositivo.

----

Instalación de Software de Radio Común
---------------------------------------

Esta sección presenta cuatro aplicaciones SDR ampliamente utilizadas, con breves descripciones, instrucciones de instalación y consejos básicos de configuración para sistemas basados en Debian.

* :ref:`install_gqrx_mini`
* :ref:`install_sdrpp_mini`
* :ref:`install_rtl433_mini`
* :ref:`install_dump1090_mini`


----

.. _install_gqrx_mini:

GQRX
^^^^^^^^^^^^

GQRX es una aplicación receptora SDR simple y fácil de usar con interfaz gráfica. Soporta una amplia gama de dispositivos SDR y es ideal para escuchar FM, AM, SSB y otras señales con espectro en tiempo real y visualizaciones waterfall.

También puedes consultar la guía oficial de instalación para Raspberry Pi aquí: https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi

**Opción 1 – Instalación Rápida (Recomendada para la mayoría de usuarios)**

Rápida, simple e integrada con las actualizaciones del sistema — pero puede que no sea la última versión.

.. code-block:: shell

   sudo apt update
   sudo apt install -y --no-install-recommends gqrx-sdr

**Opción 2 – Compilar desde el Código Fuente (Opcional, Últimas Funciones)**

Garantiza la última versión y personalización completa, pero tarda más en compilar y requiere más dependencias.

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

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Configuración en la Primera Ejecución**

* **Dispositivos de E/S**:

  * Dispositivo: ``RTL-SDR (V4)``.  
  * Tasa de entrada: ``1.8 MSPS`` (1800000).
  * Audio Output (salida de audio): selecciona tu altavoz USB o tarjeta de sonido. En una
    Raspberry Pi 5 la salida predeterminada puede ser HDMI, y un altavoz USB conectado a ella
    no suena.

* **Controles de Entrada**:

  * **Ganancia LNA**: Comienza alrededor de 25–35 dB, ajusta según sea necesario.

* **Opciones del Receptor**:

  * Establece la Corrección de Frecuencia (PPM) según tu calibración.  
  * Modo: ``WFM (mono o estéreo)`` para FM comercial.

----

.. _install_sdrpp_mini:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ es un receptor SDR moderno, rápido y multiplataforma que soporta una variedad de dispositivos, incluido el RTL-SDR Blog V4. Ofrece una interfaz limpia y fácil de usar, amplio soporte de modulación, filtrado DSP avanzado y capacidades de grabación.

Puedes consultar el manual oficial aquí: https://www.sdrpp.org/manual.pdf


**Instalar desde el Código Fuente**

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

   En Debian 13 (trixie) y posteriores el paquete se llama ``libvolk-dev``. En Debian 12
   (bookworm) —y en el Raspberry Pi OS basado en él— se llama ``libvolk2-dev``; con el nombre
   equivocado ``apt`` muestra *Unable to locate package*.

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Notas de la Primera Ejecución:**

Después de la instalación, SDR++ aparecerá en el menú de tu escritorio (usualmente bajo "Otros"), o puedes ejecutar:

   .. code-block:: shell

      sdrpp

* **Dispositivo:** Selecciona **RTL-SDR (V4)** en el menú **Source**.  
* **Tasa de muestreo:** 1.8 MSPS es típico; baja si la carga de CPU es alta.  
* **Ganancia:** Desactiva AGC y ajusta manualmente (comienza ~35 dB).  
* **Corrección PPM:** Introduce tu valor de calibración desde ``rtl_test -p``.  
* **Modo de Demodulación:** Elige WFM para FM comercial, SSB para bandas de radioaficionados, etc.

----

.. _install_rtl433_mini:

rtl_433
^^^^^^^^^^^^

rtl_433 es una herramienta de línea de comandos para decodificar transmisiones de radio de dispositivos que operan en la banda ISM de 433 MHz, como estaciones meteorológicas, sensores de presión de neumáticos y termómetros inalámbricos.

**Instalar:**

.. code-block:: shell

   sudo apt install -y rtl-433

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecuta ``rtl_433`` para detectar y decodificar automáticamente dispositivos comunes de 433 MHz.  
* Ejecuta ``rtl_433 -R`` sin argumentos para listar todos los protocolos soportados.
  La opción antigua ``-G`` ya no los lista; está obsoleta desde la 25.02.

----

.. _install_dump1090_mini:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability es un decodificador Mode S para datos de transpondedor ADS-B de aeronaves. Recibe y decodifica posiciones de aviones, velocidades y otros datos de vuelo, y puede servir un mapa en vivo a través de un navegador web.

**Instalar:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

.. note::

   ``dump1090-mutability`` está disponible en Debian 12 (bookworm), bullseye y anteriores,
   pero **no en Debian 13 (trixie)**: el paquete se eliminó del archivo y ``apt`` muestra
   *Unable to locate package dump1090-mutability*.

   En Debian 13 no hay un sustituto directo en el archivo: el paquete ``readsb`` está
   compilado **sin** soporte de RTL-SDR (``readsb --device-type rtlsdr`` responde *SDR type
   'rtlsdr' not recognized*). En esos sistemas hay que compilar un decodificador desde el
   código fuente — por ejemplo ``readsb`` con ``make RTLSDR=yes``, o ``dump1090-fa``.

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    # preferred: make the loader prefer /usr/local/lib (keeps the Debian package intact)
    echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/00-local-first.conf
    sudo ldconfig

    # fallback: remove the package and reinstall the driver
    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   ldd "$(which rtl_test)" | grep rtlsdr   # must resolve to /usr/local/lib/librtlsdr.so
   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecuta: ``dump1090 --interactive --net``.  
* Abre ``http://<raspberrypi-ip>:8080`` en tu navegador para ver el rastreo en vivo de aeronaves.
