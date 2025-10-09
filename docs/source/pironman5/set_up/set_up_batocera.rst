.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts**: Résolvez les problèmes après-vente et surmontez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager**: Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Avant-premières exclusives**: Accédez en avant-première aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales**: Profitez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours**: Participez à des tirages au sort et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _set_up_batocera:

Configuration de Batocera.linux
=========================================================

Si vous avez installé le système d'exploitation Batocera.linux, vous pouvez vous connecter à distance à ce système via SSH, puis suivre les étapes ci-dessous pour finaliser la configuration.

#. Une fois le système démarré, utilisez SSH pour vous connecter à distance à Pironman5. Sous Windows, vous pouvez ouvrir **Powershell**, tandis que sous Mac OS X et Linux, vous pouvez ouvrir directement le **Terminal**.

   .. image:: img/batocera_powershell.png
      :width: 90%
      

#. Le nom d'hôte par défaut pour le système Batocera est ``batocera``, avec l'utilisateur par défaut ``root`` et le mot de passe ``linux``. Pour vous connecter, tapez ``ssh root@batocera.local`` et entrez le mot de passe ``linux``.

   .. image:: img/batocera_login.png
      :width: 90%

#. Exécutez la commande: ``/etc/init.d/S92switch setup`` pour accéder à la page des paramètres.

   .. image:: img/batocera_configure.png  
      :width: 90%

#. Utilisez la touche flèche vers le bas pour naviguer jusqu'à la fin, puis sélectionnez et activez les services **Pironman5**.

   .. image:: img/batocera_configure_pironman5.png
      :width: 90%

#. Après avoir activé le service pironman5, sélectionnez **OK**.

   .. image:: img/batocera_configure_pironman5_ok.png
      :width: 90%

#. Exécutez la commande ``reboot`` pour redémarrer Pironman5.

   .. code-block:: shell

      reboot

#. Au redémarrage, le service ``pironman5.service`` démarrera automatiquement. Voici les principales configurations pour Pironman 5 :

   * L'écran OLED affiche l'utilisation du CPU, de la RAM, du disque, la température du CPU et l'adresse IP du Raspberry Pi.
   * Quatre LED RGB WS2812 s'allument en bleu avec un mode respiration.
   
   .. note::
    
      Les ventilateurs RGB ne tourneront pas à moins que la température n'atteigne 60°C. Pour des températures d'activation différentes, voir :ref:`cc_control_fan`.


Vous pouvez maintenant connecter le Pironman 5 à un écran, des manettes de jeu, des écouteurs, et bien plus encore, pour vous immerger dans votre univers de jeu.

.. note::

   À ce stade, vous avez correctement configuré le Pironman 5, et il est prêt à être utilisé.

   Pour un contrôle avancé de ses composants, veuillez vous référer à :ref:`control_commands_dashboard_5`.
