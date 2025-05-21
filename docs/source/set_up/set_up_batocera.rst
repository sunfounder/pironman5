.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 ! Plongez au cœur de l’univers Raspberry Pi, Arduino et ESP32 aux côtés d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Obtenez de l’aide pour résoudre les problèmes après-vente et relever les défis techniques grâce à notre équipe et à notre communauté.
    - **Apprendre & Partager** : Échangez astuces et tutoriels pour enrichir vos compétences.
    - **Avant-premières exclusives** : Soyez les premiers à découvrir les nouveaux produits et leurs fonctionnalités.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos nouveautés.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des événements promotionnels spéciaux.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _set_up_batocera:

Configuration de Batocera.linux
=========================================================

Si vous avez installé le système d’exploitation Batocera.linux, vous pouvez vous y connecter à distance via SSH, puis suivre les étapes ci-dessous pour finaliser la configuration.

#. Une fois le système lancé, utilisez SSH pour vous connecter à distance au Pironman 5. Sous Windows, ouvrez **PowerShell**, et sous Mac OS X ou Linux, ouvrez directement le **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%


#. Le nom d’hôte par défaut sous Batocera est ``batocera``, avec l’utilisateur ``root`` et le mot de passe ``linux``. Pour vous connecter, tapez ``ssh root@batocera.local`` et entrez le mot de passe ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Exécutez la commande suivante : ``/etc/init.d/S92switch setup`` pour accéder au menu des paramètres.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Utilisez la touche fléchée vers le bas pour faire défiler le menu jusqu’en bas, puis sélectionnez et activez le service **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Une fois le service activé, sélectionnez **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Exécutez la commande ``reboot`` pour redémarrer le Pironman 5.

   .. code-block:: shell

      reboot

#. Au redémarrage, le service ``pironman5.service`` se lancera automatiquement. Voici les principales fonctionnalités activées :

   * L’écran OLED affiche l’utilisation du CPU, de la RAM, du disque, la température du processeur et l’adresse IP du Raspberry Pi.
   * Quatre LED RGB WS2812 s’allument en bleu avec un effet de respiration.

   .. note::

      Les ventilateurs RGB ne se déclenchent que si la température atteint 60 °C. Pour modifier la température de déclenchement, voir :ref:`cc_control_fan`.


Vous pouvez maintenant connecter votre Pironman 5 à un écran, des manettes de jeu, des écouteurs et bien plus encore, pour plonger pleinement dans votre univers de jeu.

