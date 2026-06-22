.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

FAQ
============


Solucion rapida de problemas
-------------------------------

* El boton de encendido no funciona → :ref:`faq_power_button_not_work_max`
* La pantalla OLED no funciona → :ref:`faq_oled_max`
* Los LED RGB no funcionan → :ref:`faq_rgb_max`
* Los ventiladores GPIO no funcionan → :ref:`faq_gpio_fans_max`
* El ventilador de la CPU no gira → :ref:`faq_pwm_fan_max`
* El panel web no muestra datos → :ref:`faq_dashboard_max`
* El SSD NVMe no se detecta → :ref:`faq_nvme_max`
* El SSD NVMe se detecta pero provoca un reinicio del sistema → :ref:`faq_nvme_link_down_max`



1. Hardware
-------------------------------


.. _com_os_max:

Sistemas compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os

Boton de encendido
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_max:

El boton de encendido no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button_not_work
   :end-before: end_faq_power_button_not_work


Extremos de los tubos de cobre del disipador tipo torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La Raspberry Pi AI HAT+ no es compatible con el Pironman 5 MAX.

.. image:: img/output3.png
    :width: 400

El Raspberry Pi AI Kit combina la Raspberry Pi M.2 HAT+ y el modulo acelerador Hailo AI.

.. image:: img/output2.jpg
    :width: 400

Puedes separar el modulo acelerador Hailo AI del Raspberry Pi AI Kit e insertarlo directamente en el modulo NVMe PIP del Pironman 5 MAX.

Puedo usar la funcion del interruptor de vibracion del Pironman5 Max?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A partir de la version v1.3.6, la activacion de la pantalla OLED utiliza el boton de encendido. Debes retirar el puente del interruptor de vibracion para evitar ocupar los pines GPIO de la Raspberry Pi y prevenir posibles conflictos. Verifica si este puente existe; si no es asi, ignora este aviso.

.. image:: /pironman5_max/img/remove_vib_jumper.jpg

2. Refrigeracion y ventiladores
---------------------------------


.. _faq_pwm_fan_max:

El ventilador de la CPU no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


.. _faq_gpio_fans_max:

Los ventiladores GPIO no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_gpio_fans
   :end-before: end_faq_gpio_fans


3. OLED y RGB
-------------------------------


.. _faq_oled_max:

La pantalla OLED no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_compatible_systems| replace:: :ref:`com_os_max`
.. |link_set_up_pironman5| replace:: :ref:`set_up_pironman5_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled

.. _faq_rgb_max:

Los LED RGB no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


.. _faq_customize_oled_max:

Como personalizar la pantalla OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


4. Panel web y software
-------------------------------


.. _faq_dashboard_max:

El panel web no muestra datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard

Como deshabilitar el panel web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Como desinstalar y reinstalar el software de Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


Como controlar los componentes usando el comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_view_control_commands| replace:: :ref:`max_view_control_commands`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


5. Arranque y almacenamiento
-------------------------------

Si configuro OMV, puedo seguir usando las funciones del Pironman5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si, OpenMediaVault se instala sobre el sistema Raspberry Pi. Sigue los pasos de :ref:`set_up_os_max` para continuar con la configuracion.


El PI5 no arranca (LED rojo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_update_bootloader| replace:: :ref:`update_bootloader_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail

.. _faq_nvme_max:

El modulo NVMe PIP no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_max`

.. start_faq_nvme_pip_dual

#. Confirma que tu SSD NVMe sea compatible. Consulta la :ref:`lista de SSD NVMe compatibles <compitable_nvme_ssd_5>` para obtener unidades verificadas, estables y compatibles.

#. Asegurate de que el cable FPC que conecta el modulo NVMe PIP a la Raspberry Pi 5 este firmemente sujeto.

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(1)-11.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

   .. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="../_static/video/Nvme(2)-11.mp4" type="video/mp4">
               Tu navegador no admite la etiqueta de video.
           </video>
       </div>

#. Confirma que tu SSD este correctamente fijado al modulo NVMe PIP.

#. Verifica el estado de los LED del modulo NVMe PIP:

   Despues de confirmar todas las conexiones, enciende el Pironman 5 MAX y observa los dos indicadores en el modulo NVMe PIP:

   * **PWR LED**: Deberia estar encendido.
   * **STA LED**: Deberia parpadear para indicar el funcionamiento normal.

   .. image:: img/dual_nvme_pip_leds.png

   * Si el **PWR LED** esta encendido pero el **STA LED** no parpadea, indica que el SSD NVMe no es reconocido por la Raspberry Pi.
   * Si el **PWR LED** esta apagado, puentea los pines ``Force Enable`` en el modulo. Si el **PWR LED** se enciende, podria indicar un cable FPC suelto o una configuracion del sistema no compatible con NVMe.

   .. image:: img/dual_nvme_pip_j4.png


#. Confirma que tu SSD NVMe tenga un sistema operativo correctamente instalado. Consulta |link_install_the_os_dual|.

.. end_faq_nvme_pip_dual

#. Si el problema persiste, envianos el siguiente archivo de registro:

   .. code-block:: shell

      cat /var/log/pironman5/pironman5.log


.. _faq_nvme_link_down_max:

El SSD NVMe se detecta pero provoca un reinicio del sistema al leer/escribir?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


Como cambiar el orden de arranque de la Raspberry Pi usando comandos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Como modificar el orden de arranque con Raspberry Pi Imager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager

Como copiar el sistema de la tarjeta SD a un NVMe SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_max`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme

6. Uso avanzado
-------------------------------

Como retirar la pelicula protectora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film
