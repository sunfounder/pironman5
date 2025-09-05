.. note:: 

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Rejoignez d'autres passionnés pour approfondir vos connaissances sur Raspberry Pi, Arduino et ESP32.

    **Pourquoi nous rejoindre ?**

    - **Support d’experts** : Obtenez de l’aide pour les problèmes techniques ou après-vente grâce à notre communauté et notre équipe.
    - **Apprendre et partager** : Échangez des astuces et tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus inédits.
    - **Réductions spéciales** : Bénéficiez d’offres exclusives sur nos produits les plus récents.
    - **Promotions et cadeaux festifs** : Participez à des jeux-concours et des offres spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd’hui !

.. _set_up_pironman5_mini:

Configuration sur Raspberry Pi OS/Ubuntu/Kali Linux/Homebridge
======================================================================

Si vous avez installé Raspberry Pi OS, Ubuntu, Kali Linux ou Homebridge sur votre Raspberry Pi, vous devrez configurer le Pironman 5 Mini en ligne de commande. Des tutoriels détaillés sont disponibles ci-dessous :

.. note::

  Avant toute configuration, démarrez et connectez-vous à votre Raspberry Pi. Si vous ne savez pas comment faire, consultez le site officiel de Raspberry Pi : |link_rpi_get_start|.


Configurer l’arrêt pour désactiver l’alimentation GPIO
------------------------------------------------------------
Pour éviter que le ventilateur RGB, alimenté via le port GPIO du Raspberry Pi, ne continue de tourner après l’arrêt du système, il est nécessaire de configurer la désactivation de l’alimentation GPIO.

#. Modifiez manuellement le fichier de configuration ``EEPROM`` avec la commande suivante :

   .. code-block:: shell

     sudo rpi-eeprom-config -e

#. Modifiez la ligne ``POWER_OFF_ON_HALT`` en ``1``. Par exemple :

   .. code-block:: shell

     BOOT_UART=1
     POWER_OFF_ON_HALT=1
     BOOT_ORDER=0xf41

#. Appuyez sur ``Ctrl + X``, ``Y`` puis ``Entrée`` pour enregistrer les modifications.


Téléchargement et installation du module ``pironman5``
-----------------------------------------------------------

#. Pour les systèmes Lite, commencez par installer les outils requis comme ``git``, ``python3``, ``pip3``, ``setuptools``, etc.

   .. code-block:: shell

     sudo apt-get update
     sudo apt-get install git -y
     sudo apt-get install python3 python3-pip python3-setuptools -y

#. Téléchargez ensuite le code depuis GitHub et installez le module ``pironman5`` :

   .. code-block:: shell

      cd ~
      git clone -b 1.2.15 https://github.com/sunfounder/pironman5.git --depth 1
      cd ~/pironman5
      sudo python3 install.py

   Une fois l’installation terminée, redémarrez le système pour activer l’installation. Suivez les instructions affichées à l’écran.

   Au redémarrage, le service ``pironman5.service`` se lancera automatiquement. Voici les principales fonctionnalités activées :

   * Quatre LED RGB WS2812 s’allumeront en bleu avec un effet de respiration.
     
   .. note::

     Le ventilateur RGB ne s’active que lorsque la température atteint 60°C. Pour modifier cette température, consultez : :ref:`cc_control_fan_mini`.

#. Vous pouvez utiliser l’outil ``systemctl`` pour ``start``, ``stop``, ``restart`` ou vérifier le ``status`` de ``pironman5.service``.

   .. code-block:: shell

      sudo systemctl restart pironman5.service

   * ``restart`` : Appliquez les modifications apportées à la configuration du Pironman 5 Mini.
   * ``start/stop`` : Activez ou désactivez le service ``pironman5.service``.
   * ``status`` : Vérifiez le statut du programme ``pironman5`` avec l’outil ``systemctl``.




.. note::

   Vous avez maintenant configuré tous les composants du Pironman 5. La configuration du Pironman 5 est terminée.
   Vous pouvez désormais utiliser le Pironman 5 pour contrôler votre Raspberry Pi et d'autres appareils.
   Pour plus d'informations et pour utiliser cette page web du Pironman 5, veuillez consulter : :ref:`view_control_dashboard_mini`.