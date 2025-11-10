.. note:: 

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más a fondo en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _max_login_rpi:

Iniciar sesión en Raspberry Pi OS
=======================================

En este capítulo aprenderás cómo iniciar sesión en tu Raspberry Pi. Ya sea que tengas una pantalla conectada o necesites acceder de forma remota, esta sección te guiará para abrir la terminal, la cual usarás en capítulos posteriores para introducir comandos.

.. note::

    Si ya estás familiarizado con el uso de Raspberry Pi, puedes saltarte este capítulo.

Iniciar sesión con una pantalla
----------------------------------

Tener una pantalla conectada a tu Raspberry Pi facilita la interacción directa con el sistema.

**Componentes necesarios**

* Pironman 5 MAX  
* Adaptador de corriente  
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado  
* Adaptador de corriente del monitor  
* Cable HDMI  
* Monitor  
* Ratón  
* Teclado  

**Pasos**

#. Inserta la tarjeta Micro SD en el Pironman 5 MAX.

#. Conecta el ratón y el teclado a los puertos USB del Pironman 5 MAX.

#. Utiliza el cable HDMI para conectar el monitor al puerto HDMI del Pironman 5 MAX. Asegúrate de que el monitor esté encendido y conectado a una fuente de alimentación.

#. Enciende el Pironman 5 MAX usando el adaptador de corriente. Deberías ver el escritorio de Raspberry Pi OS aparecer en el monitor en breve.

   .. image:: img/bookwarm.png
      :width: 90%


#. Una vez que veas el escritorio, abre la Terminal haciendo clic en el ícono de la terminal o buscándola en el menú, para comenzar a ingresar comandos.

Iniciar sesión remotamente sin pantalla
---------------------------------------

Si no tienes acceso a un monitor, aún puedes usar tu Raspberry Pi iniciando sesión de forma remota.

Para acceder desde la línea de comandos, puedes utilizar SSH para conectarte a la shell Bash de Raspberry Pi, la cual te permite gestionar el dispositivo mediante comandos.

Si prefieres una interfaz gráfica, puedes usar una aplicación de escritorio remoto como VNC Viewer, que ofrece una forma visual de administrar archivos y operaciones a distancia.

**Componentes necesarios**

* Pironman 5 MAX  
* Adaptador de corriente  
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado  

**Pasos**

#. Inserta la tarjeta Micro SD en el Pironman 5 MAX.

#. Conecta el Pironman 5 MAX a una fuente de alimentación usando el adaptador.

#. Para tutoriales detallados sobre cómo configurar el acceso remoto según el sistema operativo de tu ordenador, consulta las siguientes secciones:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


