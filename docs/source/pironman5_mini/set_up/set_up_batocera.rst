.. include:: /index.rst
   :start-after: start_hello_message
   :end-before: end_hello_message


.. _set_up_batocera_mini:

Configuration sur Batocera.linux
=========================================================

Si vous avez installé le système Batocera.linux, vous pouvez vous y connecter à distance via SSH, puis suivre les étapes ci-dessous pour finaliser la configuration.

#. Une fois le système démarré, utilisez SSH pour vous connecter à distance à Pironman5. Sous Windows, ouvrez **Powershell**, et sous macOS ou Linux, ouvrez directement le **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Le nom d’hôte par défaut de Batocera est ``batocera``, avec ``root`` comme nom d’utilisateur et ``linux`` comme mot de passe. Connectez-vous en tapant ``ssh root@batocera.local``, puis entrez le mot de passe ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Exécutez la commande suivante pour accéder à la page de configuration : ``/etc/init.d/S92switch setup``.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Utilisez la touche fléchée vers le bas pour naviguer jusqu’à la fin, sélectionnez et activez les services **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Après avoir activé le service pironman5, sélectionnez **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Exécutez la commande ``reboot`` pour redémarrer Pironman5.

   .. code-block:: shell

      reboot

#. Après le redémarrage, le service ``pironman5.service`` démarrera automatiquement. Voici les principales configurations appliquées au Pironman 5 :

   * Quatre LED RGB WS2812 s’allument en bleu avec un effet de respiration.
   * Les ventilateurs RGB sont configurés par défaut sur le mode **équilibré**. Pour configurer une température différente de déclenchement, consultez :ref:`cc_control_fan_mini`.

Vous pouvez maintenant connecter le Pironman 5 à un écran, des manettes de jeu, un casque audio et bien plus encore pour vous plonger pleinement dans votre univers gaming.

.. note::

   À ce stade, vous avez correctement configuré le Pironman 5 Mini, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`view_control_commands_mini`.
