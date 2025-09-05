.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros apasionados.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.


Configuración de NextCloudPi
=======================================

NextCloud es una solución de almacenamiento en la nube privada de código abierto, similar a Google Drive o Dropbox. Puede utilizarse para almacenar archivos, compartir documentos, sincronizar fotos y gestionar calendarios y contactos.  
A diferencia de los servicios de nube pública, NextCloud brinda a los usuarios control total sobre sus datos, lo que lo hace ideal para personas y pequeños equipos que valoran la privacidad y la seguridad de los datos.

La serie Pironman5 con tecnología Raspberry Pi ofrece bajo consumo de energía, tamaño compacto y un rendimiento confiable, lo que la convierte en una excelente opción para un servidor de nube privada en el hogar. Combinado con NextCloud, puede servir como un sistema NAS rentable.


**Preparación**

* Tarjeta MicroSD (16GB+, Clase 10 recomendada)  
* Sistema oficial de Raspberry Pi Raspberry Pi OS (o Raspberry Pi OS Lite)  
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

   De forma predeterminada, verás una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores web mostrarán una advertencia sobre dichos certificados.  
   En este caso, puedes ignorar la advertencia de forma segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png


4. En el primer inicio de sesión, deberás establecer una contraseña de administrador.

   .. image:: img/home_server_app/ptn_new_admin.png

5. Después de registrar la cuenta de administrador, entrarás en la interfaz de Portainer. Desde la barra de navegación izquierda, haz clic en **Setting -> General**, busca **App Templates** e introduce la siguiente URL en el campo: ``https://raw.githubusercontent.com/novaspirit/pi-hosted/refs/heads/master/template/portainer-v3-arm64.json``

   .. image:: img/home_server_app/ptn_app_url.png

6. Haz clic en **Save Application Settings**. La configuración tardará alrededor de 10 segundos en completarse.


**Instalar NextCloud**

1. Desde la barra de navegación izquierda, haz clic en **Home -> local -> Templates -> Application**. En la barra de búsqueda superior derecha, escribe *nextcloud* y haz clic en él.

   .. image:: img/home_server_app/ptn_temp_nextcloud.png

2. Haz clic en **Deploy the stack** y espera a que se complete la implementación. Normalmente tarda unos dos minutos.

   .. image:: img/home_server_app/ptn_temp_deploy.png

Una vez completado, NextCloud estará instalado.


**Usar NextCloud**

1. Abre tu navegador y visita tu dirección de NextCloud: ``http://<your-rpi-ip-address>:32768`` .

.. note::

   De manera similar, verás una advertencia de que el sitio utiliza un certificado SSL/TLS autofirmado que no ha sido emitido por una Autoridad de Certificación (CA) reconocida. La mayoría de los navegadores web mostrarán una advertencia sobre dichos certificados.  
   En este caso, puedes ignorar la advertencia de forma segura, aceptar el riesgo y continuar.

   .. image:: img/home_server_app/private_save.png

2. En el primer inicio de sesión, deberás establecer una contraseña de administrador.

   .. image:: img/home_server_app/nc_admin_install.png

3. Después del registro, puedes comenzar a usar NextCloud.

   .. image:: img/home_server_app/nc_dashboard.png
