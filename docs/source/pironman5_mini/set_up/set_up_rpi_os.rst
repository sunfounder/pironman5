.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas posventa y retos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Accede antes que nadie a los anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante celebraciones.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Descarga e instalación del módulo ``pironman5``
-----------------------------------------------------------

.. note::

   Para los sistemas “lite”, instala primero herramientas como ``git``, ``python3``, ``pip3``, ``setuptools``, etc.
   
   .. code-block:: shell
   
      sudo apt-get install git -y
      sudo apt-get install python3 python3-pip python3-setuptools -y

#. Procede a descargar el código desde GitHub e instalar el módulo ``pironman5``.

   .. code-block:: shell

      cd ~
      git clone -b mini https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Después de una instalación exitosa, es necesario reiniciar el sistema para activar la instalación. Sigue las indicaciones en pantalla para reiniciar.

   Al reiniciar, el servicio ``pironman5.service`` se iniciará automáticamente.  
   Estas son las configuraciones principales del Pironman 5 Mini:
   
   * Cuatro LED WS2812 RGB se iluminarán de color azul con un efecto de respiración.
     
   .. note::
    
     * Los ventiladores RGB están configurados por defecto en **Always On**.  
       Para establecer diferentes temperaturas de activación, consulta :ref:`cc_control_fan_mini`.

#. Puedes usar la herramienta ``systemctl`` para ``start``, ``stop``, ``restart`` o verificar el ``status`` del servicio ``pironman5.service``.

   .. code-block:: shell
     
      sudo systemctl restart pironman5.service
   
   * ``restart``: Usa este comando para aplicar cualquier cambio en la configuración del Pironman 5 Mini.  
   * ``start/stop``: Habilita o deshabilita el servicio ``pironman5.service``.  
   * ``status``: Verifica el estado operativo del programa ``pironman5`` utilizando la herramienta ``systemctl``.

.. note::

   En este punto, has configurado correctamente el Pironman 5 Mini y está listo para su uso.  
   Para el control avanzado de sus componentes, consulta :ref:`control_commands_dashboard_mini`.
