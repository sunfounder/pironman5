.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_remote_desktop:

Acceso remoto al escritorio de Raspberry Pi
==================================================

Para quienes prefieren una interfaz gráfica de usuario (GUI) en lugar del acceso por línea de comandos, Raspberry Pi ofrece compatibilidad con escritorio remoto. Esta guía te explicará cómo configurar y utilizar VNC (Virtual Network Computing) para el acceso remoto.

Recomendamos utilizar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS, pero está deshabilitado por defecto. Sigue estos pasos para activarlo:

#. Introduce el siguiente comando en la terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega hasta **Interfacing Options** usando la flecha hacia abajo y pulsa **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%


#. Selecciona **VNC** de entre las opciones.

   .. image:: img/bookwarm_vnc.png
      :width: 90%


#. Usa las teclas de flecha para elegir **<Yes>** -> **<OK>** -> **<Finish>** y finalizar la activación del servicio VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%


**Iniciar sesión mediante VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu ordenador personal.

#. Una vez instalado, abre VNC Viewer. Introduce el nombre de host o la dirección IP de tu Raspberry Pi y pulsa Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%


#. Cuando se te solicite, introduce el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%


#. Ahora tendrás acceso a la interfaz de escritorio de tu Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%

