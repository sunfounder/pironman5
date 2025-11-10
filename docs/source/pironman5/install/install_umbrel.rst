.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? ¡Haz clic en [|link_sf_facebook|] y únete hoy mismo!


Installazione di Umbrel OS
============================================

Umbrel è una piattaforma/OS open-source per server domestici che ti consente di eseguire il tuo nodo Bitcoin, installare una varietà di app self-hosted con un clic e trasformare il tuo hardware nel tuo cloud personale. È un modo eccellente per iniziare con l’autocustodia e la privacy.

**Componenti richiesti**

* Un computer personale  
* Un SSD NVMe  
* Un adattatore NVMe a USB  
* Una scheda Micro SD e un lettore

1. Actualizar el Bootloader
--------------------------------

Primero, es necesario actualizar el bootloader del Raspberry Pi 5 para que inicie desde NVMe antes de intentar desde USB y luego desde la tarjeta SD.

.. note::

    * En este paso, se recomienda usar una tarjeta Micro SD de repuesto. Primero escribe el bootloader en esta tarjeta Micro SD y luego insértala inmediatamente en el Raspberry Pi para habilitar el arranque desde un dispositivo NVMe.  
    * Alternativamente, puedes escribir el bootloader directamente en tu dispositivo NVMe, luego insertarlo en el Raspberry Pi para cambiar el método de arranque. Posteriormente, conecta el SSD NVMe a un ordenador para instalar el sistema operativo y, una vez completada la instalación, vuelve a insertarlo en el Raspberry Pi.

#. Inserta tu tarjeta Micro SD o SSD NVMe en el ordenador o portátil utilizando un lector.

#. Dentro de |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona el modelo **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

#. En la pestaña **Operating System**, desplázate hacia abajo y selecciona **Misc utility images**.

   .. image:: img/nvme_misc.png
      :width: 90%

#. Selecciona **Bootloader (Pi 5 family)**.

   .. image:: img/nvme_bootloader.png
      :width: 90%
      

#. Selecciona **NVMe/USB Boot** para permitir que el Raspberry Pi 5 arranque desde NVMe antes de intentar USB y luego la tarjeta SD.

   .. image:: img/nvme_nvme_boot.png
      :width: 90%
      
#. En la opción **Storage**, selecciona el dispositivo de almacenamiento apropiado para la instalación.

   .. note::

      Asegúrate de seleccionar el dispositivo de almacenamiento correcto. Para evitar confusiones, desconecta cualquier otro dispositivo de almacenamiento si hay más de uno conectado.

   .. image:: img/os_choose_sd.png
      :width: 90%
      

#. Ahora puedes hacer clic en **NEXT**. Si el dispositivo de almacenamiento contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Yes** si no es necesaria ninguna copia de seguridad.

   .. image:: img/os_continue.png
      :width: 90%
      

#. En breve se te informará que **NVMe/USB Boot** ha sido escrito en tu dispositivo de almacenamiento.

   .. image:: img/nvme_boot_finish.png
      :width: 90%
      

#. Inserta tu tarjeta Micro SD o SSD NVMe en el Raspberry Pi. Después de conectar el adaptador de alimentación Type-C, el bootloader desde la tarjeta Micro SD o el SSD NVMe se escribirá en la EEPROM del Raspberry Pi.

   .. note::

      * Después de la actualización, el Raspberry Pi arrancará primero desde la unidad NVMe, luego desde USB y finalmente desde la tarjeta Micro SD.  
      * Espera uno o dos minutos, luego apaga el Raspberry Pi y retira la tarjeta Micro SD o el SSD NVMe.

2. Instalar el sistema operativo en el SSD NVMe
------------------------------------------------------------

**Pasos**

1. Descarga la última imagen de Umbrel OS y extráela. También puedes visitar la `página de lanzamientos de Umbrel <https://github.com/getumbrel/umbrel/releases>`_ para elegir una versión específica.

   * :download:`Última imagen de Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. En |link_rpi_imager|, haz clic en **Raspberry Pi Device** y selecciona **Raspberry Pi 5** del menú desplegable.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Inicia **Raspberry Pi Imager** y haz clic en **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Desplázate hasta el final y selecciona **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Selecciona el archivo de imagen de Umbrel OS que descargaste previamente y haz clic en **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. En la sección **Storage**, selecciona el SSD NVMe como destino para la instalación.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Haz clic en **NEXT**, luego selecciona **NO**. Umbrel OS inicializará automáticamente su propio sistema y configuración de usuario durante el primer arranque y no utiliza el nombre de usuario ni la contraseña establecidos en Raspberry Pi Imager.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Si el SSD NVMe contiene datos existentes, realiza una copia de seguridad antes de continuar para evitar la pérdida de datos. Haz clic en **Yes** para continuar si no es necesaria ninguna copia de seguridad.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Cuando aparezca el mensaje “Write Successful”, significa que la imagen ha sido completamente escrita y verificada. ¡Tu SSD NVMe ahora está listo para iniciar el Raspberry Pi!

   .. image:: img/umbrel_finish.png
      :width: 90%


