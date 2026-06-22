.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Solucion rapida de problemas
--------------------------------

* El botón de encendido no funciona → :ref:`faq_power_button_not_work_mini`
* Los LED RGB no funcionan → :ref:`faq_rgb_mini`
* El ventilador de la CPU no gira → :ref:`faq_pwm_fan_mini`
* El panel de control no muestra datos → :ref:`faq_dashboard_mini`
* La PI5 no arranca → :ref:`faq_pi5_boot_fail_mini`



1. Hardware
-------------------------------


.. _com_os_mini:

Sistemas compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


Botón de encendido
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El botón de encendido expone la función del botón de encendido del Raspberry Pi 5 y actúa de la misma manera.

.. image:: img/power_button.jpg
    :width: 400
    :align: center

* **Apagado**

  * Si utilizas el sistema **Raspberry Pi OS Desktop**, puedes presionar dos veces rápidamente el botón de encendido para apagarlo.
  * Si utilizas el sistema **Raspberry Pi OS Lite**, presiona una vez el botón de encendido para iniciar el apagado.
  * Para forzar un apagado, mantén presionado el botón de encendido.

* **Encendido**

  * Si la Raspberry Pi está apagada pero sigue recibiendo energía, presiona una vez para encenderla.

* Si tu sistema no admite el botón de apagado, mantén presionado por 5 segundos para forzar el apagado, y presiona una vez para encenderla.


.. _faq_power_button_not_work_mini:

El botón de encendido no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Primero, confirma el comportamiento esperado del botón de encendido:

   * **Raspberry Pi OS Desktop**: Presiona el botón de encendido dos veces rápidamente para apagar. Mantén presionado 5 segundos para forzar un apagado completo. Presiona una vez para encender desde el estado de apagado.
   * **Raspberry Pi OS Lite**: Presiona el botón de encendido una vez para apagar. Mantén presionado 5 segundos para forzar un apagado completo. Presiona una vez para encender.

#. Verifica que los pines del convertidor de alimentación estén correctamente alineados con los pads J2 del Raspberry Pi 5 (entre el conector de la batería RTC y el borde de la placa).

#. Verifica que los pines dentro del conector del convertidor de alimentación estén correctamente alineados con el conector del botón de encendido. Vuelve a conectar el cable del botón si es necesario.

#. Usa un destornillador para puentear brevemente los dos pines del conector del convertidor de alimentación donde se conecta el botón. Si la Pi se enciende, es posible que el botón esté defectuoso; de lo contrario, el problema probablemente esté en la placa convertidora o en la conexión con la Pi 5.


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5.

   .. image::  img/output3.png
        :width: 400

El kit Raspberry Pi AI combina el M.2 HAT+ con el módulo acelerador de IA Hailo.

   .. image::  img/output2.jpg
        :width: 400

Puedes separar el módulo acelerador Hailo AI del Raspberry Pi AI Kit e insertarlo directamente en el HAT del Pironman 5 Mini.


Cable Micro HDMI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recomendamos usar el cable Micro HDMI oficial de Raspberry Pi. Algunos cables de terceros con una longitud de conector inferior a 65 mm pueden causar mal contacto y problemas de visualización.

.. image:: img/need_mini_hdmi.png
   :width: 400



2. Cooling and Fans
-------------------------------


.. _faq_pwm_fan_mini:

El ventilador de la CPU no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan



3. RGB
-------------------------------


.. |link_compatible_systems| replace:: :ref:`com_os_mini`

.. _faq_rgb_mini:

Los LED RGB no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_mini:

El panel de control no muestra datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`view_control_dashboard_mini`

Cómo desactivar el panel web
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_disable_dashboard
   :end-before: end_faq_disable_dashboard


Cómo desinstalar y reinstalar el software Pironman 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_reinstall_pironman5
   :end-before: end_faq_reinstall_pironman5


.. |link_view_control_commands| replace:: :ref:`view_control_commands_mini`

Cómo controlar los componentes usando el comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command



5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_mini`

.. _faq_pi5_boot_fail_mini:

La PI5 no arranca (LED rojo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este problema puede deberse a una actualización del sistema, cambios en el orden de arranque o un cargador de arranque dañado. Puedes intentar los siguientes pasos para resolver el problema:

#. Vuelve a conectar la fuente de alimentación y verifica si la PI5 arranca correctamente.

#. Prueba la PI5 fuera de la carcasa

   * Retira la PI5 de la carcasa del Pironman 5 Mini.
   * Alimenta la PI5 directamente con el adaptador de corriente (sin la carcasa).
   * Verifica si puede arrancar normalmente.

#. Restaura el cargador de arranque

   * Si la PI5 aún no puede arrancar, es posible que el cargador de arranque esté dañado. Puedes seguir esta guía: |link_update_bootloader| y elegir si deseas arrancar desde la tarjeta SD o NVMe/USB.
   * Inserta la tarjeta SD preparada en la PI5, enciéndela y espera al menos 10 segundos. Una vez completada la recuperación, retira y formatea la tarjeta SD.
   * Luego, usa Raspberry Pi Imager para grabar la última versión de Raspberry Pi OS e intenta arrancar de nuevo.


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_mini`

Cómo cambiar el orden de arranque de la Raspberry Pi usando comandos


.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Cómo modificar el orden de arranque con Raspberry Pi Imager


.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_mini`

Cómo copiar el sistema desde la tarjeta SD a un SSD NVMe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copy_sd_to_nvme
   :end-before: end_faq_copy_sd_to_nvme



6. Advanced Usage
-------------------------------


Cómo retirar la película protectora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_remove_film
   :end-before: end_faq_remove_film


.. _openssh_powershell_mini:

Cómo instalar OpenSSH mediante PowerShell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando usas ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) para conectarte a tu Raspberry Pi, pero aparece el siguiente mensaje de error:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Significa que tu sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado. Debes seguir el siguiente tutorial para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda del escritorio de Windows, haz clic derecho sobre ``Windows PowerShell`` y selecciona ``Run as administrator`` en el menú que aparece.

   .. image:: img/powershell_ssh.png
      :width: 90%


#. Usa el siguiente comando para instalar ``OpenSSH.Client``.

   .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Tras la instalación, deberías ver una salida como la siguiente:

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación con el siguiente comando:

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Esto confirmará que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Si el mensaje anterior no aparece, significa que tu sistema Windows sigue siendo demasiado antiguo. Te recomendamos instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicia PowerShell y continúa ejecutándolo como administrador. En este punto podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá que ingreses la contraseña que configuraste anteriormente.

   .. image:: img/powershell_login.png
