.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message



FAQ
============


Solucion rapida de problemas
--------------------------------

* El botón de encendido no funciona → :ref:`faq_power_button_not_work_promax`
* La pantalla OLED no funciona → :ref:`faq_oled_promax`
* Los LED RGB no funcionan → :ref:`faq_rgb_promax`
* El ventilador no funciona → :ref:`promax_fan_faq`
* El panel de control no muestra datos → :ref:`faq_dashboard_promax`
* SSD NVMe no detectado → :ref:`faq_nvme_promax`
* SSD NVMe detectado pero causa reinicio del sistema → :ref:`faq_nvme_link_down_promax`
* La PI5 no arranca → :ref:`faq_pi5_boot_fail_promax`



1. Hardware
-------------------------------


.. _com_os_promax:

Sistemas compatibles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_com_os
   :end-before: end_faq_com_os


.. |link_safe_shutdown| replace:: :ref:`safe_shutdown_promax`

Botón de encendido
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_power_button
   :end-before: end_faq_power_button


.. _faq_power_button_not_work_promax:

El botón de encendido no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Primero, confirma el comportamiento esperado del botón de encendido:

   * **Raspberry Pi OS Desktop**: Presiona el botón de encendido dos veces rápidamente para apagar. Mantén presionado 5 segundos para forzar un apagado completo. Presiona una vez para encender desde el estado de apagado.
   * **Raspberry Pi OS Lite**: Presiona el botón de encendido una vez para apagar. Mantén presionado 5 segundos para forzar un apagado completo. Presiona una vez para encender.

#. Verifica que los pines del convertidor de alimentación estén correctamente alineados con los pads J2 del Raspberry Pi 5 (entre el conector de la batería RTC y el borde de la placa).

#. Verifica que los pines dentro del conector del convertidor de alimentación estén correctamente alineados con el conector del botón de encendido. Vuelve a conectar el cable del botón si es necesario.

#. Usa un destornillador para puentear brevemente los dos pines del conector del convertidor de alimentación donde se conecta el botón. Si la Pi se enciende, es posible que el botón esté defectuoso; de lo contrario, el problema probablemente esté en la placa convertidora o en la conexión con la Pi 5.


Extremos de los tubos de cobre del cooler de torre
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_copper_pipe_ends
   :end-before: end_faq_copper_pipe_ends


Raspberry Pi AI HAT+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Raspberry Pi AI HAT+ no es compatible con el Pironman 5 Pro MAX.

.. image:: img/output3.png
    :width: 400

El kit Raspberry Pi AI combina el Raspberry Pi M.2 HAT+ y el módulo acelerador de IA Hailo.

.. image:: img/output2.jpg
    :width: 400

Puedes separar el módulo acelerador Hailo AI del Raspberry Pi AI Kit e insertarlo directamente en el módulo NVMe PIP del Pironman 5 Pro MAX.


La pantalla de 4.3 pulgadas está en negro / no muestra imagen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La pantalla DSI de 4.3 pulgadas es plug-and-play — no requiere instalación de controladores adicionales.

.. note::

   El puente **ON/AUTO** en la placa HDMI/USB solo controla la salida de audio del altavoz. **No tiene ningún efecto** en la pantalla.

Si la pantalla está en negro o no muestra imagen, verifica lo siguiente:

#. Asegúrate de que el cable plano DSI esté conectado al puerto DSI correcto del Raspberry Pi 5.

#. Verifica que el cable plano esté completamente insertado, la abrazadera esté presionada firmemente y los contactos estén orientados en la dirección correcta.

#. Ejecuta el siguiente comando para confirmar si el sistema detecta la pantalla DSI:

   .. code-block:: shell

      sudo dmesg | grep -i dsi

   Si la pantalla es detectada, deberías ver una salida similar a ``DSI display found``. Si no hay salida, la pantalla no está siendo reconocida — vuelve a verificar la conexión física.


Pantalla HDMI externa — la barra de tareas solo aparece en la pantalla de 4.3 pulgadas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al conectar un monitor HDMI externo al Pironman 5 Pro MAX, es posible que la barra de tareas del escritorio permanezca en la pantalla DSI de 4.3 pulgadas integrada en lugar de moverse a la pantalla externa. Esto se debe a que el sistema utiliza la pantalla DSI como pantalla principal de forma predeterminada.

Si deseas configurar el monitor HDMI como pantalla principal al iniciar:

#. Crea un script de inicio:

   .. code-block:: shell

      sudo nano /usr/local/bin/fix-primary-screen.sh

#. Añade el siguiente contenido al script:

   .. code-block:: bash

      #!/bin/bash
      # Check if an external HDMI monitor is connected
      if wlr-randr | grep -q "HDMI-A-1"; then
          # Turn off the DSI screen first
          wlr-randr --output DSI-1 --off
          sleep 2
          # Re-enable DSI and place it to the right of HDMI
          wlr-randr --output DSI-1 --on --right-of HDMI-A-1
      fi

