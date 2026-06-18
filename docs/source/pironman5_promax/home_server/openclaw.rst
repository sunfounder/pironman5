.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

OpenClaw zur Steuerung des Pironman5 Pro MAX einrichten
----------------------------------------------------------------------------

Damit OpenClaw den Pironman5 Pro MAX steuern kann, müssen wir das Pironman5 Pro MAX-Skill installieren.

1.  Stellen Sie sicher, dass Sie den Pironman5 Pro MAX bereits installiert haben. Falls nicht, lesen Sie bitte :ref:`install_pironman5_module_promax`.

2.  Führen Sie den folgenden Befehl im Terminal aus:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3.  Sie können den Pironman5 Pro MAX jetzt in der ``openclaw tui`` steuern. Versuchen Sie, Befehle in der TUI zu senden, z.B. versuchen Sie, die LED-Leuchten am Gehäuse einzuschalten, ihre Farbe zu ändern oder die Kamera ein Foto machen zu lassen. Sie können sogar mitteilen, dass Sie ein DHT11-Modul an GPIO17 angeschlossen haben und es die Temperatur angeben lassen.

   .. note:: Falls OpenClaw das importierte Skill immer noch nicht erkennt, erinnern Sie es bitte an rsync.

-------------------------------------------------------------

Interaktion per Sprache
----------------------------------------------------

Das Pro MAX-Gehäuse verfügt über ein eingebautes Mikrofon und einen Lautsprecher, sodass Sie den Pironman5 Pro MAX per Sprache mit OpenClaw interagieren lassen können. Um dies zu erreichen, müssen Sie das Paket ``sunfounder-voice-assistant`` installieren.

Das Paket ``sunfounder-voice-assistant`` bietet die notwendigen Bibliotheken und Werkzeuge für den Betrieb der Pironman 5 Pro MAX Hardware.

Führen Sie den folgenden Installationsbefehl aus:

.. code-block:: bash


   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git


Hier erkunden Sie Text-to-Speech (TTS), Speech-to-Text (STT) und große Sprachmodelle (LLMs), um Ihren Pironman 5 Pro MAX zum Sprechen, Zuhören und sogar zum Chatten mit Ihnen wie ein intelligenter Roboter zu bringen.

Führen Sie dann das folgende Beispiel aus:

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Starten Sie neu. Dann können Sie die Sprachfunktionen des Pironman5 Pro MAX nutzen, um mit OpenClaw zu interagieren. Versuchen Sie, "Hallo Amy" zu sagen, um es aufzuwecken.

---------------------------------------



.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq