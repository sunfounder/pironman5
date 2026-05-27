.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Solucion rapida de problemas
-------------------------------

* La pantalla OLED no funciona → :ref:`faq_oled_5`
* Los LED RGB no funcionan → :ref:`faq_rgb_5`
* Los ventiladores GPIO no funcionan → :ref:`faq_gpio_fans_5`
* El ventilador de la CPU no gira → :ref:`faq_pwm_fan_5`
* El panel web no muestra datos → :ref:`faq_dashboard_5`
* El SSD NVMe no se detecta → :ref:`faq_nvme_5`



1. Hardware
-------------------------------


.. _compatible_systems_5:

Sistemas compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_com_os

Sistemas que pasaron las pruebas en la Raspberry Pi 5:

.. image:: img/compitable_os.png
   :width: 600
   :align: center

.. end_faq_com_os

Boton de encendido
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_5`

.. start_faq_power_button

El boton de encendido extiende el boton de encendido original de la Raspberry Pi 5 y se comporta de manera similar.

* Pulsacion breve: Encender / activar la pantalla OLED / cambiar paginas de la OLED.
* Mantener pulsado 2 segundos: Apagado seguro (requiere |link_safe_shutdown|).
* Mantener pulsado 5 segundos: Apagado forzado.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

.. end_faq_power_button


Direccion del flujo de aire
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_airflow_direction

El flujo de aire dentro del Pironman 5 esta disenado para maximizar la eficiencia de refrigeracion. El aire fresco entra a traves de la abertura GPIO y otras rejillas, pasa a traves del disipador tipo torre y es expulsado por los dos ventiladores laterales GPIO.

Para una demostracion detallada, consulta el siguiente video:

.. raw:: html

    <div style="text-align: center;">
        <video center loop autoplay muted style="max-width:90%">
            <source src="../_static/video/airflow_direction.mp4"  type="video/mp4">
            Tu navegador no admite la etiqueta de video.
        </video>
    </div>

.. end_faq_airflow_direction


Extremos de los tubos de cobre del disipador tipo torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_copper_pipe_ends

Los extremos aplanados de los tubos de calor con forma de U son parte del proceso de fabricacion normal y estan disenados para permitir que los tubos de calor pasen a traves de las aletas de aluminio.

.. image:: img/tower_cooler1.png

.. end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_ai_hat

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5.

.. image:: img/output3.png
    :width: 400

El Raspberry Pi AI Kit combina el Raspberry Pi M.2 HAT+ y el modulo acelerador Hailo AI.

.. image:: img/output2.jpg
    :width: 400

Puedes separar el modulo acelerador Hailo AI del Raspberry Pi AI Kit e insertarlo directamente en el modulo NVMe PIP del Pironman 5.

.. image:: img/output4.png
    :width: 800

.. end_faq_ai_hat



2. Refrigeracion y ventiladores
-------------------------------


.. _faq_pwm_fan_5:

El ventilador de la CPU no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_pwm_fan

El ventilador de la CPU del Pironman 5 es controlado por el sistema de la Raspberry Pi. La velocidad del ventilador de la CPU depende de la temperatura de la CPU de la Raspberry Pi 5.

Curva predeterminada del ventilador de la CPU:

* < 50 °C: Apagado (0 %)
* 50 °C+: Velocidad baja (30 %)
* 60 °C+: Velocidad media (50 %)
* 67.5 °C+: Velocidad alta (70 %)
* 75 °C+: Velocidad maxima (100 %)

Verifica la temperatura actual de la CPU (ejemplo de salida: ``temp=48.7'C``):

.. code-block:: shell

   vcgencmd measure_temp

Puedes controlar manualmente el ventilador de la CPU usando los siguientes comandos:

.. code-block:: shell

   pinctrl FAN_PWM op dl   # Activar ventilador (activo bajo)
   pinctrl FAN_PWM op dh   # Desactivar ventilador (activo alto)
   pinctrl FAN_PWM a0      # Modo automatico

Tambien puedes ajustar los umbrales de temperatura del ventilador de la CPU editando:

.. code-block:: shell

   nano /boot/firmware/config.txt

Agrega:

.. code-block:: text

   dtparam=cooling_fan=on
   dtparam=fan_temp0=40000
   dtparam=fan_temp0_hyst=10000
   dtparam=fan_temp0_speed=125

Esta configuracion inicia el ventilador de la CPU a 40 °C con un nivel de velocidad PWM de 125.

Despues de guardar el archivo, reinicia la Raspberry Pi para que los cambios surtan efecto.

.. end_faq_pwm_fan


.. _faq_gpio_fans_5:

Los ventiladores GPIO no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_gpio_fans

Primero, verifica que el puente del ventilador en la placa del expansor de E/S este instalado correctamente.

.. image:: hardware/img/io_board_fan_j9.png

Luego, configura los ventiladores GPIO en modo ``Always On`` y verifica si los ventiladores comienzan a girar.

.. code-block:: shell

   sudo pironman5 -gm 0

Tambien puedes conectar los ventiladores GPIO directamente a los pines ``5V`` y ``GND`` de la Raspberry Pi para realizar pruebas.

Si los ventiladores giran con normalidad al conectarlos directamente, el problema puede estar relacionado con la placa del expansor de E/S. Por favor, contactanos para obtener mas ayuda.

Si el problema persiste, abre la pagina **Log** del panel web y verifica si hay mensajes de error. Tambien puedes enviarnos el siguiente archivo de registro:

.. code-block:: shell

   cat /var/log/pironman5/pironman5.log

.. end_faq_gpio_fans

3. OLED y RGB
-------------------------------


.. _faq_oled_5:

La pantalla OLED no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_5`
.. |link_compatible_systems| replace:: :ref:`compatible_systems_5`