#. Haz que el script sea ejecutable:

   .. code-block:: shell

      sudo chmod +x /usr/local/bin/fix-primary-screen.sh

#. Añade el script al inicio automático. Edita el archivo de inicio de labwc:

   .. code-block:: shell

      nano ~/.config/labwc/autostart

   Añade la siguiente línea (el ``&`` lo ejecuta en segundo plano):

   .. code-block:: text

      /usr/local/bin/fix-primary-screen.sh &



2. Cooling and Fans
-------------------------------


.. _promax_fan_faq:

El ventilador no funciona / no se puede controlar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Pro MAX adopta la solución oficial de control de ventilador PWM de Raspberry Pi. Los tres ventiladores de refrigeración son controlados directamente por el sistema Raspberry Pi y no dependen del servicio pironman5 (por lo tanto, no verás opciones de control de ventiladores en la herramienta de línea de comandos ni en el panel de control).

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pwm_fan
   :end-before: end_faq_pwm_fan


El panel de control no muestra la velocidad del ventilador
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Pro MAX utiliza ventiladores personalizados de **5 pines** con la siguiente asignación: **PWM / 5V / GND / RGB Data In / RGB Data Out**.

Estos ventiladores **no** tienen un pin de tacómetro (retroalimentación de velocidad), por lo que el sistema no puede leer las RPM reales. Es normal y esperado que el panel de control no muestre la velocidad del ventilador.

La velocidad del ventilador es controlada por la curva de temperatura PWM nativa de la Raspberry Pi:

* < 50 °C: Apagado (0 %)
* 50 °C+: Bajo (30 %)
* 60 °C+: Medio (50 %)
* 67.5 °C+: Alto (70 %)
* 75 °C+: Velocidad máxima (100 %)



3. OLED and RGB
-------------------------------


.. _faq_oled_promax:

La pantalla OLED no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_set_up_pironman5| replace:: :ref:`promax_set_up_pi_os`
.. |link_compatible_systems| replace:: :ref:`com_os_promax`

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_oled
   :end-before: end_faq_oled


.. _faq_customize_oled_promax:

Cómo personalizar la pantalla OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_customize_oled
   :end-before: end_faq_customize_oled


.. _faq_rgb_promax:

Los LED RGB no funcionan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_rgb
   :end-before: end_faq_rgb


Cómo activar la pantalla OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para ahorrar energía y extender la vida útil de la pantalla, la pantalla OLED se apagará automáticamente después de un período de inactividad. Esto es parte del diseño normal y no afecta la funcionalidad del producto.

.. note::

   Para la configuración de la pantalla OLED (como encender/apagar, tiempo de reposo, rotación, etc.), consulta :ref:`promax_view_control_dashboard` o :ref:`promax_view_control_commands`.



4. Dashboard and Software
-------------------------------


.. _faq_dashboard_promax:

El panel de control no muestra datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_dashboard
   :end-before: end_faq_dashboard


.. |link_view_control_dashboard| replace:: :ref:`promax_view_control_dashboard`

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


.. |link_view_control_commands| replace:: :ref:`promax_view_control_commands`

Cómo controlar los componentes usando el comando ``pironman5``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pironman5_command
   :end-before: end_faq_pironman5_command


.. _faq_piper_tts_32bit_promax:

``pip install piper-tts`` falla con "Could Not Find a Version"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Al instalar ``sunfounder-voice-assistant`` en el Pironman 5 Pro MAX, es posible que encuentres el siguiente error:

.. code-block:: text

   ERROR: Could not find a version that satisfies the requirement piper-tts==1.3.0
   ERROR: No matching distribution found for piper-tts==1.3.0

Este error ocurre porque ``piper-tts`` 1.3.0 solo proporciona paquetes **de 64 bits** (``aarch64``). Si tu Raspberry Pi ejecuta un sistema operativo **de 32 bits**, pip no puede encontrar un paquete compatible.

**Solución:** Instala una versión de 64 bits de Raspberry Pi OS.

#. Verifica la arquitectura de tu sistema actual:

   .. code-block:: shell

      uname -m

   * ``aarch64`` → 64 bits (sin problema)
   * ``armv7l`` → 32 bits (necesita actualización)

#. Usa `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`_ para grabar una imagen **de 64 bits** de Raspberry Pi OS en tu dispositivo de almacenamiento.

#. Después de instalar el sistema operativo de 64 bits, reinstala el software ``pironman5`` y ``sunfounder-voice-assistant``.



5. Boot and Storage
-------------------------------


.. |link_update_bootloader| replace:: :ref:`update_bootloader_promax`

.. _faq_pi5_boot_fail_promax:

La PI5 no arranca (LED rojo)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_pi5_boot_fail
   :end-before: end_faq_pi5_boot_fail


.. _faq_nvme_promax:

El módulo NVMe PIP no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |link_install_the_os_dual| replace:: :ref:`install_the_os_promax`

.. include:: ../pironman5_max/faq.rst
   :start-after: start_faq_nvme_pip_dual
   :end-before: end_faq_nvme_pip_dual

#. Si el cableado es correcto y el SO está instalado, pero el SSD NVMe aún no arranca, intenta arrancar desde una tarjeta Micro SD para verificar la funcionalidad de otros componentes. Una vez confirmado, procede a :ref:`configure_boot_ssd_promax`.

#. Si el problema persiste después de realizar los pasos anteriores, envía un correo electrónico a service@sunfounder.com. Responderemos lo antes posible.


.. _faq_nvme_link_down_promax:

SSD NVMe detectado pero causa reinicio del sistema al leer/escribir
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../pironman5/faq.rst
   :start-after: start_faq_nvme_link_down
   :end-before: end_faq_nvme_link_down


.. |link_configure_boot_ssd| replace:: :ref:`configure_boot_ssd_promax`

Cómo cambiar el orden de arranque de la Raspberry Pi usando comandos


.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_command
   :end-before: end_faq_boot_order_command


Cómo modificar el orden de arranque con Raspberry Pi Imager


.. include:: ../pironman5/faq.rst
   :start-after: start_faq_boot_order_imager
   :end-before: end_faq_boot_order_imager


.. |link_copy_sd_to_nvme| replace:: :ref:`copy_sd_to_nvme_promax`

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


.. _promax_openssh_powershell:

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

#. Después de la instalación, se devolverá la siguiente salida.

   .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación con el siguiente comando.

   .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora te indica que ``OpenSSH.Client`` se ha instalado correctamente.

   .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

   .. warning::

        Si el mensaje anterior no aparece, significa que tu sistema Windows sigue siendo demasiado antiguo. Te recomendamos instalar una herramienta SSH de terceros, como |link_putty|.

#. Ahora reinicia PowerShell y continúa ejecutándolo como administrador. En este punto podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá que ingreses la contraseña que configuraste anteriormente.

   .. image:: img/powershell_login.png


Si configuro OMV, puedo seguir usando las funciones del Pironman5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sí, OpenMediaVault se configura en el sistema Raspberry Pi. Sigue los pasos de :ref:`promax_set_up_pi_os` para continuar con la configuración.


La cámara de la Raspberry Pi no funciona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando la cámara no funciona, el 90 % de los problemas están relacionados con la conexión del cable plano o con el hardware de la cámara.

Primero, usa ``rpicam-hello --list-cameras`` para confirmar si la cámara es detectada. Si se detecta correctamente, deberías ver un mensaje similar al siguiente:

.. code-block:: bash

   Available cameras
   -----------------
   0 : ov5647 [2592x1944] (/base/axi/pcie@1000120000/rp1/i2c@88000/ov5647@36)

Si la cámara no es detectada, verifica si el cable plano está invertido o no está completamente insertado. Si el problema persiste, intenta reemplazar el cable plano o el módulo de la cámara para hacer una prueba cruzada.


Puedo instalar Home Assistant OS en el Pironman 5 Pro MAX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El Pironman 5 Pro MAX no tiene su propio add-on dedicado de Home Assistant. Sin embargo, puedes usar el add-on de **Pironman 5 MAX** como alternativa — sigue la `guía del repositorio de add-ons de SunFounder <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_max/set_up/set_up_home_assistant.html#add-the-sunfounder-add-ons-repository>`_.

Ten en cuenta las siguientes limitaciones:

* **Pantalla de 4.3 pulgadas**: Home Assistant OS es un sistema **lite** sin entorno de escritorio. La pantalla de 4.3 pulgadas integrada en el Pro MAX no mostrará nada.

* **NVMe PIP de doble SSD**: Home Assistant OS no puede leer ambos SSD NVMe en el módulo NVMe PIP dual del Pro MAX.

* **Pantalla OLED y LED RGB**: Estos componentes funcionan normalmente después de instalar el add-on — no se requiere configuración adicional.

* **Ventilador de la CPU**: El ventilador de la CPU requiere configuración manual para funcionar bajo Home Assistant OS. Añade lo siguiente a ``/boot/firmware/config.txt``:

  .. code-block:: text

     dtparam=cooling_fan=on
     dtparam=fan_temp0=40000
     dtparam=fan_temp0_hyst=10000
     dtparam=fan_temp0_speed=125

  Después de guardar y reiniciar, el ventilador de la CPU será controlado por el sistema Raspberry Pi según la temperatura de la CPU. También puedes controlarlo manualmente mediante comandos ``pinctrl`` — consulta :ref:`promax_fan_faq`.