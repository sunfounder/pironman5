.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_standard:

.. start_using_openclaw

Usando OpenClaw
========================================

**¿Qué es OpenClaw?**

Piensa en ello como una versión mejorada de ChatGPT. Mientras que los chatbots tradicionales solo pueden hablar (generar texto), OpenClaw puede actuar. Comprende tus instrucciones en lenguaje natural y puede realizar operaciones en tu computadora, como ejecutar comandos, administrar archivos y llamar a varias herramientas.

Aquí tienes algunos escenarios de aplicación fantásticos:

*   **Asistente personal multiuso:** Deja que te ayude a administrar tu agenda, configurar recordatorios y realizar un seguimiento de tareas. Solo tienes que decírselo en una aplicación de chat (como Telegram, WhatsApp) y él lo recordará y ejecutará.
*   **"Pegamento" de automatización:** Puede actuar como un enlace para tus diversos servicios. Por ejemplo, puedes hacer que monitoree un sitio web en busca de cambios de precios. Una vez que se detecte una caída de precio, puede activar automáticamente un flujo de trabajo de automatización de n8n para enviarte una notificación por correo electrónico.
*   **Asistente de desarrollo dedicado:** Haz que te ayude a administrar servidores, ejecutar scripts y revisar registros. Puedes simplemente decir: "Verifica la carga del sistema por mí", y él puede conectarse por SSH a tu servidor, ejecutar el comando y devolver los resultados.
*   **"Compañero de juegos" de hardware:** Este es un caso de uso muy interesante. Puedes hacer que OpenClaw controle el hardware conectado a una Raspberry Pi. Por ejemplo, un desarrollador lo usó para controlar una aspiradora robótica con un brazo mecánico, o incluso para ayudar a analizar datos de un simulador de carreras y mostrarlos en una pantalla LED. ¡El equipo oficial de Raspberry Pi incluso lo usó para construir una cabina de fotos automática para una boda, solo mediante conversación, sin escribir una sola línea de código!

**¿Por qué instalar OpenClaw en una Raspberry Pi?**

Instalarlo en una Raspberry Pi tiene dos ventajas principales:

*   **Aislamiento de seguridad:** OpenClaw requiere permisos elevados del sistema, lo que supone un riesgo en una computadora principal. Usar una Raspberry Pi como dispositivo dedicado es como darle un "entorno aislado"; incluso si algo sale mal, no afectará a tu sistema principal.
*   **Siempre encendido 24/7:** La Raspberry Pi tiene un consumo de energía extremadamente bajo, lo que le permite permanecer encendida todo el tiempo, lista para ejecutar tareas en cualquier momento.

----------------------------------------------------------------

Inicio Rápido de OpenClaw
------------------------------

Si quieres experimentar el poder de OpenClaw lo más rápido posible, usa este método. Instalará automáticamente y lanzará un asistente de configuración interactivo.

1.  Abre la terminal en tu Raspberry Pi y ejecuta el siguiente comando directamente. Este comando descarga el script de instalación del sitio web oficial y lo ejecuta:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Debido a que las nuevas versiones se actualizan rápidamente, es normal que tus pasos de instalación difieran ligeramente.

2.  El script descargará e instalará automáticamente OpenClaw.

    .. image:: /pironman5/home_server/img/openclaw/install_open_claw.png

3.  Luego verás un mensaje de seguridad preguntando si confías en OpenClaw. Una vez que estés seguro de que es seguro y confiable, usa las teclas de flecha para navegar a "Yes" y presiona Enter.

    .. image:: /pironman5/home_server/img/openclaw/security_open_claw.png

4.  Selecciona "Quick Start" y luego presiona Enter.

    .. image:: /pironman5/home_server/img/openclaw/quickstart_open_claw.png

5.  Selecciona tu Modelo (Model) y luego presiona Enter. Aquí usamos OpenAI como ejemplo.

    .. image:: /pironman5/home_server/img/openclaw/model_provider_open_claw.png

6.  Selecciona "OpenAI API Key".

    .. image:: /pironman5/home_server/img/openclaw/api_key_open_claw.png

7.  Pega la clave API ahora.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_open_claw.png

8.  Ve a |link_openai_platform| e inicia sesión. En la página **API keys**, haz clic en **Create new secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create.png

9.  Completa los detalles (Propietario, Nombre, Proyecto y permisos si es necesario), luego haz clic en **Create secret key**.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_create_confirm.png

10. Una vez que se crea la clave, cópiala de inmediato; no podrás volver a verla. Si la pierdes, deberás generar una nueva.

    .. image:: /pironman5/home_server/img/openclaw/llm_openai_copy.png

