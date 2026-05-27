.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuración de Plex
=======================================

Plex es una potente plataforma de servidor multimedia que te permite organizar, transmitir y acceder a tus películas, series de TV, música y fotos en múltiples dispositivos.
Al configurar Plex en la serie Pironman5 impulsada por Raspberry Pi, puedes crear un centro multimedia doméstico asequible y de bajo consumo energético que funcione las 24 horas del día, los 7 días de la semana.
El tamaño compacto, el bajo consumo de energía y la flexibilidad del Raspberry Pi lo convierten en una excelente opción para alojar Plex, transformando tu Pi en un centro de entretenimiento personal accesible desde tu red doméstica o incluso de forma remota.

**Preparación**

*   Tarjeta MicroSD (16 GB+, se recomienda Clase 10)
*   Sistema oficial Raspberry Pi OS (o Raspberry Pi OS Lite)
*   Conexión de red estable (se recomienda Ethernet cableada)
*   Disco duro externo o memoria USB (para almacenamiento ampliado)

**Instalar Portainer**

Abre la terminal e introduce los siguientes comandos:

1.  Instalar Docker

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_docker.sh | sudo bash

2.  Instalar Portainer

.. code-block:: bash

   curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install_portainer.sh | sudo bash

3.  Reinicia tu Raspberry Pi. (Luego realiza los siguientes pasos **INMEDIATAMENTE**.)

4.  Después de que tu Raspberry Pi arranque, abre un navegador web y visita tu dirección de Portainer: ``http://<dirección-ip-de-tu-rpi>:9443`` .

5.  Por defecto, podrás ver una advertencia que indica que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores mostrarán esta advertencia. En este caso, puedes ignorarla sin riesgo, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

#.  Durante tu primer inicio de sesión, se te pedirá que definas una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

#.  Después de crear la cuenta de administrador, accederás a la interfaz de Portainer. Desde la barra de navegación izquierda, ve a **Settings (Configuración) -> General (General)**, encuentra **App Templates (Plantillas de Aplicación)**, e introduce la siguiente URL en el campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#.  Haz clic en **Save Application Settings (Guardar configuración de la aplicación)**. La configuración tomará unos 10 segundos.

**Instalar Plex**

1.  En la barra de navegación izquierda, haz clic en **Home (Inicio) -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2.  Ve a **Templates (Plantillas) -> Application (Aplicación)**. En la barra de búsqueda en la parte superior derecha, escribe *plex* y haz clic en ella.

   .. image:: img/home_server_app/ptn_temp_plex.png

#.  Establece el modo de red en **host (anfitrión)**.

   .. image:: img/home_server_app/ptn_plex_network_host.png

#.  Despliega **Show advanced options (Mostrar opciones avanzadas)**.

   .. image:: img/home_server_app/ptn_plex_ad_option1.png

#.  En la sección **volume mapping (mapeo de volúmenes)**, configura las rutas de almacenamiento para tus archivos multimedia y otorga a Plex los permisos de lectura/escritura. Las rutas predeterminadas son ``/portainer/TV`` y ``/portainer/Movies``, ambas con acceso de lectura/escritura habilitado.

   .. image:: img/home_server_app/ptn_plex_ad_option2.png

#.  Haz clic en **Deploy (Desplegar)** y espera a que finalice la instalación de Plex.

**Configurar el Servidor Plex**

1.  Abre tu navegador e ingresa: ``http://<tu_ip>:32400/web`` . Ahora deberías ver la interfaz de Plex.

   .. image:: img/home_server_app/plex_visit.png

2.  Ignora la oferta de suscripción premium.

3.  A continuación, verás la pantalla de **Configuración del servidor (Server Setup)**. Puedes marcar *Permitirme acceder a mis medios fuera de mi hogar (Allow me to access my media outside my home)*. Por ahora, se recomienda dejar esta opción desmarcada y configurarla más tarde si es necesario.

   .. image:: img/home_server_app/plex_server_setup1.png

4.  Luego se te pedirá que organices tus medios. Puedes elegir *Omitir (Skip)* y agregar medios más tarde a través de la configuración. Sin embargo, se recomienda agregar directamente las rutas de almacenamiento que configuraste en el mapeo de volúmenes de Portainer para que Plex pueda escanear e importar tus medios automáticamente.

   .. image:: img/home_server_app/plex_server_setup2.png

5.  Selecciona el tipo de tu biblioteca de medios, asigna un nombre a tu biblioteca y elige el idioma.

   .. image:: img/home_server_app/plex_server_setup2_add_lib1.png

6.  Agrega carpetas. Localiza las rutas de almacenamiento de medios que definiste anteriormente y haz clic en **Agregar biblioteca (Add Library)**.

   .. image:: img/home_server_app/plex_server_setup2_add_lib2.png

7.  Haz clic en **Finalizar (Finish)**. Tu servidor Plex en Raspberry Pi ahora está completamente configurado.

   .. image:: img/home_server_app/plex_server_setup3.png

8.  Ahora deberías ver tus archivos multimedia mostrados en la página de inicio del servidor Plex.

   .. image:: img/home_server_app/plex_index.png