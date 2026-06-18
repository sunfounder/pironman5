.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _promax_openclaw_5_promax:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw

Permettre à OpenClaw de faire fonctionner le Pironman5 Pro MAX
--------------------------------------------------------------

Pour permettre à OpenClaw de faire fonctionner le Pironman5 Pro MAX, nous devons installer la compétence Pironman5 Pro MAX.

1.  Assurez-vous d'avoir déjà installé le Pironman5 Pro MAX. Sinon, veuillez vous référer à :ref:`install_pironman5_module_promax`.

2.  Exécutez la commande suivante dans le terminal :

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-promax-skill/ ~/.openclaw/skills/pironman5-promax-skill/

3.  Vous pouvez maintenant faire fonctionner le Pironman5 Pro MAX dans ``openclaw tui``. Essayez d'envoyer des commandes dans le TUI, comme essayer d'allumer les LEDs du boîtier, changer leur couleur, ou faire prendre une photo à la caméra. Vous pouvez même lui dire que vous avez un module DHT11 connecté au GPIO17 et lui demander de vous donner la température.

   .. note:: Si OpenClaw ne parvient toujours pas à reconnaître la compétence que vous avez importée, n'hésitez pas à lui rappeler de faire un rsync.

-------------------------------------------------------------

Interaction vocale
----------------------------------------------------

Le boîtier Pro MAX dispose d'un microphone et d'un haut-parleur intégrés, vous pouvez donc utiliser le Pironman5 Pro MAX pour interagir avec OpenClaw par la voix. Pour y parvenir, vous devez installer le package ``sunfounder-voice-assistant``.

Le package ``sunfounder-voice-assistant`` fournit les bibliothèques et outils nécessaires pour faire fonctionner le matériel Pironman 5 Pro MAX.

Exécutez la commande d'installation suivante :

.. code-block:: bash

   sudo apt install portaudio19-dev
   sudo pip install --break git+https://github.com/sunfounder/sunfounder-voice-assistant.git

Vous explorerez ici la synthèse vocale (TTS), la reconnaissance vocale (STT) et les grands modèles de langage (LLMs) pour faire parler, écouter et même discuter avec vous votre Pironman 5 Pro MAX, comme un robot intelligent.

Ensuite, exécutez l'exemple suivant :

.. code-block:: bash

   python3 ~/pironman5/openclaw_voice.py

Redémarrez. Vous pouvez alors utiliser les fonctionnalités vocales du Pironman5 Pro MAX pour interagir avec OpenClaw. Essayez de dire « Hi Amy » pour le réveiller.

---------------------------------------



.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq