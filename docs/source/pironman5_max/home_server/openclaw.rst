.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _openclaw_5_max:


.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw
   :end-before: end_using_openclaw


Faire en sorte qu'OpenClaw pilote le Pironman5 MAX
------------------------------------------------------------------

Pour permettre à OpenClaw de piloter le Pironman5 MAX, nous devons installer le skill Pironman5 MAX.

1.  Assurez-vous d'avoir déjà installé le Pironman5 MAX. Si ce n'est pas le cas, veuillez vous référer à :ref:`install_pironman5_module_max`.

2.  Exécutez la commande suivante dans le terminal :

    .. code-block:: bash

       mkdir -p ~/.openclaw/skills && rsync -av --delete ~/pironman5/skill/pironman5-max-skill/ ~/.openclaw/skills/pironman5-max-skill/

3.  Vous pouvez maintenant piloter le Pironman5 MAX dans ``openclaw tui``. Essayez d'envoyer des commandes dans la TUI, par exemple en essayant d'allumer les LED du boîtier, de changer leur couleur, ou de faire prendre une photo par la caméra. Vous pouvez même lui dire que vous avez un module DHT11 connecté au GPIO17 et lui demander de vous donner la température.

   .. note:: Si OpenClaw ne reconnaît toujours pas le skill que vous avez importé, rappelez-lui de faire un rsync.

-------------------------------------------------------------




.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_telegram
   :end-before: end_using_openclaw_telegram

.. include:: /pironman5/home_server/openclaw.rst
   :start-after: start_using_openclaw_faq
   :end-before: end_using_openclaw_faq