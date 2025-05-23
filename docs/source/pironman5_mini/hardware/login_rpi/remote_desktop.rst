.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede anticipadamente a nuevos anuncios y vistas previas de productos.
    - **Descuentos especiales**: Aprovecha descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _remote_desktop_mini:

Acceso remoto al escritorio de Raspberry Pi
==================================================

Para quienes prefieren una interfaz gráfica de usuario (GUI) en lugar del acceso por línea de comandos, Raspberry Pi admite funcionalidad de escritorio remoto. Esta guía te mostrará cómo configurar y usar VNC (Virtual Network Computing) para acceder de forma remota.

Recomendamos utilizar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Activar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS, pero está desactivado por defecto. Sigue estos pasos para habilitarlo:

#. Introduce el siguiente comando en la terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega hasta **Interfacing Options** usando la tecla de flecha hacia abajo y presiona **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. Selecciona **VNC** de las opciones disponibles.

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. Utiliza las teclas de flecha para seleccionar **<Yes>** -> **<OK>** -> **<Finish>** y así completar la activación del servicio VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**Iniciar sesión con VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, abre VNC Viewer. Introduce el nombre de host o la dirección IP de tu Raspberry Pi y presiona Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. Cuando se te solicite, introduce el nombre de usuario y la contraseña de tu Raspberry Pi y haz clic en **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Ahora tendrás acceso a la interfaz de escritorio de tu Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

