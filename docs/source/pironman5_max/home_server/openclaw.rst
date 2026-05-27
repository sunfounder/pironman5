.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_max:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Habilitar OpenClaw para Operar el Pironman5 Max
-------------------------------------------------

Para permitir que OpenClaw opere el Pironman5 Max, necesitamos instalar la habilidad (skill) de Pironman5 Max.

1.  Asegúrate de que ya hayas instalado Pironman5 Max. Si no es así, consulta :ref:`install_pironman5_module_max`.

2.  Ejecuta el siguiente comando en la terminal:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-max-skill/ ~/.openclaw/skills/pironman5-max-skill/

3.  Ahora puedes operar el Pironman5 Max en ``openclaw tui``. Intenta enviar comandos en la TUI, como intentar encender las luces LED en la caja, cambiar su color o hacer que la cámara tome una foto. Incluso puedes decirle que tienes un módulo DHT11 conectado al GPIO17 y dejar que te diga la temperatura.

   .. note:: Si OpenClaw aún no puede reconocer la habilidad que importaste, recuérdale que haga rsync.

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq