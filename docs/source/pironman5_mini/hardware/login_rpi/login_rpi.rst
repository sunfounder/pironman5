.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete aún más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados como tú.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas técnicos y postventa con la ayuda de nuestra comunidad y equipo especializado.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios y adelantos de nuevos productos.
    - **Descuentos especiales**: Disfruta de ofertas exclusivas en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _login_rpi_mini:

Iniciar sesión en Raspberry Pi OS
=====================================

En este capítulo aprenderás cómo iniciar sesión en Raspberry Pi. Ya sea que tengas una pantalla conectada o necesites acceder de forma remota, esta sección te guiará para abrir la terminal, la cual utilizarás en los siguientes capítulos para introducir comandos.

.. note::

    Si ya estás familiarizado con el uso de Raspberry Pi, puedes omitir este capítulo.

Iniciar sesión con pantalla
-------------------------------

Tener una pantalla conectada a tu Raspberry Pi facilita la interacción directa con el sistema.

**Componentes necesarios**

* Pironman 5 Mini  
* Adaptador de corriente  
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado  
* Adaptador de corriente para el monitor  
* Cable HDMI  
* Monitor  
* Ratón  
* Teclado

**Pasos**

#. Inserta la tarjeta Micro SD en el Pironman 5 Mini.

#. Conecta el ratón y el teclado a los puertos USB del Pironman 5 Mini.

#. Usa el cable HDMI para conectar el monitor al puerto HDMI del Pironman 5 Mini. Asegúrate de que el monitor esté conectado a una fuente de energía y encendido.

#. Enciende el Pironman 5 Mini usando el adaptador de corriente. Deberías ver el escritorio de Raspberry Pi OS en el monitor en pocos segundos.

   .. image:: img/bookwarm.png
      :width: 90%


#. Una vez que el escritorio esté visible, abre la Terminal haciendo clic en el ícono correspondiente o buscándola en el menú para comenzar a introducir comandos.

Iniciar sesión de forma remota sin pantalla
----------------------------------------------

Si no tienes acceso a un monitor, aún puedes utilizar tu Raspberry Pi accediendo de forma remota.

Para acceso por línea de comandos, puedes usar SSH para conectarte al shell Bash de Raspberry Pi, el entorno de línea de comandos predeterminado de Linux que te permite administrar el dispositivo mediante comandos.

Si prefieres una interfaz gráfica, puedes usar una aplicación de escritorio remoto como VNC Viewer para gestionar archivos y operaciones visualmente.

**Componentes necesarios**

* Pironman 5 Mini  
* Adaptador de corriente  
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado

Pasos:

#. Inserta la tarjeta Micro SD en el Pironman 5 Mini.

#. Conecta el Pironman 5 Mini a una fuente de energía utilizando el adaptador de corriente.

#. Para obtener tutoriales detallados sobre cómo configurar el acceso remoto según el sistema operativo de tu ordenador, consulta las siguientes secciones:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