11. Pega la clave en la configuración de OpenClaw.

    .. image:: /pironman5/home_server/img/openclaw/paste_api_key_enter_open_claw.png

12. Selecciona el Modelo (Model) que deseas usar. En este ejemplo, usaremos **Keep current** (Mantener actual).

    .. image:: /pironman5/home_server/img/openclaw/model_config_open_claw.png

13. A continuación viene la selección del canal (Channel). Los canales se refieren a los servicios de comunicación compatibles con OpenClaw, como Telegram, WhatsApp, Discord y más. Usa la tecla de flecha hacia abajo para seleccionar la opción "Skip for now" (Saltar por ahora) y luego presiona Enter.

    .. image:: /pironman5/home_server/img/openclaw/channel_open_claw.png

14. A continuación, se te pedirá que configures las habilidades (skills) de inmediato. Selecciona "Yes" y presiona Enter.

    .. image:: /pironman5/home_server/img/openclaw/config_skill_open_claw.png

15. Instala las habilidades que necesites. En el siguiente ejemplo, seleccionamos la opción "Skip for now" (presiona la barra espaciadora para seleccionar) y luego presionamos Enter.

    .. image:: /pironman5/home_server/img/openclaw/install_skill_open_claw.png

16. Luego vienen los Hooks (enganches); marcaremos "command-logger" y "session-memory".

    .. image:: /pironman5/home_server/img/openclaw/hooks2_open_claw.png

17. La instalación ya está completa. Puedes iniciar OpenClaw seleccionando "Hatch in TUI" y presionando Enter.

    .. image:: /pironman5/home_server/img/openclaw/hatch_open_claw.png

.. note::

   Puedes iniciar OpenClaw ingresando el siguiente comando:

    .. code-block:: bash

       openclaw tui

   Y puedes presionar ctrl+c dos veces para salir de la interfaz TUI.

-----------------------------------------------------

.. end_using_openclaw

Habilitar OpenClaw para Operar el Pironman5
----------------------------------------------

Para permitir que OpenClaw opere el Pironman5, necesitamos instalar la habilidad (skill) de Pironman5.

1.  Asegúrate de que ya hayas instalado Pironman5. Si no es así, consulta :ref:`install_pironman5_module_5`.

2.  Ejecuta el siguiente comando en la terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-skill/ ~/.openclaw/skills/pironman5-skill/

3.  Ahora puedes operar el Pironman5 en ``openclaw tui``. Intenta enviar comandos en la TUI, como intentar encender las luces LED en la caja, cambiar su color o hacer que la cámara tome una foto. Incluso puedes decirle que tienes un módulo DHT11 conectado al GPIO17 y dejar que te diga la temperatura.

   .. note:: Si OpenClaw aún no puede reconocer la habilidad que importaste, recuérdale que haga rsync.

---------------------------------------

.. start_using_openclaw_telegram

Opera tu Sistema con Telegram
---------------------------------------

**Descripción general**

A través de OpenClaw, puedes usar aplicaciones de mensajería populares para operar tu sistema (aquí usamos Telegram como ejemplo). Incluso puedes dejar que OpenClaw te ayude a completar esta configuración.

Simplemente pregunta en ``openclaw tui``: *"Quiero conectarte a Telegram, ¿qué debo hacer?"*

Él te guiará paso a paso a través del proceso, y puedes seguir sus instrucciones para completar la configuración.

**Requisitos previos**

Antes de comenzar, asegúrate de tener:

*   Una **cuenta de Telegram**
*   Acceso de red a Telegram
*   OpenClaw ejecutándose correctamente (verifica con ``openclaw status``)

**Paso 1: Crear un Bot de Telegram**

1.  **Encuentra a @BotFather en Telegram** (el creador oficial de bots)
2.  **Crea un nuevo bot**: Envía el comando ``/newbot``
3.  **Sigue las instrucciones**:
    *   Dale un nombre a tu bot (ej., ``Mi Asistente OpenClaw``)
    *   Establece un nombre de usuario para tu bot (debe terminar en ``bot``, ej., ``mi_openclaw_bot``)
4.  **Al tener éxito, recibirás un mensaje** que contiene tu **Token del Bot**, similar a:

    .. code-block:: text

       1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

    .. warning:: ¡Protege este token como una contraseña!

**Paso 2: Configurar Telegram en OpenClaw**

En ``openclaw tui``, di directamente:

> *"Quiero conectar mi bot de Telegram a OpenClaw. Aquí está mi Token del Bot: <tu-token-aquí>. Por favor, ayúdame a completar la configuración."*

OpenClaw automáticamente:

