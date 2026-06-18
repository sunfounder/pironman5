.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_mini:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

OpenClaw zur Bedienung des Pironman5 Mini befähigen
----------------------------------------------------

Um OpenClaw zu ermöglichen, den Pironman5 Mini zu bedienen, müssen wir die Pironman5 Mini-Fähigkeit (Skill) installieren.

1.  Stellen Sie sicher, dass Sie Pironman5 Mini bereits installiert haben. Falls nicht, lesen Sie bitte :ref:`install_pironman5_module_mini`.

2.  Führen Sie den folgenden Befehl im Terminal aus:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-mini-skill/ ~/.openclaw/skills/pironman5-mini-skill/

3.  Sie können nun den Pironman5 Mini in ``openclaw tui`` bedienen. Versuchen Sie, Befehle in der TUI zu senden, z.B. versuchen Sie, die LED-Leuchten am Gehäuse einzuschalten, deren Farbe zu ändern oder die Kamera ein Foto machen zu lassen. Sie können ihm sogar sagen, dass Sie ein DHT11-Modul an GPIO17 angeschlossen haben, und es die Temperatur auslesen lassen.

   .. note:: Wenn OpenClaw den importierten Skill immer noch nicht erkennt, erinnern Sie es bitte an rsync.

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq