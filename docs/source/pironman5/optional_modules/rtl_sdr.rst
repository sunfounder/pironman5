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

----

Instalar el Controlador para RTL-SDR Blog V4
--------------------------------------------------

**0. Preparación**

.. code-block:: shell

   sudo apt update
   sudo apt install -y git cmake build-essential pkg-config libusb-1.0-0-dev sox

Nota:  
    ``sox`` (proporciona el comando ``play``) se incluye para pruebas directas de audio.

**1. Limpieza Completa de Bibliotecas y Binarios Antiguos (Crítica)**

.. code-block:: shell

   sudo apt purge -y 'librtlsdr*'
   sudo rm -rf /usr/lib/librtlsdr* /usr/include/rtl-sdr* \
               /usr/local/lib/librtlsdr* /usr/local/include/rtl-sdr* \
               /usr/local/include/rtl_* /usr/local/bin/rtl_*
   sudo ldconfig

Verificación A:

.. code-block:: shell

   ldconfig -p | grep rtlsdr || echo "OK: No se encontró librtlsdr en la caché del sistema."

**2. Compilar e Instalar el Controlador RTL-SDR Blog V4**

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

Verificación B:

.. code-block:: shell

   which rtl_test
   ldd "$(which rtl_test)" | grep rtlsdr   # Debe apuntar a /usr/local/lib/librtlsdr.so

**3. Deshabilitar el Módulo del Kernel DVB y Reiniciar**

.. code-block:: shell

   echo 'blacklist dvb_usb_rtl28xxu' | sudo tee /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf
   sudo reboot

Nota:  
    Los comandos de recarga inmediata (``udevadm control --reload-rules`` y ``udevadm trigger``)  
    son opcionales si planeas reiniciar de inmediato.

**4. Verificar el Controlador Después del Reinicio**

.. code-block:: shell

   rtl_test -t

Esperado:  
    La salida debe incluir ``RTL-SDR Blog V4 Detected`` sin mensajes de ``[R82XX] PLL not locked!``.  
    La línea ``Using device 0: Generic RTL2832U OEM`` es normal — solo es el nombre USB.

**6. Probar la Recepción de FM desde la Línea de Comandos**

.. code-block:: shell

   rtl_fm -f 97.1M -M wbfm -s 180000 -r 48000 -g 28 | play -t raw -r 48k -e s -b 16 -c 1 -

Consejos:

    * ``-g``: Prueba entre 25–35 dB; más alto no siempre es mejor.  
    * Reduce ``-s`` a ~170k–180k para disminuir el ruido.  
    * Ajusta la frecuencia ligeramente (ej. ``97.1005M``) para un ajuste fino.  
    * Cierra cualquier otro software SDR que pueda estar usando el dispositivo.

----

Instalación de Software de Radio Común
-----------------------------------------

Esta sección presenta cuatro aplicaciones SDR ampliamente utilizadas, con breves descripciones, instrucciones de instalación y consejos básicos de configuración para sistemas basados en Debian.

* :ref:`install_gqrx_5`
* :ref:`install_sdrpp_5`
* :ref:`install_rtl433_5`
* :ref:`install_dump1090_5`


----

.. _install_gqrx_5:

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

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Configuración en la Primera Ejecución**

* **Dispositivos de E/S**:

  * Dispositivo: ``RTL-SDR (V4)``.  
  * Tasa de entrada: ``1.8 MSPS`` (1800000).

* **Controles de Entrada**:

  * **Ganancia LNA**: Comienza alrededor de 25–35 dB, ajusta según sea necesario.

* **Opciones del Receptor**:

  * Establece la Corrección de Frecuencia (PPM) según tu calibración.  
  * Modo: ``WFM (mono o estéreo)`` para FM comercial.

----

.. _install_sdrpp_5:

SDR++ (SDRpp)
^^^^^^^^^^^^^

SDR++ es un receptor SDR moderno, rápido y multiplataforma que soporta una variedad de dispositivos, incluido el RTL-SDR Blog V4. Ofrece una interfaz limpia y fácil de usar, amplio soporte de modulación, filtrado DSP avanzado y capacidades de grabación.

Puedes consultar el manual oficial aquí: https://www.sdrpp.org/manual.pdf


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

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

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

.. _install_rtl433_5:

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

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecuta ``rtl_433`` para detectar y decodificar automáticamente dispositivos comunes de 433 MHz.  
* Usa ``rtl_433 -G`` para listar todos los protocolos soportados.

----

.. _install_dump1090_5:

dump1090-mutability
^^^^^^^^^^^^^^^^^^^^^^^^^^^

dump1090-mutability es un decodificador Mode S para datos de transpondedor ADS-B de aeronaves. Recibe y decodifica posiciones de aviones, velocidades y otros datos de vuelo, y puede servir un mapa en vivo a través de un navegador web.

**Instalar:**

.. code-block:: shell

   sudo apt install -y dump1090-mutability

**Prevención de Sobrescritura del Controlador**

Al instalar GQRX, SDR++, gnuradio-dev o gr-osmosdr, el sistema puede reinstalar ``librtlsdr`` desactualizado.  
Después de cada instalación, comprueba:

.. code-block:: shell

    ldd "$(which rtl_test)" | grep rtlsdr

Si ya no apunta a ``/usr/local/lib/librtlsdr.so``, ejecuta:

.. code-block:: shell

    sudo apt purge -y 'librtlsdr*'
    sudo ldconfig
    cd ~/rtl-sdr-blog/build && sudo make install && sudo ldconfig


Puedes probar inmediatamente (o después de un reinicio para un entorno limpio):

.. code-block:: shell

   rtl_test -t

Salida esperada:

   * Contiene RTL-SDR Blog V4 Detected.  
   * No hay mensajes [R82XX] PLL not locked!.

**Uso Básico:**

* Ejecuta: ``dump1090 --interactive --net``.  
* Abre ``http://<raspberrypi-ip>:8080`` en tu navegador para ver el rastreo en vivo de aeronaves.