*   Instalará las dependencias necesarias (como ``node-telegram-bot-api``)
*   Creará el archivo de configuración de la puerta de enlace (gateway) de Telegram
*   Probará si la conexión es exitosa

**Paso 3: Probar la Conexión**

1.  Encuentra tu bot recién creado en Telegram
2.  Envía el comando ``/start``
3.  El bot debería responder con un código de emparejamiento (pairing code), envía este código a la TUI de OpenClaw (ej., ``Pairing code: ZAN4XI34``)
4.  Espera a que se configure correctamente
5.  Intenta enviar comandos simples como "hola"
6.  Si todo está configurado correctamente, deberías ver la respuesta de tu bot

**Paso 4: ¡Disfruta!**

Después de completar esta configuración, podrás:

*   Controlar tu Raspberry Pi en cualquier momento y lugar a través de Telegram
*   Ejecutar comandos de forma remota y verificar el estado del sistema
*   Controlar dispositivos físicos integrando GPIO (como encender LEDs)
*   Disfrutar de una experiencia interactiva inteligente con tu asistente de IA

**Configuración de Seguridad (¡Crítica!)**

Para evitar que extraños controlen tu sistema, asegúrate de implementar las siguientes medidas de seguridad:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Medida de Seguridad
     - Método de Configuración
     - Descripción
   * - Restringir Usuarios
     - Establece ``allowedUsers`` en la configuración
     - Permitir solo usuarios específicos de Telegram
   * - Establecer Contraseña
     - Agrega ``"password": "tu-contraseña"`` en la configuración
     - Requerir verificación de contraseña antes de los comandos
   * - Restringir Comandos
     - Crear una lista blanca de comandos
     - Permitir solo comandos predefinidos específicos
   * - Registros de Auditoría
     - Habilitar el hook ``command-logger``
     - Registrar todos los comandos ejecutados a través de Telegram

**¡Recuerda: la seguridad es lo primero!** Siempre restringe los usuarios y el alcance de los comandos de manera apropiada. Si encuentras problemas específicos durante la configuración, no dudes en pedir ayuda.

-------------------------------------

.. end_using_openclaw_telegram

.. start_using_openclaw_faq

Solución de Problemas de OpenClaw
-------------------------------------

P. Durante la instalación, obtengo el error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. ¿Qué debo hacer?

   Puedes ignorar esto por ahora, pero podrías encontrar problemas en los siguientes pasos. Por favor, refiérete a ellos uno por uno en ese momento.

P. Cuando ejecuto ``openclaw tui``, obtengo el error ``-bash: openclaw: command not found``. ¿Qué debo hacer?

   Ejecuta el siguiente comando:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Ahora deberías poder iniciar la interfaz TUI con ``openclaw tui``.

P. En ``openclaw tui``, encuentro ``not connected to gateway — message not sent`` o el mensaje ``gateway disconnected: closed``.

   Esto se debe a que tu servicio OpenClaw Gateway no se ha iniciado. Abre otra terminal y ejecuta el siguiente comando para iniciar OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Luego reinicia ``openclaw tui`` y podrás usarlo directamente.

P. Quiero configurar el servicio OpenClaw Gateway para que se ejecute en segundo plano / se inicie automáticamente al arrancar. ¿Cómo lo hago?

   Normalmente, tu servicio OpenClaw Gateway debería iniciarse automáticamente al arrancar. Si no es así, puedes iniciarlo manualmente con el siguiente comando.

   1. Crea el directorio ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user

   2. Crea el archivo ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF

   3. Luego recarga la configuración de systemd:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Inicia el servicio:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   En este punto, reinicia ``openclaw tui`` y podrás usarlo directamente.

   5. Habilítalo para que se inicie al arrancar:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway

P. Mi OpenClaw no puede operar el sistema, ¿qué debo hacer?

   Una instalación nueva de OpenClaw puede no tener permiso para operar tu sistema Raspberry Pi por defecto; solo puede chatear. Necesitamos configurar manualmente los permisos.

   1.  Abre el archivo de configuración de OpenClaw:

       .. code-block:: bash

          nano ~/.openclaw/openclaw.json

   2.  Encuentra la opción ``tools`` y modifique los ``perfiles`` y los ``exec`` de la siguiente manera.

       .. code-block:: json

         "tools": {
            "profile": "coding",
            "exec": {
               "secrity": "full"
         },

   3.  Guarda y sal.

   4.  Ingresa el siguiente comando en la terminal para reiniciar OpenClaw Gateway:

       .. code-block:: bash

          openclaw gateway restart

   Ahora, OpenClaw debería tener permisos de lectura y escritura y ser capaz de operar tu sistema Raspberry Pi.

.. end_using_openclaw_faq