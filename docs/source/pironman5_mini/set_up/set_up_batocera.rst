.. note:: 

    Bonjour et bienvenue dans la communauté SunFounder des passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Rejoignez d'autres passionnés pour explorer en profondeur l'univers du Raspberry Pi, de l'Arduino et de l'ESP32.

    **Pourquoi nous rejoindre ?**

    - **Assistance d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce au soutien de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives** : Accédez en priorité aux annonces de nouveaux produits et aux aperçus.
    - **Remises spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et cadeaux** : Participez à des concours et à des événements promotionnels lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

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

   .. note::

     Le ventilateur RGB ne se mettra en marche que lorsque la température atteindra 60°C. Pour configurer une température différente de déclenchement, consultez :ref:`cc_control_fan_mini`.

Vous pouvez maintenant connecter le Pironman 5 à un écran, des manettes de jeu, un casque audio et bien plus encore pour vous plonger pleinement dans votre univers gaming.

.. note::

   À ce stade, vous avez correctement configuré le Pironman 5 Mini, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_mini`.
