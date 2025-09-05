.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.



Configuración de Plex
=======================================

Plex es una potente plataforma de servidor multimedia que te permite organizar, transmitir y acceder a tus películas, programas de TV, música y fotos en múltiples dispositivos.  
Al configurar Plex en la serie Pironman5 con tecnología Raspberry Pi, puedes crear un centro multimedia doméstico asequible y de bajo consumo energético que funcione 24/7.  
El tamaño compacto, el bajo consumo de energía y la flexibilidad de la Raspberry Pi la convierten en una excelente opción para alojar Plex, transformando tu Pi en un centro de entretenimiento personal accesible desde tu red doméstica o incluso de forma remota.


**Preparación**

* Tarjeta MicroSD (16GB+, Clase 10 recomendada)  
* Sistema oficial Raspberry Pi OS (o Raspberry Pi OS Lite)  
* Conexión de red estable (se recomienda Ethernet por cable)  
* Disco duro externo o memoria USB (para almacenamiento ampliado)  


**Instalar Portainer**

Abre la terminal e introduce los siguientes comandos:

1. Instalar Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2. Instalar Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3. Abre tu navegador y visita tu dirección de Portainer: ``http://<your-rpi-ip-address>:9443`` .

.. note::

   De forma predeterminada, puede que veas una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores web mostrarán dicha advertencia.  
   En este caso, puedes ignorarla de forma segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png


4. En tu primer inicio de sesión, se te pedirá que establezcas una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Después de crear la cuenta de administrador, entrarás en la interfaz de Portainer. Desde la barra de navegación izquierda, ve a **Setting -> General**, busca **App Templates** e introduce la siguiente URL en el campo:  
   ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Haz clic en **Save Application Settings**. La configuración tardará unos 10 segundos en completarse.


**Instalar Plex**

1. Desde la barra de navegación izquierda, haz clic en **Home -> local -> Templates -> Application**. En la barra de búsqueda superior derecha, escribe *plex* y selecciónalo.

   .. image:: img/home_server_app/ptn_temp_plex.png

2. Configura el modo de red en **host**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

3. Expande **Show advanced options**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

4. En la sección **volume mapping**, configura las rutas de almacenamiento para tus archivos multimedia y otorga a Plex permisos de lectura/escritura.  
   Las rutas predeterminadas son ``/portainer/TV`` y ``/portainer/Movies``, ambas con acceso de lectura/escritura habilitado.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

5. Haz clic en **Deploy** y espera a que Plex termine de instalarse.


**Configurar el Servidor Plex**

1. Abre tu navegador e introduce: ``http://<your_ip>:32400/`` . Ahora deberías ver la interfaz de Plex.

   .. image:: img/home_server_app/plex_visit.png

2. Omite la oferta de suscripción premium.

3. A continuación, verás la pantalla **Server Setup**. Puedes marcar *Allow me to access my media outside my home*.  
   Sin embargo, se recomienda dejarlo sin marcar por ahora y configurarlo más adelante si es necesario.

   .. image:: img/home_server_app/plex_server_setup1.png

4. Luego se te pedirá organizar tu contenido multimedia. Puedes elegir *Skip* y añadir contenido más tarde desde la configuración.  
   No obstante, se recomienda añadir directamente las rutas de almacenamiento que configuraste en el mapeo de volúmenes de Portainer, para que Plex pueda escanear e importar automáticamente tu contenido.

   .. image:: img/home_server_app/plex_server_setup2.png

5. Selecciona el tipo de biblioteca multimedia, asigna un nombre a tu biblioteca y elige el idioma.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6. Añade carpetas. Localiza las rutas de almacenamiento de medios que configuraste anteriormente y haz clic en **Add Library**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7. Haz clic en **Finish**. Tu servidor Plex en Raspberry Pi ya está completamente configurado.

   .. image:: img/home_server_app/plex_server_setup3.png

8. Ahora deberías ver tus archivos multimedia en la página principal del servidor Plex.

   .. image:: img/home_server_app/plex_index.png
