.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message

.. _promax_openclaw_5_promax:

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Abilitare OpenClaw per Operare il Pironman5 Pro MAX
---------------------------------------------------

Per consentire a OpenClaw di operare il Pironman5 Pro MAX, dobbiamo installare la skill per Pironman5 Pro MAX.

1. Assicurati di aver già installato il Pironman5 Pro MAX. In caso contrario, fare riferimento a :ref:`install_pironman5_module_promax`.

2. Esegui il seguente comando nel terminale:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3. Ora puoi operare il Pironman5 Pro MAX in ``openclaw tui``. Prova a inviare comandi nel TUI, come ad esempio tentare di accendere le luci LED sul case, cambiarne il colore, o far scattare una foto alla fotocamera. Puoi anche dirgli che hai un modulo DHT11 collegato al GPIO17 e fargli dire la temperatura.

   .. note:: Se OpenClaw non è ancora in grado di riconoscere la skill che hai importato, ricordagli di fare rsync.

-------------------------------------------------------------

Interagire con la Voce
----------------------------------------------------

Il case Pro MAX ha un microfono e un altoparlante integrati, quindi puoi utilizzare il Pironman5 Pro MAX per interagire con OpenClaw tramite voce. Per ottenere ciò, devi installare il pacchetto ``sunfounder-voice-assistant``.

Il pacchetto ``sunfounder-voice-assistant`` fornisce le librerie e gli strumenti necessari per operare con l'hardware Pironman 5 Pro MAX.

Esegui il seguente comando di installazione:

.. code-block:: bash

   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git

Qui esplorerai la sintesi vocale (TTS), il riconoscimento vocale (STT) e i modelli linguistici di grandi dimensioni (LLM) per far sì che il tuo Pironman 5 Pro MAX parli, ascolti e possa persino conversare con te come un robot intelligente.

Successivamente, esegui il seguente esempio:

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Riavvia. Quindi puoi utilizzare le funzionalità vocali del Pironman5 Pro MAX per interagire con OpenClaw. Prova a dire "Hi Amy" per svegliarlo.

---------------------------------------

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq