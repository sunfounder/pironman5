.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas posventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a anuncios y vistas previas de nuevos productos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en promociones de temporada y sorteos especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Instalación de Umbrel OS
============================================

Umbrel es una plataforma/sistema operativo de código abierto para servidores domésticos que te permite ejecutar tu propio nodo de Bitcoin, instalar una variedad de aplicaciones autoalojadas con un solo clic y convertir tu hardware en tu nube personal. Es una excelente manera de comenzar con la autocustodia y la privacidad.

**Componentes requeridos**

* Un ordenador personal  
* Un SSD NVMe  
* Un adaptador NVMe a USB  
* Una tarjeta Micro SD y un lector

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

2. Installare il sistema operativo sull’SSD NVMe
-------------------------------------------------------------

**Passaggi**

1. Scarica l’ultima immagine di Umbrel OS ed estraila. Puoi anche visitare la `pagina dei rilasci di Umbrel <https://github.com/getumbrel/umbrel/releases>`_ per scegliere una versione specifica.

   * :download:`Ultima immagine di Umbrel OS <https://download.umbrel.com/release/latest/umbrelos-pi5.img.zip>`

2. In |link_rpi_imager|, fai clic su **Raspberry Pi Device** e seleziona **Raspberry Pi 5** dal menu a discesa.

   .. image:: img/os_choose_device_pi5.png
      :width: 90%

3. Avvia il **Raspberry Pi Imager** e fai clic su **CHOOSE OS**.

   .. image:: img/umbrel_choose_os.png
       :width: 600
       :align: center

4. Scorri fino in fondo e seleziona **Use custom**.

   .. image:: img/umbrel_use_custom.png
       :width: 600
       :align: center

5. Seleziona il file immagine di Umbrel OS che hai scaricato in precedenza e fai clic su **Open**.

   .. image:: img/umbrel_choose_umbrel.png
       :width: 600
       :align: center

6. Nella sezione **Storage**, seleziona l’SSD NVMe come destinazione per l’installazione.

   .. image:: img/nvme_ssd_storage.png
      :width: 90%

7. Clicca su **NEXT**, poi seleziona **NO**. Umbrel OS inizializzerà automaticamente il proprio sistema e la configurazione dell’utente durante il primo avvio e non utilizza il nome utente o la password impostati nel Raspberry Pi Imager.

   .. image:: img/umbrel_clear_setting.png
      :width: 90%

8. Se l’SSD NVMe contiene dati esistenti, esegui un backup prima di procedere per evitare la perdita di dati. Clicca su **Yes** per continuare se non è necessario alcun backup.

   .. image:: img/nvme_erase.png
      :width: 90%

9. Quando appare il messaggio “Write Successful”, significa che l’immagine è stata completamente scritta e verificata. Il tuo SSD NVMe è ora pronto per avviare il Raspberry Pi!

   .. image:: img/umbrel_finish.png
      :width: 90%


