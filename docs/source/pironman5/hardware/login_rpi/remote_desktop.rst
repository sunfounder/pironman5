.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _remote_desktop:

Acceso de Escritorio Remoto para Raspberry Pi
==================================================

Para aquellos que prefieren una interfaz gráfica de usuario (GUI) en lugar del acceso por línea de comandos, Raspberry Pi admite funcionalidad de escritorio remoto. Esta guía te ayudará a configurar y utilizar VNC (Computación en Red Virtual) para el acceso remoto.

Recomendamos utilizar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS pero está deshabilitado por defecto. Sigue estos pasos para habilitarlo:

#. Ingresa el siguiente comando en la terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega hasta **Interfacing Options** usando la tecla de flecha hacia abajo, luego presiona **Enter**.

   .. image:: img/bookwarm_config_interface.png
      :width: 90%
      

#. Selecciona **VNC** de las opciones.

   .. image:: img/bookwarm_vnc.png
      :width: 90%
      

#. Usa las teclas de flecha para elegir **<Sí>** -> **<OK>** -> **<Finalizar>** y completa la activación del servicio VNC.

   .. image:: img/bookwarn_vnc_yes.png
      :width: 90%
      

**Iniciar sesión a través de VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, abre VNC Viewer. Ingresa el nombre de host o la dirección IP de tu Raspberry Pi y presiona Enter.

   .. image:: img/vnc_viewer1.png
      :width: 90%
      

#. Cuando se te solicite, ingresa el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

   .. image:: img/vnc_viewer2.png
      :width: 90%
      

#. Ahora tendrás acceso a la interfaz de escritorio de tu Raspberry Pi.

   .. image:: img/bookwarm.png
      :width: 90%
      
