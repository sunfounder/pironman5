.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d’autres passionnés pour approfondir vos connaissances et vos projets autour de Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes techniques et après-vente grâce à l’aide de notre équipe et de la communauté.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour faire évoluer vos compétences.
    - **Avant-premières exclusives** : Accédez en avant-première aux annonces et aperçus de nos nouveaux produits.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos nouveautés.
    - **Promotions festives et cadeaux** : Participez à des concours et à des événements promotionnels pendant les fêtes.

    👉 Prêt(e) à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _max_set_up_batocera:

Configuration sous Batocera.linux
=========================================================

Si vous avez installé le système Batocera.linux, vous pouvez vous y connecter à distance via SSH, puis suivre les étapes ci-dessous pour finaliser la configuration.

#. Une fois le système démarré, connectez-vous à distance à Pironman5 en SSH. Sous Windows, ouvrez **Powershell** ; sous Mac OS X ou Linux, ouvrez simplement le **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Le nom d’hôte par défaut du système Batocera est ``batocera``, avec ``root`` comme nom d’utilisateur et ``linux`` comme mot de passe. Connectez-vous donc en tapant ``ssh root@batocera.local`` puis entrez le mot de passe ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Exécutez la commande suivante : ``/etc/init.d/S92switch setup`` pour accéder au menu de configuration.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Utilisez la flèche bas pour aller à la fin du menu, sélectionnez puis activez les services **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Une fois le service pironman5 activé, sélectionnez **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Exécutez la commande ``reboot`` pour redémarrer Pironman5.

   .. code-block:: shell

      reboot

#. Au redémarrage, le service ``pironman5.service`` démarrera automatiquement. Voici les principales configurations appliquées à Pironman 5 MAX :
   
   * L’écran OLED affiche l’utilisation du CPU, de la RAM et du disque, la température du processeur, ainsi que l’adresse IP du Raspberry Pi.
   * Quatre LED RGB WS2812 s’allument en bleu avec un effet respirant (breathing mode).

   .. note::

     Les ventilateurs RGB ne s’activent que si la température atteint 60 °C. Pour des températures d’activation différentes, voir :ref:`max_cc_control_fan`.

Vous pouvez maintenant connecter le Pironman 5 MAX à un écran, des manettes de jeu, un casque audio, etc., et plonger pleinement dans votre univers de gaming.

.. note::

   Vous avez maintenant configuré tous les composants du Pironman 5. La configuration du Pironman 5 est terminée.
   Vous pouvez désormais utiliser le Pironman 5 pour contrôler votre Raspberry Pi et d'autres appareils.
   Pour plus d'informations et pour utiliser cette page web du Pironman 5, veuillez consulter : :ref:`max_view_control_dashboard`.