.. start_faq_oled

Si la pantalla OLED no se muestra o se muestra incorrectamente, sigue estos pasos de solucion de problemas:

#. Asegurate de que el cable FPC de la pantalla OLED este firmemente conectado. Se recomienda reconectar la pantalla OLED y luego encender el dispositivo.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_oled_screen.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Confirma que la Raspberry Pi este ejecutando un sistema operativo compatible.

   Consulta |link_compatible_systems|.

#. Cuando la pantalla OLED se enciende por primera vez, es posible que solo muestre bloques de pixeles. Debes seguir las instrucciones en |link_set_up_pironman5| para completar la configuracion antes de que pueda mostrar informacion correctamente.

#. Usa el siguiente comando para verificar si se detecta la direccion I2C ``0x3C`` de la OLED:

   .. code-block:: shell

      sudo i2cdetect -y 1

   * Si se detecta la direccion I2C ``0x3C``, reinicia el servicio Pironman 5:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

   * Si no se detecta la direccion, habilita I2C:

     .. code-block:: shell

        sudo nano /boot/firmware/config.txt

     Agrega:

     .. code-block:: shell

        dtparam=i2c_arm=on

     Guarda el archivo y reinicia la Raspberry Pi.

#. Si el problema persiste, envianos el siguiente archivo de registro:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_oled


.. _faq_rgb_5:

Los LED RGB no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. start_faq_rgb

#. Los dos pines del expansor de E/S sobre J9 se utilizan para conectar los LED RGB a GPIO10. Asegurate de que el puente en estos dos pines este instalado correctamente.

   .. image:: hardware/img/io_board_rgb_pin.png
      :width: 300
      :align: center

#. Confirma que la Raspberry Pi este ejecutando un sistema operativo compatible.

   Consulta |link_compatible_systems|.

#. Ejecuta el siguiente comando para habilitar SPI:

   .. code-block:: shell

      sudo raspi-config

   Navega a:

   ``3 Interfacing Options`` → ``I3 SPI`` → ``YES``

   Luego reinicia la Raspberry Pi.

#. Si el problema persiste, envianos el siguiente archivo de registro:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_rgb

.. _faq_customize_oled_5:

Como personalizar la pantalla OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_customize_oled

Si deseas personalizar la pantalla OLED, como agregar displays de imagenes personalizadas de 2 a 4 digitos, puedes modificar los archivos de paginas de la OLED de las siguientes maneras.

* **Metodo 1: Modificar los archivos instalados directamente**

  #. Lista los archivos de paginas de la OLED:

     .. code-block:: shell

        ls /opt/pironman5/venv/lib/python3.13/site-packages/pm_auto/addons/oled/pages/

  #. Modifica los archivos de Python deseados.

  #. Reinicia el servicio para aplicar los cambios:

     .. code-block:: shell

        sudo systemctl restart pironman5.service


* **Metodo 2: Clonar y reinstalar ``pm_auto``**

  #. Clona el repositorio ``pm_auto``:

     .. code-block:: shell

        git clone -b 1.4.x https://github.com/sunfounder/pm_auto/

  #. Despues de realizar los cambios, reinstala el paquete modificado:

     .. code-block:: shell

        sudo /opt/pironman5/venv/bin/pip3 uninstall pm_auto -y && \
        sudo /opt/pironman5/venv/bin/pip3 install ~/pm_auto --no-build-isolation && \
        sudo chown -R pironman5:pironman5 /opt/pironman5

  #. Reinicia el servicio:

     .. code-block:: shell

        sudo systemctl restart pironman5.service

* **Pruebas y depuracion**

  Para ver los registros en tiempo de ejecucion:

  .. code-block:: shell

     journalctl -xefu pironman5.service

  Tambien puedes detener el servicio y ejecutarlo manualmente para realizar pruebas mas rapidas:

  .. code-block:: shell

     sudo systemctl stop pironman5.service
     sudo systemctl restart pironman5.service

.. end_faq_customize_oled

4. Panel web y software
-------------------------------


.. _faq_dashboard_5:

El panel web no muestra datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_dashboard

Si el panel web no muestra datos, primero abre la pagina **Log** del panel web y verifica si hay mensajes de error relacionados con ``influxdb``.

Los errores comunes incluyen:

* ``database not found``
* ``failed to connect to influxdb``
* ``connection refused``
* ``timeout``

Puedes intentar los siguientes pasos para resolver el problema.

#. Limpia la cache de tu navegador o vuelve a abrir la pagina del panel web usando el modo **Incognito / Privado**.

#. Verifica que los siguientes servicios se esten ejecutando correctamente:

   .. code-block:: shell

      sudo systemctl status pironman5 --no-pager
      sudo systemctl status influxdb --no-pager

   Ambos servicios deberian mostrar:

   .. code-block:: text

      active (running)

#. Si algun servicio no se esta ejecutando correctamente, reinicialos:

   .. code-block:: shell

      sudo systemctl restart influxdb
      sudo systemctl restart pironman5

   Luego espera unos 30 segundos y actualiza la pagina del panel web.

#. Verifica si la base de datos ``pironman5`` existe:

   .. code-block:: shell

      influx

   Luego ejecuta:

   .. code-block:: text

      SHOW DATABASES;

   Deberias ver:

   .. code-block:: text

      pironman5
      _internal

#. Si la base de datos falta o esta danada, puedes intentar borrar los datos historicos del panel web usando:

   ``Settings`` → ``Clear All Data``

#. Si el problema persiste despues de intentar todos los pasos anteriores, recomendamos reinstalar el sistema operativo Raspberry Pi y el software Pironman 5.

.. end_faq_dashboard


Como deshabilitar el panel web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_5`

.. start_faq_disable_dashboard

Una vez que hayas completado la instalacion del modulo ``pironman5``, podras acceder al |link_view_control_dashboard|.

Si no necesitas esta funcion y deseas reducir el uso de CPU y RAM, puedes deshabilitar el panel web durante la instalacion agregando la opcion ``--disable-dashboard``.

.. code-block:: shell

   cd ~/pironman5
   sudo python3 install.py --disable-dashboard

Si ya has instalado ``pironman5``, puedes eliminar el modulo del panel web e ``influxdb``:

.. code-block:: shell

   /opt/pironman5/env/bin/pip3 uninstall pm-dashboard influxdb
   sudo apt purge influxdb
   sudo systemctl restart pironman5

.. end_faq_disable_dashboard


Como desinstalar y reinstalar el software de Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_reinstall_pironman5

#. Desinstala el software actual de ``pironman5``:

   .. code-block:: shell

      cd ~/pironman5
      sudo python3 install.py --uninstall

#. Reinicia la Raspberry Pi cuando se te indique, luego elimina el directorio ``pironman5``:

   .. code-block:: shell

      cd ~/
      sudo rm -rf pironman5

#. Ejecuta el siguiente comando para reinstalar el software para tu modelo de Pironman 5:

   .. code-block:: shell

      curl -sSL "https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/pironman5/install.sh" | sudo bash

.. end_faq_reinstall_pironman5


Como controlar los componentes usando el comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`view_control_commands_5`

.. start_faq_pironman5_command

Puedes consultar el siguiente tutorial para controlar los componentes de la serie Pironman 5 usando el comando ``pironman5``.

* |link_view_control_commands|

.. end_faq_pironman5_command



5. Arranque y almacenamiento
-------------------------------


El PI5 no arranca (LED rojo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_5`

.. start_faq_pi5_boot_fail

Este problema puede deberse a una actualizacion del sistema, cambios en el orden de arranque o un cargador de arranque danado. Puedes intentar los siguientes pasos para resolver el problema:

#. Verificar la conexion del adaptador USB-HDMI

   * Verifica cuidadosamente que el adaptador USB-HDMI este firmemente conectado al PI5.
   * Intenta desconectar y volver a conectar el adaptador USB-HDMI.
   * Luego, vuelve a conectar la fuente de alimentacion y verifica si el PI5 arranca correctamente.

#. Probar el PI5 fuera de la carcasa

   * Si reconectar el adaptador no soluciona el problema:
   * Retira el PI5 de la carcasa de la serie Pironman 5.
   * Alimenta el PI5 directamente con el adaptador de corriente (sin la carcasa).
   * Verifica si puede arrancar con normalidad.

#. Restaurar el cargador de arranque

   * Si el PI5 aun no puede arrancar, es posible que el cargador de arranque este danado. Puedes seguir esta guia: |link_update_bootloader| y elegir si deseas arrancar desde una tarjeta SD o NVMe/USB.
   * Inserta la tarjeta SD preparada en el PI5, enciendelo y espera al menos 10 segundos. Una vez completada la recuperacion, retira y formatea la tarjeta SD.
   * Luego, usa Raspberry Pi Imager para grabar la ultima version de Raspberry Pi OS e intenta arrancar de nuevo.

.. end_faq_pi5_boot_fail


.. _faq_nvme_5:

El modulo NVMe PIP no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os| replace:: :ref:`install_the_os_5`
.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_5`

.. start_faq_nvme_pip

#. Asegurate de que el cable FPC que conecta el modulo NVMe PIP a la Raspberry Pi 5 este firmemente sujeto.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip1.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_nvme_pip2.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Confirma que tu SSD este correctamente fijado al modulo NVMe PIP.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/connect_ssd.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Verifica el estado de los LED del modulo NVMe PIP:

   * **PWR LED**: Deberia estar encendido.
   * **STA LED**: Deberia parpadear durante el funcionamiento normal.

   .. image:: img/nvme_pip_leds.png

   * Si el **PWR LED** esta encendido pero el **STA LED** no parpadea, el SSD NVMe no es reconocido.
   * Si el **PWR LED** esta apagado, puentea los pines ``Force Enable`` (J4).

     .. image:: img/nvme_pip_j4.png

#. Confirma que tu SSD NVMe contenga un sistema operativo valido.

   Consulta |link_install_the_os|.

#. Si el SSD aun no arranca, intenta arrancar desde una tarjeta Micro SD primero, luego configura el arranque NVMe:

   * |link_configure_boot_ssd|

#. Si el problema persiste, envianos el siguiente archivo de registro:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log

.. end_faq_nvme_pip


Como cambiar el orden de arranque de la Raspberry Pi usando comandos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_command

Si ya has iniciado sesion en tu Raspberry Pi, puedes cambiar el orden de arranque usando comandos.

* |link_configure_boot_ssd|

.. end_faq_boot_order_command


Como modificar el orden de arranque con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_boot_order_imager

Ademas de modificar ``BOOT_ORDER`` en la configuracion de la EEPROM, tambien puedes usar Raspberry Pi Imager para cambiar el orden de arranque.

* |link_update_bootloader|

.. end_faq_boot_order_imager


Como copiar el sistema de la tarjeta SD a un NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_5`

.. start_faq_copy_sd_to_nvme

Si no tienes un adaptador de NVMe a USB, primero puedes instalar el sistema en una tarjeta Micro SD y luego copiar el sistema al SSD NVMe despues de arrancar correctamente.

* |link_copy_sd_to_nvme|

.. end_faq_copy_sd_to_nvme



6. Uso avanzado
-------------------------------


Como retirar la pelicula protectora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. start_faq_remove_film

El paquete incluye dos paneles acrilicos, ambos cubiertos con una pelicula protectora amarilla/transparente en ambos lados para evitar rayones.

La pelicula protectora puede ser dificil de retirar. Usa un destornillador para levantar suavemente una esquina y luego pela con cuidado toda la pelicula.

.. image:: img/peel_off_film.jpg
    :width: 500
    :align: center

.. end_faq_remove_film
