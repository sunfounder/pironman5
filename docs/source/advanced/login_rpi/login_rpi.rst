.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _login_rpi:

Iniciar sesión en Raspberry Pi OS
=====================================

En este capítulo, aprenderás cómo iniciar sesión en Raspberry Pi. Ya sea que tengas una pantalla conectada o necesites acceder de forma remota, esta sección te guiará para abrir la terminal, que utilizarás en los capítulos posteriores para introducir comandos.

.. note::

    Si ya estás familiarizado con las operaciones de Raspberry Pi, puedes saltarte este capítulo.

Iniciar sesión con una pantalla
------------------------------------

Tener una pantalla conectada a tu Raspberry Pi facilita la interacción directa con el sistema.

**Componentes necesarios**

* Pironman 5
* Adaptador de corriente
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado
* Adaptador de corriente para el monitor
* Cable HDMI
* Monitor
* Ratón
* Teclado

**Pasos**

#. Inserta la tarjeta Micro SD en el Pironman 5.

#. Conecta el ratón y el teclado a los puertos USB del Pironman 5.

#. Utiliza el cable HDMI para conectar el monitor al puerto HDMI del Pironman 5. Asegúrate de que el monitor esté conectado a una fuente de alimentación y encendido.

#. Enciende el Pironman 5 usando el adaptador de corriente. Deberías ver aparecer el escritorio de Raspberry Pi OS en el monitor en poco tiempo.

   .. image:: img/bookwarm.png
      :width: 90%
      

#. Una vez que el escritorio sea visible, abre la terminal haciendo clic en el ícono de la terminal o buscándola en el menú para comenzar a introducir comandos.

Iniciar sesión de forma remota sin pantalla
--------------------------------------------------

Si no tienes acceso a un monitor, aún puedes usar tu Raspberry Pi iniciando sesión de forma remota.

Para acceder a la línea de comandos, puedes usar SSH para conectarte a la shell Bash de Raspberry Pi, la shell predeterminada de Linux que permite gestionar el dispositivo a través de comandos.

Para aquellos que prefieren una interfaz gráfica, usar una aplicación de escritorio remoto como VNC Viewer ofrece una forma visual de gestionar archivos y operaciones de manera remota.

**Componentes necesarios**

* Pironman 5 
* Adaptador de corriente
* Tarjeta Micro SD o SSD NVMe con Raspberry Pi OS preinstalado

Pasos:

#. Inserta la tarjeta Micro SD en el Pironman 5.

#. Conecta el Pironman 5 a una fuente de alimentación usando el adaptador de corriente.

#. Para tutoriales detallados sobre cómo configurar el acceso remoto según el sistema operativo de tu computadora, consulta las siguientes secciones:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop


