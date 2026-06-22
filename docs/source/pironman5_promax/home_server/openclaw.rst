.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_openclaw_5_promax:

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Hacer que OpenClaw opere el Pironman5 Pro MAX
-------------------------------------------------

Para permitir que OpenClaw opere el Pironman5 Pro MAX, necesitamos instalar la skill de Pironman5 Pro MAX.

1. Asegúrese de que ya ha instalado el Pironman5 Pro MAX. Si no, consulte :ref:`install_pironman5_module_promax`.

2. Ejecute el siguiente comando en la terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3. Ahora puede operar el Pironman5 Pro MAX en ``openclaw tui``. Intente enviar comandos en el TUI, como intentar encender las luces LED de la carcasa, cambiar su color o hacer que la cámara tome una foto. Incluso puede decirle que tiene un módulo DHT11 conectado a GPIO17 y dejar que le diga la temperatura.

   .. note:: Si OpenClaw aún no puede reconocer la skill que importó, recuérdele que haga rsync.

-------------------------------------------------------------

Interacción por Voz
----------------------------------------------------

La carcasa Pro MAX tiene un micrófono y altavoz integrados, por lo que puede usar el Pironman5 Pro MAX para interactuar con OpenClaw por voz. Para lograr esto, necesita instalar el paquete ``sunfounder-voice-assistant``.

El paquete ``sunfounder-voice-assistant`` proporciona las bibliotecas y herramientas necesarias para operar el hardware del Pironman 5 Pro MAX.

Ejecute el siguiente comando de instalación:

.. code-block:: bash

   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git

Aquí explorará texto a voz (TTS), voz a texto (STT) y modelos de lenguaje de gran tamaño (LLM) para hacer que su Pironman 5 Pro MAX hable, escuche e incluso converse con usted como un robot inteligente.

Luego, ejecute el siguiente ejemplo:

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Reinicie. Luego podrá usar las funciones de voz del Pironman5 Pro MAX para interactuar con OpenClaw. Intente decir "Hi Amy" para activarlo.

---------------------------------------

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq