.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


Configuración de NextCloudPi
=======================================

NextCloud es una solución de almacenamiento en la nube privada de código abierto, similar a Google Drive o Dropbox.
Se puede utilizar para almacenar archivos, compartir documentos, sincronizar fotos y gestionar calendarios y contactos.
A diferencia de los servicios de nube públicos, NextCloud otorga a los usuarios control total sobre sus datos, lo que la convierte en una solución ideal para particulares y pequeños equipos que valoran la privacidad y la seguridad de los datos.

La serie Pironman5, impulsada por Raspberry Pi, ofrece bajo consumo de energía, tamaño compacto y rendimiento confiable, lo que la convierte en una excelente opción para un servidor en la nube privado doméstico. Combinado con NextCloud, puede funcionar como un sistema NAS económico.

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

4.  Después de que tu Raspberry Pi arranque, abre un navegador web y visita tu dirección de Portainer: ``https://<dirección-ip-de-tu-rpi>:9443`` .

5.  Por defecto, verás una advertencia que indica que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores mostrarán esta advertencia. En este caso, puedes ignorar la advertencia sin riesgo, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

#.  Durante el primer inicio de sesión, deberás establecer una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

#.  Después de registrar la cuenta de administrador, accederás a la interfaz de Portainer. Desde la barra de navegación izquierda, haz clic en **Settings (Configuración) -> General (General)**, encuentra **App Templates (Plantillas de Aplicación)**, e introduce la siguiente URL en el campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

#.  Haz clic en **Save Application Settings (Guardar configuración de la aplicación)**. La configuración tomará unos 10 segundos.

**Instalar NextCloud**

1.  En la barra de navegación izquierda, haz clic en **Home (Inicio) -> local**.

   .. image:: img/home_server_app/ptn_home_local.png

2.  Ve a **Templates (Plantillas) -> Application (Aplicación)**. En la barra de búsqueda en la parte superior derecha, escribe *nextcloud* y haz clic en ella.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

3.  Haz clic en **Deploy the stack (Desplegar la pila)**, y espera a que finalice el despliegue. Esto generalmente toma unos dos minutos.

   .. image:: img/home_server_app/ptn_temp_deploy.png

4.  Una vez terminado, NextCloud estará instalado.

   .. image:: img/home_server_app/ptn_temp_nextcloud_deploy_finish.png

**Usar NextCloud**

1.  Abre tu navegador y visita tu dirección de NextCloud: ``https://<dirección-ip-de-tu-rpi>:32768`` .

.. note::

   De la misma manera, verás una advertencia que indica que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores mostrarán esta advertencia.
   En este caso, puedes ignorar la advertencia sin riesgo, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

2.  Durante el primer inicio de sesión, deberás establecer una contraseña de administrador.

   .. image:: img/home_server_app/nc_admin_install.png

3.  Después del registro, puedes comenzar a usar NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png