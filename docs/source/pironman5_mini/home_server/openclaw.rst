.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_mini:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Abilitare OpenClaw a Operare il Pironman5
----------------------------------------------

Per consentire a OpenClaw di operare il Pironman5, dobbiamo installare l'abilità (skill) Pironman5.

1.  Assicurati di aver già installato Pironman5. In caso contrario, consulta :ref:`install_pironman5_module_mini`.

2.  Esegui il seguente comando nel terminale:

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-mini-skill/ ~/.openclaw/skills/pironman5-mini-skill/

3.  Ora puoi operare il Pironman5 in ``openclaw tui``. Prova a inviare comandi nella TUI, ad esempio provando ad accendere le luci LED sulla scocca, cambiarne il colore o far scattare una foto alla fotocamera. Puoi anche dirgli che hai un modulo DHT11 collegato al GPIO17 e lasciare che ti dica la temperatura.

   .. note:: Se OpenClaw non riesce ancora a riconoscere l'abilità importata, ricordagli di fare rsync.

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq